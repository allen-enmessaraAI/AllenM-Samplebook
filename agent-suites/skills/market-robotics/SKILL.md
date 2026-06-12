# AI Marketing Suite — Warehouse Automation & Robotics
# Vertical: Warehouse Automation / Industrial Robotics
# Base skill: market | Patched for: automation vendors, robotics manufacturers, material handling integrators

## Vertical Context

VERTICAL: Warehouse Automation & Robotics (B2B industrial marketing)
MARKETING CLIENT TYPES: AMR (autonomous mobile robot) vendors, ASRS system manufacturers, WCS/WMS software providers, system integrators, robotics-as-a-service (RaaS) platforms, material handling solution providers
WHAT THIS SKILL DOES: Builds and audits marketing strategies FOR warehouse automation companies — not marketing TO automation prospects as sales targets. When an automation vendor hires you to run their marketing, this skill drives the strategy, content engine, channel mix, and ABM framework.
PRIMARY MARKETING GOAL: Enterprise pipeline generation + thought leadership in the supply chain / distribution center community + competitive differentiation in a market where most buyers don't know the difference between vendor solutions
BUYER JOURNEY: Long (12–24 months from first touch to signed contract). Marketing's job is to be present at the awareness stage, build credibility during evaluation, and provide CFO-grade ROI content for the approval stage. This is not a demand-gen sprint — it is a sustained account-based marketing program.
COMPLIANCE CRITICAL: Customer case studies require written permission from the customer before any name or metric can be used publicly. Most Fortune 500 customers will not allow naming. Ghost case studies (unnamed, geography/size described only) are the norm.
TERMINOLOGY TO USE: throughput, pick rate, order accuracy, labor cost per pick, TCO, payback period, CapEx, greenfield, brownfield, AMR, ASRS, GTP, WMS integration, MODEX, ProMat, DC Velocity, Supply Chain Dive, Modern Materials Handling, 3PL, F&B, building materials, big box retail — never use "optimize," "leverage," "synergy," "seamlessly," "cutting-edge," or "industry-leading" — supply chain professionals instantly tune these out
MARKETING BUDGET BENCHMARK: B2B industrial technology companies typically invest 5–10% of ARR in marketing. Trade show presence (MODEX, ProMat) alone can represent $50K–$500K per event. Content marketing and thought leadership should represent 30–40% of total marketing budget.

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full automation vendor marketing audit | ROBOTICS-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second brand snapshot | Terminal output |
| `/market copy <url>` | Website copy optimization for B2B industrial | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Executive ABM email sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | LinkedIn + trade publication content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | LinkedIn Ads + Google B2B strategy | AD-CAMPAIGNS.md |
| `/market funnel <url>` | Enterprise pipeline funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Competitive positioning analysis | COMPETITOR-REPORT.md |
| `/market content <topic>` | Thought leadership content strategy | CONTENT-STRATEGY.md |
| `/market launch <product>` | New product / solution launch playbook | LAUNCH-PLAYBOOK.md |
| `/market proposal <company>` | Client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full automation vendor marketing report | ROBOTICS-MARKETING-REPORT.md |
| `/market abm <target-list>` | Account-Based Marketing program build | ABM-PROGRAM.md |
| `/market tradeshow <event>` | Trade show program strategy | TRADESHOW-PLAYBOOK.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. For sub-skill commands, use the warehouse automation vertical context to override the base skill's generic B2B logic.

### Full Automation Vendor Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with warehouse-automation-specific mandates:

1. **market-content** (automation lens) → Website messaging effectiveness for VP Supply Chain audience; ROI calculator depth; case study quality and specificity; sub-vertical coverage (F&B, 3PL, building materials, big box retail); technical credibility signals; integration documentation visibility
2. **market-conversion** (automation lens) → Demo/site-visit request flow; ROI calculator UX; content gate friction; event registration; contact form quality; response time signals (critical in enterprise B2B — slow response = lost trust)
3. **market-competitive** (automation lens) → Positioning vs. Dematic, AutoStore, Locus, 6 River, Körber; differentiation clarity; sub-vertical messaging; use-case specificity; pricing/ROI transparency vs. competitors
4. **market-technical** (automation lens) → B2B SEO for supply chain searches; LinkedIn presence and follower quality; trade publication citation signals; structured data; domain authority vs. competitors
5. **market-strategy** (automation lens) → ABM program presence; trade show participation; thought leadership program; partner/integrator channel; content marketing funnel depth; customer reference program maturity

