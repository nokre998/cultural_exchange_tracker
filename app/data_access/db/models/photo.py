# from datetime import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime, ForeignKey, String, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from data_access.db.base import Base
# from .exchanges import Exchange
# from .users import User


# class Photo(Base):
#     __tablename__ = "photos"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     exchange_id: Mapped[int] = mapped_column(ForeignKey("exchanges.id"), nullable=False)
#     uploaded_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
#     file_url: Mapped[str] = mapped_column(String, nullable=False)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

#     exchange: Mapped["Exchange"] = relationship(back_populates="photos")
#     uploaded_by_user: Mapped["User"] = relationship(back_populates="photos_uploaded")

from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_access.db.base import Base

if TYPE_CHECKING:
    from .exchanges import Exchange
    from .users import User


class Photo(Base):
    __tablename__ = "photos"

    id: Mapped[int] = mapped_column(primary_key=True)

    exchange_id: Mapped[int] = mapped_column(
        ForeignKey("exchanges.id"),
        nullable=False
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    file_url: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )

    exchange: Mapped["Exchange"] = relationship(
        "Exchange",
        back_populates="photos"
    )

    uploaded_by_user: Mapped["User"] = relationship(
        "User",
        back_populates="photos_uploaded"
    )