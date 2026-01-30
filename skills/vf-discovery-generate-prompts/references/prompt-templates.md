# Discovery Prompt Templates

Prompts are generated **per vertical**. For each vertical, generate one prompt per funding source type (7 total). Replace all `[PLACEHOLDERS]` with vertical-specific content.

## Prompt Engineering Standards

Every research prompt MUST include these elements:

1. **Context block** — Why we need this research and how it will be used
2. **Vertical-specific focus** — Agencies, firms, programs known to operate in this vertical (not just the vertical name swapped into a generic template)
3. **Scope bounds** — Funding types, stage, geography, and exclusions
4. **Sequencing** — Order of operations within the prompt
5. **Uncertainty permission** — Explicit instruction to flag gaps rather than speculate
6. **Citation format** — Exact structure for every source referenced (from `references/citation-format.md`)
7. **Example entry** — One concrete example of what a good result looks like

### Citation Format (use in all prompts)

Include the contents of `references/citation-format.md` in each generated prompt.

---

## Template 1: Federal Programs

```
I am scanning for federal funding opportunities for software ventures in [VERTICAL]. This research will identify active and upcoming federal programs so we can evaluate which to pursue.

Research the federal funding landscape for [VERTICAL] software ventures.

First, identify currently active programs:
- SBIR/STTR programs at agencies relevant to [VERTICAL] ([RELEVANT_AGENCIES])
- Other federal grant programs on grants.gov matching [VERTICAL]
- Federal contract opportunities on SAM.gov for small business software in [VERTICAL]
- Agency-specific innovation programs ([AGENCY_SPECIFIC_PROGRAMS])

Then, identify recently created or expanded programs:
- New programs created by legislation in the past 24 months relevant to [VERTICAL]
- Existing programs that received increased appropriations
- Programs with upcoming application deadlines in the next 12 months
- Pilot programs or new solicitations

For each program, document:
- Program name and sponsoring agency
- Stated purpose and eligible activities
- Funding amounts (per award and total program)
- Eligibility requirements (company size, stage, geography, certifications)
- Application timeline (open date, deadline, review period)
- Whether the program is recurring or one-time
- Any geographic preferences or set-asides

Scope:
- Vertical: [VERTICAL] software companies
- Stage: Pre-seed through growth; all award sizes
- Geography: US-based companies; national programs
- Entity types: For-profit and non-profit eligible
- Exclude: [EXCLUSION_CRITERIA]

If a program appears relevant but application details are not yet published, list it with a note about expected timeline. Do not speculate about eligibility criteria that aren't publicly documented.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

### Vertical-Specific Customization (Template 1)

When generating this prompt, replace `[RELEVANT_AGENCIES]` and `[AGENCY_SPECIFIC_PROGRAMS]` with agencies known to fund software in the given vertical:

| Vertical | Relevant Agencies | Agency-Specific Programs |
|----------|------------------|------------------------|
| Healthcare / Health IT | HHS, ONC, CMS, NIH, AHRQ, VA | CMS Innovation Center, ONC Health IT programs, VA Innovation Ecosystem |
| Cybersecurity | DHS, CISA, DOD, NSA, DOE | CISA programs, DOD SBIR cyber topics, DOE CESER |
| Fintech | Treasury, CFPB, SEC, FDIC, SBA | Treasury fintech initiatives, SBA programs |
| Edtech | ED, NSF, DOL | ED EdTech programs, NSF STEM education, DOL workforce |
| Climate / Clean Tech | DOE, EPA, NOAA, USDA | DOE ARPA-E, EPA SBIR, USDA Conservation Innovation |
| Govtech | GSA, OPM, OMB, DHS | GSA Technology Modernization Fund, 18F programs |
| Legal Tech | DOJ, LSC, SBA | DOJ grants, Legal Services Corp technology initiatives |
| HR / Future of Work | DOL, ED, SBA | DOL workforce innovation, ED career pathways |
| Supply Chain / Logistics | DOT, DOD, DHS, USDA | DOT SBIR, DOD logistics modernization |
| Agriculture / Food Tech | USDA, FDA, EPA | USDA SBIR, NIFA grants, FDA food safety tech |
| Real Estate / Proptech | HUD, FHFA, SBA | HUD innovation programs, FHFA fintech initiatives |
| AI / ML Infrastructure | NSF, DARPA, DOE, NIST | NSF AI institutes, DARPA programs, NIST AI standards |

---

## Template 2: State & Regional Programs

```
I am scanning for state and regional funding programs that support [VERTICAL] software startups. This research will identify programs across US states that provide early-stage funding or support for [VERTICAL] ventures.

