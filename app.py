import streamlit as st
import time
import streamlit.components.v1 as components
from Model.src.Controller import Controller
from Model.utility.Utility import htmlCode, htmlCode2, htmlCode3, coments


def iniciarPrograma():
    if 'controlador' not in st.session_state:
        st.session_state.controlador = Controller()

    st.set_page_config(page_title="Inicio", page_icon="😎", layout="wide", initial_sidebar_state="collapsed")  # Configuración general de la página

    # Apartado de html de la página principal
    html_code = htmlCode()
    st.markdown(html_code, unsafe_allow_html=True)
    st.write('')

    col1, col2, col3 = st.columns(3)
    with col1 :
        st.title('SNIES')
        html_code2 = htmlCode2()
        st.markdown(html_code2, unsafe_allow_html=True)

        # Apartado de comentarios para mejorar
        comentarios = []
        coments(comentarios)

    with col2:
        st.title('Importancia del Análisis de Datos')
        html_code3 = htmlCode3()
        st.markdown(html_code3, unsafe_allow_html=True)

    with col3:

        tab1, tab2 = st.tabs(["DATOS DE INTERÉS", "INFORMACIÓN"])  # Apartadi de pestañas para inmersión de la página
        with tab1:
            st.header("DATOS DE INTERÉS")
            st.write("Mantente informado con estos datos que podrían interesarte.")

            # Ejemplo de una lista de noticias
            noticias = [ {"titulo": "¿Conoces el SNIES?", "descripcion": "Aprende sobre lo que es y lo que hace el SNIES", "link": "https://www.mineducacion.gov.co/sistemasinfo/InformacionInstitucional/211868:Que-es-el-SNIES", "video": "https://www.youtube.com/watch?v=dFmZbTBSMN4"},
                         {"titulo": "¿No sabes como usar el SNIES?", "descripcion": "Descubre paso a paso como usar el SNIES de manera eficiente", "link": "https://snies.mineducacion.gov.co/portal/EL-SNIES/Como-funciona/", "video": "https://youtu.be/fPWI19h4P38"}
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
                       {"integrante": "Alejandro", "gitHub": "https://github.com/Alejost7"},
                       {"integrante": "Mateo", "gitHub": "https://github.com/Mateo"}]

            for integrante in linkGit:
                st.write(integrante["integrante"], ":")
                st.write(integrante["gitHub"])
            st.markdown('#### Agradecimientos')
            st.video('https://youtu.be/HjhXZufoIeI')
            st.subheader('Echa un vistazo al Manual Técnico de esta aplicación web')
            rutaArchivo = 'https://github.com/300CIS017-Object-Oriented-Programming/proyecto-3-pinche_trump/blob/d99d05bc03edc57dad72305e1c900d89be8dfd09/README.md'
            enlaceHtml = f"""<a href="{rutaArchivo}" target="_blank" style="font-size: 20px; color: #007BFF; text-decoration: none;">Ver manual Técnico</a>"""
            st.markdown(enlaceHtml, unsafe_allow_html=True)

if __name__ == "__main__":
    iniciarPrograma()

