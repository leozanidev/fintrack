from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UsuarioCreate, UsuarioResponse
from app.models.user import Usuarios
from app.core.security import hash_senha
from app.core.deps import get_usuario_atual


router = APIRouter()

@router.post("/users", response_model=UsuarioResponse)
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(get_db)):
    senha_hash = hash_senha(dados.senha) # Codificando a senha

    novo_usuario = Usuarios(
        # Criando o objeto novo usuário, que recebe os dados para mandar e salvar no banco
        nome = dados.nome,
        email = dados.email,
        senha_hash = senha_hash
    )

    db.add(novo_usuario) # Avisa ao SQLAlchemy que esse objeto deve ser inserido no banco de dados ( porém ainda não inseriu )
    db.commit() # Executa o insert 
    db.refresh(novo_usuario) # Atualiza a atualização do objeto com os dados que foram criados pelo banco de dados
    return novo_usuario

@router.get("/users/me", response_model=UsuarioResponse)
def busca_usuario_atual(usuario_atual: Usuarios = Depends(get_usuario_atual)):
    return usuario_atual