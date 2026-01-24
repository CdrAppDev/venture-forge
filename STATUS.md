# Venture Forge - Current Status

## What This Is

Venture Forge is a **company factory** - a framework that systematically creates software ventures from funding opportunities through to revenue.

## Key Documents

- **Thesis Document**: `docs/THESIS.md` - Full thesis for stakeholder presentation
- **Presentation**: `presentation/index.html` - Web-based presentation
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

### Materials & Funding (8-10)
8. **Case Assembly** - Evidence library, all claims cited
9. **Narrative Assembly** - Pitch deck, summaries, materials
10. **Funding Execution** - Applications, pitches, close

### Build & Launch (11-13)
11. **MVP Architecture** - Tech spec, data model, UI/UX, dev plan
12. **MVP Build** - AI-accelerated development, working software
13. **Launch & Revenue** - First customers, first revenue

## Technology Stack

- **Research**: Gemini Deep Research API (multi-step autonomous research with citations)
- **Processing/Generation**: Claude Opus 4.5 (synthesis, materials, code)
- **Orchestration**: Claude Code (workflow management)
- **Storage**: File system + GitHub
- **No custom software needed** - Claude Code IS the platform

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
3. **Gemini for research** - Use Gemini Deep Research API for comprehensive cited research
4. **Claude for everything else** - Processing, generation, orchestration, code
5. **13 phases, not 10** - Extended to include MVP build and revenue
6. **Evidence-backed** - Every claim must have third-party citation

## What's Done

- [x] Thesis document (`docs/THESIS.md`)
- [x] Web presentation (`presentation/index.html`)
- [x] GitHub Pages hosting
- [x] 13-phase workflow defined
- [x] Technology architecture defined
- [x] Proof point documented (RHTP → 5 opportunities)

## What's Next

- [ ] Update `docs/WORKFLOW.md` to match 13-phase model
- [ ] Update `docs/AGENTS.md` to include build agents
- [ ] Create research prompt templates for each phase
- [ ] Document the Gemini Deep Research integration
- [ ] Continue ClaimIQ through remaining phases
- [ ] Stakeholder presentation and approval

## Files to Read for Context

To understand the full framework:
1. `docs/THESIS.md` - The complete thesis
2. `presentation/index.html` - Visual presentation
3. `/Users/chrisroberts/Projects/rhtp/compass_artifact_*.md` - RHTP research
4. `/Users/chrisroberts/Projects/claimiq/` - ClaimIQ proof point
