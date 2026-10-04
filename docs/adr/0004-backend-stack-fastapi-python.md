# 4. Select Backend Framework and Tooling (Python & FastAPI)

Date: 2026-10-04

## Status

Accepted

## Context

The Share Help platform requires a robust backend architecture capable of handling transactional resource allocations, strict schema validations, role-based access control, and seamless integration with PostgreSQL.

The engineering team needs a stack that balances developer ergonomics, strict data modeling via type hints, strong open-source tooling, and automated API contract generation for frontend client consumption.

## Decision

We will build the core backend application using **Python 3.12+** with the **FastAPI** framework.

The supporting toolchain includes:
1. **FastAPI:** For asynchronous REST API development, dependency injection, and native OpenAPI/Swagger generation.
2. **Pydantic (v2):** For strictly typed data validation, request sanitization, and serialization (DTO layer).
3. **SQLAlchemy 2.0 (Async) & Alembic:** For database abstraction, query composition, and version-controlled PostgreSQL schema migrations.
4. **Pytest & HTTPX:** For automated testing coverage across unit, integration, and state-machine transitions.
5. **Ruff:** For lightning-fast linting and opinionated code formatting adhering to PEP 8 standards.

## Consequences

### Positive
- Automatic, interactive API documentation reduces manual documentation drift.
- Native asynchronous request handling (via `asyncio` and `uvloop`) efficiently serves concurrent I/O-bound requests.
- Type annotations across domain entities and request bodies reduce runtime payload errors.
- Rich ecosystem of geospatial libraries (such as GeoAlchemy2 and Shapely) compatible with future PostGIS features.

### Negative
- Python executes in an interpreted runtime, requiring careful performance profiling under CPU-intensive operations compared to compiled languages like Go.
- Strict discipline with type hinting is required across all modules to preserve type safety.