# Project: venture-forge

## Workflow Instructions for Claude

This is the Venture Forge framework - an agentic AI system for systematically identifying, validating, and launching ventures at scale.

### Session Start

When starting a conversation:

1. **Check portfolio status** - Query GitHub for active opportunities
2. **Announce state** - Show what phase each opportunity is in
3. **Show available actions** - Based on portfolio state

```bash
# Query GitHub for portfolio state
gh issue list --label "opportunity" --json number,title,labels

# Get details on specific opportunity
gh issue view <number>
```

### Session Start Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 VENTURE FORGE PORTFOLIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Active Opportunities:
  • ClaimIQ - Phase 6 (Business Case) - READY FOR PHASE 7
  • [Others from GitHub query]

Available Actions:
  • status - Full portfolio view
  • continue [opportunity] - Work on next phase
  • scout [source] - Add new capital source
  • research [area] - Start new opportunity

What would you like to do?
```

### Commands

| Command | Description |
|---------|-------------|
| `status` | Show full portfolio with phases |
| `scout [source]` | Add new capital source (Phase 1) |
| `research [area]` | Research new problem space (Phase 2) |
| `continue [opportunity]` | Work on next phase for opportunity |
| `review [opportunity]` | Show current phase output for review |
| `approve` | Approve current phase, move to next |
| `revise [feedback]` | Revise current phase output |

### Phase Workflow

Each opportunity progresses through 9 phases:

1. **Capital Scout** → Capital source profile
2. **Problem Research** → Problem brief with TAM/SAM
3. **Solution Design** → MVP specification
4. **Evidence Building** → Citation library
5. **Competitive Intel** → Competitive analysis
6. **Business Case** → Investor materials
7. **Customer ID** → Prospect list
8. **Outreach & LOI** → Customer commitment
9. **Funding Activation** → Funded venture

See `docs/WORKFLOW.md` for detailed phase documentation.

### Agent Behavior

When working on a phase:

1. **Research thoroughly** - Use web search, read documents, gather evidence
2. **Cite everything** - Every claim needs a third-party source
3. **Be honest** - Surface risks and competitors, don't hide them
4. **Present for review** - Show structured output, await human approval
5. **Update GitHub** - Record progress in issue comments

### Quality Standards

**Evidence Requirements:**
- Every statistic must have a third-party source
- All URLs must be verified accessible
- Minimum 3 sources per major claim

**Competitive Analysis:**
- Must identify real competitors
- Differentiation must be evidence-backed
- Risks must be surfaced, not hidden

**Business Case:**
- All stats consistent across documents
- Every claim linked to source
- Objections addressed proactively

### Portfolio Tracking

Opportunities are tracked as GitHub issues:

```bash
# Create new opportunity
gh issue create --title "Opportunity: [Name]" --label "opportunity,phase:1-scout"

# Update phase
gh issue edit <number> --remove-label "phase:1-scout" --add-label "phase:2-research"

# Add phase output
gh issue comment <number> --body "## Phase 2 Output\n..."

# Complete opportunity
gh issue close <number> --comment "Funded and launched!"
```

### ClaimIQ Reference

The ClaimIQ project (`/Users/chrisroberts/Projects/claimiq/`) is the proof-of-concept:

- **Current Phase**: 6 (Business Case complete)
- **Next Phase**: 7 (Customer ID)
- **Materials**: index.html, product-spec.html, research.html
- **Evidence**: All stats cited to third-party sources
- **Positioning**: Rural-first, backed by Black Book Research

Use ClaimIQ as the template for how opportunities should be developed.

---

## Project Structure

```
venture-forge/
├── CLAUDE.md           # This file
├── README.md           # Project overview
├── docs/
│   ├── WORKFLOW.md     # 9-phase workflow details
│   ├── AGENTS.md       # Agent specifications
│   └── QUALITY-GATES.md # Human review criteria
├── portfolio/          # Opportunity references
├── templates/          # Reusable templates
└── scripts/            # Automation
```

---

## Labels Reference

| Label | Purpose |
|-------|---------|
| `opportunity` | Marks issue as a venture opportunity |
| `phase:1-scout` | Capital Scout phase |
| `phase:2-research` | Problem Research phase |
| `phase:3-design` | Solution Design phase |
| `phase:4-evidence` | Evidence Building phase |
| `phase:5-competitive` | Competitive Intel phase |
| `phase:6-bizcase` | Business Case phase |
| `phase:7-customerid` | Customer ID phase |
| `phase:8-outreach` | Outreach & LOI phase |
| `phase:9-funding` | Funding Activation phase |
| `status:active` | Currently being worked |
| `status:review` | Awaiting human review |
| `status:blocked` | Blocked on something |
