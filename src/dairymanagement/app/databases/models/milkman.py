from dairymanagement.app.databases.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, ForeignKey, Boolean, DateTime

from datetime import datetime


class MilkMan(Base):
    __tablename__ = "milkmen"


    id:Mapped[int] = mapped_column(
        primary_key=True
    )

    unique_id:Mapped[str]= mapped_column(
        String(50),
        unique=True,
        nullable=False,

    )
    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False,

    )
    phone:Mapped[str]= mapped_column(
        String(20),
        nullable=False,
        unique=True,
      

    )
    address:Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    branch_id:Mapped[int]=mapped_column(
            ForeignKey('branches.id'),
            nullable=False,
            index=True
        )
    is_active:Mapped[bool]=mapped_column(
        Boolean,
        default=True,
        nullable=False

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

    branch = relationship(
        'Branch',
        back_populates='milkmen'
    )