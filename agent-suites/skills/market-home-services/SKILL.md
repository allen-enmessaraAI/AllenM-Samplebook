# AI Marketing Suite — Home Services
# Vertical: HVAC · Plumbing · Roofing · Electrical · Pest Control · Landscaping · Pool Service · Cleaning
# Base skill: market | Patched for: independent home service businesses, owner-operators, regional service companies

## Vertical Context

VERTICAL: Home Services (field service businesses)
BUSINESS TYPES: HVAC, plumbing, roofing, electrical, pest control, landscaping/lawn care, pool service, house cleaning, garage door, appliance repair, handyman, general contracting
FRANCHISE GATE: Before any marketing analysis, confirm independence. 1-800-Got-Junk, Two Men and a Truck, Neighborly brands (Mr. Rooter, Mr. Electric, Aire Serv), ServiceMaster, Terminix, TruGreen = franchise → marketing controlled at corporate level → regional co-op marketing may apply → redirect to local franchise marketing contact
BUYER FOR MARKETING SERVICES: Owner/Founder makes all decisions. Office Manager may handle day-to-day marketing execution but never final budget. Spouse or bookkeeper is often the hidden financial gatekeeper in family businesses. Decision cycle: days to 2 weeks (not months).
COMPLIANCE CRITICAL: State licensing board regulations (must display license number in ads in most states), EPA/OSHA compliance language (pest control, HVAC refrigerants), DOT compliance for vehicle lettering, Google Ads policies (services ads), ROC/contractor license disclosure requirements vary by state
TERMINOLOGY TO USE: truck count, dispatch board, service area, maintenance agreement, tune-up, inspection, service call, no-show, 5-star review, Angi/HomeAdvisor, Google Business Profile, LSA (Local Services Ads), technician, route, callback, estimate, job close rate, average ticket, membership program — never use generic SaaS or B2B language
REVENUE BENCHMARKS: 1 truck ≈ $200K–$400K/year; 5-truck company = $1M–$2M; 15-truck company = $3M–$6M; maintenance agreement / recurring service base multiplies revenue floor by 1.2–1.5×
SEASONAL PEAKS: HVAC: summer (AC) and winter (heat); Roofing: post-storm events + spring/summer dry season; Landscaping: spring through fall; Pest Control: spring/summer (insects) + fall (rodents); Pool Service: spring through fall
MARKETING BUDGET BENCHMARK: 5–10% of gross revenue for growth-stage companies; 2–5% for established/maintenance mode. A $1M revenue company with 7% budget = $70K/year. Most home service owners dramatically underspend — "word of mouth is working" is the #1 reason.

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full home services marketing audit | HOME-SERVICES-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second business snapshot | Terminal output |
| `/market copy <url>` | Optimized website copy for service businesses | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Maintenance agreement + recall + review sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | Home services content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Google LSA + Google Ads + Facebook strategy | AD-CAMPAIGNS.md |
| `/market funnel <url>` | New customer acquisition funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Local competitor analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | Service landing page CRO analysis | LANDING-CRO.md |
| `/market launch <service>` | New service or new market launch playbook | LAUNCH-PLAYBOOK.md |
| `/market proposal <company>` | Generate client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full home services marketing report | HOME-SERVICES-MARKETING-REPORT.md |
| `/market seo <url>` | Local SEO audit for service business | SEO-AUDIT.md |
| `/market brand <url>` | Brand voice and truck/uniform/logo consistency | BRAND-VOICE.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. For sub-skill commands, use the home services vertical context to override the base skill's generic B2B logic.

### Full Home Services Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with home-services-specific mandates:

1. **market-content** (home services lens) → Website copy effectiveness for inbound calls; service page depth; license/insurance trust signals; before/after photo quality; review content; emergency availability messaging
2. **market-conversion** (home services lens) → Phone number visibility; click-to-call on mobile; online booking friction; form length; "get a free estimate" CTA placement; live chat presence; 24/7 emergency service availability
3. **market-competitive** (home services lens) → Local competitor Google Maps positioning; review count and rating comparison; service area overlap; pricing transparency; emergency availability differentiation; Angi/HomeAdvisor profile comparison
4. **market-technical** (home services lens) → Local SEO optimization; Google Business Profile completeness; LSA setup and status; NAP consistency across directories; Core Web Vitals; mobile call experience; schema markup (LocalBusiness, Service)
5. **market-strategy** (home services lens) → Lead gen channel mix (organic vs. paid vs. referral); maintenance agreement/membership marketing; review generation system; seasonality strategy; Angi/HomeAdvisor dependency assessment; repeat customer marketing

