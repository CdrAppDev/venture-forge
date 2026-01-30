---
name: vf-discovery-generate-prompts
description: >
  Generate Claude Deep Research prompts for funding opportunity discovery.
  Reads the venture profile to produce 4 broad scan prompts covering federal
  grants, state programs, private funding, and policy signals. Output feeds
  into vf-discovery-process-research. Activate when starting a Phase 00
  discovery run.
license: MIT
metadata:
  version: "1.0.0"
  phase: 00-discovery
  when: before_research
---

# Opportunity Discovery: Generate Research Prompts

Generate Claude Deep Research prompts that scan the funding landscape for opportunities matching the venture profile. Unlike Phase 01 prompts which drill into known funders, these prompts cast a wide net across funding sources.

## Prerequisites

- Venture profile must exist at `inputs/venture-profile.md`
- Discovery run ID must be specified (format: `YYYY-MM-descriptor`)

## Workflow

1. **Read** venture profile from `inputs/venture-profile.md`
2. **Extract** verticals, geographies, capabilities, constraints, scan parameters, and exclusion criteria
3. **Generate 4 prompts** using templates in `references/prompt-templates.md`, replacing all placeholders with venture profile specifics
4. **Inject** citation format block (from `references/citation-format.md`), scope bounds, and uncertainty permission into each prompt
5. **Save** to `discovery/{run_id}/research/00-discovery-prompts.md`

## Research Areas (4 Prompts)

| # | Area | Purpose |
|---|------|---------|
| 1 | Federal Funding Landscape | Active federal grant programs matching profile verticals and constraints |
| 2 | State and Regional Programs | State economic development, research authorities, regional initiatives |
| 3 | Private and Institutional Funding | VCs, accelerators, angels, corporate innovation programs in target verticals |
| 4 | Policy and Regulatory Signals | Recent legislation, executive orders, enforcement trends creating opportunities |

## Output

File: `discovery/{run_id}/research/00-discovery-prompts.md`

Must contain:
- Run ID and date
- Venture profile summary (verticals, geographies, constraints)
- All 4 research prompts with citation requirements
- Each prompt includes: context block, sequencing, scope bounds, exclusion criteria, uncertainty permission, citation format, example entry
- Instructions for running in Claude Deep Research and saving results

## Quality Checklist

- [ ] All scan parameter categories from venture profile are represented in prompts
- [ ] Prompts include exclusion criteria from venture profile
- [ ] All prompts explicitly request citations with structured format
- [ ] Prompts target official funding announcements and published criteria, not news summaries
- [ ] Each prompt addresses a distinct funding category (no overlap between the 4)
- [ ] Each prompt specifies geography and vertical scope from venture profile
- [ ] Each prompt has context/motivation explaining why this scan matters
- [ ] Each prompt grants permission to flag uncertainty rather than speculate

See `references/prompt-templates.md` for detailed templates.
