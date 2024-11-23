import streamlit as st
import time
import streamlit.components.v1 as components
from Model.src.Controller import Controller
from Model.utility.Utility import htmlCode, htmlCode2, htmlCode3


def iniciarPrograma():
    if 'controlador' not in st.session_state:
        st.session_state.controlador = Controller()

    st.set_page_config(page_title="Inicio", page_icon="😎", layout="wide", initial_sidebar_state="collapsed")
    horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 30px; border: 40px solid #635985;'><br>"  # thin divider line
    html_code = htmlCode()
    # Incrustar HTML solo si estamos en la página principal
    if "section" not in st.query_params:
        st.markdown(html_code, unsafe_allow_html=True)
    st.write('')
    col1, col2, col3 = st.columns(3)
    with col1 :
        st.title('SNIES')
        html_code2 = htmlCode2()
        st.markdown(html_code2, unsafe_allow_html=True)
    with col2:
        st.title('Importancia del Análisis de Datos')
        html_code3 = htmlCode3()
        st.markdown(html_code3, unsafe_allow_html=True)

    with col3:

        tab1, tab2 = st.tabs(["DATOS DE INTERÉS", "INFORMACIÓN"])
        with tab1:
            st.header("DATOS DE INTERÉS")
            st.write("Mantente informado con estos datos que podrían interesarte.")

            # Ejemplo de una lista de noticias
            noticias = [ {"titulo": "¿Conoces el SNIES?", "descripcion": "Aprende sobre lo que es y lo que hace el SNIES", "link": "https://www.mineducacion.gov.co/sistemasinfo/InformacionInstitucional/211868:Que-es-el-SNIES", "video": "https://www.youtube.com/watch?v=dFmZbTBSMN4"},
                         {"titulo": "¿No sabes como usar el SNIES?", "descripcion": "Descubre paso a paso como usar el SNIES de manera eficiente", "link": "https://snies.mineducacion.gov.co/portal/EL-SNIES/Como-funciona/", "video": "https://www.youtube.com/watch?v=KcgosNzbGq4"}
            ]

            for noticia in noticias:
                st.subheader(noticia["titulo"])
                st.write(noticia["descripcion"])
                st.markdown(f"[Lee más]({noticia['link']})")
                st.video(noticia["video"])
        with tab2:
            st.header('Conoce más sobre nosotros')
            st.write('Github de las personas implicadas en el desarrollo:')
            linkGit = [{"integrante": "Jorge", "gitHub": "https://github.com/jorluos"},
                       {"integrante": "Alejandro", "gitHub": "https://github.com/Alejandro"},
                       {"integrante": "Mateo", "gitHub": "https://github.com/Mateo"}]
            for integrante in linkGit:
                st.write(integrante["integrante"], ":")
                st.write(integrante["gitHub"])

            st.subheader('Echa un vistazo al Manual Técnico de esta aplicación web')
    st.markdown("<p style='font-size: 50px;'>Deja tus comentarios aquí por favor</p>", unsafe_allow_html=True)
    soplaMonda = st.text_input("")
    soplaMondaButton = st.button('Enviar Comentarios')
    if soplaMonda and soplaMondaButton:
        st.write('Tus comentarios han sido enviados con éxito')
    elif soplaMondaButton:
        st.write('No has escrito ningún comentario')

if __name__ == "__main__":
    iniciarPrograma()

