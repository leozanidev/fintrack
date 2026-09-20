from decimal import Decimal
from pydantic import BaseModel
from datetime import datetime

class DashboardResponse(BaseModel):
    total_receitas: Decimal
    total_despesas: Decimal
    saldo: Decimal

class ResumoMensal(BaseModel):
    mes: datetime
    total_receitas: Decimal
    total_despesas: Decimal
    saldo: Decimal