---
name: vf-capital-validate
description: Run exhaustive validation of Capital Thesis outputs against all Phase 01 gate criteria before human review. Activate after vf-capital-process-research completes and outputs exist at {project}/phases/01-capital/. Checks file existence, funder profile completeness, citation minimums, thesis structure, cross-file consistency, and timeline coverage. Produces a validation report with per-check PASS/FAIL and overall recommendation. Optionally runs validate.py for deterministic checks.
version: 1.0.0
license: MIT
phase: 01-capital
when: before_gate
---

# Capital Thesis: Validate

Run exhaustive validation of Capital Thesis outputs against all gate criteria. Catches gaps early so human review focuses on strategic judgment, not missing fields.

## Prerequisites

- Phase outputs exist at `{project}/phases/01-capital/`
- Processing log exists at `{project}/phases/01-capital/processing-log.md`

## Execution Rules

**CRITICAL: You MUST run EVERY check listed below before producing the validation report. Do not stop after finding the first failure. Do not mark the report as PASS after checking only a subset. Run ALL checks, report ALL results, then determine the overall verdict.**

- Run the `validate.py` script first for deterministic checks (file existence, YAML structure, field presence, citation counts)
- Then perform semantic checks manually (cross-validation, content quality)
- Report the total number of checks run vs. total checks defined
- If any check cannot be performed (e.g., file missing), mark it FAIL and continue to the next check

## Checks to Perform

### 1. File Existence (4 checks)

Verify these files exist and are non-empty:
- `{project}/phases/01-capital/thesis.md`
- `{project}/phases/01-capital/funder-profiles.yaml`
- `{project}/phases/01-capital/sources.md`
- `{project}/phases/01-capital/processing-log.md`

**Negative test:** If any file is missing, mark FAIL and continue — do not abort validation.

### 2. Funder Profile Validation (6 checks)

Read `funder-profiles.yaml` and verify:
- `funders` array has 2+ entries
- At least 2 funders have `viable: true`
- Each funder has all required fields:
  - `name`, `type`, `viable`, `viability_rationale`
  - `funding.amount_range` and `funding.source`
  - `criteria.stated` has 1+ entry with `source` field
  - `alignment.strengths` has 1+ entry
  - `alignment.gaps` is present (can be empty if fully aligned)
  - `alignment.overall_fit` is set
- Each funder with `process.timeline_confidence: unknown` is flagged as WARNING
- No funder has `viable: true` with `confidence: low` without explicit justification
- No funder has empty `viability_rationale`

**Negative test:** A funder entry missing `viable` field should produce FAIL, not be silently skipped.

### 3. Evidence Validation (4 checks)

Count citations across all funder profiles and verify minimums:
- Funder landscape: 3+ unique sources
- Investment thesis / criteria: 2+ cited criteria entries
- Portfolio / past investments: 3+ portfolio entries with sources
- Requirements and process: 2+ process-related citations

**Negative test:** A citation without a `source` field does not count toward the minimum.

### 4. Thesis Validation (8 checks)

Read `thesis.md` and verify each section exists and is non-empty:
- Executive summary present
- Funding landscape section with citations
- Active funding sources table
- At least 2 funder deep dive sections
- Alignment strategy section
- Funding timeline table
- Evidence summary with citation counts
- Gate criteria checklist present

**Negative test:** A section heading that exists but has no content beneath it is a FAIL.

### 5. Cross-Validation (4 checks)

- Funder names in thesis.md match entries in funder-profiles.yaml
- Viability assessments are consistent between files
- Citation counts in evidence summary match actual citations (tolerance: ±1)
- Alignment gaps in thesis match those in YAML profiles

**Negative test:** A funder appearing in YAML but not in thesis (or vice versa) is a FAIL.

### 6. Timeline Completeness (3 checks)

- Each viable funder has timeline information (dates, cycles, or "unknown" flag)
- Funding timeline table in thesis has entries for all viable funders
- Any viable funder with `timeline_confidence: unknown` is explicitly noted in thesis

**Negative test:** A viable funder with no timeline entry at all (not even "unknown") is a FAIL.

### 7. Sources Validation (3 checks)

- `sources.md` lists all unique sources cited across thesis.md and funder-profiles.yaml
- Each source entry has org name, document title, date, and what it was cited for
- Sources are organized by category (e.g., Government, Industry, Funders, News)

**Negative test:** A source cited in thesis.md or funder-profiles.yaml that does not appear in sources.md is a FAIL.

### 8. URL Verification (2 checks)

- All URLs in sources.md that have a direct link are formatted correctly (not placeholder text)
- URLs from research that returned errors during processing are flagged with a note (not silently included)

**Note:** Full HTTP verification is not required at validation time, but URLs that are obviously malformed (missing protocol, placeholder text like "TBD") should be flagged.

### 9. Processing Log Validation (3 checks)

- Processing log lists all research files that were read
- Processing log documents any excluded evidence with reasons
- Processing log notes any conflicting data found

## Check Summary

**Total checks: 36**

Report format: "Checks passed: X/36"

## Output

Generate validation report at `{project}/phases/01-capital/validation-report.md`

See `references/report-template.md` for exact format.

**Verdict rules:**
- ALL 36 checks pass → **READY FOR GATE REVIEW**
- Any FAIL → **NEEDS REVISION** with every failure listed
- Any WARNING → **READY FOR GATE REVIEW WITH WARNINGS** (list warnings)

The validation report MUST include the check counter showing X/36 checks completed. If fewer than 36 checks are reported, the validation itself is invalid.
