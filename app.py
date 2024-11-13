import streamlit as st
import streamlit.components.v1 as components
from Model.src.Controller import Controller


def iniciarPrograma():
    if 'controlador' not in st.session_state:
        st.session_state.controlador = Controller()

    st.set_page_config(page_title="Inicio", page_icon="🛎😎", layout="wide", initial_sidebar_state="collapsed")

    html_code = """
    <!DOCTYPE html> 
    <html lang="es"> 
    <head> 
        <meta charset="UTF-8"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <title>SNIES</title> 
        <style> 
            body { 
                font-family: Arial, sans-serif; 
                } .header { 
                text-align: center; 
                padding: 40px; 
                background-color: #5153AC; 
                color: white;
                } 
                .banner { 
                display: flex; 
                justify-content: flex-start; 
                background-color: #5153AC; 
                color: white;
                padding: 10px; 
                align-items: flex-start;
                } 
                .banner img { 
                    max-width: 55%; 
                    height: auto; 
                } .content { 
                    display: flex; 
                    justify-content: space-around; 
                    padding: 20px; 
                    background-color: #494BA8;
                    color: white;
                } .left, .right { 
                    width: 45%; 
                } .right button { 
                    width: 100%; 
                    padding: 10px; 
                    background-color: #FFFFFF;
                    color: #494BA8;
                    padding: 15px 32px;
                    text-align: center;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 4px;
                } .button {
                    background-color: #FFFFFF;
                    border: none;
                    color: #494BA8;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 4px;
                }

        </style> 
    </head> 
    <body> 
        <div class="header"> 
            <h1>Consultas de interés</h1> 
        </div> 
        <div class="banner"> 
            <img src="https://thumbs.dreamstime.com/z/estudiantes-con-docente-estudiando-en-aula-de-diferentes-edades-sentados-juntos-mesas-estudio-grupal-profesor-270894481.jpg" alt="Estudiantes en un aula"><p> 
            <div class="banner"> 
                <div>
                    <p style="font-size: 25px;">Conozca las instituciones y programas académicos de educación superior autorizados por el Ministerio de Educación Nacional</p>
                    <div class="right">
                        <a href="https://snies.mineducacion.gov.co/portal/" class="button">SNIES portal</a>
                        <a href="https://www.ebc.mx/que-es-un-programa-academico/#:~:text=B%C3%A1sicamente%20es%20un%20plan%20de%20estudios%20detallado%2C%20donde,notar%C3%A1s%20que%20poseen%20un%20modelo%20de%20programa%20acad%C3%A9mico." class="button">Programas</button></a>
                    </div>
                </div>
            </div> 
        </div> 
        <div class="content"> 
            <div class="left"> 
                <h2>Educación</h2> 
                <p style="font-size: 20px;">Sabías que en Colombia, las instituciones de educación superior (IES) se clasifican en tres categorías principales:<br>
                 Instituciones Técnicas Profesionales, Instituciones Tecnológicas y Universidades.<br>
                Cada una ofrece programas de pregrado y posgrado en diversas áreas.</p> 
                <p style="font-size: 20px;">Este sistema provee información detallada sobre las instituciones y programas de educación superior en Colombia.</p> 
                <img src="https://static.misionesonline.news/wp-content/uploads/2020/11/Clases-universitarias-AP-def.jpg" </img>
            </div> 
            <div class="right"> 
                <button>Instituciones</button> 
                <button>Obtener Información Personalizada</button>
                <button>Información Estadística</button> 
                <button>Estadísticas Destacadas</button> 
            </div>
        </div> 
    </body> 
    </html>
    """
    # Incrustar HTML solo si estamos en la página principal
    if "section" not in st.query_params:
        st.markdown(html_code, unsafe_allow_html=True)
    st.write('hola')
if __name__ == "__main__":
    iniciarPrograma()

