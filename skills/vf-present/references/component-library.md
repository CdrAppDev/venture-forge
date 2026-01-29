# Component Library

HTML patterns for every reusable component in the Venture Forge presentation system. Use these patterns exactly as documented, substituting project-specific content where indicated by `{placeholders}`.

All components use CSS classes defined in `design-system.md`. Do not add custom styles — use the existing design system.

---

## 1. Navigation Bar

Fixed glassmorphism nav with logo and section links.

```html
<nav>
  <a href="#" class="nav-logo">{Project Name}</a>
  <ul class="nav-links">
    <li><a href="#{section-id}">{Link Label}</a></li>
    <!-- Repeat for each nav_link from phase-sections.yaml -->
  </ul>
</nav>
```

**Notes:**
- Links come from `nav_links` in phase-sections.yaml
- Nav hides at 768px (responsive rule in design system)

---

## 2. Hero Section

Full-width centered hero with gradient title, lead text, funnel visualization, and stat cards.

```html
<section class="hero">
  <div class="container">
    <h1>{Project Name}<br><span class="gradient-text">{Phase Name}</span></h1>
    <p class="lead">{Lead stat line — one sentence summarizing key numbers}</p>

    <div class="funnel">
      <div class="funnel-box">{Step 1}</div>
      <span class="funnel-arrow">&rarr;</span>
      <div class="funnel-box">{Step 2}</div>
      <span class="funnel-arrow">&rarr;</span>
      <div class="funnel-box">{Step 3}</div>
      <span class="funnel-arrow">&rarr;</span>
      <div class="funnel-box highlight">{Key Step}</div>
      <span class="funnel-arrow">&rarr;</span>
      <div class="funnel-box highlight">{Outcome}</div>
    </div>

    <div class="hero-stats">
      <div>
        <div class="hero-stat-value accent">{Value}</div>
        <div class="hero-stat-label">{Label}</div>
      </div>
      <div>
        <div class="hero-stat-value accent">{Value}</div>
        <div class="hero-stat-label">{Label}</div>
      </div>
      <div>
        <div class="hero-stat-value green">{Value}</div>
        <div class="hero-stat-label">{Label}</div>
      </div>
    </div>
  </div>
</section>
```

**Notes:**
- Use `accent` class for purple stat values, `green` for success metrics
- `highlight` class on funnel boxes for key steps (accent glow)
- Funnel steps should tell the research-to-outcome story
- 3 hero stats is standard; extract from thesis.md

---

## 3. Narrative Section

Long-form story in chapters with dividers and source links. Placed between hero and numbered sections.

```html
<section class="narrative" id="story">
  <div class="container">

    <div class="narrative-chapter">
      <div class="narrative-num">{Chapter Title}</div>
      <h3>{Headline claim}</h3>
      <p>{Paragraph with <strong>bold key stats</strong> and
        <a href="{url}" target="_blank">{Source Name}</a> inline citations.}</p>
    </div>

    <div class="narrative-divider"></div>

    <div class="narrative-chapter">
      <div class="narrative-num">{Chapter Title}</div>
      <h3>{Headline claim}</h3>
      <p>{Paragraph text...}</p>
    </div>

    <!-- Repeat chapters with dividers between them -->

    <!-- Optional CTA box at end -->
    <div class="narrative-cta">
      <strong>{Emphasis text}</strong> {Call to action or summary text.}
    </div>

  </div>
</section>
```

**Notes:**
- Container is narrower (720px) for readability
- Every factual claim should link to its third-party source
- Links use subtle purple underline style (defined in design system)
- Dividers appear between chapters, not after the last one
- Standard chapters for Phase 01: The Opportunity, The Money, The Path, The Ask

---

## 4. Section Header

Standard header for numbered content sections.

```html
<div class="section-num">{NN} / {Section Title}</div>
<h2>{Headline}</h2>
<p class="section-lead">{1-2 sentence description}</p>
```

**Notes:**
- `section-num` format: two-digit number + " / " + title (e.g., "01 / Executive Summary")
- Numbers are sequential starting from 01
- `section-lead` is optional but recommended

