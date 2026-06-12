# Cold Outreach Sequence Generator — Home Services Vertical

## Metadata
- **Title:** Cold Outreach Sequence Generator — Home Services (HVAC · Plumbing · Roofing · Electrical · Pest Control · Landscaping)
- **Invocation:** `/sales outreach home-services` or `/sales outreach <prospect>` when home services context is detected
- **Vertical Config:** `~/.claude/skills/sales/verticals/home-services.md`
- **Base Skill:** `sales-outreach` (do not modify base — this is the home services copy)
- **Input:** A home service business name, URL, Google Business Profile URL, or reference to existing research
- **Output:** `OUTREACH-SEQUENCE-HOME-SERVICES.md` written to the current working directory

---

## Vertical Context Pre-Load

**CRITICAL:** Home service business owners are not corporate buyers. They do not respond to B2B SaaS email sequences. They are dispatching trucks, managing technicians, and handling customer calls — all day, every day. Every word in this outreach must reflect that reality.

**Channel priority for home services (completely different from B2B):**
1. **Phone call** — The #1 most effective channel. Home service owners answer their phones. Use it.
2. **Email** — Works but only if it's under 80 words, reads like a text message, and leads with their Google stats
3. **Facebook Messenger / Facebook Business Page** — Surprisingly effective, especially for owner-operators under 10 trucks
4. **Text/SMS** — High open rate if you have their cell number from Google Business Profile
5. **LinkedIn** — Only effective for larger operators (10+ trucks, has an operations team)

**The cardinal rule:** A home service business owner will give you 8 seconds on email and 20 seconds on the phone. Every sentence must earn the next one.

---

## Phase 1: Personalization Research (Before Writing Anything)

**CRITICAL RULE:** Never write a single word of outreach before completing research. For home services, the single most powerful personalization anchor is their live Google Business Profile data — rating, review count, and last review date. Every email must open with a specific, verifiable observation.

### 1.1 Google Business Profile Research (PRIMARY — unique to home services)

This is the most important research step for home services outreach. Use `WebSearch` to find their Google Business Profile:

```
"[business name] [city] Google reviews"
"[business name] [city] site:google.com"
"[business name] [trade] [city] reviews"
```

Then use `WebFetch` to retrieve the business profile page if available.

**Data to extract from Google Business Profile:**

| Data Point | How to Find | Outreach Use |
|---|---|---|
| **Star Rating** | Directly on profile | Lead with this — it's the #1 pain anchor |
| **Review Count** | Directly on profile | Compare to competitive benchmark (100+ is good, under 50 is an opening) |
| **Last Review Date** | Most recent review timestamp | Recency signals health of review program |
| **Owner Response Rate** | Check if they respond to reviews | Low response rate = no review management system |
| **Response Quality** | Read their actual responses | Poor/copy-paste responses = no system |
| **Recent Negative Reviews** | Read 1-star reviews from last 90 days | Specific pain anchor for outreach |
| **Review Velocity** | Reviews this month vs. 6 months ago | Declining velocity = problem they may not see yet |
| **Google Maps Rank** | Position in local map pack | Do they appear in top 3? |

**Benchmark context to apply:**
- Under 4.5 stars = below local competitive threshold
- Under 75 reviews = losing calls to competitors with more reviews
- Under 10 reviews in last 90 days = no active review generation system
- Zero owner responses = complete reputation blind spot

### 1.2 Competitor Benchmarking Research (unique to home services)

Look up their top 2-3 local competitors on Google Maps. This is the most powerful personalization tool in home services — showing an owner that a competitor outranks them creates immediate urgency.

```
Search: "[trade] [city]" in Google Maps
Look for: companies ranking above the prospect in the local map pack
```

**For each competitor, capture:**
- Star rating
- Review count
- How they rank vs. the prospect

**Use in outreach:** "Your top competitor in [city] has 4.8 stars and 190 reviews — you're at 4.1 and 34 reviews. That gap is costing you calls every day."

### 1.3 Lead Generation Platform Research

Check if they are actively spending on lead generation platforms:

```
Search: "[business name] Angi" or "[business name] HomeAdvisor"
Search: "[business name] Thumbtack"
Check: Google Ad Library for their business name
```

**Signals to look for:**
- Active Angi/HomeAdvisor profile with reviews = confirmed lead gen spend ($500-3K/mo typically)
- Running Google Ads = confirmed digital marketing budget
- No paid presence anywhere = pure referral / cold call opportunity

### 1.4 Website & Digital Presence Research

Use `WebFetch` to retrieve their website (if they have one):

**Data to extract:**

