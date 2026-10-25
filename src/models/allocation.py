import enum
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Enum, ForeignKey, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.request import AssistanceRequest
    from src.models.resource import Resource
    from src.models.user import User


class AllocationStatus(enum.StrEnum):
    """Lifecycle stages of a resource allocation to a request."""

    PROPOSED = "PROPOSED"
    COMMITTED = "COMMITTED"
    DISPATCHED = "DISPATCHED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class Allocation(Base, TimestampMixin):
    """Associative model binding resources to assistance requests via coordinator oversight."""

    __tablename__ = "allocations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    request_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assistance_requests.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    resource_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("resources.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    coordinator_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    allocated_quantity: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )
    status: Mapped[AllocationStatus] = mapped_column(
        Enum(AllocationStatus, name="allocation_status_enum", native_enum=True),
        nullable=False,
        default=AllocationStatus.PROPOSED,
    )
    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Relationships
    request: Mapped["AssistanceRequest"] = relationship()
    resource: Mapped["Resource"] = relationship()
    coordinator: Mapped["User"] = relationship()

    # Table-level constraints
    __table_args__ = (
        CheckConstraint(
            "allocated_quantity > 0",
            name="check_positive_allocated_quantity",
        ),
    )
