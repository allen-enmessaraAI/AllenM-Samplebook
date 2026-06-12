# AI Marketing Suite — Dental Practices
# Vertical: General Dentistry / Dental Specialty
# Base skill: market | Patched for: independent dental offices, group practices, DSO-independent

## Vertical Context

VERTICAL: Dental Practices
PRACTICE TYPES: Solo-doctor general dentistry, multi-doctor group practice, specialty (orthodontics, oral surgery, pediatric, periodontics, endodontics)
CORPORATE GATE: Before any marketing analysis, confirm independence. Aspen Dental, Heartland Dental, Pacific Dental Services, Western Dental, Affordable Dentures = DSO-managed → marketing decisions made at corporate level → redirect conversation to DSO marketing team
BUYER FOR MARKETING SERVICES: Office Manager (day-to-day) + Dentist-Owner (budget approval). Marketing decisions are made by the dentist-owner for practices under $2M; above that, office managers often have autonomy up to ~$500/month without approval.
COMPLIANCE CRITICAL: ADA advertising guidelines, state dental board advertising rules, HIPAA (before/after photos require signed release), FTC testimonials/endorsements disclosure, Google review solicitation policies (never offer incentives), no fee-splitting with marketing vendors (illegal in some states)
TERMINOLOGY TO USE: new patient acquisition, case acceptance rate, hygiene recall rate, production per operatory, PPO vs. fee-for-service, treatment plan, active patient count, unscheduled treatment, reactivation, Dentrix/Eaglesoft/Open Dental, CBCT, iTero scanner, in-network, out-of-network, dental membership plan, cosmetic consult, comprehensive exam — never use generic SaaS marketing language
REVENUE BENCHMARKS: $250K–$350K/operatory/year (2-chair practice = ~$600K; 4-chair = ~$1.2M); hygiene should represent 25–35% of practice revenue; new patient goal = 20–30/month for stable growth
SEASONAL PEAKS: January–February (insurance reset — patients who maxed out benefits come back), May–June (school-year-end before summer gap), October–November (use-it-or-lose-it insurance benefits), September (back-to-school rush for pediatric dental)
MARKETING BUDGET BENCHMARK: 3–6% of gross collections for growth-stage practices; 1–3% for maintenance; dental practices at $1M production with 4% budget = ~$40K/year

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full dental practice marketing audit | DENTAL-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second dental practice snapshot | Terminal output |
| `/market copy <url>` | Generate optimized dental website copy | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Patient reactivation + recall sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | Dental social media content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Google Ads + Meta Ads strategy for new patients | AD-CAMPAIGNS.md |
| `/market funnel <url>` | New patient acquisition funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Local competitor dental practices analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | New patient landing page CRO | LANDING-CRO.md |
| `/market launch <service>` | Launch playbook for new service/technology | LAUNCH-PLAYBOOK.md |
| `/market proposal <practice>` | Generate client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full dental marketing report | DENTAL-MARKETING-REPORT.md |
| `/market seo <url>` | Local SEO audit for dental practice | SEO-AUDIT.md |
| `/market brand <url>` | Dental brand voice and positioning | BRAND-VOICE.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. For sub-skill commands, use the dental vertical context to override the base skill's generic B2B logic.

### Full Dental Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with dental-specific mandates:

1. **market-content** (dental lens) → Website copy effectiveness for new patient conversion; service page depth; dentist bio trust signals; before/after gallery compliance; patient education content quality
2. **market-conversion** (dental lens) → Online scheduling friction; new patient form length; phone tracking; appointment request flow; consultation CTA clarity
3. **market-competitive** (dental lens) → Local competitor practice comparison; Google Maps ranking position; review velocity and rating vs. competitors; service differentiation (CEREC same-day crowns, Invisalign, sedation, etc.)
4. **market-technical** (dental lens) → Local SEO optimization; Google Business Profile completeness; NAP consistency across directories; structured data for dental practice (dentist schema); Core Web Vitals; mobile booking experience
5. **market-strategy** (dental lens) → Patient acquisition channels; insurance mix and marketing implications; hygiene recall marketing; membership plan promotion; referral program; review generation system

