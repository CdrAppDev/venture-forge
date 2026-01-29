# Example Output: CyberShield Rural — Capital Thesis

The first presentation built with this design system. Use as reference for quality, structure, and data density.

## Location

- **File:** `/Users/chrisroberts/Projects/cybershield-rural/docs/index.html`
- **Live URL:** https://cdrappdev.github.io/cybershield-rural/
- **Repository:** https://github.com/CdrAppDev/cybershield-rural

## Details

| Property | Value |
|----------|-------|
| Project | CyberShield Rural |
| Phase | 01 — Capital Thesis |
| File size | ~2,100 lines |
| Sections | Hero + Narrative + 10 numbered sections |
| Sources | 41 third-party citations |
| Data files | thesis.md, funder-profiles.yaml, validation-report.md, sources.md |

## Components Used

All components from the library are demonstrated in this presentation:

- Navigation bar (9 links)
- Hero (funnel + 3 stat cards)
- Narrative (4 chapters: The Opportunity, The Money, The Path, The Ask)
- Card grid 3-col (Executive Summary, Funding Landscape)
- Callout box (critical constraints)
- Scale note (gap findings, VC timeline note)
- Stat row (market size, breach impact, compliance cost)
- Data table with filter tabs (Active Funding Sources — 14 rows, 4 category tabs)
- Badges (all variants: viability, readiness, type, severity)
- Accordion (6 deep-dive items, first open by default)
- Alignment lists (strengths + gaps with severity badges)
- Criteria lists (with source citations)
- Dual-track visualization (Track A: Grants, Track B: Equity)
- Action timeline (10 numbered priority actions with funder tags)
- Phase dependency table (7 gaps with phase tag badges)
- Data table without filters (Funding Timeline — 16 rows)
- Gate review (validation card + 4 decision cards)
- Bar chart (citation distribution — 4 categories)
- Evidence stats row (5 metrics)
- Checklist (4 gate criteria)
- Sources section (5 categories, 41 sources)
- Footer

## JavaScript Features

All three JS patterns are active:
1. Smooth scroll (all nav links)
2. Filter tabs (funder table by category)
3. Accordion toggle (deep-dive sections)

## Quality Benchmarks

Use this output to verify new presentations meet the same standard:

- Every factual claim in the narrative links to a third-party source
- Source links include the organization name (e.g., "192.7 million patient records (HIPAA Journal)")
- All external links open in new tab (`target="_blank"`)
- Badge colors match semantic meaning (strong=green, moderate=amber, blocking=red)
- Sections alternate between default and `section-alt` backgrounds
- Footer includes project name, phase name, version, date, "Venture Forge"
