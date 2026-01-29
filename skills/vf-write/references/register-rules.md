# Writing Register Rules

Three registers govern all Venture Forge narrative writing. The phase number determines which register applies.

---

## Research Register (Phases 01-07)

**Role:** Research analyst. Present evidence; do not advocate.

### Voice
Third-person analytical. Never first person.

| Allowed | Prohibited |
|---------|-----------|
| The research indicates... | We found... |
| The data suggests... | Our analysis shows... |
| Evidence from [Source] shows... | We identified... |
| This analysis examines... | Our team discovered... |

### Sentence Structure
Data-first. The first sentence of every narrative paragraph should contain a cited fact. Interpretation follows.

**Good:**
> 68% of rural hospitals have no dedicated cybersecurity leader (Black Book Research, June 2025). This staffing gap is compounded by a broader workforce shortage — cybersecurity roles take 70% longer to fill than other healthcare IT positions (HSCC, May 2025), suggesting that rural facilities face structural barriers beyond budget constraints.

*Why it works:* Leads with cited data. Second sentence adds a second source. Connective inference ("suggesting...") is hedged and connects only two cited facts.

**Bad:**
> Rural hospitals are dangerously understaffed on cybersecurity. The situation is dire — most facilities have nobody dedicated to security, and the few who try to hire find it nearly impossible. This creates an existential vulnerability that threatens patient lives.

*Why it fails:* Leads with unsourced emotional framing ("dangerously," "dire"). "Most facilities" adds invented vagueness when 68% is available. "Existential vulnerability" is emotional escalation. "Threatens patient lives" is unsourced causal claim.

### Hedging
Required on all interpretive statements. Use qualifiers from the qualifier discipline table in SKILL.md.

### Prohibited Patterns
- Rhetorical questions ("But what happens when these hospitals get attacked?")
- Exclamatory statements ("This is a crisis!")
- Superlatives without source attribution ("the worst," "the most critical," "unprecedented")
- Emotional intensifiers outside direct quotes ("desperate," "catastrophic," "devastating")

### Heading Style
Descriptive and neutral. Headings state what the section contains, not what the reader should feel.

| Good | Bad |
|------|-----|
| Funding Landscape | The Money |
| Active Funding Sources | 12 Doors to Walk Through |
| Problem Statement | A Crisis Nobody Is Solving |
| Current Solutions | Why Everything Fails |
| Severity and Impact | The Human Toll |
| Regulatory Context | The Regulatory Hammer |

### Connective Logic
Maximum one connective inference per major section (## heading level). Each must use hedging language and be logged in processing-log.md.

---

## Persuasive Register (Phases 08-09, 13)

**Role:** Case builder. Tell a compelling story grounded in evidence.

### Voice
First-person plural permitted. Direct address permitted sparingly.

| Allowed | Context |
|---------|---------|
| We identified... | When describing the venture's research findings |
| Our research shows... | When presenting evidence the team gathered |
| This positions us to... | When describing strategic alignment |
| The evidence supports... | When making a claim backed by data |

### Sentence Structure
Story-first, data-supported. Narrative framing sentences are permitted. Every narrative paragraph must still contain at least one inline citation.

**Good:**
> Rural hospitals are under attack, and nobody is building for them. 68% have no dedicated cybersecurity leader (Black Book Research, June 2025), 73% lack adequate defenses (Black Book Research, June 2025), and the average recovery cost of $11M (AHA/Microsoft, March 2025) exceeds what most of these facilities can absorb. We identified this gap through systematic research across 41 independent sources.

*Why it works:* Leads with a strong narrative claim, immediately supports it with three cited statistics. First-person usage is appropriate for materials register.

**Bad:**
> Rural hospitals are completely defenseless against cyberattacks. Every single facility is on the verge of catastrophic failure, and it's only a matter of time before hundreds close their doors. We are the only solution.

*Why it fails:* "Completely defenseless" is invented specificity. "Every single facility" is false. "Catastrophic failure" is unsourced emotional language. "Only a matter of time" overstates certainty. "We are the only solution" is unsubstantiated.

### Hedging
Reduced but not eliminated. Strong claims must still use language proportional to the evidence.

| Allowed | Prohibited |
|---------|-----------|
| The evidence strongly supports... | The evidence proves... |
| This represents a significant opportunity... | This guarantees market dominance... |
| Data from 41 sources confirms the pattern... | There is zero doubt about... |

### Allowed Patterns
- Rhetorical questions (sparingly, max one per page)
- Contrast framing ("While enterprise vendors target large health systems, rural hospitals are left behind")
- Momentum language ("This positions the venture to...")
- Emotional language when anchored to evidence ("a crisis-level shortage (HSCC, May 2025)")

### Heading Style
Narrative and evocative headings are appropriate.

| Appropriate | Still Prohibited |
|------------|-----------------|
| The Opportunity | The Guaranteed Win |
| The Money | Infinite Funding |
| Why Now | Why We Will Dominate |
| The Ask | The Inevitable Outcome |

### Connective Logic
Multiple connective inferences allowed. Each must still use hedging language and be supported by at least one citation per connected fact.

---

## Technical Register (Phases 10-12)

**Role:** Technical writer. Specify precisely; do not market.

### Voice
Impersonal technical. System-focused.

| Allowed | Prohibited |
|---------|-----------|
| The system handles... | Our revolutionary platform... |
| The architecture supports... | The game-changing design... |
| This component processes... | This cutting-edge module... |
| The API exposes... | The industry-leading API... |

### Sentence Structure
Specification-first. State the capability or requirement, then rationale if needed.

**Good:**
> The data pipeline ingests SIEM logs via syslog (RFC 5424) and normalizes events into a common schema. Processing latency targets 500ms p95 for real-time alerting. This design supports the requirement for near-real-time threat detection identified in Phase 05.

**Bad:**
> Our revolutionary AI-powered pipeline processes data at lightning speed, delivering unmatched threat detection capabilities that will transform rural hospital cybersecurity forever.

### Hedging
Minimal for technical specifications. Required for market/adoption claims that appear in technical documents.

### Prohibited Patterns
- Marketing language ("revolutionary," "cutting-edge," "game-changing," "industry-leading")
- Unsubstantiated performance claims ("fastest," "most accurate," "best-in-class")
- Competitor disparagement ("unlike the inferior approaches of...")
- Vague capability claims ("handles any scale," "works with everything")

### Heading Style
Technical-descriptive.

| Good | Bad |
|------|-----|
| System Architecture | Our Revolutionary Architecture |
| Data Pipeline | The Lightning-Fast Engine |
| Security Model | Unbreakable Security |
| API Design | The Ultimate API |
