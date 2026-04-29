import streamlit as st
from Supabase import adicionarItem, consultarCarrinho, gerarResumoCarrinho, buscarIdUsuarioPorEmail, criarPedido, limpar_carrinho
from dto import DadosConsultarCarrinho, DadosGerarResumoCarrinho, DadosProcessarPagamento
from servicoPagamento import PagamentoService

def carrinho_page():
    st.title("🛒 Meu Carrinho")
    user_id = buscarIdUsuarioPorEmail(st.session_state.user_email)

    # Consultar carrinho
    resultado = consultarCarrinho(DadosConsultarCarrinho(user_id))
    if not resultado.itens:
        st.info("Carrinho vazio.")
        return

    for item in resultado.itens:
        st.write(f"{item.tipoItem} - {item.quantidade} x R$ {item.precoUnitario:.2f}")

    st.write(f"**Total:** R$ {resultado.valorTotal:.2f}")

    resumo = gerarResumoCarrinho(DadosGerarResumoCarrinho(user_id))
    st.write(f"**Itens:** {resumo.quantidadeItens}")

    # Botão para limpar carrinho
    if st.button("🗑️ Limpar Carrinho"):
        if limpar_carrinho(user_id):
            st.success("Carrinho limpo com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao limpar carrinho.")

    # Botão para finalizar compra
    if st.button("Finalizar Compra"):
        pedido = criarPedido(user_id)
        if not pedido:
            st.error("Erro ao criar pedido no banco de dados.")
            return

        dados_pagamento = {"metodo": "cartao", "numero": "1234"}  # exemplo fixo
        requisicao = DadosProcessarPagamento(
            idPedido=pedido["id"],
            dadosPagamento=dados_pagamento
        )

        service = PagamentoService()
        resultado = service.processarPagamento(requisicao)

        if resultado.pagamentoAprovado:
            st.success(f"Pagamento aprovado! Comprovante: {resultado.comprovante}")
        else:
            st.error(f"Pagamento recusado. Status: {resultado.statusPagamento}")
