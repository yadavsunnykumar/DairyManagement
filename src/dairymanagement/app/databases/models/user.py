from dairymanagement.app.databases.models.base import Base
from datetime import datetime
from enum import Enum

from sqlalchemy import String,Boolean, Enum as SQLEnum, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserRole(str,Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    STAFF = 'STAFF'

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(
        primary_key=True
    )
    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False,

    )
    email:Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    password_hash:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    role:Mapped[str] = mapped_column(
        SQLEnum(UserRole),
        nullable=False,
        default=UserRole.STAFF
    )


    branch_id:Mapped[int]=mapped_column(
        ForeignKey('branches.id'),
        nullable=True,
        index=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    branch = relationship(
        "Branch",
        back_populates="users"
    )