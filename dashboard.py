import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# CONFIGURACIÓN DE THINGSPEAK 
CHANNEL_ID = "3343576" 
READ_API_KEY = "FC37OIGRCFBTMRBH" 

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
params = {
    "api_key": READ_API_KEY,
    "results": 50000
}

# ========== FUNCIÓN PARA OBTENER DATOS ==========
def obtener_datos():
    try:
        respuesta = requests.get(URL, params=params)
        datos = respuesta.json()
        feeds = datos["feeds"]
        df = pd.DataFrame(feeds)
        
        # Conversión de datos
        df["created_at"] = pd.to_datetime(df["created_at"])
        df["field1"] = pd.to_numeric(df["field1"], errors="coerce")
        df["field2"] = pd.to_numeric(df["field2"], errors="coerce")
        
        # Limpieza y ajuste de zona horaria (opcional)
        df = df.dropna(subset=["field1", "field2"])
        return df
    except Exception as e:
        st.error(f"Error al obtener datos: {e}")
        return pd.DataFrame()

# ========== INTERFAZ DE STREAMLIT ==========
st.set_page_config(page_title="Dashboard Taller 9", layout="wide")
st.title(" Monitor de Temperatura y Humedad")
st.markdown("Datos provenientes del sensor DHT11 vía ThingSpeak")

placeholder = st.empty()

while True:
    df = obtener_datos()
    
    with placeholder.container():
        if not df.empty:
            # Últimos valores para las métricas
            ultimo_registro = df.iloc[-1]
            temp_actual = ultimo_registro["field1"]
            hum_actual = ultimo_registro["field2"]
            fecha_actual = ultimo_registro["created_at"].strftime('%H:%M:%S')

            # Métricas principales
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperatura", f"{temp_actual} °C")
            col2.metric("Humedad", f"{hum_actual} %")
            col3.metric("Última actualización", fecha_actual)

            # Gráficas
            st.subheader("Evolución Temporal")
            
            fig_temp = px.line(df, x="created_at", y="field1", title="Temperatura (°C)",
                               labels={"created_at": "Tiempo", "field1": "Temp"},
                               line_shape="spline", render_mode="svg")
            st.plotly_chart(fig_temp, use_container_width=True)

            fig_hum = px.line(df, x="created_at", y="field2", title="Humedad (%)",
                              labels={"created_at": "Tiempo", "field2": "Hum"},
                              color_discrete_sequence=["#CCBE00"], line_shape="spline")
            st.plotly_chart(fig_hum, use_container_width=True)

            # Tabla de registros
            with st.expander("Ver tabla de datos"):
                st.dataframe(df.sort_values(by="created_at", ascending=False))
        else:
            st.warning("No se pudieron cargar datos. Verifique la conexión.")

    time.sleep(15) # Refresco automático cada 15 segundos [cite: 206]
    # streamlit run dashboard.py