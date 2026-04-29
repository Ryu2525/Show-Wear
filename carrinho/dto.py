from dataclasses import dataclass
from typing import List

@dataclass
class DadosItemCarrinhoAdicionarItem:
    idUsuario: int
    idItem: int
    tipoItem: str
    quantidade: int
    precoUnitario: float

@dataclass
class DadosConsultarCarrinho:
    idUsuario: int

@dataclass
class ItemCarrinho:
    idItem: int
    tipoItem: str
    quantidade: int
    precoUnitario: float

@dataclass
class ResultadoConsultarCarrinho:
    itens: List[ItemCarrinho]
    valorTotal: float

@dataclass
class DadosGerarResumoCarrinho:
    idUsuario: int

@dataclass
class ResultadoGerarResumoCarrinho:
    quantidadeItens: int
    valorTotal: float

@dataclass
class DadosProcessarPagamento:
    idPedido: int
    dadosPagamento: dict   # pode ser JSON com método, número do cartão, etc.

@dataclass
class ResultadoProcessarPagamento:
    pagamentoAprovado: bool
    statusPagamento: str
    comprovante: str | None

from dataclasses import dataclass

@dataclass
class PedidoDTO:
    id: int
    idClientes: int
    status_pagamento: str
    comprovante: str | None
    data_pagamento: str | None
