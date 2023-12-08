# -*- coding: utf-8 -*-
# gui.py

import streamlit as st
import pandas as pd
#from metodos import guardar_en_csv, borrar
from predecir_modelo import predecir_modelo



def main():
    st.markdown("### Predicción de la resistencia a la compresión del concreto")
    resultado = {}

    try:
        cemento = st.session_state.cemento
        escoria_de_hierro = st.session_state.escoria_de_hierro
        agua = st.session_state.agua
        superplastificador = st.session_state.superplastificador
        agregados_gruesos = st.session_state.agregados_gruesos
        agregados_finos = st.session_state.agregados_finos
        edad = st.session_state.edad
    except AttributeError:
        cemento, escoria_de_hierro, agua, superplastificador, agregados_gruesos, agregados_finos, edad = 0, 0, 0, 0, 0, 0, 0

    with st.form(key='input_form'):
        cemento = st.number_input("Cemento (kg/m³)", min_value=0, step=1, value=cemento)
        escoria_de_hierro = st.number_input("Escoria de Hierro (kg/m³)", min_value=0, step=1, value=escoria_de_hierro)
        agua = st.number_input("Agua (kg/m³)", min_value=0, step=1, value=agua)
        superplastificador = st.number_input("Superplastificador (kg/m³)", min_value=0, step=1, value=superplastificador)
        agregados_gruesos = st.number_input("Agregados Gruesos (kg/m³)", min_value=0, step=1, value=agregados_gruesos)
        agregados_finos = st.number_input("Agregados Finos (kg/m³)", min_value=0, step=1, value=agregados_finos)
        edad = st.number_input("Edad (días)", min_value=0, step=1, value=edad)

        realizar_prediccion = st.form_submit_button('Realizar Predicción')
       
    if realizar_prediccion:
        try:
            resultado = predecir_modelo(
                cemento, escoria_de_hierro, agua,
                superplastificador, agregados_gruesos, agregados_finos, edad
            )

            if isinstance(resultado, dict) and 'resistencia_compresion' in resultado:
                lower_ci = resultado['CI lower']
                upper_ci = resultado['CI upper']
                resistencia_compresion = resultado['resistencia_compresion']

                st.success(f"Resistencia a la compresión: {resistencia_compresion:.2f} MPa")
                st.info(f"Intervalo de Confianza (95%): [Lower CI:  {lower_ci:.2f} MPa, Upper CI:  {upper_ci:.2f}]")
            else:
                st.error("Error en la predicción: Resultado inesperado")
        except ValueError as e:
            st.error(f"Error de conversión: {str(e)}")
        except Exception as e:
            st.error(f"Error en la predicción: {str(e)}")
    
   