from pydantic import BaseModel
from typing import Optional

'''
    • BaseModel: Basicamente valida que los datos se envien como le indiquemos
    si queremos que sea str,int,list
    
    • Optional: Es para que el dato id pueda ser opccional para que la base de
    datos pueda asignarle uno con autoincremtal, esto se ve en models/models.py
'''
# Paso 4: Crear los modelos de los archivos que nos tienen que enviar para poder
# Crear, leer, actualizar, borrar las tablas, paso 5 en crud

class PostBase(BaseModel):
    '''
        Esta es la case base, que contiene todo lo que tendran
        las otras clases del mismo tipo, esto se hace asi por
        standard
    '''
    title: str
    content: str

class PostCreate(PostBase):
    '''
        Esta clase contiene lo mismo que la clase PostBase, pero esta
        tiene el id que se crea por defecto, se debe crear como opcional
        en None porque el id lo asigna la base de datos, se auto incrementa
        gracias a que lo definimos en la tabla en models/models.py
    '''
    id: Optional[int] = None
    
    class Config:
        from_attributes = True

class Post(PostBase):
    '''
        Aunque esta clase es indentica a PostBase se debe crear asi
        por standard, este sera el formato en el que llegaran los
        datos para poder ser leidos
    '''
    pass