---

## Warehouse Automation Vendor Marketing Score — Weighted Categories

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Thought Leadership & Content | 30% | LinkedIn authority, trade press citations, white papers, ROI calculators, technical depth |
| Website & Messaging Clarity | 25% | VP Supply Chain-grade messaging, sub-vertical specificity, use-case clarity, case study quality |
| Account-Based Marketing & Pipeline | 20% | ABM program maturity, trade show presence, executive outreach infrastructure, intent data usage |
| Competitive Differentiation | 15% | Clear differentiation from top 5 competitors, positioning specificity, win/loss narrative |
| Partner & Reference Program | 10% | System integrator relationships, customer reference library, co-marketing activity |

> Note: Thought Leadership carries 30% weight because VP Supply Chain buyers make automation decisions based on whom they trust as the authoritative voice in their sub-vertical. Brand awareness in trade media and LinkedIn is a prerequisite to being included in an RFP, not a nice-to-have.

---

## Phase 1: Vendor Classification & Discovery

### 1.1 Automation Vendor Classification

Before any analysis, classify the automation vendor:

| Vendor Type | Signals | Marketing Implications |
|------------|---------|------------------------|
| **AMR platform vendor** | AMR hardware + fleet management software, RaaS model, mid-market | LinkedIn-first, case studies by industry, ROI calculator, trade show presence at MODEX/ProMat |
| **ASRS / High-density storage** | AutoStore, vertical lift modules, horizontal carousels, cube storage | Long sales cycle, engineering-grade content, CapEx justification tools, greenfield focus |
| **Full MHE / system integrator** | Conveyor, sortation, pick-to-light, multi-system deployments | Solution-selling content, reference architecture, system design capabilities |
| **WCS / WMS software vendor** | Warehouse control or management software, automation orchestration | Integration-depth content, IT/Director of Engineering audience, partner ecosystem |
| **RaaS / OpEx model** | Monthly subscription for AMR capacity, no CapEx | CFO-friendly messaging, OpEx vs. CapEx calculator, cash flow impact content |
| **Emerging robotics startup** | Series A/B, limited customer base, specific niche | Thought leadership to punch above weight, early adopter positioning, proof-of-concept marketing |

### 1.2 Sub-Vertical Presence Check

Assess presence and messaging quality in each of the four core sub-verticals:

| Sub-Vertical | Relevant Audience | Marketing Must-Haves |
|-------------|------------------|---------------------|
| **Food & Beverage** | Food distributors, beverage companies, grocery DCs | FEFO/lot tracking case studies, FDA/FSMA awareness, temperature zone content, cold chain ROI |
| **3PL** | Third-party logistics operators | Multi-client WMS integration content, RFP competitiveness angle, SLA-based ROI framing |
| **Building Materials** | Hardware, lumber, HVAC/plumbing distribution | Irregular SKU handling content, zone automation approach, contractor-urgency seasonality |
| **Big Box Retail** | Retailer DCs, store replenishment, e-commerce fulfillment | Peak season throughput content, omnichannel case studies, corporate procurement process content |

---

## Phase 2: Channel Strategy for Automation Vendors

