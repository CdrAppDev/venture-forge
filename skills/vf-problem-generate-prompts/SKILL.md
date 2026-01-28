---
name: vf-problem-generate-prompts
description: Generate Claude Deep Research prompts for Phase 02 Problem Thesis. Activate when Phase 01 Capital Thesis is approved and exists at {project}/phases/01-capital/thesis.md. Reads the capital thesis to identify the problem hypothesis, then produces 4-5 customized research prompts covering problem prevalence/severity, customer voice from public sources (forums, reviews, Reddit, LinkedIn), current solutions and gaps, cost of status quo, and regulatory context. Each prompt includes context blocks, scope bounds, citation format, uncertainty permission, and sequencing per prompt engineering standards.
version: 1.0.0
license: MIT
phase: 02-problem
when: before_research
---

# Problem Thesis: Generate Research Prompts

Generate Claude Deep Research prompts that validate whether the problem is real, significant, and worth solving. Prompts must yield evidence satisfying phase gate criteria.

## Prerequisites

- Capital thesis approved at `{project}/phases/01-capital/thesis.md`

## Workflow

1. **Read** capital thesis from `{project}/phases/01-capital/thesis.md`
2. **Identify** the problem hypothesis aligned with funder criteria
3. **Generate 4-5 prompts** using templates in `references/prompt-templates.md`
4. **Customize** with specific problem, vertical, and target customers
5. **Inject** citation format block, scope bounds, and uncertainty permission into each prompt
6. **Save** to `{project}/research/02-problem-prompts.md`

## Research Areas (All Required)

| Area | Citation Minimum |
|------|-----------------|
| Problem prevalence and severity | 3 |
| Customer voice from public sources | 5 |
| Current solutions and shortcomings | 3 |
| Cost of status quo | 2 |
| Regulatory context (if applicable) | 1 |

## Output

File: `{project}/research/02-problem-prompts.md`

Must contain:
- Project name and date
- Context from capital thesis
- All research prompts with explicit citation requirements
- Customer voice prompt must specify: forums, reviews, Reddit, support channels, LinkedIn/Twitter
- Each prompt includes: context block, sequencing, scope bounds, uncertainty permission, citation format
- Instructions for user to save results to `research/02-problem/`

## Quality Checklist

- [ ] Prompts reference specific problem and vertical from capital thesis
- [ ] All five research areas covered
- [ ] All prompts explicitly request citations with structured format
- [ ] Customer voice prompt lists specific source types to search
- [ ] Prompts are specific enough to yield actionable research
- [ ] Each prompt has context/motivation explaining why the research matters
- [ ] Each prompt grants permission to flag uncertainty rather than speculate

See `references/prompt-templates.md` for detailed templates and output format.
