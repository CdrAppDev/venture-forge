# Gate Review Record Template

```markdown
# Gate Review Record: {Phase Name}

**Project:** {Project Name}
**Date:** {YYYY-MM-DD}
**Phase:** {phase_id}
**Reviewer:** Human (via Claude Code)
**Validator:** vf-gate-review v1.0.0
**Decision:** PROCEED / REVISE / KILL

---

## Pre-Review Auto-Fixes

**Auto-fixes applied:** {N}

| # | File | Change | Old Value | New Value | Triggered By |
|---|------|--------|-----------|-----------|-------------|
| [N] | [file path] | [what changed] | [old] | [new] | [check #N] |

[If no auto-fixes: "No mechanical issues identified. Validation report presented as-is."]

## Validation Summary (Post-Fix)

- **Checks completed:** {X}/{Y}
- **Checks passed:** {X}/{Y}
- **Warnings:** {N}
- **Failures:** {N}
- **Verdict:** READY FOR GATE REVIEW / READY WITH WARNINGS / NEEDS REVISION

[If re-validation was run after auto-fixes, note: "Re-validated after {N} auto-fixes. Previous result: {old}. Current result: {new}."]

## Blocking Decisions

| # | Question | Choice | Consequence | Notes |
|---|----------|--------|-------------|-------|
| 1 | {gate.question from phase YAML} | Proceed / Revise / Kill | {outcome description} | {human's notes} |

## Strategic Decisions

| # | Decision | Status | Revisit After | Notes |
|---|----------|--------|---------------|-------|
| [N] | [decision text] | Decided / Deferred | Phase {NN} | [human's notes or "deferred"] |

## Revision Scope

[Only present if decision is REVISE]

**Items requiring revision:**
- [specific item 1 from validation report]
- [specific item 2]
- [human's additional notes]

**Revision target:** Re-run processing with focus on [specific gaps].

## Archive Notes

[Only present if decision is KILL]

{Human's notes on why the project is being archived and any learnings to preserve.}

---

**Next action:**
- If PROCEED: Phase {next_phase_id} ({next_phase_name}) is now pending. Run `vf-{next_phase}-generate-prompts` to start.
- If REVISE: Phase {phase_id} is back in processing. Address revision items and re-run `vf-{phase}-process-research`.
- If KILL: Project archived. Phase outputs preserved at `{project}/phases/{phase_id}/`.
```
