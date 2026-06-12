# AI Marketing Suite — Medical Spas (Med Spas)
# Vertical: Aesthetic Medicine / Medical Aesthetics
# Base skill: market | Patched for: independent med spas, aesthetic clinics, cosmetic practices

## Vertical Context

VERTICAL: Medical Spas / Aesthetic Medicine
PRACTICE TYPES: Medical spa (NP/PA/MD-directed), aesthetic clinic, cosmetic dermatology, laser center, injection boutique, wellness + aesthetics hybrid
FRANCHISE GATE: Before any marketing analysis, confirm independence. Ideal Image, LaserAway, SEV Laser, Massage Envy (non-aesthetics), European Wax Center = franchise → marketing controlled at corporate level → marketing decisions not made at practice level → redirect to franchise marketing coordinator
BUYER FOR MARKETING SERVICES: Owner/Medical Director (NP, PA, MD, DO) makes all decisions. Many med spa owners ARE the brand — their Instagram presence is the practice's marketing. Operations Director or Spa Director at multi-location practices. Decision cycle: fast at solo owner level, slow at multi-location.
COMPLIANCE CRITICAL: HIPAA (patient before/after photos require signed HIPAA-compliant photo release), state medical board advertising rules (scope of practice advertising varies by state for NPs/PAs), FDA advertising rules for devices and drugs (cannot make unapproved claims for off-label use), FTC testimonials (cannot cherry-pick exceptional results without disclosure), no incentivized reviews, Alle/Aspire loyalty program co-marketing rules, state cosmetics board regulations (esthetics services)
TERMINOLOGY TO USE: rebooking rate, average ticket, consultation conversion, neurotoxin (Botox, Dysport, Xeomin, Daxxify), filler (Juvederm, Restylane, Sculptra, Radiesse), treatment room, injector, esthetician, before/after, RF microneedling (Morpheus8, Sylfirm), laser (Moxi, BBL, Clear + Brilliant, Fraxel), body contouring (CoolSculpting, Emsculpt, Emtone), Aesthetic Record, Zenoti, Boulevard, Jane App, Alle, Aspire, Brilliant Distinctions, RealSelf, VIP membership, cash-pay, treatment cycle — never use generic SaaS or healthcare language
REVENUE BENCHMARKS: $60K–$90K per treatment room per month = $720K–$1.08M/treatment room/year. Membership/VIP program: adds 20–40% revenue stability. Average ticket: $400–$600 for neurotoxin/filler; $800–$2,500 for device treatments; $3,000–$15,000+ for combination packages.
SEASONAL PEAKS: January–February (New Year transformation + pre-Valentine's), May–June (pre-summer skin and body), September–October (post-summer skin + pre-holiday glow), November (holiday party prep — busiest month). Slowest: July–August (vacations), December 15–31 (staff booked solid — do not prospect or pitch).
MARKETING BUDGET BENCHMARK: 5–10% of gross revenue for growth-stage practices; 3–5% for established practices; $1M practice at 7% = $70K/year. Med spas have the highest marketing intensity of any healthcare vertical.

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full med spa marketing audit | MEDSPA-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second med spa practice snapshot | Terminal output |
| `/market copy <url>` | Generate optimized med spa website copy | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Client retention + rebooking sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | Med spa social media content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Meta Ads + Google Ads strategy for med spa | AD-CAMPAIGNS.md |
| `/market funnel <url>` | Consultation and new client funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Local competitor med spa analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | Consultation landing page CRO | LANDING-CRO.md |
| `/market launch <service>` | Launch playbook for new device/treatment | LAUNCH-PLAYBOOK.md |
| `/market proposal <practice>` | Generate client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full med spa marketing report | MEDSPA-MARKETING-REPORT.md |
| `/market seo <url>` | Local SEO audit for med spa | SEO-AUDIT.md |
| `/market brand <url>` | Med spa brand voice and positioning | BRAND-VOICE.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. Sub-skill commands use the med spa vertical context to override base skill generic logic.

### Full Med Spa Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with med spa-specific mandates:

1. **market-content** (med spa lens) → Website and Instagram copy effectiveness; consultation CTA strength; treatment page depth; before/after gallery compliance and quality; membership/VIP program visibility; device credibility content
2. **market-conversion** (med spa lens) → Online booking or consult request friction; Instagram → booking conversion path; phone/DM response speed signals; pricing transparency vs. "call for pricing" analysis; treatment package presentation
3. **market-competitive** (med spa lens) → Local competitor practices; Instagram follower and engagement comparison; Facebook Ad Library check for active promotions; Google Maps ranking; RealSelf profile presence and review velocity
4. **market-technical** (med spa lens) → Local SEO for aesthetics; Google Business Profile; Instagram link-in-bio optimization; booking widget integration; page speed and mobile experience (most bookings happen on mobile)
5. **market-strategy** (med spa lens) → Retention vs. acquisition balance; discount dependency detection (Facebook Ad Library); membership program marketing; injector dependency risk; seasonal campaign calendar; social-first vs. search-first strategy

---

## Med Spa Marketing Score — Weighted Categories

| Category | Weight | What It Measures in Med Spa Context |
|----------|--------|--------------------------------------|
| Social Media Presence & Engagement | 30% | Instagram quality, engagement rate, follower count, content consistency, TikTok presence |
| New Client Conversion | 25% | Online booking UX, consultation CTA, Instagram → booking flow, phone/DM responsiveness |
| Content Quality & Compliance | 20% | Before/after gallery (HIPAA-compliant), treatment page depth, device credibility, testimonials |
| Reputation & Reviews | 15% | Google rating, review velocity, RealSelf profile, response rate |
| Retention Marketing | 10% | Membership program visibility, rebooking sequence, email/SMS marketing, loyalty integration (Alle/Aspire) |

**Composite Med Spa Marketing Score** = Weighted average of all 5 categories

> Critical difference from base skill: Social media carries 30% weight (vs. SEO at 20% in base) because Instagram is the #1 discovery AND conversion channel for med spa clients. A med spa with 10K Instagram followers and strong engagement can outperform a competitor with better SEO. Facebook Ad Library check is mandatory — discount promotion dependency is a leading indicator of retention and profitability problems.

---

## Phase 1: Med Spa Discovery

### 1.1 Practice Classification

| Practice Type | Signals | Marketing Implications |
|--------------|---------|------------------------|
| **Injection boutique (toxin + filler focus)** | Botox/filler prominently featured, minimal device services, often 1-2 injectors | Injector brand = practice brand; heavy reliance on individual provider's social following; injector dependency risk |
| **Full-service med spa** | Wide service menu: toxins, fillers, lasers, RF, body contouring, facials | Multiple content verticals; seasonal revenue diversification; higher average ticket ceiling |
| **Laser center / device-focused** | HIFEM, laser hair removal, CoolSculpting, Morpheus8 featured prominently | Device-specific SEO keywords; procedure education content; finance/payment plan promotion |
| **Wellness + aesthetics hybrid** | Combines IV therapy, hormone optimization, or functional wellness with aesthetics | Dual audience; wellness content stack + aesthetics content stack; membership pricing |
| **Cosmetic dermatology** | MD/DO-directed; dermatology credentials featured; skincare + procedures | Clinical authority differentiator; referral network with primary care; prescription skincare line upsells |
| **Franchise** | See gate list above | STOP — marketing controlled at corporate |

### 1.2 Mandatory Research Before Any Analysis

**Step 1: Facebook Ad Library (mandatory, free)**
Navigate to facebook.com/ads/library and search practice name:
- Active discount ads ("20% off Botox," "BOGO filler") → discount dependency = retention problem
- New patient acquisition ads vs. retention content balance
- Number of simultaneous ads running (5+ = high marketing spend, assess ROI)
- Ad creative quality (professional vs. DIY) → budget and sophistication signal

**Step 2: Instagram Account Review**
- Follower count and engagement rate (followers × 3–5% = healthy engagement for med spa)
- Content type ratio: educational vs. before/after vs. promotional
- Posting frequency: under 3x/week = content gap
- Before/after quality and HIPAA compliance signals (no name tags, no location metadata)
- Bio: booking link present? Updated? Clear service menu?

**Step 3: Google Business Profile**
- Rating (under 4.3 = visible issue)
- Review themes (rebooking difficulty, injector-specific loyalty, front desk complaints)
- Photo count and quality (recent staff photos, before/afters, facility)
- Response rate to reviews

**Step 4: RealSelf Pro Profile Check**
- Search "[practice name]" on realself.com
- Review count and recency (under 2 reviews in 6 months = inactive profile)
- Q&A engagement on RealSelf = lead generation signal

### 1.3 Key Pages to Analyze

- Homepage (first impression; consultation CTA; brand positioning)
- Services menu (depth and SEO value of individual service pages)
- Before/After gallery (compliance check; content quality; categorization by service)
- Team/Injector page (provider bios = trust signal; credential display; individual injector pages increase injector dependency risk)
- Membership/VIP page (if present — program structure, pricing, benefits)
- Booking/Consultation page (friction assessment; scheduling options)
- Blog / educational content (SEO value; authority signals)
- Contact/Location (hours, parking, phone, online booking widget)

### 1.4 Med Spa Technology Stack Detection

| Technology | Detection Method | Marketing Implication |
|-----------|-----------------|----------------------|
| **Aesthetic Record** | Footer mention, appointment reminder branding | EMR = full patient journey trackable; recall automation possible |
| **Zenoti** | Branded appointment widgets, App Store review | Enterprise-grade; membership management likely active |
| **Boulevard / Jane App** | Scheduling widget branding | Modern booking UX; strong online booking flow |
| **Mindbody / ClassPass** | ClassPass listing; Mindbody widget | Service-based pricing model; potential discounting on ClassPass |
| **Alle (Allergan)** | "Alle points" or Allergan product logo | Allergan practice → Botox/Juvederm primary; co-marketing eligible |
| **Aspire (Galderma)** | "Aspire points," Galderma product badges | Galderma practice → Dysport/Restylane primary |
| **Meta Pixel** | Source code check | Retargeting active — Facebook/Instagram ads in play |
| **Google Ads** | SpyFu check | Paid search active; assess keyword strategy |

---

## Phase 2: Med Spa Channel Strategy

### 2.1 Channel Priority for Med Spa

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **Instagram** | #1 discovery AND conversion channel for med spa clients — before/after content is the most shared format | Critical | Content creation: $500–$2,000/month |
| **Meta Ads (Facebook/Instagram)** | Primary paid acquisition and retargeting — most effective paid channel for aesthetic services | Critical | $1,000–$5,000/month |
| **Google Business Profile** | Local discovery; "med spa near me," "Botox [city]" searches; review showcase | High | Free (management time) |
| **Google Search Ads** | High-intent capture: "Botox [city]," "lip filler [city]," "Morpheus8 [city]" | High | $1,000–$4,000/month |
| **TikTok** | Fastest growing discovery channel for aesthetics; before/after transformation content performs extremely well | High | Content creation: $500–$1,500/month |
| **Email / SMS** | Client retention, rebooking, membership enrollment — highest ROI for existing clients | High | Low cost via EMR/Zenoti integration |
| **RealSelf Pro** | Research-phase lead generation; clients in consideration phase; high-intent audience | Medium | RealSelf Pro subscription: ~$200–$600/month |
| **Pinterest** | Visual platform; "Botox before after," "lip filler inspiration" — consideration-stage audience | Medium | Organic only |
| **YouTube** | Procedure education; device demos; "What is Morpheus8?" search traffic | Medium | Low cost if camera-ready team |
| **Influencer Marketing** | Local nano-influencers (5K–50K followers) for authentic before/after content; high-trust channel | Medium | Trade/barter or $200–$1,000/influencer |
| **Alle/Aspire Co-Marketing** | Manufacturer co-marketing funds and email support — often underutilized | Medium | Free (apply with rep) |
| **Direct Mail** | Less common for med spa; works for high-end membership offers in luxury zip codes | Low-Medium | $800–$2,000/campaign |

### 2.2 The Instagram-First Strategy

Med spa is the only healthcare vertical where social media should be treated as the primary marketing channel — not a supplement to search.

**Why Instagram-first:**
- 78% of aesthetic service purchasers report discovering a practice through social media (vs. 31% for Google)
- Before/after content in aesthetics is the most trusted form of social proof — more powerful than written reviews
- Med spa clients book based on: (1) results, (2) injector personality/trust, (3) location convenience — Instagram communicates #1 and #2 better than any other channel

**The Instagram flywheel for med spa:**
```
High-quality before/after content
        ↓
Organic reach + saves (saves = highest-signal engagement)
        ↓
Profile visit → link-in-bio → booking page
        ↓
New consultation booked → great result → new before/after content
        ↓ (repeat)
```

**Instagram metrics to benchmark:**
| Metric | Below Average | Average | Above Average |
|--------|--------------|---------|---------------|
| Engagement rate | Under 1% | 1–3% | 3–6%+ |
| Saves per post (before/after) | Under 20 | 20–50 | 50+ |
| Story views / follower count | Under 5% | 5–10% | 10%+ |
| Link-in-bio click rate | Under 1% | 1–3% | 3%+ |
| Follower growth rate | Under 0.5%/month | 0.5–1% | 1%+/month |

---

## Phase 3: Med Spa Content Strategy

### 3.1 Content Pillars for Med Spa

| Pillar | Theme | Content Types | Ratio |
|--------|-------|---------------|-------|
| **Before/After Results** | Treatment transformations by service category; patient journey stories | Instagram posts, TikTok, Facebook, website gallery | 35% |
| **Education & Demystification** | "What is [treatment]," myth-busting, safety and science content, FAQ reels | Instagram carousels, TikTok, blog, YouTube | 25% |
| **Injector/Provider Personality** | Provider-to-client trust building; injector education content; day-in-the-life | Instagram Reels, TikTok, Stories, YouTube | 20% |
| **Practice Culture & Lifestyle** | Office aesthetic, team culture, community, brand identity | Instagram Stories, Facebook, BTS Reels | 10% |
| **Promotions & Membership** | Seasonal offers, VIP program enrollment, package deals | Email, Instagram, Google Posts, Meta Ads | 10% |

### 3.2 Platform-Specific Med Spa Content

**Instagram (5-7x/week — primary channel, treat as full-time channel):**

*Feed Posts (3-4x/week):*
- Before/after posts (one service per post; avoid combining — algorithms and clients prefer single-treatment clarity)
- Educational carousels: "5 things nobody tells you about lip filler"
- Provider introduction posts: headshot + credentials + specialty + one personal detail
- Device/technology education: "Here's what Morpheus8 actually does to your skin (science breakdown)"

*Reels (2-3x/week):*
- Procedure narration during treatment (with verbal consent documented)
- "A day at [Practice Name]" — behind-the-scenes office and team culture
- Before/after reveal with transformation music — consistently high-performing format
- Myth-busting: "5 filler myths I hear every day as an injector"
- Client testimonial interview (not staged — authentic, on-phone format)

*Stories (daily):*
- Today's appointment slots available (drives same-day bookings)
- Client countdown to result reveal (before → day 3 → day 14)
- Poll: "Have you ever had [treatment]?"
- Q&A: "Ask me anything about [service]"
- Flash deals or last-minute availability

**TikTok (3-5x/week — rapidly becoming the #1 discovery channel for aesthetics under 40):**
- "Things I wish I knew before getting filler" — high-share format
- "Watching me do [treatment] start to finish" — procedure transparency builds trust
- Myth-busting: "You do NOT need filler to fix [concern]" — drives consultation bookings
- Before/after transformation videos (add-before-after text overlay)
- "Day in the life of a med spa injector" — career content that drives client trust
- React to viral aesthetics content / misinformation

**Google Business Profile Posts (1x/week):**
- Service feature: "We now offer [treatment] — here's what it does"
- Seasonal promotion: "Pre-summer Botox appointments available — book online"
- Team spotlight: "Meet [Injector Name], our newest aesthetic nurse"
- Before/after with caption (HIPAA release obtained)

**Facebook (3x/week — older demographic; wellness hybrid clients; VIP community):**
- Share Instagram content (cross-post carousels and Reels)
- Community events and charity partnerships
- Longer-form before/after stories with educational context
- Membership/VIP program recruitment posts

**Email/SMS (2–4x/month):**
- Monthly "What's trending at [Practice]" newsletter
- Rebooking reminders: "Your Botox results typically start to fade around week 10–12 — book before the rush"
- Membership enrollment campaigns
- Seasonal treatment reminders (holiday glow-up, summer prep)
- Treatment-specific cycle reminders: "It's been 4 months since your last neurotoxin — ready to rebook?"

### 3.3 Med Spa Content Calendar — Seasonal Framework

| Month | Theme | Priority Content Play |
|-------|-------|----------------------|
| January | New Year New You | "2025 treatment goals" campaign; consultation offer; before/after transformation series |
| February | Valentine's Day | Lip enhancement promotions; "treat yourself" messaging; couples/self-love angle |
| March | Spring Skin Prep | Laser and skin resurfacing; post-winter skin education; BBL/Moxi content |
| April | Pre-Summer Body | Body contouring push (CoolSculpting, Emsculpt); swimsuit season content |
| May | Pre-Summer Glow | Botox and filler season opener; "summer ready skin" campaign; before/afters |
| June | Summer Maintenance | Touch-up and maintenance messaging; existing client rebooking push; hydration facials |
| July–August | Summer Hold | Low marketing spend; focus on existing client retention; Staff education content |
| September | Post-Summer Recovery | Skin repair after summer; laser season begins; pigmentation and sun damage content |
| October | Pre-Holiday Glow | Full treatment menu push; "holiday party ready" campaign; combination package promotion |
| November | Peak Season | Highest ad spend month; all channels active; Black Friday membership deal; gift card push |
| December 1–14 | Gift of Aesthetics | Gift card promotion; year-end membership; last holiday appointment slots |
| December 15–31 | HOLD | Staff booked solid; reduce ads; no heavy outreach; minimal social |

---

## Phase 4: Med Spa SEO Framework

### 4.1 Local SEO Priority Areas

**Google Business Profile:**
- 100% completion: name, address, phone, website, hours, services, photos, booking link
- Services listed by treatment category: injectables (neurotoxin, filler), laser, body contouring, facials, skincare
- 50+ photos: before/afters (HIPAA-compliant), facility, injectors, equipment, events
- Review velocity: 2–4/month minimum
- Weekly Google Posts: service features, promotions, provider spotlights
- Q&A populated: "Do you do lip filler?" "How much is Botox?" "Are you taking new clients?"

**Website Local SEO — High-Value Keyword Targets:**
| Keyword | Monthly Volume Range | Notes |
|---------|---------------------|-------|
| "Botox [city]" | High | Core conversion term |
| "med spa [city]" | High | Category-level term |
| "lip filler [city]" | Medium-High | Trendy; strong conversion intent |
| "Morpheus8 [city]" / "[Device] [city]" | Medium | Device-specific; less competition |
| "medical spa near me" | High | High intent |
| "Juvederm [city]" / "Restylane [city]" | Medium | Brand-specific searches |
| "CoolSculpting [city]" / "Emsculpt [city]" | Medium | Device + location |
| "aesthetic nurse [city]" / "NP injector [city]" | Low | Qualification-seeking clients |

**Service Page SEO Rules for Med Spa:**
- Each service needs its own dedicated page (not one "injectables" page listing everything)
- Individual pages: Botox, Dysport, lip filler, cheek filler, Morpheus8, BBL, CoolSculpting, etc.
- Each page: 400+ words, before/afters, FAQ section, pricing range (even if approximate), booking CTA
- Schema markup: MedicalProcedure + LocalBusiness + MedicalOrganization

---

## Phase 5: Med Spa Paid Advertising

### 5.1 Meta Ads (Facebook/Instagram) — Primary Paid Channel

**Campaign 1: New Client Consultation**
- Objective: Lead generation or traffic to booking page
- Audience: Women 25–55, homeowners, household income $75K+, within 15-mile radius; interest: skincare, beauty, aesthetics, Botox
- Creative: Before/after carousel OR 30-second Reel of treatment process
- Offer: "Free consultation this month" or "Complimentary skin assessment"
- Budget: $800–$2,000/month
- Expected CPL: $20–$60

**Campaign 2: Retargeting (website visitors + Instagram engagers)**
- Audience: Visited website in last 30 days OR engaged with Instagram in last 60 days
- Creative: Social proof (review screenshot) + urgency ("Last spots this week")
- Offer: Appointment booking CTA — no discount required
- Budget: $200–$500/month
- Expected CPL: $10–$30

**Campaign 3: Membership / VIP Enrollment**
- Audience: Current client custom audience (email list) + lookalike of high-LTV clients
- Creative: "What [Practice] VIP members get every month — and why it pays for itself"
- CTA: "Join the VIP program"
- Budget: $300–$800/month

**Campaign 4: High-Value Device Services**
- Audience: Homeowners 35-65, skin treatment interests, within 20 miles
- Creative: Before/after Morpheus8 / CoolSculpting / specific device content
- Offer: Free consultation for device service (higher case value justifies higher CPL)
- Budget: $500–$1,500/month per device
- Expected CPL: $30–$100 (justified by $800–$3,000+ case value)

**What NOT to advertise on Meta:**
- "20% off Botox" or direct discount ads → trains clients to wait for deals → kills full-price retention
- Before/after in a way that promises specific results → FTC violation risk
- Medical claims ("fixes," "cures," "eliminates") → FDA issue for laser and device marketing

### 5.2 Google Search Ads for Med Spa

**Campaign 1: High-Intent Treatment Searches**
- Keywords: "Botox [city]," "lip filler [city]," "med spa near me," "Morpheus8 [city]"
- CTA: "Book Your Consultation — Same-Week Availability"
- CPC range: $2–$12; CPL: $30–$100

**Campaign 2: Device-Specific**
- Keywords: "[Device name] [city]" for owned devices (Morpheus8, CoolSculpting, Emsculpt, BBL, etc.)
- Landing page: Dedicated device service page with before/after and booking CTA
- CPC range: $1–$6

**Google Ad Compliance Note:** FDA prohibits certain claims for laser, energy-based devices, and injectables. Ads cannot contain: "proven to," "eliminates [condition]," "cures." Language must be factual and not imply guaranteed outcomes.

---

## Phase 6: Influencer Marketing for Med Spa

### 6.1 The Med Spa Influencer Tier System

| Tier | Follower Range | Format | Best For | Cost Range |
|------|---------------|--------|----------|------------|
| **Nano-influencer** | 1K–10K | Authentic before/after + caption | Local reach, high trust, best ROI | Trade treatment ($200–$600 value) or $100–$300 cash |
| **Micro-influencer** | 10K–100K | Reel + Stories | Broader city-level reach; strong conversion | Trade + $300–$1,000 |
| **Mid-tier influencer** | 100K–500K | Reel + dedicated post | Multi-city awareness; brand elevation | $1,000–$5,000 |
| **Macro-influencer** | 500K+ | Full campaign | Brand awareness; rarely generates direct new client conversion | $5,000–$25,000+ |

**Best practice for med spa influencer marketing:**
- Always nano/micro first — local reach and authentic trust outperform follower count for aesthetic services
- Structure as trade (free treatment = content deliverable) before cash payment
- Require: 1 Reel + 3 Stories + before/after photo at minimum
- FTC disclosure required: "#ad," "#sponsored," or "gifted" — non-negotiable
- Contract must include: usage rights for repurposing content on practice's channels (critical — this is how you extend ROI)
- Avoid: influencers who work with 3+ competing med spas in the same city simultaneously

### 6.2 Influencer Outreach Script (Instagram DM)

```
"Hi [Name] — I love your content and noticed you're based in [city].
We're [Practice Name], a med spa specializing in [2 services].
We'd love to offer you a complimentary [treatment] in exchange for
an honest Reel and a few Stories showing your experience.
Would this be something you'd be interested in?"
```

---

## Phase 7: Client Retention & Rebooking Marketing

### 7.1 The Retention Imperative

**Why retention is the #1 marketing lever for med spas:**
- New client acquisition cost: $80–$200 per lead
- Existing client rebooking cost: near zero
- First-time client rebooking rate, industry average: 40–55%
- Top-performing practices: 65–75% first-visit rebooking rate
- At $450 average ticket, every 10-point improvement in rebooking rate on a 100-new-client month = $4,500/month in additional revenue

**The discount trap:** Running frequent promotions attracts discount-seeking clients who do not rebook at full price. Average rebooking rate for discount-acquired clients: 22%. For organically acquired clients: 68%. This is the single most important marketing insight for med spas.

### 7.2 Retention Sequences via EMR/Zenoti

**Neurotoxin Retention Cycle (Botox/Dysport — treatment cycle: 3–4 months):**
- Day 0 (visit close): "Thank you for visiting [Practice] today. Your next treatment is recommended in 3–4 months. We'll remind you when it's time!"
- Month 3 (week 1): "It's been 3 months since your neurotoxin treatment — your results may be starting to relax. Ready to book?"
- Month 3 (week 3): "Most clients rebook within weeks of first results fading — here's our next availability"
- Month 4: "Your Botox results are approximately 4 months old — we recommend not waiting past this point to maintain your result"

**Filler Retention Cycle (Filler — treatment cycle: 6–18 months by area):**
- 1-week post-visit: Check-in text (genuine care: "How are your results looking?")
- Month 6 (for lip filler): "Lip filler typically needs a touch-up at 6–9 months. Here's our availability."
- Month 12 (for cheek/jawline filler): "Your cheek filler may benefit from a touch-up at 12 months. Let's assess at your next visit."

**VIP/Membership Enrollment Sequence:**
- Email 1 (day after first visit): "Welcome — did you know [Practice] VIP members save 15% on every treatment?"
- Email 2 (2 weeks post-visit): "Membership math: at your current treatment cadence, VIP pays for itself in [X] treatments"
- Email 3 (30 days post-visit): "Last invitation — enrollment closes [date] or spots limited"

---

## Phase 8: Review Strategy for Med Spa

### 8.1 Med Spa Review Benchmarks

| Platform | Minimum Rating | Minimum Reviews | Velocity Target |
|----------|---------------|-----------------|-----------------|
| Google | 4.4+ | 50+ | 3–5/month |
| RealSelf | 4.0+ | 15+ | 1–2/month |
| Yelp | 4.2+ | 25+ | 1–2/month |
| Facebook | 4.4+ | 30+ | 1–2/month |

### 8.2 Review Generation for Med Spa

**Timing matters:** The best moment to request a review is at the "reveal moment" — when the client first sees their result in the mirror. This is the highest-emotion, highest-satisfaction moment of the entire client journey.

**At-mirror script:** "Your results look incredible. Moments like this are why we love what we do — would you be willing to leave us a quick Google review? It only takes a minute and means the world to us."

**Post-visit text (2 hours after visit):**
"Hi [Name] — you looked absolutely stunning today! We hope you're loving your [treatment] results. If you have a moment, we'd love a Google review: [link]"

**RealSelf:** Request separately. Clients on RealSelf are in research mode — reviews from real clients carry significant weight. Ask specifically: "If you researched [treatment] on RealSelf, would you be willing to leave a review there? It helps others in your exact situation."

### 8.3 Reputation Monitoring for Med Spa

**Monitor weekly:**
- Google reviews (new reviews + rating change)
- Instagram mentions and tags
- Facebook check-ins and comments
- RealSelf reviews
- Yelp (set up alerts)

**Alert triggers:**
- Any review under 3 stars
- Social media post mentioning practice negatively
- RealSelf review with "not satisfied" rating
- Instagram comment on before/after questioning results

---

## Phase 9: Med Spa Marketing Audit Output

### Scoring Rubric

**Social Media Presence & Engagement (30 points)**
- 25-30: Instagram 3K+ followers with 3%+ engagement, 5+ posts/week, high before/after quality, TikTok active, consistent brand voice
- 18-24: Instagram active with good content, 1-3% engagement, 3-5 posts/week
- 10-17: Instagram present but inconsistent posting, under 1% engagement, no TikTok
- 0-9: No active social presence or abandoned accounts

**New Client Conversion (25 points)**
- 21-25: Online booking live (under 3 clicks from homepage), consultation CTA clear on every service page, Instagram bio link to booking, mobile-optimized
- 15-20: Booking available but friction, CTA present on homepage
- 8-14: Phone-only or "contact us" form, no clear consultation path
- 0-7: No CTA, generic contact form, no mobile optimization

**Content Quality & Compliance (20 points)**
- 17-20: HIPAA-compliant before/after gallery with signed releases documented, deep individual service pages, video testimonials, device credibility content
- 12-16: Before/after gallery present, adequate service descriptions
- 6-11: Limited before/after content, generic service pages, stock photos
- 0-5: No before/after content, thin service pages, compliance risks visible

**Reputation & Reviews (15 points)**
- 13-15: 4.5+ Google rating, 60+ reviews, 3+/month velocity, responds to all reviews, active RealSelf profile
- 9-12: 4.0+ rating, 30+ reviews, responds to most
- 5-8: 3.8–4.0 rating, 15-30 reviews, inconsistent responses
- 0-4: Under 3.8 rating or under 15 reviews

**Retention Marketing (10 points)**
- 9-10: Automated rebooking sequences active, VIP/membership program marketed, Alle/Aspire co-marketing utilized, treatment cycle reminders in place
- 6-8: Some email marketing, basic recall sequences
- 3-5: Manual follow-up only, no automated retention
- 0-2: No retention marketing strategy

---

## Output Format: MEDSPA-MARKETING-AUDIT.md

```markdown
# Med Spa Marketing Audit: [Practice Name]
**URL:** [url]
**Instagram:** @[handle]
**Facebook Ad Library:** [Active ads: Yes/No — promotion type]
**Date:** [current date]
**Practice Type:** [Injection boutique / Full-service / Device-focused / Hybrid]
**Independence:** [Confirmed Independent / Franchise — See Note]
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3-5 paragraphs. Open with the score and what it means for new client flow and retention.
Flag the discount dependency immediately if detected in Facebook Ad Library.
Lead with the Instagram opportunity — this is the most impactful lever for most practices.
Revenue impact framing:
"Your Instagram engagement rate of X% on X followers suggests Y clients are discovering
your practice monthly through social. Increasing posting frequency to 5x/week and shifting
content to 60% before/after format could realistically add Z additional consultation
requests per month at [practice]'s average ticket of $X."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Social Media Presence | X/100 | 30% | X | [one-line finding] |
| New Client Conversion | X/100 | 25% | X | [one-line finding] |
| Content Quality & Compliance | X/100 | 20% | X | [one-line finding] |
| Reputation & Reviews | X/100 | 15% | X | [one-line finding] |
| Retention Marketing | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## ⚠️ Discount Dependency Alert (if applicable)

[If Facebook Ad Library shows active discount promotions:]
"[Practice] is currently running [X] active discount promotions on Facebook/Instagram.
Discount-acquired clients rebook at 22% vs. 68% for organically acquired clients.
This section of the audit addresses the revenue impact and a path toward reducing
discount dependency."

---

## Quick Wins (This Week — No Budget Required)

[Instagram bio update, booking link verification, GBP photo additions, review responses,
service page CTAs, before/after gallery organization by service]

## Strategic Recommendations (This Month)

[Meta ad campaign setup, rebooking email sequence, TikTok channel launch, RealSelf profile,
influencer partnership, membership program marketing]

## Long-Term Initiatives (This Quarter)

[Instagram content system (shooting schedule, editor, 5x/week cadence), SEO service pages,
VIP program restructure, treatment cycle automation, Google Ads expansion]

---

## Platform-by-Platform Analysis

### Instagram
[Follower count, engagement rate, content type analysis, posting frequency, before/after quality,
compliance assessment, Stories activity, Reels performance, benchmark comparison]

### Facebook Ad Library
[Active ads detected, promotion types, estimated spend signals, creative quality,
discount dependency assessment, competitive ad landscape]

### Google Business Profile
[Completion score, photo count, review analysis, posting activity, ranking position estimate]

### TikTok
[Account presence: Yes/No, follower count, content quality, posting frequency, opportunity assessment]

### Website
[Mobile experience, booking flow, service page depth, before/after gallery, SEO assessment]

### Reputation & Reviews
[Platform-by-platform rating and review count, velocity analysis, response rate, RealSelf status]

### Email & Retention Marketing
[EMR integration detected, rebooking sequence assessment, membership marketing, Alle/Aspire utilization]

---

## Competitor Comparison

| Factor | [Practice] | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-----------|-------------|-------------|-------------|
| Instagram Followers | | | | |
| Instagram Engagement Rate | | | | |
| Google Rating | | | | |
| Active Facebook Ads | | | | |
| Online Booking Available | | | | |
| Membership Program | | | | |
| RealSelf Active | | | | |

---

## Revenue Impact Model

| Improvement | Est. Impact | Monthly Revenue |
|------------|-------------|-----------------|
| Instagram 5x/week + before/after focus | +8-15 consultations/month | $3,600–$6,750 |
| Rebooking sequence (improve rate 10 pts) | +10 returning clients/month | $4,500 |
| VIP membership enrollment (10 members) | Predictable monthly revenue | $5,000–$8,000 |
| Meta Ads launch ($1,500 budget) | +12-20 consultations/month | $5,400–$9,000 |
| Reduce discount dependency | +$X from full-price rebooking | +18% LTV per client |
| **Total Potential** | | **$18,500–$33,250/month** |

*Generated by AI Marketing Suite — Med Spa Vertical | `/market audit <url>`*
```

---

## Compliance Notes for Med Spa Marketing

**Always flag these in audit output:**

1. **Before/after photos — HIPAA release required**: Patient images used in marketing require a written, HIPAA-compliant authorization that specifies: (a) what information is being disclosed, (b) the purpose (marketing), (c) expiration date. Generic release forms on intake paperwork are often insufficient. State-specific requirements vary.

2. **FDA device advertising claims**: Laser and energy-based device marketing cannot include uncleared claims. "Eliminates fat cells permanently" for CoolSculpting is cleared. "Cures cellulite" is not. "Reduces the appearance of wrinkles" is acceptable. "Reverses aging" is not. Flag any absolute or cure-language claims in website or ad copy.

3. **Scope of practice advertising**: NPs and PAs practicing independently or directing a med spa have state-specific scope restrictions. Advertising "medical director" for a non-physician in states where this is prohibited is an advertising violation. Review state medical board rules before auditing provider credential claims.

4. **Allergan/Galderma co-marketing rules**: Alle and Aspire manufacturer co-marketing programs have strict guidelines about how their brands can be referenced in practice marketing. Review co-marketing agreements before referencing "official Allergan partner" or similar claims.

5. **FTC endorsements**: Client testimonials, before/after photos, and influencer content must reflect typical results. If the featured result is atypical, disclosure is required: "Results not typical. Individual results may vary." This is especially important for device treatments with variable outcomes.

6. **Incentivized reviews**: Never offer treatment discounts, credits, or gifts in exchange for reviews on Google, Yelp, or RealSelf. Platform violations + FTC exposure. Flag immediately if detected.

---

*Generated by AI Sales Team — Med Spa Vertical | `/market <command> <medspa-url>`*
