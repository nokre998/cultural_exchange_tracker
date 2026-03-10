# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .events import Event
# from .exchanges import Exchange
# from .users import User   


# class ExchangeParticipant(Base):
#     __tablename__ = "exchange_participants"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id"), nullable=False)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
#     status: Mapped[str] = mapped_column(String, nullable=False)  # planned / confirmed / completed

#     exchange: Mapped["Exchange"] = relationship(back_populates="participants")
#     user: Mapped["User"] = relationship(back_populates="exchange_participations")

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .exchanges import Exchange
    from .users import User


class ExchangeParticipant(Base):
    __tablename__ = "exchange_participants"

    id: Mapped[int] = mapped_column(primary_key=True)

    exchange_id: Mapped[int] = mapped_column(
        ForeignKey("exchanges.id"),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False
    )  # planned / confirmed / completed

    exchange: Mapped["Exchange"] = relationship(
        "Exchange",
        back_populates="participants"
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="exchange_participations"
    )