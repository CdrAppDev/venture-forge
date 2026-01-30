# Expert Research Prompts: Funding Expert

**Domain:** funding
**Date Generated:** 2026-01-29
**Phases Covered:** 01-Capital Thesis, 08-Materials Assembly, 12-Funding Execution

## Context

The Funding Expert evaluates whether the venture's capital strategy, pitch materials, and funding approach would survive scrutiny from grant reviewers, angel investors, and VC partners at the venture's current stage. This research gathers the domain expertise needed to build the `vf-expert-funding` review skill — an expert-level evaluator that assesses strategic soundness, not just mechanical completeness.

The funding domain spans three phases: identifying what funders want (Phase 01), assembling compelling materials (Phase 08), and executing the funding process (Phase 12). The expert must understand how real funders evaluate at each stage.

## Phase Outputs This Expert Will Evaluate

**Phase 01 — Capital Thesis:**
- **capital_thesis** (markdown) — Understanding of what funders want and how to align
- **funder_profiles** (yaml) — Structured profiles of target funders

**Phase 08 — Materials Assembly:**
- **evidence_library** (yaml) — Consolidated evidence with all citations
- **pitch_deck** (markdown) — Investor pitch deck content
- **executive_summary** (markdown) — One-page executive summary
- **one_pager** (markdown) — Single page overview for quick review

**Phase 12 — Funding Execution:**
- **funding_applications** (markdown) — Submitted applications and pitches
- **data_room** (mixed) — Due diligence materials
- **funding_status** (yaml) — Application tracking and outcomes

## Prompts

### Prompt 1: Evaluation Frameworks

I am building an expert review skill for Funding Expert that evaluates phase outputs from an AI-assisted venture creation process. This research will provide the published evaluation rubrics and scoring systems that real-world experts use to assess whether the venture's capital strategy, pitch materials, and funding approach would survive scrutiny from grant reviewers, angel investors, and VC partners at the venture's current stage.

The expert will review these output types:
- Capital thesis document (funding landscape, funder profiles, alignment strategy, timeline)
- Pitch materials (deck, executive summary, one-pager, evidence library)
- Funding applications and data room materials

Research published evaluation frameworks in this order:

1. First, identify formal assessment rubrics and scoring systems:
   - Published scoring criteria used by federal grant review panels (SBIR, NSF, NIH published scoring criteria and reviewer guidelines) and VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
   - Structured evaluation frameworks from academic or professional sources
   - Rubrics that assign scores, ratings, or grades to specific dimensions
   - Decision matrices used by review committees or investment teams

2. Then, document assessment dimensions and weightings:
   - What dimensions do evaluators score (team, market, traction, etc.)?
   - How are dimensions weighted relative to each other?
   - What constitutes a passing vs. failing score on each dimension?
   - Are there knockout criteria that override overall scores?

3. Finally, extract actionable evaluation criteria:
   - Specific, observable indicators for each quality level (poor/fair/good/excellent)
   - Red flags that experienced evaluators flag immediately
   - Minimum thresholds vs. aspirational benchmarks
   - How criteria change based on venture stage (pre-product, pre-revenue, post-revenue)

Scope:
- Focus on frameworks from these source types — not startup advice blogs or opinion pieces:
  - Federal grant review rubrics (SBIR, NSF, NIH published scoring criteria and reviewer guidelines)
  - VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
  - Accelerator selection criteria (Y Combinator, Techstars, MassChallenge, domain-specific programs)
  - Angel investor decision-making research (academic studies on investment criteria)
  - Pitch deck analysis (data-backed studies on what makes decks succeed or fail)
  - Venture studio evaluation methodologies (published frameworks from established studios)
- Prioritize frameworks that include scoring rubrics or structured criteria
- Include both qualitative and quantitative evaluation methods
- Stage focus: pre-product and pre-revenue ventures

If a framework is widely referenced but the original source is behind a paywall or unavailable, note the framework name and what is known about it rather than speculating about its contents.

For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.

Example of a well-documented evaluation framework entry:
---
**NSF SBIR/STTR Phase I Review Criteria**
- **Dimensions:** Intellectual Merit (technical innovation, feasibility) and Broader Impacts (commercial potential, societal benefit)
- **Weighting:** Both dimensions carry equal weight; proposals must be strong on both
- **Scoring:** Excellent / Very Good / Good / Fair / Poor on each dimension
- **Knockout:** Proposals rated "Poor" on either dimension are not funded regardless of the other score
- **Source:** NSF PAPPG (Proposal & Award Policies & Procedures Guide), Chapter III
- **Date:** Updated January 2024
- **URL:** https://nsf.gov/publications/pub_summ.jsp?ods_key=pappg
- **Relevance:** Standard federal evaluation framework applicable to early-stage tech ventures
---