Research state and regional funding programs:

1. First, identify the most active states for [VERTICAL] funding:
   - States with dedicated [VERTICAL] innovation programs
   - State research authority grants and investments
   - State economic development incentives for tech companies
   - University-affiliated commercialization programs

2. Then, identify regional programs:
   - Regional economic development organizations
   - Multi-state initiatives relevant to [VERTICAL]
   - Federal programs with state-allocated funding (block grants administered by states)

3. Document each program:
   - Program name and administering organization
   - State or region
   - Funding type (grant, equity investment, loan, tax credit, in-kind)
   - Amount available (per company and total program)
   - Eligibility requirements (must be in-state, stage requirements, vertical focus)
   - Application process and timeline
   - Track record (how many companies funded, notable alumni)

Scope:
- Vertical: [VERTICAL] software companies
- Geography: All US states, with focus on states most active in [VERTICAL] funding
- Stage: Pre-seed through growth
- Entity types: For-profit and non-profit eligible
- Exclude: [EXCLUSION_CRITERIA]

If a program's current status is unclear, note it as "Status unconfirmed — last active [date]" rather than assuming it continues.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 3: VC & Angel

```
I am scanning for venture capital firms and angel investors that fund [VERTICAL] software ventures. This research will map the private funding landscape so we can identify the most active and aligned sources.

Research VC and angel funding for [VERTICAL]:

1. First, identify VC firms with relevant thesis:
   - Firms that explicitly invest in [VERTICAL] software
   - Firms that have made investments in [VERTICAL] in the past 24 months
   - Sector-specific funds focused on [VERTICAL]
   - For each: firm name, thesis, check sizes, stage focus, recent relevant investments

2. Then, identify angel groups and syndicates:
   - Angel groups active in [VERTICAL]
   - Angel syndicates on platforms (AngelList, SyndicateList) focused on [VERTICAL]
   - Notable individual angels known for [VERTICAL] investments
   - For each: name, typical investment size, focus areas

3. Note emerging patterns:
   - Is [VERTICAL] seeing increased or decreased private investment?
   - New funds being raised focused on [VERTICAL]?
   - Notable exits that signal investor interest?

Scope:
- Vertical: [VERTICAL] software
- Stage: Pre-seed through Series A
- Geography: US-based investors
- Entity types: For-profit (equity) and non-profit (program-related investments where applicable)
- Exclude: [EXCLUSION_CRITERIA]

If an investor's current activity level is unclear, note the last confirmed investment date rather than assuming they are actively deploying.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 4: Accelerators

```
I am scanning for accelerator and incubator programs that accept [VERTICAL] software ventures. This research will identify programs offering funding, mentorship, and resources.

Research accelerator programs for [VERTICAL]:

1. First, identify general accelerators that accept [VERTICAL] companies:
   - Y Combinator (relevant batch companies in [VERTICAL])
   - Techstars (programs with [VERTICAL] focus or partnerships)
   - MassChallenge, 500 Global, Plug and Play, and other major programs
   - For each: investment terms, cohort size, acceptance rate, application timeline

2. Then, identify [VERTICAL]-specific accelerators:
   - Domain-specific programs built for [VERTICAL]
   - Corporate-backed accelerators in [VERTICAL] (see also Template 6)
   - University-affiliated programs with [VERTICAL] focus
   - For each: program name, sponsor, investment terms, cohort details, notable alumni

3. Document for each program:
   - Program name and operator
   - Investment amount and terms (equity %, SAFE, grant)
   - Program length and format (in-person, remote, hybrid)
   - Application timeline (next cohort deadline)
   - Relevant alumni companies in [VERTICAL]
   - Whether they accept non-profit or only for-profit

Scope:
- Vertical: [VERTICAL] software
- Geography: US-based programs or programs accepting US companies
- Entity types: For-profit and non-profit where accepted
- Exclude: [EXCLUSION_CRITERIA]

If an accelerator's next cohort hasn't been announced, note the most recent cohort date and typical cadence.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 5: Family Offices

