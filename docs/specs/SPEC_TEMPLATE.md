# Spec: [TICKET-ID] [Feature Name]

- **Branch:** `feature/TICKET-ID-short-description` (or `bugfix/` / `hotfix/`)
- **Author:** `[Full Name <email@emtechhouse.com>]`
- **Module Criticality:** `[Standard: 80% line / 70% branch | Critical Core/Financial/Auth: 90% line / 85% branch]`
- **Status:** `DRAFT | APPROVED`

---

## Risk Profile (Auto-Evaluated by Agent)
*Agent Instruction: Automatically evaluate and pre-check all applicable boxes below when drafting a spec from this template so the developer only needs to review and approve.*

- [ ] **Financial / Ledger:** Touches pricing, balances, tax, invoicing or monetary math
- [ ] **Auth / Multi-Tenant:** Touches login, roles, permissions or tenant-scoped data
- [ ] **Concurrency / Async:** Touches queues, webhooks, background jobs or retries

---

## 1. Problem
Briefly state the business or operational problem being solved, who is affected, and the measurable outcome.

## 2. Data Schema
List affected tables/models (`snake_case`), exact column types (`NUMERIC(19,4)` / `Decimal` for monetary or precision fields — never `float`), constraints (`PK`, `FK`, `NOT NULL`, `UNIQUE`), and required migration + `/docs/data-schema/` updates.

## 3. API Contract
- **Endpoint:** `[METHOD] /api/v1/[resource]`
- **Auth & Tenant Scope:** `[e.g., Authenticated session / Bearer JWT — tenant_id derived strictly from auth context]`
- **Request Headers & Body:**
  ```json
  {
    "idempotency_key": "uuid-v4"
  }
  ```
- **Success Response (`200 OK` / `201 Created`):**
  ```json
  {
    "status": "success",
    "data": {}
  }
  ```
- **Error Responses (`400`, `401`, `403`, `404`, `409`, `422`):**
  ```json
  {
    "status": "error",
    "error_code": "DOMAIN_ERROR_CODE",
    "message": "Safe client-facing message"
  }
  ```

## 4. Security & Edge Cases
- **Tenant Isolation (IDOR):** How cross-tenant access is prevented and tested.
- **Precision & Boundaries:** Zero/negative values, max lengths, null fields, exact `Decimal` math.
- **Concurrency & Idempotency:** Behavior on duplicate/concurrent retries.
- **Out of Scope:** Files or modules that MUST NOT be modified.

## 5. Acceptance Criteria
- **AC-1 (Happy Path):** Given ..., When ..., Then ...
- **AC-2 (Validation / Boundary):** Given ..., When ..., Then ...
- **AC-3 (Security / IDOR):** Given ..., When ..., Then ...
- **AC-4 (Idempotency / Concurrency):** Given ..., When ..., Then ...
