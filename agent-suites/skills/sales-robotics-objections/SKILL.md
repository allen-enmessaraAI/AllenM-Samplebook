# Objection Handling Playbook — Warehouse Automation & Robotics
# Vertical: Warehouse Automation / Industrial Robotics
# Base skill: sales-objections | Patched for: food & beverage, 3PL, building materials, big box retail

## Vertical Context

VERTICAL: Warehouse Automation & Robotics
BUYER TITLES: VP Supply Chain / VP Operations (economic buyer), Director of Engineering / Automation Manager (technical champion), CFO (financial gatekeeper), DC General Manager (ground champion)
TERMINOLOGY TO USE: throughput, pick rate, order accuracy, SKU velocity, FEFO, lot tracking, WMS integration, TCO, payback period, CapEx, labor cost per pick, store replenishment, e-commerce fulfillment, greenfield, brownfield, AMR, ASRS, GTP, pallet in/pallet out, RaaS — never use "optimize," "leverage," "synergy," "innovative," "cutting-edge," "seamlessly," or "industry-leading"
PROOF POINT FORMAT: Always express ROI in labor cost reduction ($/year), payback period (years), pick rate improvement (units/hr), or order accuracy gain (%). VP Supply Chain thinks in P&L impact; Director of Engineering thinks in operational metrics. Tailor the frame to who's in the room.
TRUST SIGNALS: Peer reference from same sub-vertical and similar facility size is #1. Published case study with named customer and specific metrics > general claims. WMS-specific integration proof is a hard trust filter — "we integrate with Manhattan WMS" lands very differently than "we integrate with most WMS platforms."
SALES CYCLE CONTEXT: This is a complex, committee-driven CapEx sale. The objection handling process is slower and more deliberate than transactional sales. Never push for a close prematurely — the goal of most objection conversations is to advance to the next step (discovery call, site visit, pilot proposal), not to close the deal.
BUYING COMMITTEE REALITY: VP Supply Chain may not be the only blocker. Director of Engineering can kill a deal with technical concerns. CFO can kill it with CapEx timing. Know who raised the objection and tailor accordingly.

---

## Purpose

Generate complete, word-for-word objection handling scripts for selling warehouse automation systems into distribution centers and warehouse operations. Every script must use supply chain terminology, reference specific ROI metrics, and feel like it came from someone who has walked the floor of a distribution center — not a technology sales rep reading from a script.

Follow all base objection handling frameworks (FFR and ABC) and produce all 15 universal objections plus 8 warehouse-automation-specific industry objections below.

---

## Warehouse Automation-Specific Industry Objections (16–23)

---

### Objection 16: "Our WMS isn't ready for automation / We need to modernize our WMS first"

**What it really means:** The VP of Supply Chain or Director of Engineering is worried that their Warehouse Management System isn't sophisticated enough to integrate with automation. This may be legitimate (they're running a legacy WMS or custom ERP warehouse module) or it may be a stall tactic rooted in change-management fear. Either way, it must be taken seriously — a bad WMS is a real integration risk.

**Who raises this:** Director of Engineering / IT Director (technical blocker) or VP Supply Chain (conservative framing)

**FFR Response:**
"That concern is worth taking seriously — and I appreciate you raising it upfront. [Distribution company] in [sub-vertical] had the same situation — they were running SAP WM, not SAP EWM, which is our preferred integration target. What they found was that we had two paths: we could add a middleware layer that sits between their WM system and our AMRs, or they could use our WCS as the orchestration layer while they planned the WMS migration. They chose the middleware path, went live in 90 days, and have run clean for 18 months. The WMS migration happened in parallel — 12 months later — without touching the automation. Is your concern specifically about integration risk, or are there deeper WMS modernization plans already in motion?"

**ABC Response:**
"WMS readiness is the right thing to evaluate before any automation commitment — I'm glad you raised it. (Acknowledge) Here's our honest read: if you're on Manhattan Active WMS, Blue Yonder, or SAP EWM, we have certified connectors and go-live in 60–90 days. If you're on a legacy platform or custom ERP module, we need to scope an integration carefully — and sometimes that means a phased approach where automation doesn't wait for the full WMS migration. (Bridge) Can you tell me specifically which WMS you're running and whether there's a modernization project on the roadmap? Once I know that, I can give you a completely straight answer on what integration looks like and what it would cost. (Close)"

