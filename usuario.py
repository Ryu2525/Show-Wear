import streamlit as st
from Supabase import criar_usuario, verificar_login

def login_page():
    st.title("Acesso ao Sistema")
    
    aba1, aba2 = st.tabs(["Login", "Cadastro"])
    
    with aba1:
        email_login = st.text_input("Email", key="login_email")
        senha_login = st.text_input("Senha", type="password", key="login_pass")
        
        if st.button("Entrar"):
            sucesso, resultado = verificar_login(email_login, senha_login)
            if sucesso:
                st.success(f"Bem-vindo de volta!")
                st.session_state.logado = True
                st.session_state.user_email = email_login # Salva o email na sessão
                st.rerun()
            else:
                st.error(resultado)

    with aba2:
        novo_email = st.text_input("Novo Email")
        nova_senha = st.text_input("Nova Senha", type="password")
        
        if st.button("Finalizar Cadastro"):
            if novo_email and nova_senha:
                sucesso, mensagem = criar_usuario(novo_email, nova_senha)
                if sucesso:
                    st.success(mensagem)
                    st.balloons()
                else:
                    st.error(mensagem)
            else:
                st.warning("Preencha todos os campos.")

# --- Resto do seu código de navegação ---
def catalog_page():
    # Aqui você pode usar st.session_state.user_email se quiser personalizar
    st.title(f"🛍️ Catálogo para {st.session_state.get('user_email', 'Visitante')}")
    st.info("Aqui entram seus produtos!")

if "logado" not in st.session_state:
    st.session_state.logado = False

login_nav = st.Page(login_page, title="Acesso", icon="🔐")
catalog_nav = st.Page(catalog_page, title="Catálogo", icon="🛍️")

if st.session_state.logado:
    pg = st.navigation([catalog_nav, login_nav])
else:
    pg = st.navigation([login_nav])

pg.run()