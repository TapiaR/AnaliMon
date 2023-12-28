# Actualización del código de prueba unitaria con la nueva estructura de directorios
# y la explicación de las librerías y funciones utilizadas.

import os
import unittest
from unittest.mock import patch
import pandas as pd
from biblio_krk.analizador_monedas import AnalizadorMonedas, obtener_pares_disponibles

# os: Librería estándar para interactuar con el sistema operativo, como leer rutas de archivo.
# unittest: Framework de pruebas unitarias que proporciona una forma de organizar y ejecutar pruebas.
# unittest.mock: Proporciona una forma de simular partes de tu sistema durante las pruebas.
# pandas: Librería para manipulación y análisis de datos, especialmente útil para trabajar con tablas.

# Aquí se carga el archivo CSV de prueba que se encuentra en el directorio de tests/data
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'data', 'XZECZEUR.csv')
test_data = pd.read_csv(csv_path)

# Clase de prueba para obtener_pares_disponibles
class TestObtenerParesDisponibles(unittest.TestCase):

    def test_retorno_lista(self):
        # Prueba que la función devuelve una lista.
        pares = obtener_pares_disponibles()
        self.assertIsInstance(pares, list)

    def test_lista_contiene_strings(self):
        # Prueba que cada elemento de la lista es una cadena de caracteres.
        pares = obtener_pares_disponibles()
        for par in pares:
            self.assertIsInstance(par, str)

# Clase de prueba para AnalizadorMonedas
class TestAnalizadorMonedas(unittest.TestCase):

    def setUp(self):
        # Método que se ejecuta antes de cada prueba, estableciendo condiciones iniciales.
        self.analizador = AnalizadorMonedas("XZECZEUR")

    @patch('krk_biblio.analizador_monedas.AnalizadorMonedas.descargar_datos')
    def test_descargar_datos(self, mock_descargar):
        # Simulación de la descarga exitosa de datos con mocking.
        mock_descargar.return_value = test_data
        self.analizador.descargar_datos()
        self.assertIsNotNone(self.analizador.datos)

    def test_calcular_estocastico_sin_datos(self):
        # Prueba que calcular_estocastico lanza una excepción si no hay datos.
        with self.assertRaises(ValueError):
            self.analizador.calcular_estocastico()

    def test_graficar_cotizaciones_sin_datos(self):
        # Prueba que graficar_cotizaciones lanza una excepción si no hay datos.
        with self.assertRaises(ValueError):
            self.analizador.graficar_cotizaciones()

    def test_graficar_estocastico_sin_datos(self):
        # Prueba que graficar_estocastico lanza una excepción si no hay datos.
        with self.assertRaises(ValueError):
            self.analizador.graficar_estocastico()

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
