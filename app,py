import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮")

st.title("🧮 Resolver Ecuaciones de Primer Grado")

# Generar una ecuación aleatoria de la forma: ax + b = c
def generar_ecuacion():
    a = random.randint(1, 10)
    x = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x  # también devolvemos la solución para validarla

# Usar estado de sesión para mantener la misma ecuación hasta que se resuelva
if 'a' not in st.session_state:
    a, b, c, solucion = generar_ecuacion()
    st.session_state.a = a
    st.session_state.b = b
    st.session_state.c = c
    st.session_state.solucion = solucion
else:
    a = st.session_state.a
    b = st.session_state.b
    c = st.session_state.c
    solucion = st.session_state.solucion

# Mostrar la ecuación
st.write(f"Resuelve la ecuación: `{a}x + {b} = {c}`")

# Entrada del usuario
respuesta = st.text_input("Tu respuesta para x (solo enteros):")

# Verificar que sea entero
def es_entero(valor):
    try:
        int(valor)
        return True
    except:
        return False

# Botón para verificar
if st.button("Verificar"):
    if es_entero(respuesta):
        if int(respuesta) == solucion:
            st.success("✅ ¡Correcto!")
            st.balloons()
            # Nueva ecuación
            a, b, c, solucion = generar_ecuacion()
            st.session_state.a = a
            st.session_state.b = b
            st.session_state.c = c
            st.session_state.solucion = solucion
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
    else:
        st.warning("⚠️ Por favor, ingresa un número entero.")
