# 3. Select Relational Database Engine (PostgreSQL)

Date: 2026-10-03

## Status

Accepted

## Context

The Share Help platform coordinates critical disaster relief operations requiring strict consistency, relational integrity, and tamper-evident audit trails. The system models complex interactions between multiple actors (victims, donors, volunteers, coordinators) and manages state transitions across different resource lifecycles.

Key requirements influencing data persistence include:

- Strict relational constraints (e.g., matching allocations must reference valid requests and available inventory).
- Atomic transactions (ACID compliance) to prevent over-allocation of scarce supplies during concurrent updates.
- Future support for geospatial queries to compute proximity between assistance requests and available resources.
- Immutable logging for legal compliance, public transparency, and government coordination.

## Decision

We will use **PostgreSQL** as the primary relational database management system.

PostgreSQL satisfies our requirements through:

1. Robust ACID compliance ensuring atomic updates during multi-step resource dispatch workflows.
2. Built-in relational constraints (`FOREIGN KEY`, `NOT NULL`, `CHECK`, unique constraints) safeguarding domain invariants at the storage layer.
3. PostGIS spatial extensions capability, enabling future geographical radius queries without changing database engines.
4. Rich JSON/JSONB support to store dynamic metadata for diverse resource categories alongside strongly typed relational tables.
5. Mature open-source ecosystem, broad tooling support, and transparent zero-cost licensing.

## Consequences

### Positive

- High data integrity and elimination of orphan allocations or partial transaction states.
- Predictable schema migrations and clear entity relationships.
- Seamless path for spatial query integration via PostGIS when implementing geographical matchmaking.

### Negative

- Schema evolution requires planned migrations rather than schema-on-read flexibility.
- Requires standard relational optimization (indexing, connection pooling) under heavy read/write concurrency.
