## Linked Specification (Required)
- **Spec File:** `docs/specs/TICKET-ID-short-name.md`
- **Summary of Changes:** <!-- 2–3 bullet points matching the approved spec -->

---

## 6-Point Hostile Review (`hostile-reviewer` Verdict: PASS)
- [ ] **1. Security & Auth / IDOR:** All reads/writes are strictly scoped to the authenticated user's `tenant_id` / `user_id`; zero hardcoded secrets.
- [ ] **2. Financial & Data Integrity:** All currency, rate, fee, and score fields use `Decimal` / `BigDecimal` / `NUMERIC(19,4)` (zero `float`/`double`).
- [ ] **3. Edge Cases & Nulls:** Boundary, zero, negative, and null inputs are validated; list endpoints are paginated (`?page=1&limit=20`).
- [ ] **4. Concurrency & Idempotency:** State-changing endpoints are protected against duplicate retries (`Idempotency-Key` and/or row locks).
- [ ] **5. Safe Error Handling:** Deterministic error codes returned without leaking SQL queries, stack traces, or internal paths.
- [ ] **6. Scope & Schema Sync:** Changes strictly match the linked spec; any DB migration includes a matching `/docs/data-schema/` update.

---

## Coverage Ratchet & Memory Compliance
- [ ] **Coverage Ratchet:** Branch coverage did not decrease (`>= 80%` line / `>= 70%` branch overall; `>= 90%` line / `>= 85%` branch on critical modules & new/changed code).
  - *Measured Line Coverage:* `___%` | *Measured Branch Coverage:* `___%`
- [ ] **Memory Updated:** `.agents/memory.md` updated with any new architecture decisions and any failed approaches in the **Dead-End Ledger**.
