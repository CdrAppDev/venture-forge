# Venture Forge - Current Status

## What This Is

Venture Forge is a **company factory** - a framework that systematically creates software ventures from funding opportunities through to revenue.

## Key Documents

- **Thesis Document**: `docs/THESIS.md` - Full thesis for stakeholder presentation
- **Presentation**: `docs/index.html` - Web-based presentation
- **Live URL**: https://cdrappdev.github.io/venture-forge/
- **GitHub Repo**: https://github.com/CdrAppDev/venture-forge

## The 13-Phase Workflow

### Research & Validation (1-4)
1. **Capital Thesis** - Where is funding flowing? What do funders want?
2. **Problem Thesis** - Is this a real, documented problem?
3. **Market Thesis** - Is the market big enough? TAM/SAM/SOM
4. **Competitive Thesis** - Who else is solving this? Gaps?

### Design & Model (5-7)
5. **Solution Thesis** - What do we build? Why will it win?
6. **Business Thesis** - How does it make money? Unit economics
7. **Risk Thesis** - What could go wrong? Mitigations

### Materials (8-9)
8. **Case Assembly** - Evidence library, all claims cited
9. **Narrative Assembly** - Pitch deck, summaries, materials

### Build & Traction (10-12)
10. **MVP Architecture** - Tech spec, data model, UI/UX, dev plan
11. **MVP Build** - AI-accelerated development, working software
12. **Customer Traction** - LOI or first paying customer (funders need proof)

### Funding (13)
13. **Funding Execution** - Applications with traction, pitches, close

## Technology Stack

- **Research**: Claude Deep Research (manual workflow)
- **Processing/Generation**: Claude Opus 4.5 (synthesis, materials, code)
- **Orchestration**: Claude Code (workflow management)
- **Storage**: File system + GitHub
- **No custom software needed** - Claude Code IS the platform

### Research Workflow

1. **Generate prompts** - Claude Code creates research prompts for each phase
2. **Run research** - User runs prompts manually in Claude Deep Research
3. **Upload results** - User saves results to `research/` folder in each project
4. **Process & synthesize** - Claude Code processes research into phase outputs

## Proof Points

One research pass (RHTP - Rural Health Technology Program) generated 5 software opportunities:

1. **ClaimIQ** - AI denial prevention for rural hospitals (IN DEVELOPMENT)
2. **CyberShield** - Managed security for critical access hospitals
3. **VitalLink** - Remote patient monitoring for rural populations
4. **MindBridge** - Integrated behavioral health for primary care
5. **ShiftSmart** - Workforce scheduling for rural healthcare

See `/Users/chrisroberts/Projects/claimiq/` for ClaimIQ materials.
See `/Users/chrisroberts/Projects/rhtp/` for the RHTP research.

## Key Decisions Made

1. **No costs/money in the thesis** - Don't mention costs, budgets, or "zero capital" - just describe the work
2. **Software-first** - All ventures are software products
3. **Claude for research** - Use Claude Deep Research (manual workflow) for comprehensive cited research
4. **Claude for everything else** - Processing, generation, orchestration, code
5. **13 phases, not 10** - Extended to include MVP build and revenue
6. **Evidence-backed** - Every claim must have third-party citation

## Portfolio State

See `portfolio.yaml` for current status of all projects.
See `portfolio/{project}.yaml` for detailed phase history per project.

Run `status` to see the full portfolio dashboard.

## What's Done

- [x] Thesis document (`docs/THESIS.md`)
- [x] Web presentation (`docs/index.html`)
- [x] GitHub Pages hosting
- [x] 13-phase workflow defined
- [x] Technology architecture defined
- [x] Proof point documented (RHTP → 5 opportunities)
- [x] Phase 01-02 skills built (generate-prompts, process-research, validate)
- [x] Portfolio state system (registry + per-project detail files)
- [x] CyberShield Rural Phase 01 Capital Thesis complete (gate-review)
- [x] `vf-present` shared presentation skill (design system, component library, phase section layouts)
- [x] Phase 01 retrospective — learnings applied to platform (see below)

## Learnings Applied from Phase 01 Test (CyberShield Rural)

1. **sources.md is a required deliverable** — Added to process-research skills for both Phase 01 and 02. Validation skills now check for it (capital: 36 checks, problem: 33 checks).
2. **URL verification in validation** — Validation skills now include URL format checks. Broken links caught at validation, not after the presentation is built.
3. **Narrative is mandatory** — phase-sections.yaml requires a narrative section for every phase, with 4 named chapters. The last chapter is always "The Ask" pointing to Gate Review.
4. **Presentations go in /docs** — CLAUDE.md project paths updated from `presentation/` to `docs/`. GitHub Pages only serves from `/` or `/docs`.
5. **Source name labels on citations** — Component library requires source name in all inline citation links (e.g., "192.7M records (HIPAA Journal)").
6. **Portfolio state at project init** — Portfolio system exists; future improvement: create portfolio entry when a new project starts, not after first phase completes.

## What's Next

- [ ] Create Claude Deep Research prompt templates for phases 3+
- [ ] Build skills for phases 3-12
- [ ] Complete CyberShield Rural gate review and advance to Phase 02
- [ ] Stakeholder presentation and approval

## Files to Read for Context

To understand the full framework:
1. `portfolio.yaml` - Portfolio registry (start here)
2. `CLAUDE.md` - Commands, resume logic, update rules
3. `docs/THESIS.md` - The complete thesis
4. `docs/index.html` - Visual presentation
5. `process/PROCESS.yaml` - Phase definitions and file conventions
