# CLAUDE.md – Project Rules for Claude Code

This file defines mandatory rules and expectations for all automated changes.
Claude must follow these instructions exactly.

---

## HARD RULES (must always follow)

- Do NOT modify files outside the scope of the current task or issue
- Never remove or weaken existing test coverage
- Never commit secrets, tokens, or credentials
- Never disable tests to make CI pass
- Do not refactor unrelated code
- Do not change public APIs unless explicitly requested

---

## PROJECT CONTEXT

- Primary language: Python
- Test framework: pytest
- Browser automation: Playwright
- CI runs on every PR

---

## CODING STANDARDS

- Follow PEP8
- Prefer explicit, readable code over clever optimizations
- Use type hints where reasonable
- Avoid global state
- Keep functions small and focused

---

## TESTING RULES

- All new functionality must include tests
- Update existing tests only if behavior changes intentionally
- Never remove assertions without replacing them
- Tests must be deterministic (no sleeps, random values, or timing hacks)

---

## FORMATTING & LINTING

- Format Python using `black`
- Lint using `ruff`
- Do not commit code that fails formatting or linting

---

## GIT & PR RULES

- Use clear, descriptive commit messages
- One logical change per commit
- PR descriptions must include:
  - What was changed
  - Why it was changed
  - How it was tested
- Avoid unnecessary comments in PRs
- Always leave a summary comment when explicitly asked
- If the PR complies with all rules, explicitly state "No issues found"
- Do not acknowledge reviews silently when directly prompted

---

## WHAT TO DO WHEN UNSURE

- Ask for clarification instead of making assumptions
- Prefer minimal, reversible changes
- Document tradeoffs in the PR description if needed

---

## OUTPUT EXPECTATIONS

- Favor correctness over speed
- Minimize noise
- Be precise and factual
