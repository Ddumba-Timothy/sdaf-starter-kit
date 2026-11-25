# memory.md — Persistent Project Memory & Dead-End Ledger

> **Agent Instruction:** Read this file at the start of every session before writing code. Keep entries concise to preserve context window tokens. Update whenever an architectural decision is made or a non-obvious failure is resolved.

---

## Architecture Decisions Log

| Date | Decision | Rationale | Scope / Owner |
| :--- | :--- | :--- | :--- |
| 2026-11-25 | Adopt E&M Hub SDAF v1.0 harness (`AGENTS.md`, `.agents/`, `docs/specs/`) | Enforce spec-first delivery, 6-point hostile review, and branch coverage ratchet across all AI-assisted tickets. | Repo-wide / QA & Engineering |

---

## Dead-End Ledger (Confirmed Failures — Do Not Retry)

| Date | Attempted Approach | Why It Failed | Rule Going Forward |
| :--- | :--- | :--- | :--- |
| 2026-11-25 | Used Python `float` for UGX unit price × quantity totals in FastAPI Pydantic models | Binary floating-point drift (e.g., `19.99 * 3 = 59.970000000000006`) caused ledger reconciliation mismatches and failed financial audit checks. | Always use `decimal.Decimal` (or exact integer minor units) with `NUMERIC(19,4)` in schemas, models, and calculations. Never use `float` for money. |
