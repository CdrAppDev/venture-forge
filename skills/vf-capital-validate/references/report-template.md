# Validation Report Template

```markdown
# Validation Report: Capital Thesis

**Project:** [Project Name]
**Date:** [Date]
**Validator:** Claude Code (vf-capital-validate v1.0.0)
**Result:** PASS / FAIL / PASS WITH WARNINGS
**Checks passed:** [X]/38

## 1. File Checks (3 checks)

| # | File | Status |
|---|------|--------|
| 1 | thesis.md | PASS / FAIL |
| 2 | funder-profiles.yaml | PASS / FAIL |
| 3 | processing-log.md | PASS / FAIL |

## 2. Funder Profile Checks (6 checks)

| # | Criterion | Required | Found | Status |
|---|-----------|----------|-------|--------|
| 4 | Total funders analyzed | 2+ | [N] | PASS/FAIL |
| 5 | Viable funders | 2+ | [N] | PASS/FAIL |
| 6 | All funders have required fields | Yes | [Y/N] | PASS/FAIL |
| 7 | No unknown timelines on viable funders | Yes | [N flags] | PASS/WARN |
| 8 | No low-confidence viable without justification | Yes | [Y/N] | PASS/FAIL |
| 9 | All viability rationales non-empty | Yes | [Y/N] | PASS/FAIL |

### Per-Funder Field Completeness

| Funder | Viable | Criteria Cited | Portfolio Cited | Timeline Known | Alignment Documented |
|--------|--------|---------------|-----------------|----------------|---------------------|
| [Name] | Y/N | Y/N | Y/N | Y/N | Y/N |

## 3. Evidence Checks (4 checks)

| # | Category | Required | Found | Status |
|---|----------|----------|-------|--------|
| 10 | Landscape citations | 3+ | [N] | PASS/FAIL |
| 11 | Thesis/criteria citations | 2+ | [N] | PASS/FAIL |
| 12 | Portfolio citations | 3+ | [N] | PASS/FAIL |
| 13 | Requirements citations | 2+ | [N] | PASS/FAIL |

## 4. Thesis Checks (8 checks)

| # | Section | Status |
|---|---------|--------|
| 14 | Executive summary | PASS/FAIL |
| 15 | Funding landscape with citations | PASS/FAIL |
| 16 | Active funding sources table | PASS/FAIL |
| 17 | Funder deep dives (2+) | PASS/FAIL |
| 18 | Alignment strategy | PASS/FAIL |
| 19 | Funding timeline table | PASS/FAIL |
| 20 | Evidence summary | PASS/FAIL |
| 21 | Gate criteria checklist | PASS/FAIL |

## 5. Cross-Validation (4 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 22 | Funder names consistent across files | PASS/FAIL | [List any mismatches] |
| 23 | Viability assessments consistent | PASS/FAIL | [List any mismatches] |
| 24 | Citation counts match actual (±1) | PASS/FAIL | [Claimed: X, Actual: Y] |
| 25 | Alignment gaps consistent | PASS/FAIL | [List any mismatches] |

## 5b. Inline Citation Coverage (2 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 26 | Inline citation density ≥80% | PASS/WARN/FAIL | [N of M factual claims cited (X%)] |
| 27 | Uncited claims inventory | PASS/WARN | [N uncited claims listed below] |

### Uncited Claims (if any)

| # | Claim | Section | Suggested Source |
|---|-------|---------|-----------------|
| [N] | [The uncited factual claim] | [Which section of thesis.md] | [Source from funder-profiles.yaml if available] |

## 6. Timeline Completeness (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 28 | Each viable funder has timeline info | PASS/FAIL | [List any missing] |
| 29 | Timeline table has all viable funders | PASS/FAIL | [List any missing] |
| 30 | Unknown timelines noted in thesis | PASS/FAIL/N/A | [List any unnoted] |

## 7. Sources Validation (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 31 | All sources listed in sources.md | PASS/FAIL | [N sources cited, N listed] |
| 32 | Each source has org, title, date, cited-for | PASS/FAIL | [N complete, N incomplete] |
| 33 | Sources organized by category | PASS/FAIL | [Y/N] |

## 8. URL Verification (2 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 34 | URLs formatted correctly | PASS/FAIL | [N valid, N malformed] |
| 35 | Error URLs flagged | PASS/FAIL | [Y/N] |

## 9. Processing Log Checks (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 36 | All research files listed | PASS/FAIL | [Expected: N, Found: N] |
| 37 | Excluded evidence documented | PASS/FAIL | [Section present: Y/N] |
| 38 | Conflicts documented | PASS/FAIL | [Section present: Y/N] |

## Warnings

[List any WARNING items — these don't block gate review but should be noted]

## Failures

[List each FAIL with:
- Check number and name
- What was expected
- What was found
- Specific remediation needed]

## Evidence Briefing

### What the Evidence Shows

[Auto-generated summary of key numbers from thesis.md and funder-profiles.yaml:]
- **Funders analyzed:** [N]
- **Viable funders:** [N] (of [N] analyzed)
- **Total citations:** [N] across [N] unique sources
- **Inline citation coverage:** [X]% ([N] of [M] factual claims cited)
- **Validation result:** [X]/38 checks passed, [N] warnings, [N] failures

### What's Strong

[List 3-5 strengths drawn from the data. These are things the evidence clearly supports:]
- [Strength 1 — specific, with data point. e.g., "Multiple funding tracks available (federal grants + state programs + VC), reducing single-source dependency"]
- [Strength 2]
- [Strength 3]

### What's Weak or Unresolved

[List all weaknesses, gaps, and unknowns. Be direct:]
- [Weakness 1 — specific, with data point. e.g., "7 of 12 viable funders are VC with unknown application timelines"]
- [Weakness 2]
- [Any validation warnings or failures]

### Gate Decisions

#### Blocking Decisions
[These must be resolved before the next phase can start.]

**Decision 1: [Question]** `BLOCKING`
- **Proceed** → [What happens next. e.g., "Starts Phase 02 Problem Thesis — research validates whether [specific problem] is real, documented, and severe enough to build for."]
- **Revise** → [What gets redone. e.g., "Re-runs capital research targeting [specific gap]. Estimated rework: re-process with expanded funder criteria."]
- **Kill** → [What this means. e.g., "Archives CyberShield Rural. Capital thesis data preserved in phases/01-capital/ for reference."]

#### Strategic Decisions
[These inform strategy but do not block the next phase. They can be deferred — later phases will produce data that makes these choices clearer.]

**Decision 2: [Question]** `STRATEGIC — revisit after Phase [NN]`
[State which future phase produces relevant data for this decision.]
- **Option A** → [Concrete consequence]
- **Option B** → [Concrete consequence]
- **Option C** → [Concrete consequence]

[Repeat for each pending decision]

## Recommendation

**READY FOR GATE REVIEW** / **READY FOR GATE REVIEW WITH WARNINGS** / **NEEDS REVISION: [specific items]**

Checks completed: [X]/38
Checks passed: [X]/38
Checks failed: [X]/38
Warnings: [X]/38
```
