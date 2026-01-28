# Validation Report Template

```markdown
# Validation Report: Capital Thesis

**Project:** [Project Name]
**Date:** [Date]
**Validator:** Claude Code (vf-capital-validate v1.0.0)
**Result:** PASS / FAIL / PASS WITH WARNINGS
**Checks passed:** [X]/31

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

## 6. Timeline Completeness (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 26 | Each viable funder has timeline info | PASS/FAIL | [List any missing] |
| 27 | Timeline table has all viable funders | PASS/FAIL | [List any missing] |
| 28 | Unknown timelines noted in thesis | PASS/FAIL/N/A | [List any unnoted] |

## 7. Processing Log Checks (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 29 | All research files listed | PASS/FAIL | [Expected: N, Found: N] |
| 30 | Excluded evidence documented | PASS/FAIL | [Section present: Y/N] |
| 31 | Conflicts documented | PASS/FAIL | [Section present: Y/N] |

## Warnings

[List any WARNING items — these don't block gate review but should be noted]

## Failures

[List each FAIL with:
- Check number and name
- What was expected
- What was found
- Specific remediation needed]

## Recommendation

**READY FOR GATE REVIEW** / **READY FOR GATE REVIEW WITH WARNINGS** / **NEEDS REVISION: [specific items]**

Checks completed: [X]/31
Checks passed: [X]/31
Checks failed: [X]/31
Warnings: [X]/31
```
