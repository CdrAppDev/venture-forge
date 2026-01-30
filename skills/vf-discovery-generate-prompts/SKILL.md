---
name: vf-discovery-generate-prompts
description: >
  Generate Claude Deep Research prompts for funding opportunity discovery.
  Reads the venture profile and generates prompts per vertical across all
  funding source types (federal, state, VC, accelerators, angels, family
  offices, corporate, foundations, policy signals). Output feeds into
  vf-discovery-process-research. Activate when starting a Phase 00
  discovery run.
license: MIT
metadata:
  version: "2.0.0"
  phase: 00-discovery
  when: before_research
---

# Opportunity Discovery: Generate Research Prompts

Generate Claude Deep Research prompts that scan the funding landscape for software venture opportunities. Prompts are generated **per vertical** — each vertical gets its own set of prompts covering all funding source types.

## Prerequisites

- Venture profile must exist at `inputs/venture-profile.md`
- Discovery run ID must be specified (format: `YYYY-MM-descriptor`)

## Workflow

1. **Read** venture profile from `inputs/venture-profile.md`
2. **Identify verticals** — read the Scope section to determine which verticals to scan. If the profile says "all verticals," generate a list of major software-fundable verticals (see reference list below)
3. **For each vertical**, generate prompts across funding source types using templates in `references/prompt-templates.md`
4. **Inject** citation format block (from `references/citation-format.md`), exclusion criteria, and uncertainty permission into each prompt
5. **Save** to `discovery/{run_id}/research/00-discovery-prompts.md`

## Vertical Identification

When the venture profile specifies "all verticals," use this reference list of major verticals where software ventures attract funding:

| Vertical | Examples |
|----------|----------|
| Healthcare / Health IT | EHR, telehealth, clinical decision support, patient engagement, health data |
| Cybersecurity | Enterprise security, identity, compliance, threat detection |
| Fintech | Payments, lending, insurance, banking infrastructure, regtech |
| Edtech | K-12, higher ed, corporate training, credentialing |
| Climate / Clean Tech | Energy management, carbon tracking, grid software, sustainability |
| Govtech / Civic Tech | Government services, public safety, regulatory compliance |
| Legal Tech | Contract management, discovery, compliance, access to justice |
| HR / Future of Work | Recruiting, workforce management, benefits, remote work tools |
| Supply Chain / Logistics | Warehouse, freight, procurement, last-mile, visibility |
| Agriculture / Food Tech | Precision agriculture, food safety, supply chain traceability |
| Real Estate / Proptech | Property management, construction tech, mortgage, brokerage |
| AI / ML Infrastructure | Dev tools, MLOps, data labeling, model serving |

Add or remove verticals based on operator guidance. Each vertical gets its own prompt set.

## Prompts Per Vertical (7 funding source types)

For each vertical, generate one prompt per funding source type:

| # | Funding Source Type | What to Find |
|---|---------------------|-------------|
| 1 | Federal Programs | SBIR/STTR, agency grants, federal contracts for software in this vertical |
| 2 | State & Regional | State grants, economic development programs, regional accelerators |
| 3 | VC & Angel | VC firms, angel networks, syndicates with thesis in this vertical |
| 4 | Accelerators | Programs accepting companies in this vertical (general and domain-specific) |
| 5 | Family Offices | Family offices with direct investment in this vertical's technology |
| 6 | Corporate Funding | CVC arms, innovation programs, strategic pilots, corporate accelerators in this vertical |
| 7 | Policy & Regulatory | Legislation, enforcement trends, executive orders creating funding or demand in this vertical |

## Output

File: `discovery/{run_id}/research/00-discovery-prompts.md`

Must contain:
- Run ID and date
- Venture profile summary (primary constraint, scope)
- List of verticals being scanned
- For each vertical: 7 prompts (one per funding source type)
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
    07-policy-regulatory.md
```

## Quality Checklist

- [ ] All verticals from venture profile (or reference list) have prompts generated
- [ ] All 7 funding source types covered per vertical
- [ ] Prompts include exclusion criteria from venture profile
- [ ] All prompts explicitly request citations with structured format
- [ ] Prompts target official sources — funding announcements, published criteria, portfolio pages — not news summaries
- [ ] Each prompt is vertical-specific (not generic with vertical name swapped in — include vertical-relevant agencies, firms, programs)
- [ ] Each prompt grants permission to flag uncertainty rather than speculate
- [ ] File naming instructions are clear for the human running research

See `references/prompt-templates.md` for detailed templates.
