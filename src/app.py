import streamlit as st
import streamlit_option_menu as option_menu
from dotenv import load_dotenv
import os

# Carregar variaveis de ambiente do arquivo .env
load_dotenv()

with st.sidebar:
    
    options = ["OCR", "Descrever Imagem", "Extrair Chaves e Valores", "Personalizado"]
    selection = st.segmented_control(
        "Selecionar o que deseja fazer com a imagem", options, selection_mode="single"
    )
    st.markdown(f"Your selected options: {selection}.")