#  test_app_2.py

import unittest
from unittest.mock import patch, Mock
import numpy as np
import scipy.stats as stt
import joblib
from io import StringIO
import sys
from predecir_modelo import predecir_modelo

class TestPredictModel(unittest.TestCase):
    def setUp(self):
        # Configurar datos  para las pruebas
        self.cemento = 250
        self.escoria_de_hierro = 0
        self.agua = 180
        self.superplastificador = 0
        self.agregados_gruesos = 1800
        self.agregados_finos = 900
        self.edad = 90

    def test_predict_model(self):
        # Redirigir la salida estándar a un búfer para capturarla
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            # Ejecutar la función que se está probando
            result = predecir_modelo(
                cemento=self.cemento, escoria_de_hierro=self.escoria_de_hierro, agua=self.agua,
                superplastificador=self.superplastificador, agregados_gruesos=self.agregados_gruesos,
                agregados_finos=self.agregados_finos, edad=self.edad
            )
            # Imprimir los valores numéricos específicos
            print(f"Resultado de la predicción: {result['resistencia_compresion']}")
            print(f"Intervalo de Confianza (95%): [Lower CI:  {result['CI lower']}, Upper CI:  {result['CI upper']}]")
        except Exception as e:
            # Capturar cualquier excepción que pueda ocurrir durante la predicción
            print(f"Error en la predicción: {str(e)}")
            print(f"Valor de result: {result}")
        # Restaurar la salida estándar original después de cada prueba
        sys.stdout = sys.__stdout__

        # Verificar que no hay errores en la predicción
        self.assertNotIn("Error", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()

