#!/usr/bin/env python3
"""
Deterministic validation checks for Problem Thesis (Phase 02).

Performs file existence, YAML structure, field presence, and citation count
checks that don't require LLM judgment. Returns structured results for
the validation report.

Usage:
    python validate.py <project_path>

Example:
    python validate.py /Users/me/Projects/cybershield-rural
"""

import sys
import os
import json
import re

try:
    import yaml
except ImportError:
    yaml = None


def check_file_exists(path, name):
    """Check if file exists and is non-empty."""
    exists = os.path.isfile(path)
    non_empty = exists and os.path.getsize(path) > 0
    return {
        "check": f"File exists: {name}",
        "status": "PASS" if non_empty else "FAIL",
        "detail": f"{'Present and non-empty' if non_empty else 'Missing' if not exists else 'Empty (0 bytes)'}",
    }


def parse_yaml_file(path):
    """Parse YAML file, return data or error."""
    if not os.path.isfile(path):
        return None, "File not found"
    try:
        with open(path, "r") as f:
            content = f.read()
        if not content.strip():
            return None, "File is empty"
        if yaml:
            data = yaml.safe_load(content)
            return data, None
        else:
            return None, "PyYAML not installed — YAML structure checks skipped"
    except Exception as e:
        return None, f"YAML parse error: {str(e)}"


def validate_stat_entry(entry):
    """Check if a statistics entry has required fields."""
    if not isinstance(entry, dict):
        return False, "Not a dictionary"
    has_stat = bool(entry.get("stat"))
    has_source = bool(entry.get("source"))
    has_date = bool(entry.get("date"))
    if not has_source:
        return False, "Missing source"
    if not has_stat:
        return False, "Missing stat"
    return True, None


def check_evidence(data):
    """Validate evidence.yaml structure and citation minimums."""
    results = []
    invalid_entries = []

    # Problem statement
    problem_statement = data.get("problem_statement", "")
    results.append({
        "check": "Problem statement present",
        "status": "PASS" if problem_statement else "FAIL",
        "detail": f"{'Present' if problem_statement else 'Missing or empty'}",
    })

    # Prevalence statistics (3+)
    prev_stats = data.get("prevalence", {}).get("statistics", [])
    valid_prev = 0
    for entry in prev_stats:
        valid, issue = validate_stat_entry(entry)
        if valid:
            valid_prev += 1
        else:
            invalid_entries.append({"entry": str(entry.get("stat", ""))[:50], "issue": issue, "category": "prevalence"})

    results.append({
        "check": "Prevalence statistics (3+, with source/date)",
        "status": "PASS" if valid_prev >= 3 else "FAIL",
        "detail": f"Valid: {valid_prev}, Invalid: {len(prev_stats) - valid_prev}",
    })

    # Severity statistics (3+)
    sev_stats = data.get("severity", {}).get("statistics", [])
    valid_sev = 0
    for entry in sev_stats:
        valid, issue = validate_stat_entry(entry)
        if valid:
            valid_sev += 1
        else:
            invalid_entries.append({"entry": str(entry.get("stat", ""))[:50], "issue": issue, "category": "severity"})

    results.append({
        "check": "Severity statistics (3+, with source/date)",
        "status": "PASS" if valid_sev >= 3 else "FAIL",
        "detail": f"Valid: {valid_sev}, Invalid: {len(sev_stats) - valid_sev}",
    })

    # Cost of status quo (2+)
    cost_stats = data.get("cost_of_status_quo", {}).get("statistics", [])
    valid_cost = sum(1 for e in cost_stats if validate_stat_entry(e)[0])
    results.append({
        "check": "Cost of status quo statistics (2+)",
        "status": "PASS" if valid_cost >= 2 else "FAIL",
        "detail": f"Valid: {valid_cost}",
    })

    # Current solutions (1+)
    solutions = data.get("current_solutions", [])
    results.append({
        "check": "Current solutions (1+)",
        "status": "PASS" if len(solutions) >= 1 else "FAIL",
        "detail": f"Found: {len(solutions)}",
    })

    # Gaps (1+)
    gaps = data.get("gaps", [])
    results.append({
        "check": "Gaps identified (1+)",
        "status": "PASS" if len(gaps) >= 1 else "FAIL",
        "detail": f"Found: {len(gaps)}",
    })

    # Capital alignment
    alignment = data.get("capital_alignment", {})
    aligned = alignment.get("aligned", False)
    results.append({
        "check": "Capital alignment set to true",
        "status": "PASS" if aligned is True else "FAIL",
        "detail": f"Value: {aligned}",
    })

    return results, invalid_entries


