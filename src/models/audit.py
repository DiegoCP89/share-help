import enum
import uuid
from typing import Any, TYPE_CHECKING
from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.user import User


class AuditAction(str, enum.Enum):
    """Categorization of audited system events."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    STATUS_CHANGE = "STATUS_CHANGE"


class AuditLog(Base, TimestampMixin):
    """Append-only audit trail capturing state modifications for forensic transparency."""

    __tablename__ = "audit_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    actor_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    action: Mapped[AuditAction] = mapped_column(
        Enum(AuditAction, name="audit_action_enum", native_enum=True),
        nullable=False,
    )
    entity_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
    )
    entity_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )
    previous_state: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
        nullable=True,
    )
    new_state: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    # Relationships
    actor: Mapped["User | None"] = relationship()