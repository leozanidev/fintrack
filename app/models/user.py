from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, func
from datetime import datetime

class Usuarios(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    senha_hash: Mapped[str] = mapped_column(nullable=False)
    criado_em: Mapped[datetime] = mapped_column(server_default=func.now() ,nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True)
    transacoes: Mapped[list["Transacoes"]] = relationship(back_populates="usuario")
    categorias: Mapped[list["Categorias"]] = relationship(back_populates="usuarios")