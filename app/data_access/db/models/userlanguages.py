# from datetime import datetime
# from typing import Optional
# from sqlalchemy import DateTime, ForeignKey, String
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .users import User
# from .languages import Language

# class UserLanguage(Base):
#     __tablename__ = "user_languages"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
#     language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"), nullable=False)
#     level: Mapped[str] = mapped_column(String, nullable=False)  # basic/intermediate/native

#     user: Mapped["User"] = relationship(back_populates="languages")
#     language: Mapped["Language"] = relationship(back_populates="users")

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .users import User
    from .languages import Language


class UserLanguage(Base):
    __tablename__ = "user_languages"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    language_id: Mapped[int] = mapped_column(
        ForeignKey("languages.id"),
        nullable=False
    )

    level: Mapped[str] = mapped_column(
        String,
        nullable=False
    )  # basic/intermediate/native

    user: Mapped["User"] = relationship(
        "User",
        back_populates="languages"
    )

    language: Mapped["Language"] = relationship(
        "Language",
        back_populates="users"
    )