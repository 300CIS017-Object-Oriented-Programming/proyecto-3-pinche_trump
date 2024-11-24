import streamlit as st
import menus_secundarios_informacion as msi
import menu_descargas as md

def primer_menu():
    st.title("Descarga informacion personalizada con nuestros :red[FILTROS] 🤪")
    try:
        rango = st.slider(
            "Selecciona un rango de años",
            min_value=2020,
            max_value=2023,
            value=(2020,2023)
            )
    except Exception as e:
        st.error(f"Error al seleccionar el rango: {e}")
    
    try:
        categoria_archivo = st.selectbox(
            "Que categoria desea comparar?",
            options=["admitidos", "graduados", "inscritos", "matriculados", "matriculadosPrimeraVez"],
        )
    except Exception as e:
        st.error(f"Error al seleccionar la categoria: {e}")

    if st.button("Listo"):
        st.session_state["rango"] = rango
        st.session_state["categoria"] = categoria_archivo
        st.session_state["menu"] = categoria_archivo

def app():
    if "menu" not in st.session_state:
        st.session_state["menu"] = "primero"

    if st.session_state["menu"] == "primero":
        primer_menu()
    elif st.session_state["menu"] == st.session_state["categoria"]:
        msi.menu_seleccion_filtro()
    elif st.session_state["menu"] == "descargar":
        md.menu_descargas()


app()