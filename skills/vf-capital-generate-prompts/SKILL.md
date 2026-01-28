---
name: vf-capital-generate-prompts
description: Generate Claude Deep Research prompts for Phase 01 Capital Thesis. Use when starting a new venture opportunity and need to understand the funding landscape. Reads funder criteria input and produces research prompts covering funding landscape, specific funders, requirements, and recent activity.
version: 1.0.0
phase: 01-capital
when: before_research
---

# Capital Thesis: Generate Research Prompts

Generate Claude Deep Research prompts to understand the funding landscape and identify viable capital sources.

## Prerequisites

- Funder criteria input exists at `{project}/inputs/funder-criteria.md`

## Workflow

1. **Read** funder criteria from `{project}/inputs/funder-criteria.md`
2. **Identify gaps** in what we know about funding sources
3. **Generate 3-4 prompts** using templates in `references/prompt-templates.md`
4. **Customize** by replacing placeholders with specifics from input
5. **Save** to `{project}/research/01-capital-prompts.md`

## Output

File: `{project}/research/01-capital-prompts.md`

Must contain:
- Project name and date
- Context summary from funder criteria
- All research prompts with citation requirements
- Instructions for user to run in Claude Deep Research and save results to `research/01-capital/`

## Quality Checklist

- [ ] Prompts address known funders from input
- [ ] Prompts seek additional/alternative funding sources
- [ ] All prompts explicitly request citations
- [ ] Geographic/vertical scope specified
- [ ] Covers: landscape, specific funders, requirements, recent activity

See `references/prompt-templates.md` for detailed prompt templates and output format.
