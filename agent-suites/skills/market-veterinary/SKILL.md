# AI Marketing Suite — Veterinary Practices
# Vertical: Companion Animal / Veterinary Medicine
# Base skill: market | Patched for: independent vet clinics, companion animal hospitals, specialty practices

## Vertical Context

VERTICAL: Veterinary Practices
PRACTICE TYPES: Solo-DVM companion animal clinic, multi-DVM general practice, specialty/referral hospital, emergency clinic, mixed practice (companion + large animal), mobile veterinary service
CORPORATE GATE: Before any marketing analysis, confirm independence. VCA (Mars), Banfield (PetSmart/Mars), National Veterinary Associates (NVA), PetVet Care Centers, BluePearl (Mars), EasyVet, GoodVet = corporate-owned → marketing decisions made at corporate or regional level → pivot to regional manager if engagement continues
BUYER FOR MARKETING SERVICES: Practice Owner (DVM) approves budget. Practice Manager handles execution. DVMs are skeptical of vendor relationships — marketing ROI must be framed in patient care terms, not just revenue ("more wellness visits = better health outcomes for pets")
COMPLIANCE CRITICAL: AVMA guidelines on advertising, state veterinary board advertising rules, VCPR (Veterinary-Client-Patient Relationship) requirements for telemedicine/online advice, FTC testimonials (must disclose material connections), HIPAA does not apply (pets are not covered) but practice may have its own client privacy policy, prescription drug advertising restrictions, CAN-SPAM for emails
TERMINOLOGY TO USE: wellness visit, recheck appointment, compliance rate, heartworm prevention, flea/tick prevention, dental prophylaxis, boarding, grooming, PIMS (AVImark, Cornerstone, ezyVet, Vetspire, Shepherd), client compliance, active patient count, recall protocol, fear-free certified, Fear Free, cat-friendly, AAHA accreditation — never use generic SaaS marketing language
REVENUE BENCHMARKS: $600K–$900K per full-time DVM/year; specialty hospitals $1.5M–$3M+ per specialist; average client transaction value: $150–$300 GP, $800–$2,500 specialty; pharmacy revenue: 15–25% of total practice revenue
SEASONAL PEAKS: Spring (March–May) — heartworm test and prevention season, wellness exam rush; Summer (June–August) — boarding, tick prevention, hot spots, lacerations; Fall (September–October) — dental promotion season, pre-winter wellness; Winter (November–January) — slower for GP, busier for emergency; VMX conference (January — vets traveling)
MARKETING BUDGET BENCHMARK: 1–3% of gross revenue for stable practices; 3–5% for growth-stage; $750K practice at 2% = ~$15K/year

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full veterinary practice marketing audit | VET-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second vet practice snapshot | Terminal output |
| `/market copy <url>` | Generate optimized vet website copy | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Patient recall + compliance sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | Vet social media content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Google Ads + Facebook strategy for new client acquisition | AD-CAMPAIGNS.md |
| `/market funnel <url>` | New client acquisition funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Local competitor vet practice analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | New client landing page CRO | LANDING-CRO.md |
| `/market launch <service>` | Launch playbook for new service/technology | LAUNCH-PLAYBOOK.md |
| `/market proposal <practice>` | Generate client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full veterinary marketing report | VET-MARKETING-REPORT.md |
| `/market seo <url>` | Local SEO audit for vet practice | SEO-AUDIT.md |
| `/market brand <url>` | Vet practice brand voice and positioning | BRAND-VOICE.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. Sub-skill commands use the veterinary vertical context to override base skill generic B2B logic.

### Full Veterinary Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with veterinary-specific mandates:

