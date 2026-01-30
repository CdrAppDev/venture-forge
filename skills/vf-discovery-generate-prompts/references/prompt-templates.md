# Discovery Prompt Templates

Prompts are generated **per vertical**. For each vertical, generate one prompt per funding source type (11 total). Replace all `[PLACEHOLDERS]` with vertical-specific content.

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
I am scanning for federal funding that targets problems in [VERTICAL]. This research will identify active and upcoming federal programs funding solutions to [VERTICAL] problems, regardless of solution type.

Research the federal funding landscape for [VERTICAL] problems.

First, identify currently active programs:
- SBIR/STTR programs at agencies relevant to [VERTICAL] ([RELEVANT_AGENCIES])
- Other federal grant programs on grants.gov matching [VERTICAL]
- Federal contract opportunities on SAM.gov for small business in [VERTICAL]
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
- Vertical: [VERTICAL] — all solution types
- Stage: Pre-seed through growth; all award sizes
- Geography: US-based companies; national programs
- Entity types: For-profit and non-profit eligible
- Exclude: [EXCLUSION_CRITERIA]

If a program appears relevant but application details are not yet published, list it with a note about expected timeline. Do not speculate about eligibility criteria that aren't publicly documented.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

### Vertical-Specific Customization (Template 1)

When generating this prompt, replace `[RELEVANT_AGENCIES]` and `[AGENCY_SPECIFIC_PROGRAMS]` with agencies known to fund solutions in the given vertical:

| Vertical | Relevant Agencies | Agency-Specific Programs |
|----------|------------------|------------------------|
| Healthcare / Health IT | HHS, ONC, CMS, NIH, AHRQ, VA | CMS Innovation Center, ONC Health IT programs, VA Innovation Ecosystem |
| Cybersecurity | DHS, CISA, DOD, NSA, DOE | CISA programs, DOD SBIR cyber topics, DOE CESER |
| Fintech | Treasury, CFPB, SEC, FDIC, SBA | Treasury fintech initiatives, SBA programs |
| Insurance / Insurtech | Treasury, FEMA, SBA, HHS | FEMA risk modeling programs, SBA disaster loan tech |
| Edtech | ED, NSF, DOL | ED EdTech programs, NSF STEM education, DOL workforce |
| Climate / Clean Tech | DOE, EPA, NOAA, USDA | DOE ARPA-E, EPA SBIR, USDA Conservation Innovation |
| Govtech / Civic Tech | GSA, OPM, OMB, DHS | GSA Technology Modernization Fund, 18F programs |
| Defense / National Security | DOD, DARPA, DIU, NSA, DHS | DIU programs, DARPA SBIR, AFWERX, NavalX, Army xTech |
| Legal Tech | DOJ, LSC, SBA | DOJ grants, Legal Services Corp technology initiatives |
| HR / Future of Work | DOL, ED, SBA | DOL workforce innovation, ED career pathways |
| Supply Chain / Logistics | DOT, DOD, DHS, USDA | DOT SBIR, DOD logistics modernization |
| Agriculture / Food Tech | USDA, FDA, EPA | USDA SBIR, NIFA grants, FDA food safety tech |
| Real Estate / Proptech | HUD, FHFA, SBA | HUD innovation programs, FHFA fintech initiatives |
| Construction Tech | DOT, DOD, DOE, GSA | DOT infrastructure tech, DOD construction modernization, GSA building tech |
| Manufacturing Tech | NIST, DOD, DOE, SBA | NIST Manufacturing Extension Partnership, DOD ManTech, DOE AMO |
| Retail / Commerce Tech | SBA, FTC, USDA | SBA small business tech, FTC consumer protection tech |
| Travel / Hospitality Tech | DOT, DOC, SBA | DOC tourism programs, SBA hospitality tech |
| Media / Entertainment Tech | NSF, NEA, FCC | NSF media innovation, NEA technology grants, FCC broadband programs |
| Telecom / Connectivity | FCC, NTIA, USDA RUS | FCC broadband programs, NTIA grants, USDA ReConnect |
| Biotech Software | NIH, NSF, DOE, BARDA | NIH SBIR bioinformatics, NSF bio programs, BARDA |
| Nonprofit / Social Impact Tech | HHS, ED, HUD, DOL, AmeriCorps | AmeriCorps innovation, HHS community programs, ED equity programs |
| AI / ML Infrastructure | NSF, DARPA, DOE, NIST | NSF AI institutes, DARPA programs, NIST AI standards |

