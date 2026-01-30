---
name: vf-expert-generate-prompts
description: >
  Generate Claude Deep Research prompts for domain expert knowledge. Reads
  domain definition and phase definitions to produce 5 research prompts per
  domain covering evaluation frameworks, quality standards, common failures,
  stage-appropriate expectations, and expert decision criteria. Used to build
  vf-expert-{domain} review skills. Activate when building an expert review
  skill for a domain (funding, market, product, business, traction).
license: MIT
metadata:
  version: "1.0.0"
  phase: platform
  when: before_expert_skill_build
---

# Expert Domain: Generate Research Prompts

Generate Claude Deep Research prompts that gather the domain expertise needed to build expert review skills. Each expert review skill evaluates whether phase outputs are strategically sound — not just mechanically complete.

## Prerequisites

- Domain must be specified: one of `funding`, `market`, `product`, `business`, `traction`
- Phase definitions must exist at `process/phases/{phase_id}.yaml` for all phases in the domain
- Domain definitions at `references/domain-definitions.yaml`

## Domains

| Domain | Phases | Evaluates |
|--------|--------|-----------|
| funding | 01, 08, 12 | Capital strategy, pitch materials, funding execution |
| market | 02, 03, 04 | Problem validation, market sizing, competitive analysis |
| product | 05, 09, 10 | Solution design, architecture, MVP |
| business | 06, 07 | Unit economics, pricing, risk assessment |
| traction | 11, 12 | Go-to-market, customer acquisition, funding execution |

## Workflow

1. **Read** domain definition from `references/domain-definitions.yaml` for the specified domain
2. **Read** phase definitions from `process/phases/{phase_id}.yaml` for each phase in the domain's phase list
3. **Extract** from each phase definition: purpose, outputs (name, description, format), gate criteria (id, description), gate question
4. **Generate 5 prompts** using templates in `references/prompt-templates.md`, replacing all placeholders with domain and phase specifics
5. **Inject** citation format block (from `references/citation-format.md`), scope bounds, and uncertainty permission into each prompt
6. **Save** to `process/research/expert-{domain}-prompts.md`

## Research Areas (5 Prompts)

| # | Area | Purpose |
|---|------|---------|
| 1 | Evaluation Frameworks | Published rubrics, scoring systems, assessment criteria |
| 2 | Quality Standards | What separates good from bad; benchmarks and best practices |
| 3 | Common Failures | Documented startup failure modes, red flags, anti-patterns |
| 4 | Stage-Appropriate Expectations | What "good enough" looks like at pre-product/pre-revenue stage |
| 5 | Expert Decision Criteria | How real decision-makers (funders, reviewers) actually evaluate |

## Output

File: `process/research/expert-{domain}-prompts.md`

Must contain:
- Domain name and date
- List of phases covered with their purposes
- Phase output types the expert will evaluate (from phase YAMLs)
- All 5 research prompts with citation requirements
- Each prompt includes: context block, sequencing, scope bounds, uncertainty permission, citation format, example entry
- Instructions for running in Claude Deep Research and saving results

## Quality Checklist

- [ ] All phases in the domain are represented in prompts
- [ ] Prompts reference specific output types from phase definitions (thesis.md, model.yaml, etc.)
- [ ] All prompts explicitly request citations with structured format
- [ ] Prompts target professional/academic sources, not startup advice blogs
- [ ] Each prompt addresses a distinct research area (no overlap between the 5)
- [ ] Stage-appropriate expectations prompt specifies pre-product/pre-revenue context
- [ ] Each prompt has context/motivation explaining why the research matters
- [ ] Each prompt grants permission to flag uncertainty rather than speculate

See `references/prompt-templates.md` for detailed templates and `references/domain-definitions.yaml` for domain specifications.
