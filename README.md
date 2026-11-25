# E&M Hub — SDAF v1.0 Starter Kit

**Spec-Driven Agentic Engineering Framework (SDAF v1.0)** by E&M Technology House Uganda.

90% of an AI coding agent's reliability comes from the **harness** wrapped around it—not the model. This starter kit drops directly into any repository to enforce spec-first development, 6-point hostile code review, persistent project memory, and a branch-coverage ratchet.

---

## Adopt SDAF v1.0 in 60 Seconds

### 1. Copy the harness into your repository root
```text
your-repo/
├── AGENTS.md                          # Root agent entrypoint & non-negotiable laws
├── .agents/
│   ├── SKILL.md                       # Stack rules, directory layout & security guardrails
│   ├── memory.md                      # Architecture Decisions Log & Dead-End Ledger
│   ├── agents/
│   │   └── hostile-reviewer.md        # 6-Point Hostile Review subagent
│   └── prompts/
│       └── bootstrap.md               # 60-second repo onboarding prompt
├── docs/
│   └── specs/
│       └── SPEC_TEMPLATE.md           # Mandatory feature/bugfix spec contract
└── .github/
    └── pull_request_template.md       # Enforces spec link, 6-point review & coverage ratchet
```

### 2. Paste the 60-Second Bootstrapper Prompt
Open your coding agent (Antigravity, Claude Code, Cursor, or GitHub Copilot) and paste:

```text
You are onboarding this repository to E&M Technology House Uganda's Spec-Driven Agentic Engineering Framework (SDAF v1.0).

Do NOT modify any application source code or tests yet. Execute these 5 steps only:

1. Harness Setup (Idempotent): Check if `AGENTS.md`, `.agents/`, `.github/pull_request_template.md` and `docs/specs/SPEC_TEMPLATE.md` already exist in this repository. If any are missing, fetch them from `https://github.com/Ddumba-Timothy/sdaf-starter-kit` (ignore the `/demo` folder and do not overwrite existing custom files).
2. Repository Audit: Inspect the repository layout, dependency manifests (`requirements.txt`, `pyproject.toml`, `pom.xml`, `package.json`), CI config and existing test setup.
3. Populate `.agents/SKILL.md`: Fill in the exact Tech Stack, Directory Rules, concrete Security Guardrails (no generic fluff) and working Test/Lint Commands. Verify every test/lint command actually runs cleanly in this environment before writing it down.
4. Initialize `.agents/memory.md`: Document:
   - Key existing architectural patterns (auth/tenant guard file path, response wrapper and critical financial/auth modules requiring 90% line / 85% branch coverage).
   - The current baseline test coverage if a test suite exists (to lock the Coverage Ratchet floor).
5. Report Back: Output a 5-line readiness summary listing: (a) detected stack, (b) exact test command verified, (c) critical modules identified, (d) baseline coverage floor and (e) any missing Tier 0 harness pieces (e.g., pre-commit hooks or CI coverage gate).

## The 5-Step SDAF Loop

```text

[1. Spec] → [2. Plan + Hostile Review] → [3. Tests] → [4. Build + Memory] → [5. PR Gate]
```
**CLI One-Liners**
Windows (Powershell);
```text
irm https://raw.githubusercontent.com/Ddumba-Timothy/sdaf-starter-kit/main/install.ps1 | iex
```

Mac/Linux;
```text
curl -sL https://raw.githubusercontent.com/Ddumba-Timothy/sdaf-starter-kit/main/install.sh | bash
```

| Gate | Requirement |
| :--- | :--- |
| **Spec-First** | Zero implementation code without an approved spec in `docs/specs/`. |
| **Hostile Review** | Run `hostile-reviewer` before every PR (`PASS` required across all 6 pillars). |
| **Dead-End Ledger** | Log failed approaches in `.agents/memory.md` so agents never repeat mistakes. |
| **Coverage Ratchet** | Branch coverage only goes up (`>= 80%/70%` overall; `>= 90%/85%` on critical & new code). |

---

## Live Demo (`/demo`)

The [`demo/`](demo/) directory contains a minimal Python 3.11+ FastAPI microservice paired with [`docs/specs/001-record-sale.md`](docs/specs/001-record-sale.md). It is pre-seeded with two realistic "vibe-coded" defects (floating-point currency math and a cross-tenant IDOR vulnerability) designed to showcase `hostile-reviewer` catching bugs before merge.

```bash
cd demo
pip install -r requirements.txt
uvicorn app:app --reload
```
