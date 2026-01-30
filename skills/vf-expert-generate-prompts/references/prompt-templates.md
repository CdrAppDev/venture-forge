# Expert Domain Research Prompt Templates

## Prompt Engineering Standards

Every research prompt MUST include these elements:

1. **Context block** - Why we need this research and how it will be used
2. **Scope bounds** - Domain, stage, source quality requirements, and exclusions
3. **Uncertainty permission** - Explicit instruction to flag gaps rather than speculate
4. **Sequencing** - Order of operations within the prompt (first X, then Y)
5. **Citation format** - Exact structure for every source referenced
6. **Example entry** - One concrete example of what a good result looks like

### Citation Format (use in all prompts)

Include the contents of `references/citation-format.md` in each generated prompt.

---

## Template 1: Evaluation Frameworks

```
I am building an expert review skill for [DOMAIN_NAME] that evaluates phase outputs from an AI-assisted venture creation process. This research will provide the published evaluation rubrics and scoring systems that real-world experts use to assess [DOMAIN_FOCUS].

The expert will review these output types:
[PHASE_OUTPUT_LIST]

Research published evaluation frameworks in this order:

1. First, identify formal assessment rubrics and scoring systems:
   - Published scoring criteria used by [SOURCE_TYPES_SUBSET_1]
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
- Focus on frameworks from [SOURCE_TYPES] — not startup advice blogs or opinion pieces
- Prioritize frameworks that include scoring rubrics or structured criteria
- Include both qualitative and quantitative evaluation methods
- Stage focus: pre-product and pre-revenue ventures

If a framework is widely referenced but the original source is behind a paywall or unavailable, note the framework name and what is known about it rather than speculating about its contents.

[CITATION FORMAT BLOCK]

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
```

## Template 2: Quality Standards

```
I am building an expert review skill that distinguishes between high-quality and low-quality [DOMAIN_NAME] outputs from an AI-assisted venture creation process. This research will define what "good" looks like so the expert skill can identify work that is merely complete but not strategically sound.

The expert evaluates whether outputs pass these gate criteria:
[GATE_CRITERIA]

Research quality standards and benchmarks in this order:

1. First, identify what separates good from bad in each area:
   - Published benchmarks for [DOMAIN_FOCUS]
   - Quality dimensions that experienced practitioners evaluate
   - Common quality anti-patterns (things that look right but are wrong)
   - Differences between "checked the box" and "genuinely strong"

2. Then, document specific quality indicators:
   - What does a well-reasoned [DOMAIN_NAME] analysis look like vs. a superficial one?
   - What level of evidence is expected at each stage?
   - What methodological standards apply (e.g., bottom-up vs. top-down market sizing)?
   - How do experts distinguish between rigorous analysis and motivated reasoning?

3. Finally, establish calibration benchmarks:
   - Published examples of strong vs. weak outputs (case studies, teardowns)
   - Benchmark data by vertical, stage, or geography where available
   - Industry-standard thresholds (e.g., LTV/CAC ratios, market growth rates)
   - How benchmarks differ for different venture stages

Scope:
- Focus on standards from [SOURCE_TYPES] — not anecdotal blog posts
- Prioritize standards that include concrete examples or thresholds
- Include both process quality (methodology) and output quality (results)
- Stage focus: pre-product and pre-revenue ventures

Where quality standards vary significantly by vertical or geography, note the variation rather than presenting one standard as universal.

[CITATION FORMAT BLOCK]

Example of a well-documented quality standard:
---
**Bottom-Up Market Sizing Standard**
- **Good:** Starts with identifiable customers, multiplies by realistic price point, builds up to TAM
- **Bad:** Starts with industry report total, applies arbitrary percentage ("if we get 1%...")
- **Benchmark:** Investors expect bottom-up SAM within 2x of top-down cross-check
- **Source:** First Round Capital, "The Most Common Mistake in Market Sizing"
- **Date:** 2023
- **URL:** [direct link]
- **Relevance:** Widely cited investor perspective on market sizing methodology
---
```

## Template 3: Common Failures

