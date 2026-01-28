# Skill: Problem Thesis - Generate Research Prompts

**Version:** 1.0.0
**Phase:** 02-problem
**When:** Before research

## Purpose

Generate Claude Deep Research prompts that will validate whether the problem is real, significant, and worth solving. The prompts must yield evidence that satisfies the phase gate criteria.

## Prerequisites

- Capital thesis exists at `{project}/phases/01-capital/thesis.md`
- Capital thesis has been approved (Phase 1 gate passed)

## Instructions

### Step 1: Read the Capital Thesis

Read `{project}/phases/01-capital/thesis.md` to understand:
- Target vertical/industry
- Funder criteria and constraints
- Geographic focus (if any)
- Any specific problem areas funders care about

### Step 2: Identify the Problem Hypothesis

Based on the capital thesis, identify the specific problem to validate. This should be:
- A problem within the target vertical
- Aligned with funder interests
- Specific enough to research (not "healthcare is broken")

### Step 3: Generate Research Prompts

Create 4-5 research prompts covering these areas:

**Prompt 1: Problem Prevalence and Severity**
```
Research the prevalence and severity of [PROBLEM] in [VERTICAL/MARKET].

I need:
- Statistics on how many organizations/people are affected
- Quantified impact (financial cost, time lost, outcomes affected)
- Trends over time (getting worse? better?)
- Breakdown by segment if relevant (size, geography, type)

Provide specific citations for all statistics. Include source name, date, and URL.
```

**Prompt 2: Customer Voice and Pain Points**
```
Research how [TARGET CUSTOMERS] describe their struggles with [PROBLEM].

Search:
- Industry forums and communities
- Product reviews on G2, Capterra, or relevant platforms
- Reddit discussions in relevant subreddits
- Support forums and help requests
- LinkedIn and Twitter discussions from practitioners

I need:
- Direct quotes showing how people describe this problem
- Common language and terminology used
- Emotional intensity (frustration level)
- Workarounds people have tried

Cite each quote with source and date.
```

**Prompt 3: Current Solutions and Their Shortcomings**
```
Research how [TARGET CUSTOMERS] currently address [PROBLEM].

I need:
- Existing solutions (software, services, manual processes)
- Market leaders and their approaches
- Known limitations and complaints about current solutions
- Gaps that remain unaddressed
- Why current solutions aren't sufficient

Provide citations for all claims about products and their limitations.
```

**Prompt 4: Cost of the Status Quo**
```
Research the quantified cost of [PROBLEM] for [TARGET CUSTOMERS].

I need:
- Direct financial costs (spending, losses, inefficiencies)
- Indirect costs (time, opportunity cost, risk exposure)
- Regulatory or compliance costs if relevant
- Industry benchmarks for this cost category

All figures must have citations with methodology where available.
```

**Prompt 5 (if applicable): Regulatory and Compliance Context**
```
Research regulatory requirements and compliance pressures related to [PROBLEM] in [VERTICAL].

I need:
- Relevant regulations and their requirements
- Penalties for non-compliance
- Recent enforcement actions or trends
- Upcoming regulatory changes

Cite specific regulations, enforcement actions, and authoritative sources.
```

### Step 4: Customize Prompts

Adapt the prompt templates:
- Replace [PROBLEM], [VERTICAL], [TARGET CUSTOMERS] with specifics
- Add context from the capital thesis
- Constrain to relevant geography if specified
- Add any vertical-specific sources to search

### Step 5: Write Output File

Save prompts to `{project}/research/02-problem-prompts.md` in this format:

```markdown
# Problem Thesis Research Prompts

**Project:** [Project Name]
**Date Generated:** [Date]
**Capital Thesis Reference:** phases/01-capital/thesis.md

## Context

[Brief summary of the problem being validated and relevant capital constraints]

## Prompts

### Prompt 1: Problem Prevalence and Severity

[Full prompt text]

---

### Prompt 2: Customer Voice and Pain Points

[Full prompt text]

---

[Continue for all prompts]

## Instructions for Research

1. Run each prompt in Claude Deep Research
2. Save each research result as a separate file in `research/02-problem/`
3. Name files: `01-prevalence.md`, `02-customer-voice.md`, etc.
4. Once all research is complete, notify for processing
```

## Output Format

Output file: `{project}/research/02-problem-prompts.md`

The file must contain:
- Project identification
- Context from capital thesis
- All research prompts (4-5)
- Clear instructions for the user

## Quality Checklist

- [ ] Prompts reference specific problem and vertical from capital thesis
- [ ] All five research areas covered (prevalence, severity, customer voice, current solutions, cost)
- [ ] Prompts explicitly request citations
- [ ] Customer voice prompt includes specific source types to search
- [ ] Prompts are specific enough to yield actionable research
- [ ] Instructions for saving research results are clear

## Version History

### 1.0.0 - 2025-01-28
- Initial version
- Five prompt areas: prevalence, customer voice, current solutions, cost, regulatory
- Explicit citation requirements in all prompts
