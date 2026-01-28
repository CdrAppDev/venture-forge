#!/usr/bin/env python3
"""
Deterministic validation checks for Capital Thesis (Phase 01).

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

try:
    import yaml
except ImportError:
    # Fall back to basic YAML parsing if pyyaml not installed
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


def check_funders(data):
    """Validate funder profiles structure and requirements."""
    results = []

    funders = data.get("funders", []) if data else []
    funder_count = len(funders)

    results.append({
        "check": "Total funders analyzed (2+)",
        "status": "PASS" if funder_count >= 2 else "FAIL",
        "detail": f"Found: {funder_count}",
    })

    viable_count = sum(1 for f in funders if f.get("viable") is True)
    results.append({
        "check": "Viable funders (2+)",
        "status": "PASS" if viable_count >= 2 else "FAIL",
        "detail": f"Found: {viable_count}",
    })

    # Check required fields on each funder
    field_issues = []
    for f in funders:
        name = f.get("name", "<unnamed>")
        required = {
            "name": f.get("name"),
            "type": f.get("type"),
            "viable": f.get("viable"),
            "viability_rationale": f.get("viability_rationale"),
        }
        funding = f.get("funding", {})
        required["funding.amount_range"] = funding.get("amount_range")
        required["funding.source"] = funding.get("source")

        criteria = f.get("criteria", {})
        stated = criteria.get("stated", [])
        cited = [c for c in stated if c.get("source")]
        if not cited:
            field_issues.append(f"{name}: no cited stated criteria")

        alignment = f.get("alignment", {})
        if not alignment.get("strengths"):
            field_issues.append(f"{name}: no alignment strengths")
        if "gaps" not in alignment:
            field_issues.append(f"{name}: alignment.gaps missing")
        if not alignment.get("overall_fit"):
            field_issues.append(f"{name}: alignment.overall_fit missing")

        for key, val in required.items():
            if val is None or val == "":
                field_issues.append(f"{name}: {key} missing or empty")

    results.append({
        "check": "All funders have required fields",
        "status": "PASS" if not field_issues else "FAIL",
        "detail": "; ".join(field_issues) if field_issues else "All fields present",
    })

    # Timeline confidence check
    timeline_flags = []
    for f in funders:
        if f.get("viable") is True:
            process = f.get("process", {})
            confidence = process.get("timeline_confidence", "unknown")
            if confidence == "unknown":
                timeline_flags.append(f.get("name", "<unnamed>"))

    results.append({
        "check": "No unknown timelines on viable funders",
        "status": "WARN" if timeline_flags else "PASS",
        "detail": f"Unknown timeline: {', '.join(timeline_flags)}" if timeline_flags else "All viable funders have timeline data",
    })

    # Low confidence viable check
    low_conf_viable = []
    for f in funders:
        if f.get("viable") is True and f.get("confidence") == "low":
            low_conf_viable.append(f.get("name", "<unnamed>"))

    results.append({
        "check": "No low-confidence viable without justification",
        "status": "PASS" if not low_conf_viable else "FAIL",
        "detail": f"Low-confidence viable: {', '.join(low_conf_viable)}" if low_conf_viable else "No issues",
    })

    # Empty viability rationale check
    empty_rationale = [f.get("name", "<unnamed>") for f in funders if not f.get("viability_rationale")]
    results.append({
        "check": "All viability rationales non-empty",
        "status": "PASS" if not empty_rationale else "FAIL",
        "detail": f"Empty rationale: {', '.join(empty_rationale)}" if empty_rationale else "All rationales present",
    })

    return results


def check_citations(data):
    """Count citations across funder profiles."""
    results = []
    funders = data.get("funders", []) if data else []

    # Count unique sources across all funders for landscape
    all_sources = set()
    criteria_count = 0
    portfolio_count = 0
    process_count = 0

    for f in funders:
        funding = f.get("funding", {})
        if funding.get("source"):
            all_sources.add(funding["source"])

        criteria = f.get("criteria", {})
        for c in criteria.get("stated", []):
            if c.get("source"):
                criteria_count += 1
                all_sources.add(c["source"])

        for p in f.get("portfolio", []):
            if p.get("source"):
                portfolio_count += 1

        process = f.get("process", {})
        if process.get("timeline_source"):
            process_count += 1
        for dm in process.get("decision_makers", []):
            if dm.get("source"):
                process_count += 1

    minimums = [
        ("Landscape citations", 3, len(all_sources)),
        ("Thesis/criteria citations", 2, criteria_count),
        ("Portfolio citations", 3, portfolio_count),
        ("Requirements citations", 2, process_count),
    ]

    for name, required, found in minimums:
        results.append({
            "check": f"{name} ({required}+)",
            "status": "PASS" if found >= required else "FAIL",
            "detail": f"Found: {found}",
        })

    return results


def check_thesis_sections(path):
    """Check thesis.md has required sections with content."""
    results = []
    required_sections = [
        "Executive Summary",
        "Funding Landscape",
        "Active Funding Sources",
        "Funder Deep Dives",
        "Alignment Strategy",
        "Funding Timeline",
        "Evidence Summary",
        "Gate Criteria Checklist",
    ]

    if not os.path.isfile(path):
        for section in required_sections:
            results.append({
                "check": f"Thesis section: {section}",
                "status": "FAIL",
                "detail": "thesis.md not found",
            })
        return results

    with open(path, "r") as f:
        content = f.read()

    for section in required_sections:
        # Check for heading (## or ###)
        found = False
        has_content = False
        for variant in [f"## {section}", f"### {section}"]:
            idx = content.lower().find(variant.lower())
            if idx >= 0:
                found = True
                # Check for content after heading
                after = content[idx + len(variant):]
                next_heading = after.find("\n#")
                section_content = after[:next_heading] if next_heading > 0 else after
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
        for check_name in ["Research files listed", "Excluded evidence documented", "Conflicts documented"]:
            results.append({"check": check_name, "status": "FAIL", "detail": "processing-log.md not found"})
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
    phase_dir = os.path.join(project, "phases", "01-capital")

    thesis_path = os.path.join(phase_dir, "thesis.md")
    yaml_path = os.path.join(phase_dir, "funder-profiles.yaml")
    log_path = os.path.join(phase_dir, "processing-log.md")

    all_results = []

    # 1. File existence (3 checks)
    all_results.append(check_file_exists(thesis_path, "thesis.md"))
    all_results.append(check_file_exists(yaml_path, "funder-profiles.yaml"))
    all_results.append(check_file_exists(log_path, "processing-log.md"))

    # 2. Funder profile validation (6 checks)
    yaml_data, yaml_error = parse_yaml_file(yaml_path)
    if yaml_error:
        for i in range(6):
            all_results.append({
                "check": f"Funder profile check {i+1}",
                "status": "FAIL",
                "detail": f"Cannot validate: {yaml_error}",
            })
    else:
        all_results.extend(check_funders(yaml_data))

    # 3. Evidence/citation validation (4 checks)
    if yaml_error:
        for name in ["Landscape", "Criteria", "Portfolio", "Requirements"]:
            all_results.append({
                "check": f"{name} citations",
                "status": "FAIL",
                "detail": f"Cannot count: {yaml_error}",
            })
    else:
        all_results.extend(check_citations(yaml_data))

    # 4. Thesis section validation (8 checks)
    all_results.extend(check_thesis_sections(thesis_path))

    # 5-6. Cross-validation and timeline (7 checks) — semantic, handled by LLM
    # Script outputs placeholder for these
    for check_name in [
        "Funder names consistent across files",
        "Viability assessments consistent",
        "Citation counts match actual",
        "Alignment gaps consistent",
        "Each viable funder has timeline info",
        "Timeline table has all viable funders",
        "Unknown timelines noted in thesis",
    ]:
        all_results.append({
            "check": check_name,
            "status": "SEMANTIC",
            "detail": "Requires LLM judgment — check manually",
        })

    # 7. Processing log validation (3 checks)
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
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
