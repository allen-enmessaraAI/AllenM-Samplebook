# Company Research & Firmographic Analysis — Warehouse Automation & Robotics
# Vertical: Warehouse Automation / Industrial Robotics
# Base skill: sales-research | Patched for: food & beverage, 3PL, building materials, big box retail

## Vertical Context

VERTICAL: Warehouse Automation & Robotics
RESEARCH GOAL: Produce a complete facility intelligence brief on a prospect distribution center, warehouse, or 3PL operation. Unlike SaaS company research, warehouse automation research centers on the PHYSICAL FACILITY (sq footage, throughput, temperature zones, product type), the LABOR ECONOMICS (headcount, open positions, wage rates, turnover), and the TECHNOLOGY READINESS (WMS, ERP, existing automation). Every finding directly informs the ROI model, the integration complexity estimate, and the outreach angle.
PRIMARY CONTACTS: VP Supply Chain / VP Operations (economic buyer), Director of Distribution/Logistics (operational buyer), Director of Engineering / Automation Manager (technical champion), CFO (financial gatekeeper)
CORPORATE GATE: Identify whether the facility is a corporate-owned DC or operated by a 3PL on a client's behalf. Corporate-owned = direct sale. 3PL-operated = may need to sell both the 3PL operator AND the brand (end client). In the case of Big Box retailers (Home Depot, Walmart, Target), the DC is corporate-owned but all decisions are made centrally — do NOT try to sell at the individual DC level.
TERMINOLOGY: distribution center (DC), throughput (units/hour), SKU velocity, pick rate, order accuracy, greenfield (new facility), brownfield (existing facility retrofit), FEFO (First Expired First Out — F&B critical), lot tracking, FIFO, pallet in/pallet out, case pick, each pick, piece pick, VAS (Value-Added Services), receiving, putaway, replenishment, picking, packing, shipping, cycle count, safety stock, dock doors, clear height (facility spec), WMS, WCS, ERP, AMR, ASRS, GTP, RaaS (Robotics as a Service), CapEx, OpEx, TCO, payback period
DATA FRESHNESS: Labor signals (Indeed postings): must be within 60 days. Facility announcements: within 12 months. Financial/revenue data: within 18 months. WMS information from job postings: within 24 months.

---

## Purpose

You are the company research engine for warehouse automation prospects. Produce an 8-dimension facility intelligence brief that a sales engineer and account executive can use to build a ROI model, estimate integration complexity, and select the right outreach angle. This skill is invoked standalone or as the `sales-robotics-research` subagent within `/sales robotics <company>`.

---

## Phase 1: Corporate Structure & Sub-Vertical Classification

### 1.1 Corporate Gate Check

Execute before any other research. Answer three questions:

**Q1: Who owns and operates the facility?**
- Self-operated DC (brand owns and runs their own warehouse) → direct sale
- 3PL-operated facility on behalf of a brand → sell 3PL first; brand may need to co-approve
- Contract warehouse with multiple tenants → multi-client 3PL play

