# Product Requirements & Domain Rules

## 1. Overview

**Share Help** is an open-source, non-profit tech platform designed to coordinate disaster relief operations. It connects affected populations, donors, community volunteers, and coordinating authorities during natural disasters (e.g., hurricanes, severe flooding).

The platform functions as an operational bridge and resource matchmaking engine rather than a physical warehousing or logistics intermediary.

---

## 2. User Roles & Personas (RBAC)

1. **Victim / Requester**
   - Individual or community representative affected by a disaster.
   - Submits assistance requests specifying immediate needs, severity triage, and location.
   - Held accountable for the accuracy of declared information.
2. **Donor**
   - Individual or legal entity offering consumable items or financial aid.
   - Mandatory identity verification (no anonymous donations permitted).
   - Can choose whether donation visibility is public or private.
3. **Volunteer**
   - Individual or legal entity offering time, specialized labor, heavy equipment, or transport vehicles.
   - Registers availability, skills (e.g., rescue, medical aid, debris removal), and equipment capacity.
4. **Coordinator / Official**
   - A public or private authority, or a platform moderator.
   - Validates requests, prioritizes triage, dispatches volunteers/assets, and reviews allocations.
5. **Auditor / Public**
   - Read-only access to transparent public metrics, financial balances, and public records.

---

## 3. Core Resource Taxonomies & Lifecycles

Resources are managed through explicit finite state machines:

1. **Consumable Goods** (e.g., bottled water, non-perishable food, hygiene items, medical supplies)
   - Lifecycle: `Available` → `Allocated` → `Delivered/Depleted`
2. **Reusable Assets & Heavy Equipment** (e.g., boats, trucks, generators, chainsaws)
   - Lifecycle: `Available` → `Dispatched` → `In Use` → `Returned/Decommissioned`
3. **Volunteer Services** (e.g., medical support, debris removal, supply transit)
   - Lifecycle: `Registered` → `Assigned` → `Completed`
4. **Financial Contributions** (e.g., relief funds)
   - Lifecycle: `Pledged` → `Processed` → `Disbursed/Audited`

---

## 4. Fundamental Business Rules (Invariants)

- **BR-001 (Mutual Exclusion During Active Crisis):** An individual cannot be concurrently dispatched as an active field volunteer if they have an open, unfulfilled emergency rescue request in the same crisis area.
- **BR-002 (N:M Allocation Mapping):** A single assistance request can be fulfilled by multiple distinct resource pledges. Conversely, a bulk resource donation can be fractionally allocated across multiple requests.
- **BR-003 (Audit):** Every state transition, record edit, and deletion must generate an append-only audit record capturing timestamp, actor ID, affected entities, and metadata.
- **BR-004 (Decentralized Physical Custody):** The platform coordinates, reserves, and verifies hand-offs but does not operate physical storage facilities. Donors, volunteers, and coordinators execute hand-offs upon coordinator approval.
- **BR-005 (Mandatory Identification & Compliance):** Anonymous donations and unverified registrations are rejected. Users agree during registration that data and proof of fund legitimacy may be shared with state and federal authorities upon legal inquiry.
- **BR-006 (Public Transparency):** Aggregated balances of financial donations and anonymized impact metrics are accessible publicly without authentication.
- **BR-007 (Data Isolation & Privacy):** Sensitive personal information, exact victim addresses, and private contact records are strictly isolated. Users can only inspect and manage their own profiles and designated operational tasks.

---

## 5. Non-Functional Requirements (NFRs)

- **NFR-001 (Cross-Platform Responsive Web):** The application must be delivered as a responsive web application (SPA/PWA) fully compatible with desktop environments (Windows 10+, modern Linux distributions) and mobile platforms (Android, iOS).
- **NFR-002 (Availability & Architecture):** Architected for 24/7 high availability, built on an open-source technology stack, and released under an open-source license.
- **NFR-003 (Accessibility - a11y):** The user interface must support high-contrast light/dark themes, adjustable font sizing, and colorblind-accessible palettes in compliance with WCAG guidelines.
- **NFR-004 (Authentication & Security):** User accounts must support Multi-Factor Authentication (MFA), secure password resets via time-limited tokens, and robust role-based access control (RBAC).
- **NFR-005 (Operational Scope Disclaimers):** Clear operational disclaimers must state that platform maintainers facilitate coordination but do not guarantee donor resource provenance or physical fulfillment execution.
