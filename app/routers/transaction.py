from app.schemas.transaction import TransacaoCreate, TransacaoResponse, TransacaoUpdate
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

@router.get("/transactions", response_model=list[TransacaoResponse])
def busca_transacoes(db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    transacoes_usuario = db.query(Transacoes).filter(Transacoes.user_id == usuario.id).all()
    return transacoes_usuario

@router.get("/transactions/{id}", response_model=TransacaoResponse)
def busca_transacao_id(id: int, db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    transacao_unica = db.query(Transacoes).filter(Transacoes.user_id == usuario.id).filter(Transacoes.id == id).first()
    if (transacao_unica is None):
        raise HTTPException(status_code=404, detail="Transação não encontrada!")

    return transacao_unica

@router.put("/transactions/{id}", response_model=TransacaoResponse)
def edita_transacao(id: int, dados: TransacaoUpdate , db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    transacao_editar = db.query(Transacoes).filter(Transacoes.user_id == usuario.id).filter(Transacoes.id == id).first()
    if (transacao_editar is None):
            raise HTTPException(status_code=404, detail="Transação não encontrada!")
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(transacao_editar, chave, valor)

    db.commit()
    db.refresh(transacao_editar)

    return transacao_editar

@router.delete("/transactions/{id}", status_code=204)
def deleta_transacao(id: int, db: Session = Depends(get_db), usuario: Usuarios = Depends(get_usuario_atual)):
    transacao_deletar = db.query(Transacoes).filter(Transacoes.user_id == usuario.id).filter(Transacoes.id == id).first()
    if ( transacao_deletar is None):
          raise HTTPException(status_code=404, detail="Transação não encontrada!")

    db.delete(transacao_deletar)
    db.commit()