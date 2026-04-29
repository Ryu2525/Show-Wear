import unittest
from dto import DadosProcessarPagamento
from servicoPagamento import PagamentoService

class TestPagamentoService(unittest.TestCase):
    def setUp(self):
        self.service = PagamentoService()

    def test_pagamento_aprovado(self):
        requisicao = DadosProcessarPagamento(
            idPedido=1,
            dadosPagamento={"metodo": "cartao", "numero": "1234"}
        )
        resultado = self.service.processarPagamento(requisicao)
        self.assertTrue(resultado.pagamentoAprovado)
        self.assertEqual(resultado.statusPagamento, "aprovado")
        self.assertIsNotNone(resultado.comprovante)

    def test_pagamento_recusado(self):
        requisicao = DadosProcessarPagamento(
            idPedido=2,
            dadosPagamento={"metodo": "cartao", "numero": "9999"}
        )
        resultado = self.service.processarPagamento(requisicao)
        self.assertFalse(resultado.pagamentoAprovado)
        self.assertEqual(resultado.statusPagamento, "recusado")
        self.assertIsNone(resultado.comprovante)

if __name__ == "__main__":
    unittest.main()