### 2.1 Channel Priority

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **LinkedIn (Organic + Paid)** | Primary B2B awareness and executive engagement channel — VP Supply Chain is highly active on LinkedIn | Critical | $2K–$15K/month (paid); significant organic investment |
| **Trade Shows (MODEX, ProMat)** | Highest-intent lead generation in the industry — booth presence = credibility signal | Critical | $50K–$500K per event (booth, sponsorship, travel, content) |
| **Content Marketing / Trade Press** | DC Velocity, Supply Chain Dive, Modern Materials Handling — being cited builds pre-RFP authority | High | $5K–$20K/month (content team + PR agency) |
| **Email (Account-Based)** | Targeted, personalized outreach to named accounts in ICP — not broadcast | High | Low cost; high effort per account |
| **Google Search (B2B)** | Intent-based capture for executives actively researching automation | Medium | $3K–$12K/month |
| **Webinars & Virtual Events** | Top-of-funnel thought leadership; ROI education; sub-vertical-specific content | Medium | $2K–$8K per event |
| **Customer Reference Program** | The most powerful late-funnel tool — peer-to-peer credibility | Critical | Investment in customer success, not just marketing |
| **YouTube / Video** | Product demos, facility walkthroughs, customer testimonials, ROI explainers | Medium | $3K–$10K/month |
| **Podcast Appearances** | Supply chain podcasts (The Logistics of Logistics, Talking Logistics, Supply Chain Now) | Medium | Low cost; high credibility if content is excellent |
| **Partner / Integrator Channel** | System integrators recommend and implement automation — co-marketing is high leverage | High | Co-op marketing budget allocation |

### 2.2 LinkedIn Strategy (Primary Channel)

LinkedIn is the #1 marketing channel for warehouse automation vendors because VP Supply Chain, Director of Logistics, Director of Engineering, and CFO are all highly active on LinkedIn — more so than almost any other executive cohort.

**Company Page Requirements:**
- Banner image: facility photo or system in operation (NOT a product render — too vendor-looking)
- Description: sub-vertical-specific, metric-led ("Customers reduce labor cost by 30–50% in 18-24 months")
- Featured posts: pinned ROI calculator, most compelling case study, upcoming trade show
- Post frequency: minimum 5x/week; ideal 7x/week
- Follower target: 5,000+ in supply chain industry (VP Supply Chain + Director + Engineer titles)

**Content Types by Performance (LinkedIn, supply chain audience):**
| Content Type | Relative Engagement | Best For |
|-------------|---------------------|----------|
| Customer testimonial video (30–90 seconds) | Very High | Pipeline activation, reference building |
| "Before/After" facility transformation visual | High | Awareness, shareable |
| Data-led industry insight post | High | Thought leadership, algorithm boost |
| Trade show recap / live event content | Medium-High | Event-driven pipeline |
| Product feature announcement | Medium | Technical champion audience |
| White paper / case study link | Medium | Late-funnel, content gate leads |
| Job posting shares | Low | Culture content only |
| Generic "we're excited to announce" posts | Very Low | Avoid |

**LinkedIn Thought Leadership Program:**
- Identify 3–5 internal subject matter experts (VP Sales, CTO, Head of Implementation)
- Each expert posts 2–3x/week on supply chain topics — NOT product pitches
- Topics: labor market data, sub-vertical case studies, "what I learned at MODEX," ROI modeling approaches, WMS integration challenges, automation ROI benchmarks
- Employee advocacy: amplify expert posts through company page and team shares

**LinkedIn Paid (Sponsored Content):**
- Audience: Job Title targeting (VP Supply Chain, VP Operations, Director of Distribution, Director of Engineering, CFO) + Company Size 200+ employees + Industry (Warehousing, Food & Beverage, 3PL, etc.)
- Ad formats: Single image (ROI stat), Document Ads (white paper download), Video (case study), Conversation Ads (CEO outreach — use sparingly)
- Budget: $5,000–$15,000/month for meaningful reach
- KPIs: Cost per content download < $80; Cost per demo request < $300

---

## Phase 3: Content Marketing Strategy

### 3.1 Content Pillars for Automation Vendors

| Pillar | Theme | Content Types | Audience | Ratio |
|--------|-------|---------------|----------|-------|
| **Sub-Vertical Intelligence** | Industry-specific research, benchmarks, ROI data for F&B / 3PL / Building Materials / Big Box | Reports, blog posts, LinkedIn thought leadership, webinars | VP Supply Chain (awareness) | 30% |
| **Customer Proof** | Case studies, testimonial videos, ROI results | Named (where approved) or ghost case studies, video testimonials, reference data | All stages — most powerful at evaluation | 25% |
| **Technical Credibility** | WMS integration depth, system architecture, implementation methodology | Integration documentation, technical white papers, reference architecture guides | Director of Engineering, IT | 20% |
| **ROI & Financial Justification** | CapEx business case, payback period models, labor cost analysis | ROI calculators, financial models, CFO-grade white papers | CFO, VP Supply Chain | 15% |
| **Industry Events & Community** | Trade show content, conference recaps, industry association participation | LinkedIn live from events, recap posts, speaker slides | All — awareness and community | 10% |

