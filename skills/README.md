# Venture Forge Skills

Skills package domain expertise for each phase of the Venture Forge process. They follow the [Agent Skills standard](https://agentskills.io) so Claude Code discovers and applies them automatically.

## Structure (Official Agent Skills Format)

```
skills/
├── README.md
├── vf-{phase}-{action}/
│   ├── SKILL.md              ← Entry point with YAML frontmatter
│   └── references/           ← Supporting docs loaded on demand
│       └── *.md
```

## How Discovery Works (Progressive Disclosure)

1. **Metadata** (~50 tokens) - Claude reads `name` and `description` from YAML frontmatter to decide if skill is relevant
2. **SKILL.md** (~500 tokens) - Full instructions load when skill is matched
3. **references/** (2000+ tokens) - Templates and detailed docs load only when needed

This means dozens of skills can exist without overwhelming context.

## SKILL.md Format

```yaml
---
name: vf-problem-generate-prompts
description: Generate Claude Deep Research prompts for Phase 02...
license: MIT
metadata:
  version: "1.0.0"
  phase: 02-problem
  when: before_research
---

# Skill Title

[Concise instructions, workflow, quality checklist]

See `references/` for detailed templates.
```

**Frontmatter rules (per [Agent Skills spec](https://agentskills.io/specification)):**
- Only 6 top-level fields allowed: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`
- `name` and `description` are required
- Custom fields (`version`, `phase`, `when`) go under `metadata:`
- `name` must match the directory name exactly

## Skill Types

| Type | Purpose | Naming Pattern |
|------|---------|----------------|
| discovery-generate-prompts | Create broad funding scan prompts from venture profile | `vf-discovery-generate-prompts` |
| discovery-process-research | Process scan results into opportunity profiles | `vf-discovery-process-research` |
| discovery-score | Score and rank opportunities against venture profile | `vf-discovery-score` |
| discovery-validate | Validate discovery outputs before gate review | `vf-discovery-validate` |
| generate-prompts | Create research prompts for Claude Deep Research | `vf-{phase}-generate-prompts` |
| process-research | Process uploaded research into phase outputs | `vf-{phase}-process-research` |
| synthesize | Combine prior phase outputs (no new research) | `vf-{phase}-synthesize` |
| validate | Check outputs against gate criteria | `vf-{phase}-validate` |
| generate-spec | Create technical specifications | `vf-{phase}-generate-spec` |
| compile-evidence | Consolidate evidence library | `vf-{phase}-compile-evidence` |
| gate-review | Auto-fix, present evidence briefing, collect human decisions, update portfolio | `vf-gate-review` |
| governance | Writing and quality rules referenced by other skills | `vf-write` |
| present | Generate HTML presentations from phase outputs | `vf-present` |
| expert-generate-prompts | Generate research prompts for domain expert knowledge | `vf-expert-generate-prompts` |
| expert-review | Strategic expert review of phase outputs by domain | `vf-expert-{domain}` |

## How Skills Are Used

1. Claude Code reads phase definition from `process/phases/{phase}.yaml`
2. Phase definition names the skills to execute
3. Claude discovers matching skill by `name` in YAML frontmatter
4. Claude reads SKILL.md instructions
5. Claude loads references only when needed
6. Outputs validated against quality checklist
7. Validate skill checks mechanical completeness
8. Expert review skill evaluates strategic soundness (where available)
9. Gate review presents findings for human decision

## Updating Skills

1. Identify the gap (what went wrong or could be better)
2. Update SKILL.md or references with the fix
3. Bump `version` in YAML frontmatter
4. Commit with clear message about what changed and why

Skills improve through use. Every project run is an opportunity to refine them.

## Current Skills

| Skill | Phase | Status |
|-------|-------|--------|
| `vf-discovery-generate-prompts` | 00 | Complete |
| `vf-discovery-process-research` | 00 | Complete |
| `vf-discovery-score` | 00 | Complete |
| `vf-discovery-validate` | 00 | Complete |
| `vf-capital-generate-prompts` | 01 | Complete |
| `vf-capital-process-research` | 01 | Complete |
| `vf-capital-validate` | 01 | Complete |
| `vf-problem-generate-prompts` | 02 | Complete |
| `vf-problem-process-research` | 02 | Complete |
| `vf-problem-validate` | 02 | Complete |
| `vf-gate-review` | all | Complete |
| `vf-present` | all | Complete |
| `vf-write` | all | Complete |
| `vf-expert-generate-prompts` | platform | Complete |
| `vf-expert-funding` | 01, 08, 12 | Complete |
| Remaining phases | 03-12 | To be built |

Skills for phases 03-12 will be built as the process is tested with real projects.
