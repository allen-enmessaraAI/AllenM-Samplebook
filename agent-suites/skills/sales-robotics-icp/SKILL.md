# Ideal Customer Profile Builder — Warehouse Automation & Robotics
# Vertical: Warehouse Automation / Industrial Robotics
# Base skill: sales-icp | Patched for: food & beverage, 3PL, building materials, big box retail

## Vertical Context

VERTICAL: Warehouse Automation & Robotics
PRODUCT CATEGORIES SOLD: AMRs (Autonomous Mobile Robots), ASRS (Automated Storage & Retrieval Systems), Goods-to-Person (GTP) systems, palletizing/depalletizing robotics, conveyor & sortation, robotic picking (each-picking arms), automated pallet movers, WCS/WMS integration layers, cold-chain certified automation
SUB-VERTICALS: Food & Beverage (ambient/refrigerated/frozen), 3PL (e-commerce, cold chain, general), Building Materials (heavy/irregular goods), Big Box Retail (store replenishment DCs, e-commerce DCs)
USE CASES: Store replenishment (case picking), D2C/e-commerce fulfillment (each picking), cold chain fulfillment, pallet in/pallet out, returns processing, kitting & VAS, cross-docking
DEAL SIZE RANGE: AMR pilot: $100K–$500K (3–6 month cycle). Mid-size AMR deployment: $500K–$3M (6–12 month cycle). Full ASRS/GTP: $3M–$30M+ (12–24 month cycle). Enterprise automation program: $30M–$200M+ (24–36 month cycle).
ROI FRAMING: Manual pick cost: $0.25–$0.50/unit. Automated pick cost: $0.05–$0.15/unit. Throughput improvement: 2–5×. Error rate: human 0.5–2%; automated 0.01–0.1%. Labor deflation: $3,000–$5,000 cost per warehouse worker turnover.
TERMINOLOGY: pick rate, throughput (units/hour), order accuracy, takt time, SKU count, SKU velocity, storage density, cube utilization, greenfield vs. brownfield, FEFO (First Expired First Out), lot tracking, WMS (Manhattan, Blue Yonder, Körber, SAP EWM, Oracle), ERP (SAP, Oracle, Microsoft Dynamics), TCO, payback period, CapEx, OpEx conversion, MODEX/ProMat, DC (Distribution Center), 3PL, VAS (Value-Added Services), cycle count, receiving, putaway, replenishment, picking, packing, shipping
COMPLIANCE: FSMA (Food Safety Modernization Act — F&B critical), FDA 21 CFR Part 11, OSHA (robot safety zones, ANSI/RIA R15.06), cold chain FDA guidelines, HAZMAT (some building materials), UL/CE robot certification, ISO 10218 robot safety

---

## Purpose

You are the ICP architect for warehouse automation and robotics sales. Unlike SaaS ICP frameworks that focus on employee count and funding rounds, warehouse automation ICP is built around FACILITY PROFILE — the physical characteristics of the building, the product characteristics of what's stored and moved, the labor economics, and the technology readiness of the existing WMS/ERP stack. A company with $1B in revenue and the wrong product type (e.g., all oversized irregular items) is a worse prospect than a $200M food distributor with high-velocity ambient SKUs in a 250,000 sq ft facility.

---

## Step 1: Sub-Vertical Classification

Before scoring, classify the prospect into one of four sub-verticals. Each has distinct automation use cases and buying dynamics:

### Sub-Vertical 1: Food & Beverage

**Who:** F&B manufacturers (ambient, refrigerated, frozen), F&B distributors, grocery DCs, beverage companies, cold chain logistics

**Why they automate:** Labor in freezer environments has 100%+ annual turnover. FEFO compliance requires systematic lot rotation that humans perform inconsistently. High-velocity SKUs (case picks of beverages, packaged foods) are ideal for AMR/conveyor automation. FDA FSMA traceability requirements create data integration pressure.

**Automation fit indicators:**
- Frozen or refrigerated facility (highest labor pain, most urgent automation case)
- High-velocity ambient SKUs (100+ daily picks per SKU in top 20% of catalog)
- FEFO management required → lot tracking → WMS integration requirement
- SQF, BRC, or FSMA audit pressure → compliance automation angle
- High seasonal peaks (holiday, summer beverage season)

