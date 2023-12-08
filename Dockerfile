FROM python:3.11.4-slim

WORKDIR /app

# Instalar dependencias
RUN apt-get update && apt-get install -y python3-tk

# Copiar archivos necesarios
COPY requirements.txt .
COPY archivos.py .
COPY predecir_modelo.py .
COPY main.py .
COPY residuals.csv /app
COPY modelo_entrenado.joblib /app
COPY gui.py .
COPY test_app_1.py .
COPY test_app_2.py .
COPY test_app_3.py .


# Instalar requerimientos
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]


