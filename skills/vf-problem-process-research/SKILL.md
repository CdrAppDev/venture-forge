---
name: vf-problem-process-research
description: Process uploaded Claude Deep Research results into a validated Problem Thesis with structured evidence and customer voice extraction. Activate after the user uploads research files to {project}/research/02-problem/. Reads capital thesis and all research results, extracts cited evidence into evidence.yaml, synthesizes customer voice into themed document, writes thesis.md with inline citations, and produces a processing-log.md audit trail documenting all processing decisions.
license: MIT
metadata:
  version: "1.0.0"
  phase: 02-problem
  when: after_research
---

# Problem Thesis: Process Research

Process uploaded Claude Deep Research results into a validated Problem Thesis with structured evidence, extracted customer voice, and a complete audit trail.

## Prerequisites

- Capital thesis at `{project}/phases/01-capital/thesis.md`
- Research results uploaded to `{project}/research/02-problem/`

## Workflow

1. **Read** capital thesis and all research results
2. **Log** each file read with filename and word count to processing log
3. **Extract** and categorize all cited evidence
4. **Log** each piece of evidence: included or excluded, with reason
5. **Synthesize** problem statement from evidence
6. **Build** structured evidence YAML
7. **Extract** customer voice into themed document
8. **Log** any conflicting data found across research files
9. **Write** problem thesis with inline citations
10. **Compile** sources.md — deduplicated list of all third-party sources organized by category, with org name, document, date, URL, and what each source was cited for
11. **Write** processing log with complete audit trail
12. **Output** all five files to `{project}/phases/02-problem/`

## Outputs

| File | Location | Format |
|------|----------|--------|
| Problem Thesis | `{project}/phases/02-problem/thesis.md` | Markdown |
| Evidence | `{project}/phases/02-problem/evidence.yaml` | YAML |
| Customer Voice | `{project}/phases/02-problem/customer-voice.md` | Markdown |
| Sources | `{project}/phases/02-problem/sources.md` | Markdown |
| Processing Log | `{project}/phases/02-problem/processing-log.md` | Markdown |

## Evidence Requirements

| Category | Minimum Citations |
|----------|------------------|
| Prevalence | 3 |
| Severity | 3 |
| Cost of status quo | 2 |
| Customer voice quotes | 5 (with sources) |
| Current solutions | 1 |
| Gaps | 1 |

**Uncited claims cannot be used in the thesis.**

## Inline Citation Rule (Mandatory)

**Every factual claim, statistic, or data point in `thesis.md` MUST include an inline citation in the format `(Source Name, Date)` immediately after the claim.** This is not optional. The thesis narrative is the primary human-readable output — readers must be able to verify any claim without cross-referencing other files.

**Format:** `68% have no dedicated cybersecurity leader (Black Book Research, June 2025)`

**Rules:**
- Every percentage, dollar figure, count, or quantitative claim gets an inline citation
- Every named program, policy, or regulation gets a citation on first mention
- Direct quotes include the speaker's name, title, organization, and publication source
- The sources.md file provides URLs and full bibliographic detail — thesis.md provides inline attribution for readability
- A thesis.md with fewer than 80% of factual claims cited inline is considered incomplete and must be revised before validation

## Audit Trail Requirements

The processing log MUST document:
- **Files read:** Every research file read, with filename and approximate word count
- **Evidence included:** Each piece of evidence used, which output it went into, and why
- **Evidence excluded:** Each piece of evidence found but not used, and why (duplicate, uncited, irrelevant, contradicted)
- **Customer voice decisions:** Quotes included vs. excluded, theme grouping rationale
- **Conflicts found:** Any contradictions between research sources, with both values and sources cited
- **Gaps identified:** Citation minimums not met, categories with thin evidence
- **Decisions made:** Any judgment calls during processing (e.g., which severity figure to lead with, how to group themes)

## Quality Checklist

- [ ] Problem statement is one clear sentence
- [ ] All statistics have citations (source, date, URL)
- [ ] Citation minimums met per category
- [ ] Customer voice quotes have source attribution
- [ ] Capital alignment explicitly stated
- [ ] Gate criteria checklist embedded in thesis
- [ ] Sources.md lists every unique source with org, document, date, URL, and citation purpose
- [ ] All source URLs are from pages actually visited during research (no fabricated URLs)
- [ ] Processing log is complete with all audit trail sections

See `references/output-templates.md` for exact output formats.

## Writing Governance

Follow all rules in `skills/vf-write/SKILL.md`. Before writing thesis.md narrative:
- Load `skills/vf-write/references/register-rules.md` — Phase 02 uses research register
- Load `skills/vf-write/references/word-boundaries.md` — check narrative against prohibited terms
- Log connective claims (sentences connecting separately-sourced data) in the Decisions Made section of processing-log.md