**Key metrics that matter:** Case picks per hour, FEFO compliance rate, temperature zone integrity, lot traceability accuracy, freezer workforce retention rate

**Unique objection:** "Our product is too irregular/fragile for robotics" — partially valid for some fresh produce; not valid for ambient or frozen packaged goods

**Decision makers:** VP Supply Chain, Director of Logistics/Warehouse Operations, VP of Quality (FSMA lens), VP Manufacturing (if vertically integrated)

---

### Sub-Vertical 2: 3PL (Third-Party Logistics)

**Who:** National 3PLs (GXO, Geodis, Ryder), regional 3PLs, e-commerce-focused 3PLs (Radial, Quiet Logistics), cold chain 3PLs (Lineage Logistics, Americold, US Cold Storage)

**Why they automate:** Automation is a competitive differentiator for winning client contracts — automated 3PLs command 15–25% premium pricing and offer SLA guarantees that manual operations can't match. Client contract lengths (3–5 years) justify automation investment horizon. Labor is 60–70% of 3PL operating cost.

**Automation fit indicators:**
- e-Commerce fulfillment as primary or growing service line (high each-pick volume)
- Multiple clients in same facility (multi-tenant flexibility requirement)
- Long-term client contracts in place (3+ year agreements = ROI justification)
- Currently marketing "tech-enabled" or "automated" services to win RFPs
- Hiring "automation engineer" or "robotics specialist" on Indeed
- Actively bidding on new client contracts where automation is an RFP requirement

**Key metrics that matter:** Cost per unit (CPU), order accuracy SLA, orders per hour, on-time ship rate, client onboarding speed, SQFT utilization per client

**Unique consideration:** Multi-client WMS integration — the automation layer must integrate with multiple client ERP/WMS systems simultaneously. Integration complexity is the #1 technical objection in 3PL.

**Decision makers:** VP Operations, Chief Commercial Officer (sell it to win contracts), Director of Engineering, CFO (OpEx conversion play — automation as a service)

---

### Sub-Vertical 3: Building Materials

**Who:** Building materials distributors (Ferguson, Waxman, ABC Supply, BlueScope), lumber/panel distributors (Boise Cascade, LP Building Products), hardware distributors, specialty contractors supply

