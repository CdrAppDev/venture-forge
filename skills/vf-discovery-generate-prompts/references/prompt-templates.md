# Discovery Prompt Templates

## Prompt Engineering Standards

Every research prompt MUST include these elements:

1. **Context block** - Why we need this research and how it will be used
2. **Scope bounds** - Verticals, geography, stage, funding types, and exclusions
3. **Uncertainty permission** - Explicit instruction to flag gaps rather than speculate
4. **Sequencing** - Order of operations within the prompt (first X, then Y)
5. **Citation format** - Exact structure for every source referenced
6. **Example entry** - One concrete example of what a good result looks like

### Citation Format (use in all prompts)

Include the contents of `references/citation-format.md` in each generated prompt.

---

## Prompt 1: Federal Funding Landscape

```
I am scanning for federal funding opportunities that could support new software ventures in [VERTICALS]. This research will identify active and upcoming federal programs so we can evaluate which ones to pursue.

Research the federal funding landscape for [VERTICALS] software ventures.

First, identify currently active programs:
- SBIR/STTR programs at agencies relevant to [VERTICALS] (HHS, NSF, DOD, DOE, DHS, USDA)
- Other federal grant programs on grants.gov matching [VERTICALS]
- Federal contract opportunities on SAM.gov for small business software
- Agency-specific innovation programs (e.g., CMS Innovation Center, CISA programs)

Then, identify recently created or expanded programs:
- New programs created by legislation in the past 24 months
- Existing programs that received increased appropriations
- Programs with upcoming application deadlines in the next 12 months
- Pilot programs or new solicitations in [VERTICALS]

For each program, document:
- Program name and sponsoring agency
- Stated purpose and eligible activities
- Funding amounts (per award and total program)
- Eligibility requirements (company size, stage, geography, certifications)
- Application timeline (open date, deadline, review period)
- Whether the program is recurring or one-time
- Any geographic preferences or set-asides

Scope:
- Verticals: [VERTICALS]
- Geography: [GEOGRAPHY] (company base) and national programs
- Stage: Pre-seed through seed; grants under $2M per award
- Exclude: [EXCLUSION_CRITERIA]

If a program appears relevant but application details are not yet published, list it with a note about expected timeline. Do not speculate about eligibility criteria that aren't publicly documented.

[CITATION FORMAT BLOCK]

Example of a well-documented funding opportunity:
---
**SBIR Phase I — HHS/ONC (Health IT)**
- **Agency:** Department of Health and Human Services, Office of the National Coordinator for Health IT
- **Purpose:** Fund early-stage R&D in health information technology
- **Amount:** $150K-$275K per award; ~40 awards annually
- **Eligibility:** US small business (<500 employees), principal investigator >51% effort
- **Timeline:** Annual solicitation, typically opens January, closes April
- **Recurring:** Yes, annual cycle
- **Geography:** National, no state preference
- **Source:** SBIR.gov program listing
- **Date:** Accessed 2026-01
- **URL:** https://sbir.gov
- **Relevance:** Direct alignment with health technology software ventures
---
```

## Prompt 2: State and Regional Programs

```
I am scanning for state and regional funding programs that support software startups in [VERTICALS]. This research will identify programs in [GEOGRAPHY] and nearby regions that could provide early-stage funding or support.

Research state and regional funding programs in this order:

1. First, identify programs in [STATE]:
   - State research authority grants and investments
   - State economic development incentives for tech companies
   - State-level innovation funds or startup acceleration programs
   - University-affiliated commercialization programs
   - State health IT or cybersecurity initiatives

2. Then, identify regional programs:
   - Southeast or regional economic development organizations
   - Multi-state initiatives relevant to [VERTICALS]
   - Federal programs with state-allocated funding (block grants administered by states)

3. Finally, document each program:
   - Program name and administering organization
   - Funding type (grant, equity investment, loan, tax credit, in-kind)
   - Amount available (per company and total program)
   - Eligibility requirements (must be in-state, stage requirements, vertical focus)
   - Application process and timeline
   - Track record (how many companies funded, notable alumni)

Scope:
- Primary: [STATE] programs
- Secondary: Regional and multi-state programs accessible from [STATE]
- Verticals: [VERTICALS]
- Stage: Pre-seed through seed
- Exclude: [EXCLUSION_CRITERIA]

If a program's current status is unclear (e.g., was active last year but no 2026 announcement), note it as "Status unconfirmed — last active [date]" rather than assuming it continues.

[CITATION FORMAT BLOCK]

Example of a well-documented state program:
---
**SC Research Authority (SCRA) — SC Launch**
- **Organization:** South Carolina Research Authority
- **Type:** Equity investment + acceleration support
- **Amount:** $25K-$200K per company
- **Eligibility:** SC-based technology company, early stage, scalable business model
- **Process:** Application via SC Launch portal, rolling review
- **Track record:** 100+ companies funded since 2006
- **Source:** SCRA website, SC Launch program page
- **Date:** Accessed 2026-01
- **URL:** https://scra.org/sc-launch
- **Relevance:** Direct state-level funding for SC-based tech startups
---
```

