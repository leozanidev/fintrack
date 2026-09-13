from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,ForeignKey

class Categorias(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuarios: Mapped["Usuarios"] = relationship(back_populates="categorias")
    transacoes: Mapped[list["Transacoes"]] = relationship(back_populates="categoria")
