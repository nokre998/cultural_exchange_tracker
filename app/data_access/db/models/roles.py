# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .users import User

# class Role(Base):
#     __tablename__ = "roles"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

#     users: Mapped[List["User"]] = relationship(back_populates="role")

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .users import User  # только для подсказок типов, импорт не выполняется во время runtime

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Используем строковое имя класса для relationship
    users: Mapped[List["User"]] = relationship("User", back_populates="role")