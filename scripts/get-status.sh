#!/bin/bash

# Venture Forge Portfolio Status

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " VENTURE FORGE PORTFOLIO STATUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if gh CLI is available
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) not installed. Install with: brew install gh"
    exit 1
fi

# Check if we have a remote
if ! git remote -v 2>/dev/null | grep -q origin; then
    echo "No GitHub remote configured yet."
    echo ""
    echo "Portfolio tracking will be available after running:"
    echo "  gh repo create venture-forge --private"
    echo "  git push -u origin main"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo " LOCAL PORTFOLIO (from filesystem)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    # Check for linked projects in portfolio/
    if [ -d "portfolio" ]; then
        for project in portfolio/*; do
            if [ -L "$project" ]; then
                name=$(basename "$project")
                target=$(readlink "$project")
                echo "  • $name → $target"
            fi
        done
    else
        echo "  No opportunities linked yet."
    fi
    exit 0
fi

echo "Active Opportunities:"
echo ""

# Query GitHub for opportunities
gh issue list --label "opportunity" --json number,title,labels --jq '.[] | "  #\(.number) \(.title) [\(.labels | map(.name) | join(", "))]"'

if [ $? -ne 0 ]; then
    echo "  Unable to query GitHub. Check authentication with: gh auth status"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Commands:"
echo "  status              - This status view"
echo "  scout [source]      - Add new capital source"
echo "  research [area]     - Start new opportunity"
echo "  continue [name]     - Work on next phase"
echo ""
