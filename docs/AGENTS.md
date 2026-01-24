# Venture Forge Agent Architecture

Specialized AI agents that handle research and analysis, with human quality gates between phases.

## Design Principles

1. **Agents research, humans decide**: Agents gather evidence and options; humans make strategic decisions
2. **Evidence over opinion**: Every agent output must cite third-party sources
3. **Honest analysis**: Never hide competitors or risks; surface them early
4. **Portfolio scale**: Architecture supports hundreds of concurrent opportunities

---

## Agent Roster

### 1. Capital Scout Agent

**Role**: Identify and profile funding sources

**Capabilities**:
- Parse investor criteria from conversations/documents
- Match opportunities to funding requirements
- Track funding timelines and decision processes

**Inputs**:
- Investor meeting notes
- Grant program descriptions
- Accelerator criteria pages

**Outputs**:
```yaml
capital_profile:
  source_name: string
  amount_available: number
  criteria:
    verticals: string[]
    stage: string
    requirements: string[]
  timeline: string
  decision_makers: string[]
  match_score: number  # How well current pipeline matches
```

**Tools**:
- Document parsing
- Web research
- Database queries

---

### 2. Research Agent

**Role**: Deep-dive problem space research with citations

**Capabilities**:
- Search academic and industry databases
- Find and verify statistics
- Calculate market sizing (TAM/SAM)
- Identify pain points with evidence

**Inputs**:
- Problem hypothesis
- Target vertical/market
- Capital criteria constraints

**Outputs**:
```yaml
research_brief:
  problem_statement: string
  evidence:
    - stat: string
      source: string
      url: string
      date: string
  market_sizing:
    tam: number
    tam_source: string
    sam: number
    sam_source: string
    target: number
    target_rationale: string
  pain_points:
    - pain: string
      evidence: string
      severity: 1-10
```

**Tools**:
- Web search
- Industry database access
- PDF/report parsing
- Citation verification

**Quality Standards**:
- Minimum 3 third-party sources per claim
- All URLs must be accessible
- Statistics must include date/source

---

### 3. Validation Agent

**Role**: Stress-test problem validity and solution fit

**Capabilities**:
- Cross-reference claims against multiple sources
- Identify contradicting evidence
- Assess data availability for proposed solution
- Flag assumptions that need verification

**Inputs**:
- Research brief from Research Agent
- Solution hypothesis

**Outputs**:
```yaml
validation_report:
  confidence_score: 0-100
  validated_claims:
    - claim: string
      sources: string[]
      confidence: high|medium|low
  flagged_assumptions:
    - assumption: string
      risk: string
      verification_needed: string
  data_availability:
    - data_type: string
      availability: confirmed|likely|uncertain
      source: string  # e.g., "HIPAA-mandated"
  recommendation: proceed|revise|abandon
```

**Tools**:
- Cross-reference search
- Regulatory database lookup
- Industry standard verification

---

### 4. Competitive Intel Agent

**Role**: Honest competitive landscape analysis

**Capabilities**:
- Identify all competitors (no hiding)
- Analyze offerings, pricing, target markets
- Find market gaps with evidence
- Build defensible positioning

**Inputs**:
- Solution description
- Target market
- Research brief

**Outputs**:
```yaml
competitive_analysis:
  competitors:
    - name: string
      offering: string
      target_market: string
      pricing: string
      strengths: string[]
      weaknesses: string[]
      gap_for_us: string
  market_gaps:
    - gap: string
      evidence: string
      source: string
  positioning:
    statement: string
    evidence:
      - source: string
        finding: string
        url: string
  honest_risks:
    - risk: string
      mitigation: string
```

**Quality Standards**:
- Must identify at least 3 competitors (or document why none exist with evidence)
- Positioning must be backed by third-party research
- Must surface risks, not hide them

---

### 5. Solution Architect Agent

**Role**: Design MVP specifications

**Capabilities**:
- Define feature sets (MVP vs future)
- Create technical architecture
- Plan integration strategies
- Estimate build complexity

**Inputs**:
- Validated problem
- Competitive gaps
- Technical constraints

**Outputs**:
```yaml
solution_spec:
  value_proposition: string
  features:
    mvp:
      - feature: string
        rationale: string
        complexity: low|medium|high
    phase_2:
      - feature: string
        trigger: string  # When to build
  architecture:
    type: string  # e.g., "Cloud-native SaaS"
    components: string[]
    integrations: string[]
  integration_strategy:
    crawl: string  # Manual/file-based
    walk: string   # API integration
    run: string    # Real-time/embedded
  build_estimate:
    mvp_scope: string
    key_risks: string[]
```

---

### 6. Business Case Agent

**Role**: Assemble investor-ready materials

