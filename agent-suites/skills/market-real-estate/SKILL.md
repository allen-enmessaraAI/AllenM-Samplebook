# AI Marketing Suite — Real Estate & Brokerage
# Vertical: Residential Real Estate / Agent Teams / Brokerages
# Base skill: market | Patched for: real estate agent teams, independent brokerages, buyer/seller marketing

## Vertical Context

VERTICAL: Real Estate & Brokerage
MARKETING CLIENT TYPES: Solo real estate agent, agent team (2–20 members), independent brokerage, franchise brokerage office
WHAT THIS SKILL DOES: Builds and audits marketing strategies FOR real estate agents and teams — not marketing TO them as sales targets. This is the client-delivery version: when an agent or brokerage hires you to run their marketing, this skill drives the strategy, content calendar, channel mix, and audit framework.
PRIMARY MARKETING GOAL: New buyer and seller lead generation + past client retention + agent/team brand building
COMPLIANCE: NAR Code of Ethics advertising rules, MLS display rules (listed price must be accurate; buyer's agent commission disclosure per NAR settlement), state real estate board advertising requirements (license number required in most states), Fair Housing Act (cannot target or exclude protected classes in ad targeting), CAN-SPAM, TCPA (for SMS marketing)
KEY MARKETING CONCEPT — Agent Brand vs. Brokerage Brand: A KW or RE/MAX agent is building THEIR brand, not the franchise brand. The brokerage logo appears in ads per brand standards requirements, but the agent is the business. All marketing strategy centers on the agent's or team's name, not the brokerage's. Exception: independent brokerages own both.
REVENUE TERMINOLOGY: GCI, transactions, listings, buyer consults, listing appointments, days on market, list-to-sale ratio, average sale price, production, pending pipeline, conversion rate, cost per lead (CPL), cost per closing (CPC)
SEASONAL CALENDAR ANCHOR: Spring (March–June) = highest buyer/seller activity = peak marketing spend. Fall (Sept–Nov) = second wave. Summer (July–Aug) = moderate. Winter (Dec–Feb) = lower volume; use for brand building, market report content, farming campaigns.
MARKETING BUDGET BENCHMARKS: Solo agent: $500–$2,000/month. Small team (2–5 agents): $2,000–$6,000/month. Large team (6–20 agents): $5,000–$15,000/month. Brokerage: $5,000–$25,000+/month. Portal spend (Zillow/Realtor.com) is typically separate from marketing budget and often 2–5× the marketing budget.

---

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/market audit <url>` | Full real estate marketing audit | RE-MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second agent/team snapshot | Terminal output |
| `/market copy <url>` | Generate optimized agent website copy | COPY-SUGGESTIONS.md |
| `/market emails <topic/url>` | Buyer/seller nurture + past client sequences | EMAIL-SEQUENCES.md |
| `/market social <topic/url>` | Real estate social media content calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Google Ads + Meta Ads strategy for leads | AD-CAMPAIGNS.md |
| `/market funnel <url>` | Buyer/seller lead funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Local competitor agent/team analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | Home valuation or buyer consult landing page CRO | LANDING-CRO.md |
| `/market launch <service>` | Launch playbook for new market or team expansion | LAUNCH-PLAYBOOK.md |
| `/market proposal <agent/team>` | Generate client marketing proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Full real estate marketing report | RE-MARKETING-REPORT.md |
| `/market seo <url>` | Local/hyperlocal SEO audit for agent/team | SEO-AUDIT.md |
| `/market brand <url>` | Agent/team brand voice and positioning | BRAND-VOICE.md |

---

## Routing Logic

When invoked, route to the appropriate analysis framework below. Sub-skill commands use the real estate vertical context to override base skill generic B2B logic.

### Full Real Estate Marketing Audit (`/market audit <url>`)

Launch **5 parallel subagents** with real estate-specific mandates:

1. **market-content** (RE lens) → Website copy for buyer/seller conversion; IDX home search integration; property listing presentation quality; neighborhood page depth; agent bio trust signals; testimonial/sold listings showcase
2. **market-conversion** (RE lens) → Home valuation widget friction; buyer consult CTA clarity; lead capture form quality; IDX registration gate; mobile experience for on-the-go buyers; chat/text response options
3. **market-competitive** (RE lens) → Local agent/team competitor comparison; Zillow rating/review comparison; portal presence (ZPA vs. non-ZPA); market share in farm area; Google Maps ranking; content differentiation
4. **market-technical** (RE lens) → Local SEO for "homes for sale [city]" and "[agent name] [city]"; IDX indexation; Google Business Profile completeness; NAP consistency; page speed (IDX widgets are notorious speed killers); schema markup for real estate
5. **market-strategy** (RE lens) → Channel mix and budget allocation; portal dependency assessment; database marketing strategy; listing marketing system; farm area strategy; referral/sphere marketing; video/YouTube strategy

---

## Real Estate Marketing Score — Weighted Categories

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Lead Generation & Conversion | 30% | IDX performance, home valuation widget, buyer/seller CTAs, landing pages, paid ad presence |
| Local SEO & Online Visibility | 25% | Google Business Profile, neighborhood/city page SEO, agent name ranking, portal profiles |
| Content Quality & Brand | 20% | Listing content quality, market reports, video presence, agent bio and credibility signals, testimonials |
| Reputation & Social Proof | 15% | Google/Zillow reviews, sold listings showcase, list-to-sale ratio display, client testimonials |
| Database & Retention Marketing | 10% | Past client email marketing, sphere outreach cadence, newsletter, "just sold" follow-up system |

**Composite Real Estate Marketing Score** = Weighted average of all 5 categories

> Critical difference from base skill: Lead Generation carries 30% weight (highest category) because real estate is a pure lead-to-close business model. Brand and content matter, but everything ultimately drives toward a buyer consult or listing appointment. IDX website performance is the #1 lead gen lever most agents underinvest in.

---

## Phase 1: Real Estate Marketing Discovery

### 1.1 Agent/Team Classification

| Type | Signals | Marketing Priority |
|------|---------|-------------------|
| **Solo agent** | Single name, solo brand, 1 headshot | Personal brand building + Google + sphere email |
| **Buyer-specialist team** | Buyer agents listed, "buyer's agent" language, IDX-heavy website | IDX/search lead gen + Facebook buyer ads + nurture |
| **Listing-specialist team** | Listing presentation emphasis, seller landing pages, "sold" showcase dominant | Seller lead gen + home valuation + just listed/sold campaign |
| **Geographic farm specialist** | One or two neighborhoods featured heavily, newsletter, market stats | Hyperlocal SEO + direct mail + neighborhood content |
| **Luxury specialist** | $1M+ price range, professional photography, Matterport 3D, lifestyle branding | Instagram/YouTube visual + listing portal premium placement |
| **Independent brokerage** | Recruits agents, franchise-free branding, owns the brand | Dual marketing: consumer lead gen + agent recruiting |

### 1.2 Key Pages to Analyze

- Homepage (agent/team first impression; buyer vs. seller bifurcation; IDX search widget)
- Buyer landing page (buyer consult offer; what buyers get; pre-approval path)
- Seller landing page (home valuation widget; listing presentation offer; "what's my home worth")
- Listings page (current active listings; quality of listing presentations; photo/video)
- Sold/Results page (sold listings showcase; days on market; list-to-sale ratio; testimonials)
- About/Team page (agent bio; credentials; years in market; local expertise signals)
- Blog/Market Reports (content depth; local market data; publishing frequency)
- Neighborhood pages (hyperlocal content; homes for sale in [neighborhood]; local guides)
- Contact/Home Valuation page (lead capture form; friction assessment; CTA clarity)

### 1.3 Real Estate Technology Detection

| Technology | Detection Method | Marketing Implication |
|-----------|-----------------|----------------------|
| **IDX provider** | Copyright footer (iHomeFinder, IDX Broker, Showcase IDX, Wovax) | Home search quality; lead capture integration; SEO value |
| **Website platform** | Source code or footer (Real Geeks, Placester, Luxury Presence, Agent Image, kvCORE) | Platform capability; SEO potential; built-in CRM |
| **Home valuation widget** | "What's my home worth?" page (HouseValues, HomeBot, Cloud CMA) | Seller lead capture mechanism |
| **CRM** | Job postings or kvCORE/BoomTown branding on emails | Lead nurture capability |
| **Video** | YouTube channel link; embedded video tours | Content marketing sophistication |
| **Chat widget** | Homepage live chat (Drift, Intercom, or RE-specific) | Response speed and lead conversion |
| **Matterport / 3D tour** | Listing links to Matterport | Listing quality investment |
| **Meta Pixel** | Source code | Facebook/Instagram retargeting active |
| **Google Analytics / Tag Manager** | Source code | Data-driven marketing approach |

---

## Phase 2: Real Estate Channel Strategy

### 2.1 Channel Priority Matrix

| Channel | Role | Priority | Investment Range |
|---------|------|----------|-----------------|
| **IDX Website + Local SEO** | Long-term organic buyer/seller lead gen; "homes for sale [city]" → #1 most valuable owned asset | Critical | SEO: $500–$2,000/month; website: $100–$500/month |
| **Google Business Profile** | "[Agent name] [city]," "real estate agent near me" searches; review showcase | Critical | Free (management time) |
| **Google Search Ads** | High-intent capture: "homes for sale [city]," "sell my house [city]," "realtor near me" | High | $1,000–$5,000/month |
| **Facebook/Instagram Ads** | Buyer audience (home search interests, life event targeting); seller retargeting | High | $500–$3,000/month |
| **Zillow Premier Agent** | Portal lead capture; supplement organic — NOT replace | Medium-High | $500–$5,000+/month (varies by market) |
| **Email — Database Marketing** | Past client retention; sphere nurture; highest ROI channel for repeat/referral | Critical | Low cost (MailChimp, kvCORE) |
| **Direct Mail** | Geographic farm; just listed/just sold; new mover targeting; counterintuitively high ROI in RE | High | $500–$2,500/month for consistent farm |
| **Instagram** | Listing content; market updates; agent personal brand; younger buyer audience | High | Content creation: $300–$1,000/month |
| **YouTube** | Neighborhood guides; home tours; market updates; highest-trust content format | High | Low cost if team does own video |
| **Nextdoor** | Hyperlocal neighborhood community; "just listed" posts reach immediate farm area | Medium | Free (organic) |
| **LinkedIn** | Brokerage recruiting; commercial real estate; referral network (out-of-market agents) | Low-Medium | Organic only for most agents |

### 2.2 The Portal Dependency Problem

Zillow Premier Agent (ZPA) is the single most common marketing over-investment in real estate:

**The math that matters:**
- Average ZPA CPL in competitive markets: $100–$400/lead
- Industry average ZPA close rate: 2–5%
- Cost per closing via Zillow: $5,000–$20,000+ in competitive markets
- Industry average organic website close rate: 10–18% (warm leads who found you specifically)
- Cost per closing via owned digital marketing (SEO + Google Ads + email): $500–$3,000

**Marketing position:**
Don't recommend eliminating portals — they provide immediate volume. Recommend reducing portal dependency from primary to supplement, and rebuilding owned channels (SEO, Google Ads, database email) to generate 50%+ of leads without portal fees within 12–18 months.

---

## Phase 3: Real Estate Content Strategy

### 3.1 Content Pillars for Real Estate

| Pillar | Theme | Content Types | Ratio |
|--------|-------|---------------|-------|
| **Local Market Data** | Monthly/quarterly market reports; median price; DOM; inventory; buyer/seller market status | Blog, email, Instagram carousel, YouTube, Facebook | 30% |
| **Listing Content** | Active listings, just listed/sold announcements, home tours, property highlight videos | Instagram, Facebook, YouTube, Google Posts, direct mail | 25% |
| **Educational Content** | Buying process guide, selling timeline, mortgage explainer, closing cost breakdown, market cycle education | Blog, YouTube, Instagram carousels, email | 20% |
| **Social Proof & Results** | Client testimonials, sold stats (avg days on market, list-to-sale ratio), before/after staging | Instagram, Facebook, website, Google Posts | 15% |
| **Community & Local Lifestyle** | Neighborhood spotlights, local events, restaurant/business features, area guides | YouTube, Instagram, Facebook, blog | 10% |

### 3.2 Platform-Specific Real Estate Content

**Google Business Profile (post 2–3x/week):**
- Just listed: "[Property address] — [bedrooms/baths], [price], available now"
- Just sold: "Sold in [X] days at [X]% of list price — congratulations to our clients!"
- Market update: "March [market] update: [X] homes sold, median price [X], avg [X] days on market"
- Team announcement: "Welcome [new agent] to our team — now serving [area]"
- Seasonal: "[Neighborhood] spring market is heating up — here's what sellers need to know"

**Instagram (5–7x/week):**

*Feed posts (3–4x/week):*
- Listing announcement (high-quality photo or Reel): "Just listed: [address] → [brief highlights]"
- Market update carousel: "This month in [city]: 5 things every buyer/seller needs to know"
- Client success story: "[Client first name] sold in 8 days over ask — here's what we did"
- Neighborhood spotlight: "[Neighborhood name]: Why families are moving here in 2025"

*Reels (2–3x/week):*
- Home tour walkthroughs (60–90 seconds): "Full tour of this [X-bed] in [neighborhood]"
- "Why I'd never buy a home without doing THIS first" — educational format, high saves
- Before/after staging Reel: transformation video of a listing prep
- Market update quick take: "30-second [city] market report — [month]"
- Local neighborhood feature: "5 things I love about [neighborhood]" — personal and local

*Stories (daily):*
- Showing day updates ("Showing [X] homes today — buyers are out in force")
- Open house promotion (Saturday morning countdown)
- Poll: "Rate your neighborhood: A B C D" — engagement driver
- Behind the scenes: staging, signing, key handover

**YouTube (1–2x/week — highest-trust content format in real estate):**
- Neighborhood tour guides: "[Neighborhood name]: Full neighborhood guide 2025" (10–15 min)
- Home buyer process series: "How to buy a home in [city] in 2025 — step by step" 
- Monthly market report video: "[Market] real estate market — what happened in [month]"
- Specific home tours: "Full walkthrough — [address] — [price]"
- Q&A: "You asked, I answered: [common buyer/seller questions]"
- "Why people are moving to [city]" — attracts relocation buyers

**Facebook (3–4x/week):**
- Listing shares (cross-post from Instagram)
- Local community news and events
- Market stats with longer-form explanation for older demographic
- Just sold posts with client story
- "Before and after" listing preparation stories

**Email (database — 2x/month minimum):**
- Monthly market report: "Here's what happened in [city] real estate in [month]"
- Just listed/just sold announcements to sphere: "Thought of you — we just listed in your neighborhood"
- Seasonal reminders: "Spring market is here — thinking of selling? Here's what your home might be worth"
- Personal touch: quarterly personal email from agent to top 50 sphere contacts
- Anniversary email: "One year ago, you got the keys to [address]! How's life treating you?"

**Direct Mail (farm area — monthly):**
- Just listed card: Professional design, property photo, agent branding
- Just sold card: "Sold in [X] days — your neighbors trusted us. You can too."
- Market report mailer: "[Neighborhood] market update — [quarter]"
- New mover welcome package: Letter + refrigerator magnet + local guide
- Seasonal touchpoint: Holiday cards, summer market tip sheet

### 3.3 Real Estate Content Calendar — Seasonal Framework

| Month | Theme | Priority Content Play |
|-------|-------|----------------------|
| January | New Year homebuyer/seller education | "Is now a good time to buy/sell?" market content; pre-spring lead nurture email; Google Ads ramp |
| February | Pre-spring warm-up | "Spring listing prep checklist"; buyer pre-approval push; Valentine's home feature content |
| March | Spring market launch | Peak ad spend; all channels active; open house promotion push; seller lead gen ramp |
| April | Peak spring | Max listing content; "move before school's out" buyer messaging; market update content |
| May | Move-up season | Repeat buyer content ("your current home can fund your next one"); school district content |
| June | School-year end | Family relocation content; summer move timeline; graduation → first-time buyer |
| July | Summer pace | Maintain listings; lighter content; vacation home or investment property angle |
| August | Back-to-school buyers | "Buy now, move before school starts" last call; neighborhood school feature content |
| September | Fall market | Second seasonal push; "sell before year end" messaging; home prep content |
| October | Year-end urgency | "List now, close before the holidays" seller campaign; buyer rate opportunity content |
| November | Database / sphere | Past client outreach; Thanksgiving personal touch emails; referral ask campaign |
| December | Year-end wrap | Annual market report; holiday card mail; preview spring 2026 market content |

---

## Phase 4: Real Estate SEO Framework

### 4.1 The Two-Layer SEO Model for Real Estate

Real estate requires two distinct SEO strategies that most agents conflate:

**Layer 1: Agent/Brand SEO**
Goal: Rank for "[agent name] [city]" and "[team name] [city]"
- Highest-intent search — people looking specifically for you
- Easiest to rank; managed via Google Business Profile + website

**Layer 2: Hyperlocal/Transactional SEO**
Goal: Rank for "homes for sale [neighborhood]," "real estate agent [city]," "[city] housing market"
- Highest lead volume; hardest to rank; requires dedicated neighborhood/city pages
- IDX integration is essential — active listings create crawlable content

### 4.2 IDX SEO Optimization

IDX (Internet Data Exchange) is the MLS feed embedded on real estate websites. When configured correctly, it is the most powerful SEO asset a real estate agent can own.

**IDX SEO rules:**
- Each neighborhood/zip code should have a dedicated IDX landing page with custom written content (minimum 300 words) ABOVE the listing results
- Page title format: "Homes for Sale in [Neighborhood] | [Agent/Team Name] | [City]"
- URL structure: /[city]-homes-for-sale, /[neighborhood]-real-estate
- Schema markup: RealEstateListing schema on each property page
- Mobile-first: 65%+ of home searches happen on mobile; IDX must be fully responsive

**High-value IDX page targets:**
| Page | URL Pattern | Target Keyword |
|------|------------|----------------|
| City main | /[city]-homes | "homes for sale [city]" |
| Neighborhood | /[neighborhood]-homes | "homes for sale [neighborhood]" |
| Price range | /homes-under-[X] | "homes under $[X] [city]" |
| Property type | /[city]-condos | "condos for sale [city]" |
| School district | /[district]-homes | "homes for sale [school district]" |
| New construction | /new-homes-[city] | "new construction [city]" |

### 4.3 Google Business Profile for Real Estate

**Unique to real estate:**
- Category: "Real Estate Agent" (primary) + "Real Estate Agency" if applicable
- Service area: add all zip codes served (up to 20)
- Products: add service categories (Buyer Representation, Seller Representation, Relocation Services)
- Posts: weekly market update + every just listed/just sold
- Q&A: populate with "Do you work with first-time buyers?", "What areas do you serve?", "Do you charge buyer's agents fees?"
- Photos: 40+ including agent headshots, sold properties (with permission), office, community events

**Review generation (critical for Google Maps ranking):**
- At closing (highest satisfaction moment): "If you're happy with how things went, we'd love a Google review. A lot of buyers and sellers find us through Google."
- Post-close text: "Congratulations on your new home! If you have a moment: [Google review link]. It means a lot to us."
- Target: 2+ new Google reviews/month

### 4.4 Key Real Estate SEO Keywords

| Keyword Type | Examples | Notes |
|-------------|---------|-------|
| Primary location | "real estate agent [city]," "realtor [city]," "homes for sale [city]" | Highest volume; hardest to rank |
| Neighborhood | "homes for sale [neighborhood]," "[neighborhood] real estate" | Medium volume; high conversion intent |
| Transactional seller | "sell my house [city]," "what's my home worth [city]," "listing agent [city]" | Lower volume; very high intent |
| Transactional buyer | "buy a home [city]," "first time home buyer [city]," "relocation realtor [city]" | Medium; good conversion |
| Long-tail | "3 bedroom homes for sale in [neighborhood]," "homes with pool [city]" | Low volume; very high intent |
| Agent-specific | "[agent name] realtor," "[team name] real estate" | Brand searches; should rank #1 easily |

---

## Phase 5: Paid Advertising for Real Estate

### 5.1 Google Search Ads

**Campaign 1: Seller Lead Gen**
- Keywords: "sell my house [city]," "what's my home worth," "listing agent [city]," "how much is my home worth"
- Landing page: Home valuation page with instant estimate widget + agent contact
- CTA: "Get Your Free Home Valuation"
- Budget: $500–$2,000/month
- Expected CPL: $15–$50

**Campaign 2: Buyer Lead Gen**
- Keywords: "homes for sale [city]," "houses for sale [city]," "real estate [city]," "buy a home [city]"
- Landing page: IDX home search page or buyer guide with email capture
- CTA: "Search [City] Homes"
- Budget: $500–$3,000/month
- Expected CPL: $10–$40

**Campaign 3: Agent Brand**
- Keywords: "[agent name]," "[team name]," "[brokerage name] [city]"
- Low budget, high ROI: prevents competitors from stealing branded searches
- Budget: $100–$300/month

**Negative keywords for real estate:**
- rental, rent, apartment, lease (unless agent does rentals)
- for sale by owner, FSBO, sell without agent
- jobs, career, become a realtor
- commercial (unless commercial agent)
- foreclosure (unless specialty)

### 5.2 Facebook/Instagram Ads for Real Estate

**IMPORTANT — Fair Housing Compliance:**
Facebook's Special Ad Category rules restrict real estate ad targeting. Cannot target or exclude by:
- Race, color, national origin, religion, sex, familial status, or disability
- ZIP code as a proxy for demographics
- Cannot use "Multicultural Affinity" interest targeting
Must use Special Ad Category: "Housing" which restricts some targeting options but is legally required.

**Campaign 1: Seller Lead Gen (Home Valuation)**
- Audience: Homeowners in service area (use radius + "likely to move" behavior where available under Special Ad rules)
- Creative: "What's your home worth in today's market?" + recent sold properties in their area
- Landing page: Home valuation widget
- CTA: "Get My Home's Value"
- Budget: $500–$2,000/month
- Expected CPL: $10–$40

**Campaign 2: Buyer Lead Gen**
- Audience: Service area radius, 25–55 age (permitted), renter interest signals
- Creative: Lifestyle image of neighborhood or specific property; "Search all [city] homes"
- Landing page: IDX home search page with email gate
- CTA: "Browse [City] Homes"
- Budget: $300–$1,500/month
- Expected CPL: $5–$25

**Campaign 3: Retargeting (website visitors)**
- Audience: Custom audience — visited website in last 30 days
- Creative: Specific listings they may have viewed; or "Still looking? Let's talk."
- Budget: $200–$500/month
- Expected CPL: $3–$15

**Campaign 4: Just Listed Boost**
- Objective: Reach (not lead gen) — maximize listing exposure in geographic area
- Creative: Professional listing photos + property details
- Audience: 5-mile radius of listing address
- Budget: $5–$15/day per listing for 7–14 days
- Goal: Maximize impressions of listing to local buyers and their networks

### 5.3 Direct Mail Strategy

Real estate direct mail has a counterintuitively high ROI when executed as a consistent geographic farm program — not one-off drops.

**Farm area math:**
- Ideal farm size: 300–500 homes for a solo agent; 500–2,000 for a team
- Required touch frequency: 12x/year (monthly) to establish top-of-mind awareness
- Time to dominance: 18–24 months of consistent farming
- When to claim dominance: 10%+ market share in the farm area

**Mail pieces that convert:**
| Piece | When to Send | Purpose |
|-------|-------------|---------|
| Just Listed postcard | Day of listing | Immediate neighborhood exposure |
| Just Sold postcard | Day of closing | Proof of production; "your neighbor trusted us" |
| Monthly market report | 1st week of each month | Authority positioning; value-add touch |
| New mover welcome | When new resident data available | Long-term relationship start |
| Seasonal postcard | Holiday, spring, etc. | Brand touchpoint with no selling pressure |
| "We have buyers looking in [neighborhood]" | Market-driven | Creates urgency for sellers thinking about timing |

---

## Phase 6: Database & Past Client Marketing

### 6.1 The Most Valuable Asset in Real Estate

The past client database is the highest-ROI marketing asset most agents underutilize. Industry data:
- 77% of buyers and sellers say they would use their agent again — but only 12% actually do, because agents stop marketing to them
- The average homeowner moves every 7–10 years — your past clients are your future pipeline
- Referrals from past clients close at 4–6× the rate of internet leads
- Annual past client marketing spend: $300–$500/client/year = consistently highest ROI channel

### 6.2 Database Segmentation for Real Estate

| Segment | Description | Marketing Approach |
|---------|-------------|-------------------|
| **A — Top 20 Sphere** | Best referral sources; know the agent personally | Monthly personal email + quarterly personal call/text + gifts |
| **B — Past Clients (< 3 years)** | Recent clients with fresh experience | Monthly newsletter + just sold alerts + check-in email/text |
| **C — Past Clients (3–7 years)** | Older clients who may be approaching next move | Quarterly market update + annual value conversation |
| **D — Cold Database** | Leads who never converted; old contacts | Monthly newsletter + occasional event invite |
| **E — Sphere (never done business)** | Personal network who know the agent | Monthly newsletter + annual personal outreach |

### 6.3 Past Client Email Sequences

**Monthly Newsletter (all segments):**
- [City] market update: what happened last month (prices, inventory, DOM, sold count)
- One local spotlight (restaurant, business, event, neighborhood feature)
- Real estate tip of the month (relevant to homeowners, not just buyers/sellers)
- Agent update (milestone, new team member, personal news)
- Soft CTA: "Know anyone thinking of buying or selling? I'd love the referral."

**Home Anniversary Email (automated, on closing anniversary):**
```
Subject: One year in your new home

[Name] — one year ago today, you got the keys to [address].

I hope the house has become a home in every way.

Just a reminder that I'm always here if you have questions about your home's
value, local market, or if anyone you know needs a great [city] agent.

Here's to many more great years on [street name].

[Agent name]
P.S. Your home's estimated value today: ~$[Zestimate or AVM estimate] 
```

**Market Update to Past Seller (when listing their old neighborhood):**
```
Subject: Your old neighborhood is moving

[Name] — thought of you: we just listed [nearby address], a [X-bed] similar to
your old home, at $[price]. 

The [neighborhood] market has moved significantly since you sold.
If you ever want to know what your current home is worth, I'm a text away.

[Agent name]
```

---

## Phase 7: Listing Marketing System

### 7.1 Every Listing is a Marketing Campaign

Each property listing should be treated as a standalone marketing campaign with its own budget and distribution plan:

**Listing launch sequence (first 7 days):**
- Day 0 (Coming Soon): Instagram Story + Zillow Coming Soon post + email to buyer pipeline
- Day 1 (Active): Professional photos live, 3D tour if applicable, all portal syndication confirmed
- Day 1: Instagram Reel (home tour walkthrough) + Facebook Reel share
- Day 1: Email blast to database: "Just listed — [address]"
- Day 1: Nextdoor post in listing's neighborhood
- Day 1: Just Listed postcard ordered (arrive Day 5–7)
- Day 2: Google Business Profile post: "New listing: [address]"
- Day 3: Facebook/Instagram paid boost of listing content ($5–$15/day, 5-mile radius)
- Day 7 (if not under contract): Instagram Story with "Still available — open house this weekend"

**Open house marketing (minimum 48-hour lead time):**
- Instagram + Facebook organic post (with address, time, photos)
- Nextdoor post (day before and day-of)
- Facebook/Instagram boosted post ($10–$20 for 48 hours, 3-mile radius)
- Zillow and Realtor.com open house listing added
- Google Business Profile event post
- Email to local buyer pipeline: "Open house alert — [address], [date/time]"

**Sold listing marketing (within 24 hours of close):**
- Instagram: Just Sold post with closing story + stats (DOM, list-to-sale %)
- Facebook: Just Sold post with longer client story caption
- Google Business Profile: "Just sold in [neighborhood]"
- Just Sold postcard: mail to 300-home farm around listing address
- Email to sphere: "We just sold [address] in [X] days — great opportunity for sellers in [neighborhood]"

### 7.2 Listing Presentation Content Assets

Quality listing marketing starts before the property goes live:

**Photography:** Professional photography is non-negotiable — listings with professional photos sell 32% faster and for $3K–$11K more (REBC data). Suggest minimum: 25 professional photos + twilight exterior shot.

**Video:** Listing video Reel (60–90 second walkthrough) adds measurable digital reach vs. photos alone.

**3D Tour (Matterport):** Recommended for homes over $500K. Increases listing page time by 3× and reduces wasted showings.

**Floor plan:** Digital floor plan attached to all portal listings — increases listing page engagement by 52%.

**Copywriting:** MLS remarks should be 200+ words, feature the lifestyle (not just the specs), and include the top 3 keywords buyers search for in that price range and area.

---

## Phase 8: Real Estate Marketing Audit Output

### Scoring Rubric

**Lead Generation & Conversion (30 points)**
- 25-30: IDX website generating leads, home valuation widget active, Google Ads running, Facebook ads running, multiple lead capture CTAs, proven conversion tracking
- 18-24: IDX active, one paid channel, basic CTAs
- 10-17: IDX active but no paid ads, weak CTAs
- 0-9: No IDX, no paid ads, contact form only

**Local SEO & Online Visibility (25 points)**
- 21-25: Page 1 for "[agent name] [city]," GBP fully optimized, neighborhood pages present, IDX properly indexed, Zillow/Realtor.com profiles complete
- 15-20: Good brand SEO, partial neighborhood pages, GBP mostly complete
- 8-14: Brand SEO only, no neighborhood pages, thin GBP
- 0-7: Poor or no local SEO presence

**Content Quality & Brand (20 points)**
- 17-20: Professional photography + video, active YouTube, consistent social posting (5x/week+), market reports published monthly, strong agent bio
- 12-16: Professional photography, some video, 3x/week social, occasional market reports
- 6-11: Mixed photography quality, irregular posting, no market reports
- 0-5: Stock photos, no video, no consistent social presence

**Reputation & Social Proof (15 points)**
- 13-15: 4.5+ Google + 4.8+ Zillow, 30+ total reviews, 2+/month velocity, sold stats visible on website, video testimonials
- 9-12: Good ratings on both platforms, adequate review count
- 5-8: Low review count or mixed ratings
- 0-4: Under 10 reviews or under 4.0 rating on Google or Zillow

**Database & Retention Marketing (10 points)**
- 9-10: Monthly newsletter active, automated home anniversary emails, past client text cadence, referral ask campaign
- 6-8: Irregular newsletter, some past client outreach
- 3-5: Annual check-in only
- 0-2: No past client marketing

---

## Output Format: RE-MARKETING-AUDIT.md

```markdown
# Real Estate Marketing Audit: [Agent / Team Name]
**Website:** [url]
**Zillow Profile:** [url]
**Date:** [current date]
**Agent Type:** [Solo / Small Team / Large Team / Brokerage]
**Market:** [city/metro area]
**Estimated Annual Transactions:** [X] (from Zillow sold data)
**Overall Marketing Score: [X]/100 (Grade: [letter])**

---

## Executive Summary

[3-5 paragraphs. Lead with the score and what it means for new lead flow.
Flag portal dependency if present: "Based on the marketing profile, [X]% of lead gen appears to be
portal-dependent (Zillow/Realtor.com). This creates CPL exposure as portal costs rise 15-20%/year.
The #1 opportunity is [top recommendation] — at [agent]'s current transaction volume of ~[X]/year,
closing 3 additional transactions from an improved [channel] would represent ~$[GCI estimate] in
additional annual GCI at essentially zero incremental cost."]

---

## Score Breakdown

| Category | Score | Weight | Weighted Score | Key Finding |
|----------|-------|--------|---------------|-------------|
| Lead Gen & Conversion | X/100 | 30% | X | [one-line finding] |
| Local SEO & Visibility | X/100 | 25% | X | [one-line finding] |
| Content Quality & Brand | X/100 | 20% | X | [one-line finding] |
| Reputation & Social Proof | X/100 | 15% | X | [one-line finding] |
| Database & Retention | X/100 | 10% | X | [one-line finding] |
| **TOTAL** | | **100%** | **X/100** | |

---

## Portal Dependency Assessment

| Channel | Est. % of Leads | CPL Range | Annual Cost Est. |
|---------|----------------|-----------|-----------------|
| Zillow Premier Agent | [X]% | $[X]–$[X] | $[X]/year |
| Realtor.com | [X]% | $[X]–$[X] | $[X]/year |
| Organic/SEO | [X]% | Near zero | Time investment |
| Google Ads | [X]% | $[X]–$[X] | $[X]/year |
| Facebook/Instagram | [X]% | $[X]–$[X] | $[X]/year |
| Database/Referral | [X]% | Near zero | $500–$2K/year |

**Assessment:** [Portal-heavy / Diversified / Organic-dominant] — [1-2 sentence implication]

---

## Quick Wins (This Week — No Budget Required)

[GBP optimization gaps, Zillow profile completions, review request script, social bio updates,
IDX page titles, sold stats page addition, neighborhood page fixes]

## Strategic Recommendations (This Month)

[Home valuation campaign, Google Ads launch, database email cadence, YouTube channel start,
direct mail farm setup, listing marketing playbook]

## Long-Term Initiatives (This Quarter)

[Full neighborhood SEO program, past client referral system, YouTube channel growth,
portal dependency reduction plan with owned channel replacement, recruiting if brokerage]

---

## Channel-by-Channel Analysis

### IDX Website & Lead Conversion
[Home search experience, lead capture friction, page speed, mobile assessment, home valuation widget]

### Google Business Profile & Local SEO
[GBP completion score, ranking assessment, review profile, neighborhood page inventory]

### Paid Advertising
[Active campaigns detected, budget signals, landing page quality, ad creative assessment]

### Social Media (Instagram / Facebook / YouTube)
[Platform-by-platform audit — follower count, post frequency, content type, engagement]

### Listing Marketing
[Photography quality, video presence, 3D tour, MLS remarks quality, listing syndication coverage]

### Database & Email Marketing
[Newsletter status, automation detected, sphere outreach cadence, past client marketing]

### Reputation & Reviews
[Google, Zillow, Realtor.com, Facebook ratings and review velocity]

---

## Competitor Comparison

| Factor | [Agent/Team] | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-------------|-------------|-------------|-------------|
| Google Rating (reviews) | | | | |
| Zillow Rating (reviews) | | | | |
| Est. Annual Transactions | | | | |
| Active on YouTube | | | | |
| Posting Frequency (IG) | | | | |
| Active Paid Ads | | | | |
| Neighborhood Pages | | | | |

---

## GCI Revenue Impact Model

| Improvement | Est. Additional Closings/Year | At $12,000 Avg GCI/Side | Annual GCI Impact |
|------------|------------------------------|------------------------|-------------------|
| Database email (10% conversion improvement) | +3–6 | $12,000 | $36K–$72K |
| Google Ads (new channel) | +5–12 | $12,000 | $60K–$144K |
| IDX SEO (6-month ramp) | +4–10 | $12,000 | $48K–$120K |
| Listing marketing system | +2–5 (referral lift) | $12,000 | $24K–$60K |
| Review velocity (2+/month) | +2–4 | $12,000 | $24K–$48K |
| **Total Potential** | **+16–37 closings** | | **$192K–$444K/year** |

*GCI per side estimated at $12,000 (adjust for local average sale price and commission rate)*

*Generated by AI Marketing Suite — Real Estate Vertical | `/market audit <url>`*
```

---

## NAR Settlement Compliance Note (2024+)

The August 2024 NAR settlement significantly changed buyer agent commission practices. All real estate marketing must reflect current requirements:

1. **Buyer representation agreements**: Must be signed before showing homes. Marketing that implies "free buyer's agent services" is no longer accurate and should be updated.

2. **Commission disclosure**: Offers of buyer agent compensation can no longer be listed on MLS. Any marketing language referencing "seller pays commission" or "no cost to buyers" must be reviewed against current state-specific rules.

3. **Website copy audit flag**: Review all website pages for outdated commission language. Common violations include: "we never charge buyers," "seller pays all fees," "free buyer representation." These claims are no longer uniformly accurate post-settlement.

4. **Facebook ad targeting**: Real estate ads must use the Special Ad Category "Housing" which restricts demographic targeting. Non-compliance risks Facebook account suspension and Fair Housing Act violations.

---

*Generated by AI Sales Team — Real Estate Vertical | `/market <command> <agent-website-url>`*
