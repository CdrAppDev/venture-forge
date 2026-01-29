# Problem Thesis Output Templates

## evidence.yaml Structure

```yaml
problem_statement: "[One sentence problem statement]"

prevalence:
  summary: "[How widespread is this problem]"
  statistics:
    - stat: "[Specific statistic]"
      source: "[Source name]"
      date: "[Publication date]"
      url: "[URL if available]"
    # Minimum 3 statistics

severity:
  summary: "[How painful is this problem]"
  statistics:
    - stat: "[Specific statistic]"
      source: "[Source name]"
      date: "[Publication date]"
      url: "[URL if available]"
    # Minimum 3 statistics

cost_of_status_quo:
  summary: "[Quantified cost of not solving]"
  statistics:
    - stat: "[Specific statistic]"
      source: "[Source name]"
      date: "[Publication date]"
      url: "[URL if available]"
    # Minimum 2 statistics

current_solutions:
  - name: "[Solution name]"
    type: "[Software/Service/Manual process]"
    limitations: "[Why it's not enough]"
    source: "[How we know this]"

gaps:
  - gap: "[What's missing]"
    evidence: "[How we know]"
    source: "[Citation]"

capital_alignment:
  aligned: true/false
  explanation: "[How this problem aligns with funder criteria]"
```

## customer-voice.md Structure

```markdown
# Customer Voice: [Problem]

## How Customers Describe This Problem

### Theme 1: [Common theme]

> "[Direct quote]"
> — Source: [Forum/Review/Discussion], [Date]

> "[Another quote]"
> — Source: [Forum/Review/Discussion], [Date]

### Theme 2: [Another theme]

[Continue with grouped quotes]

## Common Language and Terminology

- **[Term]**: How customers refer to [concept]
- **[Term]**: How customers describe [pain point]

## Emotional Intensity

[Assessment of how frustrated/urgent customers sound, with supporting quotes]

## Workarounds Attempted

- [Workaround 1]: "[Quote about trying this]" — Source
- [Workaround 2]: "[Quote about trying this]" — Source
```

## thesis.md Structure

```markdown
# Problem Thesis: [Problem Name]

**Project:** [Project Name]
**Version:** 1.0
**Date:** [Date]
**Status:** Pending Review

## Problem Statement

[One paragraph stating the problem clearly, with key statistics inline. EVERY statistic must have an inline citation in the format (Source Name, Date). Example: "68% have no dedicated cybersecurity leader (Black Book Research, June 2025), 73% lack adequate defenses (Black Book Research, June 2025)"]

## Who Experiences This Problem

[Description of affected population with size/scope statistics. Every statistic must include inline citation: (Source Name, Date)]

## Severity and Impact

[Quantified impact - financial, time, outcomes. Every metric must include inline citation: (Source Name, Date)]

### Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| [Metric] | [Value] | [Source, Date] |

## Current State

### Existing Solutions

[What solutions exist today]

### Why They're Insufficient

[Gaps and limitations, cited]

## Customer Voice

[Summary of how customers describe this problem, with representative quotes. Each quote must include speaker name, title, organization, and publication source inline.]

## Cost of Status Quo

[What it costs to not solve this problem. All cost figures must include inline citations: (Source Name, Date)]

## Alignment with Capital Thesis

[How this problem aligns with Phase 1 funder criteria. Reference specific funder requirements with citations.]

## Inline Citation Standard

**MANDATORY:** Every factual claim in this thesis must have an inline citation in the format `(Source Name, Date)`. A thesis with fewer than 80% of claims cited inline is incomplete. The sources.md file provides full bibliographic detail; thesis.md provides inline attribution for readability.

## Evidence Summary

- **Prevalence citations:** [X]
- **Severity citations:** [X]
- **Customer voice sources:** [X]
- **Total unique sources:** [X]

## Gate Criteria Checklist

- [ ] Problem clearly stated with third-party evidence
- [ ] Affected population sized with sources
- [ ] Cost/impact quantified
- [ ] Customer voice captured from public sources
- [ ] Aligned with capital thesis

---

*Full evidence: evidence.yaml*
*Customer voice detail: customer-voice.md*
*Processing decisions: processing-log.md*
```

## processing-log.md Structure

```markdown
# Processing Log: Problem Thesis

**Project:** [Project Name]
**Date:** [Date]
**Processor:** Claude Code (vf-problem-process-research v1.0.0)

## Files Read

| # | File | Path | Word Count |
|---|------|------|------------|
| 1 | [Filename] | research/02-problem/[filename] | ~[N] words |
| 2 | [Filename] | research/02-problem/[filename] | ~[N] words |
| 3 | [Filename] | phases/01-capital/thesis.md | ~[N] words |

**Total files read:** [N]
**Total approximate words processed:** [N]

## Evidence Included

| # | Evidence | Source | Used In | Reason |
|---|----------|--------|---------|--------|
| 1 | [Statistic or claim] | [Source, Date] | evidence.yaml / thesis.md / customer-voice.md | [Why included] |

**Total evidence items included:** [N]

## Evidence Excluded

| # | Evidence | Source | Reason for Exclusion |
|---|----------|--------|---------------------|
| 1 | [Statistic or claim] | [Source, Date] | [Duplicate / Uncited / Irrelevant / Contradicted / Outside scope] |

**Total evidence items excluded:** [N]

## Customer Voice Decisions

| # | Quote | Source | Included | Theme Assigned | Rationale |
|---|-------|--------|----------|----------------|-----------|
| 1 | "[Quote excerpt]" | [Source] | Yes/No | [Theme name or N/A] | [Why included/excluded, theme grouping logic] |

**Total quotes found:** [N]
**Total quotes included:** [N]
**Total themes identified:** [N]
**Theme grouping rationale:** [Brief explanation of how themes were determined]

## Conflicts Found

| # | Topic | Value A | Source A | Value B | Source B | Resolution |
|---|-------|---------|----------|---------|----------|------------|
| 1 | [e.g., "Breach cost figure"] | [Value] | [Source] | [Value] | [Source] | [Both presented / Led with A because...] |

**Total conflicts found:** [N]

## Gaps Identified

| # | Gap | Category | Impact |
|---|-----|----------|--------|
| 1 | [What's missing] | [Citation category] | [Minimum not met / Data incomplete] |

**Total gaps identified:** [N]

## Decisions Made

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | [e.g., "Used HHS figure over vendor study for breach cost"] | [e.g., "Government source more credible for investor materials"] |
| 2 | [e.g., "Grouped quotes into 3 themes instead of 4"] | [e.g., "Two candidate themes had only 1 quote each; merged into broader theme"] |

**Total processing decisions:** [N]

## Citation Minimum Status

| Category | Required | Found | Status |
|----------|----------|-------|--------|
| Prevalence | 3 | [N] | MET/NOT MET |
| Severity | 3 | [N] | MET/NOT MET |
| Cost of status quo | 2 | [N] | MET/NOT MET |
| Customer voice quotes | 5 | [N] | MET/NOT MET |
| Current solutions | 1 | [N] | MET/NOT MET |
| Gaps | 1 | [N] | MET/NOT MET |
```
