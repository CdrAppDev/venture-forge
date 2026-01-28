# Validation Report Template

```markdown
# Validation Report: Problem Thesis

**Project:** [Project Name]
**Date:** [Date]
**Validator:** Claude Code (vf-problem-validate v1.0.0)
**Result:** PASS / FAIL / PASS WITH WARNINGS
**Checks passed:** [X]/27

## 1. File Checks (4 checks)

| # | File | Status |
|---|------|--------|
| 1 | thesis.md | PASS / FAIL |
| 2 | evidence.yaml | PASS / FAIL |
| 3 | customer-voice.md | PASS / FAIL |
| 4 | processing-log.md | PASS / FAIL |

## 2. Evidence Checks (7 checks)

| # | Criterion | Required | Found | Status |
|---|-----------|----------|-------|--------|
| 5 | Problem statement present | Yes | [Y/N] | PASS/FAIL |
| 6 | Prevalence statistics | 3+ (with source, date) | [N] | PASS/FAIL |
| 7 | Severity statistics | 3+ (with source, date) | [N] | PASS/FAIL |
| 8 | Cost of status quo statistics | 2+ | [N] | PASS/FAIL |
| 9 | Current solutions | 1+ | [N] | PASS/FAIL |
| 10 | Gaps identified | 1+ | [N] | PASS/FAIL |
| 11 | Capital alignment set to true | Yes | [Y/N] | PASS/FAIL |

### Invalid Evidence Entries (not counted toward minimums)

| # | Entry | Issue |
|---|-------|-------|
| [N] | [Description] | [Missing source / Empty source / Missing date] |

## 3. Customer Voice Checks (4 checks)

| # | Criterion | Required | Found | Status |
|---|-----------|----------|-------|--------|
| 12 | Direct quotes with source attribution | 5+ | [N valid] | PASS/FAIL |
| 13 | Distinct themes identified | 2+ | [N] | PASS/FAIL |
| 14 | Terminology section present and non-empty | Yes | [Y/N] | PASS/FAIL |
| 15 | Workarounds section present and non-empty | Yes | [Y/N] | PASS/FAIL |

### Invalid Quotes (not counted toward minimum)

| # | Quote excerpt | Issue |
|---|-------------|-------|
| [N] | "[First few words...]" | [Missing source / Missing date / No attribution] |

## 4. Thesis Checks (6 checks)

| # | Section | Status |
|---|---------|--------|
| 16 | Problem statement with content | PASS/FAIL |
| 17 | Key statistics table with source column | PASS/FAIL |
| 18 | Customer voice section with quote(s) | PASS/FAIL |
| 19 | Capital alignment section | PASS/FAIL |
| 20 | Evidence summary with citation counts | PASS/FAIL |
| 21 | Gate criteria checklist | PASS/FAIL |

## 5. Cross-Validation (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 22 | Problem statement matches evidence.yaml | PASS/FAIL | [Match / Mismatch description] |
| 23 | Statistics in thesis appear in evidence.yaml | PASS/FAIL | [N matched, N untracked] |
| 24 | Quotes in thesis appear in customer-voice.md | PASS/FAIL | [N matched, N untracked] |

## 6. Processing Log Checks (3 checks)

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 25 | All research files listed | PASS/FAIL | [Expected: N, Found: N] |
| 26 | Excluded evidence documented | PASS/FAIL | [Section present: Y/N] |
| 27 | Conflicts documented | PASS/FAIL | [Section present: Y/N] |

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

Checks completed: [X]/27
Checks passed: [X]/27
Checks failed: [X]/27
Warnings: [X]/27
```
