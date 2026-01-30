# Red Flags Detection Guide

Research-backed patterns that indicate strategic deficiency in funding domain outputs. Organized by severity and detection confidence.

## Fatal Flaws — Block on Detection

These patterns predict immediate rejection by experienced evaluators. Based on the elimination-by-aspects model (Maxwell et al., 2011): one fatal flaw triggers rejection before any strengths are assessed.

### F1: No Market Need Evidence
- **Pattern:** Solution described without evidence that customers have the problem or would pay to solve it
- **Detection:** TAM based on aspiration ("$50B market, we need 1%"); no customer validation; solution-first positioning; problem section is vague or generic
- **Prevalence:** 42% of startup failures (CB Insights)
- **Research:** CB Insights post-mortem analysis; NSF Senior Program Director: "If you haven't shown there is actually a customer who cares, that is a fatal flaw"

### F2: Dishonesty or Inconsistency in Metrics
- **Pattern:** Claims that contradict each other across documents, or metrics that cannot be verified
- **Detection:** Different statistics in deck vs. summary vs. data room; unverifiable assertions; exaggerated achievements; market numbers that don't add up
- **Prevalence:** Instant rejection per multiple VC sources
- **Research:** DocSend behavioral data; universal evaluator red flag

### F3: "No Competitors" Claim
- **Pattern:** Asserting no competition exists in the market
- **Detection:** Explicit statement "we have no competitors" or competition slide showing only the venture checks all boxes
- **Prevalence:** Systematically absent competition analysis in failed decks (DocSend/TechCrunch)
- **Research:** VCs hear "no market" or "founder hasn't done research." Competition scrutiny up 88% in 2023.

### F4: Administrative Non-Compliance (Grants)
- **Pattern:** Missing required documents, format violations, or eligibility failures
- **Detection:** Letters of Support included in NSF Phase I (causes automatic rejection); missing commercialization plan in DOE (automatic decline); PI employment requirements not met
- **Prevalence:** 5-10% of grant proposals; automatic rejection
- **Research:** SBIR.gov official guidance; DOE explicit requirement; NSF Phase I rules

### F5: Shopped Deal Signal
- **Pattern:** Evidence the venture has been widely pitched without success
- **Detection:** Fundraising extending beyond 6 months; evidence of 100+ investors contacted; form rejection language in status tracking
- **Prevalence:** First Round: "almost impossible to get a second fresh look"
- **Research:** First Round Capital (Kopelman): negative signaling from extensive prior outreach

## Serious Gaps — Flag for Human Review

These patterns indicate significant strategic weakness but may be overcome by exceptional strengths.

### S1: Spray-and-Pray Funder Strategy
- **Pattern:** Large undifferentiated funder list with no prioritization
- **Detection:** 100+ funders listed with equal weight; no stage/sector/geography filtering; identical approach to different funder types; no alignment rationale
- **Benchmark:** Strategic approach targets 20-40 aligned funders (Suster/Upfront Ventures)
- **Research:** DocSend: weak correlation between quantity contacted and funding raised

### S2: Missing Financials in Pitch Materials
- **Pattern:** No financial projections or unit economics in pitch deck
- **Detection:** Absence of financials slide; no assumptions or unit economics discussion
- **Benchmark:** 58% of successful decks include financials; 0% of failed decks do
- **Research:** DocSend/Harvard Business School pitch deck study

### S3: Business Model Buried
- **Pattern:** Business model appears late in pitch deck or is unclear
- **Detection:** Business model slide after position 6; revenue model unclear or vague
- **Benchmark:** Successful decks position business model 4th; unsuccessful position it 10th
- **Research:** DocSend structural analysis of successful vs. unsuccessful decks

### S4: Stage-Funder Mismatch
- **Pattern:** Targeting funders whose stage requirements the venture cannot meet
- **Detection:** Seeking seed from growth-stage VCs; seeking pre-seed with Series A metrics; pitching SaaS to healthcare-specific fund without healthcare angle; wrong check size
- **Research:** Gompers (2020): screening eliminates large percentage in minutes due to misalignment

