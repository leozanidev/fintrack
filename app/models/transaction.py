from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Numeric
from enum import Enum
from sqlalchemy import Enum as SQLEnum

class TipoTransacao(Enum):
    RECEITA = "Receita"
    DESPESA = "Despesa"

class Transaction(Base):
    __tablename__ = "transacao"
    