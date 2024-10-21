from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database.database import Base

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True,unique=True)
    name = Column(String, index=True)
    date_created = Column(String, index=True)
    date_modified = Column(String, index=True)
    status = Column(String, index=True)
 
class ProductoModel(BaseModel):
    id: Optional[int] = None
    name: str
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True  # Permite la creación desde atributos de objetos ORM