### 3.2 Trade Press Strategy (DC Velocity, Supply Chain Dive, MMH)

Being cited or featured in trade publications is a prerequisite for being included in enterprise RFPs. Buyers read these publications. A vendor with zero trade press presence is perceived as unproven.

**Target Publications:**
| Publication | Audience | Content Angle |
|------------|----------|--------------|
| **DC Velocity** | DC managers, VP Supply Chain, operations leaders | Case studies, implementation stories, technology comparisons |
| **Supply Chain Dive** | C-suite supply chain leaders | Industry trends, labor market analysis, technology investment angles |
| **Modern Materials Handling** | Engineering, operations, MHE procurement | Technical specs, system design, benchmark studies |
| **Food Logistics** | F&B supply chain specifically | Cold chain automation, FEFO compliance, food safety and automation |
| **3PL Value Creation** | 3PL executives | Multi-client WMS, RaaS models, competitive differentiation for 3PLs |
| **Inbound Logistics** | Logistics and distribution broadly | Cost-per-pick benchmarks, labor market context, ROI case studies |

**Trade Press PR Strategy:**
- Monthly pitch cadence to top 3 publications
- Story angles that get published: labor market data + automation ROI data (editors love numbers), customer case study with specific metrics, novel technology application (first F&B cold chain AMR deployment at scale), industry benchmark study (survey-based data is highly publishable)
- Never pitch "company announces product X" — editors want stories about customers and market impact, not product launches
- Guest byline program: 2 contributed articles per quarter in target publications under SME bylines

### 3.3 White Paper & Report Program

White papers and industry reports are the primary lead generation tool for late-stage enterprise buyers. A VP Supply Chain evaluating automation vendors will download a sub-vertical benchmark report, share it with their team, and associate the vendor with expertise.

**Priority white papers to produce:**
1. **"The True Cost of Warehouse Labor in [Sub-Vertical]: A [Year] Benchmark Study"** — survey-based, specific to one sub-vertical. Lead gen engine for 12+ months.
2. **"WMS Integration Guide for Warehouse Automation"** — technical content that addresses the #1 concern at the Director of Engineering level.
3. **"The CFO's Guide to Automation ROI"** — CapEx justification content tailored to finance audience. Addresses payback period, NPV, and risk mitigation.
4. **"Greenfield vs. Brownfield Automation: What Every DC Manager Needs to Know"** — decision-support content for mid-evaluation stage.
5. **"[Current Year] Warehouse Automation State of the Industry"** — annual flagship report with survey data. Positions vendor as the authoritative industry voice.

**Content gate strategy:**
- White papers: gate with name, company, job title, email (4-field max)
- Blog posts: never gate — SEO value outweighs the lead capture
- ROI calculator: gate the results download only (not the calculator itself)
- Webinar recording: gate with email only (low friction = high volume)

### 3.4 ROI Calculator (Highest Converting Content Asset)

A well-built, publicly accessible ROI calculator is the single highest-ROI content investment a warehouse automation vendor can make. It gives VP Supply Chain a defensible number to take to their CFO without requiring a sales conversation.

**ROI Calculator must include:**
- Inputs: warehouse headcount (pickers), hourly wage, annual throughput, error rate, facility sq footage
- Outputs: Annual labor cost addressable, annual savings estimate, payback period, 5-year NPV
- Sub-vertical selection to apply relevant benchmarks (F&B, 3PL, Building Materials, Retail)
- Email-gated results download (PDF of their specific inputs and outputs)
- "Talk to an expert" CTA from the results page

---

## Phase 4: Account-Based Marketing (ABM) Program

### 4.1 ABM Tier Framework

Warehouse automation is a long-cycle, high-ticket sale that requires ABM — not broadcast demand gen. Segment target accounts into tiers:

