# Module 00: Project Conception & Domain Architecture

## 1. Executive Summary & Civic Mission

**Share Help** is an open-source, non-profit civic tech platform designed to coordinate resource matching and volunteer dispatch during natural disasters (such as hurricanes and flash floods).

Unlike commercial logistics networks, disaster coordination requires high operational integrity under chaotic conditions. The platform acts as a decentralized coordination bridge, matching real-time community supply with verified demand without managing physical warehouses.

---

## 2. Invariants & Business Logic Foundation

During the initial discovery phase, core operational boundaries (invariants) were established:

- **Strict Non-Profit & Compliance:** No anonymous pledges are permitted. All donors must verify identity to preserve transparency and prevent fraud.
- **Mutual Exclusion Rule (BR-001):** An active rescue requester in a disaster zone cannot simultaneously be dispatched as an operational field volunteer.
- **Fractional & Multi-party Matching (BR-002):** A single assistance request can be met by multiple donors, and a large bulk donation can be split across multiple affected locations ($N:M$ relational mapping).
- **Immutable Auditability (BR-003):** Every record modification and state transition is captured in an append-only log containing actor ID, entity reference, and previous/new state payloads.

---

## 3. Architecture Decision Records (ADRs)

Technical choices are formally recorded as ADRs in `docs/adr/` to eliminate tribal knowledge:

1. **ADR-001:** Standardized the Michael Nygard format for architectural records.
2. **ADR-002:** Defined MVP scope boundaries (excluding social scraping and warehousing to focus on matching and integrity).
3. **ADR-003:** Selected PostgreSQL as the primary RDBMS for ACID guarantees, foreign key constraints, and spatial readiness (PostGIS).
4. **ADR-004:** Selected Python 3.13+ with FastAPI, Pydantic v2, and SQLAlchemy (Async) for typed contracts, asynchronous speed, and automated OpenAPI documentation.

---

## 4. Persistence Modeling (Entity-Relationship Design)

The relational persistence model was established using Mermaid in `docs/domain/schema.md`:

- **`users`**: Base identity for Requesters, Donors, Volunteers, Coordinators, and Auditors.
- **`resources`**: Catalog of items, assets, or volunteer hours, constrained by finite state machines (`AVAILABLE` → `ALLOCATED` → `DELIVERED`).
- **`assistance_requests`**: Field requests classified by triage urgency (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).
- **`allocations`**: Associative table binding `request_id`, `resource_id`, and `coordinator_id` to govern fractional distribution.
- **`audit_logs`**: Append-only audit trail capturing operational lifecycle changes.
