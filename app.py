import streamlit as st
from Model.src.Controller import Controller

def iniciarPrograma():
    if 'controlador' not in st.session_state:
        st.session_state.controlador = Controller()

    st.set_page_config(page_title="Inicio", page_icon="🛎😎", layout="wide")
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
                padding: 20px; 
                background-color: #5153AC; 
                color: white;
                } 
                .banner { 
                display: flex; 
                flex-direction: column-wrap;
                justify-content: center; 
                align-items: flex-start; 
                background-color: #5153AC; 
                color: white;
                padding: 20px; 
                } 
                .banner img { 
                    max-width: 100%; 
                    height: auto; 
                } .banner p {
                    margin-bottom: 10px;
                } .buttons {
                    display: flex;
                    align-items: flex-start; 
                    flex-direction: column-wrap;
                    margin: 100px 0;
                    gap: 20px;
                } .content { 
                    display: flex; 
                    justify-content: space-around; 
                    padding: 20px; 
                    background-color: white;
                    color: black;
                } .left, .right { 
                    width: 45%; 
                } .right button { 
                    display: block; 
                    width: 100%; 
                    padding: 10px; 
                    margin: 10px 0; 
                    font-size: 16px; 
                    cursor: pointer; 
                } 
        </style> 
    </head> 
    <body> 
        <div class="header"> 
            <h1>Consultas de interés</h1> 
        </div> 
        <div class="banner"> 
            <img src="https://th.bing.com/th/id/OIP.uNP4CriTp85jXlGydg1EEgHaE8?rs=1&pid=ImgDetMain" alt="Estudiantes en un aula"><p> 
            <div class="banner"> 
                <div>
                    <p>Conozca las instituciones y programas académicos de educación superior autorizados por el Ministerio de Educación Nacional</p>
                    <div class="buttons">
                        <button>Instituciones</button>
                        <button>Programas</button>
                    </div>
                </div>
            </div> 
        </div> 
        <div class="content"> 
            <div class="left"> 
                <h2>Educación</h2> 
                <p>Sabías que...</p> 
                <p>Este sistema provee información detallada sobre las instituciones y programas de educación superior en Colombia.</p> 
            </div> 
            <div class="right"> 
                <button>Obtener Información Personalizada</button> 
                <button>Información Estadística</button> 
                <button>Estadísticas Destacadas</button> 
                <button>Sobre nosotros</button> 
            </div> 
        </div> 
    </body>
    </html>
    """

    st.markdown(html_code, unsafe_allow_html=True)
    st.write('Bienvenido a mi página web interactiva con estilo personalizado.')

if __name__ == "__main__":
    iniciarPrograma()