| Element | What It Reveals | Outreach Use |
|---|---|---|
| **Online booking widget** | High sophistication — may have FSM | Tailor pitch to their tech level |
| **Website age / design quality** | Digital maturity | "Your website hasn't been updated since [year]" opener |
| **Review badges** | Active or passive about reputation | |
| **Service area defined** | How large is their operation | |
| **Contact page phone number** | Primary contact method | |
| **About/Team page** | Owner's name and story | Personalize with their name and founding story |

### 1.5 Hiring Signals Research

Active job postings are one of the strongest buying signals in home services:

```
Search: "[business name] jobs Indeed"
Search: "[business name] hiring technician"
Search: "[business name] office manager OR CSR job"
```

**What hiring signals mean:**

| Posting Type | Signal | Outreach Angle |
|---|---|---|
| HVAC/Plumbing/Roofing Technician | Adding trucks, growing revenue | "You're growing — let's make sure the phones keep ringing" |
| Office Manager / CSR | Admin pain, need for systems | "Adding an office manager means your review and scheduling system needs to scale" |
| Dispatcher | High call volume, operational complexity | "Hiring a dispatcher means you're at the volume where systems matter" |
| Multiple positions | Fast growth phase | Growth-mode angle — "invest in reputation before the next truck hits the road" |

### 1.6 Facebook Business Page Research

Many home service owners are more active on Facebook than on any other platform:

```
Search: "[business name] [city] Facebook"
```

**Data to extract:**
- Review count and rating on Facebook
- Recent posts (last 30 days) — what are they talking about?
- Promotion activity (running Facebook Ads?)
- Post engagement — how active is their community?
- Direct message availability

### 1.7 Research Summary

Before writing, compile:

```
HOME SERVICES OUTREACH RESEARCH
================================
Business: [name]
Trade: [HVAC / Plumbing / Roofing / etc.]
Owner Name: [if found]
Location: [city, state]
Estimated Truck Count: [X]

Google Profile:
  Rating: [X.X] ★
  Reviews: [X] total
  Last review: [timeframe]
  Response rate: [yes/no/partial]
  Map pack position: [top 3 / page 2 / not visible]

Top Competitor:
  Name: [name]
  Rating: [X.X] ★
  Reviews: [X]

Lead Gen Spend:
  Angi/HomeAdvisor: [active / not found]
  Google Ads: [active / not found]

Hiring Signal: [none / technician / office manager / multiple]
Website Quality: [good / dated / minimal / none]

Best Outreach Angle: [Google gap / competitor benchmark / Angi cost / hiring signal]
Best Channel: [phone / email / Facebook / text]
Best Timing: [days/times based on trade and season]
```

---

## Phase 1.5: Contact Enrichment Stack — Home Services Vertical

**⚠️ IMPORTANT — Apollo.io is NOT the default enrichment tool for this vertical.**

Apollo's database is built around B2B SaaS, tech, and enterprise contacts. Local home services owner-operators (HVAC companies, plumbers, landscapers, handymen, pool services) are largely absent from Apollo's index. Testing confirmed zero records returned for small LV metro home services businesses even on paid plans. Do not use Apollo for this vertical unless a specific prospect is a multi-location franchise (20+ trucks, regional brand).

---

### Default Enrichment Stack (Home Services SMBs)

Run tools in this priority order. Stop each tool pass when email + mobile are both confirmed.

#### Tool 1: Hunter.io — Email by Domain
**Best for:** Any prospect with a website (WEAK_RATING segment, discovered sites from NO_WEBSITE enrichment)  
**API endpoint:** `GET https://api.hunter.io/v2/domain-search`  
**Free tier:** 25 searches/month per account  
**What it returns:** All email addresses indexed on a domain, email format pattern, confidence score, verification status  
**Phone numbers:** Not provided — phone validation handled by separate tool

```python
# Hunter.io domain search
resp = requests.get(
    "https://api.hunter.io/v2/domain-search",
    params={
        "domain": "businesswebsite.com",
        "api_key": HUNTER_API_KEY,
        "limit": 10,
        "type": "personal",   # prefer personal over generic
    }
)
# Returns: emails[], first_name, last_name, position, confidence, verification status
```

**Filtering rules:**
- Confidence ≥ 70 → use
- Confidence 50–69 → flag as unverified, include with note
- Confidence < 50 → discard
- Skip: info@, contact@, hello@, admin@, support@, noreply@ (generic inboxes — low reply rate)
- Keep: [firstname]@, [firstname.lastname]@, [name]@ (personal patterns)

---

