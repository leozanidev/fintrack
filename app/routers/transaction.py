from app.schemas.transaction import TransacaoCreate, TransacaoResponse
from app.models.transaction import Transacoes
from app.models.user import Usuarios
from app.core.deps import get_usuario_atual
from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/transactions", response_model=TransacaoResponse)
def cria_transacao(dados: TransacaoCreate, db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    nova_transacao = Transacoes(
        descricao = dados.descricao,
        valor = dados.valor,
        tipo = dados.tipo,
        data = dados.data,
        category_id = dados.category_id,
        user_id = usuario.id
    )

    db.add(nova_transacao) # Avisa que vai haver uma inserção
    db.commit() # Faz a inserção de fato
    db.refresh(nova_transacao) # Atualiza o objeto com os dados criados pelo banco

    return nova_transacao