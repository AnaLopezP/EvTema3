import unittest
import ejercicio2

class Test_MatrizesDet(unittest.TestCase):
    def det_iterativo(self):
        self.assertEqual(ejercicio2.sarrus_it(ejercicio2.matriz), -6)

if __name__ == '__main__':
    unittest.main()