#### Tool 2: Snov.io — Email + LinkedIn by Name + Company
**Best for:** Named contacts without a domain (owner names we confirmed via agent research)  
**API endpoint:** `POST https://api.snov.io/v1/get-emails-from-names`  
**Free tier:** 50 credits/month per account  
**What it returns:** Email addresses matched to full name + company, verification status, LinkedIn URL  
**Phone numbers:** Not provided — use Datagma for phones

```python
# Snov.io name-to-email
resp = requests.post(
    "https://api.snov.io/v1/get-emails-from-names",
    json={
        "access_token": SNOV_ACCESS_TOKEN,
        "first_name": "Lance",
        "last_name": "Koch",
        "domain": "absoluteairnv.com",  # use if known
    }
)
# Returns: emails[], sources, linkedin_profile
```

**Credit cost:** 1 credit per name lookup; verification costs additional credits  
**Stack accounts:** Each free account = 50 credits. Multiple accounts extend coverage.

---

#### Tool 3: Datagma — Phone + Email for SMB Owner-Operators
**Best for:** Finding mobile phone numbers for named owner-operators not indexed in other tools  
**API endpoint:** `GET https://api.datagma.com/api/ingram`  
**Free tier:** Limited credits on signup  
**Strength:** Strong SMB and local business coverage compared to Apollo/ZoomInfo  
**What it returns:** Mobile phone, email, LinkedIn, company firmographics

```python
# Datagma person lookup
resp = requests.get(
    "https://api.datagma.com/api/ingram",
    params={
        "apiId": DATAGMA_API_KEY,
        "fullName": "Ronen Lubaton",
        "companyName": "Open Sesame Garage Door",
        "data": "phone,email",
    }
)
# Returns: phone (with type flag), email, confidence
```

---

#### Tool 4: Phone Type Validation — NumVerify / AbstractAPI
**Purpose:** Validate ALL phone numbers (GMB phones + enriched phones) and flag mobile vs. landline vs. toll-free  
**API:** `GET https://phonevalidation.abstractapi.com/v1/` or NumVerify  
**Free tier:** AbstractAPI = 250 validations/month; NumVerify = 250/month  
**Run this on every phone number in the pipeline — including GMB numbers**

```python
# AbstractAPI phone validation
resp = requests.get(
    "https://phonevalidation.abstractapi.com/v1/",
    params={
        "api_key": ABSTRACT_API_KEY,
        "phone": "7028880842",  # strip formatting
    }
)
# Returns: valid (bool), type ("mobile"|"landline"|"voip"|"toll_free"), carrier, country
```

**Filtering rules:**
- `type == "mobile"` → ✅ keep as primary dial number
- `type == "voip"` → ✅ keep (many owner cells are VOIP/Google Voice)
- `type == "landline"` → ⚠️ keep as fallback, flag `phone_type = landline`
- `type == "toll_free"` OR prefix in (800, 888, 877, 866, 855, 844, 833) → ❌ remove from dialer list
- `valid == false` → ❌ remove

---

### Enrichment Workflow — Step by Step

```
For each hot prospect in hot_prospects_outbound.csv:

1. PHONE VALIDATION (all records):
   → Validate existing GMB phone via AbstractAPI
   → Flag type: mobile / landline / toll_free / voip / invalid
   → Remove toll_free and invalid from dialer list

2. HAS WEBSITE? (WEAK_RATING segment or discovered sites):
   YES → Hunter.io domain search
         → If personal emails found: add to contact_1_email or contact_2_email
         → If only generic: skip, note as "generic_only"

3. NAMED OWNER CONFIRMED?
   YES + domain known → Snov.io name+domain search → email
   YES + no domain    → Snov.io name+company search → email + LinkedIn
   YES (either)       → Datagma name+company → mobile phone

4. NO OWNER NAME:
   → Datagma company search → find decision maker
   → If found: add as contact_1 with source = "datagma"

5. VERIFY & FILTER:
   → Any email returned: check Hunter verification status (or run Snov verify endpoint)
   → Any phone returned: validate via AbstractAPI
   → Drop: toll_free, invalid, confidence < 50

6. WRITE BACK:
   → Update hot_prospects_outbound.csv
   → Update lv_homeservices_crm_ready.csv
   → New columns: hunter_email, snov_email, datagma_phone, datagma_email,
                  phone_type, phone_verified, enrichment_source, apollo_skip_reason
```

---

### Column Additions (Enrichment Pass 2)