---

## Home Services Marketing Score — Weighted Categories

| Category | Weight | What It Measures in Home Services Context |
|----------|--------|--------------------------------------------|
| Local Visibility & SEO | 35% | Google Business Profile score, Maps ranking, LSA status, directory presence, NAP consistency |
| Reputation & Reviews | 25% | Google rating, review count, review velocity, response rate, Angi/Yelp/BBB profile |
| Website & Conversion | 20% | Click-to-call, mobile UX, service page clarity, trust signals (license, insurance, guarantee) |
| Paid Advertising | 10% | Google LSA, Google Ads, Facebook Ads — efficiency and channel coverage |
| Retention & Recurring Revenue | 10% | Maintenance agreement marketing, past customer reactivation, email/SMS program |

**Composite Home Services Marketing Score** = Weighted average of all 5 categories

> Note: Local Visibility carries 35% weight (vs. 30% in base) because Google Maps ranking is the #1 inbound lead source for home service companies — it generates 60–70% of all calls for most service businesses. Reputation carries 25% because reviews are the deciding factor when a homeowner chooses between two Map Pack results.

---

## Phase 1: Business Classification & Discovery

### 1.1 Business Classification

Before any analysis, classify the home services company:

| Business Type | Signals | Marketing Implications |
|--------------|---------|------------------------|
| **Solo operator (1–3 trucks)** | 1 person or very small team, owner answers phone, limited online presence | Google Business Profile + reviews are everything. No budget for complex programs. |
| **Small crew (4–10 trucks)** | Office manager, basic website, some Google presence, may have Angi/HomeAdvisor | Local SEO + Google Ads + review system. Beginning to outgrow word-of-mouth. |
| **Mid-size company (11–25 trucks)** | Multiple crews, dedicated office staff, active marketing spend | Full channel strategy: LSA + SEO + Facebook + maintenance agreement marketing |
| **Established regional (25+ trucks)** | Multi-trade or multi-location, branded vehicles, established reputation | Brand consistency, multi-location SEO, retention programs, community presence |
| **Franchise location** | Brand marks on website, national brand signals | STOP — defer to franchise marketing coordinator for brand compliance |

### 1.2 Key Pages to Analyze

For home service businesses, audit these pages specifically:
- Homepage (emergency availability messaging, service area, phone CTA above fold)
- Service pages (each service = dedicated page = SEO opportunity + trust builder)
- About/Team page (owner photo, years in business, license numbers, insurance verification)
- Service Area page (critical for local SEO — city names must appear explicitly)
- Reviews/Testimonials page (or Google review widget)
- Contact/Get Estimate page (form length, phone visibility, hours of operation)
- Emergency Services page (for HVAC, plumbing, electrical — critical for high-value emergency searches)

### 1.3 Home Services Tech Stack Detection

| Technology | Detection Method | Marketing Implication |
|-----------|-----------------|----------------------|
| **Google Business Profile (GBP)** | Search company name → view GBP panel | Primary local discovery source — must be optimized |
| **Google LSA (Local Services Ads)** | Search "[trade] [city]" — green checkmark ads at top | Pay-per-lead with Google guarantee badge — high conversion signal |
| **Angi/HomeAdvisor profile** | Search company name on Angi.com | Lead dependency on expensive shared lead platform |
| **Birdeye / Podium / NiceJob** | Footer widget or "leave a review" prompt | Automated review generation in place |
| **Jobber / Housecall Pro / ServiceTitan** | Job postings ("Jobber experience preferred"), website scheduling widget | FSM in place — can integrate email/SMS marketing |
| **Facebook Business Page** | Search company name on Facebook | Social proof and ad targeting capability |
| **Google Ads** | Search "[trade] [city]" — sponsored results | Paid acquisition active — assess ad quality |

---

## Phase 2: Home Services Channel Strategy

