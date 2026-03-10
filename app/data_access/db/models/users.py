from datetime import datetime
from typing import List, Optional
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

# # from .userlanguages import UserLanguage

# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     password_hash: Mapped[str] = mapped_column(String, nullable=False)
#     full_name: Mapped[str] = mapped_column(String, nullable=False)
#     phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
#     role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
#     updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=datetime.utcnow)
    
#     role: Mapped["Role"] = relationship(back_populates="users")
#     # languages: Mapped[List["UserLanguage"]] = relationship(back_populates="user")

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .roles import Role
    from .userlanguages import UserLanguage
    from .exchange_participants import ExchangeParticipant
    from .exchanges import Exchange
    from .messages import Message
    from .photo import Photo
    from .reviews import Review

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    # full_name: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), onupdate=datetime.utcnow)

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    languages: Mapped[List["UserLanguage"]] = relationship("UserLanguage", back_populates="user")
    exchange_participations: Mapped[List["ExchangeParticipant"]] = relationship("ExchangeParticipant", back_populates="user")
    exchanges_organized: Mapped["Exchange"] = relationship("Exchange", back_populates="organizer")
    messages_sent: Mapped["Message"] = relationship("Message", back_populates="sender")
    photos_uploaded: Mapped["Photo"] = relationship("Photo", back_populates="uploaded_by_user")
    reviews: Mapped[List ["Review"]] = relationship("Review", back_populates="user")
    


