---
name: vf-problem-validate
description: Run exhaustive validation of Problem Thesis outputs against all Phase 02 gate criteria before human review. Activate after vf-problem-process-research completes and outputs exist at {project}/phases/02-problem/. Checks file existence, evidence YAML structure and citation minimums, customer voice completeness, thesis structure, cross-file consistency, and processing log. Produces a validation report with per-check PASS/FAIL and overall recommendation. Optionally runs validate.py for deterministic checks.
version: 1.0.0
license: MIT
phase: 02-problem
when: before_gate
---

# Problem Thesis: Validate

Run exhaustive validation of Problem Thesis outputs against all gate criteria. Catches gaps early so human review focuses on strategic judgment, not missing fields.

## Prerequisites

- Phase outputs exist at `{project}/phases/02-problem/`
- Processing log exists at `{project}/phases/02-problem/processing-log.md`

## Execution Rules

**CRITICAL: You MUST run EVERY check listed below before producing the validation report. Do not stop after finding the first failure. Do not mark the report as PASS after checking only a subset. Run ALL checks, report ALL results, then determine the overall verdict.**

- Run the `validate.py` script first for deterministic checks (file existence, YAML structure, field presence, citation counts)
- Then perform semantic checks manually (cross-validation, content quality)
- Report the total number of checks run vs. total checks defined
- If any check cannot be performed (e.g., file missing), mark it FAIL and continue to the next check

## Checks to Perform

### 1. File Existence (5 checks)

Verify these files exist and are non-empty:
- `{project}/phases/02-problem/thesis.md`
- `{project}/phases/02-problem/evidence.yaml`
- `{project}/phases/02-problem/customer-voice.md`
- `{project}/phases/02-problem/sources.md`
- `{project}/phases/02-problem/processing-log.md`

**Negative test:** If any file is missing, mark FAIL and continue — do not abort validation.

### 2. Evidence Validation (7 checks)

Read `evidence.yaml` and verify:
- `problem_statement` present and non-empty
- `prevalence.statistics` has 3+ entries, each with `stat`, `source`, `date`
- `severity.statistics` has 3+ entries, each with `stat`, `source`, `date`
- `cost_of_status_quo.statistics` has 2+ entries
- `current_solutions` has 1+ entries
- `gaps` has 1+ entries
- `capital_alignment.aligned` is true

**Negative test:** A statistic entry missing the `source` field does not count toward the minimum. An entry with `source: ""` is also invalid.

### 3. Customer Voice Validation (4 checks)

Read `customer-voice.md` and verify:
- 5+ direct quotes with source attribution (quote must have source and date)
- 2+ distinct themes identified (separate heading sections)
- Common language/terminology section present and non-empty
- Workarounds section present and non-empty

**Negative test:** A quote without a source citation does not count toward the minimum of 5. A theme heading with no quotes beneath it does not count as a distinct theme.

### 4. Thesis Validation (6 checks)

Read `thesis.md` and verify each section exists and is non-empty:
- Problem statement section exists with content
- Key statistics table with source column
- Customer voice section present with at least one quote
- Capital alignment section present
- Evidence summary with citation counts
- Gate criteria checklist present

**Negative test:** A section heading with no content beneath it is a FAIL.

### 5. Cross-Validation (3 checks)

- Problem statement in thesis.md matches evidence.yaml `problem_statement`
- Statistics cited in thesis.md appear in evidence.yaml
- Quotes used in thesis.md appear in customer-voice.md

**Negative test:** A statistic in thesis.md that does not appear in evidence.yaml is a FAIL (evidence of untracked claims).

### 6. Sources Validation (3 checks)

- `sources.md` lists all unique sources cited across thesis.md, evidence.yaml, and customer-voice.md
- Each source entry has org name, document title, date, and what it was cited for
- Sources are organized by category

**Negative test:** A source cited in thesis.md or evidence.yaml that does not appear in sources.md is a FAIL.

### 7. URL Verification (2 checks)

- All URLs in sources.md that have a direct link are formatted correctly (not placeholder text)
- URLs from research that returned errors during processing are flagged with a note

### 8. Processing Log Validation (3 checks)

- Processing log lists all research files that were read
- Processing log documents any excluded evidence with reasons
- Processing log notes any conflicting data found

## Check Summary

**Total checks: 33**

Report format: "Checks passed: X/33"

## Output

Generate validation report at `{project}/phases/02-problem/validation-report.md`

See `references/report-template.md` for exact format.

**Evidence Briefing (required):** After all checks, synthesize an Evidence Briefing section in the report. This is the most important part of the report — it is what the human reads to make gate decisions. It must include:

1. **What the evidence shows** — key numbers (problem statement, citation counts, customer voice count, capital alignment, validation result)
2. **What's strong** — 3-5 specific strengths from the data, each with a data point
3. **What's weak or unresolved** — every gap, warning, and unknown, each with specifics
4. **Gate decisions with consequences** — for each pending decision, explain what each option triggers in concrete terms (name the next phase and what it does, name the specific rework target, or explain what archiving means)

The briefing must be evidence-based, not a recommendation. State what the data supports. Do not tell the human what to decide.

**Verdict rules:**
- ALL 33 checks pass → **READY FOR GATE REVIEW**
- Any FAIL → **NEEDS REVISION** with every failure listed
- Any WARNING → **READY FOR GATE REVIEW WITH WARNINGS** (list warnings)

The validation report MUST include the check counter showing X/33 checks completed. If fewer than 33 checks are reported, the validation itself is invalid.
