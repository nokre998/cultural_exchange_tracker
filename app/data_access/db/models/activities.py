# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .events import Event


# class Activity(Base):
#     __tablename__ = "activities"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     start_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)
#     end_time: Mapped[Optional[DateTime]] = mapped_column(DateTime)

#     event: Mapped["Event"] = relationship(back_populates="activities")

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .events import Event


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime)

    event: Mapped["Event"] = relationship(
        "Event",
        back_populates="activities"
    )