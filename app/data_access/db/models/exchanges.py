# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import Date, DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from .chats import Chat
# from .exchange_participants import ExchangeParticipant
# from .photo import Photo
# from .partners import Partner
# from .users import User
# from data_access.db.base import Base
# from .cultures import Culture
# from .events import Event
# from .reviews import Review

# class Exchange(Base):
#     __tablename__ = "exchanges"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     culture_id: Mapped[int] = mapped_column(ForeignKey("cultures.id"))
#     organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     partner_id: Mapped[Optional[int]] = mapped_column(ForeignKey("partners.id"))
#     start_date: Mapped[Optional[Date]] = mapped_column(Date)
#     end_date: Mapped[Optional[Date]] = mapped_column(Date)
#     location: Mapped[Optional[str]] = mapped_column(String)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

#     culture: Mapped["Culture"] = relationship(back_populates="exchanges")
#     organizer: Mapped["User"] = relationship(back_populates="exchanges_organized")
#     partner: Mapped["Partner"] = relationship(back_populates="exchanges")
#     events: Mapped[List["Event"]] = relationship(back_populates="exchange")
#     participants: Mapped[List["ExchangeParticipant"]] = relationship(back_populates="exchange")
#     reviews: Mapped[List["Review"]] = relationship(back_populates="exchange")
#     photos: Mapped[List["Photo"]] = relationship(back_populates="exchange")
#     chats: Mapped[List["Chat"]] = relationship(back_populates="exchange")

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .chats import Chat
    from .exchange_participants import ExchangeParticipant
    from .photo import Photo
    from .partners import Partner
    from .users import User
    from .cultures import Culture
    from .events import Event
    from .reviews import Review


class Exchange(Base):
    __tablename__ = "exchanges"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    culture_id: Mapped[int] = mapped_column(ForeignKey("cultures.id"))
    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    partner_id: Mapped[Optional[int]] = mapped_column(ForeignKey("partners.id"))

    start_date: Mapped[Optional[Date]] = mapped_column(Date)
    end_date: Mapped[Optional[Date]] = mapped_column(Date)
    location: Mapped[Optional[str]] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )

    culture: Mapped["Culture"] = relationship("Culture", back_populates="exchanges")
    organizer: Mapped["User"] = relationship("User", back_populates="exchanges_organized")
    partner: Mapped["Partner"] = relationship("Partner", back_populates="exchanges")

    events: Mapped[List["Event"]] = relationship("Event", back_populates="exchange")
    participants: Mapped[List["ExchangeParticipant"]] = relationship("ExchangeParticipant", back_populates="exchange")
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="exchange")
    photos: Mapped[List["Photo"]] = relationship("Photo", back_populates="exchange")
    chats: Mapped[List["Chat"]] = relationship("Chat", back_populates="exchange")