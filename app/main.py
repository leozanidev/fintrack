from fastapi import FastAPI
from dotenv import load_dotenv
from app.router import user, auth
from app import models
import os



load_dotenv()
app_name = os.getenv("APP_NAME")

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def get_root():
    return {"msg":f"Bem-Vindo à minha {app_name}."}

@app.get("/health")
def get_health():
    return {"status":"ok"}