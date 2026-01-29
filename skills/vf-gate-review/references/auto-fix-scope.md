# Auto-Fix Scope

Defines exactly what the gate review skill can and cannot auto-fix. Auto-fixes are mechanical corrections where the correct value is deterministically knowable from existing files. They never involve judgment, interpretation, or strategic content.

## Source of Truth Hierarchy

When values conflict between files, the more structured source wins:

1. **YAML array data** (actual entries in the array)
2. **YAML header metadata** (summary fields like `total_funders_analyzed`)
3. **Thesis text** (narrative prose)
4. **sources.md summary counts** (footer tallies)

Example: If `funder-profiles.yaml` contains 38 entries but its header says `total_funders_analyzed: 35`, the array count (38) is correct.

## Auto-Fixable Categories

### 1. Count Mismatches

**Detection pattern:** Validation report says "YAML header says X, actual content is Y" or "Claimed: X, Actual: Y"

**Fix rule:** Update the header/summary field to match the actual count.

**Files affected:** YAML headers, thesis.md Evidence Summary section

**Example:** `funder-profiles.yaml` header says `viable_funders: 12` but 15 entries have `viable: true`. Fix: update header to `viable_funders: 15`. Also update thesis.md Evidence Summary if it cites the old number.

### 2. Missing Source Entries

**Detection pattern:** Validation report says "Source 'X' cited in thesis.md but not found in sources.md" with the source name and what it was cited for.

**Fix rule:** Add a new row to sources.md with:
- Organization name (from the inline citation)
- Document title (from the citing context or "cited source")
- Date (from the inline citation)
- URL (from the citing file if available, otherwise "—")
- Cited for (from the validation report detail)

**Files affected:** sources.md only

**Example:** Thesis cites "(Claroty/Check Point Research, 2025)" for medical device data. Add to sources.md: `| Claroty / Check Point Research | Medical Device Security Report | 2025 | — | 40%+ medical devices at end-of-life |`

### 3. Uncited Claims with Known Source

**Detection pattern:** Validation report says "Claim: [text]. Suggested source: [source]" in the Uncited Claims table.

**Fix rule:** Add inline citation `(Source Name, Date)` to the claim in thesis.md using the suggested source.

**Constraint:** Only fix if the suggested source exists in evidence.yaml or sources.md. If the validator could not identify a source, this is NOT auto-fixable.

**Files affected:** thesis.md only

**Example:** Claim "physical device lifecycles of 10-15 years" with suggested source "Claroty/Check Point Research, 2025". Fix: append `(Claroty/Check Point Research, 2025)` to the sentence.

### 4. Data Inconsistencies

**Detection pattern:** Validation report says "Thesis says X, YAML says Y" or identifies the same metric with different values in different locations.

**Fix rule:** Update the incorrect value to match the source of truth (per hierarchy above). YAML data is truth over thesis text.

**Files affected:** thesis.md (update to match YAML), or YAML header (update to match YAML array)

**Example:** Thesis says "50% operate at negative margins" in one paragraph but evidence.yaml records `46%`. Fix: change "50%" to "46%" in thesis.md.

### 5. Footer/Summary Count Mismatches

**Detection pattern:** Validation report says "Footer says N sources but M are listed" or similar count discrepancy in summary text.

**Fix rule:** Update the count to match the actual list length.

**Files affected:** sources.md footer, thesis.md Evidence Summary, any summary paragraph

## NOT Auto-Fixable

These require human judgment and must be left for the human gate review decision:

| Category | Why Not Fixable |
|----------|----------------|
| Adding/removing profiles or evidence entries | Changes the evidence base — strategic decision |
| Changing viability or confidence assessments | Analytical judgment about funder quality |
| Rewriting narrative sections | Changes thesis framing and interpretation |
| Resolving conflicting data between external sources | Requires judgment about which source to trust |
| Changing gate criteria assessments | Strategic judgment about readiness |
| Missing evidence where no source exists | Cannot fabricate citations |
| Ambiguous correct values | If the right answer is unclear, a human must decide |
| Writing governance violations (prohibited words, unhedged claims) | These are narrative quality issues requiring thoughtful rewording |
| Unknown timelines or confidence flags | These are data limitations, not errors |

## Logging Requirements

Every auto-fix must be logged with:
- File path
- What was changed (field name or line context)
- Old value
- New value
- Reason (which validation check triggered the fix)

The log is written to the gate review record for audit trail purposes.