---

### Prompt 2: Quality Standards

I am building an expert review skill that distinguishes between high-quality and low-quality Funding Expert outputs from an AI-assisted venture creation process. This research will define what "good" looks like so the expert skill can identify work that is merely complete but not strategically sound.

The expert evaluates whether outputs pass these gate criteria:

**Phase 01 — Capital Thesis:**
- funders_identified: At least 2 viable funding sources identified
- criteria_documented: Funder criteria clearly documented with sources
- alignment_path: Clear path to meeting funder requirements identified
- timeline_understood: Funding timelines and decision processes documented

**Phase 08 — Materials Assembly:**
- evidence_compiled: All citations consolidated and verified
- narrative_consistent: Same statistics used across all materials
- all_claims_cited: Every claim in materials has citation
- pitch_complete: Pitch deck covers: problem, solution, market, competition, business model, team, ask

**Phase 12 — Funding Execution:**
- applications_submitted: Funding applications submitted to target sources
- traction_highlighted: Customer traction prominently featured
- data_room_ready: Due diligence materials prepared
- funding_closed: Funding commitment received (tracked separately)

Research quality standards and benchmarks in this order:

1. First, identify what separates good from bad in each area:
   - Published benchmarks for capital strategy, pitch materials, and funding execution
   - Quality dimensions that experienced practitioners evaluate
   - Common quality anti-patterns (things that look right but are wrong)
   - Differences between "checked the box" and "genuinely strong"

2. Then, document specific quality indicators:
   - What does a well-reasoned capital thesis look like vs. a superficial one?
   - What does a compelling pitch deck look like vs. a template-filled one?
   - What level of evidence is expected at each stage?
   - How do experts distinguish between rigorous funder analysis and listing every funder with a website?

3. Finally, establish calibration benchmarks:
   - Published examples of strong vs. weak pitch materials (case studies, teardowns)
   - Benchmark data by vertical, stage, or geography where available
   - Industry-standard thresholds for what funders expect to see
   - How benchmarks differ for grant applications vs. equity pitches vs. accelerator applications

Scope:
- Focus on standards from these source types — not anecdotal blog posts:
  - Federal grant review rubrics (SBIR, NSF, NIH published scoring criteria and reviewer guidelines)
  - VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
  - Accelerator selection criteria (Y Combinator, Techstars, MassChallenge, domain-specific programs)
  - Angel investor decision-making research (academic studies on investment criteria)
  - Pitch deck analysis (data-backed studies on what makes decks succeed or fail)
  - Venture studio evaluation methodologies (published frameworks from established studios)
- Prioritize standards that include concrete examples or thresholds
- Include both process quality (methodology) and output quality (results)
- Stage focus: pre-product and pre-revenue ventures

Where quality standards vary significantly by vertical or geography, note the variation rather than presenting one standard as universal.

For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.

Example of a well-documented quality standard:
---
**Capital Thesis Quality: Funder Prioritization**
- **Good:** Ranks funders by alignment fit, stage match, and timeline feasibility; explains why top choices are prioritized over others
- **Bad:** Lists every funder found in a web search with equal weight; no differentiation between realistic and aspirational targets
- **Benchmark:** Experienced fundraisers target 20-40 aligned funders, not 100+ loosely related ones
- **Source:** First Round Capital, "How to Build Your Fundraising Target List"
- **Date:** 2023
- **URL:** [direct link]
- **Relevance:** Data-backed investor guidance on fundraising strategy quality
---

---

### Prompt 3: Common Failures

I am building an expert review skill for Funding Expert that catches failure patterns before they become costly. This research will document how ventures typically fail in capital strategy, pitch materials, and funding execution so the expert skill can flag these patterns in AI-generated outputs.

The expert should be able to answer these questions about venture outputs:
- Does the capital thesis correctly identify and prioritize viable funding sources for the venture's stage and vertical?
- Is the funding landscape analysis thorough or does it list every funder with a website?
- Are funder viability assessments defensible or optimistic?
- Are pitch materials structured to address what funders actually evaluate?
- Is the funding execution plan realistic given the venture's traction and stage?
- Does the funding sequence (grants vs. equity vs. accelerators) match the venture's readiness?

Research documented failure modes in this order:

1. First, identify systemic failure patterns:
   - Published research on why startups fail in fundraising and capital strategy
   - Post-mortem analyses from failed ventures that couldn't raise funding (published case studies)
   - Investor rejection patterns (what experienced funders see as disqualifying)
   - Academic studies on startup failure modes relevant to funding and pitch materials

2. Then, document specific anti-patterns in outputs:
   - What do failed ventures' capital theses typically look like?
   - What reasoning errors are common in funding strategies (confirmation bias, survivorship bias, etc.)?
   - What "tells" indicate the capital thesis is superficial vs. thorough?
   - What omissions are most dangerous (things people forget to address in pitch materials)?