---

## Dental Marketing Score — Weighted Categories

| Category | Weight | What It Measures in Dental Context |
|----------|--------|--------------------------------------|
| Local Visibility & SEO | 30% | Google Business Profile score, local rankings, directory presence, NAP consistency |
| New Patient Conversion | 25% | Website UX, online scheduling, phone responsiveness, first-impression copy |
| Content & Trust Signals | 20% | Doctor bios, before/after galleries (HIPAA-compliant), patient reviews, service page depth |
| Reputation & Reviews | 15% | Google rating, review velocity, response rate, third-party review profiles |
| Retention & Recall Marketing | 10% | Hygiene recall system, reactivation emails, recall reminder strategy |

**Composite Dental Marketing Score** = Weighted average of all 5 categories

> Note: SEO carries 30% weight (vs. 20% in base skill) because local search is the #1 new patient acquisition channel for dental practices. Paid social is de-emphasized accordingly.

---

## Phase 1: Dental Practice Discovery

### 1.1 Practice Classification

Before any analysis, classify the practice:

| Practice Type | Signals | Marketing Implications |
|--------------|---------|------------------------|
| **Solo GP, insurance-heavy** | 1-2 dentists, PPO listed on website, "we accept most insurances" | New patient volume focus; price sensitivity messaging; convenience differentiators |
| **Solo GP, fee-for-service** | No insurance logos, membership plan mentioned, elective services featured | Premium positioning; quality and relationship differentiators; cosmetic focus |
| **Multi-doctor group** | 3+ dentists listed, multiple locations possible | Consistent brand across providers; scheduling availability as key differentiator |
| **Specialty practice** | Specific specialty listed (ortho, oral surgery, peds, perio, endo) | Referral marketing to GPs + direct patient acquisition; case complexity differentiators |
| **DSO-affiliated** | Corporate branding, standardized website template, HR compliance language | STOP — marketing controlled at corporate level |

### 1.2 Key Pages to Analyze

Map and review all of these for dental practices:
- Homepage (first impression, new patient CTA)
- Services pages (each service = SEO opportunity + case acceptance trigger)
- Team/About page (dentist bio = primary trust signal)
- New Patient page (forms, instructions, insurance info, welcome)
- Before/After gallery (compliance check + trust builder)
- Reviews/Testimonials page
- Blog/Patient Education content
- Contact/Location page (map, hours, phone, parking)
- Online scheduling integration

### 1.3 Dental-Specific Technology Stack Detection

| Technology | Detection Method | Marketing Implication |
|-----------|-----------------|----------------------|
| **Birdeye / Podium** | Source code check, footer mention | Review generation is active |
| **Demandforce / Lighthouse360** | Footer widget, patient communication mention | Recall marketing in place |
| **NexHealth** | Online booking widget | Frictionless scheduling |
| **Google Ads** | SpyFu check, active search ads | Paid acquisition active |
| **Meta Pixel** | Source code | Retargeting active |
| **Open Dental / Dentrix / Eaglesoft** | Job postings often reveal PMS | Backend integration potential |

---

## Phase 2: Dental Channel Strategy

### 2.1 Channel Priority for Dental

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **Google Business Profile** | #1 new patient discovery source — 60%+ of dental searches include "near me" or city | Critical | Free (management time only) |
| **Google Search Ads** | High-intent capture; "dentist near me," "emergency dentist [city]," "Invisalign [city]" | High | $1,500–$5,000/month |
| **Practice Website (SEO)** | Long-term new patient acquisition; service pages + local landing pages | High | SEO investment: $500–$2,000/month |
| **Patient Review Platforms** | Google, Healthgrades, Zocdoc, Yelp, Facebook | High | Reputation management: $200–$500/month |
| **Email — Hygiene Recall** | Highest-ROI channel for existing patients; reactivation of lapsed patients | High | Low cost via PMS integration |
| **Facebook/Instagram Ads** | Cosmetic case generation (Invisalign, veneers, whitening, implants); retargeting | Medium | $500–$2,000/month |
| **Direct Mail** | Counterintuitively effective in dental — new mover lists, radius mailers | Medium | $800–$2,000/campaign |
| **Nextdoor** | Hyper-local community; strong for family dental practices | Medium | Free (organic) to low paid |
| **Referral Program** | Highest close rate and lifetime value of any channel; systematize internal referrals | High | Low cost; gift cards or charity donations |
| **LinkedIn** | Specialist referral marketing (orthodontist to GPsurgeons); not for patient acquisition | Low | Organic only |

