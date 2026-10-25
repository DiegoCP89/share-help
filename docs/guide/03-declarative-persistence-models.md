# Module 03: Relational Persistence Layer (SQLAlchemy 2.0 & PostgreSQL)

## 1. Domain Entities & Object-Relational Mapping (ORM)

The persistence layer translates domain requirements established in `docs/domain/schema.md` into strongly-typed SQLAlchemy declarative classes under `src/models/`:

- **`User` (`users`):** Platform identity covering victims, donors, volunteers, coordinators, and auditors. Utilizes UUIDv4 primary keys, role-based access control enums (`UserRole`), and soft deletion (`is_active: bool`) for audit continuity.
- **`Resource` (`resources`):** Tangible supplies, heavy equipment, financial pledges, and volunteer labor hours. Employs `Numeric(12, 2)` for zero-loss precision, decimal coordinates (`Numeric(9, 6)`) for GPS field accuracy, and table-level `CheckConstraint` bounds preventing negative inventory.
- **`AssistanceRequest` (`assistance_requests`):** Field requests prioritizing urgency classification (`UrgencyLevel`) and tracking state machine milestones (`RequestStatus`).
- **`Allocation` (`allocations`):** $N:M$ associative table linking resources to requests with mandatory coordinator oversight (`coordinator_id`) and positive allocation invariants (`allocated_quantity > 0`).
- **`AuditLog` (`audit_logs`):** Append-only forensic journal tracking entity state diffs via PostgreSQL `JSONB` structures (`previous_state`, `new_state`) with non-cascading actor preservation (`ondelete="SET NULL"`).

---

## 2. Advanced Engineering Practices Implemented

### Inheritance & Reusable Mixins (`TimestampMixin`)

Instead of duplicating audit columns across every table, `TimestampMixin` provides timezone-aware UTC creation (`created_at`) and automatic update (`updated_at`) timestamps across models.

### Circular Import Prevention (`TYPE_CHECKING`)

Cross-model relationships utilize Python's `typing.TYPE_CHECKING` guard combined with string forward references (e.g., `Mapped["User"] = relationship()`). This decouples static type checking from runtime module imports.

### Centralized Public Interface (`__all__`)

The `src/models/__init__.py` file acts as the public registry for all persistence models and enumeration classes, ensuring clear encapsulation and predictable imports across services.
