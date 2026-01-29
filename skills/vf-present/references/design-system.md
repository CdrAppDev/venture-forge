# Venture Forge Design System

This is the canonical CSS specification for all Venture Forge presentations. Copy this entire stylesheet into the `<style>` block of every presentation. Do not modify the design system — use it as-is.

## Full CSS

```css
/* ====================================================================
   DESIGN SYSTEM — Venture Forge
   ==================================================================== */
:root {
  --bg-primary: #09090b;
  --bg-secondary: #18181b;
  --bg-card: #1f1f23;
  --bg-card-hover: #27272a;
  --accent: #8b5cf6;
  --accent-light: #a78bfa;
  --accent-glow: rgba(139, 92, 246, 0.12);
  --text-primary: #fafafa;
  --text-secondary: #a1a1aa;
  --text-muted: #71717a;
  --border: rgba(255, 255, 255, 0.08);
  --border-accent: rgba(139, 92, 246, 0.3);
  --gradient-1: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
  --green: #22c55e;
  --green-bg: rgba(34, 197, 94, 0.1);
  --green-border: rgba(34, 197, 94, 0.3);
  --amber: #fbbf24;
  --amber-bg: rgba(251, 191, 36, 0.1);
  --amber-border: rgba(251, 191, 36, 0.3);
  --red: #ef4444;
  --red-bg: rgba(239, 68, 68, 0.1);
  --red-border: rgba(239, 68, 68, 0.3);
  --cyan: #06b6d4;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

/* NAVIGATION */
nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: rgba(9, 9, 11, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-logo {
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text-primary);
  text-decoration: none;
  letter-spacing: -0.01em;
}
.nav-links { display: flex; gap: 1.5rem; list-style: none; }
.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  transition: color 0.2s;
}
.nav-links a:hover { color: var(--text-primary); }

/* LAYOUT */
.container { max-width: 1100px; margin: 0 auto; }
section { padding: 6rem 2rem; }
.section-alt { background: var(--bg-secondary); }
.section-num {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 0.75rem;
}
h2 {
  font-size: clamp(2rem, 4vw, 2.75rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 1rem;
  line-height: 1.15;
}
h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}
.section-lead {
  font-size: 1.125rem;
  color: var(--text-secondary);
  max-width: 640px;
  margin-bottom: 3rem;
  line-height: 1.7;
}
.gradient-text {
  background: var(--gradient-1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* NARRATIVE */
.narrative {
  padding: 4rem 2rem 6rem;
  background: var(--bg-secondary);
}
.narrative .container { max-width: 720px; }
.narrative-chapter { margin-bottom: 3rem; }
.narrative-chapter:last-child { margin-bottom: 0; }
.narrative-num {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 0.5rem;
}
.narrative-chapter h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  letter-spacing: -0.01em;
}
.narrative-chapter p {
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.8;
}
.narrative-chapter p strong {
  color: var(--text-primary);
  font-weight: 600;
}
.narrative-divider {
  width: 48px;
  height: 2px;
  background: var(--accent);
  opacity: 0.4;
  margin: 3.5rem 0;
}
.narrative-chapter a {
  color: var(--text-secondary);
  text-decoration: underline;
  text-decoration-color: var(--accent);
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
  transition: color 0.2s;
}
.narrative-chapter a:hover { color: var(--accent-light); }
.narrative-chapter a strong { color: inherit; }
.narrative-cta {
  margin-top: 3rem;
  padding: 1.5rem 2rem;
  background: var(--accent-glow);
  border: 1px solid var(--border-accent);
  border-radius: 12px;
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.7;
}
.narrative-cta strong { color: var(--accent-light); }

/* HERO */
.hero {
  padding: 10rem 2rem 6rem;
  text-align: center;
}
.hero h1 {
  font-size: clamp(3rem, 7vw, 4.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-bottom: 1.5rem;
}
.hero .lead {
  font-size: 1.25rem;
  color: var(--text-secondary);
  max-width: 620px;
  margin: 0 auto 3rem;
  line-height: 1.7;
}
.funnel {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}
.funnel-box {
  padding: 0.6rem 1.2rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-secondary);
  background: var(--bg-card);
}
.funnel-box.highlight {
  border-color: var(--border-accent);
  background: var(--accent-glow);
  color: var(--accent-light);
}
.funnel-arrow { color: var(--text-muted); font-size: 1rem; }
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}
.hero-stat-value {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}
.hero-stat-value.accent { color: var(--accent-light); }
.hero-stat-value.green { color: var(--green); }
.hero-stat-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 0.25rem;
}

/* CARDS */
.card-grid { display: grid; gap: 1.5rem; }
.card-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
.card-grid.cols-2 { grid-template-columns: repeat(2, 1fr); }
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
}
.card-label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-weight: 600;
  margin-bottom: 0.75rem;
}
.card-label.purple { color: var(--accent-light); }
.card-label.green { color: var(--green); }
.card-label.amber { color: var(--amber); }
.card-label.red { color: var(--red); }
.card-label.cyan { color: var(--cyan); }
.card h3 { margin-bottom: 0.5rem; }
.card p { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.65; }
.callout {
  border: 1px dashed var(--amber-border);
  background: var(--amber-bg);
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-top: 2rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.65;
}
.callout strong { color: var(--amber); }

/* STAT CARDS */
.stat-row {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}
.stat-card {
  flex: 1;
  min-width: 200px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
}
.stat-card-value {
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 0.25rem;
}
.stat-card-label { font-size: 0.8rem; color: var(--text-muted); }

/* DATA TABLES */
.table-wrap { overflow-x: auto; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
.data-table thead th {
  text-align: left;
  padding: 0.75rem 1rem;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
  font-weight: 600;
  white-space: nowrap;
}
.data-table tbody td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--border);
  color: var(--text-secondary);
  vertical-align: top;
}
.data-table tbody tr:hover { background: var(--bg-card); }
.data-table .funder-name {
  color: var(--text-primary);
  font-weight: 600;
  white-space: nowrap;
}

/* BADGES */
.badge {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
}
.badge.strong { background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }
.badge.moderate { background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }
.badge.weak { background: rgba(113,113,122,0.15); color: var(--text-muted); border: 1px solid rgba(113,113,122,0.3); }
.badge.ready { background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }
.badge.not-ready { background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }
.badge.suspended { background: var(--red-bg); color: var(--red); border: 1px solid var(--red-border); }
.badge.na { background: rgba(113,113,122,0.1); color: var(--text-muted); border: 1px solid rgba(113,113,122,0.2); }
.badge.type-grant { background: rgba(6,182,212,0.1); color: var(--cyan); border: 1px solid rgba(6,182,212,0.3); }
.badge.type-equity { background: var(--accent-glow); color: var(--accent-light); border: 1px solid var(--border-accent); }
.badge.type-accel { background: var(--green-bg); color: var(--green); border: 1px solid var(--green-border); }
.badge.type-support { background: rgba(113,113,122,0.1); color: var(--text-muted); border: 1px solid rgba(113,113,122,0.2); }
.badge.blocking { background: var(--red-bg); color: var(--red); border: 1px solid var(--red-border); }
.badge.significant { background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber-border); }
.badge.minor { background: rgba(113,113,122,0.1); color: var(--text-muted); border: 1px solid rgba(113,113,122,0.2); }

/* FILTER TABS */
.filter-tabs { display: flex; gap: 0.5rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.tab-btn {
  padding: 0.45rem 1rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}
.tab-btn:hover { border-color: var(--text-muted); color: var(--text-secondary); }
.tab-btn.active {
  border-color: var(--border-accent);
  background: var(--accent-glow);
  color: var(--accent-light);
}

/* ACCORDION */
.accordion { display: flex; flex-direction: column; gap: 1rem; }
.accordion-item {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  background: var(--bg-card);
}
.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem;
  cursor: pointer;
  transition: background 0.2s;
}
.accordion-header:hover { background: var(--bg-card-hover); }
.accordion-header-left { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
.accordion-header h3 { margin: 0; font-size: 1.05rem; }
.accordion-arrow {
  font-size: 1.2rem;
  color: var(--text-muted);
  transition: transform 0.3s;
  flex-shrink: 0;
}
.accordion-item.open .accordion-arrow { transform: rotate(180deg); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; }
.accordion-item.open .accordion-content { max-height: 3000px; }
.accordion-body { padding: 0 1.5rem 1.5rem; border-top: 1px solid var(--border); }
.accordion-body p { color: var(--text-secondary); font-size: 0.9rem; line-height: 1.65; margin-top: 1.25rem; }
.accordion-body h4 {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

/* ALIGNMENT LISTS (inside accordions) */
.alignment-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
.alignment-list li {
  font-size: 0.875rem;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border-left: 3px solid;
  line-height: 1.5;
}
.alignment-list li.strength { border-color: var(--green); background: var(--green-bg); color: var(--text-secondary); }
.alignment-list li.gap-item { border-color: var(--amber); background: var(--amber-bg); color: var(--text-secondary); }
.alignment-list li.gap-item.blocker { border-color: var(--red); background: var(--red-bg); }
.criteria-list { list-style: none; display: flex; flex-direction: column; gap: 0.4rem; }
.criteria-list li {
  font-size: 0.875rem;
  color: var(--text-secondary);
  padding-left: 1rem;
  position: relative;
  line-height: 1.5;
}
.criteria-list li::before { content: "\2192"; position: absolute; left: 0; color: var(--accent-light); }
.criteria-source { font-size: 0.75rem; color: var(--text-muted); font-style: italic; }

/* DUAL-TRACK STRATEGY */
.dual-track { display: grid; grid-template-columns: 1fr auto 1fr; gap: 2rem; margin-bottom: 3rem; }
.track {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.5rem;
}
.track-header {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-weight: 600;
  margin-bottom: 1rem;
}
.track-flow { display: flex; flex-direction: column; gap: 0.5rem; }
.track-step {
  padding: 0.5rem 0.75rem;
  background: var(--bg-secondary);
  border-radius: 6px;
  font-size: 0.85rem;
  color: var(--text-secondary);
}
.track-arrow { text-align: center; color: var(--text-muted); font-size: 0.9rem; }
.track-merge { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem; }
.track-merge-label {
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-size: 0.75rem;
  color: var(--text-muted);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

/* ACTION TIMELINE */
.action-timeline { display: flex; flex-direction: column; gap: 0; }
.action-item {
  display: flex;
  gap: 1.25rem;
  padding: 1rem 0;
  border-left: 2px solid var(--border);
  margin-left: 1rem;
  padding-left: 1.5rem;
  position: relative;
}
.action-item::before {
  content: attr(data-num);
  position: absolute;
  left: -0.85rem;
  width: 1.5rem;
  height: 1.5rem;
  background: var(--accent);
  color: white;
  border-radius: 50%;
  font-size: 0.7rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.action-content { flex: 1; }
.action-content strong { font-size: 0.95rem; display: block; margin-bottom: 0.25rem; }
.action-content p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.5; }
.funder-tags { display: flex; gap: 0.35rem; margin-top: 0.5rem; flex-wrap: wrap; }
.funder-tag {
  font-size: 0.6rem;
  padding: 0.15rem 0.4rem;
  border-radius: 3px;
  background: var(--accent-glow);
  color: var(--accent-light);
  border: 1px solid var(--border-accent);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* PHASE BADGES */
.phase-tag {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  letter-spacing: 0.05em;
}
.phase-tag.p05 { background: rgba(99,102,241,0.15); color: #818cf8; }
.phase-tag.p06 { background: var(--accent-glow); color: var(--accent-light); }
.phase-tag.p11 { background: var(--green-bg); color: var(--green); }
.phase-tag.p12 { background: rgba(6,182,212,0.15); color: var(--cyan); }
.phase-tag.ext { background: var(--red-bg); color: var(--red); }

/* GATE REVIEW */
.validation-card {
  background: var(--bg-card);
  border: 1px solid var(--green-border);
  border-radius: 12px;
  padding: 1.5rem 2rem;
  margin-bottom: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  flex-wrap: wrap;
}
.validation-status { display: flex; align-items: center; gap: 1rem; }
.validation-icon {
  width: 48px; height: 48px;
  border-radius: 50%;
  background: var(--green-bg);
  border: 2px solid var(--green);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}
.validation-text h3 { margin-bottom: 0.15rem; font-size: 1rem; }
.validation-text p { font-size: 0.85rem; color: var(--text-muted); margin: 0; }
.validation-stats { display: flex; gap: 1.5rem; }
.validation-stat { text-align: center; }
.validation-stat-value { font-size: 1.5rem; font-weight: 800; }
.validation-stat-label { font-size: 0.65rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; }
.gate-cards { display: flex; flex-direction: column; gap: 1.25rem; }
.gate-card {
  background: var(--bg-card);
  border: 1px solid var(--amber-border);
  border-left: 4px solid var(--amber);
  border-radius: 12px;
  padding: 1.5rem 2rem;
}
.gate-card-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem; }
.gate-num {
  width: 2rem; height: 2rem;
  background: var(--amber-bg);
  border: 1px solid var(--amber-border);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--amber);
  flex-shrink: 0;
}
.gate-question { font-size: 1.05rem; font-weight: 600; }
.gate-context { font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem; }
.gate-options { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.gate-option {
  padding: 0.4rem 0.8rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 0.8rem;
  color: var(--text-muted);
  background: var(--bg-secondary);
}

/* BAR CHART (CSS-only) */
.bar-chart { margin-top: 2rem; }
.bar-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem; }
.bar-label { width: 120px; font-size: 0.75rem; color: var(--text-muted); text-align: right; flex-shrink: 0; }
.bar-track { flex: 1; height: 24px; background: var(--bg-secondary); border-radius: 4px; overflow: hidden; }
.bar-fill {
  height: 100%;
  border-radius: 4px;
  background: var(--gradient-1);
  display: flex;
  align-items: center;
  padding-left: 0.5rem;
  font-size: 0.7rem;
  font-weight: 600;
  color: white;
  min-width: fit-content;
}

/* EVIDENCE STATS */
.evidence-stats { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem; }
.evidence-stat {
  flex: 1;
  min-width: 120px;
  text-align: center;
  padding: 1.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
}
.evidence-stat-value { font-size: 1.75rem; font-weight: 800; color: var(--accent-light); }
.evidence-stat-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 0.25rem;
}

/* CHECKLIST */
.checklist { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
.checklist li {
  font-size: 0.9rem;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.check-icon { color: var(--green); font-size: 1rem; }

/* SCALE NOTE */
.scale-note {
  background: var(--accent-glow);
  border: 1px solid var(--border-accent);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-top: 2rem;
  line-height: 1.6;
}
.scale-note strong { color: var(--accent-light); }

/* SOURCES */
.sources-grid { display: grid; gap: 2rem; margin-top: 2rem; }
.source-category { margin-bottom: 1rem; }
.source-category h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--accent-light);
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
.source-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
.source-list li {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--border);
}
.source-list li:last-child { border-bottom: none; }
.source-list a {
  color: var(--text-secondary);
  text-decoration: underline;
  text-decoration-color: var(--accent);
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
  transition: color 0.2s;
}
.source-list a:hover { color: var(--accent-light); }
.source-org { color: var(--text-primary); font-weight: 500; }
.source-date { color: var(--text-muted); font-size: 0.8rem; }

/* FOOTER */
footer { padding: 3rem 2rem; text-align: center; border-top: 1px solid var(--border); }
footer p { font-size: 0.8rem; color: var(--text-muted); }

/* RESPONSIVE */
@media (max-width: 900px) {
  .dual-track { grid-template-columns: 1fr; }
  .track-merge { display: none; }
}
@media (max-width: 768px) {
  .nav-links { display: none; }
  .card-grid.cols-3 { grid-template-columns: 1fr; }
  .card-grid.cols-2 { grid-template-columns: 1fr; }
  .hero-stats { gap: 1.5rem; }
  .hero h1 { font-size: 2.5rem; }
  .validation-card { flex-direction: column; align-items: flex-start; }
  .validation-stats { gap: 1rem; }
  .stat-row { flex-direction: column; }
  .evidence-stats { flex-direction: column; }
  section { padding: 4rem 1.25rem; }
  .data-table { font-size: 0.8rem; }
  .data-table thead th,
  .data-table tbody td { padding: 0.5rem 0.6rem; }
}
```
