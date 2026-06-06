# -*- coding: utf-8 -*-
"""
App web - Prediccion de la tecnologia de acceso a Internet Fijo en Colombia
Proyecto Integrador CRISP-DM. Carga el pipeline serializado y predice con datos nuevos.
"""
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Predictor de tecnología de Internet", page_icon="📶")

# --- Cargar el modelo y las opciones (se cachean para no recargar en cada click) ---
@st.cache_resource
def cargar_modelo():
    pipeline = joblib.load("pipeline.pkl")
    opciones = joblib.load("opciones.pkl")
    return pipeline, opciones

pipeline, opciones = cargar_modelo()

# --- Encabezado ---
st.title("📶 Predictor de tecnología de acceso a Internet")
st.write(
    "Esta aplicación predice qué **tecnología de acceso a internet fijo** "
    "(Fibra óptica, Cable, HFC, DSL o Inalámbrica) corresponde a una conexión, "
    "a partir de su región, segmento y velocidades. "
    "Modelo entrenado con datos de **Datos Abiertos Colombia**."
)
st.divider()

# --- Entradas del usuario ---
st.subheader("Datos de la conexión")
col1, col2 = st.columns(2)
with col1:
    departamento = st.selectbox("Departamento", opciones["departamento"])
    velocidad_bajada = st.number_input(
        "Velocidad de bajada (Mbps)", min_value=1.0, max_value=2000.0,
        value=float(opciones["vel_bajada_med"]))
    no_de_accesos = st.number_input(
        "Número de accesos", min_value=1.0, max_value=100000.0,
        value=float(opciones["accesos_med"]))
with col2:
    segmento = st.selectbox("Segmento", opciones["segmento"])
    velocidad_subida = st.number_input(
        "Velocidad de subida (Mbps)", min_value=1.0, max_value=2000.0,
        value=float(opciones["vel_subida_med"]))

# --- Prediccion ---
if st.button("🔮 Predecir tecnología", type="primary"):
    entrada = pd.DataFrame([{
        "departamento": departamento,
        "segmento": segmento,
        "velocidad_bajada": velocidad_bajada,
        "velocidad_subida": velocidad_subida,
        "no_de_accesos": no_de_accesos,
    }])
    prediccion = pipeline.predict(entrada)[0]

    iconos = {"Fibra optica": "🟢", "Cable": "🔵", "HFC": "🟣",
              "DSL": "🟠", "Inalambrica": "📡"}
    st.success(f"### {iconos.get(prediccion, '✅')} Tecnología predicha: **{prediccion}**")
    st.caption(
        "Recuerda: es una predicción estadística basada en patrones históricos, "
        "no un dato oficial de la conexión."
    )

st.divider()
st.caption("Proyecto Integrador — Aprendizaje de Máquinas · Metodología CRISP-DM")
