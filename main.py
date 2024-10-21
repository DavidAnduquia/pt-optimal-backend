
from fastapi import FastAPI, HTTPException
from controllers.producto_controller import router as product_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

origins = [
    "http://localhost:3000",
    "http://frontend-app:3000",
    "https://pt-optimal-frontend.onrender.com"
]

# Configura el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Cambia esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Inicializa los routers dinámicos 
app.include_router(product_router)
 
# Mensaje de depuración para verificar que la aplicación está corriendo
@app.get("/")
def read_root():
    return {"message": "FastAPI está corriendo"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)