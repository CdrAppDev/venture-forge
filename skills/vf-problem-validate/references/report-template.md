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

## Evidence Briefing

### What the Evidence Shows

[Auto-generated summary of key numbers from thesis.md and evidence.yaml:]
- **Problem statement:** [One sentence from evidence.yaml]
- **Prevalence statistics:** [N] cited
- **Severity statistics:** [N] cited
- **Customer voice quotes:** [N] with source attribution
- **Total unique sources:** [N]
- **Capital alignment:** [Aligned / Not aligned]
- **Validation result:** [X]/33 checks passed, [N] warnings, [N] failures

### What's Strong

[List 3-5 strengths drawn from the data:]
- [Strength 1 — specific, with data point. e.g., "Problem prevalence well-documented with 5 independent sources confirming 73% of rural hospitals lack adequate cybersecurity"]
- [Strength 2]
- [Strength 3]

### What's Weak or Unresolved

[List all weaknesses, gaps, and unknowns:]
- [Weakness 1 — specific, with data point. e.g., "Cost of status quo relies on a single industry estimate — no government source confirms the figure"]
- [Weakness 2]
- [Any validation warnings or failures]

### Gate Decisions

#### Blocking Decisions
[These must be resolved before the next phase can start.]

**Decision 1: Is this problem real and significant enough to build for?** `BLOCKING`
- **Proceed** → [What happens next. e.g., "Starts Phase 03 Market Thesis — research quantifies TAM/SAM/SOM for [specific market segment]."]
- **Revise** → [What gets redone. e.g., "Re-runs problem research targeting [specific evidence gap]. Focus on: [missing data]."]
- **Kill** → [What this means. e.g., "Archives project. Problem thesis data preserved for reference."]

#### Strategic Decisions
[These inform strategy but do not block the next phase. Later phases will produce data that makes these choices clearer.]

[Repeat for any strategic decisions with `STRATEGIC — revisit after Phase [NN]` tag]

## Recommendation

**READY FOR GATE REVIEW** / **READY FOR GATE REVIEW WITH WARNINGS** / **NEEDS REVISION: [specific items]**

Checks completed: [X]/33
Checks passed: [X]/33
Checks failed: [X]/33
Warnings: [X]/33
```
