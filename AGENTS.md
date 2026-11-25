# AGENTS.md — E&M Hub SDAF v1.0 Entrypoint

> **Mandatory Protocol:** Every AI coding agent (Antigravity, Claude Code, Cursor, GitHub Copilot) operating in this repository MUST follow these rules without exception.

---

## 1. Read Context First
Before reading, editing, or generating any code:
1. Read [`.agents/SKILL.md`](.agents/SKILL.md) for stack conventions, directory boundaries, and security guardrails.
2. Read [`.agents/memory.md`](.agents/memory.md) for active architecture decisions and the **Dead-End Ledger** so you never repeat a confirmed failure.

## 2. Spec-First Law (Zero Vibe Coding)
- **No implementation code without an approved specification** in `docs/specs/`.
- Every new feature or bugfix starts by copying [`docs/specs/SPEC_TEMPLATE.md`](docs/specs/SPEC_TEMPLATE.md) into `docs/specs/<TICKET-ID>-<short-name>.md`.
- If a requested change contradicts or extends beyond the linked spec, **stop and ask** before writing code.

## 3. Mandatory Hostile Review Gate
- Before opening any Pull Request / Merge Request, you **MUST** invoke the `hostile-reviewer` subagent (defined in [`.agents/agents/hostile-reviewer.md`](.agents/agents/hostile-reviewer.md)) against your diff and linked spec.
- A PR cannot be opened until `hostile-reviewer` returns **`VERDICT: PASS`** across all 6 pillars.

## 4. Persistent Memory & Dead-End Ledger
- Whenever you encounter a non-obvious bug, environmental quirk, or failed approach, record it immediately in the **Dead-End Ledger** inside [`.agents/memory.md`](.agents/memory.md).
- Log meaningful architectural choices in the **Architecture Decisions Log** in the same file.

## 5. Coverage Ratchet Rule
- **Branch coverage must only go up, never down.**
- Minimum gates per E&M Hub SDAF v1.0:
  - **Whole Repository:** `>= 80%` line coverage, `>= 70%` branch coverage.
  - **Critical Modules** (payments, financial math, auth, tenant isolation) & **New/Changed Code:** `>= 90%` line coverage, `>= 85%` branch coverage.
  - **Legacy Repositories (< 80%):** Baseline is locked; overall coverage ratchets up by `+5%` per sprint and all new/changed code must still meet `>= 90%` line / `>= 85%` branch.