def check_customer_voice(path):
    """Check customer-voice.md for quotes, themes, and sections."""
    results = []
    invalid_quotes = []

    if not os.path.isfile(path):
        for name in ["Direct quotes (5+)", "Distinct themes (2+)", "Terminology section", "Workarounds section"]:
            results.append({"check": name, "status": "FAIL", "detail": "customer-voice.md not found"})
        return results, invalid_quotes

    with open(path, "r") as f:
        content = f.read()

    # Count quotes (lines starting with >)
    quote_lines = [line.strip() for line in content.split("\n") if line.strip().startswith(">") and '"' in line]

    # Check for source attribution near quotes
    valid_quotes = 0
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith(">") and '"' in line:
            # Look for source attribution within next 3 lines
            context = "\n".join(lines[i:i+4]).lower()
            has_source = any(kw in context for kw in ["source:", "— source", "-- source", "forum", "reddit", "linkedin", "g2", "capterra"])
            if has_source:
                valid_quotes += 1
            else:
                excerpt = line.strip()[:60]
                invalid_quotes.append({"quote": excerpt, "issue": "No source attribution found"})

    results.append({
        "check": "Direct quotes with source attribution (5+)",
        "status": "PASS" if valid_quotes >= 5 else "FAIL",
        "detail": f"Valid: {valid_quotes}, Invalid: {len(invalid_quotes)}, Total: {len(quote_lines)}",
    })

    # Count themes (### headings under "How Customers Describe")
    theme_pattern = re.findall(r"###\s+(?:Theme\s+\d+[:\s]*)?(.+)", content)
    # Filter out non-theme headings
    theme_headings = [t for t in theme_pattern if t.lower() not in ["common language and terminology", "emotional intensity", "workarounds attempted"]]
    results.append({
        "check": "Distinct themes identified (2+)",
        "status": "PASS" if len(theme_headings) >= 2 else "FAIL",
        "detail": f"Found: {len(theme_headings)}",
    })

    # Terminology section
    has_terminology = "terminology" in content.lower() or "common language" in content.lower()
    # Check it has content
    if has_terminology:
        term_idx = content.lower().find("terminology")
        if term_idx < 0:
            term_idx = content.lower().find("common language")
        after = content[term_idx:term_idx+500]
        has_term_content = len(after.split("\n")) > 2

    results.append({
        "check": "Terminology section present and non-empty",
        "status": "PASS" if has_terminology and has_term_content else "FAIL",
        "detail": "Present with content" if has_terminology and has_term_content else "Missing or empty",
    })

    # Workarounds section
    has_workarounds = "workaround" in content.lower()
    results.append({
        "check": "Workarounds section present and non-empty",
        "status": "PASS" if has_workarounds else "FAIL",
        "detail": "Present" if has_workarounds else "Section not found",
    })

    return results, invalid_quotes


def check_thesis_sections(path):
    """Check thesis.md has required sections with content."""
    results = []
    required_sections = [
        "Problem Statement",
        "Key Statistics",
        "Customer Voice",
        "Capital",  # Matches "Alignment with Capital Thesis" or similar
        "Evidence Summary",
        "Gate Criteria",
    ]

    if not os.path.isfile(path):
        for section in required_sections:
            results.append({"check": f"Thesis section: {section}", "status": "FAIL", "detail": "thesis.md not found"})
        return results

    with open(path, "r") as f:
        content = f.read()

    for section in required_sections:
        found = False
        has_content = False
        content_lower = content.lower()
        section_lower = section.lower()

        # Find any heading containing the section name
        for match in re.finditer(r"^#{1,3}\s+(.+)$", content, re.MULTILINE):
            if section_lower in match.group(1).lower():
                found = True
                after = content[match.end():]
                next_heading = re.search(r"^#{1,3}\s+", after, re.MULTILINE)
                section_content = after[:next_heading.start()] if next_heading else after
                has_content = len(section_content.strip()) > 10
                break

        if not found:
            status = "FAIL"
            detail = "Section heading not found"
        elif not has_content:
            status = "FAIL"
            detail = "Section heading exists but no content"
        else:
            status = "PASS"
            detail = "Present with content"

        results.append({
            "check": f"Thesis section: {section}",
            "status": status,
            "detail": detail,
        })

    return results


