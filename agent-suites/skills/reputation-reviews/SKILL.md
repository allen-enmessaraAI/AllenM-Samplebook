# Review Aggregation & Analysis

You are the review aggregation engine for `/reputation-reviews <url>`. You pull review data from every major platform, analyze rating distributions, extract review samples, and produce a comprehensive REVIEWS-ANALYSIS.md report.

## When This Skill Is Invoked

The user runs `/reputation-reviews <url>` or `/reputation-reviews "<business name> <city>"`.

---

## Phase 1: Business Identification

1. Identify the business name and location from the URL or text input
2. Construct search queries for each platform (see Phase 2)
3. Note the business category — it determines which platforms to prioritize

---

## Phase 2: Platform Review Collection

Search for this business on each relevant platform. Use WebSearch and WebFetch to retrieve publicly available review data.

### Platform Priority by Business Type

| Business Type | Priority Platforms | Secondary Platforms |
|--------------|-------------------|---------------------|
| Restaurant | Google, Yelp, TripAdvisor | OpenTable, DoorDash, Grubhub |
| Home Services | Google, Yelp, Angi | HomeAdvisor, Thumbtack, BBB |
| Healthcare | Google, Healthgrades | Zocdoc, Vitals, RateMDs |
| Retail / Salon | Google, Yelp | Facebook, StyleSeat |
| Hotel / Hospitality | Google, TripAdvisor | Booking.com, Expedia, Airbnb |
| Automotive | Google, Yelp | DealerRater, Cars.com, CarGurus |
| Legal / Professional | Google, Yelp | Avvo, BBB, Martindale |
| General SMB | Google, Yelp | BBB, Facebook |

### Data to Collect Per Platform

For each platform where the business is found:

| Data Point | Description |
|------------|-------------|
| Overall rating | Star rating (out of 5) |
| Total reviews | Total review count |
| Rating distribution | Count of 5/4/3/2/1-star reviews |
| Most recent review | Date of most recent review |
| Oldest review | Date of first review found |
| Review velocity | Approximate reviews per month (recent 90 days) |
| Owner responses | Does the business respond? Estimate response rate |
| Sample reviews | 3–5 representative reviews (mix of positive and negative) |
| Profile completeness | Is the profile claimed? Are photos present? |

### Search Strategy

For each platform, use these search queries:
- `"[business name]" site:google.com/maps`
- `"[business name]" site:yelp.com`
- `"[business name]" site:bbb.org`
- `"[business name]" "[city]" reviews`
- `"[business name]" [platform name]`

If the business has a claimed profile on a platform, note it as "Active Profile." If found but unclaimed, note "Unclaimed." If not found, note "Not Listed."

---

## Phase 3: Aggregate Across Platforms

### 3.1 Calculate Blended Rating

```
Blended Rating = weighted average of all platform ratings
Weight = proportional to review count on each platform
```

### 3.2 Rating Distribution Analysis

Across all platforms, calculate:
- Total 5-star reviews (and % of total)
- Total 4-star reviews
- Total 3-star reviews
- Total 2-star reviews
- Total 1-star reviews
- **Polarization score** = (5-star% + 1-star%) — high polarization means divisive experiences

### 3.3 Review Velocity Trend

Classify the review velocity:
- **Accelerating** — More reviews in last 90 days than prior 90 days
- **Stable** — Roughly equal volume
- **Decelerating** — Fewer recent reviews (possible disengagement)
- **Stagnant** — No reviews in 90+ days

---

## Phase 4: Extract Review Samples

For each platform, extract the following sample reviews:

1. **Most recent 1-star review** — with date and full text
2. **Most recent 5-star review** — with date and full text
3. **Most-helpful/most-voted review** — with date and full text
4. **Owner response example** — if responses exist, one example (positive and negative)
5. **Most detailed review** — the longest/most substantive review found

Format each sample:

```
Platform: [name]  |  Rating: ★★★★☆ (4/5)  |  Date: [date]
"[Review text — full or truncated to 200 chars]"
Owner Response: [response text or "No response"]
```

---

## Phase 5: Output — REVIEWS-ANALYSIS.md

```markdown
# Reviews Analysis: [Business Name]
**Date:** [date]  **Location:** [city, state]  **Category:** [type]

---

## Review Summary

| Metric | Value |
|--------|-------|
| Blended Rating | ★★★★☆ [X.X] / 5.0 |
| Total Reviews (all platforms) | [n] |
| Platforms Found On | [list] |
| Platforms Not Listed | [list] |
| Review Velocity | [Accelerating/Stable/Decelerating/Stagnant] |
| Polarization Score | [X]% (High/Medium/Low) |
| Owner Response Rate | [X]% |

---

## Platform Breakdown

| Platform | Rating | Reviews | Distribution | Response Rate | Profile Status | Last Review |
|----------|--------|---------|-------------|---------------|---------------|-------------|
| Google | ⭐ [X.X] | [n] | [5★:X 4★:X 3★:X 2★:X 1★:X] | [X]% | Active/Unclaimed | [date] |
| Yelp | ⭐ [X.X] | [n] | ... | [X]% | Active/Unclaimed | [date] |
| BBB | [n/a or rating] | [n complaints] | — | — | [status] | [date] |
[... additional platforms]

---

## Rating Distribution (All Platforms Combined)

| Stars | Count | Percentage | Bar |
|-------|-------|------------|-----|
| ★★★★★ 5-star | [n] | [X]% | ████████░░ |
| ★★★★☆ 4-star | [n] | [X]% | ██████░░░░ |
| ★★★☆☆ 3-star | [n] | [X]% | ████░░░░░░ |
| ★★☆☆☆ 2-star | [n] | [X]% | ██░░░░░░░░ |
| ★☆☆☆☆ 1-star | [n] | [X]% | █░░░░░░░░░ |

---

## Review Samples

### Google Reviews
[5 sample reviews in the format specified above]

### Yelp Reviews
[5 sample reviews]

### [Other Platform]
[samples]

---

## Key Observations

### Strengths Visible in Reviews
- [Specific, evidence-backed observation]
- [Specific, evidence-backed observation]
- [Specific, evidence-backed observation]

### Weaknesses Visible in Reviews
- [Specific, evidence-backed observation]
- [Specific, evidence-backed observation]

### Gaps & Missing Profiles
- [Platforms where this business should be listed but isn't]
- [Unclaimed profiles that should be claimed]

---

## Recommended Next Steps
1. [ ] [Highest-priority action]
2. [ ] [Second action]
3. [ ] [Third action]

*Run `/reputation-respond` to generate professional responses to reviews.*
*Run `/reputation-sentiment` for deep emotional tone analysis.*
```
