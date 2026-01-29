# Validation Test Cases: Capital Thesis

## Test Matrix

These test cases define expected validator behavior across normal, edge case, and out-of-scope scenarios. Use to verify the validate skill works correctly.

---

## Normal Operations (should produce PASS)

### TC-01: Complete valid output

**Setup:**
- `thesis.md` has all sections with content
- `funder-profiles.yaml` has 3 funders, 2 viable
- `sources.md` lists all unique sources by category
- `processing-log.md` has all sections populated
- All citation minimums met
- Cross-references consistent

**Expected result:** PASS — 36/36 checks passed

### TC-02: Minimum viable output

**Setup:**
- `thesis.md` has all sections, some minimal
- `funder-profiles.yaml` has exactly 2 funders, both viable
- `sources.md` lists all sources with org, document, date, cited-for
- `processing-log.md` has all sections (some empty with "None" noted)
- Citation minimums met at exactly the minimum (3, 2, 3, 2)
- Cross-references consistent

**Expected result:** PASS — 36/36 checks passed

---

## Edge Cases (should produce specific failures or warnings)

### TC-03: One file missing

**Setup:**
- `thesis.md` exists
- `funder-profiles.yaml` missing
- `processing-log.md` exists

**Expected result:** FAIL
- Check #2 (funder-profiles.yaml existence) → FAIL
- Checks #4-9 (funder profile checks) → FAIL (cannot read file)
- Checks #10-13 (evidence checks) → FAIL (cannot count citations)
- Checks #22-25 (cross-validation) → FAIL (cannot compare)
- All other checks still run and report normally
- Report shows: "Checks passed: X/31" (not "Validation aborted")

### TC-04: Only one viable funder

**Setup:**
- All files exist
- `funder-profiles.yaml` has 3 funders, only 1 viable
- Everything else valid

**Expected result:** FAIL
- Check #5 (viable funders 2+) → FAIL
- All other checks still run
- Failure detail: "Required: 2+ viable funders. Found: 1"

### TC-05: Citation minimums not met

**Setup:**
- All files exist, valid structure
- Landscape citations: 2 (need 3)
- All other minimums met

**Expected result:** FAIL
- Check #10 (landscape citations) → FAIL
- Failure detail: "Landscape citations: Required 3+, Found 2"

### TC-06: Funder in YAML but not in thesis

**Setup:**
- `funder-profiles.yaml` has funders: RHTP, SCRA, CISA
- `thesis.md` deep dives cover only RHTP and SCRA (CISA missing)

**Expected result:** FAIL
- Check #22 (funder names consistent) → FAIL
- Detail: "CISA appears in funder-profiles.yaml but not in thesis.md"

### TC-07: Empty section headings in thesis

**Setup:**
- `thesis.md` has "## Alignment Strategy" heading but no content beneath it

**Expected result:** FAIL
- Check #18 (alignment strategy) → FAIL
- Detail: "Section 'Alignment Strategy' exists but has no content"

### TC-08: Viable funder with unknown timeline

**Setup:**
- Funder has `viable: true` and `process.timeline_confidence: unknown`
- No mention of unknown timeline in thesis

**Expected result:** WARNING + FAIL
- Check #7 → WARNING (unknown timeline on viable funder)
- Check #28 → FAIL (unknown timeline not noted in thesis)

### TC-09: Citation without source field

**Setup:**
- A portfolio entry has `company` and `amount` but no `source`

**Expected result:** FAIL
- That entry does NOT count toward portfolio citation minimum
- Check #12 may fail if remaining entries fall below 3

### TC-10: Processing log missing excluded evidence section

**Setup:**
- `processing-log.md` exists
- Has "Files Read" and "Evidence Included" sections
- Missing "Evidence Excluded" section

**Expected result:** FAIL
- Check #30 → FAIL
- Detail: "Evidence Excluded section not present in processing log"

### TC-11: Viable funder with low confidence and no justification

**Setup:**
- Funder has `viable: true`, `confidence: low`
- No additional justification explaining why viable despite low confidence

**Expected result:** FAIL
- Check #8 → FAIL
- Detail: "Funder [Name] marked viable with low confidence but no justification"

### TC-11b: Low inline citation coverage

**Setup:**
- All files exist and valid
- `thesis.md` contains 40 factual claims
- Only 20 have inline `(Source Name, Date)` citations (50% coverage)

**Expected result:** FAIL
- Inline citation density check → FAIL
- Detail: "Inline citation coverage: 50% (20 of 40 factual claims cited). Required: 80%+"
- Uncited claims listed in validation report

### TC-11c: Borderline inline citation coverage

**Setup:**
- All files exist and valid
- `thesis.md` contains 40 factual claims
- 36 have inline citations (90% coverage)

**Expected result:** WARNING
- Inline citation density check → WARNING
- Detail: "Inline citation coverage: 90% (36 of 40 factual claims cited). 4 uncited claims listed below."

---

## Out-of-Scope (should not trigger or should error gracefully)

### TC-12: Wrong phase files

**Setup:**
- Files exist at `{project}/phases/02-problem/` instead of `01-capital/`

**Expected result:** FAIL on all file existence checks (#1-3)
- Validator should not attempt to read problem thesis files as capital thesis

### TC-13: Corrupted YAML

**Setup:**
- `funder-profiles.yaml` contains invalid YAML syntax

**Expected result:** FAIL
- Check #2 → PASS (file exists)
- Checks #4-9 → FAIL (cannot parse YAML)
- Error detail should note "YAML parse error" not crash

### TC-14: Empty files

**Setup:**
- All files exist but are 0 bytes

**Expected result:** FAIL on all file existence checks (non-empty requirement)
- All downstream checks also FAIL
- Report still completes with 36 checks reported

### TC-15: Missing sources.md

**Setup:**
- `thesis.md`, `funder-profiles.yaml`, `processing-log.md` all valid
- `sources.md` does not exist

**Expected result:** FAIL
- Check #4 (sources.md existence) → FAIL
- Checks #32-34 (sources validation) → FAIL (cannot read file)
- All other checks still run

### TC-16: Source in thesis not in sources.md

**Setup:**
- `thesis.md` cites "CMS RHT Program Overview (Dec 2025)"
- `sources.md` exists but does not list CMS as a source

**Expected result:** FAIL
- Check #32 (all sources listed) → FAIL
- Detail: "Source 'CMS' cited in thesis.md but not found in sources.md"

### TC-17: Malformed URL in sources.md

**Setup:**
- `sources.md` has a source with URL field containing "TBD" or "http://"

**Expected result:** FAIL
- Check #35 (URLs formatted correctly) → FAIL
- Detail: "Malformed URL for source [Name]: 'TBD'"
