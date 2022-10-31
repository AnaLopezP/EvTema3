import unittest
from ejercicio2 import *

class Test_MatrizesDet(unittest.TestCase):
    def test_det_iterativo(self):
        self.assertEqual(sarrus_it(matriz), -6)

if __name__ == '__main__':
    unittest.main()