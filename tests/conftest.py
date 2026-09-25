from app.core.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base

conn_string_test = Settings.conn_string_test
engine_test = create_engine(conn_string_test)
SessionLocalTest = sessionmaker(bind=engine_test)

def override_get_db():
    db = SessionLocalTest()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine_test)