**Follow-up question:** "Which WMS are you on right now, and has your team done any formal evaluation of the integration requirements for automation? I want to give you a realistic picture of the path, not a sales answer."

**Proof point:** Have a reference customer with a similar WMS version on the same sub-vertical. Best form: "We've integrated with [their specific WMS platform] at [number] facilities. I can put you on a call with their IT Director."

**When to walk away:** If they are running a custom-built ERP warehouse module with no WMS layer and no plans to modernize — the integration cost and complexity may exceed the automation ROI. Be honest: "At your WMS complexity level, the integration project is a $300K–$500K investment before we see a single robot on the floor. Let's talk about whether that changes the payback model."

---

### Objection 17: "We just signed a new lease / We're in the middle of a facility transition"

**What it really means:** They've recently signed a multi-year lease and either (a) feel locked into the current facility's constraints, or (b) are mid-move and can't commit to anything new. Counterintuitively, a new lease is often the BEST time to introduce automation — the facility is being designed and the window to embed automation in the layout is open.

**FFR Response:**
"A new lease is actually the best news I've heard today — and I mean that. [F&B distributor] in [city] signed their 10-year lease 60 days before I talked to them. They'd designed the floor plan around conventional racking. What they found was that by bringing us in before the racking order was placed, they redesigned a 40,000 sq ft section for GTP automation — and saved $2.2M in racking cost by not installing shelving that would have had to come out anyway. The lease commitment is exactly the reason to look at automation now, not later. What does your design timeline look like?"

**ABC Response:**
"A new facility is the moment I'd most want to be talking to you — so I'm glad you brought it up. (Acknowledge) Greenfield or significant retrofit decisions made in the first 90 days of a new lease are the ones that drive facility economics for the entire lease term. Automation designed in from day one costs 30–40% less than a brownfield retrofit. (Bridge) I'm not asking you to commit to anything. I'm asking for 45 minutes — ideally with your Director of Engineering on the call — to walk through what an automation-ready floor design would look like at your scale. If it's not the right fit, you've lost 45 minutes. If it is, you've potentially changed the economics of that facility for a decade. (Close)"

**Follow-up question:** "Has the racking order been placed yet? And what's your go-live date for the new facility? The earlier we are in the design cycle, the more options we have."

**Proof point:** "Automation designed into a new facility reduces the total project cost by 30–40% vs. retrofitting an operational facility. The break-even on automation ROI in a greenfield is 18–36 months vs. 24–48 months for brownfield."

**When to walk away:** If they have already signed off on the floor plan, placed the racking order, and go-live is in less than 90 days — this particular facility may be locked. Pivot to a future-phase conversation or an adjacent facility in their network.

---

### Objection 18: "We tried automation before and it failed"

**What it really means:** A previous AMR deployment, conveyor system, or automation vendor project failed — either technically (system didn't perform), operationally (team didn't adopt it), or commercially (the vendor went out of business or failed to support it). This is the most serious trust objection in warehouse automation and must be handled with complete seriousness — never dismissiveness.

**FFR Response:**
"That's the most important thing you could have told me — and I'm not going to brush past it. Before I say anything else, can you tell me specifically what failed? Was it the system itself, the integration with your WMS, the vendor's support after go-live, or adoption on the floor? Because what I do next depends entirely on whether the problem was the technology, the implementation, or the post-sale relationship — and I'd rather identify if we have the same issue than pitch you past it."

**ABC Response:**
"A failed automation project is a serious thing — it costs money, disrupts operations, and damages credibility with the exec team. I take that seriously. (Acknowledge) Before I tell you anything about us, I want to understand what happened. Specifically: was it a technology failure (the system didn't hit the throughput numbers promised), an integration failure (WMS didn't sync correctly), a service failure (the vendor couldn't support it after go-live), or an adoption failure (the floor team worked around the system)? (Bridge) Each of those has a different root cause — and a different answer. If the answer is the same problem we have, I'll tell you that directly. If it's something we've solved, I'd like to show you the evidence. Can you walk me through what happened? (Close)"

