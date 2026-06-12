# Full Prospect Analysis Orchestrator — Warehouse Automation & Robotics
# Vertical: Warehouse Automation / Industrial Robotics
# Base skill: sales-prospect | Patched for: food & beverage, 3PL, building materials, big box retail
# Invocation: `/sales robotics <company-name-or-url>`

## When This Skill Is Invoked

The user runs `/sales robotics <company>`. This is the flagship command for the warehouse automation vertical. It launches 4 parallel subagents specialized for industrial sales, aggregates their findings into a unified account brief with a Deal Score, and produces a ready-to-execute account plan including a first email for the VP Supply Chain.

**Unlike standard `/sales prospect`**, this orchestrator:
- Uses `sales-robotics-research` (not `sales-research`) for facility intelligence instead of SaaS firmographics
- Uses `sales-robotics-icp` scoring criteria (facility size, labor pain, WMS readiness — not company stage/funding)
- Uses `sales-robotics-outreach` (not `sales-outreach`) for supply chain-specific email sequences
- Routes the deal qualification through a CapEx/committee-buy lens (not BANT optimized for SaaS)
- Produces a ROI Model Input Sheet alongside the standard prospect analysis

---

## Phase 1: Discovery (Sequential — Pre-Analysis)

### 1.1 Initial Data Pull

If a URL is provided, use `WebFetch` to retrieve:
- Homepage (company overview, product categories, customer types, channels)
- About/Company page (ownership, leadership, history, locations)
- Careers/Jobs page (warehouse headcount signals, WMS/ERP requirements, automation engineer postings)
- Locations page (DC network size and geographic footprint)
- Press/News page (recent facility announcements, expansion news, M&A)

If only a company name is provided (no URL), use `WebSearch`:
```
"[company name]" official website
"[company name]" distribution center OR warehouse
"[company name]" supply chain logistics
```

### 1.2 Sub-Vertical Classification (Routes All Subsequent Analysis)

Before launching subagents, classify into one of four sub-verticals. This determines which ROI benchmarks, which pain points, and which outreach angles each subagent uses.

**Classification decision tree:**
```
Does the company produce, distribute, or handle food, beverage, or grocery?
  YES → Sub-vertical: FOOD & BEVERAGE
  Key priorities: Temperature zones, FEFO, FSMA compliance, freezer labor premium
  NO ↓

Does the company operate warehouses/fulfillment on behalf of other companies (clients)?
  YES → Sub-vertical: 3PL
  Key priorities: Multi-client WMS integration, e-commerce service lines, RFP competitiveness
  NO ↓

Does the company distribute building materials, hardware, lumber, or HVAC/plumbing supplies?
  YES → Sub-vertical: BUILDING MATERIALS
  Key priorities: SKU mix analysis (automatable vs. irregular), contractor urgency, store replenishment
  NO ↓

Is the company a retailer with distribution centers for store replenishment or e-commerce?
  YES → Sub-vertical: BIG BOX RETAIL
  Key priorities: Store count served, corporate decision-making, pilot program requirement, peak season
```

Include the sub-vertical classification in the discovery briefing passed to all subagents.

### 1.3 Corporate Gate Check

Determine whether this is a direct sale or requires additional stakeholder mapping:

