---
name: vf-problem-generate-prompts
description: Generate Claude Deep Research prompts for Phase 02 Problem Thesis. Use when validating whether a problem is real, significant, and worth solving. Reads the approved capital thesis and produces research prompts covering problem prevalence, customer voice from public sources, current solutions, cost of status quo, and regulatory context.
version: 1.0.0
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
5. **Save** to `{project}/research/02-problem-prompts.md`

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
- Instructions for user to save results to `research/02-problem/`

## Quality Checklist

- [ ] Prompts reference specific problem and vertical from capital thesis
- [ ] All five research areas covered
- [ ] Prompts explicitly request citations
- [ ] Customer voice prompt lists specific source types to search
- [ ] Prompts are specific enough to yield actionable research

See `references/prompt-templates.md` for detailed templates and output format.
