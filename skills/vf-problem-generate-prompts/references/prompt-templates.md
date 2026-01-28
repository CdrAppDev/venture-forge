# Problem Thesis Prompt Templates

## Prompt Engineering Standards

Every research prompt MUST include these elements:

1. **Context block** - Why we need this research and how it will be used
2. **Scope bounds** - Time range, geography, segment, and exclusions
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

## Prompt 1: Problem Prevalence and Severity

```
I am building a problem thesis for a venture addressing [PROBLEM] in [VERTICAL/MARKET]. This research will establish whether the problem is large enough and painful enough to build a business around. The findings will be used in investor materials, so every claim must be defensible.

Research the prevalence and severity of [PROBLEM] in [VERTICAL/MARKET].

First, establish the scale of the problem:
- How many organizations/people are affected (absolute numbers and percentages)
- Geographic distribution (national, concentrated in certain regions)
- Segment breakdown (by size, type, or other relevant dimension)

Then, quantify the severity:
- Financial impact per affected organization (direct costs, losses)
- Operational impact (time lost, productivity reduction, service disruption)
- Outcome impact (patient outcomes, safety incidents, quality metrics)
- Frequency of occurrence (daily burden vs. catastrophic events)

Finally, establish the trajectory:
- Is the problem getting worse, stable, or improving? Over what timeframe?
- What forces are driving the trend?
- Projections from credible sources (analyst reports, government data)

Scope:
- United States focus, with international comparisons if illuminating
- Data from [CURRENT YEAR - 3] through [CURRENT YEAR]
- Prioritize government sources (HHS, GAO, CMS) and peer-reviewed research over vendor-sponsored studies

If statistics conflict across sources, present both figures and note the discrepancy. Do not average or reconcile conflicting data—flag it for human review.

[CITATION FORMAT BLOCK]

Example of a well-documented statistic:
---
**Rural hospital cybersecurity staffing:**
- 67% of rural hospitals have no dedicated cybersecurity staff
- Source: American Hospital Association Rural Health Survey, March 2024
- URL: [direct link]
- Relevance: Establishes the resource gap that makes rural hospitals uniquely vulnerable
---
```

## Prompt 2: Customer Voice and Pain Points

```
I need to understand how [TARGET CUSTOMERS] experience and describe [PROBLEM] in their own words. This research will inform our messaging, product design, and investor narrative. Authentic customer language is more convincing than statistics alone.

Search these sources for firsthand accounts:
- Industry forums and professional communities
- Product reviews on G2, Capterra, or relevant platforms
- Reddit discussions in relevant subreddits (identify specific subreddits)
- Support forums and help desk discussions
- LinkedIn posts and articles from practitioners
- Twitter/X threads from [TARGET CUSTOMER] professionals
- Conference presentations or panel discussions (transcripts, summaries)

For each source, capture:
1. Direct quotes (exact language, not paraphrased)
2. The context (what prompted the comment, what role the person holds)
3. The emotional register (frustration, resignation, urgency, fear)
4. Any workarounds or coping mechanisms described
5. What they wish existed or what they've asked for

Then, synthesize patterns:
- Most common complaints (ranked by frequency across sources)
- Language patterns (what words and phrases recur)
- Unmet needs that multiple people express independently
- Differences in pain by segment (small vs. large, urban vs. rural)

Scope:
- Posts and reviews from [CURRENT YEAR - 2] through [CURRENT YEAR]
- Focus on [TARGET CUSTOMERS] specifically, not adjacent roles
- Minimum 10 distinct voices from at least 3 different source types

If you cannot find sufficient firsthand accounts (fewer than 5 distinct voices), state this explicitly. A thin customer voice finding is more useful than padded results.

[CITATION FORMAT BLOCK]

For quotes, use this format:
---
**Source:** Reddit r/healthIT, user [anonymized role description]
**Date:** September 2024
**Quote:** "We got hit with ransomware last year and had to go back to paper for three weeks. We're a 40-bed hospital—we don't have an IT security team. It's just me and I also do the phones."
**Context:** Thread about hospital cybersecurity challenges
**Emotional register:** Resignation, overwhelm
**Workaround mentioned:** Manual/paper fallback processes
---
```

## Prompt 3: Current Solutions and Their Shortcomings

```
I need to understand what [TARGET CUSTOMERS] currently use to address [PROBLEM], and where those solutions fall short. This research will define our competitive positioning and validate that a gap exists for our solution.

Research current approaches in this order:

1. First, map the solution landscape:
   - Commercial software products marketed to [TARGET CUSTOMERS] for this problem
   - Managed service providers offering relevant services
   - Government or nonprofit programs providing assistance
   - Manual processes and workarounds commonly used
   - "Do nothing" prevalence (what percentage simply accept the risk)

2. Then, for each major solution category, document:
   - Key vendors/providers and their market position
   - Pricing model and typical cost
   - What it covers and what it doesn't
   - Target customer profile (who it's designed for vs. who actually uses it)
   - Known limitations based on reviews, case studies, or analyst reports

3. Finally, identify the gaps:
   - What segments are underserved (and why)
   - Common complaints about existing solutions (from reviews, forums)
   - Features or capabilities that are missing
   - Barriers to adoption (cost, complexity, staffing, integration)

Scope:
- Focus on solutions accessible to [TARGET CUSTOMERS] (not enterprise-only products)
- Include both technology solutions and service-based approaches
- Current market (products available now, not announced/upcoming)

Distinguish between "no solution exists" and "solutions exist but aren't adopted." These are different problems requiring different responses. If adoption data is available, include it.

[CITATION FORMAT BLOCK]
```

