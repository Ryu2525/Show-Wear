# from dto import *
# from repositorioCarrinho import inserir_item, buscar_itens

# def adicionarItem(requisicao: DadosItemCarrinhoAdicionarItem) -> bool:
#     try:
#         inserir_item(requisicao.idUsuario, requisicao.idItem, requisicao.tipoItem, requisicao.quantidade, requisicao.precoUnitario)
#         return True
#     except Exception as e:
#         print("Erro:", e)
#         return False

# def consultarCarrinho(requisicao: DadosConsultarCarrinho) -> ResultadoConsultarCarrinho:
#     response = buscar_itens(requisicao.idUsuario)
#     itens = []
#     total = 0
#     for row in response.data:
#         preco = row.get("preco_unitario", 0)
#         qtd = row.get("quantidade", 0)
#         itens.append(ItemCarrinho(row["item_id"], row["tipo_item"], qtd, preco))
#         total += preco * qtd
#     return ResultadoConsultarCarrinho(itens, total)

# def gerarResumoCarrinho(requisicao: DadosGerarResumoCarrinho) -> ResultadoGerarResumoCarrinho:
#     resultado = consultarCarrinho(DadosConsultarCarrinho(requisicao.idUsuario))
#     qtd_total = sum([i.quantidade for i in resultado.itens])
#     return ResultadoGerarResumoCarrinho(qtd_total, resultado.valorTotal)
