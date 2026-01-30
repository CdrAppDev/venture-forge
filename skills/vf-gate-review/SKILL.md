---
name: vf-gate-review
description: >
  Conduct human gate review for any completed Venture Forge phase. Reads the
  validation report, auto-fixes mechanical issues (missing sources, count
  mismatches, data inconsistencies), re-validates after fixes, then presents
  the evidence briefing for human blocking decisions. Updates portfolio.yaml
  and portfolio/{project}.yaml based on proceed/revise/kill. Activate when
  phase_status is "gate-review" in portfolio.yaml.
license: MIT
metadata:
  version: "1.0.0"
  phase: all
  when: gate_review
---

# Gate Review

Conduct human gate review for any completed phase. Bridges the gap between validation output and human decision-making by auto-fixing mechanical issues, presenting the evidence briefing, collecting blocking decisions, and updating portfolio state.

## Prerequisites

- `portfolio.yaml` shows `phase_status: "gate-review"` for the target project
- Validation report exists at `{project}/phases/{phase_id}/validation-report.md`
- Phase definition exists at `process/phases/{phase_id}.yaml`

If multiple projects are in gate-review, ask the human which one to review.

## Step 1: Load Context

Read these files in order:

1. `portfolio.yaml` — identify the project and its `current_phase`
2. `portfolio/{project}.yaml` — get phase history, `pending_decisions`, previous gate notes
3. `process/phases/{phase_id}.yaml` — get `gate.question`, `gate.criteria`, and `gate.outcomes` (proceed/revise/kill with descriptions and `next_phase`)
4. `{project}/phases/{phase_id}/validation-report.md` — the full validation output
5. `references/auto-fix-scope.md` — rules for what can be auto-fixed

The phase YAML provides the gate structure. This keeps the skill phase-generic — it reads gate criteria and outcomes from the definition rather than hardcoding phase-specific logic.

## Step 2: Auto-Fix Mechanical Issues

Scan the validation report's Warnings and Failures sections for issues that are mechanically fixable. See `references/auto-fix-scope.md` for the complete scope definition.

**Auto-fixable categories:**
- Count mismatches (YAML header vs actual array length)
- Missing source entries (source cited in thesis but not in sources.md)
- Uncited claims with known source (validator identified the suggested source)
- Data inconsistencies (thesis says X, YAML says Y — YAML is source of truth)
- Footer/summary count mismatches (says N but lists M items)

**NOT auto-fixable (skip these — they require human judgment):**
- Adding or removing profiles or evidence entries
- Changing viability or confidence assessments
- Rewriting narrative sections
- Resolving conflicting data between external sources
- Any issue involving strategic content or interpretation

**Execution:**
1. For each Warning and Failure, check if it matches an auto-fix category
2. If fixable: apply the fix, log it (file, field, old value, new value)
3. If not fixable: leave it for human review
4. After all fixes: note total count ("N auto-fixes applied")

**Source of truth hierarchy:** YAML array data > YAML header metadata > thesis text > sources.md summary counts

## Step 3: Re-Validate (If Fixes Applied)

If auto-fixes were applied:
1. Identify the validate skill from `process/phases/{phase_id}.yaml` under `skills.validate.skill`
2. Re-run that validate skill against the fixed files
3. The new validation report replaces the old one
4. The auto-fix log is preserved in the gate review record (Step 8)

If no fixes were applied, skip this step.

If no validate skill exists for the phase (phases 03-12 not yet built), note "Re-validation skipped: no validate skill defined for phase {id}" and present the original report.

## Step 4: Present Evidence Briefing

Extract from the (potentially updated) validation report and present to the human conversationally:

```
## Gate Review: {Phase Name}
### Project: {Project Name}

### Validation Summary
- Checks: {passed}/{total} passed, {warnings} warnings, {failures} failures
- Auto-fixes applied: {N} (details in gate-review-record.md)
- Verdict: {verdict}

### What the Evidence Shows
[Key metrics from validation report Evidence Briefing]

### What's Strong
[From validation report — specific strengths with data points]

### What's Weak or Unresolved
[From validation report — minus items resolved by auto-fix]

### Blocking Decision
{gate.question from phase YAML}

(a) Proceed — {gate.outcomes.proceed.description}
(b) Revise — {gate.outcomes.revise.description}
(c) Kill — {gate.outcomes.kill.description}

### Strategic Decisions (For Your Awareness)
[From validation report — each with target phase for revisiting]
[Deferred by default unless you want to decide now]
```

**Rules:**
- The validation report's Evidence Briefing is the source of truth. Do not re-analyze the data.
- Present blocking decisions with explicit labels (a/b/c) for concise response.
- Strategic decisions are shown but marked deferrable. The human can decide any or defer all.
- This is conversational output in the terminal, not a file.