## Prompt 4: Cost of the Status Quo

```
I need to quantify what [PROBLEM] costs [TARGET CUSTOMERS] today, both in direct expenses and hidden costs. This research provides the economic justification for our venture—if we can't show the cost exceeds our price, the business case fails.

Research costs in this order:

1. First, document direct financial costs:
   - Average cost per incident or occurrence
   - Annual spending on current (inadequate) solutions
   - Insurance premium impacts
   - Regulatory fines and penalties incurred

2. Then, quantify indirect costs:
   - Staff time spent on workarounds or manual processes
   - Opportunity costs (what they can't do while dealing with this)
   - Reputational damage (quantified where possible)
   - Downstream effects on revenue or operations

3. Finally, aggregate to market level:
   - Total cost across all [TARGET CUSTOMERS] (build from per-unit to market)
   - Cost trajectory (growing, stable, declining)
   - Industry benchmarks for this cost category
   - Comparison to what adequate solutions would cost

Scope:
- United States market
- Focus on [TARGET CUSTOMER SEGMENT] specifically, not the broader market
- Use the most recent data available; flag anything older than 3 years

Where exact figures aren't available, provide ranges and explain the methodology. For example: "Based on [X hospitals] × [average cost per incident] × [incident rate], the estimated annual cost is $Y-Z." Show your work so it can be validated.

[CITATION FORMAT BLOCK]
```

## Prompt 5: Regulatory and Compliance Context (If Applicable)

```
I need to understand the regulatory environment surrounding [PROBLEM] in [VERTICAL]. Regulatory pressure is often a key buying trigger—organizations buy compliance solutions when penalties become real. This research will determine if regulation is a tailwind for our venture.

Research in this order:

1. First, identify the regulatory framework:
   - Relevant federal regulations and their specific requirements
   - State-level regulations (focus on [STATE] and states with strictest requirements)
   - Industry standards and frameworks (voluntary but influential)
   - Upcoming or proposed regulations in the pipeline

2. Then, document enforcement activity:
   - Recent enforcement actions (last 3 years)
   - Penalty amounts imposed
   - Trends in enforcement (increasing, decreasing, shifting focus)
   - High-profile cases that changed industry behavior

3. Finally, assess the compliance landscape:
   - Current compliance rates among [TARGET CUSTOMERS]
   - Common compliance gaps
   - Cost of achieving compliance vs. cost of non-compliance
   - Whether compliance requirements are expected to tighten

Scope:
- US federal and [STATE] state regulations
- Current enforcement environment ([CURRENT YEAR - 2] through [CURRENT YEAR])
- Focus on regulations that specifically affect [TARGET CUSTOMERS]

If enforcement data is not publicly available for specific customer segments, note this gap. General enforcement trends are useful but should be labeled as such, not presented as segment-specific data.

[CITATION FORMAT BLOCK]
```

## Customization Instructions

When generating prompts from these templates:

1. Replace `[PROBLEM]`, `[VERTICAL/MARKET]`, `[TARGET CUSTOMERS]`, `[STATE]` with specifics from the capital thesis
2. Insert the Citation Format Block (from the standards section above) into each prompt
3. Add context from the capital thesis to narrow the scope (e.g., "critical access hospitals under 100 beds")
4. Set the current year for time-scoping
5. Add vertical-specific search terms and data sources
6. For Prompt 2, identify specific subreddits, forums, and review platforms relevant to the vertical
7. Omit Prompt 5 if regulatory context is not relevant to the problem
8. If the capital thesis identifies specific competitors, add them to Prompt 3

## Output File Format

Save to `{project}/research/02-problem-prompts.md`:

```markdown
# Problem Thesis Research Prompts

**Project:** [Project Name]
**Date Generated:** [Date]
**Capital Thesis Reference:** phases/01-capital/thesis.md

## Context

[Brief summary of the problem being validated, the target customer, and relevant constraints from the capital thesis]

## Prompts

### Prompt 1: Problem Prevalence and Severity

[Full customized prompt with all placeholders replaced and citation format included]

---

### Prompt 2: Customer Voice and Pain Points

[Full customized prompt]

---

### Prompt 3: Current Solutions and Their Shortcomings

[Full customized prompt]

---

### Prompt 4: Cost of the Status Quo

[Full customized prompt]

---

### Prompt 5: Regulatory and Compliance Context

[Full customized prompt, or "N/A - not applicable for this vertical"]

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save each research result as a separate file in `research/02-problem/`
3. Name files: `01-prevalence.md`, `02-customer-voice.md`, `03-current-solutions.md`, `04-cost.md`, `05-regulatory.md`
4. Once all research is complete, notify for processing
```
