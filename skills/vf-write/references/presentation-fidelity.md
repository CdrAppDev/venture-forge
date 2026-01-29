# Presentation Fidelity Rules

Rules governing how vf-present renders phase outputs into HTML presentations. The core principle: **the presentation renders thesis.md; it does not rewrite it.**

---

## Data Section Fidelity

Data sections include stat rows, stat cards, tables, badges, card grids, accordion items, and bar charts.

1. **Exact match required.** Data in tables, stat rows, badges, and cards must exactly match thesis.md, evidence.yaml, funder-profiles.yaml, or other source files. No rounding, no rephrasing, no combining figures that are separate in the source.

2. **Section-lead text must summarize, not editorialize.** The 1-2 sentence description under each section header (`section-lead` class) must describe what the section contains. It should not introduce claims, framing, or interpretation that does not appear in the source files.

   **Good:** "41 unique sources across 6 categories document the prevalence, severity, and cost of inadequate rural hospital cybersecurity."
   **Bad:** "The overwhelming evidence makes an undeniable case for urgent action."

3. **Card descriptions paraphrase thesis.md, not introduce new claims.** Card body text must be traceable to a specific section or paragraph in thesis.md. If a card says something thesis.md does not say, it is a fidelity violation.

## Narrative Section Fidelity (The Story)

The narrative section (4 chapters per phase) is the only place where the presentation creates new prose. These rules constrain that prose.

### Rule 1: Register Must Match Phase Type

The narrative register must match the phase's writing register as defined in `register-rules.md`.

- Research phase presentations (01-07): Analytical register for all narrative chapters
- Materials phase presentations (08-09, 13): Persuasive register
- Build phase presentations (10-12): Technical register

### Rule 2: No New Data Points

Every factual claim in the narrative must appear in thesis.md. The narrative cannot introduce new statistics, data points, or claims that are not in the source thesis. The narrative may reorder, condense, or highlight data from thesis.md, but it cannot add to it.

**Allowed:** Selecting the 4 most impactful statistics from a thesis that contains 20.
**Prohibited:** Adding a statistic the agent recalls from research that was not included in thesis.md.

### Rule 3: Headlines Follow Phase Register

Narrative chapter headlines (`h3` elements) must follow the heading style rules for the phase type.

| Phase Type | Allowed Headlines | Prohibited Headlines |
|-----------|-------------------|---------------------|
| Research (01-07) | "12 viable funding paths across four categories" | "We found 12 doors. Here's which ones open first." |
| Research (01-07) | "68% of rural hospitals lack a dedicated CISO" | "Nobody is minding the store" |
| Materials (08-09) | "Rural hospitals are under attack" | Same text is appropriate here |
| Materials (08-09) | "A $1.5 billion problem nobody is solving" | "An inevitable market explosion" |
| Build (10-12) | "Three-tier architecture with edge processing" | "Our revolutionary platform design" |

### Rule 4: Inline Citations Mandatory and Linked

Every factual claim in narrative text must include an inline citation in the format `(Source Name, Date)`. Citations must be rendered as clickable links using URLs from sources.md. Citations without available URLs remain as plain text.

### Rule 5: Connective Logic Follows Thesis Rules

If the narrative connects two facts from different sources, it must use hedging language. The same connective logic rules from the writing governance skill apply to the presentation layer.

### Rule 6: No Amplification

The narrative cannot make a claim stronger than thesis.md makes it. If thesis.md describes an alignment as "moderate," the narrative cannot describe it as "strong." If thesis.md says "suggests," the narrative cannot say "demonstrates."

| thesis.md says | Narrative can say | Narrative cannot say |
|---------------|-------------------|---------------------|
| moderate alignment | moderate alignment, partial alignment | strong alignment, clear fit |
| suggests a connection | suggests, may indicate | demonstrates, confirms |
| potential opportunity | potential opportunity | clear opportunity, obvious gap |
| significant challenge | significant challenge | existential crisis |

## Quality Verification

After generating the presentation, spot-check at least 3 data points:
1. Pick a statistic from a stat card — verify it matches the source file exactly
2. Pick a narrative claim — verify it appears in thesis.md
3. Pick an inline citation — verify the link URL matches sources.md
