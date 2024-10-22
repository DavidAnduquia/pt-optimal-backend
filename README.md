# Proyecto CRUD de Productos con FastAPI

Este proyecto es una API backend construida con FastAPI, diseñada para proveer consultas y registros de productos en un CRUD (Create, Read, Update, Delete).

## Estructura del Proyecto

```
controllers
|-- producto_controller.py
database
|-- database.py
decorators
|-- exception_handler.py
models
|-- producto_item.py
|-- response_model.py
services
|-- producto_service.py
dboptical.db
Dockerfile
main.py
requirements.txt
```

#  Modelo de base de datos 
   Sqlite
   ```
   CREATE TABLE "producto" (
      "id"	INTEGER UNIQUE,
      "name"	TEXT NOT NULL,
      "date_created"	TEXT NOT NULL,
      "date_modified"	TEXT,
      "status"	NUMERIC NOT NULL,
      PRIMARY KEY("id" AUTOINCREMENT)
   )
   ```
   Postgresql
   ```
   CREATE TABLE producto (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    date_created VARCHAR NOT NULL,
    date_modified VARCHAR,
    status VARCHAR NOT NULL
   )
   ```
##  Instalación y Configuración local
1. Crear y Activar un Entorno Virtual

   ```
   python -m venv venv
   ```

   ```
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```
2. Instalación de Dependencias

   ```
   pip install -r requirements.txt
   ```
3. Ejecutar el servidor unicorn

   ##### 3.1 Subir en modo normal
   ```
   uvicorn main:app
   ```
   ##### 3.2 Subir el Servidor en Modo Debug para Pruebas
   ```
   uvicorn main:app --reload --log-level debug
   ```

   ###### La aplicación en esta configuracion estará disponible en http://127.0.0.1:8000

##  Instalación y Configuración con Docker
   1. Se crea archivo dockerfile en la raiz del proyecto  y se agrega instrucciones para configurar el contenedor.
      ```
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

      # Expone el puerto en el que correrá la aplicación
      EXPOSE 8000

      # Comando para correr la aplicación usando Uvicorn
      CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

      ```

   2. Construir la Imagen Docker
      ```
      docker build -t pt-optimal-backend 
      ```

   3. Ejecutar el Contenedor Docker
      ```
      docker run -p 8000:8000 pt-optimal-backend 
      ```
      ###### La aplicación estará disponible en http://127.0.0.1:8000

## Rutas Disponibles


   Base de datos: Sqlite

   ```
   GET /getProducto/{id}: Obtiene un producto por ID.

   GET /getProductos: lista todos los productos.

   POST /addProducto/{producto}: Añade un nuevo producto.

   PUT /updateProducto/{producto}: Actualiza un producto.

   DELETE /deleteProducto/{id}: Elimina un producto por id.
   ```