## Prompt 3: Private and Institutional Funding

```
I am scanning for private funding sources — VC firms, accelerators, angel groups, and corporate programs — that invest in [VERTICALS] software ventures. This research will map the private funding landscape so we can identify the most aligned sources.

Research private and institutional funding in this order:

1. First, identify VC firms with relevant thesis:
   - Firms that explicitly invest in [VERTICALS] at pre-seed or seed stage
   - Firms that have made investments in [VERTICALS] software in the past 24 months
   - Sector-specific funds focused on [VERTICALS]
   - For each: firm name, thesis, check sizes, stage focus, recent relevant investments

2. Then, identify accelerator programs:
   - National programs that accept [VERTICALS] companies (Y Combinator, Techstars, MassChallenge)
   - Domain-specific accelerators for [VERTICALS]
   - For each: program name, investment terms, cohort size, application timeline, relevant alumni

3. Next, identify angel and institutional sources:
   - Angel groups active in [VERTICALS] or [GEOGRAPHY]
   - Corporate innovation programs from large companies in [VERTICALS]
   - Health system innovation funds (if healthcare is a vertical)
   - For each: organization, typical investment, focus areas, access process

4. Finally, note emerging patterns:
   - Which verticals are seeing increased private investment?
   - Are there new funds being raised focused on [VERTICALS]?
   - Any notable exits that signal investor interest?

Scope:
- Verticals: [VERTICALS]
- Stage: Pre-seed and seed (checks under $2M)
- Geography: US-based investors, with preference for those open to [GEOGRAPHY] companies
- Exclude: [EXCLUSION_CRITERIA]

If an investor's current activity level is unclear, note the last confirmed investment date rather than assuming they are actively deploying.

[CITATION FORMAT BLOCK]

Example of a well-documented private funding source:
---
**General Catalyst — Health Assurance**
- **Type:** VC firm with healthcare thesis
- **Thesis:** "Health Assurance" — shifting from sick care to proactive health through technology
- **Check size:** $500K-$5M at seed
- **Stage:** Seed through Series A
- **Recent relevant investments:** Sword Health (digital MSK), Included Health (navigation)
- **Access:** Warm intro preferred; applies via website accepted
- **Source:** General Catalyst website, Health Assurance thesis page
- **Date:** Accessed 2026-01
- **URL:** https://generalcatalyst.com/health-assurance
- **Relevance:** Explicit healthcare technology thesis with seed-stage investments
---
```

## Prompt 4: Policy and Regulatory Signals