```
I am building an expert review skill for [DOMAIN_NAME] that catches failure patterns before they become costly. This research will document how ventures typically fail in [DOMAIN_FOCUS] so the expert skill can flag these patterns in AI-generated outputs.

The expert should be able to answer these questions about venture outputs:
[KEY_QUESTIONS]

Research documented failure modes in this order:

1. First, identify systemic failure patterns:
   - Published research on why startups fail in [DOMAIN_NAME]-related areas
   - Post-mortem analyses from failed ventures (published case studies)
   - Investor rejection patterns (what experienced funders see as disqualifying)
   - Academic studies on startup failure modes relevant to [DOMAIN_NAME]

2. Then, document specific anti-patterns in outputs:
   - What do failed ventures' [DOMAIN_NAME] documents typically look like?
   - What reasoning errors are common (confirmation bias, survivorship bias, etc.)?
   - What "tells" indicate the work is superficial vs. thorough?
   - What omissions are most dangerous (things people forget to address)?

3. Finally, categorize failures by severity:
   - Fatal flaws (venture should not proceed)
   - Serious gaps (must be addressed before next phase)
   - Minor weaknesses (note but don't block)
   - Cosmetic issues (not relevant to expert review)

Scope:
- Focus on evidence from [SOURCE_TYPES] — not survivorship-biased success stories
- Prioritize documented failures with clear causal analysis
- Include failures at the analysis/planning stage, not just execution failures
- Stage focus: pre-product and pre-revenue ventures

If failure patterns are anecdotal rather than systematically documented, label them as "Practitioner observation" rather than "Research finding."

[CITATION FORMAT BLOCK]

Example of a well-documented failure pattern:
---
**Failure Pattern: Top-Down Market Sizing Fantasy**
- **Pattern:** Venture cites large TAM from industry report, claims small percentage, presents as achievable revenue
- **Frequency:** CB Insights lists "no market need" as #1 startup failure reason (42% of failures)
- **Detection:** Look for TAM numbers from analyst reports with no bottom-up validation
- **Severity:** Serious — indicates market thesis is aspirational, not evidence-based
- **Source:** CB Insights, "Top Reasons Startups Fail"
- **Date:** 2023 update
- **URL:** [direct link]
- **Relevance:** Largest dataset of startup failure post-mortems
---
```

## Template 4: Stage-Appropriate Expectations

```
I am building an expert review skill for [DOMAIN_NAME] that calibrates expectations to the venture's actual stage. This research will define what "good enough" looks like for a pre-product, pre-revenue venture — distinct from what established companies or later-stage startups should produce.

The expert will evaluate these output types at the earliest venture stages:
[PHASE_OUTPUT_LIST]

Research stage-appropriate expectations in this order:

1. First, establish what pre-product/pre-revenue ventures can realistically produce:
   - What evidence quality is achievable before product-market fit?
   - What level of financial modeling is reasonable without revenue data?
   - What competitive analysis depth is expected before a product exists?
   - How do accelerators and early-stage funders calibrate their expectations?

2. Then, document the "good enough for this stage" standard:
   - Published guidance from [SOURCE_TYPES] on early-stage expectations
   - How evaluation criteria change across stages (idea → pre-seed → seed → A)
   - What experienced investors consider "impressive for the stage" vs. "table stakes"
   - Where do expectations differ between grant reviewers and equity investors?

3. Finally, identify over-engineering signals:
   - What work is premature at the pre-product stage?
   - What level of precision suggests the founders are planning instead of learning?
   - When does thoroughness become a red flag (spending too long on analysis vs. building)?
   - What shortcuts are acceptable or even expected at early stage?

Scope:
- Focus on expectations from [SOURCE_TYPES] — not generic "lean startup" blog advice
- Prioritize sources that explicitly address pre-product or pre-revenue context
- Include both investor expectations and grant reviewer expectations
- Note where different evaluator types (VC vs. grant reviewer vs. accelerator) diverge

Where stage-appropriate standards are not explicitly published, note that the calibration is inferred from adjacent evidence rather than directly documented.

[CITATION FORMAT BLOCK]

Example of a well-documented stage expectation:
---
**Pre-Product Market Sizing Expectations**
- **Stage:** Pre-product, pre-revenue
- **Expectation:** Bottom-up methodology with stated assumptions; exact numbers less important than logical approach
- **Over-engineering signal:** Detailed 5-year financial model with quarterly projections and no revenue data
- **Investor view:** "At pre-seed, I want to see that they understand how to think about the market, not that they have precise numbers" (First Round partner, published interview)
- **Grant view:** NSF expects "preliminary evidence" not "proof" at Phase I
- **Source:** First Round Review, "What We Look for in Pre-Seed Companies"
- **Date:** 2024
- **URL:** [direct link]
- **Relevance:** Explicitly addresses pre-product stage expectations from a major early-stage fund
---
```

## Template 5: Expert Decision Criteria

