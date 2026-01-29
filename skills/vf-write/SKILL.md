---
name: vf-write
description: >
  Writing governance rules for all Venture Forge narrative outputs.
  Defines tone, word choice, framing, and proportionality rules that vary
  by phase type (research, materials, build). Referenced by process-research
  skills when writing thesis.md, by vf-present when building presentation
  narratives, and by validate skills for compliance checks. Use when any
  skill generates prose content for thesis.md or HTML presentations.
license: MIT
user-invocable: false
metadata:
  version: "1.0.0"
  phase: all
---

# Writing Governance

Rules for all narrative writing across Venture Forge. This skill is a reference — other skills load it, it never executes independently.

## Phase Type Classification

Every phase uses one of three writing registers. The register determines tone, voice, sentence structure, and what language is permitted.

| Phases | Register | Role | Summary |
|--------|----------|------|---------|
| 01-07 | Research / Analytical | Research analyst | Data-first. Neutral. Every interpretation hedged. |
| 08-09, 13 | Persuasive | Case builder | Story-first. Evidence-anchored. Emotional language permitted when cited. |
| 10-12 | Technical | Technical writer | Specification-first. Precise. No marketing language. |

See `references/register-rules.md` for full rules, examples, and prohibited patterns per register.

## Universal Rules (All Phases)

These apply regardless of phase type or register.

### 1. No Unsourced Causal Claims

If the text states X caused Y, both X and Y must be cited, and the causal link must either:
- Come from a source that explicitly makes the causal argument, or
- Be marked as inference: "This suggests...", "This pattern indicates...", "Together, these data points support..."

**Prohibited:** "The staffing shortage caused the breach increase." (unless a source says this)
**Allowed:** "The staffing shortage (HSCC, May 2025) coincides with a 278% increase in ransomware breaches (HHS ASPR, December 2023), suggesting a connection between resource constraints and vulnerability."

### 2. No Emotional Language Without Evidence

Words that escalate emotional intensity are prohibited in prose unless they appear in a direct quote from a cited source. See `references/word-boundaries.md` for the full prohibited/substitute list.

**Prohibited:** "Rural hospitals face an existential crisis."
**Allowed:** "Rural hospitals face a significant and worsening cybersecurity challenge."
**Also allowed:** As John Riggi described it, rural hospitals face "an existential threat" (AHA, HealthTech Magazine, 2024).

### 3. Proportional Treatment of Counter-Evidence

If research contains data that weakens or contradicts the thesis, it must appear in the output. It can appear in a "Limitations," "Caveats," or "Conflicting Data" subsection, but it cannot be omitted. The processing log must document all excluded evidence and the reason for exclusion.

### 4. Qualifier Discipline

Claims must use qualifiers proportional to the evidence strength:

| Qualifier | Use When |
|-----------|----------|
| suggests | Correlational evidence; pattern observed but not controlled |
| indicates | Multiple independent sources confirm; stronger than correlation |
| demonstrates | Experimental, controlled, or direct measurement evidence |
| shows | Descriptive data from a credible source |
| supports | Evidence is consistent with a claim but does not confirm it alone |

**Never use:** "proves," "confirms beyond doubt," "definitively shows"

### 5. No Invented Specificity

The agent must not add precision that the source does not provide.

**Prohibited:** Source says "most hospitals" -> thesis says "the majority (estimated 70-80%)"
**Allowed:** Source says "most hospitals" -> thesis says "most hospitals"
**Allowed:** Source says "73% of hospitals" -> thesis says "73% of hospitals (Source, Date)"

### 6. Connective Logic Must Be Labeled

See Connective Logic Rules below.

## Connective Logic Rules

Connective logic is the highest-risk editorial category. It looks like sourced analysis but is actually agent inference.

**Definition:** A connective claim joins two or more separately-sourced facts to draw an inference.

**Example:** "The $50B RHT program (CMS, December 2025) combined with no VC-backed competitors in this segment (Black Book Research, June 2025) suggests a unique funding window." The "unique funding window" is the agent's inference connecting two independent facts.

**Allowed hedging language:** suggests, indicates, positions, supports, points to, is consistent with

**Prohibited definitive language:** proves, guarantees, means, ensures, confirms, establishes

**Processing log requirement:** Every connective claim must be logged in the Decisions Made section of processing-log.md, noting which sources were connected and what inference was drawn.

**Limit:** Research-register phases (01-07) should contain no more than one connective inference per major section. Materials-register phases have no limit but must still hedge each one.

## Framing Rules

### Research Phases (01-07)
Lead with data, follow with interpretation. The first sentence of every narrative paragraph should contain a cited fact. Interpretation and analysis follow.

**Good:** "73% of rural hospitals lack adequate cybersecurity defenses (Black Book Research, June 2025). This represents a 12-point increase from 61% in 2023, indicating a deteriorating trend."
**Bad:** "The cybersecurity landscape for rural hospitals is deteriorating rapidly. Recent data shows 73% now lack adequate defenses."

### Materials Phases (08-09, 13)
Lead with the story, support with data. Narrative framing sentences are permitted. But every narrative paragraph must still contain at least one inline citation.

**Headings** must match the register. See `references/register-rules.md` for heading style rules per phase type.

## How Other Skills Reference This Skill

### Process-Research Skills
Add to SKILL.md:
```
## Writing Governance
Follow all rules in skills/vf-write/SKILL.md. Before writing thesis.md narrative:
- Load skills/vf-write/references/register-rules.md for phase-specific register
- Load skills/vf-write/references/word-boundaries.md to check against prohibited terms
- Log connective claims in the Decisions Made section of processing-log.md
```

### vf-present
Add to workflow:
```
Load skills/vf-write/references/presentation-fidelity.md. All narrative chapters
and section-lead text must comply with fidelity rules. Phase type determines register.
```

### Validate Skills
Add 4 writing governance checks. See Validation Integration below.

## Validation Integration

Validate skills should add these 4 checks:

**WG-01: Prohibited Word Scan**
Load `references/word-boundaries.md`. Scan all prose in thesis.md (skip tables, YAML, inline citations in parentheses). Flag every occurrence of a prohibited word. Exception: word inside quotation marks with a citation is allowed. FAIL if any prohibited word found outside quotes.

**WG-02: Heading Register Check**
Extract all markdown headings from thesis.md. For research phases: check against promotional language patterns (first person, superlatives, rhetorical questions, exclamatory punctuation). FAIL if any heading violates register rules.

**WG-03: Connective Logic Audit**
Scan narrative paragraphs for sentences containing two or more different inline citations. For each, check whether it uses hedging language from the allowed list vs. definitive language from the prohibited list. Cross-check against processing-log.md Decisions Made section. FAIL if definitive language found. WARNING if connective claim not logged.

**WG-04: Counter-Evidence Check**
Read processing-log.md Evidence Excluded section. Identify entries with exclusion reason containing "contradicted." For each, verify the winning data point appears in thesis.md with qualification. FAIL if contradicted evidence is absent with no mention.
