# 60-Second SDAF v1.0 Bootstrapper Prompt

Copy and paste the prompt below into your coding agent (Antigravity, Claude Code, Cursor, or GitHub Copilot) inside **any existing E&M repository** after copying the SDAF starter files (`AGENTS.md`, `.agents/`, `docs/specs/`, `.github/`).

---

```text
You are onboarding this repository to E&M Technology House Uganda's Spec-Driven Agentic Engineering Framework (SDAF v1.0).

Do NOT modify any application source code or tests yet. Execute these 4 steps only:

1. Inspect the repository layout, dependency manifests (requirements.txt, pyproject.toml, pom.xml, package.json), CI config, and existing test setup.
2. Fill in `.agents/SKILL.md` with the exact Tech Stack, Directory Rules, Security Guardrails, and working Test/Lint Commands for this repository.
3. Initialize `.agents/memory.md` with:
   - The key existing architectural patterns (auth/tenant guard file path, response wrapper, critical financial/auth modules requiring 90% line / 85% branch coverage).
   - The current baseline test coverage if a test suite exists (to lock the Coverage Ratchet floor).
4. Report back with a 5-line readiness summary listing: (a) detected stack, (b) exact test command verified, (c) critical modules identified, and (d) any missing Tier 0 harness pieces (e.g., pre-commit hooks or CI coverage gate).
```
