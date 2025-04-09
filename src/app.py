import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
from use_case.analyze_image import AnalyzeImageUseCase
import os
from io import BytesIO

# Load environment variables
load_dotenv()

st.markdown("<h1 style='text-align: center; color: white;'>Visão Computacional com Modelo OpenAI</h1>", unsafe_allow_html=True)

with st.sidebar:

    # Select LLM
    options=["gpt-4o", "gpt-4o-mini"]
    model = st.pills("Modelos de LLM", options, selection_mode="single")
    
    # Select function
    options = ["OCR", "Descrever Imagem", "Extrair Chaves e Valores", "Personalizado"]
    selection = st.segmented_control(
        "Selecionar o que deseja fazer com a imagem", options, selection_mode="single"
    )

    # Upload image
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

    if uploaded_file is not None:
        # read image file as bytes
        image_bytes = uploaded_file.getvalue()
        st.success(f"Imagem pronta para ser analisada")
    
    if selection == "Personalizado":
        st.success("Você pode descrever o que deseja analisar na imagem")

    start = st.button("iniciar análise", key="start_analysis")

    # Validation messages
    if start:
        if not model:
            st.error("Por favor, selecione um modelo de LLM")
        if not selection:
            st.error("Por favor, selecione uma função para analisar a imagem")
        if not uploaded_file:
            st.error("Por favor, faça upload de uma imagem")

if selection == "OCR" and uploaded_file is not None and start==True and model:

    st.markdown("<h2 style='text-align: center; color: white;'>Imagem a ser analisada:</h2>", unsafe_allow_html=True)
    st.image(image_bytes, caption="Imagem carregada", width=500)

    with st.spinner("Analisando imagem..."):   
        # analyze imge
        analyze = AnalyzeImageUseCase.analyze_image(image_input=image_bytes, prompt="src/prompts/ocr_prompt.txt", model=model)
        st.markdown("<h3 style='text-align: center; color: white;'>Resultado da Análise:</h3>", unsafe_allow_html=True)
        st.code(analyze, language="text")

if selection == "Descrever Imagem" and uploaded_file is not None and start==True and model:

    st.markdown("<h2 style='text-align: center; color: white;'>Imagem a ser analisada:</h2>", unsafe_allow_html=True)
    st.image(image_bytes, caption="Imagem carregada", width=500)

    with st.spinner("Analisando imagem..."):   
        # analyze imge
        analyze = AnalyzeImageUseCase.analyze_image(image_input=image_bytes, prompt="src/prompts/image_description_prompt.txt", model=model)
        st.markdown("<h3 style='text-align: center; color: white;'>Resultado da Análise:</h3>", unsafe_allow_html=True)
        st.code(analyze, language="text")

if selection == "Extrair Chaves e Valores" and uploaded_file is not None and start==True and model:

    st.markdown("<h2 style='text-align: center; color: white;'>Imagem a ser analisada:</h2>", unsafe_allow_html=True)
    st.image(image_bytes, caption="Imagem carregada", width=500)

    with st.spinner("Analisando imagem..."):
        # analyze imge
        analyze = AnalyzeImageUseCase.analyze_image(image_input=image_bytes, prompt="src/prompts/key_value_extraction_prompt.txt", model=model)
        st.markdown("<h3 style='text-align: center; color: white;'>Resultado da Análise:</h3>", unsafe_allow_html=True)
        st.code(analyze, language="text")


if selection == "Personalizado" and uploaded_file is not None and model:
    
    st.markdown("<h2 style='text-align: center; color: white;'>Imagem a ser analisada:</h2>", unsafe_allow_html=True)
    st.image(image_bytes, caption="Imagem carregada", width=500)
    prompt = st.chat_input("Descreva o que precisa ser analisado na imagem")
    
    if prompt:
        with st.spinner("Analisando imagem..."):
            # analyze imge
            analyze = AnalyzeImageUseCase.analyze_image(image_input=image_bytes, prompt=prompt, model=model)
            st.markdown("<h3 style='text-align: center; color: white;'>Resultado da Análise:</h3>", unsafe_allow_html=True)
            st.code(analyze, language="text")
            