### 2.1 Channel Priority for Home Services

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **Google Business Profile** | #1 discovery channel — 60–70% of service calls start here | Critical | Free (management time) |
| **Google Local Services Ads (LSA)** | Pay-per-lead at top of Google SERP; Google Guarantee badge = highest trust signal | High | $500–$3,000/month (pay-per-lead) |
| **Google Search Ads** | Emergency and high-intent searches: "HVAC repair near me," "emergency plumber [city]" | High | $500–$3,000/month |
| **Review Platforms** | Google, Yelp, BBB, Facebook, Angi — rating determines click-through rate from Maps | Critical | $100–$500/month (management platform) |
| **Facebook/Instagram Ads** | Seasonal promotions, maintenance agreement offers, equipment replacement targeting | Medium | $300–$1,500/month |
| **Email / SMS** | Maintenance agreement renewal, seasonal tune-up reminders, past customer reactivation | High | Low cost (via FSM integration) |
| **Nextdoor** | Hyperlocal neighborhood recommendations — strongest referral signal in residential service | Medium | Free organic to $200/month |
| **Direct Mail** | Seasonal HVAC/roofing/lawn campaigns; new mover lists; post-storm canvassing (roofing) | Medium | $500–$2,000/campaign |
| **Angi / HomeAdvisor** | Paid lead marketplace — high cost, shared leads, but immediate volume | Medium-Low | $500–$5,000/month |
| **Door hangers / yard signs** | Post-job neighborhood canvassing — highest ROI field tactic after Google | High | $50–$300/campaign |

### 2.2 Channel Matrix by Trade

| Trade | Top Channel 1 | Top Channel 2 | Top Channel 3 | Seasonal Timing |
|-------|---------------|---------------|---------------|-----------------|
| HVAC | Google LSA (emergency AC/heat) | GBP + Reviews | Email to maintenance list | May–July, Dec–Jan |
| Plumbing | Google LSA (emergency plumbing) | GBP + Reviews | Facebook retargeting | Year-round; post-freeze |
| Roofing | GBP + Reviews | Facebook (storm targeting) | Direct mail (new movers, post-storm) | March–September |
| Electrical | Google LSA | GBP + Reviews | Nextdoor | Year-round |
| Pest Control | GBP + Reviews | Facebook/Instagram (seasonal) | Door hangers (spring canvass) | March–August |
| Landscaping | GBP + Reviews | Facebook (spring) | Door hangers / yard signs | March–October |
| Pool Service | GBP + Reviews | Facebook (pool owners) | Email to existing accounts | March–September |
| Cleaning | GBP + Reviews | Nextdoor | Facebook (homeowner targeting) | Year-round; January surge |

---

## Phase 3: Home Services Content Strategy

### 3.1 Content Pillars

| Pillar | Theme | Content Types | Ratio |
|--------|-------|---------------|-------|
| **Before & After / Proof of Work** | Completed jobs — show the result, not just describe it | Photo posts (Instagram/Facebook), GBP photos, short video walkthrough | 30% |
| **Education & Tips** | Seasonal advice homeowners actually use | "When to replace your HVAC filter," "Signs your pipes are about to fail" | 25% |
| **Social Proof / Reviews** | Real customer stories and review highlights | Screenshot shares, customer video testimonials, Nextdoor shoutout screenshots | 20% |
| **Team & Culture** | The people behind the brand — faces build trust faster than logos | Tech spotlight, "Meet [technician name]," vehicle wrap reveal, certification milestones | 15% |
| **Promotions & Seasonal** | Tune-up specials, seasonal offers, referral programs | Facebook/Instagram ads, email, GBP posts, flyers | 10% |

### 3.2 Platform-Specific Home Services Content

**Google Business Profile (post 2–3x/week minimum):**
- Before/after job photos (most engaging GBP content type)
- Seasonal service alerts ("HVAC tune-up season starts now — book before the rush")
- Team introductions ("Meet Jake — your new service tech covering [neighborhood]")
- Review responses (every review — positive and negative — must get a response)
- Special offers (discount or guarantee for new customers)
- Emergency availability ("We're open 24/7 — call for same-day service")

**Facebook (3x/week):**
- Before/after photos with detailed job story captions
- Seasonal tips and safety advice (shared from website blog)
- Community involvement (sponsoring a little league team, disaster response work)
- Promotion announcements with clear "call to book" CTA
- Customer review screenshots or video testimonials
- "This week in the field" — informal behind-the-scenes content

