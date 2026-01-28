# Venture Forge Skills

Skills are the execution instructions Claude Code follows for each phase. They define **how** to do the work that the process defines.

## Structure

```
skills/
├── README.md                          ← This file
├── {phase-id}/
│   ├── generate-prompts.md            ← Create research prompts
│   └── process-research.md            ← Process results into outputs
```

## Skill File Format

Each skill file contains:

1. **Purpose** - What this skill accomplishes
2. **Prerequisites** - What must exist before running
3. **Instructions** - Step-by-step execution guide
4. **Output Format** - Exact format for outputs
5. **Quality Checklist** - Validation criteria
6. **Version History** - Changes and learnings

## How Skills Are Used

1. Claude Code reads the phase definition from `process/phases/{phase}.yaml`
2. Phase definition specifies which skills to execute
3. Claude Code reads the skill file and follows instructions precisely
4. Outputs are validated against the skill's quality checklist
5. Phase gate criteria are checked

## Updating Skills

When a skill needs improvement:

1. Identify the gap (what went wrong or could be better)
2. Update the skill file with the fix
3. Add entry to Version History section
4. Commit with clear message about what changed and why

Skills improve through use. Every project run is an opportunity to refine them.

## Skill Naming Convention

- `generate-prompts.md` - Creates research prompts for user to run in Claude Deep Research
- `process-research.md` - Processes uploaded research results into phase outputs
- `synthesize.md` - Combines multiple inputs into a single output
- `validate.md` - Checks outputs against criteria

## Current Skills

| Phase | Skills |
|-------|--------|
| 01-capital | generate-prompts, process-research |
| 02-problem | generate-prompts, process-research |
| 03-market | generate-prompts, process-research |
| 04-competitive | generate-prompts, process-research |
| 05-solution | synthesize (no research, uses prior phases) |
| 06-business | generate-prompts, process-research |
| 07-risk | synthesize, validate |
| 08-materials | compile-evidence, generate-materials |
| 09-architecture | generate-spec |
| 10-build | (uses Claude Code directly) |
| 11-traction | generate-launch-plan |
| 12-funding | generate-applications |
