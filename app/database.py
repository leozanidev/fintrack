from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Carregando as variáveis de ambiente para dentro do arquivo
load_dotenv()

# Importando variável para montar a string de conexão com o banco de dados
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_pass_encoded = quote_plus(db_pass)
conn_string = f"postgresql://{db_user}:{db_pass_encoded}@{db_host}:{db_port}/{db_name}"

engine = create_engine(conn_string)
SessionLocal = sessionmaker(bind=engine)

# Se chamar DeclarativeBase() vai estar tentando instanciar DeclarativeBase, se chamar DeclarativeBase vai herdar
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()