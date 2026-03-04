# catalog.py
import streamlit as st

def show_catalog():
    st.title("📦 Nosso Catálogo")
    st.write("Aqui estão os produtos disponíveis:")
    
    # Exemplo de grid de produtos
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/150", caption="Produto A")
        st.button("Comprar A")
    with col2:
        st.image("https://via.placeholder.com/150", caption="Produto B")
        st.button("Comprar B")