**Instagram (3–4x/week):**
- High-quality before/after photo pairs (highest engagement content type)
- Short Reels (30–60 seconds): "How we clear a drain in 10 minutes," "What your HVAC filter should look like"
- Tech and team culture content
- Customer testimonial videos (Stories format)

**Nextdoor (ongoing):**
- Respond to every "looking for a [plumber/HVAC/etc.]" post in your service area
- Periodic business posts (not promotional — educational or community value)
- Share 5-star reviews received on Nextdoor
- Never spam — quality engagement builds recommendation velocity

**Email (past customers — monthly minimum):**
- Seasonal maintenance reminders ("Time to schedule your fall HVAC tune-up")
- Maintenance agreement renewal sequences
- Referral program ("Refer a neighbor, get $[X] off your next service")
- Emergency preparedness tips with "save our number" CTA
- Annual "loyalty appreciation" email (thank you for being a customer)

**SMS (customers who opted in — high ROI):**
- Appointment reminders (24 hours before service)
- Seasonal tune-up reminder ("Ready to schedule your spring checkup?")
- Review requests (2 hours post-job completion)
- Emergency service availability during peak weather events

### 3.3 Home Services Content Calendar — Seasonal Framework

| Month | Trade Focus | Top Content Play |
|-------|-------------|-----------------|
| January | Heating, plumbing (pipe freezes) | Emergency response content; HVAC efficiency tips; referral offer for slow season |
| February | HVAC pre-season, home improvement planning | "Spring AC tune-up" early booking offer; Valentine's Day home upgrade angle |
| March | HVAC spring tune-up, pest control, landscaping | Spring service special; pest prevention tips; lawn care start-of-season content |
| April | All trades — spring rush | Review generation push; before/after content; referral program announcement |
| May | HVAC (pre-summer), roofing (storm season), landscaping | "Beat the summer rush — schedule your AC checkup now"; storm preparation content |
| June–July | HVAC emergency season | Emergency availability content; AC filter change reminders; "don't get stuck in the heat" urgency |
| August | HVAC, roofing, back-to-school (cleaning) | Back-to-school home prep content; fall HVAC pre-booking; roofing inspection offer |
| September | HVAC (pre-winter), roofing, pest control (rodent season) | Fall tune-up campaign launch; storm damage roofing content; rodent exclusion tips |
| October | Heating season launch, pest control | Heating system checkup before first cold snap; winterization content |
| November | HVAC maintenance, plumbing (pre-freeze) | Pre-freeze plumbing inspection; "schedule before the holiday rush" urgency |
| December | Minimal marketing spend — slow for most trades | Thank you email to all customers; year-end review of Google ratings; referral ask |

---

## Phase 4: Local SEO for Home Services

### 4.1 Google Business Profile (Highest Leverage — 35% of Score)

**GBP Optimization Checklist for Home Services:**
- Business name: legal name + primary trade (never keyword stuffing: "Best HVAC Company in [City]" = suspension risk)
- Categories: Primary category = exact trade ("Heating Contractor," "Plumber," "Roofing Contractor"). Add secondary categories for additional services.
- Service area: list every city and neighborhood you service — up to 20 service areas
- Hours: set correctly including emergency/on-call hours. "Open 24 hours" for emergency trades.
- Services: list every specific service with description (not just "HVAC" but "AC repair," "furnace installation," "heat pump service," etc.)
- Photos: 25+ photos minimum. Mix: vehicles/trucks (brand signals), completed jobs (before/after), team photos, equipment, office/shop
- Weekly GBP posts: 2–3 per week
- Review velocity: 2+ new reviews per week for fast-growing companies; 2–4/month minimum for maintenance
- Q&A section: pre-populate with 10–15 common customer questions and answers

**GBP Red Flags to Flag in Audit:**
- Keyword-stuffed business name (suspension risk)
- No posts in last 30 days
- Under 25 reviews or under 4.3 rating
- No service list populated
- Photos are all stock imagery or logo only
- Business hours say "temporarily closed"
- No responses to any reviews (positive or negative)

### 4.2 Google Local Services Ads (LSA)

