# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que correrá la aplicación (ajusta según necesites)
EXPOSE 8000
 
# Comando para correr la aplicación usando Uvicorn
#CMD ["uvicorn", "main:app", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]