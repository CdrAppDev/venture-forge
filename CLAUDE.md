# Project: venture-forge

## What This Is

Venture Forge is a **company factory** - a systematic framework for creating software ventures from funding opportunities through to revenue. AI agents handle research, synthesis, and generation. Humans review and decide.

## Current Status

**Read `STATUS.md` first** - it has the current state of the project.

## The Framework

### 12 Phases (Research → Funded)

**Research & Validation (1-4)**
1. Capital Thesis - What funders want
2. Problem Thesis - Validated problem
3. Market Thesis - TAM/SAM/SOM
4. Competitive Thesis - Gaps and positioning

**Design & Model (5-7)**
5. Solution Thesis - What to build
6. Business Thesis - How it makes money
7. Risk Thesis - What could go wrong

**Materials (8)**
8. Materials Assembly - Evidence library + pitch materials

**Build & Traction (9-11)**
9. MVP Architecture - Tech spec, design
10. MVP Build - AI-accelerated development
11. Customer Traction - LOI or first customer (funders need proof)

**Funding (12)**
12. Funding Execution - Close funding with traction proof

### Technology Stack

- **Research**: Claude Deep Research (manual workflow)
- **Processing/Generation**: Claude Opus 4.5
- **Orchestration**: Claude Code
- **Storage**: Files + GitHub

### Research Workflow

1. **Generate prompts** - Claude Code creates research prompts for each phase
2. **Run research** - User runs prompts manually in Claude Deep Research
3. **Upload results** - User saves results to `research/` folder in each project
4. **Process & synthesize** - Claude Code processes research into phase outputs

### Key Principles

1. **Capital-first** - Start with what funders want, work backwards
2. **Evidence-backed** - Every claim cited to third-party source
3. **Software-first** - All ventures are software products
4. **AI-accelerated** - Research, materials, AND build
5. **Human decisions** - AI researches/generates, humans approve

## Important Files

| File | Purpose |
|------|---------|
| `portfolio.yaml` | **Portfolio registry — read this first** |
| `portfolio/{project}.yaml` | Detailed phase history per project |
| `STATUS.md` | Framework status and what needs work |
| `docs/THESIS.md` | Full thesis document |
| `docs/index.html` | Web presentation (GitHub Pages) |
| `docs/QUALITY-GATES.md` | Gate review checklists and decision criteria |
| `process/PROCESS.yaml` | Phase definitions and file conventions |
| `process/phases/*.yaml` | Individual phase specs with gate criteria |
| `skills/vf-*/SKILL.md` | Agent skills for each phase step |

## Portfolio Management

### How It Works

Projects are tracked in two layers:
- **`portfolio.yaml`** — registry with one entry per project (name, path, current phase, status)
- **`portfolio/{project}.yaml`** — detailed history (phase-by-phase decisions, validation results, notes)

State lives here in venture-forge. Work products live in each project's own repo.

### Commands

| Command | What to Do |
|---------|------------|
| `status` | Read `portfolio.yaml`, show a table of all projects with current phase and status |
| `continue [project]` | Read `portfolio.yaml` for phase/status, read `portfolio/{project}.yaml` for detail, execute the next step based on resume logic below |
| `review [project]` | Read `portfolio/{project}.yaml` to find project path and current phase, then read the phase outputs |

### Resume Logic

When a user says `continue [project]`, read the `phase_status` and execute accordingly:

| phase_status | What to Do |
|---|---|
| `pending` | Run `vf-{phase}-generate-prompts` skill for the project. Update status to `research`. |
| `research` | Tell user to run prompts in Claude Deep Research and upload results to `{project}/research/{phase_id}/`. Once uploaded, update status to `processing`. |
| `processing` | Run `vf-{phase}-process-research` skill. Update status to `validation`. |
| `validation` | Run `vf-{phase}-validate` skill. Update status to `gate-review`. |
| `gate-review` | Read `pending_decisions` from the detail file. Present gate decisions to the human. Wait for their decision. |
| `complete` | Advance `current_phase` to the next phase per `process/PROCESS.yaml`. Set new phase status to `pending`. |

### Update Rules

- **After every status change:** update BOTH `portfolio.yaml` (registry) and `portfolio/{project}.yaml` (detail)
- **After gate decision:** record `gate_decision`, `gate_date`, and `gate_notes` in the detail file
- **On `proceed`:** mark current phase `complete`, set `current_phase` to next phase, set `phase_status` to `pending`
- **On `revise`:** keep current phase, set `phase_status` to `processing`, add revision notes to `gate_notes`
- **On `kill`:** set `phase_status` to `killed`, add notes explaining why

### Project Paths

Each project is a separate repo. The `path` field in portfolio files points to the project root. All file conventions from `process/PROCESS.yaml` apply:

```
{project}/inputs/              # Human-provided context
{project}/research/{phase_id}/ # Claude Deep Research outputs
{project}/phases/{phase_id}/   # Phase deliverables (thesis.md, YAML, sources.md, validation-report.md, processing-log.md)
{project}/docs/                # Web presentations (GitHub Pages serves from /docs on main branch)
```

## Live Presentation

- **URL**: https://cdrappdev.github.io/venture-forge/
- **Repo**: https://github.com/CdrAppDev/venture-forge

## Phase Output Rules

Every phase MUST produce these files in `{project}/phases/{phase_id}/`:
- `thesis.md` — narrative with inline citations
- Structured data files (phase-specific: YAML profiles, evidence, etc.)
- `sources.md` — deduplicated list of all third-party sources organized by category
- `validation-report.md` — automated check results
- `processing-log.md` — audit trail of all processing decisions

**Sources are a required deliverable, not an afterthought.** The sources.md file must be compiled during processing, not after the presentation is built. Every unique source gets an entry with: org name, document title, date, URL (where available), and what it was cited for.

**Presentations go in `{project}/docs/`.** GitHub Pages serves from `/docs` on main branch. Never use `/presentation/` — it is not a valid Pages source.

**Narrative is mandatory.** Every phase presentation must include a narrative section that tells the story in plain language. The narrative exists for human decision-makers, not as documentation. Every factual claim in the narrative must link to its third-party source with the source name in the label (e.g., "192.7M records (HIPAA Journal)").

## Communication Guidelines

**NEVER mention costs, budgets, money, or "zero capital"** in thesis or presentation materials. Don't position things as "free" or "no investment needed" - just describe the work without financial framing.

## What Needs Work

1. Build skills for phases 3-12
2. Test Phase 02 with CyberShield Rural (next)
3. Complete CyberShield Rural Phase 01 gate review