**Q2: Is this a corporate decision or site-level decision?**
- Big box retailers (Home Depot, Walmart, Target, Costco, Lowe's, Ace): ALL decisions made centrally at HQ. Individual DC managers have no budget authority. Find corporate supply chain VP.
- Regional distributors ($50M–$1B revenue): VP Operations or COO makes the decision, often with CEO input.
- 3PLs: VP Operations + Chief Commercial Officer (automation wins contracts) + CFO (CapEx approval).

**Q3: Is this a public or private company?**
- Public: SEC EDGAR for 10-K, 10-Q — look for CapEx line items mentioning "distribution," "fulfillment," "warehouse modernization," or "automation." Investor day presentations often contain DC investment disclosures.
- Private: No financials available. Revenue must be estimated from employees, industry benchmarks, and trade press.

### 1.2 Sub-Vertical Classification

| Sub-Vertical | Detection Signals | Key Research Angle |
|-------------|-----------------|-------------------|
| **Food & Beverage** | Food distributor, beverage company, grocery DC, cold chain, FSMA/SQF mentions | Temperature zones, FEFO/lot tracking requirements, FDA compliance, seasonal peaks |
| **3PL** | "Third-party logistics," "contract warehousing," "fulfillment services," multiple client logos | Multi-client WMS integration, client contract lengths, e-commerce service lines, RaaS model receptivity |
| **Building Materials** | Hardware, lumber, pipe, roofing, fasteners, HVAC products, contractor supply | Irregular SKU mix, automatable vs. non-automatable zone split, seasonal construction peaks |
| **Big Box Retail** | Retail DC, store replenishment, omnichannel fulfillment, regional distribution hub | Store count served, throughput estimates, e-commerce channel growth, corporate decision-making level |

---

## Phase 2: The 8 Research Dimensions (Warehouse Automation Edition)

### Dimension 1: Company & Facility Overview

**Data points to capture:**

| Field | Description | Sources |
|-------|-------------|---------|
| Legal company name | Parent entity and operating subsidiary | Website, SEC filings, state business registry |
| Ownership structure | Public / private / PE-backed / family-owned | Press, Crunchbase, Bloomberg, PitchBook |
| Revenue estimate | Annual revenue — use sub-vertical benchmarks if not public | 10-K, press releases, employee-based estimation |
| Number of DCs / warehouses | Network size — 1 DC vs. 50 DC network = very different scope | Website, 10-K, logistics press |
| DC locations | City, state, zip code — proximity to labor markets and service infrastructure | Website, Google Maps, logistics press, EDGAR |
| Primary facility size | Square footage of main DC — critical for ROI model | Press releases, building permits, CoStar signals, job postings |
| Facility type | Greenfield / brownfield / leased / owned | Lease announcements, building permits, real estate press |
| Products handled | SKU types — ambient, frozen, refrigerated, building materials, retail goods | Website, product catalog, trade press |
| Annual throughput estimate | Units/year — estimate from revenue × industry conversion factors | See calculation table below |
| Temperature zones | Ambient only / ambient + refrigerated / ambient + frozen / multi-temp | Job postings (freezer pay differential = frozen), website, trade press |

**Throughput estimation table (directional — note confidence level):**
| Sub-Vertical | Revenue Range | Est. Units/Year | Basis |
|-------------|--------------|-----------------|-------|
| F&B distributor | $100M–$500M | 5M–25M | ~$20 avg case value |
| F&B manufacturer | $200M–$1B | 3M–15M | Higher avg unit value |
| 3PL (e-commerce) | $50M–$300M | 10M–100M | Low avg unit value ($5–$15) |
| Building materials | $100M–$500M | 1M–10M | Higher avg unit value |
| Big box retail DC | N/A (look at store count) | 20M–500M | Store count × avg store throughput |

Always note: "Throughput estimate is directional, based on [basis]. Actual throughput required for ROI model — request during discovery call."

---

### Dimension 2: Labor Economics Profile

**This is the most important dimension.** Labor pain is the primary buying trigger in warehouse automation. A company with extreme labor pain but small facility is still a better prospect than a large facility with no labor signal.

**Data points to capture:**

**Indeed / ZipRecruiter / LinkedIn Jobs (execute all three searches):**
Search "[company name] warehouse" AND "[city]":

| Job Posting | Signal Interpretation |
|------------|----------------------|
| 10+ open warehouse picker / order selector / fulfillment associate positions | CRITICAL: Labor crisis signal. This is the #1 outreach trigger. |
| Sign-on bonus mentioned ($500–$3,000) | Labor market is tight — company is competing for workers |
| "Weekend differential pay" or "freezer premium" | Difficulty filling specific shifts/zones |
| Temp agency partnership mentioned | Using contingent labor = high variable labor cost, lower commitment to automation |
| "Immediate openings" or "start this week" | Urgency = current operation is understaffed |
| "No experience required" or "will train" | Low bar = struggling to find qualified workers |
| Hiring "Automation Engineer" or "Robotics Technician" | Company is actively evaluating or deploying automation |
| Hiring "WMS Analyst" or "Supply Chain Systems Manager" | WMS modernization in progress = automation window |
| Multiple simultaneous postings across multiple locations | Network-level labor crisis = enterprise deal potential |

**Glassdoor / Indeed company reviews:**
- Search "[company name] reviews" filtered to "warehouse" and "operations"
- Keywords to flag: "understaffed," "short-handed," "high turnover," "no help," "unrealistic expectations," "not enough workers"
- Average Glassdoor rating under 3.0 in warehouse operations: strong labor culture problem signal
- Recent reviews (last 90 days) are more credible than older reviews

**Geographic labor market context:**
- Note the metro area of each facility
- Tight labor markets: Los Angeles, New York/NJ, Chicago, Dallas, Atlanta, Phoenix (logistics hub with Amazon oversaturation)
- These markets have structural warehouse labor shortages regardless of the company
- Flag: "Facility is located in [metro] — a historically tight warehouse labor market. This amplifies the automation ROI case regardless of company-specific signals."

**Labor cost estimation:**
- Warehouse picker avg wage by market: $18–$26/hour (2024 US range)
- Including benefits, taxes, and overhead: multiply hourly rate × 1.35 (loaded cost)
- Annual cost per FTE picker at $22/hour loaded: ~$61,000/year
- If company has 100 pickers and 50% are automatable: $3.05M/year in labor cost addressable by automation

Document: "Estimated addressable labor cost: $[X]M/year based on [X] open/estimated picker headcount at $[X]/hr loaded rate in [metro] market."

---

### Dimension 3: Technology Stack Assessment

**WMS Detection (most important tech signal):**

| WMS Platform | Detection Method | Automation Compatibility | Notes |
|-------------|-----------------|------------------------|-------|
| **Manhattan Active WMS** | Job postings: "Manhattan WMS experience required" | Excellent API integration | Modern REST API; most automation vendors have certified connectors |
| **Blue Yonder WMS** | Job postings, LinkedIn skills on ops team | Excellent | JDA rebranded to Blue Yonder; strong API layer |
| **Körber (HighJump)** | Job postings, LinkedIn, trade press | Good | Körber acquired HighJump; common in F&B and 3PL |
| **SAP Extended Warehouse Management (EWM)** | Job postings: "SAP EWM" or "SAP WM" | Good (SAP EWM) / Difficult (SAP WM) | EWM = modern; WM = legacy, requires middleware |
| **Oracle WMS** | Job postings: "Oracle WMS" or "Oracle SCM Cloud" | Moderate | Cloud version better than on-prem |
| **Infor WMS** | Job postings: "Infor WMS" or "Infor SCE" | Moderate | Common in F&B and distribution |
| **3PL Central / Extensiv** | 3PL job postings, website mentions | Basic | Designed for SMB 3PL; limited automation integration |
| **Custom / Legacy** | No WMS named + iSeries / AS400 job postings | Difficult | Major integration project required |
| **None / Spreadsheets** | No WMS mentioned anywhere | Very Difficult | Must implement WMS before automation |

**ERP Detection:**
Search job postings and LinkedIn team profiles:
- SAP S/4HANA or SAP R/3: standard large enterprise, strong integration ecosystem
- Oracle ERP Cloud: strong integration, more common in retail and F&B
- Microsoft Dynamics 365: mid-market; growing in distribution
- NetSuite: SMB/mid-market; simpler WMS integration but less robust

**Existing Automation Detection:**
Search "[company name] automation" and "[company name] robotics" in trade press:
- Prior AMR deployment: what vendor? Still in service? (If competitor installation, note which competitor)
- Conveyor/sortation: common in any facility over 100K sq ft
- ASRS already installed: deal is likely replacement or expansion, not greenfield
- "Pilot program" mentioned: in evaluation stage — high receptivity

---

### Dimension 4: Facility Intelligence

**Physical facility signals determine what automation systems are viable:**

**Clear height (critical for ASRS systems):**
- Under 24 ft: standard racking only; most ASRS systems incompatible
- 24–32 ft: AMR systems viable; some ASRS viable; AutoStore viable
- 32–40 ft: full ASRS viable; maximum storage density achievable
- Detection: building permit filings (county GIS systems), industrial real estate listings (CoStar, LoopNet), job postings that mention "high-bay warehouse"

**Dock door count:**
- Dock doors ÷ 10,000 sq ft is a standard throughput ratio
- High dock count = high receiving/shipping velocity = strong throughput signal
- Detection: Google Maps satellite view (count dock doors), facility descriptions in press releases

**Lease vs. owned:**
- Owned facility = company controls renovation timeline; automation CapEx is more committable
- Leased facility = landlord approval may be required for floor anchoring (some ASRS systems require floor anchors)
- Detection: "acquired facility" or "own" in press vs. "lease" or "new lease" announcements

**Greenfield signals (highest automation opportunity):**
A greenfield facility is the ideal automation scenario — no legacy infrastructure to work around, automation can be designed in from the start.
```
Detection searches:
"[company name]" "new distribution center" site:supplychaindive.com
"[company name]" "ground breaking" OR "broke ground" warehouse
"[company name]" "new facility" OR "new DC" "[state]" [year]
county building permit search: commercial/industrial permits > 100,000 sq ft near company's known markets
```

**Brownfield signals:**
- Existing facility with no announced expansion = retrofit automation opportunity
- Clear height and column spacing are key constraints for brownfield — must research before proposing ASRS

---

### Dimension 5: Supply Chain & Logistics Profile

**Data points to capture:**

| Field | Description | Sources |
|-------|-------------|---------|
| Network structure | Single DC / regional DCs / national network | Website "locations," 10-K, press |
| Primary use cases | Store replenishment / e-commerce fulfillment / cold chain / manufacturing supply | Website, job postings, trade press |
| Order profile | B2B bulk orders (full pallets) vs. B2C individual orders (each picks) | Infer from channel mix and customer types |
| Carrier relationships | LTL / FTL / parcel (UPS, FedEx, USPS) / private fleet | Website, job postings ("carrier management") |
| Inventory ownership | First-party inventory vs. 3PL consignment | Business model signals |
| Seasonal peaks | When are their peak volume periods? | Industry calendar (holiday = retail; spring = building materials; summer = F&B beverage) |
| Returns volume | Returns processing = additional automation use case | e-commerce channel = returns; B2B bulk = minimal |
| Compliance requirements | FSMA (F&B), SOX (financial), FDA, HAZMAT | Sub-vertical and job posting language |

**E-commerce channel detection:**
- Website has a "Shop" or "Order Online" section → direct e-commerce = each-pick volume
- Job posting: "e-commerce fulfillment," "small parcel," "DTC," "direct-to-consumer" → e-commerce automation use case
- Investor day mentions "e-commerce growth" or "digital channel" → growing each-pick volume

---

### Dimension 6: Decision Maker Map

**Target contacts for warehouse automation — in priority order:**

| Title | Buying Role | Detection Source | Priority |
|-------|------------|-----------------|----------|
| VP Supply Chain / CSCO | Economic buyer; strategic authority | LinkedIn, company website leadership page | #1 |
| VP Operations / COO (smaller companies) | Economic buyer at mid-size; day-to-day pain owner | LinkedIn, website | #1 |
| Director of Logistics / Director of Distribution | Operational champion; knows the pain best | LinkedIn, website, job postings | #2 |
| Director of Engineering / Automation Manager | Technical champion; likely already researching vendors | LinkedIn (keywords: "automation," "robotics," "WMS"), Indeed | #2 |
| CIO / VP of IT | Technical gatekeeper for integration | LinkedIn, website | #3 |
| CFO / VP Finance | Financial gatekeeper for CapEx approval | LinkedIn, 10-K (public companies), website | #3 |
| DC / Warehouse General Manager | Ground-level champion; direct pain owner | LinkedIn, job postings ("reports to VP Operations") | #4 |

**LinkedIn search for decision makers:**
```
Search 1: "[company name]" + "VP Supply Chain" OR "VP Operations" OR "Chief Supply Chain"
Search 2: "[company name]" + "Director" + "Distribution" OR "Logistics" OR "Warehouse"
Search 3: "[company name]" + "Automation" OR "Robotics" + "Manager" OR "Director" OR "Engineer"
Search 4: "[company name]" + "Director of Engineering" + "operations" OR "distribution"
```

**Personalization research per contact:**
For each identified decision maker, collect:
- LinkedIn activity: recent posts, comments, shares — automation/supply chain content engagement = warm signal
- Conference speaking: MODEX, ProMat, WERC, CSCMP — speakers are open to vendor engagement
- Published articles or LinkedIn articles: topics reveal priorities
- Tenure at company: <18 months = new leader looking to make mark = high receptivity to change; >10 years = may be entrenched in current processes
- Career history: prior company had automation = familiar with the technology; no prior automation experience = needs more education

---

### Dimension 7: Competitive Intelligence

**Current automation vendor detection:**

**Step 1: Direct search for prior automation deployments:**
```
"[company name]" "automation" OR "robotics" OR "AMR" OR "ASRS" site:dcvelocity.com
"[company name]" "automation" site:supplychaindive.com
"[company name]" "automates" OR "automated" OR "deploys robots"
"[company name]" "[competitor name: Locus / AutoStore / Dematic / 6 River]"
```

**Step 2: Job posting technology signals:**
- "Experience with [competitor WCS/WMS layer]" → that competitor's software is in use
- "Locus Robotics system administrator" → Locus deployment in place
- "AutoStore" or "Cube Storage" experience → AutoStore installation

**Step 3: Case study searches:**
- Search competitor websites for case studies featuring the prospect company
- Dematic, Locus, AutoStore, 6 River Systems all publish case studies by client name

**Competitive landscape documentation:**
| Competitor Detected | Confidence | Evidence | Switching Cost Assessment |
|--------------------|-----------|----------|--------------------------|
| [vendor name] | High/Medium/Low | [specific evidence] | High (ASRS infrastructure) / Medium (AMR — can add fleet) / Low (WCS software only) |

---

### Dimension 8: Trigger Events & Recent Developments

**Execute these searches for each prospect:**

```
Search 1: "[company name]" "distribution center" OR "warehouse" [current year]
Search 2: "[company name]" "expansion" OR "new facility" OR "greenfield"
Search 3: "[company name]" "automation" OR "robotics" OR "modernize"
Search 4: "[company name]" "acquisition" OR "acquired" OR "merger"
Search 5: "[company name]" "e-commerce" OR "DTC" OR "direct-to-consumer" OR "omnichannel"
Search 6: "[company name]" "labor" OR "workforce" OR "hiring" OR "staffing"
Search 7: "[company name]" MODEX OR ProMat OR WERC OR CSCMP [recent years]
```

**Real estate / greenfield detection:**
```
site:bizjournals.com "[company name]" "distribution center" OR "warehouse"
site:costar.com "[company name]" [skip — paywalled; note for manual lookup]
county assessor "[company name]" commercial construction [county name]
```

**Trigger event classification:**

| Trigger | Recency | Outreach Window |
|---------|---------|----------------|
| Greenfield facility announced | < 6 months | HOT — reach out before design is locked in |
| New DC lease signed | < 3 months | HOT — fit-out planning is starting |
| WMS implementation announced | < 6 months | HOT — integration planning window |
| New VP Supply Chain / VP Operations hired | < 4 months | WARM — new leader evaluating everything |
| E-commerce channel launch announced | < 6 months | WARM — each-pick volume is new and growing |
| M&A announcement (acquiring) | < 3 months | WARM — network rationalization creates automation evaluation |
| Peak season failure reported | < 90 days post-event | WARM — pain is fresh and documented |
| MODEX/ProMat attendance confirmed | During or just after event | WARM — they are actively evaluating |
| Investor day mentions distribution investment | < 12 months | WARM — CapEx is approved or being approved |
| Prior automation competitor deployment (completed) | Any | COOL — assess if expansion opportunity or locked out |

---

## Output Format: RE-FACILITY-RESEARCH.md

```markdown
# Warehouse Automation Prospect Research: [Company Name]
**Website:** [url]
**Date:** [current date]
**Sub-Vertical:** [F&B / 3PL / Building Materials / Big Box Retail]
**Ownership:** [Public / Private / PE-backed]
**Corporate Gate:** [Self-operated / 3PL-operated / Corporate DC — decision at HQ]
**Facility Fit Score: [X]/100**

---

## Executive Summary

[2-3 paragraphs. Open with sub-vertical classification and corporate structure.
Cover: estimated facility size and throughput, primary labor pain signals,
WMS/ERP stack, detected trigger events, and top outreach angle.
Close with recommended first contact and suggested ROI angle.

Example: "[Company] is a privately-held ambient food distributor operating
approximately [X] sq ft of DC space in [city]. Based on [X] open warehouse
picker positions on Indeed and Glassdoor reviews citing 'constant understaffing,'
the labor pain signal is [High/Moderate/Low]. Their WMS appears to be [platform]
based on job posting language. A greenfield facility was announced in [month/year],
creating a [90/180]-day outreach window before the design phase locks. 
Recommended entry point: [VP Operations name] — reached via email + LinkedIn.
Outreach angle: store replenishment throughput at the new [city] DC."]

---

## Facility Snapshot

| Field | Value |
|-------|-------|
| **Company** | [name] |
| **Sub-Vertical** | [F&B / 3PL / Building Materials / Big Box Retail] |
| **Ownership** | [Public / Private / PE-backed] |
| **Revenue Est.** | ~$[X]M (confidence: [H/M/L]) |
| **Primary DC Location(s)** | [city, state] |
| **Est. Facility Size** | ~[X,XXX] sq ft (source: [building permit / press / estimate]) |
| **Est. Annual Throughput** | ~[X]M units/year (directional) |
| **Temperature Zone** | [Ambient / Refrigerated / Frozen / Multi-temp] |
| **WMS Detected** | [platform or "Not detected"] |
| **ERP Detected** | [platform or "Not detected"] |
| **Existing Automation** | [Vendor if detected / "None detected" / "Unknown"] |
| **Open Warehouse Positions** | [X] (as of [date]) |
| **Trigger Event** | [event or "None detected"] |

---

## 1. Company & Facility Overview

[Sub-vertical classification rationale, corporate structure, network size,
facility locations, ownership, revenue estimate methodology]

## 2. Labor Economics Profile

[Open position count and analysis, wage signals, Glassdoor review themes,
geographic labor market context, estimated addressable labor cost]

**Addressable Labor Cost Estimate:**
- Estimated warehouse headcount: [X] pickers/selectors
- Geographic wage rate: ~$[X]/hr loaded
- Estimated annual labor cost: ~$[X]M
- Est. automatable portion (% of picks): [X]%
- Addressable labor cost for automation ROI: ~$[X]M/year

## 3. Technology Stack Assessment

[WMS platform with confidence level, ERP platform, existing automation,
IT infrastructure signals, integration complexity estimate]

**Integration Complexity Rating:** [Low / Medium / High / Very High]
*Rationale: [1-2 sentences — e.g., "SAP EWM with modern API = standard integration; no custom middleware required"]*

## 4. Facility Intelligence

[Clear height estimate, dock door count, lease vs. owned, greenfield/brownfield
classification, automation zone assessment for irregular-SKU sub-verticals]

**Automation Viability Assessment:**
- Facility type: [Greenfield ideal / Brownfield viable / Brownfield constrained]
- Clear height: [confirmed / estimated / unknown]
- Recommended system types for this facility: [AMR / ASRS / GTP / Palletizer / etc.]

## 5. Supply Chain & Logistics Profile

[Network structure, use cases, order profile, channel mix, seasonal peaks,
compliance requirements, e-commerce channel presence]

## 6. Decision Maker Map

| Name | Title | Buying Role | Contact Signal | Priority |
|------|-------|-------------|---------------|----------|
| [name] | [title] | [Economic Buyer / Champion / Technical / Financial] | [LinkedIn active / Email pattern / Phone] | [#1 / #2 / #3] |

**Top Contact for First Outreach:**
- Name: [name]
- Title: [title]
- Rationale: [why this person first]
- Personalization anchor: [specific recent activity, post, conference, tenure event]
- Recommended channel: [email / LinkedIn / phone]

## 7. Competitive Intelligence

[Prior automation deployment detected or not, WCS signals in job postings,
competitor case study check, switching cost assessment]

**Competitive Landscape at This Account:**
| Competitor | Presence | Confidence | Switching Cost |
|-----------|---------|-----------|----------------|
| [vendor] | [In use / Evaluating / Not present / Unknown] | [H/M/L] | [High/Med/Low] |

## 8. Trigger Events (Last 12 Months)

| Trigger | Date/Source | Outreach Window | How to Use |
|---------|------------|----------------|-----------|
| [event] | [date — source] | [Hot/Warm/Cool] | [specific angle] |

---

## Facility Fit Score: [X]/100

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Facility & Volume Fit | [X]/30 | [key evidence] |
| Labor Pain Severity | [X]/25 | [key evidence] |
| Technology Readiness | [X]/20 | [key evidence] |
| Growth & Trigger Signals | [X]/15 | [key evidence] |
| Budget Authority | [X]/10 | [key evidence] |
| **Total** | **[X]/100** | |

---

## Recommended ROI Model Inputs

*To be refined with prospect data in discovery call:*

| Input | Estimated Value | Source | Confidence |
|-------|----------------|--------|-----------|
| Warehouse headcount (pickers) | [X] FTEs | [Indeed postings + industry benchmark] | Medium |
| Annual labor cost (loaded) | ~$[X]M | [Headcount × wage × 1.35] | Medium |
| Annual throughput | ~[X]M units | [Revenue-based estimate] | Low |
| Current pick rate | ~[X] units/hr (industry avg for this sub-vertical) | [WERC benchmark] | Low |
| Error rate | ~[X]% (industry avg) | [Sub-vertical benchmark] | Low |
| Automatable % of picks | ~[X]% | [Product type assessment] | Low |

*Note: All inputs are directional. Actual discovery call data should replace these before presenting an ROI model.*

---

## Top 3 Outreach Angles

1. **[Angle 1]** — Based on: [specific evidence]. First line: "[suggested opening]"
2. **[Angle 2]** — Based on: [specific evidence]. Best for: [which email in sequence]
3. **[Angle 3]** — Based on: [specific evidence]. Use if angles 1–2 don't land

---

*Generated by AI Sales Team — Warehouse Automation Vertical | `/sales robotics research <company>`*
```

---

## Cross-Skill Integration

- Pass findings to `sales-robotics-outreach` for sequence generation — labor pain score and trigger event directly select the outreach framework
- Facility size and throughput estimates → feed into ROI model for Email 1 financial anchor
- WMS detected → informs integration complexity angle and technical champion messaging
- Trigger event → determines Email 1 timing and framework selection (greenfield trigger = Framework 3 immediately)
- Decision maker map → feeds into multi-threading strategy and LinkedIn touchpoint sequence

*Generated by AI Sales Team — Warehouse Automation Vertical | `/sales robotics research <company>`*
