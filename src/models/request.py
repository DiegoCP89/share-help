import enum
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.user import User


class UrgencyLevel(enum.StrEnum):
    """Triage urgency classification for field assistance requests."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class AssistanceCategory(enum.StrEnum):
    """Domain category for the emergency assistance needed."""

    FOOD_WATER = "FOOD_WATER"
    MEDICAL = "MEDICAL"
    SHELTER = "SHELTER"
    EVACUATION = "EVACUATION"
    LOGISTICS = "LOGISTICS"


class RequestStatus(enum.StrEnum):
    """Operational lifecycle stages of an assistance request."""

    PENDING = "PENDING"
    TRIAGED = "TRIAGED"
    MATCHED = "MATCHED"
    IN_TRANSIT = "IN_TRANSIT"
    FULFILLED = "FULFILLED"
    CANCELLED = "CANCELLED"


class AssistanceRequest(Base, TimestampMixin):
    """Declarative persistence model representing emergency aid requests."""

    __tablename__ = "assistance_requests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    requester_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    category: Mapped[AssistanceCategory] = mapped_column(
        Enum(AssistanceCategory, name="assistance_category_enum", native_enum=True),
        nullable=False,
    )
    urgency: Mapped[UrgencyLevel] = mapped_column(
        Enum(UrgencyLevel, name="urgency_level_enum", native_enum=True),
        nullable=False,
        default=UrgencyLevel.MEDIUM,
    )
    status: Mapped[RequestStatus] = mapped_column(
        Enum(RequestStatus, name="request_status_enum", native_enum=True),
        nullable=False,
        default=RequestStatus.PENDING,
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    latitude: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 6),
        nullable=True,
    )
    longitude: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 6),
        nullable=True,
    )
    location_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Relationships
    requester: Mapped["User"] = relationship()
