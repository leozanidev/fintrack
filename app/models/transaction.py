from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric, func
from enum import Enum
from sqlalchemy import Enum as SQLEnum
from datetime import datetime
from decimal import Decimal

class TipoTransacao(Enum):
    RECEITA = "Receita"
    DESPESA = "Despesa"

class Transacoes(Base):
    __tablename__ = "transacoes"
    id:Mapped[int] = mapped_column(primary_key=True)
    descricao:Mapped[str] = mapped_column(String(512), nullable=False)
    valor:Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    tipo:Mapped[TipoTransacao] = mapped_column(SQLEnum(TipoTransacao), nullable=False)
    data:Mapped[datetime] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    category_id:Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    usuario: Mapped["Usuarios"] = relationship(back_populates="transacoes")
    categoria: Mapped["Categorias"] = relationship(back_populates="transacoes")