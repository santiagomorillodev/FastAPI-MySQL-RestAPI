from sqlalchemy.orm import Session
from models.models import Post 
from schemas.post import PostCreate

'''
    • Session: Importamos una vez mas el Session para indicar
    el tipo de dato que nos debe llegar en el parametro
    database
    
    • Post, PostCreate: Son los modelos de como queremos que nos llegen los datos
    como lo indicamos en el archivo schemas/post.py
    
    PostModel: Es el modelo de tabla al cual queremos convertir los datos
    que nos llegan como Clases en este caso PostCreate
'''


# Paso 5: Creamos las funciones que se usaran en nuestra app
def create_post(database: Session, post_data: PostCreate):
    '''
        Args:
            database (Session): Es la conexion temporal que creamos para
            poder enviar los datos para crear el post que nos llega desde
            get_db() en el archivo app.py
            
            post_data (PostCreate): Es la clase de pydantic que definimos
            para crear una publicacion, lo que validara que los datos
            lleguen como los requerimos
    '''
    obj = Post(**post_data.dict())
    '''
        Aqui convertimos post_data a un formato que SQLAlchemy pueda
        usar, por eso lo convertimos en un diccionario en ejemplo:

        {"title": "Mi primer post","content": "Esto es un ejemplo"}
        
        luego usamos **(kwargs) para desempaquetar los argumentos
        lo cual en un ejemplo se veria como algo asi:
        
        PostModel(title="Mi primer post", content="Esto es un ejemplo")
    '''
    database.add(obj)
    # agregamos el objeto a la sesion (conexion)
    database.commit()
    # Aqui guardamos el objeto en la base de datos
    database.refresh(obj)
    # luego actualizamos el objeto para que tenga los valores actualizados
    return obj
    # Lo retornamos como respuesta del endpoint

def get_posts(database: Session, skip: int = 0, limit: int = 10):
    '''
        Args:
            database (Session): Es la conexion temporal que creamos para
            poder enviar los datos para crear el post que nos llega desde
            get_db() en el archivo app.py
            
            skip (int): número de registros que quieres saltar antes de 
            empezar a devolver resultados.
            
            limit (int): número máximo de registros que quieres obtener.
    '''
    query = database.query(Post)
    # aqui seleccionamos la tabla que queremos usar el PostModel es la representacion
    # de la tabla "post" que creamos en models/models.py
    query = query.offset(skip)
    # offset(n) salta los primeros n resultados.
    query = query.limit(limit)
    # limit(n) indica cuántos registros quieres recibir como máximo.
    return query.all()
    # .all() ejecuta la consulta y devuelve una lista de objetos Post.