---

## Template 2: State & Regional Programs

```
I am scanning for state and regional funding programs that support [VERTICAL] startups. This research will identify programs across US states that provide early-stage funding or support for [VERTICAL] ventures.

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
- Vertical: [VERTICAL] — all solution types
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
I am scanning for venture capital firms and angel investors that fund [VERTICAL] ventures. This research will map the private funding landscape so we can identify the most active and aligned sources.

Research VC and angel funding for [VERTICAL]:

1. First, identify VC firms with relevant thesis:
   - Firms that explicitly invest in [VERTICAL]
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
- Vertical: [VERTICAL]
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
I am scanning for accelerator and incubator programs that accept [VERTICAL] ventures. This research will identify programs offering funding, mentorship, and resources.

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
- Vertical: [VERTICAL]
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
I am scanning for family offices that directly invest in [VERTICAL] ventures. This research will identify family offices with known technology or [VERTICAL] investment programs.

Research family office funding for [VERTICAL]:

1. First, identify family offices with known [VERTICAL] or technology thesis:
   - Single-family offices that have made direct [VERTICAL] investments
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
- Vertical: [VERTICAL]
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
I am scanning for corporate funding sources — CVC arms, innovation programs, strategic partnerships, and corporate accelerators — that invest in or partner with [VERTICAL] ventures. This research will identify corporations actively seeking [VERTICAL] technology through investment or partnership.

Research corporate funding for [VERTICAL]:

1. First, identify corporate venture capital (CVC) arms:
   - CVCs of companies operating in [VERTICAL] ([RELEVANT_CORPORATES])
   - CVCs with thesis that includes [VERTICAL]
   - For each: CVC name, parent company, check sizes, stage, recent [VERTICAL] investments

2. Then, identify corporate innovation and partnership programs:
   - Pilot-to-invest programs where corporates test solutions before investing
   - Strategic partnership programs with funding attached
   - Open innovation challenges or competitions with prizes/investment
   - Corporate accelerators (distinct from independent accelerators in Template 4)

3. Finally, identify strategic acquirers:
   - Companies that have acquired [VERTICAL] startups in the past 24 months
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
- Vertical: [VERTICAL]
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
| Insurance / Insurtech | State Farm, Allstate, AIG, Munich Re, Swiss Re, Berkshire Hathaway |
| Edtech | Pearson, McGraw Hill, 2U, Chegg, Google for Education, Microsoft Education |
| Climate / Clean Tech | Schneider Electric, Siemens, NextEra, Brookfield, Microsoft Climate |
| Govtech / Civic Tech | Palantir, Booz Allen, SAIC, Leidos, Maximus |
| Defense / National Security | Lockheed Martin, Raytheon, Northrop Grumman, General Dynamics, L3Harris |
| Legal Tech | Thomson Reuters, LexisNexis/RELX, Wolters Kluwer |
| HR / Future of Work | Workday, ADP, SAP SuccessFactors, LinkedIn/Microsoft |
| Supply Chain / Logistics | Flexport, FedEx, UPS, Amazon, Maersk |
| Agriculture / Food Tech | Deere, Cargill, ADM, Syngenta, Corteva |
| Real Estate / Proptech | Zillow, CoStar, CBRE, JLL, Realogy |
| Construction Tech | Autodesk, Trimble, Procore, Oracle Construction, Bentley Systems |
| Manufacturing Tech | Siemens, Rockwell Automation, Honeywell, GE, ABB |
| Retail / Commerce Tech | Shopify, Amazon, Walmart, Target, Salesforce Commerce |
| Travel / Hospitality Tech | Booking Holdings, Marriott, Hilton, Airbnb, Expedia |
| Media / Entertainment Tech | Disney, Warner Bros Discovery, Netflix, Spotify, YouTube/Google |
| Telecom / Connectivity | AT&T, Verizon, T-Mobile, Comcast, Charter |
| Biotech Software | Illumina, Thermo Fisher, Roche, Genentech, Moderna |
| Nonprofit / Social Impact Tech | Salesforce.org, Google.org, Microsoft Philanthropies, Chan Zuckerberg Initiative |
| AI / ML Infrastructure | NVIDIA, Google, Microsoft, Amazon, Meta, Databricks |

---

## Template 7: Foundations / Philanthropic

```
I am scanning for foundation and philanthropic funding sources for [VERTICAL] ventures. This research will identify foundations, program-related investments (PRIs), and philanthropic programs that fund solutions to [VERTICAL] problems — especially relevant for non-profit and social impact ventures.

