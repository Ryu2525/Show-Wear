from dto import DadosProcessarPagamento, ResultadoProcessarPagamento
from Supabase import atualizarPedidoPagamento

class PagamentoService:
    def processarPagamento(self, requisicao: DadosProcessarPagamento) -> ResultadoProcessarPagamento:
        dados = requisicao.dadosPagamento

        if dados.get("metodo") == "cartao" and dados.get("numero") == "1234":
            resultado = ResultadoProcessarPagamento(
                pagamentoAprovado=True,
                statusPagamento="aprovado",
                comprovante=f"CONF-{requisicao.idPedido}-XYZ"
            )
        else:
            resultado = ResultadoProcessarPagamento(
                pagamentoAprovado=False,
                statusPagamento="recusado",
                comprovante=None
            )

        # Atualiza pedido no Supabase
        atualizarPedidoPagamento(
            requisicao.idPedido,
            resultado.statusPagamento,
            resultado.comprovante
        )

        return resultado