| Column | Source | Notes |
|---|---|---|
| `hunter_email` | Hunter.io | Best personal email found on domain |
| `hunter_confidence` | Hunter.io | 0–100 confidence score |
| `snov_email` | Snov.io | Email matched to owner name |
| `snov_linkedin` | Snov.io | LinkedIn URL if found |
| `datagma_email` | Datagma | Email from Datagma |
| `datagma_phone` | Datagma | Mobile phone from Datagma |
| `phone_type` | AbstractAPI | mobile / landline / voip / toll_free / invalid |
| `phone_verified` | AbstractAPI | true / false |
| `best_email` | Merged | Highest-confidence email across all sources |
| `best_phone` | Merged | Best mobile number across GMB + Datagma |
| `enrichment_source` | Script | Which tools returned data |
| `apollo_skip_reason` | Static | "SMB_local_not_indexed" |

---

### API Key Storage (project_config.json — home services campaigns)

```json
"enrichment": {
  "hunter":   { "api_key": "YOUR_HUNTER_KEY" },
  "snov":     { "client_id": "YOUR_SNOV_ID", "client_secret": "YOUR_SNOV_SECRET" },
  "datagma":  { "api_key": "YOUR_DATAGMA_KEY" },
  "abstract": { "api_key": "YOUR_ABSTRACT_KEY" },
  "apollo":   { "skip": true, "reason": "SMB local operators not indexed — wrong database for vertical" }
}
```

---

### Credit Management (Free Tier)

| Tool | Free Credits | Cost Per Call | 68-Record Estimate |
|---|---|---|---|
| Hunter.io | 25/mo/account | 1 per domain search | ~7 calls (websites only) |
| Snov.io | 50/mo/account | 1 per name lookup | ~29 calls (named owners) |
| Datagma | varies/signup | 1 per lookup | ~68 calls |
| AbstractAPI | 250/mo/account | 1 per phone | ~68 calls |

**For 68 hot prospects:** 1 Hunter account + 1 Snov account + 1 Datagma account + 1 AbstractAPI account covers this campaign without overflow. If credits run out mid-run, the script pauses, reports remaining records, and prompts for next API key.

---

## Phase 2: Framework Selection — Home Services Edition

Home services outreach uses a simplified framework selection. The research above almost always points to one dominant angle.

### Framework 1: The Google Gap (use when rating < 4.6 or reviews < 75)

**Structure:**
```
[Their specific Google stat] compared to [local benchmark or competitor stat].
[What that gap costs them in real terms — calls, jobs, revenue].
[Short, specific ask.]
```

**Best for:** The majority of home service prospects. This is the #1 opener because owners know their rating cold and react immediately.

### Framework 2: The Angi Drain (use when active Angi/HomeAdvisor spend is confirmed)

**Structure:**
```
[Acknowledge they're on Angi / paying per lead].
[Reframe: cost per booked job vs. owned inbound].
[Short ask tied to the math.]
```

**Best for:** Owners who are actively frustrated with lead marketplace costs. Opens naturally because the pain is already named.

### Framework 3: The Growth Signal (use when hiring signal is detected)

**Structure:**
```
[Reference their specific hiring activity — "saw you're looking for a tech in [city]"].
[Connect growth to the specific problem it creates — more trucks = more reviews needed, more dispatching complexity, etc.].
[Ask tied to timing — "before the next truck is rolling"].
```

**Best for:** Companies in active growth mode. Creates urgency tied to something happening right now.

### Framework 4: The Competitor Mirror (use when a specific competitor outranks them significantly)

**Structure:**
```
[Name the specific competitor and their stats].
[Show the gap — their rating/reviews vs. the competitor].
[Ask: "want to see how they got there?"]
```

**Best for:** Owners who are competitive by nature (most of them). Seeing a local competitor winning is the fastest way to create urgency.

### Framework Selection Logic for Home Services:

```
Is their Google rating under 4.5 OR review count under 75?
  YES → Framework 1 (The Google Gap)
  NO ↓

Is there confirmed Angi/HomeAdvisor spending?
  YES → Framework 2 (The Angi Drain)
  NO ↓

Is there an active job posting for a tech, CSR, or dispatcher?
  YES → Framework 3 (The Growth Signal)
  NO ↓

Does a local competitor significantly outrank them?
  YES → Framework 4 (The Competitor Mirror)
  NO → Use Framework 1 with industry benchmark instead of personal data
```

---

## Phase 3: The Multi-Channel Home Services Sequence

**Important difference from base skill:** Phone calls are integrated as the primary first touch. Email supports and follows up. The sequence runs 14 days, not 21 — home service owners make decisions faster than corporate buyers.

### Channel Sequence Overview