| Tier | Account Profile | Marketing Investment | Strategy |
|------|----------------|---------------------|----------|
| **Tier 1 (Named Accounts)** | 50–100 highest-priority accounts; confirmed buying intent or greenfield trigger | $5K–$20K per account/year | 1:1 personalized outreach, custom ROI model, executive gifting, dedicated SDR |
| **Tier 2 (Industry Segment)** | 200–500 accounts in priority sub-verticals with confirmed ICP fit | $500–$2K per account/year | 1:few content; sub-vertical webinars; LinkedIn retargeting by account |
| **Tier 3 (Broad ICP)** | Remaining ICP-fit accounts in addressable market | $50–$200 per account/year | Broad LinkedIn, content marketing, trade show lead capture |

### 4.2 Tier 1 ABM Plays

**Greenfield Play (highest priority):**
- Trigger: Company announces new DC, new DC lease, or facility expansion
- Response within 48 hours: personalized outreach from VP Sales or CEO with specific reference to the announcement
- Content: "Greenfield ROI Model" customized for their sub-vertical and announced facility size
- Follow-on: site visit request, reference customer intro in same sub-vertical

**New VP Hire Play:**
- Trigger: New VP Supply Chain or VP Operations joins the target account
- Response within 30 days: LinkedIn connection + personalized note acknowledging new role
- Content: Sub-vertical state-of-industry report + invitation to exclusive peer roundtable event
- Follow-on: discovery call positioned as "help you benchmark your operation" not "our product pitch"

**Labor Signal Play:**
- Trigger: Target account has 10+ open warehouse positions on Indeed
- Response: outreach from SDR with specific position count reference
- Content: "What [X] open positions is costing you — and what leading [sub-vertical] companies are doing about it"
- Follow-on: ROI calculator pre-populated with their estimated headcount

**MODEX/ProMat Engagement Play:**
- Pre-show: invite Tier 1 accounts to exclusive roundtable dinner or private meeting suite at show
- At show: capture all badge scans, route to AE for same-day or next-day follow-up
- Post-show: personalized "great connecting at MODEX" LinkedIn message within 48 hours

---

## Phase 5: Trade Show Marketing Program

### 5.1 Priority Events

| Event | Frequency | Audience | Investment Range | Priority |
|-------|-----------|----------|-----------------|----------|
| **MODEX** | Biennial (Atlanta) | DC professionals, VP Supply Chain, Directors, Engineers | $100K–$500K | Critical |
| **ProMat** | Biennial (Chicago, alternates with MODEX) | Same as MODEX | $100K–$500K | Critical |
| **WERC Annual Conference** | Annual | Warehouse operations leaders | $20K–$80K | High |
| **CSCMP EDGE** | Annual | C-suite supply chain leaders | $25K–$100K | High |
| **Food Shippers Conference** | Annual | F&B logistics specifically | $15K–$50K | High (F&B focus) |
| **Council of Supply Chain Management Professionals (CSCMP) regional** | Multiple/year | Regional supply chain community | $5K–$20K | Medium |
| **NRF / Retail's Big Show** | Annual (New York) | Big box retail, e-commerce | $50K–$200K | Medium (retail sub-vertical) |

### 5.2 MODEX/ProMat Program (Major Event Playbook)

**Pre-Show (6 weeks out):**
- Publish "What to see at MODEX [year]" blog post → positions as community resource
- LinkedIn campaign: "See us at MODEX Booth [X]" targeting supply chain executives
- Email invitation to Tier 1 and Tier 2 accounts: "Reserve time at our booth / join our private dinner"
- Book speaking slot application (submitted 12+ months in advance)
- Schedule private meeting suite if budget allows ($15K–$40K investment — highest ROI activity at MODEX)

**At Show:**
- Demo station in booth: live AMR demo running continuously, not a video loop
- Staff briefing: every booth rep must know the 3 key stats (current pick rate, labor cost reduction, payback period for your typical customer)
- Badge scanning: every badge scan must have a 30-second qualifying note added immediately
- Private roundtable dinner or reception: 20–30 Tier 1 prospects in same sub-vertical, facilitated by CEO or VP Sales
- LinkedIn live: 2–3 "day at MODEX" videos from the booth floor

