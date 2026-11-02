from dairymanagement.app.databases.models.base import Base
from datetime import datetime

from sqlalchemy import DateTime, Numeric, CheckConstraint,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal



class MilkRate(Base):
    __tablename__ = 'milk_rates'

    __table_args__ = (
        CheckConstraint(
            "rate_per_litre > 0",
            name="ck_milk_rates_positive_rate",
        ),
        CheckConstraint(
            "effective_to IS NULL OR effective_to > effective_from",
            name="ck_milk_rates_valid_dates",
        ),
    )

    id:Mapped[int]= mapped_column(
        primary_key=True
    )
    rate_per_litre:Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )
    effective_from:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        index=True
    )


    effective_to: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_by:Mapped[int]= mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    creator = relationship("User")