### 2.2 Channel Matrix by Practice Type

| Practice Type | Top Channel 1 | Top Channel 2 | Top Channel 3 |
|--------------|---------------|---------------|---------------|
| Solo GP, insurance | Google Business Profile | Google Search Ads | Direct mail (new movers) |
| Solo GP, FFS/cosmetic | Google Search Ads (cosmetic terms) | Instagram/Facebook (before/afters) | SEO (cosmetic dentist [city]) |
| Pediatric | Nextdoor + Facebook | Google Business Profile | School/community sponsorships |
| Orthodontics | Google Search Ads (Invisalign) | Instagram (teen audience) | GP referral network |
| Oral Surgery | GP referral network | Google (emergency/wisdom teeth) | Healthgrades profile |

---

## Phase 3: Dental Content Strategy

### 3.1 Content Pillars for Dental

| Pillar | Theme | Content Types | Ratio |
|--------|-------|---------------|-------|
| **Patient Education** | Oral health tips, procedure explanations, myth-busting | Blog posts, Instagram carousels, short videos | 35% |
| **Social Proof** | Patient testimonials, before/afters, Google review highlights | Instagram posts, website embeds, video testimonials | 25% |
| **Team & Culture** | Doctor introductions, team spotlights, office tours, community involvement | Instagram Stories, Facebook, short-form video | 20% |
| **Promotions & Offers** | New patient specials, whitening promotions, insurance benefit reminders | Email, Google Posts, Facebook ads | 10% |
| **Community** | Local events, charity partnerships, sports sponsorships | Facebook, Nextdoor, Instagram | 10% |

### 3.2 Platform-Specific Dental Content

**Google Business Profile Posts (post weekly):**
- Service highlight posts ("Did you know we offer same-day crowns with CEREC?")
- Seasonal promotions ("Don't let your 2024 dental benefits expire — schedule before December 31")
- Team introductions ("Meet Dr. [Name], our new associate dentist")
- Before/after cases (with HIPAA release)
- Holiday greetings and office hours updates

**Instagram (3-4x/week):**
- Before/after transformations (highest engagement content in dental)
- Procedure education in Reels format (30-60 seconds: "How we place a crown in one visit")
- Team culture content (office birthday, team lunch, certification celebration)
- Patient testimonials in video Story format
- Oral health tips as carousels ("5 foods that stain your teeth")

**Facebook (3x/week):**
- Community involvement and local news sharing
- Patient review shares (screenshot or embed)
- Educational articles (shared from blog or ADA)
- Event promotions (free community screenings, school visits)
- Before/after cases with detailed story captions

**Email (patient database — 2x/month minimum):**
- Monthly newsletter with oral health tips + office updates
- Hygiene recall reminders (automated via PMS integration)
- Insurance benefit expiration reminders (October–November)
- Reactivation campaign for patients not seen in 18+ months
- Post-procedure check-in (automated)

