import streamlit as st
import pandas as pd
from Supabase import (
    buscarShowsAtivos, 
    buscarVestuarioTematico, 
    buscar_ingressos_por_show,
    verificarDisponibilidade,
    buscarIdUsuarioPorEmail,
    adicionarItem
)

from dto import DadosItemCarrinhoAdicionarItem

def show_catalog():
    if 'show_selecionado' not in st.session_state:
        st.session_state.show_selecionado = None
    if 'tela_atual' not in st.session_state:
        st.session_state.tela_atual = "selecao_show"

    if st.session_state.tela_atual == "selecao_show":
        render_selecao_show()
    elif st.session_state.tela_atual == "escolha_categoria":
        render_escolha_categoria()
    elif st.session_state.tela_atual == "detalhes_vestuario":
        render_vestuarios()
    elif st.session_state.tela_atual == "detalhes_ingresso":
        render_ingressos()

# --- TELA 1: SELEÇÃO DO SHOW ---
def render_selecao_show():
    st.title("🎭 Próximos Eventos")
    lista_shows = buscarShowsAtivos()
    
    if not lista_shows:
        st.warning("Nenhum show encontrado no banco de dados.")
        return

    for s in lista_shows:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(s['nome'])
                data_pt = s['data_evento'].split('-')
                data_exibicao = f"{data_pt[2]}/{data_pt[1]}/{data_pt[0]}" if len(data_pt) == 3 else s['data_evento']
                st.write(f"📍 **Local:** {s['local']} | 📅 **Data:** {data_exibicao}")
            with col2:
                if st.button("Explorar Show", key=f"btn_{s['id']}", use_container_width=True):
                    st.session_state.show_selecionado = s
                    st.session_state.tela_atual = "escolha_categoria"
                    st.rerun()

# --- TELA 2: CATEGORIAS ---
def render_escolha_categoria():
    show = st.session_state.show_selecionado
    st.title(f"🔍 Explorando: {show['nome']}")
    
    if st.button("⬅️ Voltar para lista de Shows"):
        st.session_state.tela_atual = "selecao_show"
        st.rerun()

    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 🎟️ Ingressos")
            st.write("Garanta seu lugar no evento.")
            if st.button("Ver Disponibilidade", use_container_width=True):
                st.session_state.tela_atual = "detalhes_ingresso"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("### 👗 Vestuários")
            st.write("Confira o figurino oficial.")
            if st.button("Ver Peças", use_container_width=True):
                st.session_state.tela_atual = "detalhes_vestuario"
                st.rerun()

# --- TELA 3: VESTUÁRIOS ---
def render_vestuarios():
    show = st.session_state.show_selecionado
    st.title(f"👗 Figurinos: {show['nome']}")
    
    if st.button("⬅️ Voltar"):
        st.session_state.tela_atual = "escolha_categoria"
        st.rerun()

    pecas = buscarVestuarioTematico(show['id'])
    
    if pecas:
        for p in pecas:
            disponivel, mensagem = verificarDisponibilidade(p['id'])
            icone = "✅" if disponivel else "❌"
            
            with st.expander(f"{icone} {p['nome_peca']} ({p['categoria']})"):
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.image(p.get('foto_url', "https://via.placeholder.com/200"), use_container_width=True)
                with c2:
                    st.write(f"**Categoria:** {p.get('categoria', 'N/A')}")
                    st.write(f"**Preço:** R$ {p.get('preco', 0.0):.2f}")
                    st.write(f"**Disponíveis:** {p.get('quantidade_disponivel', 0)}")
                    
                    if disponivel:
                        st.success(mensagem)
                        if st.button(f"Reservar {p['nome_peca']}", key=f"res_{p['id']}"):
                            req = DadosItemCarrinhoAdicionarItem(
                                idUsuario=buscarIdUsuarioPorEmail(st.session_state.user_email),
                                idItem=p['id'],
                                tipoItem="vestuario",
                                quantidade=1,
                                precoUnitario=p.get('preco', 0.0)
                            )
                            adicionarItem(req)
                            st.success(f"{p['nome_peca']} adicionado ao carrinho!")
                    else:
                        st.error(mensagem)
                        st.button("Indisponível", disabled=True, key=f"disabled_{p['id']}")
    else:
        st.info("Nenhum vestuário cadastrado para este show.")

# --- TELA 4: INGRESSOS ---
def render_ingressos():
    show = st.session_state.show_selecionado
    st.title(f"🎟️ Ingressos: {show['nome']}")
    
    if st.button("⬅️ Voltar"):
        st.session_state.tela_atual = "escolha_categoria"
        st.rerun()

    ingressos = buscar_ingressos_por_show(show['id'])
    
    if ingressos:
        for ing in ingressos:
            with st.container(border=True):
                c1, c2, c3 = st.columns([2, 1, 1])
                c1.subheader(ing['tipo_setor'])
                c2.write(f"💰 **R$ {ing.get('preco', 0.0):.2f}**")
                
                qtd = ing.get('quantidade_disponivel', 0)
                if qtd > 0:
                    c3.success(f"🔥 {qtd} restantes")
                    if st.button(f"Comprar {ing['tipo_setor']}", key=f"buy_{ing['id']}", use_container_width=True):
                        req = DadosItemCarrinhoAdicionarItem(
                            idUsuario=buscarIdUsuarioPorEmail(st.session_state.user_email),
                            idItem=ing['id'],
                            tipoItem="ingresso",
                            quantidade=1,
                            precoUnitario=ing.get('preco', 0.0)
                        )
                        adicionarItem(req)
                        st.success("Ingresso adicionado ao carrinho!")
                else:
                    c3.error("🚫 Esgotado")
    else:
        st.info("Sem ingressos cadastrados.")
