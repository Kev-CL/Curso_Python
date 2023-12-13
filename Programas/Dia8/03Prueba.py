#Sirve para verificar que el resultado de nuestro código es lo que esperabamos

import unittest
import Cambiatexto

class ProbarCambiarTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = Cambiatexto.todo_mayusculas(palabra)
        self.assertEqual(resultado,"BUEN DIA")

if __name__ == '__main__':
    unittest.main()
