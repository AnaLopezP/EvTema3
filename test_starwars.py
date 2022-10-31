import unittest
from ejercicio3 import *

class Test_Starwars(unittest.TestCase):
    def test_ordenar_lista(self):
        self.assertEqual(ordenar_pasajeros(toda_info, 3), list_ordenada)
        self.assertEqual(ordenar_pasajeros(toda_info, 1), list_ordenada_tamaño)

    def test_at(self):
        self.assertEqual(at(lista, si_at), si_at)

if __name__ == '__main__':
    unittest.main()
