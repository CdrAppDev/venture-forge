# Venture Forge Agent Architecture

This is a **machine**, not a tool. Autonomous AI agents perform coordinated work to transform funding criteria into funded ventures. Humans provide strategic oversight at decision points. The machine handles everything else.

## The Agentic Difference

Traditional software tools wait for human input. Venture Forge agents are **autonomous workers**:

- **Research agents** investigate problems for 30-60 minutes without supervision, producing comprehensive cited reports
- **Synthesis agents** reason through complex multi-source material, resolving contradictions and identifying gaps
- **Generation agents** produce investor-ready materials with consistent narratives
- **Build agents** develop software from specs, writing code, tests, and documentation

The orchestration layer (itself an AI agent) coordinates this work across dozens of concurrent opportunities.

## Design Principles

1. **Agents execute, humans decide**: Agents do the work; humans make strategic calls at phase gates
2. **Evidence over opinion**: Every claim must trace to a third-party source
3. **Honest analysis**: Surface competitors and risks early—hiding them helps no one
4. **Parallel at scale**: Architecture supports dozens of opportunities running concurrently
5. **AI-native development**: Code generation, not code writing

---

## Technology Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         VENTURE FORGE STACK                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                         RESEARCH LAYER                               │    │
│  │                 Claude Deep Research (Manual Workflow)               │    │
│  │                                                                      │    │
│  │  • Claude Code generates research prompts                           │    │
│  │  • User runs prompts in Claude Deep Research                        │    │
│  │  • Results uploaded to project research/ folder                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      PROCESSING & BUILD LAYER                        │    │
│  │                         Claude Opus 4.5                              │    │
│  │                                                                      │    │
│  │  • Research synthesis and structuring                                │    │
│  │  • Material generation (decks, documents)                            │    │
│  │  • Code generation and development (via Claude Code)                 │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      ORCHESTRATION LAYER                             │    │
│  │                          Claude Code                                 │    │
│  │                                                                      │    │
│  │  • Workflow state management                                         │    │
│  │  • Phase progression logic                                           │    │
│  │  • Human review routing                                              │    │
│  │  • Portfolio tracking                                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Roster

### Research & Validation Agents (Phases 1-4)

#### 1. Capital Scout Agent

**Role**: Identify and profile funding sources

**Phase**: 1 - Capital Thesis

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
  match_score: number
```

**Tools**: Document parsing, web research, database queries

---

#### 2. Problem Research Agent

**Role**: Deep-dive problem space research with citations

**Phase**: 2 - Problem Thesis

**Capabilities**:
- Search academic and industry databases
- Find and verify statistics
- Document pain points with evidence
- Synthesize customer voice from public sources

**Inputs**:
- Problem hypothesis
- Target vertical/market
- Capital criteria constraints

**Outputs**:
```yaml
problem_brief:
  problem_statement: string
  evidence:
    - stat: string
      source: string
      url: string
      date: string
  pain_points:
    - pain: string
      evidence: string
      severity: 1-10
  customer_voice:
    - quote: string
      source: string
```

**Tools**: Claude Deep Research (manual), web search, industry databases

**Quality Standards**:
- Minimum 3 third-party sources per claim
- All URLs must be accessible
- Statistics must include date/source

---

#### 3. Market Sizing Agent

**Role**: Calculate and validate market size

**Phase**: 3 - Market Thesis

**Capabilities**:
- Calculate TAM/SAM/SOM with methodology
- Identify market segments
- Research growth trends
- Assess market timing

**Inputs**:
- Problem brief from Phase 2
- Target customer definition
- Geographic scope

**Outputs**:
```yaml
market_sizing:
  tam:
    value: number
    calculation: string
    sources: string[]
  sam:
    value: number
    calculation: string
    sources: string[]
  som:
    value: number
    calculation: string
    rationale: string
  segments:
    - name: string
      size: number
      characteristics: string[]
  growth_trends:
    - trend: string
      source: string
      date: string