---

## 5. Card Grid (3-column)

Three equal-width cards in a row.

```html
<div class="card-grid cols-3">
  <div class="card">
    <div class="card-label {color}">{Label}</div>
    <h3>{Card Title}</h3>
    <p>{Card description text}</p>
  </div>
  <div class="card">
    <div class="card-label {color}">{Label}</div>
    <h3>{Card Title}</h3>
    <p>{Card description text}</p>
  </div>
  <div class="card">
    <div class="card-label {color}">{Label}</div>
    <h3>{Card Title}</h3>
    <p>{Card description text}</p>
  </div>
</div>
```

**Card label colors:** `purple`, `green`, `amber`, `red`, `cyan`

---

## 6. Card Grid (2-column)

Two equal-width cards in a row.

```html
<div class="card-grid cols-2">
  <div class="card">
    <div class="card-label {color}">{Label}</div>
    <h3>{Card Title}</h3>
    <p>{Card description text}</p>
  </div>
  <div class="card">
    <div class="card-label {color}">{Label}</div>
    <h3>{Card Title}</h3>
    <p>{Card description text}</p>
  </div>
</div>
```

---

## 7. Callout Box

Dashed-border attention box for critical constraints or important notes.

```html
<div class="callout">
  <strong>{Bold label}</strong> {Description text explaining the constraint or note.}
</div>
```

**Notes:**
- Amber dashed border by default
- Use for critical constraints, timing warnings, key caveats
- `<strong>` renders in amber color

---

## 8. Scale Note

Purple-accent info box for gap findings, notes, or context.

```html
<div class="scale-note">
  <strong>{Bold label}</strong> {Description text.}
</div>
```

**Notes:**
- Purple accent border and background
- Use for gap findings, supplementary info, and non-critical notes
- `<strong>` renders in accent-light color

---

## 9. Stat Row

Horizontal row of stat cards with large numbers.

```html
<div class="stat-row">
  <div class="stat-card">
    <div class="stat-card-value" style="color: var(--accent-light);">{Value}</div>
    <div class="stat-card-label">{Description}</div>
  </div>
  <div class="stat-card">
    <div class="stat-card-value" style="color: var(--red);">{Value}</div>
    <div class="stat-card-label">{Description}</div>
  </div>
  <div class="stat-card">
    <div class="stat-card-value" style="color: var(--amber);">{Value}</div>
    <div class="stat-card-label">{Description}</div>
  </div>
</div>
```

**Notes:**
- Use inline `style` for value colors: `--accent-light` (purple), `--green`, `--amber`, `--red`, `--cyan`
- Flex layout, wraps on small screens
- Typically used above a card grid in landscape/evidence sections

---

## 10. Data Table with Filter Tabs

Filterable table with category tabs.

```html
<div class="filter-tabs">
  <button class="tab-btn active" data-filter="all">All ({count})</button>
  <button class="tab-btn" data-filter="{category}">Category ({count})</button>
  <!-- Repeat for each category -->
</div>

<div class="table-wrap">
  <table class="data-table" id="{table-id}">
    <thead>
      <tr>
        <th>{Column 1}</th>
        <th>{Column 2}</th>
        <th>{Column 3}</th>
        <!-- ... -->
      </tr>
    </thead>
    <tbody>
      <tr data-category="{category}">
        <td class="funder-name">{Primary name}</td>
        <td><span class="badge {type}">{Badge text}</span></td>
        <td>{Data}</td>
        <!-- ... -->
      </tr>
      <!-- Repeat for each row -->
    </tbody>
  </table>
</div>
```

**Data attributes:**
- `data-filter` on tab buttons — matches `data-category` on rows
- `data-category` on `<tr>` — category identifier (e.g., "federal", "state", "vc", "accelerator")
- The table needs an `id` for the JavaScript filter to target it

**Requires JavaScript:** Filter tabs (see JS section below)

---

## 11. Data Table (no filters)

Simple table without filter tabs.

