#test_app_3.py

import unittest
from unittest.mock import patch, Mock
import pandas as pd
from io import StringIO
import sys
import os  # Importar el módulo os para obtener información del sistema de archivos

class TestImportArchivos(unittest.TestCase):
    def setUp(self):
        # Redirigir la salida estándar a un búfer para capturarla
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Restaurar la salida estándar original después de cada prueba
        sys.stdout = sys.__stdout__

    @patch("pandas.read_csv", return_value=Mock())
    def test_import_archivos(self, mock_read_csv):
        # Imprimir el contenido del directorio actual antes de la importación
        current_directory = os.getcwd()
        print(f"Contenido del directorio actual: {os.listdir(current_directory)}")

        # Ejecutar la importación del archivo
        import archivos

        # Verificar que la función read_csv se llamó con el nombre de archivo esperado
        mock_read_csv.assert_called_once_with("residuals.csv")

        # Verificar que la salida contenga la información esperada
        expected_output = "Archivo 'residuals.csv' importado correctamente."
        actual_output = self.captured_output.getvalue()
        print(f"Actual Output: {actual_output}")  # Agregar esta línea
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
