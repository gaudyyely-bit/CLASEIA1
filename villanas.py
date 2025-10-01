import streamlit as st

st.set_page_config(page_title="Quiz de Villanas Disney", page_icon="🧙‍♀️", layout="centered")

st.title("🧙‍♀️ Quiz de Villanas Disney")
st.write("Responde correctamente las 5 preguntas para hacer llover 🍕 pizzas.")

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de 'La Sirenita'?",
        "opciones": ["Úrsula", "Maléfica", "Cruella de Vil"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana quiere robarse 101 dálmatas?",
        "opciones": ["Madame Medusa", "Cruella de Vil", "Yzma"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Quién lanza una maldición sobre la Bella Durmiente?",
        "opciones": ["Maléfica", "Gothel", "Lady Tremaine"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Cuál es el nombre de la madrastra de Cenicienta?",
        "opciones": ["Lady Tremaine", "Gothel", "Madame Medusa"],
        "respuesta": "Lady Tremaine"
    },
    {
        "pregunta": "¿Qué villana aparece en 'Enredados'?",
        "opciones": ["Gothel", "Úrsula", "Yzma"],
        "respuesta": "Gothel"
    }
]

respuestas_usuario = []
puntos = 0

with st.form("formulario_quiz"):
    for i, q in enumerate(preguntas):
        respuesta = st.radio(q["pregunta"], q["opciones"], key=f"pregunta_{i}")
        respuestas_usuario.append(respuesta)
    enviar = st.form_submit_button("Enviar respuestas")

if enviar:
    for i, respuesta in enumerate(respuestas_usuario):
        if respuesta == preguntas[i]["respuesta"]:
            puntos += 1

    st.write(f"Has acertado **{puntos} de 5** preguntas.")

    if puntos == 5:
        st.success("🎉 ¡Perfecto! ¡A llover pizzas! 🍕")

        # Animación de pizzas con HTML+CSS
        pizza_lluvia = """
        <style>
        .pizza-container {
            position: relative;
            width: 100%;
            height: 300px;
            overflow: hidden;
        }
        .pizza {
            position: absolute;
            width: 80px;
            animation: caer 4s linear infinite;
        }
        .pizza:nth-child(1) { left: 5%; animation-delay: 0s; }
        .pizza:nth-child(2) { left: 25%; animation-delay: 0.5s; }
        .pizza:nth-child(3) { left: 45%; animation-delay: 1s; }
        .pizza:nth-child(4) { left: 65%; animation-delay: 1.5s; }
        .pizza:nth-child(5) { left: 85%; animation-delay: 2s; }

        @keyframes caer {
            0% { top: -100px; opacity: 1; transform: rotate(0deg); }
            100% { top: 400px; opacity: 0; transform: rotate(360deg); }
        }
        </style>

        <div class="pizza-container">
            <img src="https://i.imgur.com/0umadnY.png" class="pizza">
            <img src="https://i.imgur.com/0umadnY.png" class="pizza">
            <img src="https://i.imgur.com/0umadnY.png" class="pizza">
            <img src="https://i.imgur.com/0umadnY.png" class="pizza">
            <img src="https://i.imgur.com/0umadnY.png" class="pizza">
        </div>
        """
        st.markdown(pizza_lluvia, unsafe_allow_html=True)
    else:
        st.error("😢 ¡Ups! Necesitas acertar las 5 para que lluevan pizzas.")
