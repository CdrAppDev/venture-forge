---
name: vf-discovery-validate
description: >
  Validate discovery outputs before human gate review. Checks that
  opportunity profiles have cited sources, funder-criteria.md files
  are Phase 01-compatible, scores are consistent, and exclusion
  criteria are respected. Activate before Phase 00 gate review.
license: MIT
metadata:
  version: "1.0.0"
  phase: 00-discovery
  when: before_gate
---

# Opportunity Discovery: Validate

Check discovery outputs against gate criteria before human review. Produces a validation report identifying issues to fix before the gate decision.

## Prerequisites

- Discovery report at `discovery/{run_id}/discovery-report.md`
- Opportunity profiles at `discovery/{run_id}/opportunities/`
- Funder-criteria files at `discovery/{run_id}/outputs/`
- Venture profile at `inputs/venture-profile.md`

## Workflow

1. **Read** venture profile from `inputs/venture-profile.md`
2. **Read** discovery report from `discovery/{run_id}/discovery-report.md`
3. **Read** all opportunity profiles from `discovery/{run_id}/opportunities/`
4. **Read** all funder-criteria files from `discovery/{run_id}/outputs/`
5. **Validate** against gate criteria and quality checks
6. **Save** validation report to `discovery/{run_id}/validation-report.md`

## Validation Checks

### Gate Criteria Checks

| Check | Gate Criterion | Pass Condition |
|-------|---------------|----------------|
| G1 | opportunities_found | At least 2 opportunities scored 60+ in discovery report |
| G2 | exclusion_compliance | Every opportunity respects exclusion criteria from venture profile |
| G3 | evidence_quality | Every funding source in every opportunity has a citation with URL |
| G4 | actionability | Every funder-criteria.md has minimum required fields (see below) |

### Funder-Criteria Completeness (per file)

| Field | Required |
|-------|----------|
| At least 1 named funding source with amount range | Yes |
| Target vertical with customer segment | Yes |
| Geographic focus (company base + market) | Yes |
| At least 2 Known Context data points | Yes |
| "Additional Sources (Need Research)" section | Recommended |

### Quality Checks

| Check | Description |
|-------|-------------|
| Q1 | No funding sources appear in multiple opportunities without cross-reference note |
| Q2 | Scoring math is correct (dimension scores sum to composite) |
| Q3 | All opportunities with "Pursue" recommendation have score >= 80 |
| Q4 | No opportunity violates exclusion criteria |
| Q5 | Citations include URLs (not just source names) |
| Q6 | Funding amounts are specific ranges, not vague ("significant funding") |

## Output

File: `discovery/{run_id}/validation-report.md`

```markdown
# Discovery Validation Report

**Run ID:** {run_id}
**Date:** {date}
**Opportunities Validated:** {count}

## Gate Criteria

| Criterion | Status | Detail |
|-----------|--------|--------|
| opportunities_found | PASS/FAIL | {count} opportunities scored 60+ |
| profile_alignment | PASS/FAIL | {detail} |
| evidence_quality | PASS/FAIL | {count} sources missing citations |
| actionability | PASS/FAIL | {count} funder-criteria files complete |

## Quality Checks

| Check | Status | Detail |
|-------|--------|--------|
| Q1-Q6 | PASS/FAIL/WARN | {detail for each} |

## Issues to Fix

{List of specific issues that must be resolved before gate review}

## Gate Readiness

{READY / NOT READY — with summary of blocking issues}
```

## Quality Checklist

- [ ] All gate criteria are checked with specific evidence
- [ ] Every funder-criteria.md file is validated against the template
- [ ] Scoring consistency is verified (math check)
- [ ] Venture profile exclusion criteria are enforced
- [ ] Citation completeness is checked (URL present, not just source name)
- [ ] Report clearly states READY or NOT READY with blocking issues listed
