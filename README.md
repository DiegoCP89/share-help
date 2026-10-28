# Share Help <img src="https://flagcdn.com/24x18/us.png" alt="US Flag" height="20"> 🤝 <img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Flag_of_Texas.svg" alt="Texas Flag" height="20">

[![Continuous Integration](https://github.com/DiegoCP89/share-help/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DiegoCP89/share-help/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Architecture: Modular Monolith](https://img.shields.io/badge/architecture-modular__monolith-orange.svg)](docs/adr/0005-modular-monolith-layered-architecture.md)

A civic-tech emergency coordination engine engineered for rapid, auditable resource allocation during extreme climate disasters.

---

## 1. Context & Operational Domain

While engineered as a globally adaptable platform, Share Help's primary validation baseline focuses on **coastal storm surge and extreme hurricane scenarios along the US Gulf Coast (specifically Texas)**.

During major hurricanes, standard municipal logistics face critical bottlenecks:

- **Volunteer Fleet Mobilization:** Coordinating private shallow-draft rescue vessels and 4x4 transport assets (e.g., civilian rescue operations like the Texas/Cajun volunteer fleets).
- **Critical Asset Tracking:** Managing mobile power generation units, portable water filtration systems, and non-perishable rations during widespread electrical grid failures.
- **Auditability & Integrity:** Delivering an immutable, append-only ledger for post-disaster accountability and transparent public reporting.

---

## 2. Architectural Overview & Engineering Standard

Share Help is structured as a **Modular Monolith** adhering to strict **Layered Architecture** principles (documented via [ADR-005](docs/adr/0005-modular-monolith-layered-architecture.md)). It cleanly decouples transport contracts, domain invariants, and persistence logic:

- **`src/api/` (Transport Layer):** FastAPI REST routers handling HTTP contracts, dependency injection, and status code negotiation.
- **`src/schemas/` (Contract Layer / DTOs):** Pydantic v2 schemas enforcing incoming payload validation and outbound JSON serialization.
- **`src/services/` (Domain Logic Layer):** Business rule orchestrations, state machines, and transactional invariant enforcement.
- **`src/models/` (Persistence Layer):** Strongly-typed SQLAlchemy 2.0 declarative mappings for PostgreSQL.
- **`src/core/` (Cross-Cutting Concerns):** Centralized runtime configurations (`pydantic-settings`) and security constraints.
- **`src/db/` (Database Engine & Migrations):** Async PostgreSQL session factory and Alembic migration scripts.

For formal engineering decisions, review our Architectural Decision Records under [`docs/adr/`](docs/adr/).

---

## 3. Core Domain Models

The relational schema implements core operational entities reflecting field coordination:

1. **`User` (`users`):** Role-based actors (`VICTIM`, `DONOR`, `VOLUNTEER`, `COORDINATOR`, `AUDITOR`) with soft-delete capabilities (`is_active: bool`).
2. **`Resource` (`resources`):** Tangible assets, consumables, volunteer labor, and financial pledges tracked with `Numeric(12, 2)` zero-loss precision and GPS coordinates.
3. **`AssistanceRequest` (`assistance_requests`):** Emergency aid tickets categorized by field urgency (`UrgencyLevel`) and tracking milestones (`RequestStatus`).
4. **`Allocation` (`allocations`):** $N:M$ associative resolution matching resources to requests under coordinator verification.
5. **`AuditLog` (`audit_logs`):** Append-only forensic journal tracking state transitions via native PostgreSQL `JSONB`.

---

## 4. Technology Stack

- **Runtime:** Python 3.13+
- **API Framework:** FastAPI
- **Data Validation:** Pydantic v2 / Pydantic Settings
- **ORM & Database:** SQLAlchemy 2.0 (Async) & PostgreSQL
- **Migrations:** Alembic
- **Static Analysis & Formatting:** Ruff
- **Testing Engine:** Pytest & HTTPX TestClient
- **CI Automation:** GitHub Actions

---

## 5. Setup Guide for New Contributors

> **Note for Active Maintainers:** If your local virtual environment (`.venv`) is already provisioned and active, proceed directly to running quality checks or launching the application.

### Initial Setup Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DiegoCP89/share-help.git](https://github.com/DiegoCP89/share-help.git)
   cd share-help
   ```