**Post-Show (within 72 hours):**
- Personalized LinkedIn connection to every badge scan
- Segmented follow-up email by sub-vertical interest noted at booth
- Hot leads (demo requested, meeting scheduled): AE follow-up within 24 hours
- Warm leads (booth stop, took collateral): sequence enrollment within 48 hours
- Cold leads (badge scan only): educational content sequence, 30-day nurture

---

## Phase 6: Customer Reference Program

### 6.1 Why Reference Program is a Marketing Priority

In warehouse automation, the VP Supply Chain's #1 trust signal is talking to a peer at a similar company who has deployed the system. A well-managed reference program:
- Closes deals that would otherwise go to RFP delay
- Shortens sales cycles by 30–50%
- Generates case studies, testimonials, and trade press features
- Creates advocates who recommend at MODEX/ProMat and LinkedIn

### 6.2 Reference Program Structure

| Tier | Requirements | Benefits to Customer | Marketing Deliverable |
|------|-------------|---------------------|----------------------|
| **Named Reference** | Willing to take peer calls; name used in case study | Priority support, early access to new features, advisory board status | Full case study with metrics, video testimonial, trade press pitch |
| **Unnamed Reference** | Willing to take peer calls; name not used externally | Priority support, renewal discount consideration | Ghost case study, anonymous metric, "customer in [sub-vertical]" reference |
| **Peer Call Only** | Takes peer calls from qualified prospects; no marketing use | Priority support SLA | Prospect intro facilitated by AE |

### 6.3 Case Study Standards

Every case study must contain:
- Company profile (sub-vertical, facility size/scope — even if unnamed)
- Challenge: specific before-state with metrics (pick rate, error rate, labor cost, throughput ceiling)
- Solution: specific system type, use case covered, WMS integrated with
- Results: specific, verified metrics (% pick rate improvement, $ labor cost reduction, payback period months)
- Quote from economic buyer (VP Supply Chain or VP Operations) — not a generic "great partner to work with"

**What kills a case study:**
- Generic language ("improved operational efficiency")
- Missing before/after metrics
- Quote from a mid-level contact, not the economic buyer
- No specificity on facility type, size, or sub-vertical

---

## Phase 7: Website & Messaging Analysis

### 7.1 Website Must-Haves for Automation Vendors

**Homepage above the fold:**
- Headline: metric-specific, not product-describing ("Reduce labor cost by 30–50% in 18 months" NOT "The next generation of warehouse automation")
- Sub-headline: sub-vertical specificity or use-case specificity
- Social proof: "Trusted by X DCs across [sub-verticals]" with logos (where approved)
- Primary CTA: "Calculate your ROI" or "Schedule a site visit" — NOT "Learn More" or "Request a Demo"
- Secondary CTA: relevant case study or industry report download

**Sub-vertical hub pages:**
- One dedicated page per sub-vertical: /food-beverage-automation, /3pl-automation, /building-materials-automation, /retail-distribution-automation
- Each page: sub-vertical-specific challenge framing, relevant case study, ROI benchmarks, customer logos (where approved)
- These pages must rank for: "[sub-vertical] warehouse automation," "[sub-vertical] distribution center robotics"

**Integration page:**
- Lists every WMS partner with API integration documentation
- This page is heavily evaluated by Director of Engineering during the shortlisting phase
- Missing integrations that competitors have = disqualifying

**ROI calculator:**
- Must be live, functional, and prominently linked from homepage, sub-vertical pages, and all ads
- Results should generate a downloadable PDF (gated with email)

### 7.2 Messaging Hierarchy by Audience

| Audience | Primary Message | Secondary Message | Proof Required |
|----------|----------------|------------------|---------------|
| **VP Supply Chain** | "Reduce labor cost by [X]% with [payback period] payback" | Sub-vertical case study with similar company profile | Named or ghost case study with metrics |
| **Director of Engineering** | "Integrates with your [WMS] without custom middleware" | Technical architecture documentation | WMS integration certification + architecture diagram |
| **CFO** | "OpEx impact: $[X]M savings over [X] years; CapEx: $[X]M; NPV: $[X]M" | Risk mitigation: uptime SLA, maintenance contract, vendor financial stability | Financial model + SLA contract terms |
| **DC General Manager** | "Your floor team will be up to speed in [X] days" | Floor-level case study: what daily operations look like post-deployment | Implementation timeline + training documentation |

