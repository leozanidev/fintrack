from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UsuarioLogin
from app.models.user import Usuarios
from app.core.security import verifica_senha, cria_access_token

router = APIRouter()

@router.post("/login")
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.email == dados.email).first() # Mande um SELECT na tabela USUARIOS com WHERE e pega o PRIMEIRO registro
    if not usuario or not verifica_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos.")
    token = cria_access_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}