1. **market-content** (vet lens) → Website copy effectiveness for new client conversion; species-specific service pages; DVM bio trust signals; species photos; content authority (pet health education); Fear Free / AAHA signals
2. **market-conversion** (vet lens) → Online appointment request friction; new client form; phone tracking; species selection flow; appointment type clarity (wellness vs. sick vs. emergency)
3. **market-competitive** (vet lens) → Local competitor clinic analysis; Google Maps ranking; review velocity; differentiators (Fear Free, specialty services, extended hours, species expertise, pharmacy services)
4. **market-technical** (vet lens) → Local SEO for veterinary; Google Business Profile completeness; AVMA and AAHA directory listings; mobile appointment booking experience; PIMS-connected booking widget
5. **market-strategy** (vet lens) → Client acquisition channels; pharmacy retention marketing; wellness plan promotion; compliance marketing; referral program for specialty/GP cross-referral network

---

## Veterinary Marketing Score — Weighted Categories

| Category | Weight | What It Measures in Veterinary Context |
|----------|--------|------------------------------------------|
| Local Visibility & SEO | 30% | Google Business Profile, local rankings, directory presence, species-specific pages |
| New Client Conversion | 25% | Online scheduling, phone responsiveness, new client UX, appointment type clarity |
| Content & Trust Signals | 20% | DVM bios, team photos, patient pet photos (with permission), education content, certifications |
| Reputation & Reviews | 15% | Google rating, review velocity, response rate, Yelp/Facebook profiles |
| Retention & Compliance Marketing | 10% | Recall system, wellness plan marketing, heartworm/prevention compliance campaigns |

**Composite Veterinary Marketing Score** = Weighted average of all 5 categories

> Note: SEO carries 30% weight because 70%+ of new veterinary client searches begin on Google. Instagram and TikTok are growing channels for companion animal practices due to high pet content engagement — social weight is elevated vs. a typical local business.

---

## Phase 1: Veterinary Practice Discovery

### 1.1 Practice Classification

| Practice Type | Signals | Marketing Implications |
|--------------|---------|------------------------|
| **Solo DVM, companion animal** | 1 DVM, dogs + cats listed, "family veterinarian" | Relationship + community focus; availability and convenience differentiators |
| **Multi-DVM companion animal** | 2+ DVMs, appointment availability emphasis | More marketing budget; new client acquisition focus; staff team content |
| **Fear Free / Cat Friendly certified** | Certification listed, specific page or logo | Anxiety-reduction messaging; differentiated patient experience; premium positioning |
| **AAHA accredited** | AAHA logo, accreditation page | Quality and standards messaging; appeals to discerning pet owners |
| **Specialty / Referral hospital** | Specialists listed (cardiologist, oncologist, surgeon, neurologist), "referral accepted" | Dual marketing: GP referral network + direct owner search for complex conditions |
| **Emergency clinic** | 24/7 hours, emergency services, "walk-ins welcome" | Urgency-focused copy; Google emergency terms; always-on paid ads |
| **Large animal / Mixed practice** | Horses, livestock, farm services listed | Entirely different audience; Facebook and agricultural community focus |
| **Corporate-owned** | See gate list above | STOP or pivot to corporate contact |

### 1.2 Key Pages to Analyze

