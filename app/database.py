from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import Settings

engine = create_engine(Settings.conn_string)
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