# Usa una imagen base de Python 3.11
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio /app
COPY requirements.txt /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install openai

# Copia el archivo app.py al directorio /app (si está ubicado en una carpeta diferente)
COPY app.py /app

# Expone el puerto 8080
EXPOSE 8080

# Especifica el comando de inicio para ejecutar la aplicación Python
CMD ["python", "/app/app.py"]
