# Spec: 001 Record Shop Sale (UGX)

- **Branch:** `feature/001-record-sale`
- **Author:** `Timothy Ddumba <timothy.ddumba@emtechhouse.com>`
- **Module Criticality:** `Critical Financial / Auth (90% line / 85% branch coverage)`
- **Status:** `APPROVED`

---

## Risk Profile (Auto-Evaluated by Agent)
*Agent Instruction: Automatically evaluate and pre-check all applicable boxes below when drafting a spec from this template so the developer only needs to review and approve.*

- [x] **Financial / Ledger:** Touches pricing, balances, tax, invoicing or monetary math
- [x] **Auth / Multi-Tenant:** Touches login, roles, permissions or tenant-scoped data
- [ ] **Concurrency / Async:** Touches queues, webhooks, background jobs or retries

---

## 1. Problem
Multi-tenant retail shops on the E&M platform need a reliable API endpoint to record point-of-sale transactions in Ugandan Shillings (UGX). Every sale must be strictly isolated to the authenticated shop tenant and computed with exact arithmetic so end-of-day cash reconciliation never drifts.

## 2. Data Schema
Table / Record: `sales`

| Column | Type | Constraints |
| :--- | :--- | :--- |
| `sale_id` | `UUID` (string) | `PRIMARY KEY`, server-generated |
| `tenant_id` | `VARCHAR(64)` | `NOT NULL`, indexed, strictly derived from / verified against authenticated session |
| `item_sku` | `VARCHAR(64)` | `NOT NULL`, non-empty |
| `quantity` | `INTEGER` | `NOT NULL`, `> 0` |
| `unit_price_ugx` | `NUMERIC(19,4)` / `Decimal` | `NOT NULL`, `> 0` — **NEVER `float`** |
| `total_amount_ugx` | `NUMERIC(19,4)` / `Decimal` | `NOT NULL`, exact `Decimal(quantity) * unit_price_ugx` |
| `currency` | `CHAR(3)` | `NOT NULL`, fixed `"UGX"` |
| `recorded_at` | `TIMESTAMPTZ` | `NOT NULL`, UTC ISO-8601 |

## 3. API Contract
- **Endpoint:** `POST /sales`
- **Authentication & Tenant Header (Required):**
  - `X-Tenant-ID`: Authenticated shop tenant identifier injected by the API gateway / session middleware.
- **Request Body:**
  ```json
  {
    "tenant_id": "shop-kampala-01",
    "item_sku": "SUGAR-1KG",
    "quantity": 3,
    "unit_price_ugx": "4500.50"
  }
  ```
- **Success Response (`201 Created`):**
  ```json
  {
    "status": "success",
    "data": {
      "sale_id": "a1b2c3d4-...",
      "tenant_id": "shop-kampala-01",
      "item_sku": "SUGAR-1KG",
      "quantity": 3,
      "unit_price_ugx": "4500.50",
      "total_amount_ugx": "13501.50",
      "currency": "UGX",
      "recorded_at": "2026-11-25T08:00:00Z"
    }
  }
  ```
- **Error Responses:**
  - `401 Unauthorized` — Missing or blank `X-Tenant-ID` session header.
  - `403 Forbidden` — `tenant_id` in request body does not match the authenticated `X-Tenant-ID` session header (IDOR attempt).
  - `422 Unprocessable Entity` — Invalid `quantity <= 0`, `unit_price_ugx <= 0`, or blank `item_sku`.

## 4. Security & Edge Cases
- **Strict Tenant Isolation (IDOR Defense):** Never blindly persist `tenant_id` from the request body. The authenticated `X-Tenant-ID` header is mandatory; if the body supplies a different `tenant_id`, reject immediately with `403 Forbidden`.
- **Exact Monetary Arithmetic:** All price and total calculations MUST use `decimal.Decimal` (or exact integer minor units). Using `float` is strictly prohibited.
- **Boundary Validation:** Reject `quantity <= 0`, `unit_price_ugx <= 0`, and whitespace-only `item_sku`.
- **Out of Scope:** Inventory stock deduction and payment gateway settlement.

## 5. Acceptance Criteria
- **AC-1 (Happy Path):** Given a valid `X-Tenant-ID` header matching the payload `tenant_id`, `quantity = 3`, and `unit_price_ugx = Decimal("4500.50")`, When `POST /sales` is called, Then the API returns `201 Created` with exact `total_amount_ugx = "13501.50"` and `currency = "UGX"`.
- **AC-2 (Tenant Isolation / IDOR):** Given `X-Tenant-ID: shop-kampala-01` and payload `tenant_id: "shop-entebbe-99"`, When `POST /sales` is called, Then the API rejects the request with `403 Forbidden` and persists nothing.
- **AC-3 (Missing Auth Header):** Given no `X-Tenant-ID` header, When `POST /sales` is called, Then the API returns `401 Unauthorized`.
- **AC-4 (Numeric Precision):** Given `quantity = 3` and `unit_price_ugx = Decimal("19.99")`, When `POST /sales` is called, Then `total_amount_ugx` is exact `"59.97"` with zero floating-point drift.
- **AC-5 (Boundary Validation):** Given `quantity <= 0` or `unit_price_ugx <= 0`, When `POST /sales` is called, Then the API returns `422 Unprocessable Entity`.
