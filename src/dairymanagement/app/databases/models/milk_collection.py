
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dairymanagement.app.databases.models.base import Base


class MilkCollection(Base):
    __tablename__ = "milk_collections"

    __table_args__ = (
        CheckConstraint(
            "quantity_litres > 0",
            name="ck_milk_collections_positive_quantity",
        ),
        CheckConstraint(
            "rate_per_litre > 0",
            name="ck_milk_collections_positive_rate",
        ),
        CheckConstraint(
            "amount >= 0",
            name="ck_milk_collections_nonnegative_amount",
        ),
        UniqueConstraint(
            "milkman_id",
            "collection_date",
            name="uq_milk_collections_milkman_date",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    milkman_id: Mapped[int] = mapped_column(
        ForeignKey("milkmen.id"),
        nullable=False,
        index=True,
    )

    milk_rate_id: Mapped[int] = mapped_column(
        ForeignKey("milk_rates.id"),
        nullable=False,
    )

    collection_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    quantity_litres: Mapped[Decimal] = mapped_column(
        Numeric(10, 3),
        nullable=False,
    )

    rate_per_litre: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    recorded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    milkman = relationship("Milkman")
    milk_rate = relationship("MilkRate")
    recorder = relationship("User")