**Follow-up question:** "What vendor was it, and what specifically was promised vs. what was delivered? I want to know whether the gap was in the technology, the implementation, or the support model."

**Proof point:** Prepare a "lessons learned from prior deployments" document specific to the failure mode they describe. If it was a Locus failure — explain specifically how your architecture differs. If it was a WMS integration failure — have a technical architecture document ready.

**When to walk away:** If the failure was less than 12 months ago and involved a system still in place (they tried to rip it out but it's still running at partial capacity) — this is a political situation, not just a technical one. The last vendor may have contractual relationships that complicate your path. Assess carefully before investing in this account.

---

### Objection 19: "The CapEx doesn't fit our budget cycle / We're not in an automation CapEx year"

**What it really means:** CapEx budget for the fiscal year has already been allocated, or the annual planning cycle hasn't opened a warehouse automation line item. This is often a genuine timing objection — large companies plan CapEx 12–18 months in advance. It may also be a soft rejection from a VP who hasn't gotten executive alignment.

**Who raises this:** CFO / VP Finance (budget gatekeeper), or VP Supply Chain deflecting because they haven't gotten C-suite buy-in.

**FFR Response:**
"Budget cycle timing is real — and I respect it. [3PL company] in [city] had the same answer in February. What they found was that when they documented the labor cost impact — specifically, $2.8M in annual picker labor on 120 open positions — their CFO opened an expedited CapEx review. They were approved in 60 days because the CFO could see that waiting another 12 months for the next cycle was costing $280K per month. The question isn't whether automation fits this year's budget — it's whether the cost of not automating is visible to the people who control the budget. Is your CFO aware of the current labor cost run rate?"

**ABC Response:**
"Budget cycles are real and I'm not going to pretend they aren't. (Acknowledge) What I'd ask you to consider is this: most CapEx cycle timing questions turn into approved projects when the right financial model reaches the CFO. Every month you wait is a quantifiable labor cost. If your facility has 80 pickers at $22/hour loaded — that's $4.1M per year. A $3M automation deployment that runs for 10 years starts paying back in Year 2. The question isn't whether it fits the budget cycle — it's whether the CFO has seen a number that makes delaying more expensive than approving. (Bridge) Would it be worth building a preliminary financial model together — even directionally — so you have something specific to bring to the next CapEx review? (Close)"

**Follow-up question:** "When does your next CapEx planning cycle open? And has anyone at your company built a financial model for automation yet, or is this the first time it's been quantified?"

**Proof point:** "The companies I've seen go from 'not in budget' to 'approved' fastest are the ones where someone brought a CFO-ready P&L model to the table. I can build a directional version in 48 hours using public data. Would that be useful?"

**When to walk away:** If this is genuinely a budget constraint (the year is almost over, the next cycle is 4 months away, and there's no urgency driver) — use the time to build the CFO model and get executive alignment now so they go into the planning cycle with an approved concept, not a cold ask.

---

### Objection 20: "We need to go to RFP / Our procurement policy requires competitive bids"

**What it really means:** Enterprise procurement requires a formal RFP process before any capital purchase above a threshold (typically $500K–$2M, depending on company size). This is a legitimate structural requirement, not a rejection. But it's also an objection that can be influenced — the company that helps write the requirements typically wins the RFP.

**FFR Response:**
"An RFP process is completely appropriate at this scale — and I'd expect nothing less. [Company] in [sub-vertical] went through a 6-vendor RFP. What they found was that the vendor who had been engaged in the discovery process before the RFP was issued understood their specific WMS constraints, their throughput profile, and their labor profile in a way that the other five vendors didn't. That depth of understanding came through in every requirement they wrote — and it showed in the final scoring. I'm not asking to skip your RFP — I'm asking to be the vendor who understands your operation at the level that makes the RFP requirements match your actual problem. Can I get on a site visit before you write the requirements?"

**ABC Response:**
"A competitive RFP is the right governance for a decision of this size — I respect that. (Acknowledge) Here's what I know about automation RFPs: the companies that write the requirements without deep vendor input often get bids that are technically compliant but operationally mismatched. The vendors who win RFPs usually started the relationship before the RFP was written. (Bridge) I'm not asking to influence the process unfairly — I'm asking for the opportunity to understand your specific operation well enough that the requirements you write actually solve your problem. A site visit and a discovery call before the RFP goes out doesn't cost you anything, and it makes your requirements sharper. Would you be open to that? (Close)"

**Follow-up question:** "When is the RFP expected to go out, and who is leading the requirements development on your team? I want to make sure we're connected with the right people at the right time."

**Proof point:** "In the last four RFPs we were involved in from the beginning, we won three. In the two RFPs we received cold without prior engagement, we won zero. The difference is discovery depth."

**When to walk away:** If procurement has formally locked the RFP process and cannot allow pre-RFP vendor engagement due to fairness policies — participate in the RFP on its terms, but invest maximum effort in the requirements clarification process and technical specification questions.

---

### Objection 21: "We already work with [Dematic / AutoStore / Locus / 6 River / Symbotic]"

**What it really means:** An existing automation vendor is installed in one or more of their facilities. This may mean you're locked out entirely, or it may mean you have an expansion or adjacent use case opportunity. Know the competitor's specific system type before responding — ASRS displacement has high switching cost; AMR expansion is common.

**FFR Response:**
"Good to know — and I want to understand the scope before I say anything else. Is [competitor] deployed in a single facility or across your network? And is it handling one use case or the full picking operation? I ask because [company] in [sub-vertical] had [competitor] running their pallet storage — it was working well — and they brought us in for a completely different use case: their each-pick zone and returns processing, which [competitor] couldn't handle economically. They never displaced [competitor]; they added us as a complementary system for the use cases outside their contract. Is your operation 100% covered, or are there zones or facilities that aren't in scope?"

**ABC Response:**
"[Competitor] is a real player — good to understand where they are in your operation. (Acknowledge) Before I position against them, I'd want to know: what use cases are they covering, and are there any throughput gaps, accuracy issues, or zones they're not handling? (Bridge) I'm not here to displace a working system — that's expensive and disruptive. But most large operations have multiple use cases, and very few vendors are the right solution for all of them. If there's a zone where you're still doing it manually, or a throughput ceiling you're hitting despite the automation in place, that's where I'd want to look. (Close)"

**Follow-up question:** "What use case and zones is [competitor] covering, and what's your order accuracy and pick rate in those zones vs. the rest of the facility? I want to see if there's a specific gap before I make any claim."

**Competitive framing by competitor:**
- **Dematic:** "Dematic is strong on ASRS and conveyor. They're typically not cost-effective for each-pick AMR applications at your scale."
- **AutoStore:** "AutoStore is excellent for each-pick density storage. Their constraint is throughput ceiling at high volume — if you're scaling past X units/hour, they hit a performance limit."
- **Locus Robotics:** "Locus is a solid AMR platform. If they're in place, the question is whether the ROI model accounted for RaaS subscription costs at full deployment scale."
- **6 River (Shopify):** "6 River is primarily an e-commerce operator tool. If you're doing B2B bulk distribution or store replenishment, there are use cases they weren't designed for."

**When to walk away:** If the competitor has a fully deployed, enterprise-wide ASRS installation with a 10-year service contract — displacing that infrastructure is a 24-36 month sales cycle minimum. Assess whether the expansion opportunity is real before investing.

---

### Objection 22: "Labor isn't really a problem for us right now"

**What it really means:** They haven't experienced an acute labor crisis, they may be in a lower-cost labor market, or they have managed turnover through wage premiums and retention programs. This objection requires precision — it's very possible they don't have a labor crisis, in which case accuracy, throughput ceiling, or real estate constraints may be the better angle.

**FFR Response:**
"I appreciate you saying that — it tells me that the labor angle isn't where I should start. Can I ask: what's your current pick rate, and where do you see your throughput ceiling? Because the reason a lot of facilities get to automation isn't a labor crisis — it's that they can't add enough floor space and headcount fast enough to keep up with volume growth. [Building materials distributor] in [city] had strong labor retention, low turnover, and a solid team. The reason they automated was that they needed to add 40% throughput capacity without a 50,000 sq ft expansion. What's your volume growth trajectory look like over the next 3 years?"

**ABC Response:**
"If labor is stable for you right now, that's actually better — it means we can have a conversation about throughput and capacity rather than crisis management. (Acknowledge) Automation ROI has three drivers: labor cost reduction, accuracy improvement, and throughput capacity expansion. Not every company comes to automation through a labor crisis. Some come because they're growing 20% a year and can't add square footage fast enough, or because their order accuracy is generating chargebacks that cost more than the automation would. (Bridge) Which of those resonates with your situation? I'd rather find the right angle for your operation than assume you have a problem you've already told me you don't have. (Close)"

**Follow-up question:** "What's your volume growth forecast, and what's your current pick accuracy rate? If labor is solid, I want to understand which of the other ROI drivers might be relevant to your operation."

**When to walk away:** If they genuinely have low labor costs (rural location, strong retention, minimal turnover), strong pick accuracy, stable throughput well within capacity, and no growth projections — the ROI model may not justify automation at this facility. Be honest: "At your current labor cost and throughput level, the payback period on full automation may be longer than your typical CapEx threshold. Let's talk about what would change that calculus and stay in touch."

---

### Objection 23: "Our SKUs are too irregular / Our product mix isn't automation-friendly"

**What it really means:** Their product catalog includes many non-conveyable items — oversized, irregular, fragile, heavy, or variable-dimension products — that don't fit conventional automation assumptions. This is most common in building materials, industrial distribution, and mixed F&B operations. It's a legitimate technical concern that requires an honest response.

**FFR Response:**
"That's one of the most important technical questions to answer before proposing anything — and I'm glad you raised it. [Building materials distributor] in [city] said the same thing. They carried everything from 3-inch screws to 12-foot conduit. What they found was that automation doesn't have to be all-or-nothing: they identified their top 300 SKUs by pick frequency — mostly fasteners, fittings, and small hardware — which represented 70% of their pick activity and were perfectly automatable. They left the oversized and irregular items on conventional racks with human pickers. Their labor reduction came entirely from automating the high-frequency zone. Have you done a SKU velocity analysis to see what percentage of your pick activity comes from your most conveyable items?"

**ABC Response:**
"SKU mix analysis is exactly the right place to start — I wouldn't want to propose a system without it. (Acknowledge) Here's what I've seen across similar operations: most irregular SKU catalogs have a core of high-frequency, regular-dimension items that represent 60–80% of pick activity. The question isn't whether all your SKUs are automatable — it's whether enough of your pick activity is to justify the ROI. (Bridge) If you can share your SKU velocity data, or even your top 100 SKUs by pick frequency, I can run a quick automatable-SKU analysis and tell you exactly what the potential throughput impact is — and what we'd leave to manual. Would that be a useful first step? (Close)"

**Follow-up question:** "Can you give me a rough breakdown of your pick activity by SKU type — what percentage are standard-dimension items vs. irregular or oversized? Even a rough estimate helps me assess the opportunity before we go any further."

**Proof point:** "In facilities with high SKU irregularity, we typically find that 55–70% of actual pick volume comes from the automatable portion of the catalog. That 55–70% is all the ROI model needs to justify the investment."

**When to walk away:** If they are a pure irregular/heavy/oversized SKU operation — building materials with no standard small hardware, or an industrial distributor handling only large equipment — the automation ROI genuinely may not be there with current technology. Be honest and come back when the technology catches up (heavy-item AMRs are improving rapidly).

---

## Universal Objections — Warehouse Automation Framing Notes

Apply these overlays to the 15 universal objections from the base skill:

| Objection | Warehouse Automation-Specific Framing |
|-----------|---------------------------------------|
| "Too expensive" | Translate price to payback period and annual labor cost reduction. "$3M system saving $1.8M/year in labor = 20-month payback." Never just quote price. |
| "Happy with current solution" | Ask for current pick rate, order accuracy rate, and labor cost per pick. "Happy" without metrics is just unfamiliarity with the gap. |
| "Need to think about it" | Identify whether it's CapEx timing, WMS readiness, or committee alignment. Each has a specific response. |
| "Send more information" | Send a sub-vertical-specific case study + directional ROI model using their publicly available labor data. Never generic content. |
| "Not ready right now" | Tie to their CapEx cycle: "When does your next CapEx planning window open? I want to make sure the financial model is ready when that window does." |
| "Need to talk to my team" | "Who specifically? I want to make sure I have the right materials for each stakeholder — the CFO presentation is different from the Director of Engineering briefing." |
| "Tried it before" | This is the most important objection in this vertical. Never brush past it. Ask exactly what failed before saying anything about yourself. |
| "Competitor has feature X" | Ask what WMS the competitor integrates with and at what version. Integration depth is your most common differentiator. |
| "We can build this" | Rare in this vertical — "we can build this" usually means "we already have a WCS vendor in mind." Ask who. |
| "Don't see ROI" | Build the ROI from their labor data. Never use industry averages alone. "At your labor cost, the payback is X years — here's the math." |
| "Locked in a contract" | Ask which vendor and what the remaining term is. Start relationship now — win the next decision cycle. |
| "Not a priority" | Quantify the current cost: "Your open warehouse positions represent approximately $[X]M in labor cost and throughput gaps. When does this become a priority?" |
| "No bandwidth to implement" | "Implementation is managed by our project team. Your Director of Engineering leads 3 design sessions. Your floor team gets 2 training days. We run the deployment." |
| "How do I know it'll work?" | Offer a reference from same sub-vertical + similar facility size + same WMS. Offer a site visit to a live deployment. |
| "Not interested" | "What would need to be true for automation to be interesting? Is it a throughput threshold, a labor cost threshold, or a timeline trigger I should watch for?" |

---

## Competitive Positioning — Quick Reference

| Competitor | Primary Use Case | Key Weakness | Your Opening Line |
|-----------|-----------------|-------------|-------------------|
| **Dematic** | ASRS, conveyor, sortation | High minimum project size ($5M+), long lead times, limited AMR portfolio | "Dematic is the right choice for a $15M ASRS project. If your use case is each-pick AMR or a sub-$5M deployment, let's talk about fit." |
| **AutoStore** | Each-pick cube storage | Throughput ceiling at high volume, requires custom bin dimensions | "AutoStore is excellent up to [X] units/hour. If your peak demand is above that, we need to look at a different architecture." |
| **Locus Robotics** | AMR pick-assist | RaaS model can exceed CapEx TCO at high deployment scale, Shopify acquisition uncertainty | "Locus built a strong AMR platform. The question is whether the RaaS model at your deployment scale pencils out vs. an ownership model." |
| **6 River Systems** | AMR pick-assist (e-commerce) | Limited B2B/bulk distribution capabilities, Shopify-influenced roadmap | "6 River is optimized for e-commerce each-pick. If you're doing B2B bulk distribution or store replenishment, the use case fit is worth examining." |
| **Symbotic** | Full ASRS (Walmart-scale) | Minimum deal size $50M+, 24–36 month implementation | "Symbotic is a transformational platform at the Walmart scale. For regional DC networks, the economics and timeline are usually out of range." |
| **Körber** | WMS + automation integration | More WMS vendor than automation vendor; AMR portfolio is limited | "Körber's automation story runs through their WMS. If your WMS is already locked, their AMR story is limited." |

---

## Pricing Deep Dive — Warehouse Automation Framing

When handling price objections in warehouse automation, always anchor to labor economics:

**The Labor Cost Frame:**
"Let's use your numbers. You have approximately [X] pickers in your pick zone. At $[X]/hour loaded — that's $[X]M per year in addressable labor. Our system replaces [X]% of that pick activity. Annual savings: $[X]M. System cost: $[X]M. Payback: [X] years. Does that payback period fit your CapEx threshold?"

**The Throughput Ceiling Frame:**
"You're growing [X]% year over year. At that trajectory, you'll need to add [X] additional pickers next year to maintain throughput — or build a [X] sq ft expansion. What would either of those cost? Our automation investment replaces both."

**The Accuracy Chargeback Frame:**
"What's your current order accuracy rate? Industry average for manual pick operations in your sub-vertical is [X]%. At [X] million units per year, the cost of the error rate — chargebacks, re-picks, customer service — is approximately $[X]M annually. Our system runs at 99.9% accuracy. The accuracy improvement alone funds a meaningful portion of the investment."

---

*Generated by AI Sales Team — Warehouse Automation Vertical | `/sales robotics objections <prospect>`*
