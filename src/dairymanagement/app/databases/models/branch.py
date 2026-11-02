from dairymanagement.app.databases.models.base import Base

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import mapped_column, Mapped, relationship



class Branch(Base):
    __tablename__ = "branches"

    id:Mapped[int]=mapped_column(primary_key=True)

    name:Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False

    )
    address:Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False


    )
    updated_at:Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    
    users:Mapped[list["User"]] = relationship(
        "User",
        back_populates='branch'
    )

    milkmen:Mapped[list["MilkMan"]] = relationship(
        "MilkMan",
        back_populates="branch"
    )

