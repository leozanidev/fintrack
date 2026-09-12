from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,ForeignKey

class Category(Base):
    __tablename__ = "categoria"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
