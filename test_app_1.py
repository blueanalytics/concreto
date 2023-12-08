import unittest
from unittest.mock import patch
import streamlit as st
import sys
from io import StringIO
import gui

class TestApp(unittest.TestCase):
    def setUp(self):
        # Redirigir la salida estándar a un búfer para capturarla
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Restaurar la salida estándar original después de cada prueba
        sys.stdout = sys.__stdout__

    def test_main(self):
        # Simular la interacción del usuario y la realización de la predicción
        with patch("streamlit.number_input", side_effect=[180, 0, 260, 0, 1500, 900, 60, True]):
            with patch("streamlit.form_submit_button", return_value=True):
                gui.main()

        # Verificar que la salida contiene las claves esperadas
        expected_output = {'CI lower', 'CI upper', 'resistencia_compresion'}
        for key in expected_output:
            self.assertIn(key, self.captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
