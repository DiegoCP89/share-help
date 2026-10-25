import enum
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.user import User


class ResourceCategory(str, enum.Enum):
    """Categorization for relief supply cataloging."""

    CONSUMABLE = "CONSUMABLE"
    ASSET = "ASSET"
    VOLUNTEER_LABOR = "VOLUNTEER_LABOR"
    FINANCIAL = "FINANCIAL"


class ResourceStatus(str, enum.Enum):
    """Lifecycle states of an inventory resource."""

    AVAILABLE = "AVAILABLE"
    ALLOCATED = "ALLOCATED"
    DISPATCHED = "DISPATCHED"
    COMPLETED = "COMPLETED"
    RETIRED = "RETIRED"


class Resource(Base, TimestampMixin):
    """Declarative persistence model for donated or registered relief assets."""

    __tablename__ = "resources"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    donor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    category: Mapped[ResourceCategory] = mapped_column(
        Enum(ResourceCategory, name="resource_category_enum", native_enum=True),
        nullable=False,
    )
    item_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    total_quantity: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )
    available_quantity: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )
    unit_of_measure: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    status: Mapped[ResourceStatus] = mapped_column(
        Enum(ResourceStatus, name="resource_status_enum", native_enum=True),
        default=ResourceStatus.AVAILABLE,
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
    donor: Mapped["User"] = relationship()

    # Table-level constraints
    __table_args__ = (
        CheckConstraint(
            "available_quantity >= 0",
            name="check_positive_available_quantity",
        ),
        CheckConstraint(
            "available_quantity <= total_quantity",
            name="check_available_le_total_quantity",
        ),
    )