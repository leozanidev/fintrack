from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome: str

class CategoriaResponse(BaseModel):
    id: int
    nome: str
    user_id: int