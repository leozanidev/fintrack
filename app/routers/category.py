from fastapi import APIRouter, Depends
from app.models.category import Categorias
from app.models.user import Usuarios
from app.schemas.category import CategoriaCreate, CategoriaResponse
from app.database import get_db
from app.core.deps import get_usuario_atual
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/categories", response_model=CategoriaResponse)
def cria_categoria(dados: CategoriaCreate, db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    nova_categoria = Categorias(
        nome = dados.nome,
        user_id = usuario.id
    )

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria