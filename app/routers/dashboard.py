from app.schemas.transaction import TransacaoCreate, TransacaoResponse, TransacaoUpdate
from app.models.transaction import Transacoes, TipoTransacao
from app.models.user import Usuarios
from app.schemas.dashboard import DashboardResponse, ResumoMensal
from app.core.deps import get_usuario_atual
from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

router = APIRouter()

@router.get("/dashboard", response_model=DashboardResponse)
def busca_dashboard(usuario: Usuarios = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    total_receita = db.query(func.sum(Transacoes.valor)).filter(Transacoes.user_id == usuario.id).filter(Transacoes.tipo == TipoTransacao.RECEITA).scalar()
    total_despesa = db.query(func.sum(Transacoes.valor)).filter(Transacoes.user_id == usuario.id).filter(Transacoes.tipo == TipoTransacao.DESPESA).scalar()
    if(total_receita is None):
        total_receita = 0    
    if(total_despesa is None):
        total_despesa = 0

    saldo = total_receita - total_despesa

    return {"total_receitas": total_receita, "total_despesas":total_despesa,"saldo": saldo}

@router.get("/dashboard/monthly", response_model=list[ResumoMensal])
def busca_dashboard_mensal(usuario: Usuarios = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    total_receitas = db.query(
        func.date_trunc("month", Transacoes.data),
        func.sum(Transacoes.valor)).filter(Transacoes.user_id == usuario.id).filter(Transacoes.tipo == TipoTransacao.RECEITA).group_by(func.date_trunc("month", Transacoes.data)).all()
    
    total_despesas = db.query(
        func.date_trunc("month", Transacoes.data),
        func.sum(Transacoes.valor)).filter(Transacoes.user_id == usuario.id).filter(Transacoes.tipo == TipoTransacao.DESPESA).group_by(func.date_trunc("month", Transacoes.data)).all()

    resumo = {} # Dicionário vazio
    for mes, soma in total_receitas:
        resumo[mes] = resumo.get(mes, {"total_receitas": 0, "total_despesas": 0})
        resumo[mes]["total_receitas"] = soma
    for mes, soma in total_despesas:
        resumo[mes] = resumo.get(mes, {"total_receitas": 0, "total_despesas": 0})
        resumo[mes]["total_despesas"] = soma

    resultado_final = []

    for mes, valores in resumo.items():
        saldo_mes = valores["total_receitas"] - valores["total_despesas"]
        resumo_mes = {
            "mes": mes,
            "total_receitas": valores["total_receitas"], 
            "total_despesas": valores["total_despesas"],
            "saldo": saldo_mes
        }
        resultado_final.append(resumo_mes)

    return resultado_final