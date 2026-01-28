# Capital Thesis Output Templates

## funder-profiles.yaml Structure

```yaml
project: "[Project Name]"
date: "[Date]"
total_funders_analyzed: [N]
viable_funders: [N]

funders:
  - name: "[Funder Name]"
    type: "[Grant/Equity/Accelerator/Loan]"
    viable: true/false
    viability_rationale: "[One sentence on why viable or not]"
    confidence: "high/medium/low"

    overview:
      description: "[What this funder does]"
      focus_areas: ["area1", "area2"]
      geography: "[Geographic focus]"
      stage: "[Pre-seed/Seed/Series A/Any]"

    funding:
      amount_range: "[e.g., $25K-$50K or $200K-$300K]"
      type: "[Grant/Equity/Convertible note/etc.]"
      source: "[Source name]"
      date: "[Source date]"
      url: "[Source URL]"

    criteria:
      stated:
        - criterion: "[What they say they look for]"
          source: "[Citation]"
          date: "[Date]"
          url: "[URL]"
      inferred:
        - criterion: "[Pattern from portfolio]"
          evidence: "[What we observed]"
          confidence: "medium/low"
          note: "Inferred from portfolio, not confirmed criteria"

    process:
      application_type: "[Open/Invite-only/Rolling/Cycle-based]"
      timeline: "[Application to decision timeline]"
      deadlines: ["List specific dates if known"]
      stages: ["Stage 1", "Stage 2"]
      decision_makers:
        - name: "[Name if public]"
          role: "[Role]"
          source: "[Citation]"
      timeline_source: "[Citation for timeline info]"
      timeline_confidence: "high/medium/low/unknown"

    portfolio:
      - company: "[Company name]"
        relevance: "[Why relevant to our venture]"
        amount: "[If known]"
        date: "[Investment date]"
        source: "[Citation]"

    alignment:
      strengths:
        - "[What we already meet]"
      gaps:
        - gap: "[What we lack]"
          severity: "blocking/significant/minor"
          resolution: "[What phase or action addresses this]"
      overall_fit: "strong/moderate/weak"

  # Repeat for each funder
```

## thesis.md Structure

```markdown
# Capital Thesis: [Project Name]

**Project:** [Project Name]
**Version:** 1.0
**Date:** [Date]
**Status:** Pending Review

## Executive Summary

[2-3 sentences: What funders are available, what they want, and whether our venture can align. State the conclusion up front.]

## Funding Landscape

[Overview of the funding environment for this vertical. How many active funders, what they're focused on, recent trends. All cited.]

### Active Funding Sources

| Funder | Type | Amount | Stage | Viability |
|--------|------|--------|-------|-----------|
| [Name] | [Type] | [Range] | [Stage] | Strong/Moderate/Weak |

## Funder Deep Dives

### [Funder 1 Name]

**Type:** [Grant/Equity/etc.]
**Amount:** [Range]
**Viability:** [Strong/Moderate/Weak]

**What They Fund:** [Description with citations]

**Criteria:**
- [Criterion 1] (Source: [citation])
- [Criterion 2] (Source: [citation])

**Our Alignment:**
- Strengths: [What we meet]
- Gaps: [What we lack and how to address]

**Timeline:** [Application process and dates]

### [Funder 2 Name]

[Same structure]

## Alignment Strategy

[How we position this venture to meet funder requirements. What must be true by the time we apply. Which gaps are addressed in which phases.]

### Priority Alignment Actions

1. [Action 1] — Addresses [Funder X] requirement for [Y]
2. [Action 2] — Addresses [Funder X, Z] requirement for [Y]

## Funding Timeline

| Funder | Next Deadline | Decision Timeline | Our Readiness |
|--------|--------------|-------------------|---------------|
| [Name] | [Date or "Rolling"] | [Timeline] | [Ready/Not yet - needs X] |

## Evidence Summary

- **Funders analyzed:** [N]
- **Viable funders:** [N]
- **Total citations:** [N]
- **Landscape citations:** [N]
- **Thesis/criteria citations:** [N]
- **Portfolio citations:** [N]
- **Requirements citations:** [N]

## Gate Criteria Checklist

- [ ] At least 2 viable funding sources identified
- [ ] Funder criteria clearly documented with sources
- [ ] Clear path to meeting funder requirements identified
- [ ] Funding timelines and decision processes documented

---

*Full funder data: funder-profiles.yaml*
*Processing decisions: processing-log.md*
```

## processing-log.md Structure

```markdown
# Processing Log: Capital Thesis

**Project:** [Project Name]
**Date:** [Date]
**Processor:** Claude Code (vf-capital-process-research v1.0.0)

## Files Read

| # | File | Path | Word Count |
|---|------|------|------------|
| 1 | [Filename] | research/01-capital/[filename] | ~[N] words |
| 2 | [Filename] | research/01-capital/[filename] | ~[N] words |
| 3 | [Filename] | inputs/funder-criteria.md | ~[N] words |

**Total files read:** [N]
**Total approximate words processed:** [N]

## Evidence Included

| # | Evidence | Source | Used In | Reason |
|---|----------|--------|---------|--------|
| 1 | [Statistic or claim] | [Source, Date] | funder-profiles.yaml / thesis.md | [Why included: meets criteria, strong source, etc.] |
| 2 | [Statistic or claim] | [Source, Date] | funder-profiles.yaml / thesis.md | [Why included] |

**Total evidence items included:** [N]

## Evidence Excluded

| # | Evidence | Source | Reason for Exclusion |
|---|----------|--------|---------------------|
| 1 | [Statistic or claim] | [Source, Date] | [Duplicate / Uncited / Irrelevant / Contradicted by stronger source / Outside scope] |

**Total evidence items excluded:** [N]

## Conflicts Found

| # | Topic | Value A | Source A | Value B | Source B | Resolution |
|---|-------|---------|----------|---------|----------|------------|
| 1 | [e.g., "SCRA grant amount"] | [Value] | [Source] | [Value] | [Source] | [Both presented / Led with A because...] |

**Total conflicts found:** [N]

## Gaps Identified

| # | Gap | Category | Impact |
|---|-----|----------|--------|
| 1 | [What's missing] | [Citation category] | [Minimum not met / Data incomplete / Timeline unknown] |

**Total gaps identified:** [N]

## Decisions Made

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | [e.g., "Led with RHTP as primary funder over SCRA"] | [e.g., "Larger funding amount and stronger alignment with cybersecurity vertical"] |
| 2 | [e.g., "Marked CISA as viable despite thin data"] | [e.g., "Program criteria align well; confidence set to low pending further research"] |

**Total processing decisions:** [N]

## Citation Minimum Status

| Category | Required | Found | Status |
|----------|----------|-------|--------|
| Funder landscape | 3 | [N] | MET/NOT MET |
| Investment thesis / criteria | 2 | [N] | MET/NOT MET |
| Portfolio / past investments | 3 | [N] | MET/NOT MET |
| Requirements and process | 2 | [N] | MET/NOT MET |
```
