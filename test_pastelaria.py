
import unittest

from vendas import registrar_venda, consultar_fiados, vendas
from estoque import ingredientes


class TestPastelariaFacil(unittest.TestCase):

    def setUp(self):
        vendas.clear()

    def test_estoque_baixo(self):
        farinha = ingredientes["Farinha de trigo"]
        self.assertLess(
            farinha["quantidade"],
            farinha["minimo"]
        )

    def test_estoque_adequado(self):
        queijo = ingredientes["Queijo"]
        self.assertGreaterEqual(
            queijo["quantidade"],
            queijo["minimo"]
        )

    def test_registro_fiado(self):
        registrar_venda("Joao Silva", 30.00, "Fiado")
        saldo = consultar_fiados("Joao Silva")
        self.assertEqual(saldo, 30.00)

    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            registrar_venda("Joao Silva", -10, "Fiado")


if __name__ == "__main__":
    unittest.main()