```
I am scanning for family offices that directly invest in [VERTICAL] software ventures. This research will identify family offices with known technology or [VERTICAL] investment programs.

Research family office funding for [VERTICAL]:

1. First, identify family offices with known [VERTICAL] or technology thesis:
   - Single-family offices that have made direct [VERTICAL] software investments
   - Multi-family offices with venture allocation in [VERTICAL]
   - Family office networks that syndicate deals in [VERTICAL]

2. Then, identify access points:
   - Family office conferences and events where [VERTICAL] companies present
   - Intermediaries and platforms that connect startups with family offices
   - Networks (Tiger 21, HNWI groups) with known technology interest

3. Document for each:
   - Family office or network name (where publicly known)
   - Investment thesis or focus areas
   - Typical check size and stage preference
   - Known [VERTICAL] investments (public information only)
   - Access method (direct, via intermediary, via event)

Scope:
- Vertical: [VERTICAL] software
- Geography: US-based family offices
- Stage: Seed through Series A (family offices typically invest later than angels but some do early-stage)
- Exclude: [EXCLUSION_CRITERIA]

Family offices are private by nature. Document only publicly available information. If a family office is rumored to invest in [VERTICAL] but no public confirmation exists, note it as "Unverified — cited in [source]." Do not present unconfirmed investment activity as fact.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 6: Corporate Funding

```
I am scanning for corporate funding sources — CVC arms, innovation programs, strategic partnerships, and corporate accelerators — that invest in or partner with [VERTICAL] software ventures. This research will identify corporations actively seeking [VERTICAL] technology through investment or partnership.

Research corporate funding for [VERTICAL]:

1. First, identify corporate venture capital (CVC) arms:
   - CVCs of companies operating in [VERTICAL] ([RELEVANT_CORPORATES])
   - CVCs with thesis that includes [VERTICAL] software
   - For each: CVC name, parent company, check sizes, stage, recent [VERTICAL] investments

2. Then, identify corporate innovation and partnership programs:
   - Pilot-to-invest programs where corporates test software before investing
   - Strategic partnership programs with funding attached
   - Open innovation challenges or competitions with prizes/investment
   - Corporate accelerators (distinct from independent accelerators in Template 4)

3. Finally, identify strategic acquirers:
   - Companies that have acquired [VERTICAL] software startups in the past 24 months
   - Corporations with stated M&A interest in [VERTICAL]
   - This signals where corporates see value and may invest earlier in the pipeline

4. Document for each:
   - Program or CVC name and parent company
   - Funding type (equity, pilot contract, grant, prize, strategic investment)
   - Amount or typical deal size
   - What they look for (stage, product maturity, integration potential)
   - Application or engagement process
   - Notable portfolio companies or past participants

Scope:
- Vertical: [VERTICAL] software
- Geography: US-based corporates or those investing in US companies
- Entity types: For-profit primarily; some corporate social responsibility programs accept non-profits
- Exclude: [EXCLUSION_CRITERIA]

If a corporate program is rumored but not publicly announced, note it as unconfirmed.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

### Vertical-Specific Customization (Template 6)

Replace `[RELEVANT_CORPORATES]` with major corporations in each vertical:

| Vertical | Relevant Corporates |
|----------|-------------------|
| Healthcare / Health IT | UnitedHealth/Optum, CVS Health, Humana, Epic, Cerner, Change Healthcare |
| Cybersecurity | Palo Alto Networks, CrowdStrike, Microsoft, Google, Cisco, Fortinet |
| Fintech | JPMorgan, Goldman Sachs, Visa, Mastercard, Stripe, PayPal |
| Edtech | Pearson, McGraw Hill, 2U, Chegg, Google for Education, Microsoft Education |
| Climate / Clean Tech | Schneider Electric, Siemens, NextEra, Brookfield, Microsoft Climate |
| Govtech | Palantir, Booz Allen, SAIC, Leidos, Maximus |
| Legal Tech | Thomson Reuters, LexisNexis/RELX, Wolters Kluwer |
| HR / Future of Work | Workday, ADP, SAP SuccessFactors, LinkedIn/Microsoft |
| Supply Chain / Logistics | Flexport, FedEx, UPS, Amazon, Maersk |
| Agriculture / Food Tech | Deere, Cargill, ADM, Syngenta, Corteva |
| Real Estate / Proptech | Zillow, CoStar, CBRE, JLL, Realogy |
| AI / ML Infrastructure | NVIDIA, Google, Microsoft, Amazon, Meta, Databricks |

