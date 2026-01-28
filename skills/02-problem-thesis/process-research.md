# Skill: Problem Thesis - Process Research

**Version:** 1.0.0
**Phase:** 02-problem
**When:** After research

## Purpose

Process the uploaded Claude Deep Research results into a validated Problem Thesis with structured evidence and extracted customer voice.

## Prerequisites

- Capital thesis exists at `{project}/phases/01-capital/thesis.md`
- Research results uploaded to `{project}/research/02-problem/`
- Research prompts file exists at `{project}/research/02-problem-prompts.md`

## Instructions

### Step 1: Read All Inputs

Read in order:
1. Capital thesis: `{project}/phases/01-capital/thesis.md`
2. Research prompts: `{project}/research/02-problem-prompts.md`
3. All research results in: `{project}/research/02-problem/`

### Step 2: Extract and Validate Evidence

For each research result file:

1. **Identify all cited statistics and claims**
2. **Verify citations are present** (source, date, URL where available)
3. **Categorize evidence** by type:
   - Prevalence (how widespread)
   - Severity (how painful)
   - Cost (quantified impact)
   - Customer voice (direct quotes)
   - Current solutions (what exists)
   - Gaps (what's missing)

4. **Flag any uncited claims** - these cannot be used in thesis

### Step 3: Synthesize Problem Statement

Write a clear problem statement that:
- States the problem in one sentence
- Identifies who experiences it
- Quantifies the impact
- Is backed by the evidence collected

Format:
```
[WHO] experiences [PROBLEM], resulting in [QUANTIFIED IMPACT].
Currently, [CURRENT STATE], leaving [GAP].
```

### Step 4: Build Evidence Structure

Create `evidence.yaml` with this structure:

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

### Step 5: Extract Customer Voice

Create `customer-voice.md` with:

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

### Step 6: Write Problem Thesis

Create `thesis.md` with:

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

### Step 7: Create Output Directory

Ensure all outputs are in `{project}/phases/02-problem/`:
- `thesis.md`
- `evidence.yaml`
- `customer-voice.md`

## Output Format

| File | Location | Format |
|------|----------|--------|
| Problem Thesis | `{project}/phases/02-problem/thesis.md` | Markdown |
| Evidence | `{project}/phases/02-problem/evidence.yaml` | YAML |
| Customer Voice | `{project}/phases/02-problem/customer-voice.md` | Markdown |

## Quality Checklist

- [ ] Problem statement is one clear sentence
- [ ] All statistics have citations (source, date, URL)
- [ ] Minimum 3 prevalence citations
- [ ] Minimum 3 severity citations
- [ ] Minimum 2 cost citations
- [ ] Minimum 5 customer voice quotes with sources
- [ ] Current solutions documented with limitations
- [ ] Gaps clearly identified
- [ ] Capital alignment explicitly stated
- [ ] Gate criteria checklist included in thesis

## Version History

### 1.0.0 - 2025-01-28
- Initial version
- Three output files: thesis.md, evidence.yaml, customer-voice.md
- Explicit citation minimums per category
- Gate criteria checklist embedded in thesis
