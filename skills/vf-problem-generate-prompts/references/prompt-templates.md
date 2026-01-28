# Problem Thesis Prompt Templates

## Prompt 1: Problem Prevalence and Severity

```
Research the prevalence and severity of [PROBLEM] in [VERTICAL/MARKET].

I need:
- Statistics on how many organizations/people are affected
- Quantified impact (financial cost, time lost, outcomes affected)
- Trends over time (getting worse? better?)
- Breakdown by segment if relevant (size, geography, type)

Provide specific citations for all statistics. Include source name, date, and URL.
```

## Prompt 2: Customer Voice and Pain Points

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

## Prompt 3: Current Solutions and Their Shortcomings

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

## Prompt 4: Cost of the Status Quo

```
Research the quantified cost of [PROBLEM] for [TARGET CUSTOMERS].

I need:
- Direct financial costs (spending, losses, inefficiencies)
- Indirect costs (time, opportunity cost, risk exposure)
- Regulatory or compliance costs if relevant
- Industry benchmarks for this cost category

All figures must have citations with methodology where available.
```

## Prompt 5: Regulatory and Compliance Context (If Applicable)

```
Research regulatory requirements and compliance pressures related to [PROBLEM] in [VERTICAL].

I need:
- Relevant regulations and their requirements
- Penalties for non-compliance
- Recent enforcement actions or trends
- Upcoming regulatory changes

Cite specific regulations, enforcement actions, and authoritative sources.
```

## Customization Instructions

- Replace `[PROBLEM]`, `[VERTICAL/MARKET]`, `[TARGET CUSTOMERS]` with specifics from capital thesis
- Add context from capital thesis to constrain research
- Constrain to relevant geography if specified
- Add vertical-specific sources to search
- Omit Prompt 5 if regulatory context is not relevant

## Output File Format

Save to `{project}/research/02-problem-prompts.md`:

```markdown
# Problem Thesis Research Prompts

**Project:** [Project Name]
**Date Generated:** [Date]
**Capital Thesis Reference:** phases/01-capital/thesis.md

## Context

[Brief summary of the problem being validated and relevant capital constraints]

## Prompts

### Prompt 1: Problem Prevalence and Severity

[Full customized prompt]

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
