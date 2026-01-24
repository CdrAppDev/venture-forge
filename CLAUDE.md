# Project: venture-forge

## What This Is

Venture Forge is a **company factory** - a systematic framework for creating software ventures from funding opportunities through to revenue. AI agents handle research, synthesis, and generation. Humans review and decide.

## Current Status

**Read `STATUS.md` first** - it has the current state of the project.

## The Framework

### 13 Phases (Research → Revenue)

**Research & Validation (1-4)**
1. Capital Thesis - What funders want
2. Problem Thesis - Validated problem
3. Market Thesis - TAM/SAM/SOM
4. Competitive Thesis - Gaps and positioning

**Design & Model (5-7)**
5. Solution Thesis - What to build
6. Business Thesis - How it makes money
7. Risk Thesis - What could go wrong

**Materials & Funding (8-10)**
8. Case Assembly - Evidence library
9. Narrative Assembly - Pitch materials
10. Funding Execution - Close the deal

**Build & Launch (11-13)**
11. MVP Architecture - Tech spec, design
12. MVP Build - AI-accelerated development
13. Launch & Revenue - First customers, first dollars

### Technology Stack

- **Research**: Gemini Deep Research API
- **Processing/Generation**: Claude Opus 4.5
- **Orchestration**: Claude Code
- **Storage**: Files + GitHub

### Key Principles

1. **Capital-first** - Start with what funders want, work backwards
2. **Evidence-backed** - Every claim cited to third-party source
3. **Software-first** - All ventures are software products
4. **AI-accelerated** - Research, materials, AND build
5. **Human decisions** - AI researches/generates, humans approve

## Important Files

| File | Purpose |
|------|---------|
| `STATUS.md` | Current state, what's done, what's next |
| `docs/THESIS.md` | Full thesis document |
| `presentation/index.html` | Web presentation |
| `docs/WORKFLOW.md` | Phase details (needs update to 13 phases) |
| `docs/AGENTS.md` | Agent specs (needs update for build agents) |

## Live Presentation

- **URL**: https://cdrappdev.github.io/venture-forge/
- **Repo**: https://github.com/CdrAppDev/venture-forge

## Proof Points

RHTP research → 5 opportunities:
1. ClaimIQ (in development) - `/Users/chrisroberts/Projects/claimiq/`
2. CyberShield - `/Users/chrisroberts/Projects/cybershield-rural/`
3. VitalLink - `/Users/chrisroberts/Projects/vitallink-rpm/`
4. MindBridge - `/Users/chrisroberts/Projects/mindbridge-rural/`
5. ShiftSmart - `/Users/chrisroberts/Projects/shiftsmart-health/`

RHTP Research: `/Users/chrisroberts/Projects/rhtp/`

## Communication Guidelines

**NEVER mention costs, budgets, money, or "zero capital"** in thesis or presentation materials. Don't position things as "free" or "no investment needed" - just describe the work without financial framing.

## Commands

| Command | Description |
|---------|-------------|
| `status` | Show portfolio state |
| `continue [opportunity]` | Work on next phase |
| `review [opportunity]` | Show current phase output |

## What Needs Work

1. Update `docs/WORKFLOW.md` to 13-phase model
2. Update `docs/AGENTS.md` to include build phase agents
3. Create Gemini Deep Research prompt templates
4. Continue ClaimIQ through phases 7-13
5. Stakeholder presentation and greenlight
