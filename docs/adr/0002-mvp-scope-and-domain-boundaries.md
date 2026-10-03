# 2. Define MVP Scope and Domain Boundaries

Date: 2026-10-02

## Status

Accepted

## Context

During major natural disasters, resource matching and volunteer dispatching suffer from fragmented communication and lack of real-time visibility. While governmental agencies operate macro-level emergency alert systems (e.g., NOAA, FEMA WEA), local communities often struggle to connect real-time demand (victims) with distributed supply (community resources, specialized labor, and private fleet assets).

Attempting to implement complex social media scraping algorithms and complete physical warehouse operations in the initial MVP would expand scope excessively without solving the immediate bottleneck: reliable coordination, accountability, and auditability.

## Decision

We will constrain the MVP to a core **Resource Allocation and Coordination Engine** prioritizing:

1. Assistance request submission with geolocation and severity triage.
2. Resource cataloging across consumables, reusable equipment, volunteer services, and audited financial pledges.
3. Coordinator-driven matching mechanisms connecting requests and pledges.
4. An immutable audit trail for external reporting, public transparency, and multi-agency coordination.
5. Cross-platform accessibility via a responsive web client with accessible UI standards (WCAG, light/dark themes, colorblind support).

Social media web-scraping and physical warehouse custody management are explicitly excluded from the MVP scope.

## Consequences

### Positive

- Accelerated delivery of the core relational data model and critical business invariants.
- High focus on data integrity, state machines, and relational constraints.
- Clear separation between the civic coordination software and external emergency agency duties.
- High accessibility across desktop and mobile browsers without requiring native platform-specific builds.

### Negative

- Direct integrations with live weather APIs and multi-agency broadcast systems are deferred to subsequent development phases.
- Real-time social media signal harvesting is omitted in favor of direct user-submitted requests.