| Day | Channel | Action | Goal |
|---|---|---|---|
| **Day 0** | Research | Pull Google profile, rating, reviews, competitor data | Arm the call |
| **Day 1** | **Phone Call** | First call — 60-second opener with their Google stats | Get a response or callback |
| **Day 1** | Email | Email 1 — The Google Gap (sent same day as call) | Reinforce the call, give them something to look at |
| **Day 2** | **Phone Call** | Voicemail if no answer — reference the email | Second touch |
| **Day 4** | Email | Email 2 — The Value Add (local benchmark or case study) | Build credibility |
| **Day 7** | Facebook / Text | Facebook Messenger or text (if cell from GBP) | Cross-channel presence |
| **Day 10** | Email | Email 3 — The Social Proof | Peer proof point |
| **Day 14** | **Phone Call + Email** | Final call + Email 4 (Breakup) | Respectful close |

### The Phone Call Scripts (unique to home services — not in base skill)

#### Call 1 — Day 1 Opening Script

**Duration target:** Under 60 seconds for the pitch. If they engage, go with it.

```
"Hey, is this [owner name]? 

This is [your name] — I work with [trade] companies in [city] on their Google presence.

I looked up [business name] before I called — you're sitting at [X] stars with [X] reviews.
Your top competitor in [their zip code], [competitor name], is at 4.8 with [X] reviews.

That gap is costing you calls every week — and it's fixable.

I've got 8 minutes to show you exactly how. When's a good time — Tuesday morning before dispatch, or Thursday before 9?"
```

**If they say "send me an email":**
"Absolutely — checking your inbox now is [your email]. I'll send it in the next 2 minutes. Subject line will say '[business name] Google Rating'. Look for it."
*(Then send Email 1 immediately.)*

**If they say "I'm not interested":**
"Fair enough. Last question before I let you go — what's your Google rating sitting at right now?" *(Their answer re-opens the conversation 40% of the time.)*

**If they say "I'm busy":**
"I hear you — when's a slow morning? Tuesday or Thursday before 9?" *(Give them a specific choice, not an open-ended question.)*

#### Voicemail Script — Day 2

**Under 20 seconds:**

```
"Hey [owner name], this is [your name]. I sent you an email yesterday
about [business name]'s Google rating — subject line '[business name] Google Rating'.
Give it 30 seconds when you get a chance.
If you want to talk, I'm at [phone number]. 
That's [repeat number]. Talk soon."
```

#### Final Call Script — Day 14

```
"Hey [owner name], [your name] again.

I've reached out a couple of times about the Google gap between you
and [competitor name]. I don't want to keep bugging you if the timing's not right.

Two quick questions before I stop calling:
One — is your rating something you're actively working on?
Two — if not, is there a better time of year to circle back?

Happy either way — just don't want to disappear without giving you a chance to say so."
```

---

### Email Writing Rules — Home Services Edition

**Rules that override the base skill:**

1. **Ultra-short:** Under 70 words for emails 1-3. Under 50 for the breakup. Home service owners read on their phone between jobs.
2. **No corporate jargon:** Zero. Not even "reach out," "leverage," or "solution." Say "call," "use," and "fix."
3. **Always lead with their specific number:** Rating, review count, or competitor comparison. Not a generic observation.
4. **Plain text only:** No images, no HTML, no tracking pixels on the first email. It should look like a text from a person.
5. **Phone number in signature:** Home service owners respond to phone as often as email — make it easy to call back.
6. **One ask, one sentence:** The CTA must be answerable in 3 words.

**Subject line rules for home services:**
- Include their business name or city — "Mike's HVAC — Google rating" gets opened more than any generic subject
- Or use their trade + problem: "34 reviews isn't enough in [city]"
- Short, specific, no exclamation marks
- Test: Would this look like a real email from a real person or a marketing blast?

---

### Email 1 — The Google Gap (Day 1)

**Goal:** Show them you did your homework. Create a specific, uncomfortable comparison. Get a response.

**Framework:** Lead with their exact stats → competitor comparison → cost in real terms → one ask.

```
Subject A: [Business name] — Google gap
Subject B: 34 reviews vs. 190 in [city]

[Owner name],

Looked up [business name] before I reached out.
You're at [X.X] stars with [X] reviews.
[Top competitor] in your area is at 4.8 with [X] reviews.

That gap costs you calls every week — people scroll to them first.

I help [trade] companies close that gap in 60 days.
Worth 8 minutes Tuesday morning?

[Your name]
[Phone number]
```

**A/B Opening Variations:**
- A: "Looked up [business name] before I reached out."
- B: "Your Google profile is costing you calls in [city] — here's why."

