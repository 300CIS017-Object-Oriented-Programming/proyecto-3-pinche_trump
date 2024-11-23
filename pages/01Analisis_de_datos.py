import streamlit as st

def quienesSomos(controlador):
    st.set_page_config(page_title="Analizar Datos", layout="wide",page_icon="🤫", initial_sidebar_state="collapsed")
    st.title('Análisis de Datos')
    st.markdown(""" 
        <p style="font-size: 25px;">Usa nuestro servicio de análisis de datos </p>
            <p><img src="https://interlat.co/wp-content/uploads/2020/05/59915-2048x1363.jpg"></p>
            """, unsafe_allow_html=True)
    col1, col2= st.columns(2)
    with col1:
        st.subheader('Analizar los datos')
    with col2:
        st.subheader('Filtrar datos')
        tab1, tab2 = st.tabs(["Ver gráficos", "Estadísticas"])

quienesSomos(st.session_state.controlador)