Research foundation and philanthropic funding for [VERTICAL]:

1. First, identify major foundations with [VERTICAL] programs:
   - Foundations with stated interest in [VERTICAL] or related issues
   - Foundation program areas that align with [VERTICAL] solutions
   - For each: foundation name, program area, typical grant size, eligibility

2. Then, identify program-related investments (PRIs):
   - Foundations making PRIs in [VERTICAL] technology
   - Impact investors with philanthropic capital in [VERTICAL]
   - For each: organization, PRI terms, what they've funded

3. Next, identify philanthropic programs:
   - Corporate philanthropy programs relevant to [VERTICAL] (distinct from CVC in Template 6)
   - Donor-advised fund networks with [VERTICAL] focus
   - Community foundations with technology or [VERTICAL] priorities

4. Document for each:
   - Organization name and program area
   - Funding type (grant, PRI, recoverable grant, in-kind)
   - Amount range (per grant and annual program budget)
   - Eligibility (non-profit only? for-profit eligible? fiscal sponsor accepted?)
   - Application process and timeline
   - What they've funded previously in [VERTICAL]

Scope:
- Vertical: [VERTICAL]
- Geography: US-based foundations and those funding US organizations
- Entity types: Non-profit primarily; for-profit where PRIs or social enterprise programs exist
- Exclude: [EXCLUSION_CRITERIA]

If a foundation's current program priorities are unclear, note the most recent annual report date and stated priorities at that time.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

### Vertical-Specific Customization (Template 7)

| Vertical | Relevant Foundations |
|----------|-------------------|
| Healthcare / Health IT | RWJF, Commonwealth Fund, California Health Care Foundation, Kresge |
| Cybersecurity | Hewlett Foundation (cyber policy), Ford Foundation (digital rights) |
| Fintech | Gates Foundation (financial inclusion), Omidyar Network, MetLife Foundation |
| Insurance / Insurtech | Geneva Association, Insurance Institute, Ewing Marion Kauffman |
| Edtech | Gates Foundation, Walton Family Foundation, Chan Zuckerberg Initiative, Lumina |
| Climate / Clean Tech | Bloomberg Philanthropies, Bezos Earth Fund, ClimateWorks, Hewlett Foundation |
| Govtech / Civic Tech | Knight Foundation, Omidyar Network, Bloomberg Philanthropies |
| Defense / National Security | Limited philanthropic presence; Smith Richardson Foundation, Bradley Foundation |
| Legal Tech | Ford Foundation (access to justice), Open Society Foundations, Pew Charitable Trusts |
| HR / Future of Work | Lumina Foundation, Markle Foundation, Walmart Foundation, JPMorgan Chase Foundation |
| Supply Chain / Logistics | Rockefeller Foundation (food systems), Walmart Foundation |
| Agriculture / Food Tech | Rockefeller Foundation, Gates Foundation, Walton Family Foundation |
| Real Estate / Proptech | Ford Foundation (housing), Enterprise Community Partners, Kresge Foundation |
| Construction Tech | Limited; Charles Stewart Mott Foundation (community development) |
| Manufacturing Tech | Kauffman Foundation, Manufacturing Institute foundations |
| Retail / Commerce Tech | Walmart Foundation, Target Foundation |
| Travel / Hospitality Tech | Limited philanthropic presence |
| Media / Entertainment Tech | Knight Foundation, MacArthur Foundation, Ford Foundation (media) |
| Telecom / Connectivity | Schmidt Futures, Mozilla Foundation, Ford Foundation (digital equity) |
| Biotech Software | Wellcome Trust, Howard Hughes Medical Institute, Chan Zuckerberg Initiative |
| Nonprofit / Social Impact Tech | Skoll Foundation, Omidyar Network, Draper Richards Kaplan, Echoing Green |
| AI / ML Infrastructure | Patrick J. McGovern Foundation, Mozilla Foundation, Open Philanthropy |

