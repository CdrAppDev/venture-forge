---
name: vf-present
description: >
  Generate standalone HTML presentations for Venture Forge phase outputs.
  Activate after validation passes (phase_status: gate-review) or when user
  requests a presentation. Reads phase outputs from {project}/phases/{phase_id}/
  and produces {project}/docs/phase-{NN}.html plus updates {project}/docs/index.html
  (project landing page). Each phase gets its own page; all pages share navigation
  and design system. Owns the design system — all projects share the same visual
  language. See references/ for design system, components, and per-phase section layouts.
license: MIT
metadata:
  version: "1.0.0"
  phase: all
  when: after_validation
---

# Presentation Generator

Build a standalone HTML presentation for a Venture Forge phase output. The presentation uses the Venture Forge design system and adapts its sections based on the phase being presented. Every project gets the same visual treatment — dark theme, purple accent, glassmorphism nav, interactive components.

## Prerequisites

- Phase outputs exist at `{project}/phases/{phase_id}/` (thesis.md + structured data + validation report)
- Validation has passed (phase_status is `gate-review` or user explicitly requests presentation)
- Sources file exists at `{project}/phases/{phase_id}/sources.md` (or will be generated alongside)

## Workflow

1. **Identify the phase.** Read the project's portfolio detail file or ask the user which phase to present.

2. **Read phase-sections.yaml** from `references/phase-sections.yaml`. Find the entry for the current phase ID. This tells you what sections to build, what components each section uses, and what data files to read.

3. **Read all phase outputs.** Load every file listed in the phase-sections data mappings:
   - `{project}/phases/{phase_id}/thesis.md` — narrative content, stats, tables
   - `{project}/phases/{phase_id}/*.yaml` — structured data (funder profiles, evidence, etc.)
   - `{project}/phases/{phase_id}/validation-report.md` — gate review data
   - `{project}/phases/{phase_id}/sources.md` — citation list

4. **Build source URL lookup.** Parse `sources.md` to create a mapping of source names to URLs. This mapping is used in step 5 to convert inline citations into clickable links.

4b. **Load writing governance.** Read `skills/vf-write/references/presentation-fidelity.md`. All narrative chapters and section-lead text must comply with these fidelity rules. The phase type (research/materials/build) determines the writing register — see `skills/vf-write/references/register-rules.md`.

5. **Build the HTML file.** Use `references/design-system.md` for all CSS and `references/component-library.md` for HTML patterns. For each section in phase-sections.yaml:
   - Use the specified component pattern
   - Populate with actual data from the phase outputs
   - Adapt section numbering (01, 02, 03...) sequentially
   - Build navigation links from the `nav_links` list
   - **Link inline citations:** Every `(Source Name, Date)` citation in narrative text must be rendered as `(<a href="URL" target="_blank" class="source-link">Source Name, Date</a>)` using the URL from the source lookup map. Citations without URLs in sources.md remain as plain text.

6. **Add JavaScript.** Include only the JS needed for components used in this phase:
   - Smooth scroll — always include
   - Filter tabs — include if any section uses `filter-table` component
   - Accordion toggle — include if any section uses `accordion` component

7. **Write phase page** to `{project}/docs/phase-{NN}.html` (e.g., `phase-01.html`, `phase-02.html`).

8. **Update landing page.** Update `{project}/docs/index.html` — the project dashboard showing all phases, their status, and links to completed phase pages. If `index.html` doesn't exist, create it. Update phase card status badges and stats when new phases complete.

9. **Add phase navigation.** Each phase page gets a fixed phase nav bar above the section nav:
   - Previous phase link (if exists)
   - Project name linking to `index.html`
   - Next phase link (greyed out if not yet complete)

10. **Quality check.** Before finishing, verify:
   - Every section from phase-sections.yaml is present in the HTML
   - All data from phase outputs appears (no placeholder text, no "TBD")
   - All external links use `target="_blank"`
   - Nav links match section IDs
   - Badge colors match data (strong=green, moderate=amber, weak=gray, etc.)
   - Footer includes project name, phase name, version, date, "Venture Forge"

## Output Rules

- **Multi-page site.** One `index.html` landing page plus one `phase-{NN}.html` per completed phase. Each page is self-contained with embedded `<style>` and `<script>`. No external CSS, JS, or font files.
- **GitHub Pages compatible.** Files go in `{project}/docs/` so Pages can serve from `/docs` on main branch. Landing page at root, phase pages linked from it.
- **No CDN dependencies.** Font stack uses system fonts (`Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`).
- **Responsive.** Must work at desktop (1100px+), tablet (900px), and mobile (768px).
- **Accessible.** Semantic HTML, contrast ratios maintained, interactive elements keyboard-navigable.

## Design System

See `references/design-system.md` for the complete CSS specification.

**Do not modify the design system.** Use it exactly as documented. If a new component is needed that doesn't exist in the library, add it following the existing patterns (same color variables, same spacing, same border styles).

## Component Library

See `references/component-library.md` for HTML patterns for every reusable component.

Each component is documented with its exact HTML structure, required CSS classes, data attributes, and JavaScript requirements. Use the patterns as-is, substituting project-specific content.

## Phase Layouts

See `references/phase-sections.yaml` for the section layout map per phase.

If a phase is not yet defined in the map, build a reasonable layout using the available components. Every phase presentation should include at minimum: hero, narrative (story), gate review, and sources.

## Quality Checklist

- [ ] All sections from phase-sections.yaml are rendered
- [ ] Data matches source files exactly (spot-check 3+ data points)
- [ ] No placeholder text or "TBD" values
- [ ] Navigation links work (smooth scroll to correct sections)
- [ ] Filter tabs toggle correctly (if used)
- [ ] Accordion expand/collapse works (if used)
- [ ] Responsive layout at 768px (grids stack, nav hides)
- [ ] All external links open in new tab
- [ ] Badge colors match semantic meaning
- [ ] Footer has project name, phase, date, "Venture Forge"
- [ ] Sources section lists all citations from sources.md
- [ ] Inline citations are clickable links (where URL exists in sources.md)
- [ ] Source links open in new tab with `target="_blank"`
- [ ] Source link CSS (`.source-link`) is included in the style block