---

### Email 2 — The Value Add (Day 4)

**Goal:** Give them something useful with zero ask. Build credibility. Prove you know their world.

**Framework:** Industry benchmark or local stat → what it means for them → no CTA (or very soft one).

```
Subject A: what good looks like in [city] [trade]
Subject B: [trade] review benchmark — [city]

[Owner name],

Quick benchmark for [trade] companies in [city]:

Top-ranked shops have 4.7+ stars and 120+ reviews.
They get 3x the Google calls compared to shops under 4.5.

[Business name] is at [X.X] / [X] reviews right now.

That's the gap I'd want to show you how to close.
No pitch — just the numbers.

[Your name]
[Phone]
```

**What to include as a value-add:**
- Local benchmark data (rating and review count of top 3 competitors in their zip code)
- Trade-specific stat ("HVAC companies with 100+ reviews close 12% more calls than those under 50")
- A brief insight about their specific Google profile ("You're not in the local map pack for '[trade] [city]' — I can show you why")

---

### Email 3 — The Social Proof (Day 10)

**Goal:** One contractor story, one specific result, one ask. Peer proof is everything in home services.

**Framework:** Contractor in their trade → specific before/after → why it matters for them → ask.

```
Subject A: [trade] company, [city], 90 days
Subject B: from 3.9 to 4.7 — here's what changed

[Owner name],

[ABC Plumbing] was at 3.9 stars with 28 reviews.
Same situation you're in.

After 90 days: 4.7 stars, 112 reviews, 14 more Google calls per month.
They cut their Angi spend in half.

Same playbook works for [trade] companies in [city].

8 minutes Thursday morning — want to see the before/after?

[Your name]
[Phone]
```

**Case study selection rules for home services:**
- Must be same trade (HVAC case study for HVAC prospect)
- Must be similar truck count / market size
- Must have specific numbers — rating before, rating after, review count, call volume, or revenue impact
- If you have a case study in their specific city or region, use it — local proof converts better than anything

---

### Email 4 — The Breakup (Day 14)

**Goal:** Respectful close. Leave them feeling good. Create just enough FOMO to prompt a response.

**Home services-specific rule:** Home service owners respect directness. The breakup email should be 3-4 sentences max and sound like it came from a real person.

```
Subject A: closing the loop — [business name]
Subject B: not the right time?

[Owner name],

Going to stop reaching out after this — don't want to be that guy.

If your Google rating or review count is something you want to work on
before [upcoming season] hits, I'd love to help.

Either way, here's my cell: [number].
Good luck with the season.

[Your name]
```

**Breakup email timing note:** For HVAC, send this 4-6 weeks before shoulder season. For roofing, send it 4-6 weeks before storm season starts. The seasonal urgency in the breakup converts significantly better than a generic close.

---

## Phase 4: Channel-Specific Touchpoints

### Facebook Messenger (Day 7)

Many home service business owners check their Facebook Business page more than their email. If their Facebook Business page has Messenger enabled:

```
"Hey [owner name] — sent a couple emails about [business name]'s Google rating.
Figured I'd try here since a lot of guys miss emails.

You're at [X.X] stars / [X] reviews right now.
[Competitor] next door is at 4.8 / [X].

Got 8 minutes this week to show you the gap? 
—[Your name], [phone]"
```

**Rules for Facebook Messenger outreach:**
- Keep it under 60 words
- Don't pitch — ask a question
- Use their name, their stats, their competitor
- Include your phone number (many owners prefer to call back)

### Text / SMS (Day 7 — if cell number available from Google Business Profile)

Some owners list their personal cell on their Google Business Profile. If available:

```
"Hi [owner name], [your name] here — I do Google ratings/reviews for [trade] companies in [city].
Noticed [business name] is at [X.X] stars.
[Competitor] up the road is at 4.8.
Worth a quick call? [your number]"
```

**Rules for SMS outreach:**
- Only use if cell number is publicly listed — never use scraped or purchased cell numbers
- Under 160 characters if possible
- Include opt-out: "Reply STOP to not hear from me" at the end

### LinkedIn (Day 10 — for larger operators only, 10+ trucks)

LinkedIn is only relevant for home service businesses with an operations team or corporate structure. For owner-operators, skip LinkedIn entirely.

**Connection note (under 300 characters):**
```
"[Owner name] — saw [business name] is growing in [city].
I work with [trade] companies on their Google presence.
Quick question about your review strategy — mind connecting?"
```

