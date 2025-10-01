import streamlit as st
from streamlit_lottie import st_lottie
import json

# -------------------------------
# Cargar animación Lottie desde archivo
# -------------------------------
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Cargar animación de lluvia de pizzas
pizza_rain = load_lottie("pizza.json")

# -------------------------------
# Definir las preguntas del quiz
# -------------------------------
questions = [
    {
        "question": "¿Cómo se llama la villana de 'La Sirenita'?",
        "options": ["Úrsula", "Maléfica", "Cruella de Vil"],
        "answer": "Úrsula"
    },
    {
        "question": "¿Qué villana quiere un abrigo de dálmatas?",
        "options": ["Madrastra de Cenicienta", "Cruella de Vil", "Yzma"],
        "answer": "Cruella de Vil"
    },
    {
        "question": "¿Quién secuestra a Rapunzel en 'Enredados'?",
        "options": ["Maléfica", "Madre Gothel", "Úrsula"],
        "answer": "Madre Gothel"
    },
    {
        "question": "¿Quién maldice a Aurora en 'La Bella Durmiente'?",
        "options": ["Maléfica", "Cruella", "La Reina Malvada"],
        "answer": "Maléfica"
    },
    {
        "question": "¿Quién es la villana de 'Blancanieves'?",
        "options": ["Yzma", "La Reina Malvada", "Madrastra de Cenicienta"],
        "answer": "La Reina Malvada"
    }
]

# -------------------------------
# Configuración de la App
# -------------------------------
st.set_page_config(page_title="Quiz Villanas de Disney", page_icon="👸")
st.title("👸 Quiz de Villanas de Disney")
st.markdown("Responde las 5 preguntas correctamente y obtén una *lluvia de pizzas* 🍕✨")

# Variables de control
user_answers = []
score = 0

# -------------------------------
# Formulario de preguntas
# -------------------------------
with st.form("quiz_form"):
    for i, q in enumerate(questions):
        user_choice = st.radio(q["question"], q["options"], key=f"q{i}")
        user_answers.append(user_choice)
    submit = st.form_submit_button("Enviar respuestas")

# -------------------------------
# Comprobar resultados
# -------------------------------
if submit:
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.markdown(f"### ✅ Obtuviste **{score} / {len(questions)}** respuestas correctas.")

    if score == len(questions):
        st.success("¡Perfecto! ¡Lluvia de pizzas para ti! 🍕🎉")
        st_lottie(pizza_rain, height=400, speed=1)
    else:
        st.warning("No acertaste todas... ¡Inténtalo de nuevo para conseguir tus pizzas! 🍕😅")