**LSA is the most important paid channel for home service businesses:**
- Google Guarantee badge = immediate trust signal above all organic and regular paid results
- Pay-per-lead model: only pay when a qualified customer calls or messages
- Verification required: background check, license verification, insurance verification
- Setup: go.google.com/localservices

**LSA optimization factors:**
- Respond to every lead within 5 minutes (response time directly affects ranking)
- Mark bookings in the platform (Google uses booking rate to determine ranking)
- Dispute bad leads immediately (wrong service area, wrong job type)
- Budget: set high enough to not run out during peak hours (7am–noon and 5–8pm)
- Categories: enable every relevant job type you serve — more categories = more lead opportunities

**Target cost per lead by trade (LSA benchmarks):**
| Trade | Average CPL | High-Value Jobs | Priority? |
|-------|------------|----------------|-----------|
| HVAC | $15–$45 | Equipment replacement ($5K–$15K) | Critical |
| Plumbing | $20–$55 | Emergency and remodel ($500–$5K) | Critical |
| Roofing | $25–$75 | Full replacement ($8K–$25K) | Critical |
| Electrical | $20–$50 | Panel upgrade, remodel ($500–$5K) | High |
| Pest Control | $15–$40 | Annual contract ($500–$1,500) | High |
| Landscaping | $10–$30 | Annual contract ($1K–$5K) | Medium |

### 4.3 Website Local SEO for Home Services

**Homepage must have:**
- H1: "[Trade] in [City, State] | [Company Name]"
- Service area explicitly listed on homepage (not hidden on a separate page)
- Phone number in header, visible above the fold on mobile
- License number displayed (required in many states — also a trust signal)
- Insurance/bonding badge or statement

**Service pages (one dedicated page per service):**
- Each service = separate URL (e.g., /ac-repair-[city], /furnace-installation-[city])
- 400+ words of original content per page
- Include: service description, process, FAQ, pricing range (if comfortable), and local area mention
- Schema markup: Service schema on each page

**Service area pages (for companies serving multiple cities):**
- Create a dedicated page for each major city served
- Content: neighborhood-specific mentions, local references, local team/office info if applicable
- URL: /hvac-[city-name] or /plumber-[city-name]
- Avoid thin or duplicate service area pages — each needs original content

**Local keyword targets for home services:**
| Intent | Keyword Examples | Priority |
|--------|-----------------|----------|
| Emergency | "emergency plumber [city]," "24 hour AC repair [city]," "furnace repair near me" | Highest |
| Specific service | "AC installation [city]," "roof replacement [city]," "electrician near me" | High |
| Brand/trust | "best HVAC company [city]," "licensed plumber [city]," "insured roofer [city]" | High |
| Educational | "how much does [service] cost," "[service] vs [service]" | Medium |
| Seasonal | "spring HVAC tune-up," "winter furnace checkup," "fall gutter cleaning" | Medium |

---

## Phase 5: Paid Advertising for Home Services

### 5.1 Google Search Ads (Below LSA)

**Campaign Structure for Home Services:**

**Campaign 1: Emergency / High Intent**
- Keywords: "emergency [trade] [city]," "[trade] near me," "[trade] open now," "same day [trade]"
- Match type: Exact and phrase
- Ad schedule: 24/7 or business hours + 2 hours
- CTA: "Call Now — Same-Day Service Available"
- Expected CPC: $8–$35; CPL: $40–$120

**Campaign 2: Specific Service (High Ticket)**
- Keywords: "AC installation [city]," "furnace replacement [city]," "roof replacement [city]"
- CTA: "Free Estimate — Licensed & Insured"
- Expected CPC: $5–$20; CPL: $50–$150

**Campaign 3: Maintenance & Seasonal**
- Keywords: "HVAC tune-up [city]," "furnace checkup [city]," "spring pest control [city]"
- CTA: "Schedule Your [Season] Tune-Up — $[X] Off"
- Expected CPC: $3–$12; CPL: $30–$80