```

**Tools**: Claude Deep Research (manual), industry reports, government databases

---

#### 4. Competitive Intel Agent

**Role**: Honest competitive landscape analysis

**Phase**: 4 - Competitive Thesis

**Capabilities**:
- Identify all competitors (no hiding)
- Analyze offerings, pricing, target markets
- Find market gaps with evidence
- Build defensible positioning

**Inputs**:
- Solution description
- Target market
- Problem brief

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
- Must identify at least 3 competitors (or document why none exist)
- Positioning must be backed by third-party research
- Must surface risks, not hide them

---

### Design & Model Agents (Phases 5-7)

#### 5. Solution Architect Agent

**Role**: Design MVP specifications

**Phase**: 5 - Solution Thesis

**Capabilities**:
- Define feature sets (MVP vs future)
- Create technical architecture overview
- Plan integration strategies
- Assess build complexity

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
    future:
      - feature: string
        trigger: string
  architecture:
    type: string
    components: string[]
    integrations: string[]
  integration_strategy:
    crawl: string
    walk: string
    run: string
```

---

#### 6. Business Model Agent

**Role**: Design and validate business model

**Phase**: 6 - Business Thesis

**Capabilities**:
- Research revenue models in the space
- Calculate unit economics
- Build financial projections
- Identify key assumptions

**Inputs**:
- Solution spec
- Market sizing
- Competitive pricing data

**Outputs**:
```yaml
business_model:
  revenue_model: string
  pricing:
    mechanism: string
    tiers: object[]
  unit_economics:
    cac: number
    ltv: number
    ltv_cac_ratio: number
    gross_margin: number
    payback_period: string
  projections:
    year_1: object
    year_2: object
    year_3: object
  assumptions:
    - assumption: string
      basis: string
      risk_level: low|medium|high
```

---

#### 7. Risk Assessment Agent

**Role**: Identify and plan for risks

**Phase**: 7 - Risk Thesis

**Capabilities**:
- Research failure modes in the space
- Identify regulatory risks
- Map competitive threats
- Anticipate investor objections

**Inputs**:
- All previous phase outputs
- Industry research

**Outputs**:
```yaml
risk_register:
  risks:
    - category: string
      risk: string
      likelihood: low|medium|high
      impact: low|medium|high
      mitigation: string
  investor_objections:
    - objection: string
      response: string
      evidence: string
  regulatory_requirements:
    - requirement: string
      status: string
      timeline: string
```

---

### Materials & Funding Agents (Phases 8-10)

#### 8. Evidence Compiler Agent

**Role**: Assemble and verify all evidence

**Phase**: 8 - Case Assembly

**Capabilities**:
- Compile all citations into Evidence Library
- Create Claim-to-Source Matrix
- Verify all links are accessible
- Identify gaps requiring additional research

**Inputs**:
- All phase outputs (1-7)

**Outputs**:
```yaml
evidence_library:
  claims:
    - claim: string
      source: string
      url: string
      date: string
      verified: boolean
      used_in: string[]
  verification_report:
    total_claims: number
    verified: number
    broken_links: number
    gaps: string[]
```

---

#### 9. Narrative Agent

**Role**: Generate investor-ready materials

**Phase**: 9 - Narrative Assembly

**Capabilities**:
- Generate presentation content
- Integrate citations throughout
- Ensure cross-document consistency
- Address objections proactively

**Inputs**:
- All previous phase outputs
- Evidence library
- Presentation templates

**Outputs**:
```yaml
pitch_materials:
  files:
    - type: string
      file: string
      status: string
  narrative:
    problem: string
    solution: string
    why_us: string
    why_now: string
  consistency_check:
    stats_aligned: boolean
    all_cited: boolean
    links_verified: boolean
```

---

---

### Build & Traction Agents (Phases 10-12)

#### 10. Architecture Agent

**Role**: Create detailed technical specifications

**Phase**: 10 - MVP Architecture

**Capabilities**:
- Design system architecture
- Create data models
- Define API specifications
- Design UI/UX wireframes
- Plan infrastructure
- Create development timeline

**Inputs**:
- Solution spec from Phase 5
- Technical constraints
- Compliance requirements