---

## Template 8: Government Contracts

```
I am scanning for government contract opportunities for [VERTICAL] — all solution types. Unlike grants (Template 1), these are procurement vehicles where government agencies buy products or services. This research will identify contract vehicles and procurement pathways.

Research government contract opportunities for [VERTICAL]:

1. First, identify relevant contract vehicles:
   - GSA Schedule contracts relevant to [VERTICAL]
   - Government-Wide Acquisition Contracts (GWACs) for IT
   - Agency-specific IDIQ contracts for [VERTICAL]
   - Blanket Purchase Agreements (BPAs) for [VERTICAL]
   - For each: vehicle name, administering agency, scope, how to get on schedule

2. Then, identify active procurements:
   - Current RFPs/RFQs on SAM.gov for [VERTICAL]
   - Sources sought notices and RFIs signaling upcoming procurements
   - Small business set-asides in [VERTICAL]
   - For each: opportunity title, agency, estimated value, deadline, set-aside status

3. Next, identify pathways for new companies:
   - Other Transaction Authority (OTA) programs accepting [VERTICAL] companies
   - Simplified acquisition procedures for small purchases
   - Agency innovation programs that lead to contracts (e.g., DIU for defense)
   - For each: program, how to engage, typical timeline from first contact to contract

4. Document for each:
   - Contract vehicle or opportunity name
   - Administering agency
   - Scope and eligible products/services
   - Estimated value range
   - Eligibility requirements (certifications, clearances, past performance)
   - How a new company can access this vehicle
   - Timeline from application to award

Scope:
- Vertical: [VERTICAL]
- Geography: US federal, state, and local government procurement
- Entity types: For-profit primarily (some non-profit contract vehicles exist)
- Exclude: [EXCLUSION_CRITERIA]

If a contract vehicle requires certifications or clearances, document what's needed and typical timeline to obtain them.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 9: University / Research Partnerships

```
I am scanning for university and research institution partnerships that fund or support [VERTICAL] ventures. This includes STTR programs (which require university partnership), tech transfer offices, spinout programs, and university venture funds.

Research university and research partnerships for [VERTICAL]:

1. First, identify universities with strong [VERTICAL] research:
   - Universities with top-ranked [VERTICAL]-related programs
   - Research centers or labs focused on [VERTICAL]
   - For each: university, department/center, key faculty, research focus

2. Then, identify partnership funding mechanisms:
   - STTR programs (require university co-PI) relevant to [VERTICAL]
   - University venture funds that invest in spinouts
   - Tech transfer offices with active [VERTICAL] portfolios
   - NSF I-Corps programs at universities with [VERTICAL] focus
   - For each: mechanism, funding amount, terms, how to engage

3. Next, identify research-to-startup pathways:
   - University incubators and accelerators for [VERTICAL]
   - Proof-of-concept grant programs
   - Industry-university research consortia in [VERTICAL]
   - For each: program, eligibility (must be faculty? alumni? external?), support provided

