from typing import List
from fastapi import HTTPException
import pytz 
from models.producto_item import Producto, ProductoModel
from database.database import SessionLocal
from datetime import datetime
from decorators.exception_handler import service_exception_handler
 
class ProductoService:

    colombia_timezone = pytz.timezone("America/Bogota")

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_productos(self) -> List[Producto]:
        return self.db.query(Producto).all()
 
    @service_exception_handler
    def get_producto(self, item_id: int):
        # Valida campo nulo o menor de 0
        if item_id is None or item_id <= 0:
            raise HTTPException(status_code=400, detail="El ID debe ser mayor que 0.")
        producto = self.db.query(Producto).filter(Producto.id == item_id).first()
        if not producto:
            raise HTTPException(status_code=200, detail="Producto no encontrado.")
        producto = ProductoModel.model_validate(producto) 
        return producto
         
    @service_exception_handler
    def create_item(self, producto: ProductoModel):
        # Valida campo vacio
        if not producto.name.strip():
            raise HTTPException(status_code=404, detail="El nombre no puede estar vació.")
        producto.date_created = str(datetime.now(self.colombia_timezone).strftime("%d/%m/%Y %H:%M:%S"))
        producto.status = "A" # Asignacion de campo
        new_producto = Producto(**producto.model_dump())
        self.db.add(new_producto)
        self.db.commit()
        self.db.refresh(new_producto)
        return new_producto  
    
    @service_exception_handler
    def update_item(self, usuario_param: ProductoModel):
        producto = self.db.query(Producto).filter(Producto.id == usuario_param.id)
        data = producto.first()
        if data:
            update_data = usuario_param.model_dump()
            del update_data['id']  # Para evitar editar el ID
            from datetime import datetime
            # Valida campo vacio
            if not usuario_param.name.strip():
                raise HTTPException(status_code=404, detail="El nombre no puede estar vació.")
            update_data['date_modified'] = datetime.now(self.colombia_timezone).strftime("%d/%m/%Y %H:%M:%S") # Nueva fecha con formato
            producto.update(dict(**update_data))
            self.db.commit()
            return self.db.query(Producto).filter(Producto.id == usuario_param.id).first()
  
    @service_exception_handler
    def delete_item(self, id: int):
        item = self.db.query(Producto).filter(Producto.id == id)
        if item.first():
            producto_data = ProductoModel.model_validate(item.first())
            update_data = producto_data.model_dump() 
            update_data['status'] = "I" # Marcar como Inactivo
            update_data['date_modified'] = datetime.now(self.colombia_timezone).strftime("%d/%m/%Y %H:%M:%S") # Nueva fecha con formato
            item.update(dict(**update_data))
            self.db.commit()
            return item.first()
        else:
            raise HTTPException(status_code=404,detail="No se encuentra el producto con el id ingresado.")
            
   