**Outputs**:
```yaml
architecture_spec:
  tech_stack:
    frontend: string
    backend: string
    database: string
    ai_ml: string
    infrastructure: string
  data_model:
    entities:
      - name: string
        fields: string[]
        relationships: string[]
  api_spec:
    endpoints:
      - method: string
        path: string
        description: string
        auth: string
  ui_spec:
    screens:
      - name: string
        purpose: string
        components: string[]
    user_flows:
      - name: string
        steps: string[]
  infrastructure:
    environments: string[]
    ci_cd: string
    monitoring: string
  timeline:
    phases:
      - name: string
        deliverables: string[]
```

**Tools**: Claude Code for spec generation, diagramming tools

---

#### 11. Build Agent

**Role**: AI-accelerated software development

**Phase**: 11 - MVP Build

**Capabilities**:
- Generate code using Claude Code
- Implement features from specs
- Write tests
- Set up infrastructure
- Perform code reviews
- Create documentation

**Inputs**:
- Architecture spec from Phase 11
- Existing codebase (if any)
- External API documentation

**Outputs**:
```yaml
build_status:
  repository:
    url: string
    branches: string[]
  components:
    - name: string
      status: not_started|in_progress|complete
      tests:
        coverage: number
        passing: boolean
      files: string[]
  deployment:
    environment: string
    url: string
    status: string
  security:
    vulnerabilities: number
    compliance: string[]
  documentation:
    readme: boolean
    api_docs: boolean
    deployment_guide: boolean
```

**Tools**: Claude Code (primary), GitHub, CI/CD pipelines

**Quality Standards**:
- All code must have tests
- Security review before deployment
- Documentation for all components
- Code review for all changes

---

#### 12. Customer Traction Agent

**Role**: Secure customer commitment before funding

**Phase**: 12 - Customer Traction

**Capabilities**:
- Targeted outreach to pilot customers
- Demo and trial coordination
- LOI and contract negotiation support
- First customer onboarding
- Traction documentation for funders

**Inputs**:
- Working software from Phase 11
- Customer target list from research phases
- Pitch materials from Phase 9

**Outputs**:
```yaml
traction_status:
  commitment_type: "LOI" | "Contract" | "Paying Customer"
  customers:
    - name: string
      type: string
      terms: string
      value: number
      signed_date: date
      contact: string
      willing_to_reference: boolean
  pipeline:
    qualified_leads: number
    in_discussion: number
    negotiating: number
  proof_for_funders:
    lois_signed: number
    contracts_signed: number
    mrr: number
    pipeline_value: number
```

**Activities**:
- Outreach campaign support
- Demo preparation
- LOI/contract template generation
- Reference customer coordination
- Traction summary for funders

---

### Funding Agent (Phase 13)

#### 13. Funding Execution Agent

**Role**: Close funding with proof of traction

**Phase**: 13 - Funding Execution

**Capabilities**:
- Prepare funding applications with traction evidence
- Build due diligence data room
- Track application status
- Support negotiations

**Inputs**:
- Pitch materials from Phase 9
- Evidence library from Phase 8
- Traction proof from Phase 12
- Funder requirements

**Outputs**:
```yaml
funding_status:
  traction_summary:
    lois: number
    contracts: number
    revenue: number
    pipeline: number
  applications:
    - funder: string
      submitted: date
      status: string
      traction_highlighted: string
  data_room:
    url: string
    documents: number
    includes_traction: boolean
  due_diligence:
    questions_received: number
    questions_answered: number
    pending: string[]
  closed_funding:
    amount: number
    source: string
    date: date
    terms: string
```

**Activities**:
- Application preparation with traction evidence
- Data room assembly
- Due diligence response support
- Term sheet review support

---

## Orchestration

### Agent Workflow

```
                         Human Director
                               │
                               ▼
             ┌─────────────────────────────────────┐
             │         Orchestration Layer          │
             │           (Claude Code)              │
             └─────────────────────────────────────┘
                               │
     ┌─────────────┬───────────┼───────────┬─────────────┐
     │             │           │           │             │
     ▼             ▼           ▼           ▼             ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│RESEARCH │  │ DESIGN  │  │MATERIALS│  │ BUILD & │  │ FUNDING │
│ AGENTS  │  │ AGENTS  │  │ AGENTS  │  │TRACTION │  │ AGENT   │
│ (1-4)   │  │ (5-7)   │  │ (8-9)   │  │ (10-12) │  │  (13)   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
     │             │           │           │             │
     └─────────────┴───────────┼───────────┴─────────────┘
                               ▼
                     ┌─────────────────┐
                     │  Quality Gates  │
                     │ (Human Review)  │
                     └─────────────────┘
                               │
                               ▼
                     ┌─────────────────┐
                     │ Portfolio State │
                     │  (File System)  │
                     └─────────────────┘
```

