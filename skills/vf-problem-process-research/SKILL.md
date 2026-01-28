---
name: vf-problem-process-research
description: Process Claude Deep Research results into a validated Problem Thesis. Use after the user has uploaded research results for Phase 02. Reads research from the project research folder and produces thesis document, structured evidence YAML, and customer voice extraction.
version: 1.0.0
phase: 02-problem
when: after_research
---

# Problem Thesis: Process Research

Process uploaded Claude Deep Research results into a validated Problem Thesis with structured evidence and extracted customer voice.

## Prerequisites

- Capital thesis at `{project}/phases/01-capital/thesis.md`
- Research results uploaded to `{project}/research/02-problem/`

## Workflow

1. **Read** capital thesis and all research results
2. **Extract** and categorize all cited evidence
3. **Synthesize** problem statement from evidence
4. **Build** structured evidence YAML
5. **Extract** customer voice into themed document
6. **Write** problem thesis with inline citations
7. **Output** all three files to `{project}/phases/02-problem/`

## Outputs

| File | Location | Format |
|------|----------|--------|
| Problem Thesis | `{project}/phases/02-problem/thesis.md` | Markdown |
| Evidence | `{project}/phases/02-problem/evidence.yaml` | YAML |
| Customer Voice | `{project}/phases/02-problem/customer-voice.md` | Markdown |

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

## Quality Checklist

- [ ] Problem statement is one clear sentence
- [ ] All statistics have citations (source, date, URL)
- [ ] Citation minimums met per category
- [ ] Customer voice quotes have source attribution
- [ ] Capital alignment explicitly stated
- [ ] Gate criteria checklist embedded in thesis

See `references/output-templates.md` for exact output formats.
