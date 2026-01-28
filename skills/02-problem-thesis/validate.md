# Skill: Problem Thesis - Validate

**Version:** 1.0.0
**Phase:** 02-problem
**When:** Before gate review

## Purpose

Check that the Problem Thesis phase outputs meet all gate criteria before presenting to human for review. Catch gaps early so human review focuses on strategic judgment, not completeness checking.

## Prerequisites

- Phase outputs exist:
  - `{project}/phases/02-problem/thesis.md`
  - `{project}/phases/02-problem/evidence.yaml`
  - `{project}/phases/02-problem/customer-voice.md`

## Instructions

### Step 1: Verify All Required Files Exist

Check that these files exist and are non-empty:
- `{project}/phases/02-problem/thesis.md`
- `{project}/phases/02-problem/evidence.yaml`
- `{project}/phases/02-problem/customer-voice.md`

If any file is missing, FAIL with: "Missing output: [filename]"

### Step 2: Validate Evidence Structure

Read `evidence.yaml` and verify:

- [ ] `problem_statement` is present and non-empty
- [ ] `prevalence.statistics` has at least 3 entries
- [ ] Each statistic has: `stat`, `source`, `date`
- [ ] `severity.statistics` has at least 3 entries
- [ ] `cost_of_status_quo.statistics` has at least 2 entries
- [ ] `current_solutions` has at least 1 entry
- [ ] `gaps` has at least 1 entry
- [ ] `capital_alignment.aligned` is true

If any check fails, record the specific failure.

### Step 3: Validate Customer Voice

Read `customer-voice.md` and verify:

- [ ] At least 5 direct quotes with sources
- [ ] Quotes include source attribution and date
- [ ] At least 2 distinct themes identified
- [ ] Common language/terminology section present
- [ ] Workarounds section present

### Step 4: Validate Thesis Document

Read `thesis.md` and verify:

- [ ] Problem statement section exists
- [ ] Key statistics table present with source column
- [ ] All statistics have citations (source, date)
- [ ] Customer voice section references customer-voice.md findings
- [ ] Capital alignment section present
- [ ] Evidence summary section with citation counts
- [ ] Gate criteria checklist present at bottom

### Step 5: Cross-Validate

- [ ] Problem statement in thesis.md matches evidence.yaml
- [ ] Statistics cited in thesis.md appear in evidence.yaml
- [ ] Customer quotes in thesis.md appear in customer-voice.md

### Step 6: Generate Validation Report

Create a validation report with this structure:

```markdown
# Validation Report: Problem Thesis

**Project:** [Project Name]
**Date:** [Date]
**Result:** PASS / FAIL

## File Checks

| File | Status |
|------|--------|
| thesis.md | Present / Missing |
| evidence.yaml | Present / Missing |
| customer-voice.md | Present / Missing |

## Evidence Checks

| Criterion | Required | Found | Status |
|-----------|----------|-------|--------|
| Prevalence citations | 3+ | [N] | PASS/FAIL |
| Severity citations | 3+ | [N] | PASS/FAIL |
| Cost citations | 2+ | [N] | PASS/FAIL |
| Current solutions | 1+ | [N] | PASS/FAIL |
| Gaps identified | 1+ | [N] | PASS/FAIL |
| Capital aligned | Yes | [Y/N] | PASS/FAIL |

## Customer Voice Checks

| Criterion | Required | Found | Status |
|-----------|----------|-------|--------|
| Direct quotes | 5+ | [N] | PASS/FAIL |
| Themes identified | 2+ | [N] | PASS/FAIL |
| Terminology section | Yes | [Y/N] | PASS/FAIL |
| Workarounds section | Yes | [Y/N] | PASS/FAIL |

## Thesis Checks

| Criterion | Status |
|-----------|--------|
| Problem statement | PASS/FAIL |
| Statistics table with sources | PASS/FAIL |
| Customer voice section | PASS/FAIL |
| Capital alignment section | PASS/FAIL |
| Evidence summary | PASS/FAIL |
| Gate checklist | PASS/FAIL |

## Failures

[List each failure with specific detail about what's missing]

## Recommendation

**READY FOR GATE REVIEW** / **NEEDS REVISION: [specific items]**
```

Output the report to `{project}/phases/02-problem/validation-report.md`

## Output Format

File: `{project}/phases/02-problem/validation-report.md`

## Quality Checklist

- [ ] All three output files checked for existence
- [ ] Citation minimums verified by count
- [ ] Cross-validation between files performed
- [ ] Specific failures identified with detail
- [ ] Clear pass/fail recommendation

## Version History

### 1.0.0 - 2025-01-28
- Initial version
- Checks: file existence, citation counts, cross-validation
