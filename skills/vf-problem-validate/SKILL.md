---
name: vf-problem-validate
description: Validate Problem Thesis outputs against gate criteria before human review. Use after processing research for Phase 02. Checks that all required files exist, citation minimums are met, customer voice is captured, and cross-references are consistent. Produces a validation report.
version: 1.0.0
phase: 02-problem
when: before_gate
---

# Problem Thesis: Validate

Check that Problem Thesis outputs meet all gate criteria before presenting to human for review. Catches gaps early so human review focuses on strategic judgment.

## Prerequisites

- Phase outputs exist at `{project}/phases/02-problem/`

## Checks to Perform

### 1. File Existence

Verify these files exist and are non-empty:
- `{project}/phases/02-problem/thesis.md`
- `{project}/phases/02-problem/evidence.yaml`
- `{project}/phases/02-problem/customer-voice.md`

### 2. Evidence Validation

Read `evidence.yaml` and verify:
- `problem_statement` present and non-empty
- `prevalence.statistics` has 3+ entries, each with `stat`, `source`, `date`
- `severity.statistics` has 3+ entries
- `cost_of_status_quo.statistics` has 2+ entries
- `current_solutions` has 1+ entries
- `gaps` has 1+ entries
- `capital_alignment.aligned` is true

### 3. Customer Voice Validation

Read `customer-voice.md` and verify:
- 5+ direct quotes with source attribution
- 2+ distinct themes identified
- Common language/terminology section present
- Workarounds section present

### 4. Thesis Validation

Read `thesis.md` and verify:
- Problem statement section exists
- Key statistics table with source column
- Customer voice section present
- Capital alignment section present
- Evidence summary with citation counts
- Gate criteria checklist present

### 5. Cross-Validation

- Problem statement in thesis.md matches evidence.yaml
- Statistics in thesis.md appear in evidence.yaml
- Quotes in thesis.md appear in customer-voice.md

## Output

Generate validation report at `{project}/phases/02-problem/validation-report.md`

See `references/report-template.md` for exact format.

**Result: READY FOR GATE REVIEW or NEEDS REVISION with specific items listed.**
