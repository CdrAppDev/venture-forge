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

[One paragraph stating the problem clearly, with key statistics inline]

## Who Experiences This Problem

[Description of affected population with size/scope statistics]

## Severity and Impact

[Quantified impact - financial, time, outcomes]

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

[Summary of how customers describe this problem, with representative quotes]

## Cost of Status Quo

[What it costs to not solve this problem]

## Alignment with Capital Thesis

[How this problem aligns with Phase 1 funder criteria]

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
```
