---
name: vf-expert-funding
description: >
  Expert review of funding domain outputs (Phases 01, 08, 12). Evaluates
  whether capital thesis, pitch materials, and funding execution are
  strategically sound — not just mechanically complete. Uses research-backed
  rubrics, red flags, and stage calibration to identify fatal flaws, serious
  gaps, and quality standards that validate skills cannot catch. Activate
  after validate skill, before gate-review.
license: MIT
metadata:
  version: "1.0.0"
  phase: funding
  when: after_validate
---

# Expert Review: Funding Domain

Evaluate whether funding domain outputs are strategically sound. The validate skill checks mechanical completeness (files exist, citations present, counts match). This skill checks whether the work would survive scrutiny from grant reviewers, angel investors, and VC partners.

## Pipeline Position

```
process-research → validate (mechanical) → expert-review (strategic) → gate-review (human decision)
```

## Phases Covered

| Phase | Outputs Evaluated |
|-------|-------------------|
| 01 — Capital Thesis | capital_thesis.md, funder-profiles.yaml |
| 08 — Materials Assembly | evidence_library.yaml, pitch-deck.md, executive-summary.md, one-pager.md |
| 12 — Funding Execution | funding_applications/, data-room/, funding-status.yaml |

## Prerequisites

- Phase outputs exist at `{project}/phases/{phase_id}/`
- Validation report exists (mechanical checks passed or issues noted)
- This skill runs for whichever funding phase is currently at gate

## Workflow

1. **Read** the phase definition from `process/phases/{phase_id}.yaml`
2. **Read** all phase outputs for the current phase
3. **Read** the validation report (to avoid duplicating mechanical checks)
4. **Evaluate** outputs against the rubric in `references/rubric.yaml`
5. **Scan** for red flags from `references/red-flags.md`
6. **Calibrate** expectations using `references/stage-calibration.md`
7. **Write** expert review report to `{project}/phases/{phase_id}/expert-review.md`

## Evaluation Approach

### What This Skill Does (Strategic)

- Is the funder list strategically prioritized or a spray-and-pray dump?
- Does the capital thesis demonstrate genuine understanding of what each funder evaluates?
- Are pitch materials structured to survive the 2.5-minute investor scan?
- Does the funding execution match the venture's actual stage and traction?
- Are there fatal flaws that would cause immediate rejection?

### What This Skill Does NOT Do (Mechanical — handled by validate)

- Check file existence or format compliance
- Count citations or verify URLs
- Validate YAML structure or field presence
- Check word counts or section completeness

## Severity Classification

Every finding is classified using the research-backed severity taxonomy:

| Severity | Definition | Action |
|----------|-----------|--------|
| **Fatal Flaw** | Would cause immediate rejection by evaluators. One fatal flaw overrides all strengths (elimination-by-aspects model). | Block — must be resolved before gate review |
| **Serious Gap** | Major red flag that may be overcome only by exceptional strengths elsewhere. | Flag for human — requires judgment call |
| **Minor Weakness** | Addressable issue that doesn't predict failure. | Note for improvement — don't block |
| **Observation** | Stage-calibration note or strategic suggestion. | Informational — no action required |

## Output

File: `{project}/phases/{phase_id}/expert-review.md`

```markdown
# Expert Review: {Phase Name}

**Project:** {project}
**Phase:** {phase_id}
**Date:** {date}
**Reviewer:** vf-expert-funding v1.0.0

## Executive Summary

{2-3 sentence assessment: Is this strategically sound? What is the primary
strength and primary concern?}

## Findings

### Fatal Flaws
{List with evidence and research basis. If none: "No fatal flaws identified."}

### Serious Gaps
{List with evidence and research basis. If none: "No serious gaps identified."}

### Minor Weaknesses
{List with specific improvement suggestions.}

### Observations
{Stage-calibration notes and strategic suggestions.}

## Rubric Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| {dimension} | {1-5} | {specific evidence from outputs} |

**Composite:** {weighted average}/5

## Stage Calibration

{Note where outputs exceed or fall short of pre-product/pre-revenue
expectations. Flag over-engineering as well as under-development.}

## Recommendation

{PROCEED / CONCERNS / BLOCK}

- **PROCEED** — No fatal flaws, no serious gaps. Ready for gate review.
- **CONCERNS** — No fatal flaws but serious gaps exist. Human should weigh
  these at gate review.
- **BLOCK** — Fatal flaw(s) identified. Must be resolved before gate review.
```

## Quality Checklist

- [ ] Every finding cites specific evidence from the outputs being reviewed
- [ ] Every finding references the research basis (which framework, study, or benchmark)
- [ ] Severity classifications follow the taxonomy (fatal/serious/minor/observation)
- [ ] Stage calibration applied — not holding pre-product ventures to post-revenue standards
- [ ] Over-engineering flagged as well as under-development
- [ ] Rubric scores have specific rationale, not generic assessments
- [ ] Recommendation is one of three levels (PROCEED/CONCERNS/BLOCK)
- [ ] Expert review does not duplicate mechanical checks from validation report

See `references/rubric.yaml` for scoring criteria, `references/red-flags.md` for detection patterns, and `references/stage-calibration.md` for stage-appropriate expectations.
