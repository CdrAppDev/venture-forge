---
name: vf-discovery-score
description: >
  Score and rank discovered funded problems. Evaluates each opportunity
  on funding certainty, problem clarity, timing, magnitude, competition,
  and venture potential. Produces a ranked discovery report with rationale.
  Activate after vf-discovery-process-research.
license: MIT
metadata:
  version: "1.0.0"
  phase: 00-discovery
  when: after_processing
---

# Opportunity Discovery: Score and Rank

Score each discovered funded problem and produce a ranked discovery report for human gate review.

## Prerequisites

- Opportunity profiles at `discovery/{run_id}/opportunities/`
- Venture profile at `inputs/venture-profile.md`

## Workflow

1. **Read** venture profile from `inputs/venture-profile.md`
2. **Read** all opportunity profiles from `discovery/{run_id}/opportunities/`
3. **Score** each opportunity on 6 dimensions using the rubric in `references/scoring-rubric.md`
4. **Rank** opportunities by composite score
5. **Write** discovery report with scores, rationale, and recommendation
6. **Save** to `discovery/{run_id}/discovery-report.md`

## Scoring Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Funding Certainty | 25% | Is the funding announced, open, and documented? Or speculative? |
| Problem Clarity | 25% | Is the funded problem well-defined? Are affected populations and pain points clear? |
| Timing | 15% | Are deadlines approaching? Is the program in early or late cycle? |
| Magnitude | 15% | Total funding potential across all sources in the bundle |
| Competition | 10% | How many applicants are likely? How specific are the requirements? |
| Venture Potential | 10% | Is there a plausible venture (any type) that could address this problem? |

## Output

File: `discovery/{run_id}/discovery-report.md`

```markdown
# Discovery Report: {Run ID}

**Date:** {date}
**Venture Profile:** inputs/venture-profile.md
**Opportunities Evaluated:** {count}

## Rankings

| Rank | Opportunity | Score | Top Signal | Risk |
|------|-------------|-------|------------|------|
| 1 | {name} | {score}/100 | {why it scored high} | {main risk} |
| 2 | {name} | {score}/100 | {why} | {risk} |

## Detailed Scores

### 1. {Opportunity Name} — {Score}/100

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Funding Certainty | {}/25 | {evidence} |
| Problem Clarity | {}/25 | {evidence} |
| Timing | {}/15 | {evidence} |
| Magnitude | {}/15 | {evidence} |
| Competition | {}/10 | {evidence} |
| Venture Potential | {}/10 | {evidence} |

**Recommendation:** {Pursue / Investigate further / Pass}
**Key risk:** {biggest uncertainty}

[Repeat for each opportunity]

## Opportunities Not Scored

{Any opportunities excluded by venture profile constraints, with reason}
```

## Quality Checklist

- [ ] Every opportunity from the processing step is either scored or excluded with reason
- [ ] Scoring rationale cites specific evidence from opportunity profiles
- [ ] Funding Certainty scores distinguish between announced programs, rumored programs, and speculative sources
- [ ] Problem Clarity scores assess how well-defined the funded problem is
- [ ] Composite scores are mathematically correct given dimension weights
- [ ] Rankings are consistent with scores (no manual overrides without explanation)
- [ ] Report is readable by a human making go/no-go decisions

See `references/scoring-rubric.md` for detailed scoring criteria per dimension.
