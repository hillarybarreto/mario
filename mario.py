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

# ------------------------
# Formulario de preguntas
# ------------------------

with st.form("formulario_quiz"):
    for idx, pregunta in enumerate(preguntas):
        seleccion = st.radio(
            f"{idx+1}. {pregunta['pregunta']}",
            pregunta["opciones"],
            key=f"pregunta_{idx}"
        )
        respuestas_usuario.append(seleccion)

    enviado = st.form_submit_button("Enviar respuestas")

# ------------------------
# Evaluar resultados
# ------------------------

if enviado:
    aciertos = 0
    for i, respuesta in enumerate(respuestas_usuario):
        if respuesta == preguntas[i]["respuesta"]:
            aciertos += 1

    st.write(f"✅ Respuestas correctas: {aciertos} de {len(preguntas)}")

    if aciertos == len(preguntas):
        st.success("🎉 ¡Felicitaciones! Has acertado todas las preguntas.")
        st_lottie(animacion_feliz, height=400, loop=True)
    else:
        st.error("😢 Fallaste alguna pregunta. Intenta de nuevo.")
        st_lottie(animacion_triste, height=400, loop=True)
