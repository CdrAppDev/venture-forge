# Capital Thesis Prompt Templates

## Prompt 1: Funding Landscape

```
Research the funding landscape for [VERTICAL/STAGE] ventures.

I need:
- Active investors, grants, and accelerators in this space
- Their stated investment thesis or funding criteria
- Recent investments or grants made (last 2 years)
- Funding amounts and stages they focus on

Provide citations for all claims including source name, date, and URL.
```

## Prompt 2: Specific Funder Analysis

```
Research [SPECIFIC FUNDER(S)] in detail.

I need:
- Their stated investment/funding criteria
- Portfolio companies or past grantees
- Decision-making process and timeline
- Key decision makers and their backgrounds
- Any public statements about what they look for

Cite all information with sources.
```

## Prompt 3: Funder Requirements

```
Research the typical requirements for [FUNDING TYPE] in [VERTICAL].

I need:
- Common criteria across funders (stage, traction, team)
- Documentation typically required
- Timeline from application to decision
- Success rates and competitive dynamics
- Red flags that disqualify applicants

Provide sources for all requirements mentioned.
```

## Prompt 4: Recent Funding Activity

```
Research recent [FUNDING TYPE] activity in [VERTICAL] (last 12-18 months).

I need:
- Notable deals or grants awarded
- Emerging trends in funder priorities
- Changes in funding environment
- New entrants or exits from the space

All examples and trends should be cited.
```

## Customization Instructions

- Replace all bracketed `[PLACEHOLDERS]` with specifics from funder criteria input
- Add any specific funders mentioned in the criteria
- Constrain to relevant geography if specified
- Add vertical-specific sources to search

## Output File Format

Save to `{project}/research/01-capital-prompts.md`:

```markdown
# Capital Thesis Research Prompts

**Project:** [Project Name]
**Date Generated:** [Date]
**Input Reference:** inputs/funder-criteria.md

## Context

[Summary of what we know about funding targets and what we need to learn]

## Prompts

### Prompt 1: Funding Landscape

[Full customized prompt]

---

### Prompt 2: Specific Funder Analysis

[Full customized prompt]

---

[Continue for all prompts]

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save each result to `research/01-capital/`
3. Name files: `01-landscape.md`, `02-funder-analysis.md`, etc.
4. Once all research is complete, notify for processing
```
