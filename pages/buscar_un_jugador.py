import streamlit as st

st.title("Buscar un jugador")

query = st.text_input("Ingresá nombre o ID del jugador")

if st.button("Buscar"):
    st.info("Acá iría la búsqueda real (después lo hacemos).")
