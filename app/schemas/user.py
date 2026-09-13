from pydantic import BaseModel
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    criado_em: datetime
    ativo: bool