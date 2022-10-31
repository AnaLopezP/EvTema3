import unittest
import ejercicio3

class Test_Starwars(unittest.TestCase):
    def ordenar_lista(self):
        self.assertEqual(ejercicio3.ordenar_pasajeros(ejercicio3.lista), ejercicio3.lista_ordenada)

    def at(self):
        self.assertEqual(ejercicio3.at(ejercicio3.lista, ejercicio3.si_at), ejercicio3.si_at)

if __name__ == '__main__':
    unittest.main()
