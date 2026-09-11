from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"msg":"Bem-Vindo à minha API."}

@app.get("/health")
def get_health():
    return {"status":"ok"}