- Homepage (first impression, new client CTA, species clarity)
- Services pages (by species or by service type)
- Team/About page (DVM bios = trust signal #1; technician team inclusion = warmth signal)
- New Client page (form, what to bring, first visit experience)
- Patient portal / online scheduling link
- Pharmacy page (in-house pharmacy = revenue signal; links to Chewy/1-800-PetMeds = leakage signal)
- Wellness plans / preventive care packages
- Species-specific content (separate pages for dogs, cats, exotic pets)
- Reviews / testimonials page
- Blog / pet health education content
- Location / contact / hours page (emergency contact protocol)

### 1.3 Veterinary-Specific Technology Stack Detection

| Technology | Detection Method | Marketing Implication |
|-----------|-----------------|----------------------|
| **VetMatrix / AVID / Vetstreet** | Footer widget, branded recall emails | Recall automation in place |
| **PetDesk** | App mention, "download our app" CTA | Client engagement app active |
| **Petly Plans / VetSuccess** | Wellness plan page, subscription language | Membership-based retention active |
| **IDEXX / VetConnect Plus** | IDEXX lab partner mention | Deep IDEXX integration; influences reminder platform choice |
| **Google Ads** | SpyFu / ad preview check | Paid acquisition active |
| **Chewy Health links** | Pharmacy page external links | Pharmacy revenue leakage signal |
| **Online booking widget** | NexHealth, PetDesk, PIMS native | Frictionless scheduling available |

---

## Phase 2: Veterinary Channel Strategy

### 2.1 Channel Priority for Veterinary

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **Google Business Profile** | #1 new client discovery source — "vet near me" + "veterinarian [city]" | Critical | Free (management time) |
| **Practice Website (SEO)** | Species + service + location pages; "cat vet [city]," "dog dermatologist [city]" | High | $500–$2,000/month |
| **Google Search Ads** | Capture high-intent searches: "emergency vet," "vet near me," "dog dentist [city]" | High | $500–$2,000/month |
| **Facebook** | Community-building; pet owner audience; event promotion; senior pet owner demographic | High | Organic + $200–$800/month paid |
| **Instagram** | Pet photo content; behind-the-scenes; Fear Free moments; team culture | High | Organic (free); critical for Gen Millennial/Z pet owners |
| **TikTok** | Fastest-growing platform for companion animal practices; pet procedure education; vet personality content | Medium-High | Low cost; high reward |
| **Email — Recall & Compliance** | Heartworm/wellness recall; prevention reminders; lapsed client reactivation | High | Low cost via PIMS integration |
| **Nextdoor** | Hyper-local neighborhood community; word-of-mouth amplifier | Medium | Free (organic) |
| **YouTube** | Longer educational content; "how to give your dog a pill," "what to expect at a vet visit" | Medium | Low cost if camera-ready team |
| **Direct Mail** | New mover welcome; seasonal prevention reminders; lower competition than dental | Medium | $600–$1,500/campaign |
| **VIN Community / Veterinary Forums** | Specialty referral network building; long-play warm channel | Low-Medium | Organic only |

### 2.2 Channel Matrix by Practice Type

| Practice Type | Top Channel 1 | Top Channel 2 | Top Channel 3 |
|--------------|---------------|---------------|---------------|
| Solo/small companion animal | Google Business Profile | Instagram/TikTok (pet photos) | Nextdoor (neighborhood) |
| Multi-DVM companion animal | Google Ads (new client) | Facebook (community) | Email recall automation |
| Fear Free / premium positioning | Instagram (experience content) | Google SEO (differentiator terms) | Facebook community groups |
| Emergency clinic | Google Ads (emergency terms, 24/7 schedule) | Google Business Profile (hours prominence) | Maps (directions + phone) |
| Specialty / referral | GP referral network outreach | Healthgrades / specialist directories | LinkedIn (DVM-to-DVM) |
| Large animal / mixed | Facebook (agricultural groups) | Direct mail (rural routes) | Local agricultural events |

---

## Phase 3: Veterinary Content Strategy

### 3.1 Content Pillars for Veterinary

| Pillar | Theme | Content Types | Ratio |
|--------|-------|---------------|-------|
| **Pet Education** | Health tips, preventive care, disease awareness, species-specific advice | Blog posts, Instagram carousels, TikTok, YouTube | 35% |
| **Patient Spotlight** | Pet photos, before/after recovery stories, patient of the month, success stories | Instagram, Facebook, Google Posts | 25% |
| **Team & Culture** | DVM and tech introductions, behind-the-scenes, Fear Free moments, office pets | Instagram Stories, TikTok, Facebook | 20% |
| **Community** | Local events, charity partnerships, shelter support, school visits | Facebook, Nextdoor, Instagram | 10% |
| **Seasonal Promotions** | Heartworm season, dental month, senior wellness, spay/neuter specials | Email, Google Posts, Facebook ads | 10% |

### 3.2 Platform-Specific Veterinary Content

**Google Business Profile Posts (post 1–2x/week):**
- "Heartworm season is here — schedule your dog's annual test and prevention"
- "February is National Pet Dental Health Month — does your pet's breath smell off?"
- "Meet [DVM name], our newest veterinarian — accepting new patients now"
- Patient milestone posts ("Bella the rescue lab is one year cancer-free!")
- Hours and holiday schedule updates

**Instagram (4-5x/week — highest priority platform for vet practices):**
- Pet recovery photos with heartwarming caption (highest engagement content)
- "Day in the life of a vet tech" Reels (30–60 seconds)
- Educational carousels ("5 plants that are toxic to dogs")
- Fear Free procedure videos ("Here's how we use treats to make a nail trim less scary")
- Before/after weight loss or recovery transformations
- Team pet introductions ("Meet Dr. Kim's cat, Mango")

**TikTok (3-5x/week — fastest-growing channel for vet practices):**
- "Things your vet wishes you knew" — short education format, high shareability
- Procedure narration while working ("What I'm checking during a wellness exam")
- Myth-busting: "You do NOT need to wait until spring to start heartworm prevention"
- Funny/heartwarming patient stories (with permission)
- "Vet reacts to [viral pet video]" — reaction format drives high discovery

**Facebook (3-4x/week):**
- Community event participation
- Pet health news articles with practice commentary
- Senior pet care content (Facebook skews older — matches senior pet owner demographic)
- Local shelter shoutouts and adoption shares
- Client-submitted pet photos ("Send us your best summer pet photo")

**Email (client database — 2x/month minimum):**
- Seasonal prevention reminders (heartworm, flea/tick, holiday foods to avoid)
- Wellness plan enrollment invitations
- Monthly pet health tip newsletter
- Automated recall: "Bella is due for her annual wellness exam and heartworm test"
- Reactivation: "We haven't seen [pet name] in over a year — everything okay?"

### 3.3 Veterinary Content Calendar — Seasonal Framework

| Month | Theme | Top Content Play |
|-------|-------|-----------------|
| January | New Year Pet Resolutions + Recovery (post-holiday) | "New Year pet health goals"; dental month preview |
| February | Pet Dental Health Month | Dental promotion; before/after dental cleaning content; "bad breath = dental disease" education |
| March | Heartworm Awareness Month Begins | Heartworm test + prevention campaign; "missed winter month? Here's why year-round matters" |
| April | Heartworm Awareness Month + Spring wellness | Annual wellness visit push; tick prevention for hiking season |
| May | Outdoor safety + parasite season | "Top 5 summer pet dangers"; flea/tick content; outdoor adventure pet photos |
| June | Summer heat safety | Heat stroke awareness; pool safety for dogs; traveling with pets |
| July | National Lost Pet Prevention Month + Summer | Microchipping promotion; ID tag check; summer boarding |
| August | Back-to-school / Separation Anxiety | Pet anxiety content; behavior and enrichment tips; school schedule adjustment |
| September | Senior Pet Wellness Month | Senior wellness packages; arthritis content; senior pet love stories |
| October | Dental promotions (pre-holidays) + pet Halloween safety | Halloween pet safety (costumes, candy toxicity); dental awareness |
| November | National Pet Cancer Awareness Month | Lump check content; early detection messaging; cancer survivor stories |
| December | Holiday pet safety + year-end | Holiday food hazards; "give the gift of veterinary care"; thank-you client messages |

---

## Phase 4: Veterinary SEO Framework

### 4.1 Local SEO Priority Areas

**Google Business Profile (highest leverage):**
- 100% profile completion (hours, species served, services, payment methods, booking link)
- 40+ photos (team photos, facility photos, patient pets with permission, equipment)
- Weekly Google Posts (seasonal content, promotions, new DVM announcements)
- Review velocity: 2–3 new reviews/month minimum
- Q&A section populated: "Do you see cats?" "Do you offer payment plans?" "Are you Fear Free?"
- Services listed: wellness exams, vaccinations, surgery, dental, emergency, each species
- Booking link connected to online scheduler

**Website Local SEO:**
- Title tag: "[City] Veterinarian | [Practice Name] | Accepting New Patients"
- H1 must include city name and "veterinarian" or specialty
- Species-specific service pages: "Dog Vet in [City]," "Cat Vet in [City]," "Exotic Pet Vet"
- Emergency services page: "Emergency Vet [City]" (even for GP practices with same-day sick visits)
- NAP in footer matching GBP exactly
- Schema markup: Veterinary schema (VeterinaryCare) + LocalBusiness + MedicalOrganization

**Key Local SEO Keywords for Veterinary:**
| Intent | Keyword Examples | Notes |
|--------|-----------------|-------|
| Emergency | "emergency vet [city]," "24 hour vet [city]," "vet open now" | High urgency, high conversion |
| New client | "vet near me," "veterinarian [city]," "animal clinic [city]" | Highest volume |
| Species-specific | "cat vet [city]," "dog vet [city]," "exotic pet vet [city]" | Medium volume, high relevance |
| Service-specific | "dog dental [city]," "spay neuter [city]," "heartworm test [city]" | Lower volume, high intent |
| Differentiator | "Fear Free vet [city]," "AAHA vet [city]," "fear free veterinarian" | Low volume, premium client signal |
| Specialty | "veterinary cardiologist [city]," "canine oncologist [city]" | Low volume, very high value |

**Citation Sources for Veterinary:**
- Google Business Profile
- Yelp
- Facebook Business Page
- VetRatingz
- Healthgrades (if applicable)
- Nextdoor Business
- Yellow Pages
- Apple Maps
- AVMA member directory (if listed)
- AAHA member directory (if accredited)

---

## Phase 5: Veterinary Paid Advertising

### 5.1 Google Search Ads for Veterinary

**Campaign 1: Emergency / Urgent Care**
- Keywords: "emergency vet [city]," "vet open now [city]," "sick dog [city]," "sick cat vet"
- Ad schedule: 24/7 (or extended hours if applicable)
- CTA: "Call Now — Same-Day Sick Visits"
- CPC range: $3–$15; CPL: $30–$100

**Campaign 2: New Client Acquisition**
- Keywords: "vet near me," "veterinarian [city]," "animal hospital [city]," "pet doctor [city]"
- CTA: "Welcoming New Patients — Book Online"
- CPC range: $2–$8; CPL: $25–$80

**Campaign 3: Seasonal Prevention**
- Keywords: "heartworm test [city]," "dog flea prevention [city]," "tick prevention dogs [city]"
- Run heavily: March–June
- CTA: "Schedule Heartworm Test — Spring Special"
- CPC range: $1–$5

**Campaign 4: Specialty / Differentiator**
- Keywords: "Fear Free vet [city]," "cat-only vet [city]," "AAHA accredited vet [city]"
- Run continuously for brand positioning
- CPC range: $1–$4 (low competition niche terms)

**Negative Keywords for Vet Campaigns:**
- human doctor, human health, human medical
- DIY, home treatment (unless creating awareness content)
- free, no cost (unless running a promotion)
- veterinary school, vet tech school, jobs, careers
- exotic (unless practice offers exotic services)

### 5.2 Facebook/Instagram Ads for Veterinary

**Use Case 1: New Client Acquisition**
- Audience: Pet owners (Facebook interest targeting: dogs, cats, pets), within 10-mile radius
- Creative: Happy patient photo with DVM and pet owner; or team photo with tagline
- Offer: "New client exam special — [price]"
- Budget: $300–$1,000/month

**Use Case 2: Heartworm/Prevention Season Push (March–June)**
- Audience: Dog owners in service area
- Creative: Mosquito danger infographic or short video ("This is a heartworm — this is your dog's heart without prevention")
- CTA: "Schedule a Heartworm Test"
- Budget: $200–$500/month for 4 months

**Use Case 3: Dental Month (February)**
- Audience: All pet owners in service area
- Creative: Before/after dental cleaning (pet, not human — no HIPAA concern)
- Offer: "February dental cleaning special — $X off dental prophylaxis"
- Budget: $200–$500/month for February only

**Use Case 4: Lapsed Client Reactivation**
- Audience: Custom audience from client email list (18+ months inactive)
- Creative: Pet photo with "We miss [pet name]" messaging
- CTA: "Is it time for [pet's name]'s annual checkup?"
- Budget: $150–$300/month

---

## Phase 6: Reputation Management for Veterinary

### 6.1 Veterinary Review Benchmarks

| Platform | Minimum Rating | Minimum Reviews | Velocity Target |
|----------|---------------|-----------------|-----------------|
| Google | 4.3+ | 40+ | 2–3 new/month |
| Yelp | 4.0+ | 15+ | 1/month |
| Facebook | 4.3+ | 25+ | 1–2/month |
| VetRatingz | 4.0+ | 10+ | Ongoing |

### 6.2 Review Generation for Veterinary

**Emotional timing (unique to vet):** Pet owners are most likely to leave a positive review immediately after an emotionally positive visit — a puppy vaccine appointment, a successful surgery recovery, or a post-euthanasia compassionate experience (counter-intuitive but true).

**At checkout:**
- Front desk hands review QR card → direct link to Google review
- Script: "We're so glad [pet name] did great today — if you have a moment, we'd really appreciate a Google review. Other pet owners in [city] use reviews to find us."
- Never: Offer discounts, credits, or any incentive for reviews (FTC + Google violation)

**Post-visit text (2–4 hours after visit):**
- "Hi [Name] — thank you for bringing [pet name] in today! We hope the visit went smoothly. If you'd like to share your experience: [link]"

**Automated review request via PMS/reputation platform:**
- PetDesk, Birdeye, NiceJob — connects to PIMS and triggers review request on visit close
- Target: 8–12% of visits converting to a review

### 6.3 Review Response for Veterinary

**Positive reviews:** Respond within 48 hours. Use pet's name if mentioned. Reinforce the care team.
```
"Thank you so much for sharing this, [Name]! We adore Bella and are so glad
she's feeling better. Dr. [Name] and the whole team really appreciate your
kind words. We'll see you both at the next visit!"
```

**Negative reviews:** Respond within 24 hours. Acknowledge, do not argue, take offline.
```
"We're sorry to hear about your experience, [Name]. We hold ourselves to a
very high standard of care for every pet and owner. We'd love the chance to
make this right — please call us at [phone] and ask for [practice manager name]."
```

**Euthanasia-related reviews:** Always respond with empathy, never defensively.
```
"We're deeply grateful you shared this, [Name]. Saying goodbye to [pet name]
is one of the hardest moments, and we're honored to have been there with your
family. Our hearts are with you."
```

---

## Phase 7: Patient Email Marketing for Veterinary

### 7.1 Veterinary Email Sequences

**Sequence 1: New Client Welcome (4 emails)**
- Email 1 (Appointment confirmed): Confirmation + what to bring + directions + "meet our team" link
- Email 2 (Day of visit, morning): "Looking forward to meeting [pet name] today" + parking + check-in process
- Email 3 (Day +1): Thank you + review request + post-visit care instructions link (if applicable)
- Email 4 (Day +7): "Any questions about [pet name]'s care plan?" + soft recall scheduling CTA

**Sequence 2: Annual Wellness Recall (3-email automation via PIMS)**
- Email 1 (1 month before due): "[Pet name] is due for annual wellness and heartworm test — let's schedule before the spring rush"
- Email 2 (On due date): "[Pet name]'s wellness exam is due today — book online in seconds"
- Email 3 (1 month overdue): "[Pet name] is overdue — their annual health check is important for catching early issues"

**Sequence 3: Heartworm/Prevention Compliance (Spring campaign)**
- Email 1 (March 1): "Mosquito season is coming — is [pet name] protected? Here's what heartworm prevention really means"
- Email 2 (March 15): "Don't wait until you see a mosquito — heartworm is established before symptoms appear"
- Email 3 (April 1): "Last call before peak season — schedule [pet name]'s heartworm test this month"

**Sequence 4: Dental Month (February)**
- Email 1 (February 1): "February is Pet Dental Health Month — does [pet name]'s breath pass the sniff test?"
- Email 2 (February 14): "This Valentine's Day, give [pet name] the gift of a healthy mouth — our dental special runs through February"
- Email 3 (February 24): "One week left: February dental promotion closes soon"

**Sequence 5: Lapsed Client Reactivation**
- Trigger: No visit in 18+ months
- Email 1: "We haven't seen [pet name] in a while — everything okay?"
- Email 2 (2 weeks later): "Annual wellness visits catch problems early — here's what we check"
- Email 3 (2 weeks later): "Final check-in — [pet name]'s records are still with us. Ready to schedule?"

### 7.2 Email Performance Benchmarks for Veterinary

| Metric | Good | Excellent | Note |
|--------|------|-----------|------|
| Open rate | 25–35% | 40%+ | Pet-related subject lines outperform nearly any industry |
| Click rate | 3–8% | 10%+ | Direct scheduling links dramatically increase CTR |
| Recall email conversion | 15–25% | 35%+ | Pets with names in subject line get 20-30% higher open rates |

---

## Phase 8: Veterinary Pharmacy Retention Marketing

### 8.1 The Pharmacy Revenue Problem

**Industry benchmark:** Independent practices lose 30–45% of preventive medication revenue to Chewy, 1-800-PetMeds, and Amazon annually. This represents $50K–$150K+ in annual revenue for an average practice.

**Marketing approach to pharmacy retention:**
- Never frame it as competing with Chewy on price — you can't win that fight
- Frame in-clinic pharmacy as convenience + safety: "When you fill with us, we flag drug interactions with [pet name]'s other medications automatically"
- Online pharmacy portal (Vetsource, VetSource, Covetrus Pulse) = same auto-ship convenience as Chewy, but keeps revenue in-clinic
- Wellness plan bundled prevention = automatic compliance, no Chewy competition

### 8.2 Pharmacy Marketing Tactics

**Website:**
- Add dedicated pharmacy page: "Why Fill With Us?" featuring safety, convenience, and price-match language
- Highlight online pharmacy portal if active
- Embed "refill request" button on pharmacy page

**Email:**
- "Did you know you can get [pet name]'s Heartgard refill delivered straight to your door — and it still supports our practice?"
- Follow up prescription expiration 30 days before lapse
- Auto-ship enrollment email for prevention medications

**In-clinic signage:**
- "Fill your prescriptions here — we verify every refill against [pet name]'s full medical history"
- At checkout: "Would you like to set up a refill reminder for [pet name]'s Heartgard?"

---

## Phase 9: Veterinary Marketing Audit Output

### Scoring Rubric

**Local Visibility & SEO (30 points)**
- 25-30: GBP fully optimized (species, services, photos, booking link, weekly posts), top-3 map ranking, 40+ reviews
- 18-24: GBP mostly complete, page-1 ranking, adequate review count
- 10-17: GBP partially complete, page-2 ranking, thin review profile
- 0-9: Incomplete GBP, no local rankings, citation errors

**New Client Conversion (25 points)**
- 21-25: Online scheduling live, appointment type clarity (wellness vs. sick vs. emergency), clear species indication, mobile-optimized
- 15-20: Scheduling link exists but friction, good first-impression copy
- 8-14: Phone-only contact, unclear species services, no appointment type differentiation
- 0-7: No CTA, confusing website, poor mobile experience

**Content & Trust (20 points)**
- 17-20: DVM bios with photos, pet patient photos (with permission), Fear Free/AAHA credentials visible, deep service pages, patient education blog
- 12-16: Bios and team photos present, adequate service descriptions
- 6-11: Generic bios, stock photography, thin service pages
- 0-5: No team photos, no educational content, no differentiators visible

**Reputation & Reviews (15 points)**
- 13-15: 4.5+ Google rating, 60+ reviews, 2+/month velocity, responds to all
- 9-12: 4.0+ rating, 25+ reviews, responds to most
- 5-8: 3.5–4.0 rating, 10-25 reviews, inconsistent responses
- 0-4: Under 3.5 rating or under 10 reviews

**Retention & Compliance Marketing (10 points)**
- 9-10: Automated recall active, seasonal prevention campaigns documented, pharmacy retention system in place
- 6-8: PIMS-based recall, some email campaigns
- 3-5: Reminder calls only, no automated email campaigns
- 0-2: No systematic recall or compliance marketing

---

## Output Format: VET-MARKETING-AUDIT.md

```markdown
# Veterinary Practice Marketing Audit: [Practice Name]
**URL:** [url]
**Date:** [current date]
**Practice Type:** [Solo DVM / Multi-DVM / Specialty / Emergency]
**Independence:** [Confirmed Independent / Corporate — See Note]
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3-5 paragraphs. Lead with the score and what it means for new client flow and compliance revenue.
Reference the biggest gap (usually GBP optimization or lack of automated recall for most practices).
Include estimated new client and revenue impact:
"Improving your recall email system to an automated 3-touch sequence could recover an estimated
[X]% of lapsed patients. At [practice's] active patient count of ~[estimate], that's
[X] additional annual wellness visits worth ~$[X] in exam + prevention revenue."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Local Visibility & SEO | X/100 | 30% | X | [one-line finding] |
| New Client Conversion | X/100 | 25% | X | [one-line finding] |
| Content & Trust Signals | X/100 | 20% | X | [one-line finding] |
| Reputation & Reviews | X/100 | 15% | X | [one-line finding] |
| Retention & Compliance Marketing | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## Quick Wins (This Week — No Budget Required)

[GBP gaps, missing photos, review response drafts, CTA language, species clarity fixes]

## Strategic Recommendations (This Month)

[Email recall system setup, Google Ads campaigns, blog content plan, pharmacy page build]

## Long-Term Initiatives (This Quarter)

[SEO program, TikTok channel launch, wellness plan marketing, pharmacy retention portal]

---

## Channel Analysis

### Google Business Profile
### Website & Local SEO
### Paid Advertising
### Social Media (Instagram / Facebook / TikTok)
### Reputation & Reviews
### Email & Recall Marketing
### Pharmacy Retention

---

## Competitor Comparison

| Factor | [Practice] | Competitor 1 | Competitor 2 |
|--------|-----------|-------------|-------------|
| Google Rating | | | |
| Google Review Count | | | |
| Online Booking Available | | | |
| Fear Free / AAHA Certified | | | |
| Active Social Media | | | |
| Active Google Ads | | | |

---

## Revenue Impact Model

| Improvement | Est. Impact | Annual Value |
|------------|-------------|--------------|
| GBP top-3 ranking | +5-10 new clients/month | $36K–$72K/year |
| Recall automation | +15-25 annual wellness visits/month | $27K–$45K/year |
| Pharmacy retention portal | Recover 20% of pharmacy leakage | $15K–$40K/year |
| Google Ads launch | +8-15 new clients/month | $58K–$108K/year |
| **Total Potential** | | **$136K–$265K/year** |

*Generated by AI Marketing Suite — Veterinary Vertical | `/market audit <url>`*
```

---

## Compliance Notes for Veterinary Marketing

**Always flag these in audit output:**

1. **Online prescription dispensing**: VCPR requirements — a valid veterinarian-client-patient relationship must exist before dispensing. Online pharmacies and telemedicine prescriptions have state-specific rules. Marketing should not imply prescriptions are dispensed without an established VCPR.

2. **No HIPAA (but practice privacy policy)**: Unlike human medicine, veterinary practices are not HIPAA-covered entities. However, publishing client information (names, emails, photos) without consent can create legal exposure. Pet photos used in marketing require owner consent.

3. **FTC testimonials**: Client testimonials must reflect typical results. "My dog's cancer is in remission!" used as a marketing testimonial implies a typical outcome — must include disclosure if the result is exceptional.

4. **AVMA advertising guidelines**: AVMA's Principles of Veterinary Medical Ethics Section III covers advertising. Prohibits false, deceptive, or misleading advertising. Prohibits fee advertising that could be construed as price-fixing if coordinated.

5. **Controlled substance advertising**: Do not market controlled substances (Schedule II-V) directly to pet owners. Relevant for practices advertising ketamine therapy, certain seizure medications, or pain management protocols.

---

*Generated by AI Sales Team — Veterinary Vertical | `/market <command> <vet-practice-url>`*
