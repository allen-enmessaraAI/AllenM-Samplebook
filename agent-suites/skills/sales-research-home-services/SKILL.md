# Company Research & Firmographic Analysis — Home Services Vertical

## Metadata
- **Title:** Company Research & Firmographic Analysis — Home Services (HVAC · Plumbing · Roofing · Electrical · Pest Control · Landscaping)
- **Invocation:** `/sales research home-services` or `/sales research <url>` when home services context is detected
- **Vertical Config:** `~/.claude/skills/sales/verticals/home-services.md`
- **Base Skill:** `sales-research` (do not modify base — this is the home services copy)
- **Input:** A business name, website URL, Google Business Profile URL, or Google Maps listing
- **Output:** `HOME-SERVICES-RESEARCH.md` written to the current working directory

---

## Vertical Context Pre-Load

**CRITICAL:** Home service businesses are fundamentally different from the SaaS and B2B companies the base research skill is built for. The data sources, revenue estimation methods, competitive signals, and scoring dimensions are completely different.

**What does NOT apply from base research:**
- Crunchbase / funding data (home service companies don't raise venture capital)
- SEC filings (private family businesses)
- G2 / Capterra reviews (these are their customers' tools, not theirs)
- LinkedIn employee count (most home service companies have 5-50 people; LinkedIn is unreliable at this size)
- SaaS revenue-per-employee benchmarks

**What REPLACES these for home services:**
- Google Business Profile (primary intelligence source)
- Google Maps ranking position
- Angi / HomeAdvisor / Thumbtack profiles
- Yelp Business listing
- BBB (Better Business Bureau) profile
- Facebook Business Page
- Indeed / ZipRecruiter job postings (hiring = growth signal)
- Truck count estimation (primary revenue proxy)
- Company website (secondary)

---

## Phase 1: Primary Source Research — Google & Local Platforms

### 1.1 Google Business Profile (Most Important Source)

This is the single richest intelligence source for any home service business. Use `WebSearch` to locate it:

```
Search: "[business name] [city] Google reviews"
Search: "[business name] [trade] [city]"
Search: site:google.com/maps "[business name]"
```

Then use `WebFetch` to retrieve the profile page where accessible.

**Data to extract — do not skip any field:**

| Data Point | Where Found | Intelligence Value |
|---|---|---|
| **Star Rating** | Profile header | Primary pain signal — below 4.5 is an opening |
| **Total Review Count** | Profile header | Volume signal — under 75 is an opening |
| **Review Velocity** | Dates of recent reviews | Reviews per month — declining = no system |
| **Most Recent Review Date** | Latest review timestamp | Freshness — last review 60+ days ago = dead pipeline |
| **Owner Response Rate** | Scan all reviews for responses | Low = no reputation management system |
| **Response Quality** | Read actual owner responses | Copy-paste = no system; personalized = manual but active |
| **Review Content Themes** | Read 10-15 reviews | What do customers praise? What do they complain about? |
| **Recent 1-star Reviews** | Filter by lowest rating | Specific pain points, crisis risk signals |
| **Google Maps Pack Position** | Search their trade + city | Top 3 = visible; not in top 3 = opportunity |
| **Business Hours** | Profile hours section | Hours reflect operational scale |
| **Services Listed** | Services section | Full breadth of offerings |
| **Photos Count & Recency** | Photo gallery | Engagement with profile — more/newer = more active |
| **Q&A Section** | Questions and answers | Owner engagement level |
| **Website Link** | Profile link | Leads to website research |

**Review analysis protocol:**
Read the 10 most recent reviews and the 5 most recent 1-star reviews. Note:
- What do happy customers specifically praise? (speed, cleanliness, expertise, price, communication)
- What do unhappy customers complain about? (no-shows, pricing disputes, quality issues, communication)
- Are there patterns that suggest operational problems?
- Is the owner responding? With what quality and tone?

### 1.2 Google Maps Competitive Positioning

Search `"[trade] [city]"` in Google Maps and identify the top 3-5 competitors. This is critical context for the sales conversation.

**For each top-ranking competitor, capture:**

| Competitor | Rating | Review Count | Map Pack Position | Notes |
|---|---|---|---|---|
| [Competitor 1] | X.X★ | X reviews | #1 | [distinguishing notes] |
| [Competitor 2] | X.X★ | X reviews | #2 | |
| [Competitor 3] | X.X★ | X reviews | #3 | |
| **[Prospect]** | X.X★ | X reviews | #[X] | |

**Competitive gap analysis:**
- Rating gap vs. top competitor: [X.X - X.X = X.X stars]
- Review count gap vs. top competitor: [X - X = X reviews]
- Map pack visibility: [in top 3 / on page 2 / not visible]
- What would it take to move the prospect into the top 3?

### 1.3 Angi / HomeAdvisor Profile Research

```
Search: "[business name] Angi"
Search: "[business name] HomeAdvisor"
Fetch: angi.com/companylist search for their name if found
```

**Data to extract:**

| Field | Intelligence Value |
|---|---|
| **Active Angi profile** | Confirmed lead gen spend (typically $500-3K/mo) |
| **Angi rating** | Compare to Google rating — often different |
| **Angi review count** | May have reviews they haven't cultivated on Google |
| **Verified status** | Level of investment in the platform |
| **Services listed** | Full service breadth |
| **Years on Angi** | Tenure and dependency on the platform |
| **Response rate** | Engagement level with the platform |

**Interpretation:**
- Active, well-maintained Angi profile = confirmed lead gen budget and a pain point (Angi costs are near-universally resented)
- No Angi presence = pure referral / organic; different conversation angle

### 1.4 Yelp Business Profile Research

```
Search: "[business name] [city] Yelp"
Fetch: yelp.com listing if found
```

**Data to extract:**

| Field | Intelligence Value |
|---|---|
| **Yelp rating** | Cross-reference with Google rating |
| **Yelp review count** | Volume indicator; some trades are more Yelp-heavy (plumbing, cleaning) |
| **Check-ins** | Activity signal |
| **Photos** | Engagement with platform |
| **Claimed status** | Active vs. unclaimed = engagement level |
| **Response rate** | Review management engagement |

### 1.5 BBB (Better Business Bureau) Profile Research

```
Search: "[business name] BBB"
Fetch: bbb.org listing if found
```

**Data to extract:**

| Field | Intelligence Value |
|---|---|
| **BBB Accreditation** | Investment in credibility/trust signals |
| **BBB Rating (A+ to F)** | Complaint history indicator |
| **Complaint Count** | Number and nature of filed complaints |
| **Complaint Resolution** | How they handle formal complaints |
| **Years in Business** | Actual founding date vs. self-reported |
| **Business contact** | Sometimes reveals owner name if not elsewhere |

**Note:** BBB accreditation in home services is a moderate trust signal, particularly for older companies. A low BBB rating with multiple unresolved complaints is a significant risk indicator.

### 1.6 Facebook Business Page Research

```
Search: "[business name] [city] Facebook"
Fetch: facebook.com/[businessname] if found
```

**Data to extract:**

| Field | Intelligence Value |
|---|---|
| **Facebook Rating** | Cross-platform review signal |
| **Review Count on Facebook** | May have reviews not on Google |
| **Page Likes / Followers** | Community size and brand investment |
| **Post Frequency** | How active they are in digital marketing |
| **Last Post Date** | Recent activity signal |
| **Post Content** | What are they promoting? Specials, job openings, team spotlights? |
| **Ad Activity** | Are they running Facebook Ads? (Indicates marketing budget) |
| **Messenger Response Rate** | "Typically responds in X" — engagement signal |
| **Reviews Content** | What do Facebook reviewers say? |

---

## Phase 2: Website Analysis

Use `WebFetch` on their website if they have one. Many smaller operators have minimal web presence — note this if so.

### 2.1 Key Pages to Analyze

| Page | Priority Data for Home Services |
|---|---|
| **Homepage** | Services offered, service area, phone number, years in business, key differentiators |
| **About/Our Story** | Founder story, family business vs. corporate, years in business, community ties |
| **Services** | Full breadth of services — HVAC only vs. multi-trade, residential vs. commercial |
| **Reviews/Testimonials** | How are they displaying social proof? Any notable stories? |
| **Contact/Service Area** | Geographic footprint, response time claims |
| **Online Booking** | Do they have online booking? Indicates FSM integration |
| **Blog/News** | Do they produce content? Sophistication signal |

### 2.2 Website Quality Assessment

Rate the website on a 1-5 scale across these dimensions:

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Strong) |
|---|---|---|---|
| **Design Quality** | 10+ years old, broken elements | Functional, basic | Professional, modern |
| **Mobile Experience** | Not mobile-optimized | Responsive | Mobile-first design |
| **Speed** | Slow loading | Adequate | Fast |
| **Trust Signals** | None | Some reviews/certifications | Full social proof suite |
| **Clear CTA** | No obvious contact path | Phone number present | Multiple clear CTAs |
| **Online Booking** | No | Basic form | Full scheduling widget |
| **Content Depth** | No service descriptions | Basic descriptions | Detailed pages per service |
| **Local SEO Signals** | No location keywords | Some local signals | Optimized for local search |

**Overall website score:** [X/5]

**What the score means:**
- 1.0–2.0: Digital presence problem — losing local SEO visibility and credibility
- 2.1–3.5: Functional but not competitive — likely behind top local competitors
- 3.6–5.0: Reasonably well-positioned — other pain points may be more acute

### 2.3 Technology Stack Detection — Home Services Edition

Home service tech stacks are fundamentally different from SaaS companies. Look for:

| Technology Category | What to Look For | Where to Find It |
|---|---|---|
| **Field Service Management (FSM)** | Online booking widget style, "Powered by ServiceTitan/Jobber/HCP" footer | Website footer, job postings mentioning "experience with [FSM]" |
| **Payment Processing** | Square badge, Stripe button, "pay online" link | Footer, contact page |
| **Chat Widget** | Live chat in corner | Homepage |
| **Review Widgets** | Google review badge, Birdeye/Podium widget | Homepage, footer |
| **Scheduling Widget** | "Book now" button behavior | Homepage, contact page |
| **Marketing Tools** | Google Tag Manager (check source), Facebook Pixel | Page source |
| **Email Marketing** | MailChimp/Constant Contact footer links | Email subscription forms |

**FSM Identification Method:**
Look at job postings — almost all home service job posts mention the FSM they use:
- "Experience with ServiceTitan preferred"
- "Will train on Jobber"
- "We use Housecall Pro"

---

## Phase 3: Hiring & Growth Intelligence

### 3.1 Job Posting Research

```
Search: "[business name] jobs"
Search: "[business name] hiring"
Search: "[business name] Indeed"
Search: "[business name] ZipRecruiter"
```

**For each job posting found, capture:**

| Field | Intelligence Value |
|---|---|
| **Role Title** | Technician = field capacity growth; CSR/Office Mgr = admin scaling |
| **Pay Range** | Revenue scale indicator (higher pay = more revenue to support it) |
| **Number of Openings** | Scale of growth |
| **Requirements Listed** | FSM mentioned, certifications required |
| **Job Description Language** | Reveals culture, scale, pain points ("must handle high call volume") |
| **Date Posted** | Recent = active growth; older = stale or filled |
| **Indeed/Glassdoor Reviews** | Employee sentiment, management style, tool complaints |

**Growth signal interpretation:**

| Hiring Pattern | Signal | Revenue Implication |
|---|---|---|
| 1 technician role | Normal growth | Adding ~$200-350K revenue capacity |
| 2+ technician roles | Fast growth | Significant expansion phase |
| Office Manager / CSR | Admin pain at scale | 5+ techs, revenue over $1M |
| Dispatcher | High call volume | 8+ techs, revenue over $2M |
| Operations Manager | Corporate structure forming | 15+ techs, revenue over $3M |
| Multiple departments | Enterprise-level home services | Full team structure |

### 3.2 Indeed / Glassdoor Employee Reviews

```
Search: "[business name] Glassdoor reviews"
Search: "[business name] Indeed reviews"
```

**What to look for:**
- Software frustrations ("the scheduling software is a mess")
- Management style ("owner is hands-on and micromanages")
- Growth patterns ("company has grown a lot in the last year")
- Tool mentions ("we use [FSM name]" or "they need to upgrade from spreadsheets")
- Turnover signals ("high turnover in the office")

---

## Phase 4: Revenue & Scale Estimation

### 4.1 Truck Count Estimation (Primary Revenue Proxy)

Unlike SaaS companies where revenue-per-employee works, home service revenue is best estimated from truck/technician count:

**Estimation methods (use all available, cross-reference):**

| Method | How to Apply |
|---|---|
| **Fleet photos on website** | Count trucks visible in "About" or "Team" photos |
| **Job postings** | 3 open tech roles + likely existing team → estimate total techs |
| **Google Street View** | Sometimes shows fleet parked at business address |
| **Glassdoor reviews** | Employees often mention company size ("small 5-person team") |
| **Facebook posts** | Fleet photos, "meet our team" posts often show count |
| **Local news / awards** | "Best of [city] HVAC company" articles sometimes mention size |
| **BBB listing** | Sometimes lists number of employees |

**Revenue estimation from truck count:**

| Estimated Trucks | Low Revenue Estimate | High Revenue Estimate | Notes |
|---|---|---|---|
| 1-2 | $150K | $500K | Solo/micro operator |
| 3-5 | $600K | $1.5M | Owner-operator sweet spot |
| 6-10 | $1.5M | $3M | Growth-mode operator |
| 11-20 | $3M | $6M | Established regional operator |
| 21-50 | $6M | $15M | Regional leader |
| 50+ | $15M+ | $50M+ | Likely on enterprise FSM |

**Always state confidence level:** High (direct count from photos), Medium (estimated from job posts and reviews), Low (inferred from limited data).

### 4.2 Revenue Signals Checklist

Use these signals to refine the estimate:

| Signal | Revenue Implication |
|---|---|
| Runs Google Ads | Has marketing budget — likely $1M+ revenue |
| Active Angi spend | Has marketing budget — likely $500K+ revenue |
| Multiple service areas listed | Regional reach — likely $1M+ revenue |
| Online booking widget | Technology investment — likely $500K+ revenue |
| Commercial work listed | Higher average tickets — revenue multiplier |
| 24/7 emergency service offered | Sufficient staff to cover — likely $1M+ |
| Financing offered | Revenue scale to support financing risk — likely $1M+ |
| Brand new trucks in photos | Recent capital investment — likely profitable |
| Multiple brand logos (Carrier, Trane, etc.) | Manufacturer relationships — likely established, $1M+ |

---

## Phase 5: The 8 Research Dimensions — Home Services Edition

### Dimension 1: Business Overview

**Data points to capture:**

| Field | Description | Primary Source |
|---|---|---|
| Business Name | Legal DBA name | GBP, website, BBB |
| Founded / Years in Business | Age of the business | BBB, About page, "Est. [year]" on website or trucks |
| Owner / Founder | Name and background | About page, GBP, Facebook |
| Headquarters / Service Area | Primary location and coverage area | GBP, website |
| Trade(s) | HVAC only vs. multi-trade | Services page, GBP |
| Business Type | Residential, commercial, or mixed | Services page, job posts |
| Estimated Truck Count | Fleet size | Photos, job posts, reviews |
| Estimated Annual Revenue | Range with confidence | Truck count × revenue per truck |
| Business Structure | Family-owned, partnership, franchise, corporate-owned | About page, BBB |
| Franchise Status | Independent vs. part of franchise system | About page, website footer |

### Dimension 2: Reputation & Review Profile

This is the most important dimension for home services — it IS the product quality signal AND the marketing signal.

**Data points to capture:**

| Platform | Rating | Count | Response Rate | Notes |
|---|---|---|---|---|
| **Google** | X.X★ | X reviews | X% responses | Primary platform |
| **Yelp** | X.X★ | X reviews | X% responses | Important for some trades |
| **Facebook** | X.X★ | X reviews | — | Social credibility |
| **Angi** | X.X★ | X reviews | — | Lead gen platform |
| **BBB** | X.X / A+–F | X complaints | — | Trust signal |
| **HomeAdvisor** | X.X★ | X reviews | — | Lead gen platform |

**Review trend analysis:**
- Reviews in last 30 days: [X]
- Reviews 31-90 days ago: [X]
- Reviews 91-180 days ago: [X]
- Trend: [accelerating / stable / declining / stagnant]
- What trend means: [declining review velocity = likely no active review system]

**Top praise themes** (from reading actual reviews):
1. [Theme 1] — mentioned in [X] reviews
2. [Theme 2] — mentioned in [X] reviews
3. [Theme 3] — mentioned in [X] reviews

**Top complaint themes** (from 1-2 star reviews):
1. [Theme 1] — mentioned in [X] reviews
2. [Theme 2] — mentioned in [X] reviews

**Response quality assessment:**
- [Personalized / Template / No response]
- Sample response tone: [describe]
- Notable: [any specific responses that reveal owner personality or management style]

### Dimension 3: Local Market Position

**Data points to capture:**

| Competitor | Rating | Reviews | Est. Trucks | Google Rank | Notes |
|---|---|---|---|---|---|
| [Competitor 1] | X.X★ | X | [X] | #1 | |
| [Competitor 2] | X.X★ | X | [X] | #2 | |
| [Competitor 3] | X.X★ | X | [X] | #3 | |
| **[Prospect]** | X.X★ | X | [X] | #[X] | |

**Competitive gap summary:**
- Stars behind #1: [X.X stars]
- Reviews behind #1: [X reviews]
- Estimated additional calls #1 gets per month over prospect: [X based on rating differential]
- Specific keywords where they do/don't appear in top 3: [trade] [city], [trade] near me, etc.

**Market opportunity:** If they moved from their current position to #1 in Google Maps, what would the call volume increase be? (Rough estimate: each full map pack position = 15-25% more visibility.)

### Dimension 4: Lead Generation Strategy

**Data points to capture:**

| Channel | Active? | Est. Monthly Spend | Quality Signal |
|---|---|---|---|
| **Angi/HomeAdvisor** | Yes / No | $[X] est. | Shared leads, competitive |
| **Thumbtack** | Yes / No | $[X] est. | Pay-per-contact |
| **Google LSA** | Yes / No | $[X] est. | Verified leads, high intent |
| **Google Ads (PPC)** | Yes / No | $[X] est. | High intent, controlled |
| **Facebook Ads** | Yes / No | $[X] est. | Brand awareness, lower intent |
| **Yelp Ads** | Yes / No | $[X] est. | Moderate intent |
| **SEO / Organic** | Yes / No | N/A | Long-term, owned channel |
| **Referrals / Word of Mouth** | Yes (assumed) | N/A | Highest quality, not scalable |

**Lead gen dependency assessment:**
- Highly dependent on paid platforms (Angi/HomeAdvisor dominant): Vulnerable to price increases, shared leads, competitor undercutting
- Balanced mix (paid + organic + referral): More resilient
- Pure referral / organic only: Ceiling risk — can't scale beyond personal network

**How to detect active Angi/Google Ads spend:**
- Search for their business name in Facebook Ad Library: `facebook.com/ads/library`
- Check if their Google Business Profile has an "Ad" badge when appearing in search
- Search their business name + "Angi" to see if they have a maintained profile with reviews

### Dimension 5: Technology Stack

**Data points to capture:**

| Category | Tool Identified | Confidence | How Found |
|---|---|---|---|
| **FSM / Scheduling** | [ServiceTitan / Jobber / HCP / Spreadsheet / Unknown] | H/M/L | [job post / website / review mention] |
| **Payment Processing** | [Square / Stripe / Check only / Unknown] | H/M/L | [website] |
| **Review Management** | [Birdeye / Podium / NiceJob / Manual / None] | H/M/L | [widget on site / review response pattern] |
| **Online Booking** | [Yes / No] | H/M/L | [website CTA] |
| **Chat** | [Yes / No / which tool] | H/M/L | [website] |
| **Email Marketing** | [Yes / No / which tool] | H/M/L | [subscribe form footer] |
| **CRM** | [Unknown for most / ServiceTitan has built-in] | H/M/L | [job post] |

**Tech sophistication level (1-4):**
- Level 1: Whiteboard / paper / personal phone — no digital tools
- Level 2: Basic (Gmail, QuickBooks, maybe a simple website)
- Level 3: FSM + Google presence managed + some paid marketing
- Level 4: Full stack (FSM + review management + marketing automation + online booking)

**Current FSM implications:**

| FSM Detected | What It Means for Your Sale |
|---|---|
| No FSM (whiteboard/spreadsheet) | High pain, low sophistication — education sale required |
| Housecall Pro or Jobber | Active software buyer, will compare ROI, reasonable sophistication |
| ServiceTitan | Premium buyer, likely has office staff, compare to ST's ecosystem |
| FieldEdge / Successware | Older/traditional shop, may be frustrated with legacy UX |

### Dimension 6: Team & Operations

**Data points to capture:**

| Field | Value | Source |
|---|---|---|
| **Owner Name** | [name] | GBP, About page, Facebook |
| **Owner Background** | [technician who started the business / business background / second-generation] | About page, Facebook, news |
| **Years Owner Has Run Business** | [X years] | BBB, About page |
| **Office Staff** | [yes / no / estimated count] | Job posts, reviews, About page |
| **Tech Count (Estimated)** | [X technicians] | Job posts, photos, truck count |
| **Service Area Coverage** | [city only / metro / regional / statewide] | Website service area, GBP |
| **Hours of Operation** | [standard / extended / 24/7] | GBP, website |
| **Emergency Service** | [yes / no] | Services page, GBP |
| **Commercial Work** | [yes / no / percentage] | Services page |
| **Key Certifications** | [NATE, EPA 608, licensed, bonded, insured] | Website, BBB |

**Owner profile summary:**
- Type: [Technician founder / business buyer / second-generation / investor-owner]
- Likely decision-making style: [solo and fast / collaborative / deliberate]
- What they care about most: [infer from about page tone, years in business, growth signals]

### Dimension 7: Seasonal & Market Context

**Data points to capture:**

| Element | Assessment |
|---|---|
| **Trade seasonality** | [High season / low season / year-round for their trade] |
| **Current season status** | [What month is it and what does that mean for this trade?] |
| **Market density** | [How many competitors in their Google Maps search area?] |
| **Market maturity** | [Highly competitive market / emerging market / underserved area] |
| **Weather patterns** | [Extreme climate = HVAC dependency; storm-prone = roofing demand] |
| **Local economic indicators** | [Is the market growing? New housing? Commercial development?] |

**Best time to approach (seasonal recommendation):**
Based on their trade, when is their shoulder season — the ideal window when they have both money and time?
- [Specify month range]
- [If currently in shoulder season: note "now is the ideal time"]
- [If in peak season: note "wait X weeks until [month]"]

### Dimension 8: Recent Activity & Signals (Last 90 Days)

**Data points to capture:**

| Category | Activity Found | Date | Sales Implication |
|---|---|---|---|
| **New bad review** | [yes / no] | [date] | Pain is fresh and visible |
| **Owner responded to negative review** | [yes / no] | [date] | Awareness of problem, no system |
| **New job postings** | [yes / no / role] | [date] | Growth signal |
| **Facebook posts about growth** | [yes / no] | [date] | Growth mindset |
| **New vehicle photos** | [yes / no] | [date] | Capital investment = revenue growth |
| **Special offer / promotion** | [yes / no] | [date] | Slow period signal — generating demand |
| **Community post / local news** | [yes / no] | [date] | Brand investment |
| **Website update** | [yes / no] | [date] | Digital investment signal |

---

## Phase 6: Scoring — Home Services Company Fit Score

This replaces the base skill's scoring entirely. Home services requires completely different scoring dimensions.

### Company Fit Score (0-100) — Home Services

| Dimension | Max Points | Scoring Criteria |
|---|---|---|
| **Revenue / Scale Fit** | 20 | Is this company the right size for your product's price point and ROI threshold? |
| **Pain Signal Strength** | 25 | How acute and confirmed are the pain points? (Google rating, review gap, Angi spend) |
| **Tech Readiness** | 15 | Can they implement and benefit from your product? (Level 2-3 is ideal) |
| **Owner Access** | 20 | How direct is the path to the decision maker? |
| **Timing / Season** | 20 | Is it the right time of year to approach? |

**Revenue / Scale Fit (0-20):**

| Estimated Revenue | Score | Rationale |
|---|---|---|
| Under $300K (1-2 trucks) | 3-6 | Below minimum viable deal size; owner too stretched |
| $300K–$800K (2-4 trucks) | 8-12 | Lower end of sweet spot; price-sensitive |
| $800K–$3M (4-12 trucks) | 15-20 | **Ideal range** — budget exists, pain is real, decision cycle is short |
| $3M–$8M (12-25 trucks) | 12-17 | Larger deal but more stakeholders; may need business case |
| Over $8M (25+ trucks) | 5-10 | Likely on ServiceTitan with dedicated ops team — different motion |

**Pain Signal Strength (0-25):**

| Signal Combination | Score | Rationale |
|---|---|---|
| Rating < 4.3 AND reviews < 50 AND active Angi spend | 22-25 | Triple-confirmed acute pain |
| Rating < 4.5 AND reviews < 75 | 16-21 | Two confirmed signals |
| Rating < 4.7 OR reviews < 100 | 10-15 | One confirmed signal |
| Rating 4.7+ but Angi-dependent AND no owned lead gen | 8-12 | Hidden pain — good reputation but rented leads |
| Rating 4.8+ AND 150+ reviews AND owned lead gen | 0-5 | No visible review/reputation pain; look for other pain points |

**Tech Readiness (0-15):**

| Tech Level | Score | Rationale |
|---|---|---|
| Level 1 (no tools) | 4-7 | Can implement but needs more hand-holding |
| Level 2 (basic — Gmail + QuickBooks) | 10-13 | **Ideal** — ready to buy, no competing tool |
| Level 3 (FSM but no review system) | 11-15 | **Ideal** — can integrate with existing FSM |
| Level 4 (full stack including review tool) | 2-6 | Already has a solution; needs compelling displacement angle |

**Owner Access (0-20):**

| Access Level | Score | Rationale |
|---|---|---|
| Owner name + cell phone listed on GBP or website | 18-20 | Direct access — call today |
| Owner name found, phone on website | 14-17 | One step to contact |
| Owner name found on Facebook/LinkedIn | 10-13 | Research needed to get contact info |
| Business phone only, owner name not public | 6-9 | Cold call to business; ask for owner by name |
| Franchise or corporate-owned — no local owner | 1-4 | Decision maker is not local; different motion |

**Timing / Season (0-20):**

| Timing Situation | Score | Rationale |
|---|---|---|
| Currently in shoulder season for their trade | 18-20 | **Ideal** — has money and time |
| 2-4 weeks before shoulder season | 15-17 | Start the conversation now, close in shoulder season |
| Just coming out of peak season | 12-15 | Has cash, slightly fatigued, receptive |
| Currently in peak season | 4-8 | Too busy; note and return in [X weeks] |
| Dead of slow season | 2-6 | No cash, low morale; hold unless pain is critical |

### Score Interpretation

| Total Score | Grade | Recommended Action |
|---|---|---|
| 85-100 | **A+** | Call today. Right company, right time, confirmed pain, direct access to owner. |
| 70-84 | **A** | High priority. Start outreach this week with personalized approach. |
| 55-69 | **B** | Good fit. Add to calling sequence. Return if not reached in 2 weeks. |
| 40-54 | **C** | Marginal. Add to email nurture. Check back next shoulder season. |
| Under 40 | **D** | Do not pursue now. Note reason and set 6-month reminder. |

---

## Output Format: HOME-SERVICES-RESEARCH.md

Write the full output to `HOME-SERVICES-RESEARCH.md` in the current directory:

```markdown
# Home Services Company Research: [Business Name]
**Input:** [URL or business name provided]
**Trade:** [HVAC / Plumbing / Roofing / etc.]
**Date:** [current date]
**Company Fit Score: [X]/100 — Grade [A+/A/B/C/D]**

---

## Executive Summary

[2-3 paragraphs. Who is this company? What's their reputation look like?
Are they a fit? What's the key pain signal? What's the right approach?
Written for a sales rep who needs to get up to speed in 60 seconds before a call.]

---

## Business Snapshot

| Field | Value |
|---|---|
| **Business Name** | [name] |
| **Trade** | [trade(s)] |
| **Owner** | [name if found] |
| **Founded** | [year / "est. X years ago"] |
| **Location** | [city, state] |
| **Service Area** | [coverage area] |
| **Estimated Trucks** | [X] (confidence: [H/M/L]) |
| **Revenue Estimate** | $[X]–$[X] (confidence: [H/M/L]) |
| **Google Rating** | [X.X]★ |
| **Google Reviews** | [X] |
| **Map Pack Position** | [#X / not visible] |
| **FSM Platform** | [name / unknown] |
| **Lead Gen Platforms** | [Angi / Google Ads / Organic / etc.] |
| **Tech Level** | [1–4] |
| **Seasonal Window** | [current season status] |

---

## 1. Business Overview
[Full Dimension 1 findings]

## 2. Reputation & Review Profile
[Full Dimension 2 findings — platform-by-platform table, trends, themes]

## 3. Local Market Position
[Full Dimension 3 findings — competitor table and gap analysis]

## 4. Lead Generation Strategy
[Full Dimension 4 findings]

## 5. Technology Stack
[Full Dimension 5 findings]

## 6. Team & Operations
[Full Dimension 6 findings]

## 7. Seasonal & Market Context
[Full Dimension 7 findings]

## 8. Recent Activity (Last 90 Days)
[Full Dimension 8 findings]

---

## Company Fit Score: [X]/100

| Dimension | Score | Key Evidence |
|---|---|---|
| Revenue / Scale Fit | [X]/20 | [evidence] |
| Pain Signal Strength | [X]/25 | [evidence] |
| Tech Readiness | [X]/15 | [evidence] |
| Owner Access | [X]/20 | [evidence] |
| Timing / Season | [X]/20 | [evidence] |
| **Total** | **[X]/100** | Grade: [A+/A/B/C/D] |

---

## Top 3 Strengths (Sales Opportunity Signals)

1. **[Strength]** — [Evidence]. *Sales use: [how to use this in outreach/conversation]*
2. **[Strength]** — [Evidence]. *Sales use: [how to use this]*
3. **[Strength]** — [Evidence]. *Sales use: [how to use this]*

## Top 3 Risks / Challenges

1. **[Risk]** — [Evidence]. *Mitigation: [how to handle this]*
2. **[Risk]** — [Evidence]. *Mitigation: [how to handle this]*
3. **[Risk]** — [Evidence]. *Mitigation: [how to handle this]*

## Key Insights for Sales

1. **[Insight]** — [Evidence]. *Action: [what to do with this]*
2. **[Insight]** — [Evidence]. *Action: [what to do with this]*
3. **[Insight]** — [Evidence]. *Action: [what to do with this]*

---

## Recommended Outreach Approach

**Best channel:** [Phone / Email / Facebook / combination]
**Best timing:** [Days, times, and seasonal window]
**Lead opening angle:** [Which framework to use and why — specific to their pain]
**Opening line for phone call:**
"[Full opening line incorporating their specific Google stats and competitor comparison]"

**Opening line for email:**
"[First line of email 1 — specific, verifiable, under 15 words]"

---

## Next Steps

1. [Most important immediate action]
2. [Second action]
3. [Third action]

---

*Generated by AI Sales Team — `/sales research home-services`*
*Reference: ~/.claude/skills/sales/verticals/home-services.md*
```

---

## Terminal Output

```
=== HOME SERVICES RESEARCH COMPLETE ===

Business: [name] ([trade])
Owner:    [name or "not found"]
Location: [city, state]

Revenue Estimate: $[X]–$[X] ([X] trucks est.)
Tech Level: [1–4] / [FSM if known]

Company Fit Score: [X]/100 — Grade [A+/A/B/C/D]
  Revenue/Scale Fit:    [XX]/20 ████████░░
  Pain Signal Strength: [XX]/25 ██████░░░░
  Tech Readiness:       [XX]/15 ███████░░░
  Owner Access:         [XX]/20 █████░░░░░
  Timing / Season:      [XX]/20 ████████░░

Google Profile:
  Rating:       [X.X]★ ([X] reviews)
  Map Position: #[X] for "[trade] [city]"
  Top Rival:    [name] — [X.X]★ / [X] reviews
  Review Gap:   [X] reviews behind top competitor

Lead Gen:
  Angi/HAdvisor: [active / not found]
  Google Ads:    [active / not found]

Seasonal Window: [status for their trade]
Best Outreach:   [days/times]

Full report saved to: HOME-SERVICES-RESEARCH.md
```

---

## Error Handling

- If no Google Business Profile is found, try searching for their Yelp or Facebook page and use those as primary sources
- If the business has no website, note it as "No website found — digital presence is minimal" and increase pain score accordingly (a business with no website is almost certainly losing calls)
- If owner name is not findable, note it as a gap and suggest calling the business directly and asking for the owner by the business name on the GBP
- If truck count cannot be estimated, use job postings and employee review mentions to approximate
- Always complete the report regardless of data gaps — limited data is itself a signal (low digital sophistication = higher need for digital tools)
- If the business appears to be a franchise location, note this prominently — the local manager may not be the economic buyer

## Cross-Skill Integration

- Output file `HOME-SERVICES-RESEARCH.md` feeds directly into `/sales outreach home-services` for personalized sequence generation
- Output feeds into `/sales qualify` for opportunity scoring (note: use home-services BANT weights from vertical config)
- Output feeds into `/sales prep` for meeting preparation
- Suggest follow-up: `/sales outreach home-services` to generate a personalized outreach sequence using this research