```
I am building an expert review skill for [DOMAIN_NAME] that mirrors how real decision-makers evaluate ventures. This research will document the actual decision criteria used by funders, reviewers, and advisors when they assess [DOMAIN_FOCUS] — not what they say they look for, but what research shows they actually weight.

The expert evaluates: [DOMAIN_FOCUS]

Research expert decision-making criteria in this order:

1. First, identify how decision-makers actually evaluate (not what they claim):
   - Published research on funder decision-making processes
   - Studies comparing stated vs. revealed evaluation criteria
   - Interview-based research with grant reviewers, VCs, angel investors
   - Decision-making patterns from [SOURCE_TYPES]

2. Then, document heuristics and shortcuts experts use:
   - What do experienced evaluators look at first?
   - What "quick kills" eliminate ventures from consideration?
   - What signals override detailed analysis (team quality, traction, etc.)?
   - How much time do reviewers actually spend on each section?

3. Finally, map decision criteria to specific outputs:
   - What in a capital thesis makes a funder lean in vs. pass?
   - What in a market thesis makes an investor confident vs. skeptical?
   - What in a pitch deck gets a second meeting vs. a form rejection?
   - How do decision-makers handle uncertainty and missing data?

Scope:
- Focus on research from [SOURCE_TYPES] — not pattern-matching from TechCrunch profiles
- Prioritize empirical studies over opinion pieces
- Include decision criteria from multiple evaluator types (grant panels, angel groups, VCs, accelerators)
- Stage focus: evaluating pre-product and pre-revenue ventures

Where decision criteria are based on qualitative interview research rather than quantitative studies, note the methodology and sample size.

[CITATION FORMAT BLOCK]

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
```

---

## Placeholder Reference

| Placeholder | Source |
|-------------|--------|
| `[DOMAIN_NAME]` | domain-definitions.yaml → `name` |
| `[DOMAIN_FOCUS]` | domain-definitions.yaml → `evaluation_focus` |
| `[PHASE_OUTPUT_LIST]` | Built from phase YAML `outputs` sections (name, description, format) |
| `[SOURCE_TYPES]` | domain-definitions.yaml → `source_types` (full list) |
| `[SOURCE_TYPES_SUBSET_1]` | First 2-3 entries from `source_types` relevant to the template |
| `[KEY_QUESTIONS]` | domain-definitions.yaml → `key_questions` (as bullet list) |
| `[GATE_CRITERIA]` | Built from phase YAML `gate.criteria` sections (id, description) |
| `[CITATION FORMAT BLOCK]` | Contents of `references/citation-format.md` |

## Customization Instructions

When generating prompts from these templates for a specific domain:

1. Read the domain entry from `references/domain-definitions.yaml`
2. Read all phase YAMLs listed in the domain's `phases` array
3. Replace `[DOMAIN_NAME]` with the domain's `name` field
4. Replace `[DOMAIN_FOCUS]` with the domain's `evaluation_focus` field
5. Build `[PHASE_OUTPUT_LIST]` from each phase YAML's `outputs` section — include output name, description, and format as a bullet list
6. Replace `[SOURCE_TYPES]` with the domain's `source_types` as a bullet list
7. Replace `[KEY_QUESTIONS]` with the domain's `key_questions` as a bullet list
8. Build `[GATE_CRITERIA]` from each phase YAML's `gate.criteria` section — include criterion id and description
9. Insert the full citation format block from `references/citation-format.md`
10. Review each prompt to ensure it references the specific output types from phase definitions (thesis.md, model.yaml, etc.)

## Output File Format

Save to `process/research/expert-{domain}-prompts.md`:

```markdown
# Expert Research Prompts: {Domain Name}

**Domain:** {domain_id}
**Date Generated:** {date}
**Phases Covered:** {phase list with names}

## Context

{Domain evaluation_focus. What this expert covers, which phases, what the
research builds toward (the vf-expert-{domain} review skill).}

## Phase Outputs This Expert Will Evaluate

{Bullet list built from phase YAML outputs sections:}
- **{output_name}** ({format}) — {description} — from Phase {phase_id}

## Prompts

### Prompt 1: Evaluation Frameworks

{Full customized prompt with all placeholders replaced}

---

### Prompt 2: Quality Standards

{Full customized prompt with all placeholders replaced}

---

### Prompt 3: Common Failures

{Full customized prompt with all placeholders replaced}

---

### Prompt 4: Stage-Appropriate Expectations

{Full customized prompt with all placeholders replaced}

---

### Prompt 5: Expert Decision Criteria

{Full customized prompt with all placeholders replaced}

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save results to `process/research/expert-{domain}/`
3. Name files:
   - `01-evaluation-frameworks.md`
   - `02-quality-standards.md`
   - `03-common-failures.md`
   - `04-stage-expectations.md`
   - `05-decision-criteria.md`
4. Use results to build the `vf-expert-{domain}` review skill
```