```
I am scanning for policy and regulatory changes that create new funding opportunities or market demand for [VERTICALS] software ventures. This research will identify tailwinds — government actions that either directly fund or indirectly create demand for the types of ventures we build.

Research policy and regulatory signals in this order:

1. First, identify recent legislation (past 24 months):
   - Federal legislation creating new funding programs relevant to [VERTICALS]
   - Appropriations bills that increased funding for [VERTICALS] agencies
   - Bipartisan legislation with strong passage likelihood relevant to [VERTICALS]
   - State-level legislation in [STATE] affecting [VERTICALS]

2. Then, identify regulatory enforcement trends:
   - Agencies increasing enforcement in [VERTICALS] areas (creates compliance demand)
   - New regulations requiring technology adoption
   - Upcoming compliance deadlines that create urgency
   - Penalties that have increased, making compliance tools more valuable

3. Next, identify executive and agency actions:
   - Executive orders directing spending on [VERTICALS]
   - Agency strategic plans prioritizing [VERTICALS]
   - Federal requests for information (RFIs) signaling upcoming programs
   - White House initiatives or task forces relevant to [VERTICALS]

4. Finally, assess the funding implications:
   - Which policy signals are most likely to create direct funding (grants, contracts)?
   - Which create indirect demand (compliance requirements, market pressure)?
   - What is the likely timeline for each signal to translate to actionable opportunity?

Scope:
- Verticals: [VERTICALS]
- Geography: Federal and [STATE] policy
- Time horizon: Actions in the past 24 months and announced upcoming actions
- Exclude: [EXCLUSION_CRITERIA]

If a policy signal is rumored but not officially announced, label it as "Unconfirmed signal" with the source of the rumor. Do not present speculative policy predictions as fact.

[CITATION FORMAT BLOCK]

Example of a well-documented policy signal:
---
**Rural Health Technology Program (RHTP)**
- **Type:** Federal legislation creating new funding
- **Details:** $50B over 5 years (FY2026-2030), $10B annually across states
- **Relevance:** SC received $200M allocation with "Tech Catalyst Fund" for health startups
- **Category alignment:** Category F (IT Assistance) for cybersecurity; Category D (Training/Tech Adoption) for training
- **Timeline:** Grant cycles aligned with federal fiscal year; first solicitations expected Q2 2026
- **Funding implication:** Direct — creates grant funding for health technology ventures in SC
- **Source:** Congress.gov, RHTP Act text; SC DHEC implementation guidance
- **Date:** Signed into law 2025
- **URL:** [direct link to legislation]
- **Relevance:** Largest single funding source identified for rural health technology ventures
---
```

---

## Placeholder Reference

| Placeholder | Source |
|-------------|--------|
| `[VERTICALS]` | venture-profile.md → Verticals section (as comma-separated list) |
| `[GEOGRAPHY]` | venture-profile.md → Geographies section (company base and target markets) |
| `[STATE]` | venture-profile.md → Geographies → Company base state |
| `[EXCLUSION_CRITERIA]` | venture-profile.md → Exclusion Criteria section (as bullet list) |
| `[CITATION FORMAT BLOCK]` | Contents of `references/citation-format.md` |

## Customization Instructions

When generating prompts from these templates:

1. Read the venture profile from `inputs/venture-profile.md`
2. Replace `[VERTICALS]` with the priority verticals as a comma-separated list
3. Replace `[GEOGRAPHY]` with company base and target market description
4. Replace `[STATE]` with the company base state
5. Replace `[EXCLUSION_CRITERIA]` with the exclusion criteria as a bullet list
6. Insert the full citation format block from `references/citation-format.md`
7. If the venture profile mentions specific scan parameters, add targeted sub-questions about those sources
8. Set the current year for time-scoping

## Output File Format

Save to `discovery/{run_id}/research/00-discovery-prompts.md`:

```markdown
# Opportunity Discovery Research Prompts

**Run ID:** {run_id}
**Date Generated:** {date}
**Venture Profile:** inputs/venture-profile.md

## Profile Summary

**Verticals:** {verticals}
**Geography:** {geography}
**Stage:** {stage preferences}
**Constraints:** {key constraints}

## Prompts

### Prompt 1: Federal Funding Landscape

{Full customized prompt}

---

### Prompt 2: State and Regional Programs

{Full customized prompt}

---

### Prompt 3: Private and Institutional Funding

{Full customized prompt}

---

### Prompt 4: Policy and Regulatory Signals

{Full customized prompt}

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save results to `discovery/{run_id}/research/00-discovery/`
3. Name files:
   - `01-federal-funding.md`
   - `02-state-programs.md`
   - `03-private-funding.md`
   - `04-policy-signals.md`
4. Once all research is complete, run vf-discovery-process-research
```
