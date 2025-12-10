import streamlit as st

st.set_page_config(
    page_title="Estimador de Recuperación",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Menú")

st.sidebar.write("Usa el menú de la izquierda para navegar por la aplicación.")

st.title("🏥 Estimador de días de recuperación de lesiones deportivas")

st.write("""
Bienvenido a la aplicación de análisis y predicción de lesiones.
Seleccioná una sección desde el menú lateral para comenzar.
""")