```html
<div class="table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>{Column 1}</th>
        <th>{Column 2}</th>
        <!-- ... -->
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="funder-name">{Primary name}</td>
        <td>{Data}</td>
        <!-- ... -->
      </tr>
      <!-- Repeat -->
    </tbody>
  </table>
</div>
```

---

## 12. Badges

Inline status indicators. Use inside tables, accordion headers, alignment lists.

```html
<!-- Viability / strength -->
<span class="badge strong">Strong</span>
<span class="badge moderate">Moderate</span>
<span class="badge weak">Weak</span>

<!-- Readiness -->
<span class="badge ready">Ready</span>
<span class="badge not-ready">Not yet</span>
<span class="badge suspended">Expired</span>
<span class="badge na">N/A</span>

<!-- Funder type -->
<span class="badge type-grant">Grant</span>
<span class="badge type-equity">Equity</span>
<span class="badge type-accel">Accelerator</span>
<span class="badge type-support">Support</span>

<!-- Gap severity -->
<span class="badge blocking">Blocking</span>
<span class="badge significant">Significant</span>
<span class="badge minor">Minor</span>
```

**Color mapping:**
- `strong`, `ready`, `type-accel` → green
- `moderate`, `not-ready`, `significant` → amber
- `blocking`, `suspended` → red
- `type-grant` → cyan
- `type-equity` → purple
- `weak`, `minor`, `na`, `type-support` → gray

---

## 13. Accordion

Expandable content sections, typically for deep dives.

```html
<div class="accordion">

  <div class="accordion-item open">
    <div class="accordion-header">
      <div class="accordion-header-left">
        <h3>{Item Title}</h3>
        <span class="badge {type}">{Type Badge}</span>
        <span class="badge {viability}">{Viability Badge}</span>
      </div>
      <span class="accordion-arrow">&#9660;</span>
    </div>
    <div class="accordion-content">
      <div class="accordion-body">
        <p>{Summary paragraph}</p>

        <h4>{Sub-heading (e.g., Stated Criteria)}</h4>
        <ul class="criteria-list">
          <li>{Criterion text} <span class="criteria-source">({Source name, date})</span></li>
          <!-- Repeat -->
        </ul>

        <h4>Alignment</h4>
        <ul class="alignment-list">
          <li class="strength">{Strength text}</li>
          <li class="gap-item">{Gap text} <span class="badge significant">Significant</span></li>
          <li class="gap-item blocker">{Blocking gap text} <span class="badge blocking">Blocking</span></li>
        </ul>

        <h4>Timeline</h4>
        <p>{Timeline text}</p>
      </div>
    </div>
  </div>

  <div class="accordion-item">
    <!-- Same structure, without "open" class -->
  </div>

</div>
```

**Notes:**
- First item gets `open` class to be expanded by default
- Criteria list items use arrow prefix (CSS `::before`)
- Alignment list items use colored left border: `.strength` (green), `.gap-item` (amber), `.gap-item.blocker` (red)
- `criteria-source` is italic gray text for inline citations

**Requires JavaScript:** Accordion toggle (see JS section below)

---

## 14. Dual-Track Visualization

Three-column grid showing two parallel tracks with a merge point.

```html
<div class="dual-track">
  <div class="track">
    <div class="track-header" style="color: var(--cyan);">Track A &mdash; {Track Name}</div>
    <div class="track-flow">
      <div class="track-step">{Step 1}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 2}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 3}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 4}</div>
    </div>
  </div>
  <div class="track-merge">
    <div class="track-merge-label">Converge</div>
  </div>
  <div class="track">
    <div class="track-header" style="color: var(--accent-light);">Track B &mdash; {Track Name}</div>
    <div class="track-flow">
      <div class="track-step">{Step 1}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 2}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 3}</div>
      <div class="track-arrow">&darr;</div>
      <div class="track-step">{Step 4}</div>
    </div>
  </div>
</div>
```

**Notes:**
- Track A typically uses `--cyan`, Track B uses `--accent-light`
- Merge column has vertical text label
- Collapses to single column at 900px (merge column hides)

