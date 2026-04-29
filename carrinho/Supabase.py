from supabase import create_client, Client
from dto import *

url: str = "https://frqlowmyzyhacwyxukxw.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZycWxvd215enloYWN3eXh1a3h3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1NjM2NDUsImV4cCI6MjA4ODEzOTY0NX0.fHhePOQoI7teZKNteFwvKj7A51fTsK9vt4FNwHW9suY" # Use a chave que você postou
supabase: Client = create_client(url, key)

def cadastrarUsuario(email, senha):
    try:
        dados = {"email": email, "senha": senha}
        supabase.table("clientes").insert(dados).execute()
        return True, "Usuário cadastrado com sucesso!"
    except Exception as e:
        return False, f"Erro ao cadastrar: {str(e)}"

def  realizarLogin(email, senha):
    try:
        response = supabase.table("clientes").select("*").eq("email", email).eq("senha", senha).execute()
        if len(response.data) > 0:
            return True, response.data[0]
        else:
            return False, "E-mail ou senha incorretos."
    except Exception as e:
        return False, f"Erro na conexão: {str(e)}"

# --- FUNÇÕES PARA O CATÁLOGO ---

def  buscarShowsAtivos():
    try:
        response = supabase.table("show").select("*").execute()
        return response.data
    except Exception as e:
        return []

def buscarVestuarioTematico(show_id):
    try:
        response = supabase.table("vestuarios").select("*").eq("show_id", show_id).execute()
        return response.data
    except Exception as e:
        return []

def buscar_ingressos_por_show(show_id):
    try:
        response = supabase.table("ingressos").select("*").eq("show_id", show_id).execute()
        return response.data
    except Exception as e:
        print(f"Erro: {e}")
        return []

def verificarDisponibilidade(vestuario_id):
    try:
        response = supabase.table("vestuarios").select("status, nome_peca").eq("id", vestuario_id).execute()
        
        if response.data:
            item = response.data[0]
            status = item.get("status", "").lower()
            
            if status == "disponível":
                return True, f"O produto '{item['nome_peca']}' está disponível!"
            else:
                return False, f"O produto '{item['nome_peca']}' não está disponível no momento (Status: {status})."
        else:
            return False, "Produto não encontrado."
            
    except Exception as e:
        return False, f"Erro ao verificar disponibilidade: {str(e)}"
    

def buscarIdUsuarioPorEmail(email: str):
    try:
        response = supabase.table("clientes").select("id").eq("email", email).execute()
        if response.data and len(response.data) > 0:
            return response.data[0]["id"]
        else:
            return None
    except Exception as e:
        print("Erro ao buscar id do usuário:", e)
        return None

# Carrinho

def adicionarItem(requisicao: DadosItemCarrinhoAdicionarItem) -> bool:
    try:
        inserir_item(requisicao.idUsuario, requisicao.idItem, requisicao.tipoItem, requisicao.quantidade, requisicao.precoUnitario)
        return True
    except Exception as e:
        print("Erro:", e)
        return False

def consultarCarrinho(requisicao: DadosConsultarCarrinho) -> ResultadoConsultarCarrinho:
    response = buscar_itens(requisicao.idUsuario)
    itens = []
    total = 0
    for row in response.data:
        preco = row.get("preco_unitario", 0)
        qtd = row.get("quantidade", 0)
        itens.append(ItemCarrinho(row["item_id"], row["tipo_item"], qtd, preco))
        total += preco * qtd
    return ResultadoConsultarCarrinho(itens, total)

def gerarResumoCarrinho(requisicao: DadosGerarResumoCarrinho) -> ResultadoGerarResumoCarrinho:
    resultado = consultarCarrinho(DadosConsultarCarrinho(requisicao.idUsuario))
    qtd_total = sum([i.quantidade for i in resultado.itens])
    return ResultadoGerarResumoCarrinho(qtd_total, resultado.valorTotal)

def limpar_carrinho(idUsuario: int):
    try:
        supabase.table("carrinho").delete().eq("usuario_id", idUsuario).execute()
        return True
    except Exception as e:
        print("Erro ao limpar carrinho:", e)
        return False


def inserir_item(user_id, item_id, tipo_item, quantidade, preco_unitario):
    dados = {
        "user_id": user_id,
        "item_id": item_id,
        "tipo_item": tipo_item,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario
    }
    return supabase.table("cart_items").insert(dados).execute()

def buscar_itens(user_id):
    return supabase.table("cart_items").select("*").eq("user_id", user_id).execute()

def limpar_carrinho(user_id):
    return supabase.table("cart_items").delete().eq("user_id", user_id).execute()

# Pedidos

# --- FUNÇÕES PARA PEDIDOS ---

def criarPedido(idUsuario: int):
    try:
        response = supabase.table("pedido").insert({
            "idclientes": idUsuario,
            "status_pagamento": "pendente"
        }).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print("Erro ao criar pedido:", e)
        return None

def atualizarPedidoPagamento(idPedido: int, status: str, comprovante: str | None):
    try:
        response = supabase.table("pedido").update({
            "status_pagamento": status,
            "comprovante": comprovante,
            "data_pagamento": "now()"
        }).eq("id", idPedido).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print("Erro ao atualizar pedido:", e)
        return None