3. Finally, categorize failures by severity:
   - Fatal flaws (venture should not proceed to fundraising)
   - Serious gaps (must be addressed before submitting applications)
   - Minor weaknesses (note but don't block)
   - Cosmetic issues (not relevant to expert review)

Scope:
- Focus on evidence from these source types — not survivorship-biased success stories:
  - Federal grant review rubrics (SBIR, NSF, NIH published scoring criteria and reviewer guidelines)
  - VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
  - Accelerator selection criteria (Y Combinator, Techstars, MassChallenge, domain-specific programs)
  - Angel investor decision-making research (academic studies on investment criteria)
  - Pitch deck analysis (data-backed studies on what makes decks succeed or fail)
  - Venture studio evaluation methodologies (published frameworks from established studios)
- Prioritize documented failures with clear causal analysis
- Include failures at the analysis/planning stage, not just execution failures
- Stage focus: pre-product and pre-revenue ventures

If failure patterns are anecdotal rather than systematically documented, label them as "Practitioner observation" rather than "Research finding."

For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.

Example of a well-documented failure pattern:
---
**Failure Pattern: Spray-and-Pray Fundraising**
- **Pattern:** Venture sends identical pitch to 200+ investors with no customization for thesis alignment, stage fit, or sector focus
- **Frequency:** Fundraising advisors consistently cite this as top failure mode; DocSend data shows personalized decks get 2.3x more follow-up meetings
- **Detection:** Look for capital thesis that lists funders without alignment analysis; identical pitch materials with no funder-specific variants
- **Severity:** Serious — indicates capital strategy is volume-based rather than fit-based
- **Source:** DocSend Pitch Deck Study
- **Date:** 2023
- **URL:** [direct link]
- **Relevance:** Largest dataset of pitch deck engagement metrics
---

---

### Prompt 4: Stage-Appropriate Expectations

I am building an expert review skill for Funding Expert that calibrates expectations to the venture's actual stage. This research will define what "good enough" looks like for a pre-product, pre-revenue venture — distinct from what established companies or later-stage startups should produce.

The expert will evaluate these output types at the earliest venture stages:

**Phase 01 — Capital Thesis:**
- capital_thesis (markdown) — Understanding of what funders want and how to align
- funder_profiles (yaml) — Structured profiles of target funders

**Phase 08 — Materials Assembly:**
- evidence_library (yaml) — Consolidated evidence with all citations
- pitch_deck (markdown) — Investor pitch deck content
- executive_summary (markdown) — One-page executive summary
- one_pager (markdown) — Single page overview for quick review

**Phase 12 — Funding Execution:**
- funding_applications (markdown) — Submitted applications and pitches
- data_room (mixed) — Due diligence materials
- funding_status (yaml) — Application tracking and outcomes

Research stage-appropriate expectations in this order:

1. First, establish what pre-product/pre-revenue ventures can realistically produce:
   - What capital thesis quality is achievable before the venture has traction?
   - What pitch materials are expected when there's no product demo or revenue?
   - What funding sources are realistic before product-market fit?
   - How do accelerators and early-stage funders calibrate their expectations for pre-product ventures?

2. Then, document the "good enough for this stage" standard:
   - Published guidance from grant reviewers, VCs, and accelerators on early-stage expectations
   - How evaluation criteria change across stages (idea → pre-seed → seed → A)
   - What experienced investors consider "impressive for the stage" vs. "table stakes" in pitch materials
   - Where do expectations differ between grant reviewers (SBIR) and equity investors (angels, VCs)?

3. Finally, identify over-engineering signals:
   - What funding materials are premature at the pre-product stage?
   - What level of financial detail suggests the founders are planning instead of learning?
   - When does thoroughness in a data room become a red flag at early stage?
   - What shortcuts are acceptable or even expected in pre-seed pitch decks?

Scope:
- Focus on expectations from these source types — not generic "lean startup" blog advice:
  - Federal grant review rubrics (SBIR, NSF, NIH published scoring criteria and reviewer guidelines)
  - VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
  - Accelerator selection criteria (Y Combinator, Techstars, MassChallenge, domain-specific programs)
  - Angel investor decision-making research (academic studies on investment criteria)
  - Pitch deck analysis (data-backed studies on what makes decks succeed or fail)
  - Venture studio evaluation methodologies (published frameworks from established studios)
- Prioritize sources that explicitly address pre-product or pre-revenue context
- Include both investor expectations and grant reviewer expectations
- Note where different evaluator types (VC vs. grant reviewer vs. accelerator) diverge

Where stage-appropriate standards are not explicitly published, note that the calibration is inferred from adjacent evidence rather than directly documented.

For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.

Example of a well-documented stage expectation:
---
**Pre-Product Pitch Deck Expectations**
- **Stage:** Pre-product, pre-revenue
- **Expectation:** Problem/market slides with evidence; solution slide with concept (mockup acceptable, no demo required); team slide with relevant domain experience
- **Over-engineering signal:** Detailed product roadmap with quarterly milestones, revenue projections with basis points, fully built data room
- **Investor view:** "At pre-seed, I want to see that the founders understand the problem deeply and have a plausible path to a solution" (published YC partner guidance)
- **Grant view:** SBIR Phase I explicitly funds "feasibility research" — no working product expected
- **Source:** Y Combinator, "How to Apply to YC"
- **Date:** 2024
- **URL:** [direct link]
- **Relevance:** Largest accelerator's published guidance on pre-product expectations
---

---

### Prompt 5: Expert Decision Criteria

I am building an expert review skill for Funding Expert that mirrors how real decision-makers evaluate ventures. This research will document the actual decision criteria used by funders, reviewers, and advisors when they assess capital strategy, pitch materials, and funding readiness — not what they say they look for, but what research shows they actually weight.

The expert evaluates: Whether the venture's capital strategy, pitch materials, and funding approach would survive scrutiny from grant reviewers, angel investors, and VC partners at the venture's current stage.

Research expert decision-making criteria in this order:

1. First, identify how decision-makers actually evaluate (not what they claim):
   - Published research on funder decision-making processes
   - Studies comparing stated vs. revealed evaluation criteria among VCs, angels, and grant reviewers
   - Interview-based research with grant reviewers, VCs, angel investors
   - Decision-making patterns from federal grant review panels, VC partnerships, angel groups, and accelerator selection committees

2. Then, document heuristics and shortcuts experts use:
   - What do experienced grant reviewers look at first in an application?
   - What do VCs look at first in a pitch deck?
   - What "quick kills" eliminate ventures from consideration before a full review?
   - What signals override detailed analysis (team quality, traction, market size)?
   - How much time do reviewers actually spend on each section of a pitch or application?

3. Finally, map decision criteria to specific outputs:
   - What in a capital thesis makes a funder lean in vs. pass?
   - What in pitch materials gets a second meeting vs. a form rejection?
   - What in a grant application scores high vs. gets triaged out?
   - How do decision-makers handle uncertainty, missing data, and unproven assumptions?

Scope:
- Focus on research from these source types — not pattern-matching from TechCrunch profiles:
  - Federal grant review rubrics (SBIR, NSF, NIH published scoring criteria and reviewer guidelines)
  - VC evaluation frameworks published by firms or partners (a16z, Sequoia, First Round, sector-specific funds)
  - Accelerator selection criteria (Y Combinator, Techstars, MassChallenge, domain-specific programs)
  - Angel investor decision-making research (academic studies on investment criteria)
  - Pitch deck analysis (data-backed studies on what makes decks succeed or fail)
  - Venture studio evaluation methodologies (published frameworks from established studios)
- Prioritize empirical studies over opinion pieces
- Include decision criteria from multiple evaluator types (grant panels, angel groups, VCs, accelerators)
- Stage focus: evaluating pre-product and pre-revenue ventures

Where decision criteria are based on qualitative interview research rather than quantitative studies, note the methodology and sample size.

For every claim, provide a citation in this format:
- **Source:** [Publication or organization name]
- **Date:** [Publication date or "Accessed YYYY-MM"]
- **URL:** [Direct link to the source]
- **Relevance:** [One sentence on why this source matters]

If a data point cannot be verified with a credible source, state "Unverified - requires confirmation" rather than omitting it or presenting it as fact.

Example of a well-documented decision criterion:
---
**VC Pattern Matching on Team**
- **Criterion:** Team background and domain expertise
- **Stated importance:** VCs rank "team" #1 in surveys (Gompers et al., 2020)
- **Revealed importance:** Actual investment decisions correlate more with market size than team in early rounds (Bernstein et al., 2017)
- **Implication:** Expert review should weight market evidence alongside team, not defer to team quality alone
- **Source:** Bernstein, Korteweg, & Laws, "Attracting Early-Stage Investors: Evidence from a Randomized Field Experiment," Journal of Finance
- **Date:** 2017
- **URL:** [direct link]
- **Relevance:** Rare experimental study revealing gap between stated and actual VC decision criteria
---

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save results to `process/research/expert-funding/`
3. Name files:
   - `01-evaluation-frameworks.md`
   - `02-quality-standards.md`
   - `03-common-failures.md`
   - `04-stage-expectations.md`
   - `05-decision-criteria.md`
4. Use results to build the `vf-expert-funding` review skill
