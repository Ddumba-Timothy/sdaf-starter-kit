# SKILL.md — Repository Engineering & QA Guardrails

> Customize the bracketed sections (`[...]`) during onboarding using [`.agents/prompts/bootstrap.md`](prompts/bootstrap.md).

---

## 1. Tech Stack
- **Language & Runtime:** `[e.g., Python 3.11+ | Java 21 | TypeScript 5.x]`
- **Framework:** `[e.g., FastAPI + Pydantic v2 | Spring Boot 3.x | React + Vite | Angular 18]`
- **Database & Migrations:** `[e.g., PostgreSQL 16 + Alembic / Flyway]`
- **Test Runner:** `[e.g., pytest + pytest-cov + httpx | JUnit 5 | Vitest + Playwright]`

---

## 2. Directory Rules
Follow E&M Hub Development Standards (Section 15):
- `docs/specs/` — Approved feature and bugfix specifications (`*.md`).
- `docs/data-schema/` — Living database schema documentation (must stay in sync with migrations).
- `migrations/` — Versioned database migrations only; never mutate production schemas manually.
- Application code follows strict layer separation:
  - **Python (FastAPI):** `app/api/` (thin routers), `app/services/` (business logic), `app/models/` (DB entities), `app/schemas/` (Pydantic DTOs), `tests/`.
  - **Java (Spring Boot):** `controller/`, `service/`, `repository/`, `entity/`, `dto/`, `config/`.
  - **Frontend (React / Angular):** Strict TypeScript (`any` disallowed), typed API clients, schema-validated forms.
- Keep functions small (`< 40 lines`), single-responsibility, and free of dead code or `TODO` stubs.

---

## 3. Security Guardrails (Non-Negotiable)
1. **Zero Hardcoded Secrets:** Never commit API keys, tokens, passwords, or connection strings. Load all secrets from `.env` (local) or Secrets Manager (prod).
2. **Strict Tenant & Ownership Isolation (IDOR Defense):** Every read and write MUST be scoped to the authenticated user's `tenant_id` / `user_id` derived from a verified auth token or session header — **never** trust a `tenant_id` supplied in the request body or URL alone.
3. **Exact Financial & Precision Math:** Always use `Decimal` / `BigDecimal` / `NUMERIC(19,4)` (or exact integer minor units) for currency, fees, interest rates, and scores. **Never use `float` or `double`.**
4. **Concurrency & Idempotency:** Protect state-changing `POST`/`PUT` financial or workflow endpoints against duplicate retries using `Idempotency-Key` headers and/or row-level locks (`SELECT ... FOR UPDATE`).
5. **Safe Error Handling:** Return clean, deterministic error envelopes with a `request_id`. Never leak SQL queries, stack traces, or internal file paths.
6. **AI Supply-Chain Hygiene:** Use only E&M-approved Tier 1 endpoints for proprietary code/specs. Never route Hub code through unvetted third-party proxy routers.

---

## 4. Test & Verification Commands
```bash
# Run unit & API tests with line + branch coverage (Python example)
pytest --cov=app --cov-branch --cov-report=term-missing

# Lint & format check
ruff check . && ruff format --check .

# Pre-commit security & quality gates
pre-commit run --all-files
```
