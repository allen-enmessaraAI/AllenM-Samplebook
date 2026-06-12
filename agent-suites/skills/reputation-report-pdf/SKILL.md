# Professional PDF Report Generator

You are the PDF report generator for `/reputation-report-pdf`. You collect data from the most recent reputation analysis outputs and generate a polished, professional PDF document — the kind you hand directly to a client or prospective client.

## When This Skill Is Invoked

The user runs `/reputation-report-pdf` after completing one or more reputation analysis commands.

---

## Phase 1: Locate Analysis Data

### 1.1 Scan for Output Files

Search the current directory for reputation analysis output files. In priority order:

1. `REPUTATION-AUDIT.md` — Full audit with composite score
2. `REVIEWS-ANALYSIS.md` — Platform review data
3. `SENTIMENT-ANALYSIS.md` — Sentiment and theme analysis
4. `COMPETITIVE-ANALYSIS.md` — Competitor benchmarking
5. `REPUTATION-TRENDS.md` — Trend trajectory
6. `CRISIS-PLAYBOOK.md` — Crisis assessment
7. `REVIEW-RESPONSES.md` — Generated responses

Use all available files. The more files found, the richer the PDF.

**If no files found:**
"No reputation analysis data found in the current directory. Please run `/reputation-audit <url>` first, then run `/reputation-report-pdf` to generate the PDF."

### 1.2 Extract Key Data Points

From available files, extract:

| Data Point | Source |
|-----------|--------|
| Business name & location | Any audit file header |
| Reputation Score (0–100) | REPUTATION-AUDIT.md |
| Grade & label | REPUTATION-AUDIT.md |
| Score breakdown (5 dimensions) | REPUTATION-AUDIT.md |
| Platform ratings table | REVIEWS-ANALYSIS.md |
| Top praise themes | SENTIMENT-ANALYSIS.md or REPUTATION-AUDIT.md |
| Top complaint themes | SENTIMENT-ANALYSIS.md or REPUTATION-AUDIT.md |
| Competitive rank | COMPETITIVE-ANALYSIS.md or REPUTATION-AUDIT.md |
| Crisis level | CRISIS-PLAYBOOK.md or REPUTATION-AUDIT.md |
| Trajectory direction | REPUTATION-TRENDS.md or REPUTATION-AUDIT.md |
| Recommended services | REPUTATION-AUDIT.md |
| Quick wins | Any audit file |

---

## Phase 2: Generate the PDF

### 2.1 Find or Generate the Script

Look for the PDF generation script at:
1. `./scripts/generate_reputation_pdf.py`
2. `../scripts/generate_reputation_pdf.py`

### 2.2 Run the Script

```bash
python3 scripts/generate_reputation_pdf.py --input REPUTATION-AUDIT.md --output REPUTATION-REPORT.pdf
```

### 2.3 Fallback — Inline Python

If no script is found, generate the PDF using inline Python with ReportLab. Write a complete script to `/tmp/generate_reputation_pdf.py` and execute it.

---

## Phase 3: PDF Layout Specification

### Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Primary (headers) | Deep Navy | #1a365d |
| Accent (highlights) | Royal Blue | #2b6cb0 |
| Excellent | Forest Green | #276749 |
| Good | Emerald | #38a169 |
| Average | Amber | #d69e2e |
| Below Average | Orange | #c05621 |
| Poor / Crisis | Crimson | #c53030 |
| Light background | Off White | #f7fafc |
| Borders | Light Gray | #e2e8f0 |

### 3.1 Cover Page

```
[Full-width navy header bar]

REPUTATION ANALYSIS REPORT

[Business Name]
[City, State]

[Large circular gauge showing Reputation Score]

Reputation Score: [XX]/100
Grade: [Letter] — [Label]

Prepared: [Date]
Powered by AI Reputation Manager

[Full-width navy footer bar]
```

Score gauge color: Green (85–100), Emerald (70–84), Amber (55–69), Orange (40–54), Crimson (0–39)

### 3.2 Executive Summary Page

- 3–4 paragraph narrative summary
- Business snapshot table (name, category, location, score, rank, platforms)
- 3 key findings boxes (color-coded: green = strength, red = risk, amber = opportunity)

### 3.3 Score Dashboard Page

- Large score breakdown table with visual bars for each dimension
- Each dimension's score rendered as a 10-segment progress bar
- Color-coded by performance (green/amber/red)

### 3.4 Platform Review Data Page (if REVIEWS-ANALYSIS.md available)

- Platform-by-platform table with ratings, review counts, response rates
- Rating distribution stacked bar chart
- Top 3 review sample quotes

### 3.5 Sentiment Analysis Page (if SENTIMENT-ANALYSIS.md available)

- Top 5 Praise Themes (green section, with quote samples)
- Top 5 Complaint Themes (red section, with quote samples)
- Sentiment trajectory arrow graphic (↑ Improving / → Stable / ↓ Declining)

### 3.6 Competitive Benchmarking Page (if COMPETITIVE-ANALYSIS.md available)

- Competitive rank callout box (e.g., "#2 of 5 in local market")
- Side-by-side competitor comparison table
- Competitive gaps and opportunities

### 3.7 Crisis Assessment Page (if CRISIS-PLAYBOOK.md available)

- Crisis severity badge (color-coded by level)
- Crisis items found (or "No active crises detected" in green)
- Immediate action checklist

### 3.8 Recommended Services Page

```
RECOMMENDED SERVICES

[Box 1 — Critical Priority]
Service Name
What's included
$XXX–$XXX/month

[Box 2 — High Priority]
...

[Box 3 — Add-On]
...

Total Estimated Investment: $XXX–$XXX/month
```

### 3.9 Action Plan Page

- 30-Day Quick Wins checklist
- 90-Day Roadmap (3 columns: Month 1 / Month 2 / Month 3)
- Next steps

### 3.10 Footer (All Pages)

```
Left: [Business Name] — Reputation Analysis Report
Center: CONFIDENTIAL
Right: Page X of Y
```

---

## Phase 4: Verify & Present

1. Confirm PDF created: "PDF report generated: `REPUTATION-REPORT.pdf`"
2. State the absolute file path
3. List sections included in the report
4. Note any sections skipped due to missing data

## Service Pricing Reference

Use these ranges in the Recommended Services section:

| Service | Monthly Range |
|---------|--------------|
| Review Monitoring & Alerts | $200–$500/mo |
| Review Response Management | $300–$800/mo |
| Review Generation Campaign | $500–$1,200/mo |
| Reputation Monitoring Dashboard | $300–$600/mo |
| Crisis Response Retainer | $500–$1,500/mo |
| Competitor Tracking | $200–$500/mo |
| Full Reputation Management Program | $1,500–$3,500/mo |
| Google Business Profile Optimization | $300–$800 one-time |
| Sentiment Analysis Reports | $300–$600/mo |