## Step 5: Collect Blocking Decisions

Ask the human for the blocking decision:

```
What is your decision? (a) Proceed, (b) Revise, (c) Kill
```

**If proceed:** Move to Step 6.

**If revise:** Ask:
```
What needs revision? The validation report identified these remaining items:
[list remaining warnings/failures not resolved by auto-fix]
```
The human's response becomes `gate_notes`. Move to Step 7.

**If kill:** Ask:
```
Any notes for the archive? (optional)
```
Move to Step 7.

## Step 6: Record Strategic Decisions

Present strategic decisions from the validation report:

```
These strategic decisions can be deferred to later phases:

1. {Decision} — revisit after Phase {NN}
2. {Decision} — revisit after Phase {NN}

Decide any now, or defer all? (type numbers to decide, or "defer all")
```

For decisions the human makes now: record the choice and rationale.
For deferred decisions: record as "deferred — revisit after Phase {NN}".

## Step 7: Update Portfolio

Update both portfolio files per `references/portfolio-update-spec.md`:

**On Proceed:**
- `portfolio.yaml`: set `current_phase` to next phase (from `gate.outcomes.proceed.next_phase`), set `phase_status` to `"pending"`
- `portfolio/{project}.yaml`: mark current phase `"complete"` with `gate_decision: "proceed"`, `gate_date`, `gate_notes`. Add next phase entry with `status: "pending"`, `started: "{date}"`.

**On Revise:**
- `portfolio.yaml`: set `phase_status` to `"processing"`
- `portfolio/{project}.yaml`: set `gate_decision: "revise"`, `gate_date`, `gate_notes` with revision scope. Set `phase_status` to `"processing"`.

**On Kill:**
- `portfolio.yaml`: set `phase_status` to `"killed"`
- `portfolio/{project}.yaml`: set `gate_decision: "kill"`, `gate_date`, `gate_notes`.

## Step 8: Write Gate Review Record

Write `{project}/phases/{phase_id}/gate-review-record.md` using the template in `references/gate-review-template.md`.

This record documents:
- Auto-fixes applied (file, change, old/new values)
- Post-fix validation summary
- Blocking decision and rationale
- Strategic decisions (decided or deferred with target phase)
- Revision scope or archive notes (if applicable)

The record lives alongside validation-report.md and thesis.md as the permanent audit trail of the gate decision.

## Phase 00 (Discovery) Gate Variant

When the current phase is `00-discovery`, the gate review follows a **1-to-many** flow instead of the standard single-project flow. The discovery phase produces multiple opportunities, each requiring an individual approve/reject decision.

### How It Differs

1. **Context files** are at `discovery/{run_id}/` instead of `{project}/phases/{phase_id}/`
2. **Validation report** is at `discovery/{run_id}/validation-report.md`
3. **Discovery report** at `discovery/{run_id}/discovery-report.md` contains ranked opportunities
4. **Blocking decision** is per-opportunity, not per-phase

### Presentation

Present each opportunity from the discovery report with its score and rationale:

```
## Discovery Gate Review

### Run: {run_id}

### Opportunities Found: {count}

| # | Opportunity | Score | Recommendation |
|---|-------------|-------|----------------|
| 1 | {name} | {score}/100 | Pursue |
| 2 | {name} | {score}/100 | Investigate |

### For each opportunity:

**{Opportunity Name}** — {score}/100
- Funding sources: {list}
- Total potential: {amount}
- Top signal: {why it scored high}
- Main risk: {key uncertainty}

Decision: (a) Pursue → creates project, starts Phase 01
          (b) Skip → opportunity archived
          (c) Investigate → flagged for manual research before deciding
```

### On Pursue (per opportunity)

For each opportunity the human selects "Pursue":
1. Create project directory at the conventional path
2. Copy `discovery/{run_id}/outputs/{slug}/funder-criteria.md` to `{project}/inputs/funder-criteria.md`
3. Add entry to `portfolio.yaml` with `current_phase: "01-capital"`, `phase_status: "pending"`
4. Create `portfolio/{project}.yaml` with initial phase history

### Gate Review Record

Write `discovery/{run_id}/gate-review-record.md` (not in a project directory) documenting:
- All opportunities presented
- Decision per opportunity (pursue/skip/investigate)
- Human rationale for each decision
- Projects created (with paths)

## Quality Checklist

- [ ] All context files read before presenting to human
- [ ] Auto-fixes limited to scope defined in auto-fix-scope.md
- [ ] Re-validation run after any auto-fixes
- [ ] Evidence briefing presented from validation report (not re-analyzed)
- [ ] Blocking decision collected before strategic decisions
- [ ] Both portfolio files updated consistently
- [ ] Gate review record written with complete audit trail
- [ ] Strategic decisions recorded with target phase for revisiting
