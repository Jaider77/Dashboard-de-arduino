# Dashboard de Temperatura y Humedad

Este proyecto contiene un dashboard construido con Streamlit que muestra datos de temperatura y humedad recolectados por un sensor DHT11 y enviados a ThingSpeak.

## Archivos principales

- `dashboard.py`: aplicación principal de Streamlit.

## Funcionalidad

- Obtiene datos de un canal de ThingSpeak utilizando la API de lectura.
- Muestra los valores actuales de temperatura y humedad.
- Grafica la evolución temporal de ambas variables.
- Presenta una tabla con los registros cargados.
- Actualiza los datos automáticamente cada 15 segundos.

## Requisitos

- Python 3.8+ (recomendado)
- `streamlit`
- `requests`
- `pandas`
- `plotly`

## Instalación

1. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
```

2. Activa el entorno virtual:

- Windows PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Windows CMD:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

3. Instala las dependencias:

```bash
pip install streamlit requests pandas plotly
```

## Ejecución

Ejecuta el dashboard con Streamlit:

```bash
streamlit run dashboard.py
```

Después de ejecutar el comando, se abrirá una ventana del navegador con la interfaz del dashboard.

## Configuración

El archivo `dashboard.py` usa los siguientes valores por defecto:

- `CHANNEL_ID`: `3343576`
- `READ_API_KEY`: `FC37OIGRCFBTMRBH`

Si deseas usar otro canal de ThingSpeak, reemplaza estos valores por los correspondientes a tu cuenta.

## Notas

- La aplicación realiza un refresco automático cada 15 segundos.
- Si no se pueden cargar datos, muestra una advertencia para verificar la conexión.