4. Document for each:
   - University or institution name
   - Program or mechanism name
   - Funding type and amount
   - Eligibility (affiliation required? open to external founders?)
   - IP terms (who owns what?)
   - Application process
   - Notable [VERTICAL] spinouts or success stories

Scope:
- Vertical: [VERTICAL]
- Geography: US universities and research institutions
- Entity types: For-profit and non-profit
- Exclude: [EXCLUSION_CRITERIA]

If a university program's current status or funding level is unclear, note the most recent confirmed activity.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 10: Competitions / Prizes

```
I am scanning for competitions, challenges, and prize programs that fund or recognize [VERTICAL] ventures. These provide non-dilutive capital and visibility.

Research competitions and prizes for [VERTICAL]:

1. First, identify major competitions:
   - XPRIZE competitions relevant to [VERTICAL]
   - challenge.gov challenges from federal agencies in [VERTICAL]
   - MIT Solve challenges relevant to [VERTICAL]
   - Hult Prize and similar global competitions with [VERTICAL] themes
   - For each: competition name, sponsor, prize amount, timeline, eligibility

2. Then, identify industry-specific competitions:
   - Trade association innovation awards with funding in [VERTICAL]
   - Corporate-sponsored challenges in [VERTICAL]
   - Pitch competitions at major [VERTICAL] conferences
   - For each: competition, sponsor, prize, how to enter

3. Next, identify recurring programs:
   - Annual innovation challenges in [VERTICAL]
   - Startup battlefield / demo day competitions that include [VERTICAL]
   - Government innovation challenges (beyond challenge.gov)
   - For each: program, frequency, next deadline, past winners

4. Document for each:
   - Competition or prize name
   - Sponsor organization
   - Prize amount and form (cash, services, equity investment, media exposure)
   - Eligibility requirements (stage, geography, entity type)
   - Application timeline and process
   - Notable past winners in [VERTICAL]

Scope:
- Vertical: [VERTICAL]
- Geography: Open to US-based companies
- Entity types: For-profit and non-profit
- Exclude: [EXCLUSION_CRITERIA]

If a competition hasn't announced its next cycle, note the most recent edition and typical cadence.

[CITATION FORMAT BLOCK]

[EXAMPLE_ENTRY]
```

---

## Template 11: Policy & Regulatory Signals

```
I am scanning for policy and regulatory changes that create new funding opportunities or market demand for [VERTICAL] ventures. This research will identify tailwinds — government actions that either directly fund or indirectly create demand for [VERTICAL].

Research policy and regulatory signals for [VERTICAL]:

1. First, identify recent legislation (past 24 months):
   - Federal legislation creating new funding programs relevant to [VERTICAL]
   - Appropriations that increased funding for [VERTICAL]-related agencies
   - State-level legislation affecting [VERTICAL]

2. Then, identify regulatory enforcement trends:
   - Agencies increasing enforcement in [VERTICAL] (creates compliance solution demand)
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
| `[RELEVANT_FOUNDATIONS]` | Vertical-specific foundations (see Template 7 customization table) |
| `[EXCLUSION_CRITERIA]` | venture-profile.md → Exclusion Criteria section |
| `[CITATION FORMAT BLOCK]` | Contents of `references/citation-format.md` |
| `[EXAMPLE_ENTRY]` | Generate a vertical-specific example showing what a good funding source entry looks like |

## Customization Instructions

When generating prompts from these templates:

1. Read the venture profile from `inputs/venture-profile.md`
2. Determine verticals to scan (from profile or operator instruction — all 22 or a subset)
3. For each vertical:
   a. Replace `[VERTICAL]` with the vertical name
   b. Replace agency, corporate, foundation, and program placeholders with vertical-specific entries from the customization tables
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
**Funding Source Types:** 11 per vertical ({N × 11} total prompts)

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
   - `07-foundations.md`
   - `08-government-contracts.md`
   - `09-university-research.md`
   - `10-competitions.md`
   - `11-policy-regulatory.md`
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

(... all 11 prompts ...)

---

## Vertical: {Next Vertical}

(... repeat ...)
```