---

## Phase 8: Marketing Audit Output

### Scoring Rubric

**Thought Leadership & Content (30 points)**
- 26–30: Flagship annual industry report, 5+ sub-vertical case studies, ROI calculator live, active trade press citations (DC Velocity/SCM Dive/MMH in last 12 months), executive LinkedIn program active, webinar program quarterly+
- 18–25: Some case studies, occasional trade press, ROI calculator present but limited, moderate LinkedIn activity
- 10–17: 1–2 case studies, no trade press, no ROI calculator, LinkedIn inconsistent
- 0–9: No case studies, no content program, no LinkedIn presence

**Website & Messaging Clarity (25 points)**
- 22–25: Metric-led homepage headline, sub-vertical hub pages, integration page complete, VP Supply Chain-grade messaging throughout
- 16–21: Good messaging, some sub-vertical specificity, adequate integration documentation
- 8–15: Generic messaging, no sub-vertical specificity, weak case studies
- 0–7: Product-first messaging, no customer proof, poor navigation for buyer journey

**ABM & Pipeline Program (20 points)**
- 17–20: Intent data platform in use, MODEX/ProMat presence with private suite, Tier 1 ABM program documented, greenfield trigger response process in place
- 12–16: Trade show presence, some ABM activity, good SDR program
- 6–11: Trade show only, no structured ABM, reactive outreach
- 0–5: No event presence, no structured pipeline program

**Competitive Differentiation (15 points)**
- 13–15: Clear 1-sentence positioning vs. each top competitor, sub-vertical win rate data, differentiation by use case documented
- 9–12: Good general differentiation, limited competitor-specific positioning
- 4–8: Generic differentiation claims, no competitor-specific messaging
- 0–3: "We're different because we care" messaging — no specific differentiation

**Partner & Reference Program (10 points)**
- 9–10: Certified integrator network, customer reference program documented, co-marketing active with top 3 integrators, 5+ referenceable customers by sub-vertical
- 6–8: Some integrator relationships, a few referenceable customers
- 3–5: Informal integrator relationships, 1–2 reference customers
- 0–2: No integrator program, no referenceable customers

---

## Output Format: ROBOTICS-MARKETING-AUDIT.md

