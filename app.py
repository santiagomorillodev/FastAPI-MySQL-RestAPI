from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine, Base
from models.models import Post
from schemas.post import Post, PostCreate
from crud import create_post, get_posts
from routes.user import user

app = FastAPI()

# Paso 6: Creamos una funcion que se encargara de crear la conexion
# Temporal con la base de datos que usaremos en las funciones crud
# que usaran los endpoints
def get_db():
    '''
        Params:
            database (session): Es una conexion temporal con la base de datos
        
        • Yield database: devuelve la conexion temporal para que otras partes
        del codigo puedan usarla
        
        • Finally: Una vez terminado el proceso se ejecuta el finally que
        contiene el database.close() que cierra la conexion temporal
    '''
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

# Paso 7: Creamos los endpoints
@app.post("/post", response_model=Post)
def create_post_route(post:PostCreate, database: Session = Depends(get_db)):
    '''
        Args:
        
            post (PostCreate): es la clase de informacion que queremos que nos llegue
            esta clase la creamos en schemas/post.py
            
            database (Session): Es la conexion temporal que nos llega desde la funcion
            get_db()
            
        Returns:
            create_post (func): Una vez obtenida y validada la informacion se envia a la
            funcion create_post en el archivo crud
    '''
    return create_post(database, post)

@app.get("/get/post")
def read_posts(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):                          # Parámetros opcionales de paginación
    return get_posts(database, skip, limit) 