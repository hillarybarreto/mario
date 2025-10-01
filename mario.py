import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

st.set_page_config(page_title="Mario Quiz", layout="centered")

# --- Función para cargar animaciones Lottie ---
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# --- Título ---
st.title("🎮 Quiz de Mario Bros")
st.markdown("Responde las siguientes 5 preguntas sobre el mundo de **Mario Bros**. ¡Suerte!")

# --- Preguntas ---
preguntas = [
    {
        "pregunta": "¿Cómo se llama el hermano de Mario?",
        "opciones": ["Luigi", "Wario", "Toad", "Yoshi"],
        "respuesta": "Luigi"
    },
    {
        "pregunta": "¿Cuál es el enemigo principal de Mario?",
        "opciones": ["Bowser", "Donkey Kong", "Koopa", "Goomba"],
        "respuesta": "Bowser"
    },
    {
        "pregunta": "¿Qué objeto hace crecer a Mario?",
        "opciones": ["Estrella", "Hongo", "Flor de fuego", "Campana"],
        "respuesta": "Hongo"
    },
    {
        "pregunta": "¿Cuál es el nombre del dinosaurio amigo de Mario?",
        "opciones": ["Yoshi", "Toad", "Boo", "Waluigi"],
        "respuesta": "Yoshi"
    },
    {
        "pregunta": "¿Cómo se llama la princesa que Mario siempre rescata?",
        "opciones": ["Peach", "Daisy", "Zelda", "Rosalina"],
        "respuesta": "Peach"
    }
]

respuestas_usuario = []

with st.form("quiz_form"):
    for i, q in enumerate(preguntas):
        respuesta = st.radio(f"{i+1}. {q['pregunta']}", q["opciones"], key=i)
        respuestas_usuario.append(respuesta)
    submit = st.form_submit_button("Enviar respuestas")

# --- Resultado ---
if submit:
    correctas = 0
    for i, respuesta in enumerate(respuestas_usuario):
        if respuesta == preguntas[i]["respuesta"]:
            correctas += 1

    st.subheader("Resultados")
    st.write(f"Respuestas correctas: {correctas} de {len(preguntas)}")

    if correctas == len(preguntas):
        st.success("¡Felicidades! Has acertado todas las preguntas 🎉")
        animacion = load_lottiefile("assets/happy.json")
    else:
        st.warning("¡Sigue intentando! No acertaste todas las preguntas 😢")
        animacion = load_lottiefile("assets/sad.json")

    st_lottie(animacion, height=400, key="resultado_animacion")