### S5: Weak Commercialization Plan (Grants)
- **Pattern:** Generic market description without specific customer, competitive, or pricing data
- **Detection:** "Customers, competition, and market size not specifically delineated"; vague commercialization pathway; no Phase III transition partner identified
- **Research:** NIH/SBIR reviewer guidance: top-3 rejection reason

### S6: Over-Engineering at Pre-Product Stage
- **Pattern:** Excessive detail that signals planning over learning
- **Detection:** 40+ tab financial models; quarterly projections for years 3-5; detailed product roadmap beyond 18 months; complex cap table modeling; extensive legal documentation
- **Benchmark:** a16z: "we don't expect a fully-baked model." SVB: "slick, overly produced is a red flag." Highline Beta: "walk away" from deep financials at pre-seed.
- **Research:** a16z data room guidance (Moore, 2022); SVB published guidance

### S7: Vanity Traction
- **Pattern:** Traction claims that don't indicate real customer engagement
- **Detection:** "Strong interest from potential customers"; downloads without engagement; page views without conversions; "we've talked to 50 people who would buy" without specifics
- **Benchmark:** Genuine traction: LOIs with terms, waitlist with conversion, documented interviews with quotes, specific metrics
- **Research:** Mercury: LOIs, waitlist, first customers. YC Seibel: "bad traction is worse than no traction"

### S8: Company Too Old for Stage
- **Pattern:** Operating for years while still seeking early-stage funding
- **Detection:** Founded 3+ years ago; multiple pivots without commercialization; seeking pre-seed validation after extensive development
- **Research:** Incisive VC: "company too old for stage" is key red flag

## Minor Weaknesses — Note for Improvement

### M1: Suboptimal Slide Ordering
- **Detection:** Business model after slide 6; "Why Now?" after slide 8; team slide buried at end
- **Impact:** Reduces engagement but not fatal

### M2: Excessive Deck Length
- **Detection:** More than 15-20 slides for pre-seed/seed
- **Benchmark:** 11-20 slides are 43% more successful (DocSend)

### M3: Missing "Why Now?" Section
- **Detection:** No timing justification or buried late in materials
- **Benchmark:** 92% of successful decks include "Why Now?" (Papermark); 65% more VC time spent on this section in 2023

### M4: Marketing Buzzwords
- **Detection:** "Revolutionize," "disrupt," "synergy," "innovate," "groundbreaking," "world-class," "unique" — density >3 per page
- **Research:** YC explicitly warns against these terms. "Well-designed and easy to use" is not an insight.

### M5: Exit Strategy at Pre-Seed
- **Detection:** Detailed exit plan in early-stage materials
- **Research:** Signals lack of confidence or commitment at pre-product stage

## Detection Confidence Levels

| Confidence | Meaning | Action |
|-----------|---------|--------|
| HIGH | Pattern is unambiguous and reliably detectable from outputs | Flag automatically |
| MEDIUM | Pattern may have valid exceptions depending on context | Flag with caveat for human review |
| LOW | Pattern is suggestive but requires broader context to confirm | Note as observation |

| Red Flag | Confidence |
|----------|-----------|
| F1: No market need evidence | HIGH |
| F2: Metric inconsistency | HIGH |
| F3: "No competitors" | HIGH |
| F4: Grant non-compliance | HIGH |
| F5: Shopped deal | MEDIUM |
| S1: Spray-and-pray | HIGH |
| S2: Missing financials | HIGH |
| S3: Business model buried | MEDIUM |
| S4: Stage-funder mismatch | HIGH |
| S5: Weak commercialization | MEDIUM |
| S6: Over-engineering | MEDIUM |
| S7: Vanity traction | MEDIUM |
| S8: Company too old | MEDIUM |
| M1-M5: Minor patterns | HIGH |
