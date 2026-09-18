from pydantic import BaseModel
from datetime import datetime
from app.models.transaction import TipoTransacao
from decimal import Decimal

class TransacaoCreate(BaseModel):
    descricao: str
    valor: Decimal
    tipo: TipoTransacao
    data: datetime
    category_id: int 

class TransacaoResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: TipoTransacao
    data: datetime
    category_id: int
    user_id: int

class TransacaoUpdate(BaseModel):     
    descricao: str | None = None
    valor: Decimal | None = None
    tipo: TipoTransacao | None = None
    data: datetime | None = None
    category_id: int | None = None
