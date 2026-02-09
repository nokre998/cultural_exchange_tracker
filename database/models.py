from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
from database.db import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    role_id: Mapped[str] = mapped_column(ForeignKey(), nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[int] = mapped_column(DateTime, nullable=True)


class Role(Base):
    __tablename__ = "roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)