**Why they automate:** High mix of small parts (fittings, screws, fasteners, connectors) that are labor-intensive to pick. Store replenishment for big box customers (Home Depot, Lowe's, Ace Hardware) requires consistent throughput and accuracy. Contractor will-call urgency creates throughput pressure during peak construction season.

**Automation fit indicators:**
- High SKU count with large proportion of small-parts items (C and D class SKUs)
- Store replenishment as primary channel (regular high-volume orders to retail customers)
- Seasonal construction peak (spring/summer surge 3–4× baseline volume)
- Hiring "warehouse picker" or "order selector" positions on Indeed
- Current pick rate is below 80 units/hour per associate
- Growing e-commerce/digital ordering channel creating new each-pick volume

**Key metrics that matter:** Lines per order, pick rate (units/hour), pick accuracy, will-call turnaround time (contractor waits = lost sales), truck load time

**Unique challenge:** Irregular and heavy items (pipe, lumber, drywall) cannot be automated with standard AMRs — automation fit is only for the small parts / fastener / fitting portion of the catalog. Facility zoning (automatable vs. non-automatable zones) is critical to scoping.

**Decision makers:** VP Operations, Director of Distribution/Logistics, VP of IT (WMS integration), COO (for mid-size private distributors)

---

### Sub-Vertical 4: Big Box Retail / Distribution

**Who:** Big box retailer DCs (Home Depot, Lowe's, Target, Walmart, Costco, Ace Hardware), specialty retail DCs (PetSmart, Chewy, Williams-Sonoma), grocery retail DCs

**Why they automate:** Store replenishment automation improves on-shelf availability. E-commerce DC automation handles increasing each-pick volume. Labor is the #1 cost in distribution. Speed-to-shelf is a competitive metric (faster replenishment = more revenue per store).

**Automation fit indicators:**
- Regional DC serving 100+ store locations
- Growing e-commerce channel requiring dedicated each-pick capacity
- Known CAPEX planning cycle for distribution network modernization
- Annual distribution conference/investor day where "supply chain efficiency" is mentioned
- Peak season failure in prior year (holiday stock-out events → urgent automation evaluation)
- ESG/sustainability initiative involving logistics optimization

**Key metrics that matter:** Units per hour (UPH), truck turns per day, store fill rate, on-time delivery to stores, e-commerce same-day cutoff, returns processing time

**Unique buying dynamic:** Big box retailers are extremely sophisticated buyers — they've evaluated everything and will run a competitive RFP. Pilot program requirement is non-negotiable. Decision is made centrally by VP/SVP Supply Chain, not at the DC level.

**Decision makers:** SVP/VP Supply Chain, VP Distribution Operations, VP IT/CIO, CFO (CapEx approval at enterprise level)

---

## ICP Firmographic Criteria

| Criteria | Ideal Range | Why It Matters | Red Flag If Missing |
|----------|------------|----------------|---------------------|
| **Facility size** | 100,000–1,000,000 sq ft (primary DC) | Below 100K = ROI rarely justified. Above 1M = likely already automated or has in-house engineering team | Under 50,000 sq ft = micro-operation, disqualify |
| **Annual throughput** | 500K–50M+ units/year | Throughput × labor cost = the automation ROI numerator | Under 200K units/year = payback period exceeds 10 years for most systems |
| **Revenue** | $50M–$10B (varies by sub-vertical) | Revenue = budget proxy. F&B $100M+; 3PL $50M+; BB retail $500M+ | Under $20M revenue = no CapEx budget for automation |
| **Warehouse labor headcount** | 50–2,000 warehouse associates | Labor headcount × avg wage = the cost base automation replaces | Under 30 associates = too small; over 2,000 = likely already invested |
| **Company type** | Private or public industrial/logistics company | Private = faster decisions, simpler approval. Public = larger budget but longer procurement | Consumer startup building first warehouse = no operational expertise for integration |
| **WMS in place** | Manhattan, Blue Yonder, Körber, SAP EWM, Oracle WMS | WMS presence = integration maturity. No WMS = foundational gap (fix WMS first) | No WMS = high implementation risk; must solve WMS layer first |
| **Geography** | North America primary (US + Canada); Western Europe secondary | Proximity for implementation support and service response | Emerging markets without local service infrastructure = execution risk |
| **Facility age / type** | 5–25 years old (brownfield viable) or new construction (greenfield ideal) | Greenfield = best automation ROI; brownfield = ceiling heights and structural specs matter | Historical buildings with <24-ft clear height = many ASRS systems incompatible |

---

## ICP Technographic Signals

**Technology readiness levels for warehouse automation buyers:**

| Tech Category | Ideal Signal | Risk Signal | Disqualifier |
|--------------|-------------|-------------|--------------|
| **WMS** | Manhattan WMS v6+, Blue Yonder, Körber (HighJump), SAP EWM — modern API-capable | Legacy AS400-based WMS (IBM iSeries) — integration possible but complex | No WMS at all — automation without WMS is operationally dangerous |
| **ERP** | SAP S/4HANA, Oracle Cloud, Microsoft Dynamics 365 — API-first | SAP ECC 6.0 (on-premise, end of mainstream support) | Custom-built legacy ERP with no API layer — integration will block project |
| **Connectivity** | Wi-Fi 6 or industrial-grade wireless infrastructure in place | Single-band Wi-Fi with dead zones | No industrial wireless in facility — must be budgeted separately |
| **Existing automation** | Conveyor, sortation, or forklift fleet in place — automation-ready culture | Manual-only operations with no automation history | Actively hostile to technology (union agreement explicitly restricts automation) |
| **Data availability** | WMS generates pick data, SKU velocity reports, order history — can be pulled for ROI modeling | Manual spreadsheet tracking only | No historical data available for ROI model = sales cycle extends significantly |
| **IT organization** | Dedicated IT team with OT (Operational Technology) experience; automation engineer on staff or being hired | IT team exists but has no warehouse/OT experience — integration will require external support | No IT department — every integration is a services engagement |

---

## ICP Pain Point Map

### Pain 1: Warehouse Labor Crisis — **CRITICAL**

**Manifestation:** Cannot fill open positions even at elevated wages. Using temp agencies at 1.5–2× the cost of FTE. Turnover exceeds 80%/year in ambient; 120%+ in frozen. Training cost per new hire: $3,000–$5,000. Operations supervisor time consumed by hiring instead of managing throughput.

**Business impact:** $500K–$5M+ annual labor premium for large facilities. Throughput variability destroys SLA adherence. Peak season requires 2–3× temporary labor at highest cost.

**Trigger events:** Local minimum wage increase announcement; NLRB or union organizing activity; consecutive seasons of staffing failure; competing employer (Amazon, Walmart DC) opening nearby.

**Current workaround:** Temp agencies, sign-on bonuses, wage increases — all increase OPEX without solving the structural problem.

**Automation angle:** Direct labor cost reduction and throughput predictability. ROI model: (current annual labor cost) × (% of picks automatable) × (labor cost delta after automation) = annual savings.

---

### Pain 2: Throughput Ceiling — **CRITICAL**

**Manifestation:** Peak season demand consistently exceeds facility capacity. Business is growing but the warehouse is the bottleneck. Manual operations can't scale linearly beyond current floor space. Customers or stores receive partial fills or late shipments during peak.

**Business impact:** Revenue is limited by warehouse throughput. Partial fills cause deductions from retail customers. Late shipments trigger SLA penalties in 3PL contracts. New business is turned away because the facility can't handle more volume.

**Trigger events:** Signing a major new retail account; e-commerce channel launch; acquisition of a new business unit; M&A integration requiring network consolidation.

**Current workaround:** Expanded shift coverage (2nd or 3rd shift), adding more pickers — but labor isn't available at the rate needed.

**Automation angle:** Throughput multiplier (2–5× pick rate improvement). Automation runs 3 shifts without overtime. Present as a revenue enabler, not just a cost reducer.

---

### Pain 3: Order Accuracy & Compliance — **HIGH**

**Manifestation:** Pick error rate of 0.5–2% creates customer chargebacks (retail), recall exposure (F&B), and returns processing cost. FEFO compliance requires manual lot date checking — associates skip it under throughput pressure. FDA FSMA audit findings tied to traceability gaps.

**Business impact:** Each 0.1% error rate at 1M daily picks = 1,000 errors × average cost of $15–$50 per error (pick, repack, reship, credit) = $15K–$50K/day in error cost. Retail customer chargebacks can be 1–2% of invoice value. FSMA non-compliance can trigger facility closure.

**Trigger events:** Failed retail audit with chargeback notice; FDA FSMA audit finding; major recall event in the industry (peer company recall creates urgency); new retail customer RFP requiring 99.9%+ accuracy SLA.

**Automation angle:** Automated systems achieve 99.9–99.99% accuracy. Automated FEFO logic enforced at the system level regardless of throughput pressure.

---

### Pain 4: Space Utilization / Real Estate Pressure — **HIGH**

**Manifestation:** Current facility is at 90%+ capacity utilization. Considering leasing additional space (expensive) or building a new facility. Cost of warehouse real estate in key markets has increased 30–50% since 2020.

**Business impact:** Additional facility adds fixed cost without proportional revenue. Dual-facility operations create split inventory and transportation complexity. New construction or greenfield costs $100–$200/sq ft.

**Trigger events:** Lease renewal at significantly higher rate; facility capacity analysis showing <6 months runway at current growth; expansion announcement in adjacent market.

**Automation angle:** ASRS systems increase storage density 3–5× vs. conventional racking. Automation can defer or eliminate a facility expansion decision. Present as real estate cost avoidance with 5-year NPV calculation.

---

### Pain 5: Visibility & Inventory Accuracy — **MEDIUM**

**Manifestation:** Cycle count accuracy below 98%. Inventory shrinkage (theft, miscount, misplacement). Real-time inventory position unknown without manual spot checks. Order promising reliability is low because inventory records drift from physical reality.

**Business impact:** Safety stock required to buffer inaccuracy = working capital tied up. Stockouts despite having inventory on hand. Oversells requiring cancellations damage customer relationships.

**Current workaround:** Frequent full physical inventory counts (1–4x/year) that shut down operations. Paper-based cycle count programs that aren't consistently executed.

**Automation angle:** Automated systems provide real-time inventory position by location. Put-away and retrieval are system-directed, not human-directed — location accuracy is system-enforced.

---

## ICP Scoring Rubric

**Total: 100 points**

### Facility & Volume Fit (30 pts) — Highest weight because it's the hardest to change

| Score | Criteria |
|-------|----------|
| 27–30 | 250,000+ sq ft facility. Annual throughput >2M units. Multiple temperature zones or complex product mix. WMS confirmed in place. Warehouse headcount 100+. |
| 20–26 | 100K–250K sq ft. 500K–2M units/year. Single temperature zone. WMS in place. 50–100 warehouse associates. |
| 12–19 | 50K–100K sq ft. 200K–500K units/year. Basic WMS or spreadsheet tracking. 25–50 associates. |
| 5–11 | Under 50K sq ft or throughput cannot be estimated. WMS absent or unclear. Under 25 warehouse associates. |
| 0–4 | Facility details unknown and no public signals available. Company appears too small. |

### Labor Pain Severity (25 pts) — Primary buying trigger in this vertical

| Score | Criteria |
|-------|----------|
| 22–25 | Hiring 10+ warehouse/picking positions on Indeed. Reviews mention "high turnover" or "understaffed." Located in tight labor market (urban DC, logistics hub). Frozen/refrigerated facility (highest labor pain). |
| 16–21 | Hiring 3–9 warehouse positions. Indirect labor pain signals (agency temp use mentioned). Mid-tier labor market. |
| 9–15 | 1–2 open positions. Labor market is neutral. Pain is inferred from sub-vertical norms, not confirmed. |
| 3–8 | No open warehouse positions. Region has loose labor market. No pain signals found. |
| 0–2 | Company appears fully staffed. Active labor relations (union) that may complicate automation. |

### Technology Readiness (20 pts) — Integration risk gating

| Score | Criteria |
|-------|----------|
| 17–20 | Modern WMS (Manhattan v6+, Blue Yonder, SAP EWM, Körber) confirmed. ERP is SAP S/4 or Oracle Cloud. IT team with OT experience. Wi-Fi or connectivity infrastructure confirmed. |
| 12–16 | WMS in place but older version or mid-tier platform. ERP is SAP ECC or Oracle on-premise. IT team exists but limited OT experience. |
| 6–11 | WMS exists but cannot be confirmed. No ERP identified. Integration pathway unclear. |
| 2–5 | No WMS confirmed. Likely on manual or spreadsheet operations. Integration would require WMS deployment first. |
| 0–1 | No WMS, no ERP, no IT infrastructure signals. Requires foundational technology layer before automation is viable. |

### Growth & Trigger Signals (15 pts) — Creates urgency

| Score | Criteria |
|-------|----------|
| 13–15 | Greenfield facility announced, new DC lease, e-commerce channel launch, recent M&A, or WMS implementation announced in last 90 days. |
| 9–12 | 1 growth signal in last 6 months (expansion, new client, peak season failure mentioned in trade press). |
| 5–8 | Sub-vertical growth trend applies but no specific company signal. Company revenue growing 10%+ based on available signals. |
| 2–4 | Stable operation, no growth signals detected. |
| 0–1 | Declining revenue signals, cost-cutting mode, or negative press. |

### Budget Authority & CapEx Signals (10 pts) — Deal viability gate

| Score | Criteria |
|-------|----------|
| 9–10 | Public company with CapEx line in 10-K or investor day discussion of distribution investment. OR private company with recent announcement of facility expansion (implies CapEx approval). Decision maker title is VP/SVP or C-suite. |
| 6–8 | Private company with 1+ growth signals suggesting CapEx availability. VP-level contact identified. |
| 3–5 | Private company, financial signals unclear, Director-level contact. |
| 0–2 | No budget signals. Only manager-level contacts. No CapEx indicators. |

**Grade Bands:**
- **A+ (90–100):** Large facility, confirmed labor crisis, modern WMS, hot trigger event. Assign senior AE immediately. Custom ROI model within 72 hours.
- **A (75–89):** Strong facility and pain signals, good tech readiness, at least one trigger. Personalized outreach within 48 hours. Invest in facility analysis.
- **B (60–74):** Qualified facility, some pain signals, moderate tech readiness. Standard outreach sequence. Monitor for trigger events.
- **C (40–59):** Marginal fit — facility may be too small or tech readiness too low. Nurture only. Re-score in 90 days.
- **D (0–39):** Does not fit ICP. Disqualify or monitor for 12+ months.

---

## Negative ICP — Disqualification Criteria

| Disqualifier | Red Flag Signal | Why It Disqualifies |
|-------------|----------------|---------------------|
| Facility under 50,000 sq ft | Small building, low headcount | ROI math doesn't work — payback period exceeds 7+ years; deal too small |
| Under 200,000 units/year throughput | Low volume estimate from revenue/industry data | Automation cannot generate sufficient cost savings to justify CapEx |
| No WMS in place | No WMS mentioned in job postings; no tech stack signals | Automation without WMS creates inventory chaos — must solve WMS first |
| Primarily irregular/oversized product only | All SKUs are pallets, lumber, machinery, bulk materials | Current robotics cannot handle these SKUs; system integrator, not AMR/ASRS play |
| Active labor union with restrictive agreements | UAW, Teamsters agreements that explicitly prohibit automation or require headcount maintenance | Legal barrier to automation deployment; multi-year political hurdle |
| Company in financial distress | Layoff announcements, Chapter 11 search results, credit rating downgrades | No CapEx budget; deal will die at CFO approval |
| Less than 18 months old | Newly founded; first facility being built | No operational data for ROI model; no existing pain to solve; too early |
| Acquisition announcement pending | Being acquired, merger announced | Decision-making frozen; new ownership will restart evaluation |
| Geographic location with no service coverage | Remote areas outside implementation partner reach | Installation and ongoing maintenance requires local service infrastructure |
| Deeply locked with a direct competitor | Recent ASRS/AMR installation just completed | Switching costs too high; 5–10 year depreciation commitment; no urgency |

---

## Buyer Personas

### Persona 1: "The Operational VP Under Fire" — VP of Supply Chain / VP of Operations

**Profile:** 42–55 years old. Promoted into VP role after 15+ years in operations. Grew up on the warehouse floor. Strong operational intuition but increasing pressure from CEO to "modernize." Manages 3–5 direct reports (DC managers, transportation director, S&OP manager). Reports to COO or CEO.

**Day-in-the-life:** Morning: reviews last night's shipping report and fill rates. Spends 60% of day in firefighting mode — staffing gaps, carrier issues, customer escalations. Tries to block time for strategic projects (automation evaluation) but it keeps getting displaced. Friday afternoons are for industry reading (DC Velocity, Supply Chain Dive).

**KPIs they're measured on:** Fill rate, on-time shipping, cost per unit, inventory accuracy, headcount budget.

**Pain in their words:** "I can't keep up with the hiring. We onboard 20 people and 15 quit within 90 days." / "My Q4 plan requires 300 temps and the agency can only get me 220." / "The CEO keeps asking me why we're not automating. I don't have a good answer."

**Information diet:** DC Velocity, Supply Chain Dive, MHI (Material Handling Institute) publications, WERC (Warehouse Education and Research Council), LinkedIn peers, industry peer groups (CSCMP, WERC chapter), MODEX/ProMat conference sessions.

**Messaging that resonates:** Lead with their specific throughput or labor pain (use their industry benchmarks). Frame automation as giving them back operational control, not taking away jobs. Reference a peer company in their sub-vertical that has deployed successfully. Show payback period in years and labor headcount reduction in FTE-equivalents, not percentages.

**Subject lines for this persona:** "your Q4 labor plan" / "what [competitor] did about warehouse staffing" / "throughput question for your DC in [city]"

**What turns them off:** Vendor-speak ("our industry-leading platform"). Overpromising ("fully automated in 6 months"). Not knowing basic warehouse operations terminology. Calling it "innovative" without citing numbers.

---

### Persona 2: "The ROI Gatekeeper" — CFO / VP Finance

**Profile:** 45–58 years old. Background in corporate finance or accounting. Sees every capital project through the lens of payback period, IRR, and NPV. Has been burned before by capital projects that overran budget or underdelivered savings.

**Day-in-the-life:** Spends mornings on P&L reviews, investor calls, and treasury. Afternoon on CapEx review committee meetings. Skeptical of every vendor ROI model ("they always show what I want to see").

**KPIs they're measured on:** EBITDA, CapEx to revenue ratio, labor cost as % of revenue, inventory turns, OpEx budget variance.

**Pain in their words:** "Show me the actual labor savings, not the potential savings." / "What happens to utilization if volume drops 20%?" / "How long before we break even? And what are the implementation risks that could extend that?"

**Messaging that resonates:** Conservative ROI model with documented assumptions. Show sensitivity analysis (what if volume drops 15%?). Reference customer examples with signed audited results, not vendor case studies. Frame automation as OpEx conversion (from variable labor to fixed depreciation) — this matters on EBITDA. Address what happens at contract end (asset value, refresh cycle).

**Subject lines for this persona:** "the build vs. buy question for [company] logistics" / "CapEx model for [sub-vertical] automation — 30-minute review?" / "what [peer company] found after 3 years"

**What turns them off:** ROI models with "up to" language. Avoiding questions about implementation overruns. Framing payback as "2–3 years" without showing the math.

---

### Persona 3: "The Technical Champion" — Director of Engineering / Automation Manager / DC General Manager

**Profile:** 35–48 years old. Often the person who championed automation evaluation and found your company. Highly credible internally — the VP listens to them on technical matters. Can be the internal champion who builds the business case and navigates internal approval.

**Day-in-the-life:** Reviews system performance dashboards, manages maintenance and facilities team, evaluates vendors, runs pilot programs, writes capital appropriation requests.

**KPIs they're measured on:** System uptime, pick rate, order accuracy, maintenance cost, implementation timeline adherence.

**Pain in their words:** "I know automation is the right answer but I can't get the VP to prioritize it." / "We evaluated two vendors and their integration with our WMS was terrible." / "I need to build a business case the CFO will approve and I've never done that before."

**Messaging that resonates:** Deep technical credibility (know WMS integration specs cold, know their WMS by name). Reference specific robot models and throughput specs for their use case. Offer to help them build the internal business case (give them the ROI model they can present upward). Respect their expertise — they know more about their operation than you do.

**Subject lines for this persona:** "WMS integration for [Manhattan/Blue Yonder] — quick question" / "throughput calc for your [pick/palletize] operation" / "business case template — [sub-vertical] automation"

**What turns them off:** Oversimplifying the technical complexity. Saying integration is "easy" without specifics. Not knowing your own product's technical specifications.

---

## Prospecting Playbook

### Where to Find Warehouse Automation Prospects

**Trade publications (monitor weekly):**
- DC Velocity (dcvelocity.com) — "new facility" announcements, automation case studies
- Supply Chain Dive (supplychaindive.com) — industry news, M&A, company expansions
- Modern Materials Handling (mmh.com) — product news, facility profiles
- Food Logistics (foodlogistics.com) — F&B supply chain news
- Logistics Management (logisticsmgmt.com) — 3PL and retail DC news

**Conference targeting:**
- MODEX (biennial, March, Atlanta) and ProMat (biennial, Chicago) — the two largest material handling shows. Exhibitor list = vendors (not prospects). ATTENDEE list = prospects.
- WERC Annual Conference (WERC.org) — warehouse operations professionals
- CSCMP Edge Conference — supply chain executives
- GMA (Grocery Manufacturers Association) — F&B executives
- IWLA Annual Conference — 3PL executives
- NRHA (North American Retail Hardware Association) — building materials/hardware distribution

**LinkedIn search strategies:**
```
Title: "VP Supply Chain" OR "Director of Logistics" OR "Director of Distribution" AND 
Industry: "Food & Beverage" OR "Warehousing and Storage" OR "Logistics and Supply Chain"
Company Size: 201–10,000 employees

Title: "VP Operations" AND "3PL" OR "third-party logistics" OR "fulfillment"

Title: "Director of Engineering" AND "distribution" OR "warehouse" OR "fulfillment"

Title: "Automation Manager" OR "Director of Automation" AND warehouse OR distribution
```

**Google Search operators for greenfield signals:**
```
"distribution center" "breaking ground" OR "new facility" site:supplychaindive.com [year]
"[company name]" "new warehouse" OR "new DC" OR "new distribution center"
"[city]" "warehouse" "building permit" "[square feet]"
"[company name]" "expand" OR "expansion" "distribution" -[your company name]
```

**Indeed monitoring (labor pain signal — most important trigger):**
- Set weekly alert: "warehouse picker" OR "order selector" OR "forklift operator" in target geographies
- Companies posting 10+ warehouse positions simultaneously = priority prospect
- Postings with "competitive wages," "sign-on bonus," or "weekend differential" = labor crisis signal

**Greenfield Detection Sources:**
- CoStar (commercial real estate database) — new warehouse permits and leases
- Dodge Data & Analytics — construction project database
- state/county building permit portals — search for industrial permits over 100,000 sq ft
- Industrial real estate brokers (CBRE, JLL, Prologis press releases)
- Area Development magazine — corporate facility announcements

**Disqualification speed check (60-second rule):**
1. What is the facility size? (Under 50K sq ft → disqualify)
2. What is the WMS? (No WMS → qualify only if greenfield with budget to implement WMS)
3. Is the product automatable? (All pallets / all irregular/oversized → wrong product for most systems)
4. Is labor a pain signal visible? (No open warehouse positions + stable reviews → low urgency)
5. Is there a decision maker reachable? (No VP/Director contact findable → low contact access score)

---

## Competitive Context

**Primary competitors the sales team will encounter:**

| Competitor | Target Segment | Differentiator | Vulnerability |
|-----------|---------------|----------------|---------------|
| **Dematic (KION Group)** | Enterprise ($5M+ projects), F&B, retail | Full system integration; global service network | Long implementation timelines; less flexible for brownfield; expensive |
| **Locus Robotics** | e-Commerce 3PL, mid-market ($500K–$3M) | AMR speed to deploy; SaaS/RaaS model | Single-use case (each-picking); WMS integration requires Locus WCS layer |
| **AutoStore** | High-density storage; pharma, retail, 3PL | Extreme storage density (4–6× conventional); proven technology | High cost per bin; requires greenfield or major retrofit; cold chain limitations |
| **6 River Systems (Shopify)** | 3PL, e-commerce, omnichannel retail | Chuck robots; fast deployment; Shopify ecosystem integration | Post-acquisition uncertainty; less enterprise sales support |
| **Vanderlande (Toyota)** | Airports, parcel, retail DC | Conveyor/sortation leader; strong service network | Less flexible for AMR/GTP; large minimum engagement |
| **Berkshire Grey (SoftBank)** | Retail, 3PL, e-commerce — AI-picking arm | AI-based piece picking; handles irregular items | Early technology maturity; high cost; limited throughput for high-volume operations |
| **Geekplus** | 3PL, e-commerce — AMR | Cost-competitive AMRs; fast deployment | US service network less developed; WMS integration documentation quality |

**Common displacement scenarios:**
- Replacing manual operations entirely (no prior automation)
- Replacing aging conveyor/sortation systems (ROI on modernization)
- Expanding successful pilot to full deployment (most common for AMR)
- Replacing failed competitor deployment (AutoStore or early AMR vendor that underdelivered)

**Market trends accelerating the ICP:**
1. **E-commerce volume permanently elevated post-2020** — every F&B, building materials, and 3PL company now has an e-commerce channel that didn't exist at scale 5 years ago. Each-picking demand is the primary growth driver.
2. **Warehouse labor structural shortage** — BLS data shows warehouse/fulfillment labor demand is growing 3× faster than supply. This is not cyclical — it's structural.
3. **IRA (Inflation Reduction Act) Section 45X manufacturing credits** — US-made automation equipment now eligible for domestic production credits, improving US automation economics vs. imports.

---

*Generated by AI Sales Team — Warehouse Automation & Robotics Vertical | `/sales robotics icp`*
