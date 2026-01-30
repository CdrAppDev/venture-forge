---
name: vf-discovery-generate-prompts
description: >
  Generate Claude Deep Research prompts for funding opportunity discovery.
  Reads the venture profile and generates prompts per vertical across all
  funding source types (federal, state, VC, accelerators, angels, family
  offices, corporate, foundations, government contracts, university,
  competitions, policy signals). Output feeds into
  vf-discovery-process-research. Activate when starting a Phase 00
  discovery run.
license: MIT
metadata:
  version: "3.0.0"
  phase: 00-discovery
  when: before_research
---

# Opportunity Discovery: Generate Research Prompts

Generate Claude Deep Research prompts that scan the funding landscape for funded problems across all verticals. Prompts are generated **per vertical** — each vertical gets prompts across all 11 funding source types.

Full matrix: 22 verticals × 11 source types = 242 prompts. Designed for eventual API automation. For manual runs, generate all prompts but the operator picks which verticals to run first.

## Prerequisites

- Venture profile must exist at `inputs/venture-profile.md`
- Discovery run ID must be specified (format: `YYYY-MM-descriptor`)
- Operator specifies which verticals to include in this run (all, or a subset)

## Workflow

1. **Read** venture profile from `inputs/venture-profile.md`
2. **Identify verticals** — use the full reference list (22 verticals) or a subset specified by the operator
3. **For each vertical**, generate 11 prompts (one per funding source type) using templates in `references/prompt-templates.md`
4. **Inject** citation format block (from `references/citation-format.md`), exclusion criteria, and uncertainty permission into each prompt
5. **Save** to `discovery/{run_id}/research/00-discovery-prompts.md`

## Verticals (22)

| # | Vertical | Examples |
|---|----------|----------|
| 1 | Healthcare / Health IT | EHR, telehealth, clinical decision support, patient engagement, health data |
| 2 | Cybersecurity | Enterprise security, identity, compliance, threat detection |
| 3 | Fintech | Payments, lending, banking infrastructure, regtech |
| 4 | Insurance / Insurtech | Underwriting, claims, distribution, risk modeling |
| 5 | Edtech | K-12, higher ed, corporate training, credentialing |
| 6 | Climate / Clean Tech | Energy management, carbon tracking, grid optimization, sustainability |
| 7 | Govtech / Civic Tech | Government services, public safety, regulatory compliance |
| 8 | Defense / National Security | Mission systems, intelligence tools, C2 systems, cleared platforms |
| 9 | Legal Tech | Contract management, discovery, compliance, access to justice |
| 10 | HR / Future of Work | Recruiting, workforce management, benefits, remote work tools |
| 11 | Supply Chain / Logistics | Warehouse, freight, procurement, last-mile, visibility |
| 12 | Agriculture / Food Tech | Precision agriculture, food safety, supply chain traceability |
| 13 | Real Estate / Proptech | Property management, mortgage, brokerage, tenant experience |
| 14 | Construction Tech | Project management, estimating, BIM, safety, field operations |
| 15 | Manufacturing Tech | MES, digital twin, quality management, predictive maintenance |
| 16 | Retail / Commerce Tech | POS, inventory, e-commerce infrastructure, personalization |
| 17 | Travel / Hospitality Tech | Booking, operations, guest experience, revenue management |
| 18 | Media / Entertainment Tech | Streaming, creator tools, content platforms, rights management |
| 19 | Telecom / Connectivity | Network management, 5G applications, rural broadband, connectivity |
| 20 | Biotech Software | Bioinformatics, drug discovery platforms, lab management, LIMS |
| 21 | Nonprofit / Social Impact Tech | Fundraising platforms, program management, impact measurement |
| 22 | AI / ML Infrastructure | Dev tools, MLOps, data labeling, model serving, vector databases |

## Funding Source Types (11)

For each vertical, generate one prompt per funding source type:

| # | Funding Source Type | What to Find |
|---|---------------------|-------------|
| 1 | Federal Programs | SBIR/STTR, agency grants, federal innovation programs |
| 2 | State & Regional | State grants, economic development, state innovation funds |
| 3 | VC & Angel | VC firms, angel networks, syndicates with thesis in this vertical |
| 4 | Accelerators | General and domain-specific accelerator programs |
| 5 | Family Offices | Family offices with direct investment in this vertical |
| 6 | Corporate Funding | CVC arms, innovation programs, strategic pilots, corporate accelerators |
| 7 | Foundations / Philanthropic | Foundation grants, PRIs, philanthropic programs (especially for non-profit ventures) |
| 8 | Government Contracts | IDIQ, BPA, GSA Schedule, agency-specific contract vehicles |
| 9 | University / Research | STTR partnerships, tech transfer, spinout programs, university venture funds |
| 10 | Competitions / Prizes | XPRIZE, challenge.gov, MIT Solve, industry challenges with funding |
| 11 | Policy & Regulatory Signals | Legislation, enforcement trends, executive orders creating funding or demand |

## Output

File: `discovery/{run_id}/research/00-discovery-prompts.md`

Must contain:
- Run ID and date
- Venture profile summary (primary constraint, scope)
- List of verticals included in this run
- Total prompt count
- For each vertical: 11 prompts (one per funding source type)
- Each prompt includes: context block, vertical-specific focus, sequencing, exclusion criteria, uncertainty permission, citation format, example entry
- Instructions for running in Claude Deep Research and saving results

## File Naming Convention for Results

Instruct the human to save results as:
```
discovery/{run_id}/research/00-discovery/
  {vertical-slug}/
    01-federal.md
    02-state-regional.md
    03-vc-angel.md
    04-accelerators.md
    05-family-offices.md
    06-corporate.md
    07-foundations.md
    08-government-contracts.md
    09-university-research.md
    10-competitions.md
    11-policy-regulatory.md
```

## Quality Checklist

- [ ] All specified verticals have prompts generated
- [ ] All 11 funding source types covered per vertical
- [ ] Prompts include exclusion criteria from venture profile
- [ ] All prompts explicitly request citations with structured format
- [ ] Prompts target official sources — funding announcements, published criteria, portfolio pages — not news summaries
- [ ] Each prompt is vertical-specific (not generic with vertical name swapped in — include vertical-relevant agencies, firms, programs)
- [ ] Each prompt grants permission to flag uncertainty rather than speculate
- [ ] File naming instructions are clear for the human running research

See `references/prompt-templates.md` for detailed templates.
