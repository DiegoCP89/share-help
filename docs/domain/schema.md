# Database Entity-Relationship Model (ERD)

## Overview

This schema documents the relational persistence model for the Share Help platform, enforcing domain invariants, RBAC boundaries, state-machine tracking, and audit trails.

```mermaid
erDiagram
    USERS ||--o{ RESOURCES : "registers/donates"
    USERS ||--o{ ASSISTANCE_REQUESTS : "submits"
    USERS ||--o{ ALLOCATIONS : "authorizes"
    USERS ||--o{ AUDIT_LOGS : "triggers"

    ASSISTANCE_REQUESTS ||--o{ ALLOCATIONS : "fulfilled_by"
    RESOURCES ||--o{ ALLOCATIONS : "assigned_to"

    USERS {
        uuid id PK
        string full_name
        string email UK
        string phone_number
        string role "VICTIM | DONOR | VOLUNTEER | COORDINATOR | AUDITOR"
        boolean is_active
        timestamp created_at
        timestamp updated_at
    }

    RESOURCES {
        uuid id PK
        uuid donor_id FK
        string category "CONSUMABLE | ASSET | VOLUNTEER_LABOR | FINANCIAL"
        string item_name
        decimal total_quantity
        decimal available_quantity
        string unit_of_measure
        string status "AVAILABLE | ALLOCATED | DISPATCHED | COMPLETED | RETIRED"
        decimal latitude
        decimal longitude
        text location_description
        timestamp created_at
        timestamp updated_at
    }

    ASSISTANCE_REQUESTS {
        uuid id PK
        uuid requester_id FK
        string priority "LOW | MEDIUM | HIGH | CRITICAL"
        string status "PENDING | IN_PROGRESS | FULFILLED | CANCELLED"
        integer people_count
        boolean medical_assistance_required
        text situation_details
        decimal latitude
        decimal longitude
        text address_reference
        timestamp created_at
        timestamp updated_at
    }

    ALLOCATIONS {
        uuid id PK
        uuid request_id FK
        uuid resource_id FK
        uuid coordinator_id FK
        decimal allocated_quantity
        string status "PENDING | IN_TRANSIT | DELIVERED | CANCELLED"
        text dispatch_notes
        timestamp created_at
        timestamp updated_at
    }

    AUDIT_LOGS {
        uuid id PK
        uuid actor_id FK
        string target_entity
        uuid target_entity_id
        string action "CREATE | UPDATE | STATE_TRANSITION | DELETE"
        jsonb previous_state
        jsonb new_state
        timestamp recorded_at
    }
```