**Direct Mail (2-4x/year):**
- New mover welcome mailer (radius around practice)
- Seasonal promotion mailer (January insurance reset, October use-it-or-lose-it)
- Treatment plan follow-up (for patients who didn't schedule)

### 3.3 Dental Content Calendar — Seasonal Framework

| Month | Theme | Top Content Play |
|-------|-------|-----------------|
| January | New Year, New Smile + Insurance Reset | "Your benefits reset — here's what you get covered" email blast + Google Ads surge |
| February | Valentine's Day Whitening | Whitening promotions; couple before/after; social push |
| March | Spring Checkup | Hygiene recall push; reactivation email to lapsed patients |
| April | Dental Health Month (April in some regions) | Education-heavy content; community event; blog series |
| May | Pre-Summer Cosmetic | Invisalign/whitening/cosmetic consult offers; Instagram push |
| June–July | Back to School Prep (pediatric) | Sealant and checkup promotions; Nextdoor + Facebook |
| August | Back to School | School-age exam and cleaning push; Facebook parent targeting |
| September | Ortho Push | Invisalign promotions; before/after Instagram; teen audience |
| October | Use It or Lose It — Benefits | Email campaign: "You have $X in unused dental benefits" |
| November | Year-End Treatment Planning | Unscheduled treatment follow-up; last-chance insurance messaging |
| December | Holiday Hold (avoid heavy spending) | Maintain GBP posting; light social only; no high-spend ads |

---

## Phase 4: Dental SEO Framework

### 4.1 Local SEO Priority Areas

**Google Business Profile (highest leverage):**
- 100% profile completion (all 8 sections)
- 35+ photos (interior, exterior, team, equipment, before/after)
- Weekly Google Posts
- Review velocity: aim for 2+ new reviews/month
- Q&A populated with common patient questions
- Services listed with descriptions and prices (where permitted)
- Appointment link connected to online scheduler

**Website Local SEO:**
- Homepage title: "[Dr. Name] — [City] Dentist | [Practice Name]"
- H1 must include city name and "dentist" or specialty
- Dedicated location page if multi-location
- Embedded Google Maps iframe on contact page
- NAP (Name, Address, Phone) in footer — exact match to GBP listing
- Service pages for each core service (at minimum: general dentistry, cosmetic, implants, Invisalign)
- City + service landing pages for highest-value keywords: "implants [city]," "Invisalign [city]"

**Key Local SEO Keywords for Dental:**
| Intent | Keyword Examples | Monthly Volume Range |
|--------|-----------------|---------------------|
| Emergency | "emergency dentist [city]," "dentist open now," "toothache [city]" | High — immediate conversion |
| New patient | "dentist near me," "dentist [city]," "family dentist [city]" | Very high |
| Cosmetic | "Invisalign [city]," "veneers [city]," "teeth whitening [city]" | Medium — high value |
| Specific procedure | "dental implants [city]," "wisdom teeth removal [city]," "same-day crowns" | Medium |
| Insurance | "dentists that accept [insurance] [city]," "PPO dentist [city]" | Medium |

**Citation Sources for Dental (NAP must match exactly):**
- Google Business Profile
- Yelp
- Healthgrades
- Zocdoc (if active)
- WebMD Health
- RateMDs
- Facebook Business Page
- Apple Maps
- Bing Places

---

## Phase 5: Dental Paid Advertising

### 5.1 Google Search Ads

**Campaign Structure for Dental:**

**Campaign 1: Emergency / Immediate Need**
- Keywords: "emergency dentist [city]," "dentist open now," "toothache [city]," "broken tooth [city]"
- Match types: Exact and phrase match
- Ad schedule: 24/7 or hours + 2 hours before/after
- CTA: "Call Now — Same-Day Appointments"
- Expected CPC: $8–$25; CPL: $50–$150

**Campaign 2: New Patient Acquisition (General)**
- Keywords: "dentist near me," "family dentist [city]," "best dentist [city]," "new patient dentist"
- Match types: Phrase and modified broad
- CTA: "New Patients Welcome — Book Online"
- Expected CPC: $4–$12; CPL: $40–$120

**Campaign 3: High-Value Services**
- Keywords: "dental implants [city]," "Invisalign [city]," "veneers [city]," "sedation dentist [city]"
- Match types: Exact and phrase match
- CTA: "Free Consultation — [Service Name]"
- Expected CPC: $10–$35; CPL: $80–$200 (justified by higher case value)

**Negative Keywords for Dental Campaigns:**
- veterinary, vet, dog, cat, animal
- dental school, dental hygienist school
- DIY, home remedy
- cheap, free (unless running a promotion)
- jobs, careers, employment

### 5.2 Meta Ads (Facebook/Instagram) for Dental

**Use Case 1: Cosmetic Case Generation**
- Audience: Women 28–54, homeowners, within 10-mile radius
- Creative: Before/after transformation (HIPAA-compliant, patient consent signed)
- Offer: "Free cosmetic consultation — this month only"
- CTA: "Book Free Consult"
- Budget: $500–$1,500/month
- Expected CPL: $25–$80

**Use Case 2: New Mover Targeting**
- Audience: "New movers" demographic in 5-mile radius
- Creative: "Welcome to the neighborhood — taking new patients"
- Offer: New patient special ($X exam + cleaning + X-rays)
- Budget: $300–$800/month

**Use Case 3: Lapsed Patient Reactivation**
- Audience: Custom audience from patient email list (18+ months inactive)
- Creative: "We miss you — your oral health matters"
- Offer: Hygiene visit special
- Budget: $200–$500/month

---

## Phase 6: Reputation Management for Dental

### 6.1 Dental Review Benchmarks

| Platform | Minimum Rating | Minimum Reviews | Review Velocity Target |
|----------|---------------|-----------------|----------------------|
| Google | 4.3+ | 50+ | 2–4 new reviews/month |
| Healthgrades | 4.0+ | 10+ | 1–2/month |
| Yelp | 4.0+ | 15+ | 1/month |
| Facebook | 4.3+ | 20+ | 1–2/month |
| Zocdoc | 4.3+ | 10+ | Ongoing |

### 6.2 Review Generation System

**At checkout (highest conversion point):**
- Front desk hands patient review card with QR code → directly to Google review link
- Never say "leave us a 5-star review" — FTC and Google guidelines prohibit incentivizing
- Script: "If you had a great experience today, we'd really appreciate a Google review — it helps other patients find us"

**Post-visit text (2-hour delay):**
- "Hi [Name], thank you for visiting [Practice]. We hope your experience was excellent! If you'd like to share your thoughts: [short link]"
- Keep under 160 characters (SMS), include practice name

**Automated via PMS or reputation platform:**
- Birdeye, Podium, NiceJob, or Demandforce — connects to PMS and sends post-visit requests automatically
- Target: capture 10–15% of visits as reviews

### 6.3 Review Response Strategy for Dental

**Positive reviews:** Respond within 48 hours, personalize first line, do NOT include specific treatment details (HIPAA), thank and invite back
```
"Thank you so much, [First Name]! We're so glad you had a great experience.
Our team works hard to make every visit comfortable. Looking forward to seeing
you at your next appointment!"
```

**Negative reviews:** Respond within 24 hours, do NOT confirm or deny patient relationship (HIPAA), take offline
```
"We're sorry to hear about your experience. Patient care is our top priority,
and we'd like the opportunity to make this right. Please call us at [phone]
and ask for [name] — we'll take care of you personally."
```

---

## Phase 7: Patient Email Marketing

### 7.1 Dental Email Sequences

**Sequence 1: New Patient Welcome (4 emails)**
- Email 1 (Day 0, after appointment booked): Confirmation + what to bring + directions + team intro
- Email 2 (Day of appointment, -2 hours): "We're looking forward to seeing you today" + parking/entry info
- Email 3 (Day +1, post-visit): Thank you + review request + post-procedure instructions link
- Email 4 (Day +3): "Any questions about your treatment plan?" + soft scheduling CTA

**Sequence 2: Hygiene Recall (3-email automation)**
- Email 1 (6 months after last visit): "Time for your 6-month checkup — your smile will thank you"
- Email 2 (6 months + 3 weeks): "Don't forget — your hygiene visit is overdue"
- Email 3 (6 months + 6 weeks): "Last reminder — plus, your insurance benefits may expire soon"

**Sequence 3: Insurance Benefit Expiration (October–November)**
- Email 1 (October 1): "Your 2024 dental benefits expire December 31 — here's what you have left"
- Email 2 (November 1): "8 weeks left to use your dental benefits — book now"
- Email 3 (December 1): "Final reminder: 31 days left to use your dental benefits"

**Sequence 4: Unscheduled Treatment Reactivation**
- Trigger: Patient has accepted treatment plan but has not scheduled
- Email 1 (Day +7 after consult): "Your treatment plan is ready — just waiting on you"
- Email 2 (Day +21): "Pain-free options available — we can work with your schedule and budget"
- Email 3 (Day +45): "We still have your treatment plan on file — ready when you are"

**Sequence 5: Lapsed Patient Reactivation**
- Trigger: No visit in 18+ months
- Email 1: "We miss you at [Practice Name] — it's been a while"
- Email 2 (2 weeks later): "Are you due for a cleaning? Your oral health matters"
- Email 3 (2 weeks later): "Final note — a special welcome-back offer is waiting for you"

### 7.2 Email Compliance Notes

- HIPAA: Never include treatment details or appointment specifics in subject lines
- CAN-SPAM: Always include unsubscribe link + physical address
- Subject lines: Do not use "FREE" in all caps or medical urgency language ("Your teeth are at risk!") — triggers spam filters
- Best send days for dental patients: Tuesday–Thursday, 9am–11am or 6pm–8pm

---

## Phase 8: Dental Marketing Audit Output

### Scoring Rubric

**Local Visibility & SEO (30 points)**
- 25-30: GBP fully optimized (photos, posts, Q&A, booking link), top-3 map ranking for core terms, 50+ reviews, strong citation profile
- 18-24: GBP mostly complete, ranking page-1 but not top-3, adequate review count
- 10-17: GBP partially complete, page-2 ranking, thin review profile
- 0-9: Incomplete GBP, no local rankings, citation inconsistencies

**New Patient Conversion (25 points)**
- 21-25: Online scheduling live, under 3-click booking, clear new patient offer, phone tracking, mobile-optimized
- 15-20: Online scheduling but friction, clear CTA, good mobile experience
- 8-14: No online scheduling, generic contact form, unclear new patient path
- 0-7: No CTA, phone-only contact, poor mobile experience

**Content & Trust (20 points)**
- 17-20: Detailed dentist bios with photo, video, and credentials; HIPAA-compliant before/after gallery; patient video testimonials; deep service pages
- 12-16: Dentist bio present, some before/after, good service descriptions
- 6-11: Generic bio, few photos, thin service pages
- 0-5: Stock photography, no team photos, minimal content

**Reputation & Reviews (15 points)**
- 13-15: 4.5+ Google rating, 75+ reviews, 2+/month velocity, responds to all reviews
- 9-12: 4.0+ rating, 30+ reviews, responds to most
- 5-8: 3.5–4.0 rating, 15-30 reviews, inconsistent responses
- 0-4: Under 3.5 rating or under 15 reviews

**Retention & Recall Marketing (10 points)**
- 9-10: Automated recall system active, reactivation campaigns running, insurance benefit campaigns documented
- 6-8: Manual recall system, some email marketing
- 3-5: PMS recall reminders only, no email campaigns
- 0-2: No systematic recall marketing

---

## Output Format: DENTAL-MARKETING-AUDIT.md

```markdown
# Dental Practice Marketing Audit: [Practice Name]
**URL:** [url]
**Date:** [current date]
**Practice Type:** [Solo GP / Group / Specialty]
**Insurance Model:** [PPO-heavy / FFS / Mixed]
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3-5 paragraphs. Lead with the score and what it means for new patient flow.
Identify the #1 opportunity (almost always GBP or review velocity for most practices).
Include estimated new patient impact: "Improving your GBP optimization score could
move you from position 4 to top-3 in Maps — at [city]'s average of 120 searches/month
for 'dentist near me,' that's an estimated 8-15 additional new patient inquiries/month."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Local Visibility & SEO | X/100 | 30% | X | [one-line finding] |
| New Patient Conversion | X/100 | 25% | X | [one-line finding] |
| Content & Trust Signals | X/100 | 20% | X | [one-line finding] |
| Reputation & Reviews | X/100 | 15% | X | [one-line finding] |
| Retention & Recall Marketing | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## Quick Wins (This Week — No Budget Required)

[5-10 specific, implementable actions that require no budget and minimal time:
- GBP profile gaps to fill
- Missing photos to add
- Review response scripts
- CTA language fixes on website
- Hours/holiday schedule updates]

## Strategic Recommendations (This Month — Moderate Investment)

[3-7 recommendations with specific implementation paths, expected costs, and patient impact:
- Email recall system setup
- Google Ads launch plan with starter keywords
- Before/after gallery build-out]

## Long-Term Initiatives (This Quarter — Significant Investment)

[2-4 major initiatives with ROI projections:
- SEO content program
- Full reputation management system
- Direct mail + digital retargeting program]

---

## Channel-by-Channel Analysis

### Google Business Profile
[Detailed GBP audit — completion score, photo count, review analysis, posting activity]

### Website & Local SEO
[Page-by-page analysis, keyword rankings, NAP consistency, technical issues]

### Paid Advertising
[Active campaigns detected, estimated spend, landing page quality, recommendations]

### Social Media Presence
[Platform-by-platform audit — follower count, post frequency, engagement quality, content type]

### Reputation & Reviews
[Rating per platform, review velocity, response analysis, competitor comparison]

### Patient Email Marketing
[Recall system assessment, automation detected, list size estimate, campaign cadence]

---

## Competitor Comparison

| Factor | [Practice] | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-----------|-------------|-------------|-------------|
| Google Rating | | | | |
| Google Review Count | | | | |
| GBP Photo Count | | | | |
| Online Scheduling | | | | |
| Website Mobile Score | | | | |
| Social Presence | | | | |
| Active Ads Detected | | | | |

---

## New Patient Revenue Impact Model

| Improvement | Est. Additional New Patients/Month | At $500 Lifetime Value | Annual Revenue Impact |
|------------|-----------------------------------|----------------------|-----------------------|
| GBP top-3 ranking | +5-12 | $500 | $30K–$72K/year |
| Online scheduling friction removed | +2-5 | $500 | $12K–$30K/year |
| Review velocity 2+/month | +3-8 | $500 | $18K–$48K/year |
| Google Ads launch | +8-20 | $500 | $48K–$120K/year |
| **Total Potential** | **+18-45** | | **$108K–$270K/year** |

---

## Recommended 90-Day Marketing Plan

**Month 1 (Foundation):**
- [ ] Complete GBP optimization
- [ ] Launch review generation system
- [ ] Fix website conversion friction points
- [ ] Set up email recall automation

**Month 2 (Visibility):**
- [ ] Launch Google Search Ads (emergency + new patient campaigns)
- [ ] Begin weekly GBP posting cadence
- [ ] Publish 2 service-specific SEO pages
- [ ] Start before/after content calendar

**Month 3 (Acceleration):**
- [ ] Expand Google Ads to cosmetic services
- [ ] Launch Facebook retargeting
- [ ] Begin insurance benefit email series
- [ ] Direct mail new mover campaign

*Generated by AI Marketing Suite — Dental Vertical | `/market audit <url>`*
```

---

## Compliance Notes for Dental Marketing

**Always flag these risks in audit output:**

1. **Before/after photos without HIPAA release**: Common violation. Before posting any patient images, a signed photo release is required. State boards can sanction practices for HIPAA violations in marketing.

2. **Google review incentives**: Offering discounts, gifts, or entry into drawings in exchange for reviews violates Google's policies and FTC endorsement guidelines. If detected, flag immediately.

3. **Misleading claims**: "Best dentist in [city]" or "Most affordable" require substantiation. State dental boards prohibit false or misleading advertising — recommend removing unsubstantiated superlatives.

4. **Fee-splitting disclosure**: Some states require disclosure when a marketing vendor receives a percentage of revenue. Review state dental board advertising rules before structuring performance-based marketing arrangements.

5. **TCPA compliance for SMS**: Patient recall text messages require written consent. PMS-generated texts from existing patient relationships have different rules than new marketing texts.

---

*Generated by AI Sales Team — Dental Vertical | `/market <command> <dental-practice-url>`*
