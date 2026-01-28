# Skill: Capital Thesis - Generate Research Prompts

**Version:** 1.0.0
**Phase:** 01-capital
**When:** Before research

## Purpose

Generate Claude Deep Research prompts to understand the funding landscape and identify viable capital sources.

## Prerequisites

- Funder criteria input exists at `{project}/inputs/funder-criteria.md`
- This can be: meeting notes, grant program descriptions, investor thesis pages, etc.

## Instructions

### Step 1: Read Funder Criteria Input

Read `{project}/inputs/funder-criteria.md` to understand:
- What funding sources are being considered
- Any known criteria or requirements
- Geographic or vertical focus
- Stage preferences
- Timeline constraints

### Step 2: Identify Research Gaps

Determine what additional information is needed:
- Are there other funding sources in this space?
- What are the detailed criteria for identified sources?
- What have these funders invested in recently?
- What is their decision process and timeline?

### Step 3: Generate Research Prompts

Create 3-4 research prompts:

**Prompt 1: Funding Landscape**
```
Research the funding landscape for [VERTICAL/STAGE] ventures.

I need:
- Active investors, grants, and accelerators in this space
- Their stated investment thesis or funding criteria
- Recent investments or grants made (last 2 years)
- Funding amounts and stages they focus on

Provide citations for all claims including source name, date, and URL.
```

**Prompt 2: Specific Funder Analysis**
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

**Prompt 3: Funder Requirements**
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

**Prompt 4: Recent Funding Activity**
```
Research recent [FUNDING TYPE] activity in [VERTICAL] (last 12-18 months).

I need:
- Notable deals or grants awarded
- Emerging trends in funder priorities
- Changes in funding environment
- New entrants or exits from the space

All examples and trends should be cited.
```

### Step 4: Customize Prompts

- Replace bracketed placeholders with specifics from input
- Add any specific funders mentioned in the criteria
- Focus on relevant geography if specified
- Add vertical-specific sources to search

### Step 5: Write Output File

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

[Full prompt]

---

### Prompt 2: Specific Funder Analysis

[Full prompt]

---

[Continue for all prompts]

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save results to `research/01-capital/`
3. Name files: `01-landscape.md`, `02-funder-analysis.md`, etc.
4. Notify when complete for processing
```

## Output Format

File: `{project}/research/01-capital-prompts.md`

## Quality Checklist

- [ ] Prompts address known funders from input
- [ ] Prompts seek additional/alternative funding sources
- [ ] All prompts request citations
- [ ] Geographic/vertical scope is specified
- [ ] Prompts cover: landscape, specific funders, requirements, recent activity

## Version History

### 1.0.0 - 2025-01-28
- Initial version
