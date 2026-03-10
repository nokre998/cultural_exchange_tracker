# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# # from .activities import Activity
# from .exchanges import Exchange


# class Event(Base):
#     __tablename__ = "events"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id"), nullable=False)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     event_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
#     location: Mapped[Optional[str]] = mapped_column(String)

#     exchange: Mapped["Exchange"] = relationship(back_populates="events")
#     # activities: Mapped[List["Activity"]] = relationship(back_populates="event")

from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .exchanges import Exchange
    from .activities import Activity


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    exchange_id: Mapped[int] = mapped_column(
        ForeignKey("exchanges.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    event_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    location: Mapped[Optional[str]] = mapped_column(String)

    exchange: Mapped["Exchange"] = relationship(
        "Exchange",
        back_populates="events"
    )

    activities: Mapped[list["Activity"]] = relationship(
        "Activity",
        back_populates="event"
    )