---

## Template 7: Policy & Regulatory Signals

```
I am scanning for policy and regulatory changes that create new funding opportunities or market demand for [VERTICAL] software ventures. This research will identify tailwinds — government actions that either directly fund or indirectly create demand for [VERTICAL] software.

Research policy and regulatory signals for [VERTICAL]:

1. First, identify recent legislation (past 24 months):
   - Federal legislation creating new funding programs relevant to [VERTICAL]
   - Appropriations that increased funding for [VERTICAL]-related agencies
   - State-level legislation affecting [VERTICAL]

2. Then, identify regulatory enforcement trends:
   - Agencies increasing enforcement in [VERTICAL] (creates compliance software demand)
   - New regulations requiring technology adoption in [VERTICAL]
   - Upcoming compliance deadlines creating urgency
   - Penalties that have increased, making compliance tools more valuable

3. Next, identify executive and agency actions:
   - Executive orders directing spending on [VERTICAL]
   - Agency strategic plans prioritizing [VERTICAL] technology
   - Federal RFIs signaling upcoming programs
   - White House initiatives relevant to [VERTICAL]

4. Finally, assess funding implications:
   - Which signals create direct funding (grants, contracts)?
   - Which create indirect demand (compliance, market pressure)?
   - What is the likely timeline for each signal to become actionable?

Scope:
- Vertical: [VERTICAL]
- Geography: Federal and state policy (all states)
- Time horizon: Past 24 months and announced upcoming actions
- Exclude: [EXCLUSION_CRITERIA]

If a policy signal is rumored but not officially announced, label it as "Unconfirmed signal" with the source. Do not present speculative policy predictions as fact.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Placeholder Reference

| Placeholder | Source |
|-------------|--------|
| `[VERTICAL]` | Current vertical being scanned |
| `[RELEVANT_AGENCIES]` | Vertical-specific agency list (see Template 1 customization table) |
| `[AGENCY_SPECIFIC_PROGRAMS]` | Vertical-specific programs (see Template 1 customization table) |
| `[RELEVANT_CORPORATES]` | Vertical-specific corporates (see Template 6 customization table) |
| `[EXCLUSION_CRITERIA]` | venture-profile.md → Exclusion Criteria section |
| `[CITATION FORMAT BLOCK]` | Contents of `references/citation-format.md` |
| `[EXAMPLE_ENTRY]` | Generate a vertical-specific example showing what a good funding source entry looks like |

## Customization Instructions

When generating prompts from these templates:

1. Read the venture profile from `inputs/venture-profile.md`
2. Determine verticals to scan (from profile or reference list)
3. For each vertical:
   a. Replace `[VERTICAL]` with the vertical name
   b. Replace agency, corporate, and program placeholders with vertical-specific entries from the customization tables
   c. Generate a vertical-specific `[EXAMPLE_ENTRY]` (not the same example for every vertical)
   d. Insert exclusion criteria from venture profile
   e. Insert citation format block from `references/citation-format.md`
4. Group all prompts by vertical in the output file

## Output File Format

Save to `discovery/{run_id}/research/00-discovery-prompts.md`:

```markdown
# Opportunity Discovery Research Prompts

**Run ID:** {run_id}
**Date Generated:** {date}
**Venture Profile:** inputs/venture-profile.md

## Profile Summary

**Primary Constraint:** Software companies only
**Scope:** {scope summary}
**Verticals:** {N} verticals being scanned
**Funding Source Types:** 7 per vertical ({N × 7} total prompts)

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save results to `discovery/{run_id}/research/00-discovery/{vertical-slug}/`
3. Name files per the convention:
   - `01-federal.md`
   - `02-state-regional.md`
   - `03-vc-angel.md`
   - `04-accelerators.md`
   - `05-family-offices.md`
   - `06-corporate.md`
   - `07-policy-regulatory.md`
4. You can run verticals in any order — run the most interesting ones first
5. Once a vertical's research is complete, it can be processed independently

---

## Vertical: {Vertical Name}

### Prompt 1: Federal Programs — {Vertical}

{Full customized prompt}

---

### Prompt 2: State & Regional — {Vertical}

{Full customized prompt}

---

(... all 7 prompts ...)

---

## Vertical: {Next Vertical}

(... repeat ...)
```