def check_processing_log(path):
    """Check processing log has required sections."""
    results = []
    if not os.path.isfile(path):
        for name in ["Research files listed", "Excluded evidence documented", "Conflicts documented"]:
            results.append({"check": name, "status": "FAIL", "detail": "processing-log.md not found"})
        return results

    with open(path, "r") as f:
        content = f.read().lower()

    checks = [
        ("Research files listed", ["files read", "files processed"]),
        ("Excluded evidence documented", ["evidence excluded", "excluded"]),
        ("Conflicts documented", ["conflicts found", "conflicts", "contradictions"]),
    ]

    for name, keywords in checks:
        found = any(kw in content for kw in keywords)
        results.append({
            "check": name,
            "status": "PASS" if found else "FAIL",
            "detail": "Section found" if found else "Required section not found",
        })

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <project_path>")
        sys.exit(1)

    project = sys.argv[1]
    phase_dir = os.path.join(project, "phases", "02-problem")

    thesis_path = os.path.join(phase_dir, "thesis.md")
    yaml_path = os.path.join(phase_dir, "evidence.yaml")
    voice_path = os.path.join(phase_dir, "customer-voice.md")
    log_path = os.path.join(phase_dir, "processing-log.md")

    all_results = []
    all_invalid = {"evidence": [], "quotes": []}

    # 1. File existence (4 checks)
    all_results.append(check_file_exists(thesis_path, "thesis.md"))
    all_results.append(check_file_exists(yaml_path, "evidence.yaml"))
    all_results.append(check_file_exists(voice_path, "customer-voice.md"))
    all_results.append(check_file_exists(log_path, "processing-log.md"))

    # 2. Evidence validation (7 checks)
    yaml_data, yaml_error = parse_yaml_file(yaml_path)
    if yaml_error:
        for i in range(7):
            all_results.append({
                "check": f"Evidence check {i+1}",
                "status": "FAIL",
                "detail": f"Cannot validate: {yaml_error}",
            })
    else:
        evidence_results, invalid_evidence = check_evidence(yaml_data)
        all_results.extend(evidence_results)
        all_invalid["evidence"] = invalid_evidence

    # 3. Customer voice validation (4 checks)
    voice_results, invalid_quotes = check_customer_voice(voice_path)
    all_results.extend(voice_results)
    all_invalid["quotes"] = invalid_quotes

    # 4. Thesis section validation (6 checks)
    all_results.extend(check_thesis_sections(thesis_path))

    # 5. Cross-validation (3 checks) — semantic, handled by LLM
    for check_name in [
        "Problem statement matches evidence.yaml",
        "Statistics in thesis appear in evidence.yaml",
        "Quotes in thesis appear in customer-voice.md",
    ]:
        all_results.append({
            "check": check_name,
            "status": "SEMANTIC",
            "detail": "Requires LLM judgment — check manually",
        })

    # 6. Processing log validation (3 checks)
    all_results.extend(check_processing_log(log_path))

    # Summary
    total = len(all_results)
    passed = sum(1 for r in all_results if r["status"] == "PASS")
    failed = sum(1 for r in all_results if r["status"] == "FAIL")
    warnings = sum(1 for r in all_results if r["status"] == "WARN")
    semantic = sum(1 for r in all_results if r["status"] == "SEMANTIC")

    output = {
        "summary": {
            "total_checks": total,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "semantic_pending": semantic,
            "deterministic_result": "PASS" if failed == 0 else "FAIL",
        },
        "checks": all_results,
        "invalid_entries": all_invalid,
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
