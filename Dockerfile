# Usamos una imagen base ligera de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Exponemos el puerto 5000 (el mismo que en app.py)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
