# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from .chats import Chat
# from .users import User
# from data_access.db.base import Base



# class Message(Base):
#     __tablename__ = "messages"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
#     sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
#     message_text: Mapped[str] = mapped_column(Text, nullable=False)
#     sent_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

#     chat: Mapped["Chat"] = relationship(back_populates="messages")
#     sender: Mapped["User"] = relationship(back_populates="messages_sent")

from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .chats import Chat
    from .users import User


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"),
        nullable=False
    )

    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    message_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )

    chat: Mapped["Chat"] = relationship(
        "Chat",
        back_populates="messages"
    )

    sender: Mapped["User"] = relationship(
        "User",
        back_populates="messages_sent"
    )