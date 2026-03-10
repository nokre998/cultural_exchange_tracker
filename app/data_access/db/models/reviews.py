# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from .exchanges import Exchange
# from .users import User
# from data_access.db.base import Base


# class Review(Base):
#     __tablename__ = "reviews"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
#     exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id"), nullable=False)
#     rating: Mapped[int] = mapped_column(Integer, nullable=False)
#     comment: Mapped[Optional[str]] = mapped_column(Text)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

#     user: Mapped["User"] = relationship(back_populates="reviews")
#     exchange: Mapped["Exchange"] = relationship(back_populates="reviews")

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .users import User
    from .exchanges import Exchange


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    exchange_id: Mapped[int] = mapped_column(
        ForeignKey("exchanges.id"),
        nullable=False
    )

    rating: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    comment: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="reviews"
    )

    exchange: Mapped["Exchange"] = relationship(
        "Exchange",
        back_populates="reviews"
    )