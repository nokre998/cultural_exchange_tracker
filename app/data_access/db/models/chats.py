from datetime import datetime
from typing import List, Optional
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base
# from .exchanges import Exchange
# from .messages import Message
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .exchanges import Exchange
    from .messages import Message

class Chat(Base):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    exchange: Mapped["Exchange"] = relationship(
        "Exchange",
        back_populates="chats"
    )
    messages: Mapped[List["Message"]] = relationship(
        "Message",
        back_populates="chat"
    )