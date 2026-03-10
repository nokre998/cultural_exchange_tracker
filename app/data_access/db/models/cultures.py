# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .exchanges import Exchange


# class Culture(Base):
#     __tablename__ = "cultures"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String, nullable=False)
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     country: Mapped[Optional[str]] = mapped_column(String)

#     exchanges: Mapped[List["Exchange"]] = relationship(back_populates="culture")

from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .exchanges import Exchange


class Culture(Base):
    __tablename__ = "cultures"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    country: Mapped[Optional[str]] = mapped_column(String)

    exchanges: Mapped[List["Exchange"]] = relationship(
        "Exchange",
        back_populates="culture"
    )