**LinkedIn message (Day 10):**
```
"Hey [owner name] — sent a couple emails last week about [business name]'s
Google profile vs. [competitor]. Not sure if they hit the right inbox.

You're at [X.X] stars / [X] reviews — [competitor] is at 4.8 / [X].

Worth a 10-minute call? I work with [trade] companies in [city] on exactly this.
—[Your name]"
```

---

## Phase 5: Timing Guide — Home Services Edition

This completely replaces the base skill timing section. Timing in home services is governed by trade-specific seasonality, not corporate calendar cycles.

### Best Times to Reach Home Service Owners

| Time | Why It Works |
|---|---|
| **Tue–Thu, 7:30–9:00am** | Before the dispatch chaos starts. Owner is in the office or just arriving. Most focused time of day. |
| **Tue–Thu, 6:00–7:00pm** | After the last job wraps. Owner is reviewing the day, catching up on messages. |
| **Saturday, 8:00–10:00am** | Surprisingly effective for smaller operators — they're working but not slammed. |

### Times to Avoid

| Time | Why |
|---|---|
| **Monday mornings** | Dealing with weekend emergencies and the week's backlog |
| **Friday afternoons** | Mentally done, not interested in new conversations |
| **Peak season mid-day** | Unreachable — phones are ringing off the hook |
| **Dead of slow season** | No cash, depressed, not buying anything |

### Seasonal Timing by Trade

| Trade | Peak Season (avoid for new outreach) | Best Outreach Window |
|---|---|---|
| **HVAC** | June–August (AC), Dec–Jan (heat) | March–May, September–October |
| **Roofing** | May–October (storm season) | February–April, November |
| **Plumbing** | Year-round (no strong peak) | Avoid December holidays |
| **Electrical** | Year-round | Avoid summer if residential AC-heavy market |
| **Pest Control** | March–August | September–November, January–February |
| **Landscaping** | April–October | November–February |
| **Pool Service** | May–September | February–March, October–November |

**The golden rule:** Reach them when they have money in the bank (just post-peak) and time to think (shoulder season). The sequence start date should be timed to this window, not to your internal calendar.

---

## Phase 6: Outreach Readiness Score — Home Services Edition

When running as a subagent, calculate the score using home services-specific criteria:

| Sub-Dimension | Points | Criteria |
|---|---|---|
| **Google Profile Data Found** (0-25) | 20-25: Rating, review count, competitor data all found. 15-19: Rating and count found, no competitor data. 10-14: Business found but limited profile data. 0-9: No Google profile found. | Quality of Google presence data |
| **Pain Signal Strength** (0-25) | 20-25: Rating under 4.5 AND reviews under 75 AND confirmed Angi spend. 15-19: Two confirmed pain signals. 10-14: One confirmed pain signal. 0-9: No clear pain signal visible. | Specificity and urgency of identified pain |
| **Owner Contact Access** (0-25) | 20-25: Owner name + phone on Google Business Profile or website. 15-19: Owner name found, phone findable. 10-14: Business phone only, owner name findable on Facebook. 0-9: No owner information found. | Direct access to decision maker |
| **Seasonal Timing** (0-25) | 20-25: Currently in shoulder season for their trade. 15-19: Approaching shoulder season (4-6 weeks out). 10-14: Neutral timing. 0-9: Currently in peak season (too busy) or dead slow season (no budget). | Trade-specific seasonal window |

---

## Output Format: OUTREACH-SEQUENCE-HOME-SERVICES.md

Write the full output to `OUTREACH-SEQUENCE-HOME-SERVICES.md` in the current directory:

