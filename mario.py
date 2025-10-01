import streamlit as st
from streamlit_lottie import st_lottie
import json


# ------------------------
# Configuración inicial
# ------------------------
st.set_page_config(page_title="Mario Bros Quiz", layout="centered")
st.title("🎮 Mario Bros Quiz")
st.write("Responde las siguientes preguntas. ¡Debes acertarlas todas para ganar!")

# ------------------------
# Cargar animaciones Lottie
# ------------------------

def cargar_animacion(ruta: str):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Cargar animaciones locales (asegúrate de tener estos archivos en /assets/)
animacion_feliz = cargar_animacion("assets/happy.json")
animacion_triste = cargar_animacion("assets/sad.json")

# ------------------------
# Preguntas del quiz
# ------------------------

preguntas = [
    {
        "pregunta": "¿Cómo se llama el hermano de Mario?",
        "opciones": ["Luigi", "Wario", "Toad", "Yoshi"],
        "respuesta": "Luigi"
    },
    {
        "pregunta": "¿Cuál es el enemigo principal de Mario?",
        "opciones": ["Bowser", "]()
