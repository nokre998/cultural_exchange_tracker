# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .userlanguages import UserLanguage
# from .roles import Role

# class Language(Base):
#     __tablename__ = "languages"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String, nullable=False)
#     code: Mapped[str] = mapped_column(String(5), unique=True, nullable=False)

#     users: Mapped[List["UserLanguage"]] = relationship(back_populates="language")

from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .userlanguages import UserLanguage


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[str] = mapped_column(String(5), unique=True, nullable=False)

    users: Mapped[List["UserLanguage"]] = relationship(
        "UserLanguage",
        back_populates="language"
    )