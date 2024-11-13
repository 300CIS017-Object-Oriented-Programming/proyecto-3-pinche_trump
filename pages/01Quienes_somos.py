import streamlit as st

def quienesSomos(controlador):
    st.set_page_config(page_title="Quienes Somos", layout="wide",page_icon="🤫", initial_sidebar_state="collapsed")
    st.title('¿QUIENES SOMOS?')
    st.markdown(""" 
        <p style="font-size: 25px;">Somos un grupo de desarrolladores que ofrecemos una applicación web
            que permite el análisis de datos del SNIES</p>""", unsafe_allow_html=True)

quienesSomos(st.session_state.controlador)