---

## 15. Action Timeline

Numbered vertical timeline with action items and funder tags.

```html
<div class="action-timeline">
  <div class="action-item" data-num="1">
    <div class="action-content">
      <strong>{Action title}</strong>
      <p>{Description of what this action addresses}</p>
      <div class="funder-tags">
        <span class="funder-tag">{Funder 1}</span>
        <span class="funder-tag">{Funder 2}</span>
      </div>
    </div>
  </div>
  <div class="action-item" data-num="2">
    <div class="action-content">
      <strong>{Action title}</strong>
      <p>{Description}</p>
      <div class="funder-tags">
        <span class="funder-tag">{Funder}</span>
      </div>
    </div>
  </div>
  <!-- Repeat for each action -->
</div>
```

**Data attributes:**
- `data-num` on `.action-item` — displayed as numbered circle via CSS `::before`

---

## 16. Phase Dependency Table

Table mapping gaps to resolution phases with phase tag badges.

```html
<div class="table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>Gap</th>
        <th>Resolution</th>
        <th>Funders Affected</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="funder-name">{Gap description}</td>
        <td><span class="phase-tag {phase-class}">{Phase NN}</span> {Phase Name}</td>
        <td>{List of affected funders}</td>
      </tr>
      <!-- Repeat -->
    </tbody>
  </table>
</div>
```

**Phase tag classes:**
- `.p05` — indigo (Phase 05 Solution)
- `.p06` — purple (Phase 06 Business)
- `.p11` — green (Phase 11 Build)
- `.p12` — cyan (Phase 12 Traction)
- `.ext` — red (External dependency)

Add new phase tag classes as needed following the same pattern.

---

## 17. Gate Review

Validation summary card + decision cards with amber accent.

```html
<!-- Validation summary -->
<div class="validation-card">
  <div class="validation-status">
    <div class="validation-icon">&#10003;</div>
    <div class="validation-text">
      <h3>{Status title}</h3>
      <p>{Summary text}</p>
    </div>
  </div>
  <div class="validation-stats">
    <div class="validation-stat">
      <div class="validation-stat-value" style="color: var(--green);">{N}</div>
      <div class="validation-stat-label">Passed</div>
    </div>
    <div class="validation-stat">
      <div class="validation-stat-value" style="color: var(--amber);">{N}</div>
      <div class="validation-stat-label">Warning</div>
    </div>
    <div class="validation-stat">
      <div class="validation-stat-value" style="color: var(--red);">{N}</div>
      <div class="validation-stat-label">Failed</div>
    </div>
  </div>
</div>

<!-- Decision cards -->
<div class="gate-cards">
  <div class="gate-card">
    <div class="gate-card-header">
      <div class="gate-num">{N}</div>
      <div class="gate-question">{Decision question}</div>
    </div>
    <p class="gate-context">{Context paragraph explaining the decision}</p>
    <div class="gate-options">
      <div class="gate-option">{Option 1}</div>
      <div class="gate-option">{Option 2}</div>
      <div class="gate-option">{Option 3}</div>
    </div>
  </div>
  <!-- Repeat for each decision -->
</div>
```

**Notes:**
- Validation card has green border when passing
- Gate cards have amber left border (4px) — these are pending human decisions
- Gate numbers use amber background circles
- Options are non-interactive display elements (decisions made outside the presentation)

---

## 18. Bar Chart (CSS-only)

Horizontal bar chart using CSS widths.

```html
<div class="bar-chart">
  <div class="bar-row">
    <div class="bar-label">{Category}</div>
    <div class="bar-track">
      <div class="bar-fill" style="width: {percent}%;">{value}</div>
    </div>
  </div>
  <!-- Repeat for each bar -->
</div>
```

**Notes:**
- Calculate `width` as percentage of the maximum value (largest bar = 100%)
- Bar uses gradient fill (purple to cyan)
- Value text renders inside the bar
- No JavaScript required

---

## 19. Evidence Stats Row

Compact stat cards for evidence metrics.

