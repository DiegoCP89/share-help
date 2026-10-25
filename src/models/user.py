import enum
import uuid
from sqlalchemy import Boolean, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import Base, TimestampMixin


class UserRole(str, enum.Enum):
    """User operational roles for RBAC authorization."""

    VICTIM = "VICTIM"
    DONOR = "DONOR"
    VOLUNTEER = "VOLUNTEER"
    COORDINATOR = "COORDINATOR"
    AUDITOR = "AUDITOR"


class User(Base, TimestampMixin):
    """Declarative persistence model representing platform participants."""

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )
    phone_number: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
    )
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role_enum", native_enum=True),
        nullable=False,
        default=UserRole.VICTIM,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )