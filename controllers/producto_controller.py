from typing import List
from fastapi import APIRouter
from models.producto_item import ProductoModel
from services.producto_service import ProductoService
from models.response_model import ResponseModel
from decorators.exception_handler import controller_exception_handler

# Define propiedades del router
router = APIRouter()
router.prefix="/producto"
router.tags=["Producto"]

producto_service = ProductoService()

@router.get("/getProducto/{id}", response_model=ResponseModel)
@controller_exception_handler
def get_producto(id: int): 
    producto = producto_service.get_producto(id) 
    return ResponseModel().create_response(success=True, 
        message="Producto encontrado.", status_code=200,
        data=producto)

@router.get("/getProductos", response_model=ResponseModel)
@controller_exception_handler
def get_productos(): 
    productos = producto_service.get_productos()
    productos_data = [ProductoModel.model_validate(producto).model_dump() for producto in productos]
    return ResponseModel().create_response(success=True,status_code=200, 
        message="Lista de productos.", 
        data=productos_data) 
 
@router.post("/addProducto")
@controller_exception_handler
def add_producto(producto_model: ProductoModel):
    producto = producto_service.create_item(producto_model) 
    return ResponseModel().create_response(success=True, 
        message="Producto creado", status_code=200,
        data={"producto": producto})

@router.put("/updateProducto")
@controller_exception_handler
def update_producto(producto_model: ProductoModel):
    producto = producto_service.update_item(producto_model)
    #producto_model_data = 

    return ResponseModel().create_response(success=True, 
        message="Producto actualizado", status_code=200, 
        data={"producto": producto})
         
@router.delete("/deleteProducto/{item_id}")
@controller_exception_handler
def delete_item(item_id: int):
    producto = producto_service.delete_item(item_id)
    return ResponseModel().create_response(success=True, 
        message="Producto eliminado", status_code=200,
        data={"producto": producto})
