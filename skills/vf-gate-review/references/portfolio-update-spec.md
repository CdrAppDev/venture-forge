# Portfolio Update Specification

Exact YAML field updates for each gate review outcome. Both `portfolio.yaml` (registry) and `portfolio/{project}.yaml` (detail) must be updated consistently.

## Deriving Next Phase

Read `process/phases/{current_phase_id}.yaml` and extract:
```yaml
gate.outcomes.proceed.next_phase
```
This gives the next phase ID (e.g., `"02-problem"` from Phase 01's proceed outcome).

## On Proceed

### portfolio.yaml

```yaml
projects:
  {project-slug}:
    current_phase: "{next_phase_id}"      # e.g., "02-problem"
    phase_status: "pending"
```

### portfolio/{project}.yaml

```yaml
current_phase: "{next_phase_id}"
phase_status: "pending"

phases:
  {current_phase_id}:
    status: "complete"
    gate_decision: "proceed"
    gate_date: "{YYYY-MM-DD}"
    gate_notes: "{any notes from human}"
    pending_decisions: []                  # Clear — all blocking resolved

  {next_phase_id}:
    status: "pending"
    started: "{YYYY-MM-DD}"
```

## On Revise

### portfolio.yaml

```yaml
projects:
  {project-slug}:
    current_phase: "{current_phase_id}"    # Stays the same
    phase_status: "processing"
```

### portfolio/{project}.yaml

```yaml
current_phase: "{current_phase_id}"
phase_status: "processing"

phases:
  {current_phase_id}:
    status: "processing"
    gate_decision: "revise"
    gate_date: "{YYYY-MM-DD}"
    gate_notes: "{revision scope from human}"
    pending_decisions:
      - "{remaining items needing revision}"
```

## On Kill

### portfolio.yaml

```yaml
projects:
  {project-slug}:
    current_phase: "{current_phase_id}"
    phase_status: "killed"
```

### portfolio/{project}.yaml

```yaml
current_phase: "{current_phase_id}"
phase_status: "killed"

phases:
  {current_phase_id}:
    status: "killed"
    gate_decision: "kill"
    gate_date: "{YYYY-MM-DD}"
    gate_notes: "{archive notes from human}"
```

## Date Format

All dates use `YYYY-MM-DD` format (e.g., `2026-01-29`).

## Validation

After updating both files, verify:
1. `portfolio.yaml` `current_phase` matches `portfolio/{project}.yaml` `current_phase`
2. `portfolio.yaml` `phase_status` matches `portfolio/{project}.yaml` `phase_status`
3. Gate decision fields are populated (not null)
4. On proceed: next phase entry exists with `status: "pending"`
