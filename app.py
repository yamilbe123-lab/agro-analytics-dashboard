import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(
    page_title="AgroAnalytics Dashboard",
    page_icon="🌱",
    layout="wide"
)

API_BASE_URL = "http://localhost:8080/api/v1/telemetry"

st.title("🌱 AgroAnalytics - Panel de Telemetría")
st.markdown("Visualización y registro de datos agroclimáticos.")

st.sidebar.header("📡 Estación de Monitoreo")
station_id = st.sidebar.text_input("ID de la Estación", value="ESTACION-01")

st.sidebar.subheader("➕ Registrar Nueva Lectura")
temp_input = st.sidebar.number_input("Temperatura (°C)", min_value=-10.0, max_value=60.0, value=24.5, step=0.1)
hum_input = st.sidebar.slider("Humedad Relativa (%)", min_value=0.0, max_value=100.0, value=65.0, step=0.5)
soil_input = st.sidebar.slider("Humedad del Suelo (%)", min_value=0.0, max_value=100.0, value=42.0, step=0.5)

if st.sidebar.button("Enviar Lectura a la API"):
    payload = {
        "stationId": station_id,
        "temperature": temp_input,
        "humidity": hum_input,
        "soilMoisture": soil_input
    }
    try:
        response = requests.post(API_BASE_URL, json=payload, timeout=3)
        if response.status_code in [200, 201]:
            st.sidebar.success("¡Datos enviados correctamente!")
        else:
            st.sidebar.error(f"Error en API: {response.status_code}")
    except requests.exceptions.RequestException:
        st.sidebar.warning("⚠️ No se pudo conectar con la API (puerto 8080).")

@st.cache_data(ttl=5)
def fetch_telemetry_data(station):
    url = f"{API_BASE_URL}/{station}/recent"
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200 and len(res.json()) > 0:
            return pd.DataFrame(res.json()), False
    except requests.exceptions.RequestException:
        pass
    
    mock_data = [
        {"id": 1, "stationId": station, "temperature": 22.1, "humidity": 58.0, "soilMoisture": 40.0, "timestamp": "2026-10-28T18:00:00Z"},
        {"id": 2, "stationId": station, "temperature": 23.5, "humidity": 60.0, "soilMoisture": 41.5, "timestamp": "2026-10-28T19:00:00Z"},
        {"id": 3, "stationId": station, "temperature": 25.0, "humidity": 64.0, "soilMoisture": 43.0, "timestamp": "2026-10-28T20:00:00Z"},
        {"id": 4, "stationId": station, "temperature": 24.2, "humidity": 62.5, "soilMoisture": 42.2, "timestamp": "2026-10-28T21:00:00Z"}
    ]
    return pd.DataFrame(mock_data), True

data_df, is_mock = fetch_telemetry_data(station_id)

if is_mock:
    st.info("ℹ️ Mostrando datos de respaldo locales.")

latest_record = data_df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura Actual", f"{latest_record['temperature']} °C")
col2.metric("Humedad Ambiente", f"{latest_record['humidity']} %")
col3.metric("Humedad de Suelo", f"{latest_record['soilMoisture']} %")

st.divider()

st.subheader("📈 Historial de Sensores")
fig = px.line(
    data_df, 
    x="timestamp", 
    y=["temperature", "humidity", "soilMoisture"],
    labels={"value": "Medición", "timestamp": "Tiempo", "variable": "Sensor"},
    title=f"Evolución temporal - {station_id}"
)
st.plotly_chart(fig, use_container_width=True)

with st.expander("Ver tabla de datos completa"):
    st.dataframe(data_df.sort_values(by="id", ascending=False), use_container_width=True)