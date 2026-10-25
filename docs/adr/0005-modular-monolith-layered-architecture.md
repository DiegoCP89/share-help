# 5. Adopt Modular Monolith with Layered Architecture

Date: 2026-10-25

## Status

Accepted

## Context

Designing an emergency coordination platform requires balancing development velocity, operational simplicity, and rigorous domain isolation. Distributed architectural patterns (such as microservices) introduce significant operational overhead: distributed transaction management, network latency, multi-repository maintenance, and complex infrastructure orchestration (e.g., service meshes, distributed tracing).

Conversely, an unconstrained monolith often degenerates into a tightly-coupled "big ball of mud," where persistence logic, HTTP transport, and business rules intermingle, hindering automated testing and future refactoring.

We require an architectural blueprint that enforces separation of concerns, guarantees clear domain boundaries, and enables rapid iteration without the premature complexity of distributed systems.

## Decision

We will build the Share Help backend as a **Modular Monolith** organized into a **Layered Architecture** (*Separation of Concerns*).

The codebase is partitioned into explicit operational layers under `src/`:

1. **`api/` (Transport & Presentation Layer):** Handles HTTP contracts, routing, query parameter parsing, and status codes. Dispatches requests to services; contains zero business logic or direct persistence queries.
2. **`schemas/` (Data Transfer Objects - DTOs):** Governed by Pydantic models. Enforces strict input validation, type coercion, and deterministic JSON response serialization.
3. **`services/` (Domain Logic Layer):** Houses the core business rules, transactional orchestrations, state machines, and invariants (e.g., verifying requester status before volunteer dispatch).
4. **`models/` (Persistence Layer):** Contains declarative SQLAlchemy ORM mappings reflecting the PostgreSQL relational schema, including table-level constraints and foreign key relationships.
5. **`core/` (Cross-Cutting Concerns):** Houses global configurations, security configurations, and environment parsers.
6. **`db/` (Database Infrastructure):** Manages connection pooling, engine configurations, and Alembic database version control migrations.

Microservices and fully decoupled event-driven architectures are deferred until operational metrics demonstrate clear domain partitioning and scaling bottlenecks that warrant distributed deployment.

## Consequences

### Positive

- **Operational Simplicity:** Single deployment artifact, straightforward local development setup, and zero network hops between internal domains.
- **Maintainability & Testability:** In-memory testing via pytest with dependency injection; business logic can be tested in complete isolation from the HTTP layer.
- **Clear Domain Boundaries:** Modularity allows future extraction of isolated domains (e.g., matching or dispatch) into dedicated microservices with minimal friction if scalability demands require it.
- **Prevention of Circular Coupling:** Explicit layering prevents cyclic imports and spaghetti dependencies.

### Negative

- **Discipline Overhead:** Requires strict developer adherence to layer boundaries (e.g., never querying the database directly inside an API route).
- **Coupled Deployments:** A failure in one module's deployment affects the entire application runtime.