```markdown
# Cold Outreach Sequence: [Business Name] — Home Services
**Owner:** [Name if found]
**Business:** [Name]
**Trade:** [HVAC / Plumbing / Roofing / etc.]
**Location:** [City, State]
**Date:** [current date]
**Outreach Readiness Score: [X]/100**
**Selected Framework:** [Framework name]

---

## Research Summary

| Field | Value |
|---|---|
| **Google Rating** | [X.X] ★ |
| **Google Reviews** | [X] total |
| **Map Pack Position** | [top 3 / not visible] |
| **Top Competitor** | [name] — [X.X]★ / [X] reviews |
| **Angi/HomeAdvisor** | [active / not found] |
| **Hiring Signal** | [none / type of role] |
| **Estimated Truck Count** | [X] |
| **Best Outreach Timing** | [days/times] |
| **Seasonal Window** | [current status for their trade] |

---

## Pain Signal Analysis

[2-3 sentences summarizing the specific pain points identified.
Include the Google gap, competitor comparison, and any lead gen spend signals.
This is the foundation every email and call is built on.]

---

## Selected Framework: [Framework Name]

**Reasoning:** [1-2 sentences on why this framework was selected based on the research]

---

## Full Sequence

### Call 1 — Day 1 (Primary Touch)
[Full call script personalized to their specific stats]

### Email 1 — Day 1 (Same Day as Call)
**Subject A:** [subject]
**Subject B:** [subject]
[Full email — copy-paste ready, under 70 words]

**A/B Opening Line A:** [primary]
**A/B Opening Line B:** [alternative]

---

### Voicemail — Day 2 (if no call answer)
[Full voicemail script, under 20 seconds]

### Email 2 — Day 4 (Value Add)
**Subject A:** [subject]
**Subject B:** [subject]
[Full email — copy-paste ready]

---

### Facebook / Text — Day 7
**Facebook Messenger:** [full message if Facebook page has Messenger]
**SMS (if cell listed):** [full text, under 160 chars]

---

### Email 3 — Day 10 (Social Proof)
**Subject A:** [subject]
**Subject B:** [subject]
[Full email — copy-paste ready]

---

### Final Call + Email — Day 14 (Close)
**Call Script:** [full final call script]
**Email Subject A:** [subject]
**Email Subject B:** [subject]
[Full breakup email — copy-paste ready, under 50 words]

---

## Channel Summary

| Day | Channel | Action |
|---|---|---|
| 1 | Phone | First call with Google stats opener |
| 1 | Email | Email 1 — The Google Gap |
| 2 | Phone | Voicemail if no answer |
| 4 | Email | Email 2 — Value Add |
| 7 | Facebook/Text | Cross-channel touch |
| 10 | Email | Email 3 — Social Proof |
| 14 | Phone + Email | Final call + Breakup email |

---

## Timing Recommendation

- **Best call times:** [specific days/times based on trade and season]
- **Seasonal context:** [is it peak/shoulder/slow for their trade right now?]
- **Sequence start date recommendation:** [if shoulder season is 6 weeks away, note it]

---

## Top 3 Likely Objections & Quick Responses

| Objection | Response |
|---|---|
| "I don't have time" | [1-sentence response] |
| "We get referrals" | [1-sentence response] |
| "We use Angi already" | [1-sentence response] |

---

*Generated by AI Sales Team — `/sales outreach home-services`*
*Reference: ~/.claude/skills/sales/verticals/home-services.md*
```

---

## Terminal Output

```
=== HOME SERVICES OUTREACH SEQUENCE GENERATED ===

Business: [name]
Trade:    [HVAC/Plumbing/Roofing/etc.]
Owner:    [name if found]
Location: [city, state]

Outreach Readiness Score: [X]/100
  Google Profile Data:  [XX]/25 ████████░░
  Pain Signal Strength: [XX]/25 ██████░░░░
  Owner Contact Access: [XX]/25 ███████░░░
  Seasonal Timing:      [XX]/25 █████░░░░░

Key Stats:
  Their Rating:      [X.X]★ / [X] reviews
  Top Competitor:    [X.X]★ / [X] reviews
  Gap:               [X] stars / [X] reviews

Selected Framework: [name]

Sequence Overview:
  Day 1:  Phone call + Email 1 (The Google Gap)
  Day 2:  Voicemail follow-up
  Day 4:  Email 2 (Value Add — local benchmark)
  Day 7:  Facebook/Text cross-channel
  Day 10: Email 3 (Social Proof — contractor story)
  Day 14: Final call + Email 4 (Breakup)

Best Call Times: [days/times]
Seasonal Window: [status for their trade]

Full sequence saved to: OUTREACH-SEQUENCE-HOME-SERVICES.md
```

---

## Error Handling

- If no Google Business Profile is found, search for their Yelp, Facebook, or BBB profile and use those stats as the pain anchor
- If owner name is not findable, address emails to "[Business Name] team" and open calls with "Hey, is the owner available?"
- If no competitor data is found, use trade-specific city benchmarks ("most top-ranked [trade] companies in [city] have 100+ Google reviews")
- If currently in the wrong seasonal window (peak or dead slow), note this prominently and recommend a specific start date instead
- Always generate a complete sequence regardless of research gaps — note where personalization is weaker

## Cross-Skill Integration

- If `HOME-SERVICES-RESEARCH.md` or `COMPANY-RESEARCH.md` exists, use business data for personalization
- If `LEAD-QUALIFICATION.md` exists, use pain signals and timing scores for framework selection
- Suggest follow-up: `/sales objections home-services` for objection preparation before calls, `/sales prep` for meeting prep after getting a response