### Phase Progression

```
RESEARCH & VALIDATION          DESIGN & MODEL
┌────────────────────────┐    ┌────────────────────────┐
│ 1. Capital ──▶ 2. Problem ──▶ 3. Market ──▶ 4. Competitive │
└────────────────────────┘    └────────────────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ 5. Solution ──▶ 6. Business ──▶ 7. Risk │
                              └────────────────────────┘
                                         │
                                         ▼
MATERIALS                          BUILD & TRACTION
┌────────────────────────┐    ┌────────────────────────┐
│ 8. Case ──▶ 9. Narrative │ ──▶ │ 10. Arch ──▶ 11. Build ──▶ 12. Traction │
└────────────────────────┘    └────────────────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │      13. Funding       │
                              │   (with traction proof)│
                              └────────────────────────┘
```

### Parallel Execution

Multiple opportunities can be processed simultaneously:

```
Opportunity A: [Phase 11 - Build    ████████░░] → In development
Opportunity B: [Phase 7 - Risk      ██████████] → Awaiting review
Opportunity C: [Phase 4 - Competitive ████░░░░] → Research in progress
Opportunity D: [Phase 1 - Capital   ██░░░░░░░░] → Just started
Opportunity E: [Phase 12 - Traction ████████░░] → Getting first customer
```

### Human Quality Gates

Every phase transition requires human approval:

| Phase | Agent | Human Reviews | Approval Question |
|-------|-------|---------------|-------------------|
| 1 → 2 | Capital Scout | Funding profiles | "Which sources should we target?" |
| 2 → 3 | Problem Research | Problem brief | "Is this problem real?" |
| 3 → 4 | Market Sizing | TAM/SAM/SOM | "Is the market big enough?" |
| 4 → 5 | Competitive Intel | Analysis | "Is positioning defensible?" |
| 5 → 6 | Solution Architect | MVP spec | "Is this buildable?" |
| 6 → 7 | Business Model | Financials | "Is this viable?" |
| 7 → 8 | Risk Assessment | Risk register | "Are risks manageable?" |
| 8 → 9 | Evidence Compiler | Citation library | "Is everything verifiable?" |
| 9 → 10 | Narrative | Pitch materials | "Would I invest?" |
| 10 → 11 | Architecture | Tech spec | "Ready to build?" |
| 11 → 12 | Build | Working software | "Ready for customers?" |
| 12 → 13 | Customer Traction | LOI/Customer proof | "Enough traction for funders?" |
| 13 → Done | Funding Execution | Closed funding | "Deal terms acceptable?" |

---

## Implementation Notes

### Agent Communication

Agents communicate through structured outputs (YAML/JSON), not free-form text. This enables:
- Automated validation of outputs
- Easy handoff between agents
- Portfolio-wide analytics
- Human review of specific fields

### State Management

All state lives in the file system:
- Opportunities = Project folders
- Phase outputs = Structured files
- Status = Status tracking files
- Progress = Git commits

### Scaling

To process multiple opportunities:
1. Capital Scout identifies funding sources
2. Problem Research explores problem spaces (via Claude Deep Research)
3. Market/Competitive agents process in parallel
4. Human reviews at each gate (batch mode)
5. Build agents work sequentially per opportunity
6. Launch can run parallel across funded ventures

Expected throughput: 10-20 opportunities through research phases per month, 2-4 through build phases per month with one human director.

### AI-Accelerated Build

The Build phase (11-12) uses Claude Code to:
- Generate code from specifications
- Implement features rapidly
- Write comprehensive tests
- Set up infrastructure as code
- Create documentation

This reduces typical MVP build time significantly while maintaining quality through:
- Specification-driven development
- Test coverage requirements
- Security review gates
- Human approval at milestones
