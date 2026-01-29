---
name: vf-capital-process-research
description: Process uploaded Claude Deep Research results into a validated Capital Thesis with structured funder profiles. Activate after the user uploads research files to {project}/research/01-capital/. Reads funder criteria input and all research results, extracts cited evidence per funder, builds funder-profiles.yaml, synthesizes thesis.md with inline citations, and produces a processing-log.md audit trail documenting all processing decisions.
license: MIT
metadata:
  version: "1.0.0"
  phase: 01-capital
  when: after_research
---

# Capital Thesis: Process Research

Process uploaded Claude Deep Research results into a Capital Thesis with structured funder profiles and a complete audit trail.

## Prerequisites

- Funder criteria input at `{project}/inputs/funder-criteria.md`
- Research results uploaded to `{project}/research/01-capital/`

## Workflow

1. **Read** funder criteria input and all research results
2. **Log** each file read with filename and word count to processing log
3. **Extract** and categorize all cited evidence per funder
4. **Log** each piece of evidence: included or excluded, with reason
5. **Build** structured funder profiles YAML (one entry per funder)
6. **Synthesize** capital thesis narrative from evidence
7. **Assess** alignment path for each funder (what the venture must demonstrate)
8. **Document** timelines, decision processes, and application requirements
9. **Log** any conflicting data found across research files
10. **Write** capital thesis with inline citations
11. **Compile** sources.md — deduplicated list of all third-party sources organized by category, with org name, document, date, URL, and what each source was cited for
12. **Write** processing log with complete audit trail
13. **Output** all four files to `{project}/phases/01-capital/`

## Outputs

| File | Location | Format |
|------|----------|--------|
| Capital Thesis | `{project}/phases/01-capital/thesis.md` | Markdown |
| Funder Profiles | `{project}/phases/01-capital/funder-profiles.yaml` | YAML |
| Sources | `{project}/phases/01-capital/sources.md` | Markdown |
| Processing Log | `{project}/phases/01-capital/processing-log.md` | Markdown |

## Evidence Requirements

| Category | Minimum Citations |
|----------|------------------|
| Funder landscape | 3 |
| Investment thesis / criteria | 2 |
| Portfolio / past investments | 3 |
| Requirements and process | 2 |

**Uncited claims cannot be used in the thesis.**

## Inline Citation Rule (Mandatory)

**Every factual claim, statistic, or data point in `thesis.md` MUST include an inline citation in the format `(Source Name, Date)` immediately after the claim.** This is not optional. The thesis narrative is the primary human-readable output — readers must be able to verify any claim without cross-referencing other files.

**Format:** `CMS allocated $200M to South Carolina through the Rural Health Transformation program (CMS, December 2025)`

**Rules:**
- Every dollar figure, program size, deadline, or quantitative claim gets an inline citation
- Every named program, fund, or funder criteria statement gets a citation on first mention
- Funder deep dives cite the source for each criterion, portfolio example, and timeline
- The sources.md file provides URLs and full bibliographic detail — thesis.md provides inline attribution for readability
- A thesis.md with fewer than 80% of factual claims cited inline is considered incomplete and must be revised before validation

## Processing Rules

1. **One profile per funder** — Every distinct funding source gets its own entry in `funder-profiles.yaml`, even if information is thin. Mark thin profiles with `confidence: low`.
2. **Viability assessment** — Each funder profile must include a `viable: true/false` field with a one-sentence rationale. At least 2 must be viable to pass the gate.
3. **Alignment gaps** — For each funder, list what the venture currently lacks vs. what the funder requires. These gaps feed Phase 02-07 priorities.
4. **Timeline extraction** — Pull every date, deadline, and cycle mentioned in research into the funder profile. Missing timeline data should be flagged, not guessed.
5. **Conflicting information** — If research results contradict each other on funder criteria or amounts, present both and flag for human review. Log the conflict in processing-log.md.

## Audit Trail Requirements

The processing log MUST document:
- **Files read:** Every research file read, with filename and approximate word count
- **Evidence included:** Each piece of evidence used, which output it went into, and why
- **Evidence excluded:** Each piece of evidence found but not used, and why (duplicate, uncited, irrelevant, contradicted)
- **Conflicts found:** Any contradictions between research sources, with both values and sources cited
- **Gaps identified:** Citation minimums not met, funder data incomplete, timeline data missing
- **Decisions made:** Any judgment calls during processing (e.g., which of two conflicting figures to lead with)

## Quality Checklist

- [ ] Every funder mentioned in research has a profile in YAML
- [ ] At least 2 funders assessed as viable
- [ ] All criteria/requirements have citations (source, date, URL)
- [ ] Citation minimums met per category
- [ ] Alignment gaps documented per funder
- [ ] Timelines documented where available, flagged where not
- [ ] Gate criteria checklist embedded in thesis
- [ ] Sources.md lists every unique source with org, document, date, URL, and citation purpose
- [ ] All source URLs are from pages actually visited during research (no fabricated URLs)
- [ ] Processing log is complete with all audit trail sections

See `references/output-templates.md` for exact output formats.

## Writing Governance

Follow all rules in `skills/vf-write/SKILL.md`. Before writing thesis.md narrative:
- Load `skills/vf-write/references/register-rules.md` — Phase 01 uses research register
- Load `skills/vf-write/references/word-boundaries.md` — check narrative against prohibited terms
- Log connective claims (sentences connecting separately-sourced data) in the Decisions Made section of processing-log.md