```markdown
# Warehouse Automation Vendor Marketing Audit: [Company Name]
**URL:** [url]
**Date:** [current date]
**Vendor Type:** [AMR / ASRS / System Integrator / WCS Software / RaaS]
**Primary Sub-Verticals Served:** [F&B / 3PL / Building Materials / Big Box Retail]
**Stage:** [Startup / Growth / Established]
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3–5 paragraphs. Lead with score and what it means for pipeline generation.
Identify the #1 opportunity — for most automation vendors this is thought leadership
depth or sub-vertical content specificity.
Include estimated pipeline impact: "Adding a F&B sub-vertical hub page and a single
named case study in that vertical would make you competitive in approximately [X] active
F&B RFPs where you are currently not on the shortlist due to perceived lack of
sub-vertical expertise."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Thought Leadership & Content | X/100 | 30% | X | [one-line finding] |
| Website & Messaging Clarity | X/100 | 25% | X | [one-line finding] |
| ABM & Pipeline Program | X/100 | 20% | X | [one-line finding] |
| Competitive Differentiation | X/100 | 15% | X | [one-line finding] |
| Partner & Reference Program | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## Quick Wins (This Month — No Budget Required)

[5–10 specific, high-impact actions:
- Homepage headline rewrite (metric-led vs. product-led)
- LinkedIn post cadence start
- ROI calculator addition or improvement
- Trade press pitch topics
- Case study format improvements]

## Strategic Recommendations (This Quarter — Moderate Investment)

[3–7 recommendations with specific implementation paths and pipeline impact]

## Long-Term Initiatives (This Half — Significant Investment)

[2–4 major initiatives with ROI projections and competitive position impact]

---

## Channel-by-Channel Analysis

### LinkedIn Program
[Company page quality, follower count and quality, post frequency and engagement, 
executive thought leadership program status, paid LinkedIn activity]

### Website & Content
[Homepage messaging grade, sub-vertical hub pages, case study quality, ROI calculator,
integration documentation, SEO for key supply chain search terms]

### Trade Show Presence
[MODEX/ProMat participation, booth investment level, pre/post-show program, 
speaking slot history, private event presence]

### Trade Press
[Citations in DC Velocity/SCM Dive/MMH in last 12 months, contributed content,
guest byline program, PR agency relationship]

### ABM Program
[Tier 1 named account program, intent data usage, SDR outreach quality, 
trigger event response process]

---

## Competitive Positioning Analysis

| Factor | [Company] | Dematic | AutoStore | Locus | 6 River |
|--------|-----------|---------|----------|-------|---------|
| LinkedIn Followers | | | | | |
| Trade Press Citations (12mo) | | | | | |
| Case Studies (public) | | | | | |
| ROI Calculator | | | | | |
| Sub-vertical Specificity | | | | | |
| Integration Documentation | | | | | |
| MODEX/ProMat Presence | | | | | |

---

## Pipeline Generation Model

| Initiative | Est. Annual SQLs Generated | At [X]% Close Rate, $[X]M Avg Deal | Annual Pipeline Impact |
|-----------|---------------------------|-------------------------------------|------------------------|
| Thought leadership / trade press | | | |
| MODEX/ProMat program | | | |
| LinkedIn paid (Tier 2 ABM) | | | |
| ROI calculator / inbound | | | |
| **Total Potential** | | | |

---

## Recommended 90-Day Marketing Plan

**Month 1 (Foundation):**
- [ ] Homepage messaging rewrite (metric-led)
- [ ] Launch LinkedIn thought leadership program (3 internal SMEs posting 3x/week)
- [ ] Begin first white paper / benchmark study (sub-vertical selection)
- [ ] Audit all case studies for metric specificity and rewrite to standard

**Month 2 (Content Engine):**
- [ ] Publish sub-vertical #1 hub page
- [ ] Launch trade press PR pitch program (DC Velocity first)
- [ ] Build ROI calculator v1 (MVP version, email-gated PDF output)
- [ ] LinkedIn paid launch (Tier 2 ABM campaign)

**Month 3 (Pipeline Activation):**
- [ ] Launch white paper (gated download, SDR follow-up sequence)
- [ ] MODEX/ProMat pre-registration (if applicable)
- [ ] Tier 1 ABM: identify top 50 greenfield accounts, build custom outreach
- [ ] Launch certified integrator partner program

*Generated by AI Marketing Suite — Warehouse Automation Vertical | `/market audit <url>`*
```

---

## Compliance Notes for Automation Vendor Marketing

**Always flag these risks in audit output:**

1. **Customer naming without permission:** Never reference a customer by name in any public-facing content without a signed media release. Enforce this regardless of how casually the customer agreed verbally. Violations result in immediate customer relationship damage and potential contract disputes.

2. **Performance claims:** Statements like "reduces labor costs by 50%" or "3× faster throughput" in advertising copy require substantiation from documented customer results. Unsubstantiated performance claims = FTC risk and procurement disqualification.

3. **RFP ethics (pre-RFP engagement):** In government or public company procurement, there are regulations around vendor communication during formal RFP periods. Know when an RFP has been formally issued and route all communication through the designated procurement contact only.

4. **Integration claims:** Claiming integration with a WMS platform "out of the box" without a formal, tested integration creates liability if the integration fails during implementation. All integration claims must be reviewed by engineering before inclusion in marketing materials.

5. **Patent/IP competitive claims:** Statements comparing your technology favorably to a competitor's patented approach must be reviewed by legal before publication. "Our system outperforms [competitor]" without specific, verifiable data = defamation risk in B2B.

---

*Generated by AI Marketing Suite — Warehouse Automation Vertical | `/market <command> <vendor-url>`*
