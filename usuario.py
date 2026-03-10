import streamlit as st
from Supabase import cadastrarUsuario,  realizarLogin
from catalogo import show_catalog 

st.set_page_config(page_title="Sistema Showwear", page_icon="🛍️")

# --- Inicialização do Estado de Sessão ---
if "logado" not in st.session_state:
    st.session_state.logado = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None

# --- Definição das Funções de Página ---

def login_page():
    st.title("🔐 Acesso ao Sistema")
    
    if st.session_state.logado:
        st.success(f"Você está logado como: {st.session_state.user_email}")
        if st.button("Sair da Conta"):
            st.session_state.logado = False
            st.session_state.user_email = None
            st.rerun()
        return

    aba1, aba2 = st.tabs(["Login", "Cadastro"])
    
    with aba1:
        email_login = st.text_input("Email", key="login_email")
        senha_login = st.text_input("Senha", type="password", key="login_pass")
        
        if st.button("Entrar"):
            sucesso, resultado =  realizarLogin(email_login, senha_login)
            if sucesso:
                st.session_state.logado = True
                st.session_state.user_email = email_login 
                st.rerun()
            else:
                st.error(resultado)

    with aba2:
        novo_email = st.text_input("Novo Email", key="cad_email")
        nova_senha = st.text_input("Nova Senha", type="password", key="cad_pass")
        
        if st.button("Finalizar Cadastro"):
            if novo_email and nova_senha:
                sucesso, mensagem = cadastrarUsuario(novo_email, nova_senha)
                if sucesso:
                    st.success(mensagem)
                    st.balloons()
                else:
                    st.error(mensagem)
            else:
                st.warning("Preencha todos os campos.")

def catalog_page():
    if not st.session_state.logado:
        st.warning("Por favor, faça login para acessar o catálogo.")
        login_page()
        return

    st.title("🛍️ Catálogo Showwear")
    st.write(f"Bem-vindo, **{st.session_state.user_email}**!")
    show_catalog()


login_nav = st.Page(login_page, title="Minha Conta", icon="🔐")
catalog_nav = st.Page(catalog_page, title="Catálogo de Produtos", icon="🛍️")

if st.session_state.logado:
    pg = st.navigation([catalog_nav, login_nav])
else:
    pg = st.navigation([login_nav])

# Executa a navegação selecionada
pg.run()