```html
<div class="evidence-stats">
  <div class="evidence-stat">
    <div class="evidence-stat-value">{Value}</div>
    <div class="evidence-stat-label">{Label}</div>
  </div>
  <!-- Repeat for each stat (typically 4-5) -->
</div>
```

---

## 20. Checklist

Green checkmark list for gate criteria or requirements.

```html
<ul class="checklist">
  <li><span class="check-icon">&#10003;</span> {Criterion text}</li>
  <li><span class="check-icon">&#10003;</span> {Criterion text}</li>
  <!-- Repeat -->
</ul>
```

---

## 21. Sources Section

Categorized list of third-party sources with org names, dates, and links.

```html
<div class="sources-grid">

  <div class="source-category">
    <h3>{Category Name} ({count})</h3>
    <ul class="source-list">
      <li>
        <span class="source-org">{Organization}</span> &mdash; {Document name}
        <span class="source-date">({Date})</span><br>
        <a href="{url}" target="_blank">{domain}</a> &mdash; {What it was cited for}
      </li>
      <!-- For sources without URLs -->
      <li>
        <span class="source-org">{Organization}</span> &mdash; {Document name}
        <span class="source-date">({Date})</span><br>
        {What it was cited for}
      </li>
      <!-- Repeat -->
    </ul>
  </div>

  <!-- Repeat for each category -->

</div>

<p style="margin-top: 2rem; font-size: 0.85rem; color: var(--text-muted);">
  {Note about sources without direct URLs, if applicable}
</p>
```

**Notes:**
- Categories come from sources.md (e.g., Government, Industry, Funders, News)
- All external links use `target="_blank"`
- Source links use purple underline style (defined in design system)

---

## 22. Footer

Project metadata footer.

```html
<footer>
  <div class="container">
    <p>{Project Name} &mdash; {Phase Name} v1.0 &mdash; {Date} &mdash; Venture Forge</p>
  </div>
</footer>
```

---

## Section Wrapper Patterns

**Standard section:**
```html
<section id="{section-id}">
  <div class="container">
    <!-- Section content -->
  </div>
</section>
```

**Alternating background section:**
```html
<section class="section-alt" id="{section-id}">
  <div class="container">
    <!-- Section content -->
  </div>
</section>
```

**Notes:**
- Alternate between default (`--bg-primary`) and `.section-alt` (`--bg-secondary`) backgrounds
- Hero section uses its own `.hero` class (no `.section-alt`)
- Narrative section uses its own `.narrative` class
- Every section should have an `id` matching its nav link `href`

---

## JavaScript Patterns

Include only the JavaScript needed for components used in the phase presentation.

### JS 1: Smooth Scroll (always include)

```html
<script>
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });
</script>
```

### JS 2: Filter Tabs (include if `filter-table` component is used)

```html
<script>
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      const filter = this.dataset.filter;
      document.querySelectorAll('#{table-id} tbody tr').forEach(row => {
        row.style.display = (filter === 'all' || row.dataset.category === filter) ? '' : 'none';
      });
    });
  });
</script>
```

**Notes:**
- Replace `{table-id}` with the actual table element ID
- If multiple filter tables exist, use separate selectors or generalize

### JS 3: Accordion Toggle (include if `accordion` component is used)

```html
<script>
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', function() {
      const item = this.parentElement;
      item.classList.toggle('open');
    });
  });
</script>
```

**Notes:**
- Toggling `open` class triggers CSS transitions for arrow rotation and `max-height`
- First accordion item should have `open` class in the HTML for default-expanded state

---

## Page Structure

Complete page skeleton showing where all components fit:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Project Name} — {Phase Name}</title>
  <style>
    /* Full CSS from design-system.md */
  </style>
</head>
<body>

  <!-- Navigation (component 1) -->
  <!-- Hero section (component 2) -->
  <!-- Narrative section (component 3) -->
  <!-- Numbered sections (components 4-21, per phase-sections.yaml) -->
  <!-- Footer (component 22) -->

  <script>
    /* JS patterns as needed */
  </script>

</body>
</html>
```