| Scenario | Action |
|----------|--------|
| Brand operating its own DC | Direct sale — VP Supply Chain is primary target |
| 3PL operating client's DC | Sell to 3PL operator first; may need brand co-approval for major deployments |
| Big box retailer (Home Depot, Walmart, Target, Costco, Lowe's) | Corporate decision only — DO NOT engage at DC-level; find SVP/VP Supply Chain at HQ |
| PE-backed company | CapEx approval likely requires PE sponsor sign-off above certain threshold — note in deal plan |
| Public company | Check SEC EDGAR 10-K and recent investor day for CapEx language referencing distribution |

### 1.4 Compile Discovery Briefing

Before launching subagents, compile:

```
ROBOTICS DISCOVERY BRIEFING
============================
Company: [name]
URL: [url or "name only"]
Sub-Vertical: [F&B / 3PL / Building Materials / Big Box Retail]
Corporate Gate: [Direct / 3PL dual-sell / Corporate-HQ-only / PE-backed]
Company Type: [Public / Private / PE-backed / Subsidiary]

Key Pages Found: [list with URLs]
Homepage Content: [stored]
Careers Content: [stored — WMS, automation, warehouse headcount signals]
Locations Content: [stored — DC network]
Press Content: [stored — announcements, expansions]
Initial Signals:
  - Est. DC size: [X sq ft or "unknown"]
  - Open warehouse positions: [X or "not checked yet"]
  - WMS detected: [platform or "not detected"]
  - Trigger events: [list or "none found"]
  - Sub-vertical: [classification with rationale]
```

---

## Phase 2: Parallel Analysis — 4 Subagents Simultaneously

Launch all 4 subagents simultaneously using the Claude Code Task tool. Each receives the full discovery briefing above.

**CRITICAL:** Launch all 4 in parallel. Do NOT run sequentially.

---

### Subagent 1: sales-robotics-research (Facility Intelligence)

**Skill file:** `skills/sales-robotics-research/SKILL.md`
**Weight:** 30% of Deal Score
**Focus:** Facility profile, labor economics, technology readiness, trigger events, decision maker map

**Task prompt must include:**
- Full discovery briefing
- Sub-vertical classification
- Instruction to produce a Facility Fit Score (0-100)
- Instruction to return: facility size estimate, throughput estimate, temperature zones, WMS detected, open warehouse positions count, addressable labor cost estimate, trigger events with dates, top 3 contacts with personalization anchors

**Expected output — Facility Fit Score (0-100) across:**
- Facility & Volume Fit (0-30): size, throughput, product type automatable
- Labor Pain Severity (0-25): open positions, wage signals, geographic market
- Technology Readiness (0-20): WMS, ERP, integration complexity
- Growth & Trigger Signals (0-15): greenfield, new VP, e-commerce launch, M&A
- Budget Authority (0-10): CapEx signals, decision maker seniority

---

### Subagent 2: sales-robotics-qualify (Opportunity Assessment — CapEx Committee Lens)

**Skill file:** Base `skills/sales-qualify/SKILL.md` with warehouse automation overlay
**Weight:** 25% of Deal Score
**Focus:** CapEx qualification, committee buying process, MEDDIC for industrial sales, deal size estimation, timeline estimation

**Task prompt must include:**
- Full discovery briefing
- Sub-vertical classification
- Instruction to produce an Opportunity Quality Score (0-100)
- Instruction to assess: deal size estimate (AMR pilot vs. mid-size deployment vs. full ASRS), buying committee composition, CapEx approval threshold and process, MEDDIC elements for this account

**MEDDIC for warehouse automation:**
| Element | Warehouse Automation Translation |
|---------|--------------------------------|
| **Metrics** | Pick rate improvement (units/hr), labor cost reduction ($M/year), order accuracy (%), payback period (years), storage density improvement (%) |
| **Economic Buyer** | CFO (CapEx approval), VP Supply Chain (operational authority), CEO (above ~$5M threshold) |
| **Decision Criteria** | Integration with existing WMS, throughput guarantee, uptime SLA (99.5%+), total cost of ownership, vendor service network proximity |
| **Decision Process** | RFP or direct evaluation? Pilot required? Board approval needed? Implementation partner required? |
| **Identify Pain** | Labor crisis (documented by Indeed postings), throughput ceiling (peak season failures), accuracy SLA misses (chargeback evidence), real estate pressure (capacity timeline) |
| **Champion** | Director of Engineering or Automation Manager — the person who will build the internal business case and present to the VP/CFO |

**Deal size estimation:**
| Signal | Estimated Deal |
|--------|---------------|
| Under 100,000 sq ft facility, 1–2 use cases | AMR pilot: $100K–$500K |
| 100K–300K sq ft, single use case (each-pick OR palletize) | Mid deployment: $500K–$3M |
| 300K+ sq ft, multiple use cases, ASRS consideration | Full deployment: $3M–$15M |
| Multi-DC network, greenfield or full ASRS | Enterprise: $15M–$100M+ |

**Expected output — Opportunity Quality Score (0-100) across:**
- Deal size viability (0-25): estimated deal size vs. minimum viable deal threshold
- CapEx authority mapped (0-25): CFO/board approval threshold and process identified
- Pain confirmation (0-25): labor pain, throughput ceiling, accuracy/compliance pain — evidence quality
- Timeline signals (0-25): greenfield timing, fiscal year CapEx cycle, lease expiration urgency

---

### Subagent 3: sales-robotics-contacts (Decision Maker Intelligence)

**Skill file:** Base `skills/sales-contacts/SKILL.md` with warehouse automation contact overlay
**Weight:** 20% of Deal Score
**Focus:** Buying committee mapping, decision maker identification, personalization anchors, multi-threading strategy

**Task prompt must include:**
- Full discovery briefing
- Sub-vertical classification
- Instruction to produce a Contact Access Score (0-100)
- Instruction to map: VP Supply Chain (economic buyer), Director of Engineering / Automation Manager (technical champion), CFO (financial gatekeeper), DC General Manager (ground-level champion), relevant search queries

**Priority contact search queries to execute:**
```
LinkedIn: "[company name]" + "VP Supply Chain" OR "Chief Supply Chain Officer"
LinkedIn: "[company name]" + "VP Operations" OR "VP Logistics" OR "VP Distribution"
LinkedIn: "[company name]" + "Director" + "Engineering" OR "Automation" OR "Distribution"
LinkedIn: "[company name]" + "CFO" OR "VP Finance" OR "Chief Financial Officer"
LinkedIn: "[company name]" + "General Manager" + "distribution" OR "warehouse" OR "DC"
```

**Personalization anchor research per contact:**
- LinkedIn post activity (last 90 days): supply chain topics, automation engagement, MODEX/ProMat attendance
- Conference speaking: MODEX, ProMat, WERC, CSCMP, industry vertical conference
- Published articles or LinkedIn articles
- Tenure at company (new = high receptivity; long-tenured = values peer credibility)
- Prior company: did they deploy automation at a previous employer?

**Expected output — Contact Access Score (0-100) across:**
- Economic buyer identified (0-30): VP Supply Chain or VP Operations confirmed with contact info
- Technical champion identified (0-25): Director of Engineering / Automation Manager found
- Financial gatekeeper mapped (0-20): CFO found; CapEx approval threshold estimated
- Personalization quality (0-25): quality of personalization anchors per top 3 contacts

---

### Subagent 4: sales-robotics-outreach (Outreach Strategy & First Email)

**Skill file:** `skills/sales-robotics-outreach/SKILL.md`
**Weight:** 25% of Deal Score
**Focus:** Outreach framework selection, multi-thread strategy, first email for VP Supply Chain, LinkedIn approach for technical champion, trade show follow-up if applicable

**Task prompt must include:**
- Full discovery briefing
- Sub-vertical classification
- Facility Fit Score findings from Subagent 1 (pass key signals: labor count, trigger event, WMS)
- Contact findings from Subagent 3 (pass VP name, personalization anchor, Director of Engineering name)
- Instruction to produce an Outreach Readiness Score (0-100)
- Instruction to return: selected framework with rationale, Email 1 (copy-paste ready) for VP Supply Chain, LinkedIn connection note for Director of Engineering, recommended timing, multi-thread plan

**Expected output — Outreach Readiness Score (0-100) across:**
- Personalization depth (0-25): labor signal + facility data + WMS + contact personalization anchor
- Trigger event quality (0-25): greenfield/new hire/ISA hire = hot; benchmark only = cool
- Channel strategy (0-25): VP email + Director LinkedIn + EA phone number found
- Message-market fit (0-25): sub-vertical case study matched, payback estimate specific to facility type

---

## Phase 3: Synthesis — Deal Score Calculation & Account Plan

### 3.1 Deal Score (0-100)

```
Deal Score = (
    Facility_Fit_Score      * 0.30 +
    Opportunity_Quality     * 0.25 +
    Contact_Access          * 0.20 +
    Outreach_Readiness      * 0.25
)
```

**Deal Score interpretation:**

| Score | Grade | Label | Action |
|-------|-------|-------|--------|
| 88–100 | A+ | Priority Account | Assign Senior AE immediately. Custom ROI model within 72 hours. Multi-thread outreach this week. Request internal executive sponsor for first call. |
| 75–87 | A | Strong Account | Begin personalized outreach within 48 hours. Invest in facility analysis. Prepare sub-vertical case study and payback model. |
| 60–74 | B | Qualified Account | Standard outreach sequence. Monitor Indeed for labor signal escalation. Set 30-day trigger event re-check. |
| 40–59 | C | Nurture Account | Add to 90-day nurture cadence. Re-score when facility or labor signal changes. Do not invest in deep customization yet. |
| 0–39 | D | Disqualify | Facility too small, product incompatible, or deeply locked with competitor. Remove from active pipeline. |

### 3.2 ROI Model Input Sheet

Generate a preliminary ROI Model Input Sheet from available data. Flag all estimated values as "directional — to be confirmed in discovery call."

```
ROI MODEL INPUT SHEET — [Company Name]
Sub-Vertical: [F&B / 3PL / Building Materials / Big Box Retail]
Date: [current date]
All values marked [EST] are estimates — replace with actual data in discovery.

LABOR INPUTS
- Estimated warehouse picker headcount: [X] FTEs [EST — based on Indeed postings]
- Annual loaded labor cost per picker: $[X] (wage: $[X]/hr × 1.35 overhead)
- Annual labor cost (total picking function): ~$[X]M [EST]
- Estimated annual turnover rate: [X]% (sub-vertical benchmark) [EST]
- Annual turnover cost: ~$[X]K ([headcount × turnover% × $4,000 avg cost]) [EST]
- TOTAL ADDRESSABLE LABOR COST: ~$[X]M/year [EST]

THROUGHPUT INPUTS
- Estimated annual throughput: ~[X]M units [EST — revenue-based]
- Current pick rate (sub-vertical avg): ~[X] units/associate/hour [WERC benchmark]
- Automated pick rate equivalent: ~[X] units/hour [automation benchmark]
- Throughput improvement potential: ~[X]× [EST]

ACCURACY INPUTS
- Current error rate (sub-vertical avg): ~[X]% [WERC benchmark]
- Automated accuracy rate: ~99.9% [industry standard]
- Annual cost of pick errors: ~$[X]K ([error rate × volume × $15 avg cost/error]) [EST]

ROI SUMMARY (directional)
- Automation target (% of picks): [X]% [to be scoped in discovery]
- Annual savings potential: ~$[X]M [labor + error cost reduction] [EST]
- Estimated system cost range: $[X]M–$[X]M [based on facility size and use cases]
- Directional payback period: [X]–[X] years [EST]
- 5-year NPV (10% discount rate): ~$[X]M [EST]

DATA NEEDED IN DISCOVERY CALL:
□ Actual annual throughput (units picked per year)
□ Current pick rate (units/associate/hour on pick shifts)
□ Warehouse headcount (picking associates only)
□ Loaded labor cost (wages + benefits + overtime)
□ WMS platform and version
□ Facility clear height and column spacing
□ Current or planned lease term
□ CapEx approval threshold and process
□ Peak season volume multiplier
□ [F&B only] Temperature zones and FEFO requirements
□ [3PL only] Client contract lengths and e-commerce % of volume
□ [Building materials only] Automatable SKU % estimate
```

### 3.3 Prioritized Account Plan

**Immediate (Next 48 Hours):**
1. Send Email 1 to VP Supply Chain — [Name, Title] — [specific email generated by Subagent 4]
2. Send LinkedIn connection request to Director of Engineering — [Name] — [specific note from Subagent 4]
3. Follow VP Supply Chain on LinkedIn — engage with any recent automation/supply chain post
4. [If greenfield trigger]: Alert field sales manager — design timeline is moving now
5. Log account in CRM with Facility Fit Score, trigger events, and ROI inputs

**Short-Term (Next 2 Weeks):**
1. Send Emails 2 and 3 per sequence (Day 3 and Day 7)
2. LinkedIn message to Director of Engineering / Automation Manager (Day 10)
3. [If MODEX/ProMat upcoming]: Send pre-show outreach to request meeting at show
4. Research and order sub-vertical case study that matches WMS and throughput profile
5. Build preliminary ROI model using estimated inputs — ready to share at first call

**Long-Term (Next 30-90 Days):**
1. If no response by Day 21: re-research Indeed for labor signal change; rescore account
2. [If greenfield]: Set calendar reminder 30 days after announcement to re-engage on design timeline
3. [If new VP hire]: Re-engage at 60-day mark (new leaders are most receptive at 30–90 days)
4. Target secondary contacts (CFO, DC General Manager) if primary thread stalls
5. Submit to MODEX/ProMat speaking CFP or roundtable if deal is priority account

---

## Output Format: ROBOTICS-ACCOUNT-BRIEF.md

Write the final report to `ROBOTICS-ACCOUNT-BRIEF.md` in the current directory:

```markdown
# Warehouse Automation Account Brief: [Company Name]
**Website:** [url]
**Date:** [current date]
**Sub-Vertical:** [F&B / 3PL / Building Materials / Big Box Retail]
**Corporate Gate:** [Direct / 3PL dual-sell / Corporate-HQ-only / PE-backed]
**Deal Score: [X]/100 (Grade: [letter] — [label])**
**Estimated Deal Size:** $[X]M–$[X]M ([deal type])
**Estimated Sales Cycle:** [X]–[X] months
**Confidence:** [High / Medium / Low]

---

## Executive Summary

[3-5 paragraphs. Lead with Deal Score and sub-vertical.
Cover: facility profile (size, throughput, temperature zones), labor pain (open positions,
geographic context, addressable labor cost), technology readiness (WMS, ERP, integration
complexity), primary trigger event with urgency window, recommended deal type and size,
top decision maker, and go/no-go recommendation with rationale.]

---

## Facility Snapshot

| Field | Value | Confidence |
|-------|-------|-----------|
| **Sub-Vertical** | [classification] | High |
| **Ownership** | [Public / Private / PE-backed] | [H/M/L] |
| **Revenue Est.** | ~$[X]M | [H/M/L] |
| **Primary DC Location(s)** | [cities] | [H/M/L] |
| **Est. Facility Size** | ~[X,XXX] sq ft | [H/M/L] |
| **Est. Annual Throughput** | ~[X]M units/year | Low — estimate only |
| **Temperature Zone** | [Ambient / Refrigerated / Frozen / Multi-temp] | [H/M/L] |
| **Open Warehouse Positions** | [X] as of [date] | High — confirmed |
| **WMS Detected** | [platform or "Not detected"] | [H/M/L] |
| **ERP Detected** | [platform or "Not detected"] | [H/M/L] |
| **Existing Automation** | [vendor or "None detected"] | [H/M/L] |
| **Primary Trigger Event** | [event — date] | [H/M/L] |

---

## Deal Score Breakdown

| Dimension | Score | Weight | Weighted | Key Finding |
|-----------|-------|--------|----------|-------------|
| Facility Fit | [X]/100 | 30% | [X] | [one-line finding] |
| Opportunity Quality | [X]/100 | 25% | [X] | [one-line finding] |
| Contact Access | [X]/100 | 20% | [X] | [one-line finding] |
| Outreach Readiness | [X]/100 | 25% | [X] | [one-line finding] |
| **TOTAL** | | **100%** | **[X]/100** | |

---

## Facility & Labor Intelligence

[Full output from sales-robotics-research subagent:
labor economics profile, addressable labor cost estimate, WMS/ERP stack,
facility profile, trigger events with outreach windows]

---

## Buying Committee

| Name | Title | Buying Role | Personalization Anchor | Recommended Channel |
|------|-------|-------------|----------------------|-------------------|
| [name] | VP Supply Chain | Economic Buyer | [anchor] | Email + LinkedIn |
| [name] | Director of Engineering | Technical Champion | [anchor] | LinkedIn first |
| [name] | CFO | Financial Gatekeeper | [anchor] | Email at Email 4 stage |
| [name] | DC General Manager | Ground Champion | [anchor] | LinkedIn only |

### Top Priority Contact
**Name:** [name]
**Title:** [title]
**Why first:** [rationale]
**Personalization anchor:** [specific — conference talk, LinkedIn post, recent role change]
**Email pattern:** [first.last@company.com based on detected pattern]
**LinkedIn:** [URL or search]

---

## Opportunity Assessment (CapEx Lens)

### Deal Sizing

| Deal Type | Est. Size | Likely Timeline | Triggers Needed |
|-----------|----------|-----------------|----------------|
| AMR Pilot (1 zone, 1 use case) | $[X]K–$[X]M | 3–6 months | Decision maker access + lab or reference site |
| Mid-Size Deployment | $[X]M–$[X]M | 6–12 months | VP + CFO alignment + pilot success |
| Full Deployment / ASRS | $[X]M–$[X]M | 12–24 months | Enterprise CapEx approval + RFP |
| **Most likely deal type** | **[recommendation]** | **[timeline]** | |

### MEDDIC Assessment

| Element | Finding | Evidence | Confidence |
|---------|---------|----------|-----------|
| Metrics | [pick rate, labor cost, accuracy targets] | [source] | [H/M/L] |
| Economic Buyer | [name, title] | [source] | [H/M/L] |
| Decision Criteria | [WMS integration, throughput SLA, TCO, uptime] | [source] | [H/M/L] |
| Decision Process | [RFP likely? Pilot required? Board threshold?] | [source] | [H/M/L] |
| Identify Pain | [top 2 pain categories with evidence] | [source] | [H/M/L] |
| Champion | [name — Director of Engineering / Automation Manager] | [source] | [H/M/L] |

### Risk Flags

- [Risk 1: e.g., "Existing ASRS competitor installed 18 months ago — high switching cost"]
- [Risk 2: e.g., "PE ownership may require sponsor approval above $2M CapEx"]
- [Risk 3: e.g., "WMS is custom-built — integration pathway unclear without discovery call"]

---

## Competitive Intelligence

[Prior automation vendor detection, WCS signals, competitor case study check,
switching cost assessment, recommended competitive positioning angle]

---

## ROI Model Input Sheet

[Full ROI Input Sheet from Section 3.2 with sub-vertical-specific inputs]

---

## Account Plan

### Immediate (Next 48 Hours)
1. [Specific action]
2. [Specific action]
3. [Specific action]

### Short-Term (Next 2 Weeks)
1. [Specific action]
2. [Specific action]
3. [Specific action]

### Long-Term (Next 30–90 Days)
1. [Specific action]
2. [Specific action]

---

## Ready-to-Send Email — VP Supply Chain

**To:** [Name], [Title] — [Company]
**Subject Line A:** [subject]
**Subject Line B:** [subject]
**Best Send Time:** [day/time — 7:30–8:30am or 4–5pm Tuesday–Thursday]

---

[Full email body — copy-paste ready, under 100 words,
references specific Indeed labor data, facility trigger, or sub-vertical benchmark]

---

**LinkedIn Note — Director of Engineering / Automation Manager:**
**To:** [Name]
[Connection request note — under 300 characters, references WMS or automation angle]

---

*Generated by AI Sales Team — Warehouse Automation Vertical | `/sales robotics <company>`*
```

---

## Terminal Output

```
============================================
  WAREHOUSE AUTOMATION ACCOUNT BRIEF
============================================

Company:      [name]
Sub-Vertical: [F&B / 3PL / Building Materials / Big Box Retail]
Gate:         [Direct / 3PL / Corporate-HQ / PE-backed]

Deal Score: [X]/100 (Grade: [letter] — [label])
Confidence: [High / Medium / Low]

Score Breakdown:
  Facility Fit:       [XX]/100 ████████░░
  Opportunity Quality:[XX]/100 ██████░░░░
  Contact Access:     [XX]/100 ███████░░░
  Outreach Readiness: [XX]/100 █████░░░░░

Estimated Deal: $[X]M–$[X]M ([deal type])
Est. Sales Cycle: [X]–[X] months

Primary Contact: [Name], [Title]
Primary Trigger: [trigger — date]
Open Positions: [X] warehouse roles on Indeed (as of [date])
WMS Detected: [platform or "Not detected"]
Addressable Labor Cost: ~$[X]M/year (directional)

Top 3 Outreach Angles:
  1. [angle]
  2. [angle]
  3. [angle]

Immediate Action: [single most important next step]

Full account brief saved to: ROBOTICS-ACCOUNT-BRIEF.md
ROI model inputs included in brief.
============================================
```

---

## Error Handling

- **URL unreachable:** Proceed with company name research via WebSearch. Note lower confidence.
- **Subagent failure:** Assign neutral score (50) for that dimension. Reduce overall confidence by one tier. Continue with available data.
- **Big box retailer identified:** Flag immediately in terminal output — "CORPORATE DECISION ONLY — individual DC has no CapEx authority. Route to SVP/VP Supply Chain at [HQ city]."
- **Active automation competitor detected:** Flag in Competitive Intelligence section. Note switching cost tier. Consider whether expansion (additional DC or new use case) is viable vs. displacement.
- **No WMS detected:** Flag as HIGH RISK — "No WMS in place. Automation without WMS creates inventory integrity risk. Recommend qualifying WMS timeline before proposing automation."

## Cross-Skill Integration

- `/sales robotics icp` — run first to establish scoring framework before analyzing specific accounts
- `/sales robotics research <company>` — run standalone for initial account triage before full prospect analysis
- `/sales robotics outreach <company>` — run standalone to generate full 5-email sequence after initial research
- `/sales prep` — use before a discovery call scheduled as result of this analysis
- `/sales proposal` — use after discovery call to generate formal automation proposal

*Generated by AI Sales Team — Warehouse Automation Vertical | `/sales robotics <company>`*
