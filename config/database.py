from sqlalchemy import create_engine
# Se crea el motos con engine y 
from sqlalchemy.orm import sessionmaker
from models.models import Base
'''
    • create_engine: Es la conexion que tiene la aplicacion con la base de datos
    es como un puente entre a la aplicacion y la base de datos
    
    • sessionmaker: El sessionmaker es basicamente lo que lleva y trae la informacion
    es necesario para leer y escribir datos con el ORM
    
    • models.models: Es la carpeta models que contiene el archivo models.py que contiene
    la clase Base que a su vez contiene las tablas que queremos crear

'''
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/facebook_post_db"

# Paso 1: Creamos la conexion o puente entre la app y la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=False)
'''
    • SQLALCHEMY_DATABASE_URL: Es la url de la base de datos
    
    • pool_pre_ping: Si se pierde la conexion, la revisa antes de cada consulta y si 
    es necesario la reestablece
    
    • echo: Si se pone en True muestra las consultas SQL que se ejecutan
'''
# Paso 2: Creamos la funcion que llevara y traera la informacion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
'''
    • autocommit: Requiere que usemos session.commit() para guardar los cambios
    
    • autoflush: No envia los cambios automaticamente 
    es necesario la reestablece
    
    • bind: conecta la sesion al engine que se conceta a la base de datos
    
    SessionLocal se usara cuando queramos leer, añadir, borrar o actualizar elementos
    de las tablas, en este caso se usa en el archivo "app" en la funcion "get_data()"
'''
# Paso 3: Creamos las tablas en el archivo models que esta en la carpeta models
Base.metadata.create_all(engine)

'''
    • Base.metadata: Contiene los modelos de las tablas que se definieron en models
    
    • create_all(engine): Se conecta con la base de datos y crea todas las tablas que
    aun no existen y excluye las que ya existen
'''
# Paso 4 en la carpeta schemas y en el archivo post.py
















#fastapi dev --app app