**Negative Keywords for Home Services:**
- DIY, how to, instructions, tutorial
- Jobs, hiring, careers, employment
- School, training, certification
- Cheap, free (unless running a promo)
- Reviews (unless they're searching for your brand)

### 5.2 Facebook & Instagram Ads for Home Services

**Use Case 1: Seasonal Service Promotion**
- Audience: Homeowners (Facebook homeowner interest + demographic), 5–15 mile radius from service area
- Creative: Before/after photo or short video testimonial
- Offer: "Book your [season] tune-up — $[X] off this [month]"
- Budget: $300–$1,000/month
- Expected CPL: $20–$60

**Use Case 2: Emergency/Awareness Retargeting**
- Audience: Website visitors in last 30 days
- Creative: "Still need a plumber? We're available 24/7."
- Budget: $100–$300/month

**Use Case 3: Maintenance Agreement Upsell**
- Audience: Custom audience of past customers (from CRM/FSM export)
- Creative: "Protect your [equipment] year-round — maintenance plans from $[X]/year"
- Budget: $200–$500/month
- Expected CPL: $15–$40 (warmer audience)

**Use Case 4: Post-Storm Roofing / Seasonal Event**
- Trigger: When a significant weather event (hail storm, freeze) hits the service area
- Creative: "Worried about roof damage from last week's storm? Free inspection — no obligation."
- Audience: Homeowners in affected zip codes
- Budget: Burst campaign — $500–$2,000 for 2–3 weeks post-event

---

## Phase 6: Reputation Management for Home Services

### 6.1 Home Services Review Benchmarks

| Platform | Minimum Rating | Minimum Reviews | Velocity Target |
|----------|---------------|-----------------|-----------------|
| Google | 4.5+ | 50+ | 2–4 new reviews/week |
| Yelp | 4.0+ | 25+ | 1–2/week |
| Facebook | 4.3+ | 25+ | 1–2/week |
| BBB | A rating | Accredited | Dispute resolution active |
| Angi | 4.0+ | 10+ | Ongoing from jobs |
| Nextdoor | Recommendations | 10+ | Ongoing |

> Note: Google rating is the most critical metric in home services. A 4.3 vs. 4.7 rating in a competitive Map Pack can drive a 30–40% difference in click-through rate.

### 6.2 Review Generation System (Most Important Marketing Activity)

**At job completion (highest conversion moment):**
1. Tech asks verbally: "If everything looked good today, it would mean a lot to us if you left us a Google review. It only takes 2 minutes and really helps our small business."
2. Text message sent automatically via FSM (Jobber, Housecall Pro, ServiceTitan): 30 minutes–2 hours after job close
3. Followup text if no review: 3 days later

**Text template (post-job review request):**
```
"Hi [First Name]! Thanks for choosing [Company Name] today. If we did a great job,
a quick Google review would mean the world to us:
[Short Google review link]
— [Technician Name] & the [Company] team"
```

**Never incentivize reviews** — violates Google policy and FTC guidelines. Do not offer discounts, gifts, or drawings in exchange for reviews.

**Handling negative reviews:**
- Respond within 24 hours
- Never argue, never be defensive
- Acknowledge, apologize (even if you disagree), offer to make it right offline
- Script: "We're sorry to hear about your experience — this is not the standard we hold ourselves to. Please call [owner name] directly at [phone] so we can make this right."
- Move the conversation offline immediately — do not resolve disputes in public

### 6.3 Angi/HomeAdvisor Strategy

Most home service companies have a love/hate relationship with Angi. Frame it honestly:

**When Angi makes sense:** Early-stage company (under 50 Google reviews), new service area, new trade added, slow season fill-in
**When to reduce Angi:** Google Maps position is top 3, own review count exceeds competitors, Google LSA is live and converting

**Angi audit questions:**
- What's your cost per closed lead from Angi vs. Google? (Angi average: $150–$400/closed job; Google LSA average: $80–$180/closed job)
- Are your Angi leads shared or exclusive?
- What percentage of your Angi leads close vs. your Google/LSA leads?

---

## Phase 7: Retention & Recurring Revenue Marketing

### 7.1 Maintenance Agreement / Membership Marketing

The highest-ROI marketing activity for HVAC, pest control, pool service, and lawn care companies is building a recurring revenue base through maintenance agreements or membership programs.

**Why it matters:**
- Maintenance customers have 3–4x higher lifetime value than one-time customers
- Maintenance visits create upsell opportunities (equipment replacement, add-on services)
- Predictable recurring revenue smooths seasonal cash flow swings
- Maintenance customers give reviews at 2x the rate of one-time service customers

**Marketing plays for maintenance agreements:**
1. **Post-service offer:** Every tech offers a maintenance agreement at the end of every service call. Script: "One more thing — do you have a maintenance plan with us? For $[X]/year, we include [X] visits, priority scheduling, and [bonus]. Most customers find it pays for itself in the first visit."
2. **Email campaign to past customers:** "You had us out [X] months ago for [service]. Did you know we offer a maintenance plan that covers [services]? Here's what's included: [list]. [X]% of our maintenance customers renew every year."
3. **Facebook retargeting:** Target past customers with maintenance offer within 90 days of their last service date.
4. **Seasonal renewal campaign:** Each fall/spring, email all lapsed maintenance customers with a "come back" offer.

### 7.2 Past Customer Reactivation Sequences

**Trigger:** Customer hasn't booked a service in 12+ months

**Email Sequence:**
- Email 1 (12 months after last service): "It's been a while — is everything holding up okay?" + seasonal maintenance tip + soft booking CTA
- Email 2 (14 months): "Quick reminder: [Trade] units that go [X]+ months without service are [risk]. Are you due?"
- Email 3 (16 months): "Last reminder — we'd love to have you back. Here's a [discount/priority booking] for returning customers."

**SMS Sequence (for opted-in customers):**
- Text 1 (12 months): "Hi [Name], [Company] here. Time for your annual [service]? Reply YES to book or call us at [phone]."
- Text 2 (13 months, no response): "Just checking in — still happy to help with any [trade] needs. Book at [link]."

---

## Phase 8: Home Services Marketing Audit Output

### Scoring Rubric

**Local Visibility & SEO (35 points)**
- 30–35: GBP fully optimized (25+ photos, weekly posts, 50+ reviews at 4.5+, complete service list), top-3 Maps ranking, LSA active, strong citation profile
- 22–29: GBP mostly complete, page-1 Maps ranking, adequate reviews
- 12–21: GBP partially complete, page-2 Maps ranking, thin review profile
- 0–11: Incomplete GBP, no Maps ranking, citation inconsistencies

**Reputation & Reviews (25 points)**
- 21–25: 4.5+ Google rating, 75+ reviews, 2+/week velocity, responds to all reviews within 48h
- 15–20: 4.0–4.5 rating, 30–75 reviews, moderate response rate
- 8–14: 3.5–4.0 rating, 15–30 reviews, inconsistent responses
- 0–7: Under 3.5 rating or under 15 reviews

**Website & Conversion (20 points)**
- 17–20: Phone number above fold on mobile, click-to-call, clear service area, license displayed, service-specific pages, fast mobile load, online booking available
- 12–16: Good phone visibility, clear services, adequate trust signals
- 6–11: Generic website, poor mobile, no service-specific pages
- 0–5: Poor UX, no mobile optimization, no trust signals

**Paid Advertising (10 points)**
- 9–10: LSA active with Google Guarantee, Google Ads running, Facebook seasonal campaigns, appropriate bid management
- 6–8: Google Ads or LSA active, limited Facebook
- 3–5: Angi only, no owned paid channel
- 0–2: No paid advertising presence

**Retention & Recurring Revenue (10 points)**
- 9–10: Maintenance agreement program active, automated review requests, email reactivation sequence running
- 6–8: Some retention marketing, manual review requests
- 3–5: Basic email list, no automation
- 0–2: No retention marketing in place

---

## Output Format: HOME-SERVICES-MARKETING-AUDIT.md

```markdown
# Home Services Marketing Audit: [Company Name]
**URL:** [url]
**Date:** [current date]
**Trade:** [HVAC / Plumbing / Roofing / Electrical / Pest Control / Landscaping / Other]
**Company Size:** [Truck count / Employee estimate]
**Revenue Estimate:** ~$[X]K–$[X]M
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3–5 paragraphs. Lead with the score and what it means for their inbound call volume.
Identify the #1 opportunity — for most home service companies this is Google Business Profile
or review velocity. Include estimated call impact: "Moving from position 6 to top-3 in the
Maps Pack for '[trade] [city]' — which gets approximately [X] searches/month — could
mean 5–15 additional inbound calls per month at your close rate."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Local Visibility & SEO | X/100 | 35% | X | [one-line finding] |
| Reputation & Reviews | X/100 | 25% | X | [one-line finding] |
| Website & Conversion | X/100 | 20% | X | [one-line finding] |
| Paid Advertising | X/100 | 10% | X | [one-line finding] |
| Retention & Recurring Revenue | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## Quick Wins (This Week — No Budget Required)

[5–10 specific, zero-cost actions:
- GBP profile gaps to fill (photos, hours, services)
- Missing review responses to write
- Phone number placement fixes on website
- Service area page updates
- Google Q&A to populate]

## Strategic Recommendations (This Month — Moderate Investment)

[3–7 recommendations with implementation paths, costs, and call impact projections]

## Long-Term Initiatives (This Quarter — Significant Investment)

[2–4 major initiatives with ROI projections and payback estimates]

---

## Channel-by-Channel Analysis

### Google Business Profile
[Completion score, photo count, review analysis, posting activity, ranking position for top 3 keywords]

### Google LSA & Google Ads
[LSA status (active/inactive/not set up), Ads detected, estimated spend, landing page quality]

### Website & Local SEO
[Page-by-page assessment, mobile score, service page analysis, keyword rankings, NAP consistency]

### Review Profiles
[Rating per platform, review count, velocity, response analysis, competitor comparison]

### Social Media
[Facebook/Instagram audit — frequency, content quality, engagement, ad presence]

### Retention & Recurring Revenue
[Maintenance agreement marketing assessment, email/SMS capability, FSM integration status]

---

## Competitor Comparison

| Factor | [Company] | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-----------|-------------|-------------|-------------|
| Google Rating | | | | |
| Google Review Count | | | | |
| GBP Photo Count | | | | |
| Maps Pack Position | | | | |
| LSA Status | | | | |
| Angi Profile | | | | |
| Website Mobile Score | | | | |

---

## Revenue Impact Model

| Improvement | Est. Additional Calls/Month | At [X]% Close, $[X] Avg Ticket | Annual Revenue Impact |
|------------|----------------------------|--------------------------------|-----------------------|
| GBP top-3 ranking | +5-15 | | |
| Reviews to 4.7+ | +3-8 | | |
| LSA launch | +8-20 | | |
| Review generation system | +3-10 | | |
| **Total Potential** | | | |

---

## Recommended 90-Day Marketing Plan

**Month 1 (Foundation):**
- [ ] Complete GBP optimization (photos, services, hours, service area)
- [ ] Launch automated review request (post-job text via FSM)
- [ ] Fix website mobile conversion issues
- [ ] Apply for Google LSA and complete verification

**Month 2 (Visibility):**
- [ ] Launch Google Search Ads (emergency + high-intent service campaigns)
- [ ] Begin weekly GBP posting cadence
- [ ] Respond to all existing reviews (positive and negative)
- [ ] Set up Facebook retargeting for website visitors

**Month 3 (Retention):**
- [ ] Launch maintenance agreement email campaign to past customers
- [ ] Start Facebook seasonal promotion campaign
- [ ] Build out service-specific landing pages for top 3 services
- [ ] Implement past-customer reactivation email sequence

*Generated by AI Marketing Suite — Home Services Vertical | `/market audit <url>`*
```

---

## Compliance Notes for Home Services Marketing

**Always flag these risks in audit output:**

1. **License number omission:** Many states require contractor license numbers to appear in all advertising materials (ads, website, vehicles). Failure = state licensing board complaint risk. Audit all digital and physical ad materials.

2. **Unlicensed/uninsured claims:** Never claim "licensed and insured" in advertising without confirming active license and current insurance certificate. These are verifiable — competitors and customers check.

3. **EPA HVAC refrigerant regulations:** HVAC companies must not advertise refrigerant services that imply use of unlicensed technicians (EPA Section 608 certification required). Review ad copy carefully.

4. **Pesticide advertising rules:** Pest control companies face state-specific restrictions on what claims can be made about treatment effectiveness. Review state pesticide advertising guidelines before writing pest control ad copy.

5. **Google LSA background check compliance:** LSA requires individual background checks for service technicians. Failure to maintain these properly results in Google Guarantee badge removal and LSA suspension.

6. **Review gating:** Tools that filter negative reviews before sending a review request link (showing only the 4–5 star path) violate Google's review policies. Flag any such tools in the audit.

---

*Generated by AI Marketing Suite — Home Services Vertical | `/market <command> <business-url>`*
