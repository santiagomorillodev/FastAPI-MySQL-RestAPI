Aquí tienes el archivo listo para copiar:
# 🚀 FastAPI MySQL REST API con SQLAlchemy

Este proyecto implementa una API REST utilizando **FastAPI** y **SQLAlchemy** para conectar con una base de datos **MySQL**, proporcionando una estructura modular y escalable.

---

## 📌 Tecnologías utilizadas
✅ **FastAPI** – Framework web moderno y rápido  
✅ **SQLAlchemy** – ORM para bases de datos SQL  
✅ **MySQL** – Sistema de gestión de bases de datos  
✅ **Pydantic** – Validación y serialización de datos  
✅ **Uvicorn** – Servidor ASGI optimizado para FastAPI  

---

## 📂 Estructura del proyecto
📁 `config/` ➜ Configuración de la base de datos  
📁 `models/` ➜ Definición de modelos SQLAlchemy  
📁 `schemas/` ➜ Esquemas Pydantic para validación  
📁 `routes/` ➜ Rutas de la API  
📄 `crud.py` ➜ Funciones CRUD para manipulación de datos  
📄 `app.py` ➜ Punto de entrada de la API  
📄 `requirements.txt` ➜ Dependencias del proyecto  

---

## 🔧 Instalación y configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/fastapi-mysql-restapi.git
cd fastapi-mysql-restapi


2️⃣ Instalar dependencias
pip install -r requirements.txt


3️⃣ Configurar la base de datos en MySQL
Ejecuta en MySQL para crear la base de datos:
CREATE DATABASE facebook_post_db;


Configura la conexión en config/database.py:
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/facebook_post_db"



📝 Definición del modelo SQLAlchemy
En models/models.py, se define la estructura de la tabla Post:
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)



📌 Esquemas Pydantic
📄 schemas/post.py define el formato de los datos que la API manejará:
from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    id: Optional[int] = None
    class Config:
        from_attributes = True

class Post(PostBase):
    pass



📌 Endpoints disponibles
📄 app.py define los siguientes endpoints de FastAPI:
| Método | Ruta | Descripción | 
| POST | /post | Crear un nuevo post | 
| GET | /get/post | Obtener lista de posts | 


Ejemplo de uso en FastAPI:
@app.post("/post")
def create_post_route(post: PostCreate, database: Session = Depends(get_db)):
    return create_post(database, post)

@app.get("/get/post")
def read_posts(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):
    return get_posts(database, skip, limit)



🚀 Iniciar el servidor
Ejecuta el siguiente comando para iniciar el servidor FastAPI con Uvicorn:
uvicorn app:app --reload


🔹 Swagger UI: http://127.0.0.1:8000/docs
🔹 Redoc: http://127.0.0.1:8000/redoc

📌 Cómo contribuir
Si deseas mejorar el proyecto, ¡envía un Pull Request o reporta problemas en Issues! 🎯

📜 Licencia
Este proyecto está bajo la licencia MIT.