**Capabilities**:
- Generate presentation content
- Integrate citations throughout
- Ensure cross-document consistency
- Address objections proactively

**Inputs**:
- All previous agent outputs
- Presentation templates

**Outputs**:
```yaml
business_case:
  narrative:
    problem: string
    solution: string
    why_us: string
    why_now: string
  materials:
    - type: "landing_page"
      file: "index.html"
    - type: "product_spec"
      file: "product-spec.html"
    - type: "research"
      file: "research.html"
  objections_addressed:
    - objection: string
      response: string
      evidence: string
  consistency_check:
    stats_aligned: boolean
    all_cited: boolean
    links_verified: boolean
```

---

### 7. Customer ID Agent

**Role**: Build qualified prospect lists

**Capabilities**:
- Define ideal customer profile
- Query industry databases
- Score and prioritize prospects
- Research contact information

**Inputs**:
- Target market definition
- Solution fit criteria
- Pain indicators

**Outputs**:
```yaml
prospect_list:
  ideal_customer_profile:
    characteristics: string[]
    pain_indicators: string[]
    disqualifiers: string[]
  prospects:
    - organization: string
      location: string
      size_metrics: object
      pain_score: 1-10
      contacts:
        - name: string
          title: string
          email: string
          linkedin: string
      notes: string
  total_prospects: number
  high_priority: number
```

**Data Sources**:
- Industry association databases
- LinkedIn
- Public filings
- News mentions

---

### 8. Outreach Agent

**Role**: Personalized prospect engagement

**Capabilities**:
- Generate personalized outreach
- Track engagement
- Schedule follow-ups
- Prepare discovery call briefs

**Inputs**:
- Prospect list
- Business case materials
- Outreach templates

**Outputs**:
```yaml
outreach_campaign:
  prospect: string
  messages:
    - channel: email|linkedin|phone
      content: string
      personalization_points: string[]
      sent_date: date
      response: string
  status: not_started|in_progress|meeting_scheduled|negotiating|committed|declined
  next_action: string
  next_date: date
```

**Note**: Human reviews all outreach before sending

---

## Orchestration

### Agent Workflow

```
                    Human Director
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │         Orchestration Layer          │
        │  (Task queue, state management)      │
        └─────────────────────────────────────┘
                          │
    ┌─────────┬─────────┬─┴───────┬─────────┬─────────┐
    ▼         ▼         ▼         ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Capital│ │Research│ │Valid- │ │Compet-│ │Solution│ │Biz    │
│Scout  │ │       │ │ation  │ │itive  │ │Arch   │ │Case   │
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘
    │         │         │         │         │         │
    └─────────┴─────────┴────┬────┴─────────┴─────────┘
                             ▼
                    ┌─────────────────┐
                    │  Quality Gates  │
                    │ (Human Review)  │
                    └─────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Portfolio State │
                    │   (GitHub)      │
                    └─────────────────┘
```

### Parallel Execution

Multiple opportunities can be processed simultaneously:

```
Opportunity A: [Research ████████░░] → Awaiting validation
Opportunity B: [Competitive ██████████] → Complete, awaiting review
Opportunity C: [Customer ID ████░░░░░░] → In progress
Opportunity D: [Capital Scout ██░░░░░░░░] → Just started
```

### Human Quality Gates

Every phase transition requires human approval:

| Gate | Human Reviews | Approval Criteria |
|------|---------------|-------------------|
| Research → Validation | Problem brief | "Is this problem worth solving?" |
| Validation → Design | Validation report | "Do I believe this evidence?" |
| Design → Evidence | Solution spec | "Is this buildable?" |
| Evidence → Competitive | Citation library | "Is every claim sourced?" |
| Competitive → Business Case | Analysis | "Is positioning defensible?" |
| Business Case → Customer ID | Materials | "Would I invest?" |
| Customer ID → Outreach | Prospect list | "Are these the right targets?" |
| Outreach → Funding | LOI/contract | "Is this commitment solid?" |

---

## Implementation Notes

### Agent Communication

Agents communicate through structured outputs (YAML/JSON), not free-form text. This enables:
- Automated validation of outputs
- Easy handoff between agents
- Portfolio-wide analytics
- Human review of specific fields

### State Management

All state lives in GitHub:
- Opportunities = GitHub Issues (epics)
- Phase outputs = Issue comments
- Status = Labels
- Progress = Sub-issues

### Scaling

To process 100 opportunities:
1. Capital Scout identifies 5 funding sources
2. Research Agent explores 200 problem spaces (parallel)
3. Validation Agent filters to 100 viable problems
4. Human reviews top 50 (batch approval)
5. Remaining agents process in parallel
6. Human reviews at each gate (batch mode)

Expected throughput: 20-50 opportunities through full pipeline per month with one human director.
