# Validation Test Cases: Problem Thesis

## Test Matrix

These test cases define expected validator behavior across normal, edge case, and out-of-scope scenarios. Use to verify the validate skill works correctly.

---

## Normal Operations (should produce PASS)

### TC-01: Complete valid output

**Setup:**
- `thesis.md` has all sections with content
- `evidence.yaml` has all categories meeting minimums, all with source/date fields
- `customer-voice.md` has 6 quotes across 3 themes, terminology and workarounds sections
- `processing-log.md` has all sections populated
- Cross-references consistent

**Expected result:** PASS — 27/27 checks passed

### TC-02: Minimum viable output

**Setup:**
- `thesis.md` has all sections, some minimal
- `evidence.yaml` has exactly: 3 prevalence, 3 severity, 2 cost, 1 solution, 1 gap
- `customer-voice.md` has exactly 5 quotes across 2 themes
- `processing-log.md` has all sections (some with "None found" noted)
- Cross-references consistent

**Expected result:** PASS — 27/27 checks passed

---

## Edge Cases (should produce specific failures or warnings)

### TC-03: One file missing

**Setup:**
- `thesis.md` exists
- `evidence.yaml` missing
- `customer-voice.md` exists
- `processing-log.md` exists

**Expected result:** FAIL
- Check #2 (evidence.yaml existence) → FAIL
- Checks #5-11 (evidence validation) → FAIL (cannot read file)
- Checks #22-23 (cross-validation on evidence) → FAIL
- All other checks still run and report normally
- Report shows: "Checks passed: X/27" (not "Validation aborted")

### TC-04: Customer voice below minimum

**Setup:**
- All files exist
- `customer-voice.md` has 3 quotes (need 5), 2 themes

**Expected result:** FAIL
- Check #12 (direct quotes 5+) → FAIL
- Failure detail: "Direct quotes with source attribution: Required 5+, Found 3"

### TC-05: Quote without source attribution

**Setup:**
- `customer-voice.md` has 6 quotes total
- 2 quotes have no source attribution

**Expected result:**
- Only 4 valid quotes counted → FAIL on check #12
- Invalid quotes listed in "Invalid Quotes" table
- Detail: "6 quotes found, 2 invalid (missing source), 4 valid. Required: 5+"

### TC-06: Statistic in thesis not in evidence.yaml

**Setup:**
- `thesis.md` cites "67% of rural hospitals lack cybersecurity staff"
- This statistic does not appear in `evidence.yaml`

**Expected result:** FAIL
- Check #23 (statistics match evidence.yaml) → FAIL
- Detail: "Untracked statistic in thesis: '67% of rural hospitals lack cybersecurity staff' — not found in evidence.yaml"

### TC-07: Evidence entry missing source field

**Setup:**
- `evidence.yaml` has 4 prevalence entries
- 1 entry has `stat` and `date` but no `source` field

**Expected result:**
- Only 3 valid entries counted
- Check #6 → PASS (3 meets minimum of 3)
- Invalid entry listed in "Invalid Evidence Entries" table
- If the invalid entry was the 3rd, dropping it to 2 valid → FAIL

### TC-08: Empty section in thesis

**Setup:**
- `thesis.md` has "## Customer Voice" heading but no content beneath it

**Expected result:** FAIL
- Check #18 (customer voice section with quote) → FAIL
- Detail: "Section 'Customer Voice' exists but contains no quotes"

### TC-09: Problem statement mismatch

**Setup:**
- `thesis.md` states: "Rural hospitals face critical cybersecurity gaps"
- `evidence.yaml` has `problem_statement: "Small hospitals lack IT security resources"`

**Expected result:** FAIL
- Check #22 (problem statement matches) → FAIL
- Detail: "Problem statement in thesis.md does not match evidence.yaml"

### TC-10: Theme heading with no quotes

**Setup:**
- `customer-voice.md` has 3 theme headings
- Theme 3 has the heading but no quotes beneath it

**Expected result:**
- Only 2 valid themes counted
- Check #13 → PASS (2 meets minimum of 2)
- Note: if this dropped count to 1 → FAIL

### TC-11: Processing log missing research file

**Setup:**
- `research/02-problem/` contains 5 files
- `processing-log.md` lists only 4 files in "Files Read"

**Expected result:** FAIL
- Check #25 → FAIL
- Detail: "Expected 5 research files, processing log lists 4. Missing: [filename]"

### TC-12: Capital alignment set to false

**Setup:**
- `evidence.yaml` has `capital_alignment.aligned: false`

**Expected result:** FAIL
- Check #11 → FAIL
- Detail: "capital_alignment.aligned is false — problem does not align with capital thesis"

---

## Out-of-Scope (should not trigger or should error gracefully)

### TC-13: Wrong phase files

**Setup:**
- Files exist at `{project}/phases/01-capital/` instead of `02-problem/`

**Expected result:** FAIL on all file existence checks (#1-4)
- Validator should not attempt to read capital thesis files as problem thesis

### TC-14: Corrupted YAML

**Setup:**
- `evidence.yaml` contains invalid YAML syntax

**Expected result:** FAIL
- Check #2 → PASS (file exists)
- Checks #5-11 → FAIL (cannot parse YAML)
- Error detail should note "YAML parse error" not crash

### TC-15: Empty files

**Setup:**
- All files exist but are 0 bytes

**Expected result:** FAIL on all file existence checks (non-empty requirement)
- All downstream checks also FAIL
- Report still completes with 27 checks reported
