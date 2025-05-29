from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()

''' 
    • Column: Ayuda a definer la configuracion de cada fila como id,tilte...
    
    • Integer,String,Text: Son los tipos de datos que tendran las columnas
    
    • declarative_base(): Es una clase que contiene el metadata y el registro
    de todas las tablas que se crean cuando una clase hereda la clase Base    

    Cuando una clase hereda el Base, SQLAlchemy crea un objeto Table,entonces 
    el objeto representa la tabla que queremos crearen este caso con el nombre 
    "post" y se guarda automaticamente dentro del Base.metadata.tables, que al
    final tendra un diccionario con todas las tablas definidas y sus columnas
'''

# Paso 3.1: Creamos las tablas
class Post(Base):
    __tablename__ = 'post'
    # Paso 3.1.1: Creamos las filas y las columnas de cada tabla
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )
    title = Column(
        String(100),
        nullable=False
    )
    content = Column(
        Text,
        nullable=False
    )