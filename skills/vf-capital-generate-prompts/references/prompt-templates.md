# Capital Thesis Prompt Templates

## Prompt Engineering Standards

Every research prompt MUST include these elements:

1. **Context block** - Why we need this research and how it will be used
2. **Scope bounds** - Time range, geography, stage, and exclusions
3. **Uncertainty permission** - Explicit instruction to flag gaps rather than speculate
4. **Sequencing** - Order of operations within the prompt (first X, then Y)
5. **Citation format** - Exact structure for every source referenced
6. **Example entry** - One concrete example of what a good result looks like

### Citation Format (use in all prompts)

```
For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.
```

---

## Prompt 1: Funding Landscape

```
I am building a capital thesis for a [VERTICAL/STAGE] venture. This research will identify the full landscape of potential funders so we can prioritize outreach and align our positioning to what funders actually want.

Research the funding landscape for [VERTICAL/STAGE] ventures.

First, identify all active funding sources in these categories:
- Government grants and federal programs
- State-level economic development programs
- Venture capital firms with relevant thesis
- Strategic investors (corporates, health systems)
- Accelerators and incubators

Then, for each funding source, provide:
- Organization name and program name
- Stated investment thesis or funding criteria
- Funding amounts and stages they target
- Recent investments or grants made (last 2 years)
- Application process overview (if public)

Scope:
- Focus on programs active as of [CURRENT YEAR]
- Include [GEOGRAPHY] programs and national programs
- Early-stage focus (pre-seed through Series A, grants under $1M)

If a funding source appears relevant but you cannot find detailed criteria, list it with a note that further research is needed. Do not speculate about criteria that aren't publicly documented.

[CITATION FORMAT BLOCK]

Example of a well-documented funding source entry:
---
**SBIR Phase I (HHS)**
- **Thesis:** Fund early-stage R&D in health technology with commercial potential
- **Amount:** $150K-$275K per award
- **Stage:** Pre-revenue, proof of concept
- **Recent awards:** 47 cybersecurity-related awards in FY2024 (Source: SBIR.gov, Accessed 2025-01)
- **Process:** Annual solicitation, 6-month review cycle
---
```

## Prompt 2: Specific Funder Analysis

```
I am evaluating [SPECIFIC FUNDER(S)] as primary funding targets for a [VERTICAL] startup based in [LOCATION]. This deep dive will inform our application strategy and help us tailor materials to each funder's specific priorities.

For each funder listed below, research in this order:

1. First, establish the program structure:
   - How the program works (grant vs. equity vs. loan)
   - Eligibility requirements and restrictions
   - Funding amounts available
   - Application cycles and deadlines

2. Then, analyze their decision-making:
   - Stated evaluation criteria and scoring rubrics (if public)
   - Key decision makers and their backgrounds
   - Public statements about priorities or thesis
   - Board composition or investment committee

3. Finally, examine their track record:
   - Portfolio companies or past grantees (last 3 years)
   - Any funded projects in similar spaces to [VERTICAL]
   - Success stories they highlight publicly
   - Reported outcomes or ROI of funded projects

Funders to research:
[LIST SPECIFIC FUNDERS FROM INPUT]

If a funder's application process or criteria are not publicly available, state this explicitly. Do not infer criteria from funded projects alone—note that as circumstantial evidence, not confirmed criteria.

[CITATION FORMAT BLOCK]
```

## Prompt 3: Funder Requirements

```
I need to understand what it takes to successfully apply for [FUNDING TYPE] in [VERTICAL]. This will help us prepare application materials and assess our readiness before applying.

Research typical requirements in this order:

1. First, identify common criteria across funders:
   - Team requirements (experience, credentials, full-time commitment)
   - Stage and traction requirements (revenue, users, LOIs)
   - Technical requirements (IP, prototype, working product)
   - Market requirements (TAM thresholds, customer validation)

2. Then, document the application process:
   - Standard documentation required (business plan, financials, pitch deck)
   - Technical documentation (architecture, security review, compliance)
   - Timeline from application to decision (typical ranges)
   - Multi-stage processes (LOI → full application → interview → decision)

3. Finally, analyze success factors:
   - Success rates where publicly available
   - Common reasons for rejection (if documented)
   - Red flags that disqualify applicants
   - Competitive dynamics (number of applicants vs. awards)

Scope:
- Focus on [VERTICAL]-specific requirements, not generic startup advice
- Include both federal grant requirements and private investment requirements
- Note where requirements differ significantly between program types

Where success rates or rejection reasons are not publicly documented, say so rather than estimating.

[CITATION FORMAT BLOCK]
```

## Prompt 4: Recent Funding Activity

```
I need to understand the current momentum and trends in [VERTICAL] funding to position our venture within the current market context. This will inform both our timing and our narrative.

Research recent funding activity in [VERTICAL] (last 12-18 months).

First, document specific deals and awards:
- Notable VC investments (company, amount, round, investors, date)
- Federal grants awarded for [VERTICAL] projects
- Accelerator cohorts that included [VERTICAL] companies

Then, identify emerging patterns:
- Shifts in funder priorities (what's hot, what's cooling)
- New entrants to the funding space
- Changes in average deal size or terms
- Geographic trends (emerging hubs or distributed models)

Finally, assess the macro environment:
- Policy changes affecting funding (new programs, budget changes)
- Major industry events that shifted funder attention (breaches, regulations)
- Market consolidation or exits that signal maturity

Scope:
- Primary focus: [CURRENT YEAR - 1] through [CURRENT YEAR]
- Geography: US-focused with notable international deals
- Stage: Pre-seed through Series B

If trends are anecdotal rather than data-backed, label them as "Emerging signal" vs. "Established trend."

[CITATION FORMAT BLOCK]
```

## Customization Instructions

When generating prompts from these templates:

1. Replace all `[PLACEHOLDERS]` with specifics from `inputs/funder-criteria.md`
2. Insert the Citation Format Block (from the standards section above) into each prompt
3. Add any specific funders mentioned in the input to Prompt 2's funder list
4. Constrain geography to match the project's base and target market
5. Add vertical-specific search terms (e.g., "HIPAA" for healthcare, "FedRAMP" for government)
6. Set the current year for time-scoping
7. If the input mentions specific programs, add targeted sub-questions about those programs

## Output File Format

Save to `{project}/research/01-capital-prompts.md`:

```markdown
# Capital Thesis Research Prompts

**Project:** [Project Name]
**Date Generated:** [Date]
**Input Reference:** inputs/funder-criteria.md

## Context

[Summary of what we know about funding targets and what we need to learn]

## Prompts

### Prompt 1: Funding Landscape

[Full customized prompt with all placeholders replaced and citation format included]

---

### Prompt 2: Specific Funder Analysis

[Full customized prompt]

---

[Continue for all prompts]

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save each result to `research/01-capital/`
3. Name files: `01-landscape.md`, `02-funder-analysis.md`, `03-requirements.md`, `04-recent-activity.md`
4. Once all research is complete, notify for processing
```
