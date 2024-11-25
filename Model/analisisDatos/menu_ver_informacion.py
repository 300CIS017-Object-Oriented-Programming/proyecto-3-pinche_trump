import streamlit as st
from st_aggrid import AgGrid
from Model.analisisDatos.gestor_lectura import gestor_lectura as gl

def boton_volver_categoria():
    if st.button("Volver", key="volver2"):
        st.session_state["menu"] = st.session_state["categoria"]

def menu_ver_informacion():
    boton_volver_categoria()
    if "dataframe" in st.session_state and not st.session_state["dataframe"].empty:
        lectura = gl(st.session_state["dataframe"])
        a_mostrar = lectura.obtener_filas_filtro(st.session_state["filtro_columna"], st.session_state["fila_filtro"])
        st.title("Tabla Interactiva")
        AgGrid(a_mostrar, height=800)