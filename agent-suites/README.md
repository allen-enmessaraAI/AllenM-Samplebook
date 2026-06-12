# AllenM Samplebook Agent Suites
This repository contains the complete saved agent-suite library copied from the active local skills root. It is organized as Codex-compatible skill folders under `skills/`, with each agent prompt saved in its own `SKILL.md`.
## Contents
- Skill prompts: 154
- Total copied files: 208
- Source root: `<USER_HOME>/.agents/skills`
- Generated implementation plan: `IMPLEMENTATION_PLAN.md`

## Suite Inventory
### Content (11)
- `content` - Content Skill orchestrator for enmessara.ai — coordinates the LinkedIn content engine from voice extraction through drafting, cleanup, calendars, hooks, and repurposing
- `content-calendar-planner` - Agent 7 of the Content Skill — builds a 30-day LinkedIn content calendar from the 4 pillars, cadence, lead magnets, launches, hook frameworks, goals, and voice context
- `content-cleanup` - Agent 4 of the Content Skill — removes AI smell from LinkedIn drafts while preserving meaning, structure, and the saved writer voice
- `content-contrarian-pov` - Agent 9 of the Content Skill — writes contrarian POV and hot-take LinkedIn posts in the saved writer voice using a consensus view, actual position, proof, and tone
- `content-hook-library` - Agent 6 of the Content Skill — generates 30 LinkedIn hook variations by desire, curiosity, and fear triggers for a topic, goal, voice profile, and content pillar
- `content-listicle` - Agent 8 of the Content Skill — writes structured LinkedIn listicle posts for authority, saves, DMs, and tactical education in the saved writer voice
- `content-pillar-mapping` - Agent 5 of the Content Skill — maps 4 LinkedIn content pillars directly to offer, ICP, positioning, booked-call goals, and downstream post strategy
- `content-post-draft` - Agent 3 of the Content Skill — drafts 3 LinkedIn post versions in the saved writer voice from a topic, story, client conversation, insight, or rough idea
- `content-repurposing` - Agent 10 of the Content Skill — turns long-form source content into 5 distinct LinkedIn posts across listicle, contrarian, story, framework, and lead magnet angles
- `content-system-prompt-template` - Agent 2 of the Content Skill — converts the Agent 1 Voice Profile into a reusable LinkedIn ghostwriter system prompt for Projects, Custom GPTs, Gems, or downstream drafting agents
- `content-voice-extraction` - Agent 1 of the Content Skill — turns 10 LinkedIn posts into a structured Voice Profile that powers every downstream content agent

### Engagement (9)
- `engagement` - Engagement Skill orchestrator for enmessara.ai - coordinates an 8-agent LinkedIn engagement loop for daily lists, comments, connection messages, DMs, replies, qualification, follow-ups, and weekly strategy
- `engagement-comment-generator` - Agent 2 of the Engagement Skill - drafts five LinkedIn comment variations for a strategic post, optimized for visibility, specificity, and conversation-starting
- `engagement-connection-message` - Agent 3 of the Engagement Skill - drafts five LinkedIn connection request note variations under 300 characters with specific, no-pitch relationship context
- `engagement-daily-list-builder` - Agent 1 of the Engagement Skill - builds a curated daily LinkedIn engagement list of 20 profiles across ICP targets, adjacent voices, peers, and existing connections
- `engagement-dm-outreach` - Agent 4 of the Engagement Skill - drafts cold-ish LinkedIn DM opener variations for first-degree connections, plus reply and no-reply follow-up messages
- `engagement-follow-up-sequencer` - Agent 7 of the Engagement Skill - builds a four-touch LinkedIn DM follow-up sequence for warm leads who have not booked yet, spread over 30 days
- `engagement-lead-qualifier` - Agent 6 of the Engagement Skill - scores LinkedIn DM leads across ICP fit, pain awareness, budget, timing, and decision power to recommend book, qualify, nurture, or exit
- `engagement-reply-handler` - Agent 5 of the Engagement Skill - drafts three reply variations for inbound LinkedIn DMs based on the sender, conversation goal, fit, and next best action
- `engagement-strategy-planner` - Agent 8 of the Engagement Skill - builds a weekly LinkedIn engagement strategy with daily activities, time budget, priority matrix, KPIs, and recommendations

### Analytics (7)
- `analytics` - Analytics Skill orchestrator for enmessara.ai - coordinates a 6-agent LinkedIn analytics system for weekly post review, hook win rates, pillar effectiveness, funnel leaks, profile health, and monthly strategy refresh
- `analytics-dm-funnel-diagnoser` - Agent 4 of the Analytics Skill - diagnoses where the LinkedIn lead-generation funnel leaks from impressions to booked calls and clients
- `analytics-hook-win-rate` - Agent 2 of the Analytics Skill - tracks win rates across nine LinkedIn hook frameworks using qualified DMs and booked calls rather than vanity engagement
- `analytics-monthly-strategy-refresh` - Agent 6 of the Analytics Skill - synthesizes monthly LinkedIn analytics from Agents 1-5 into a 30-day strategy refresh and operating plan
- `analytics-pillar-effectiveness` - Agent 3 of the Analytics Skill - analyzes which LinkedIn content pillars drive qualified DMs and booked calls versus empty engagement
- `analytics-profile-click-audit` - Agent 5 of the Analytics Skill - audits LinkedIn profile clicks, connection conversion, profile health, and top-of-funnel visitor quality
- `analytics-weekly-post-review` - Agent 1 of the Analytics Skill - reviews last week's LinkedIn posts to identify top performers, flops, patterns, wasted reach, lead quality, and next-week recommendations

### Lead Magnet (9)
- `lead-magnet` - Lead Magnet Skill orchestrator for enmessara.ai - coordinates an 8-agent lead magnet funnel from idea, hook, post, deliverables, CTA, P.S., resource outline, and DM delivery sequence
- `lead-magnet-cta-variants` - Agent 5 of the Lead Magnet Skill - generates five CTA variations for LinkedIn lead magnet posts and recommends which to test based on reach, lead quality, DMs, or booked-call goals
- `lead-magnet-deliverables` - Agent 4 of the Lead Magnet Skill - generates 5-7 concrete deliverable bullets for a lead magnet post, using only assets actually inside the resource
- `lead-magnet-dm-sequence` - Agent 8 of the Lead Magnet Skill - writes a four-message DM delivery sequence that sends the lead magnet, keeps the conversation alive, and converts commenters into calls
- `lead-magnet-hook-framework` - Agent 2 of the Lead Magnet Skill - selects the best hook framework from 9 proven options based on lead magnet, proof level, ICP awareness, and post goal
- `lead-magnet-ideator` - Agent 1 of the Lead Magnet Skill - generates 10 lead magnet ideas mapped to offer, ICP pain, reusable resources, proof, build difficulty, honesty, and lead quality
- `lead-magnet-post-structure` - Agent 3 of the Lead Magnet Skill - builds a full LinkedIn lead magnet post using the proven 7-part structure from a selected hook, deliverables, keyword, offer, and voice profile
- `lead-magnet-ps-generator` - Agent 6 of the Lead Magnet Skill - generates eight P.S. variations for LinkedIn lead magnet posts across done-for-you, time saver, filter, curiosity, repost, connection, proof, and call angles
- `lead-magnet-resource-outline` - Agent 7 of the Lead Magnet Skill - designs the actual lead magnet resource structure readers receive, including master layout, sections, CTA copy, DM script, and upsell path

### Agency (9)
- `agency`
- `agency-client` - Client lookup and history — searches all output files for a client and displays a comprehensive summary
- `agency-onboard` - Full Agency Onboard — launches 5 parallel audit teams and produces a unified client-ready report with composite scoring
- `agency-pipeline` - Prospect Pipeline Manager — scans all audit files to build a scored, staged pipeline view with revenue projections
- `agency-propose` - Unified Agency Proposal Generator — builds a three-tier service proposal with ROI projections from all available audit data
- `agency-quick` - 60-Second Agency Snapshot — rapid 5-dimension assessment without subagents, outputs a compact scorecard
- `agency-report-pdf` - Unified PDF report generator — combines all audit scores into a professional client-ready PDF
- `agency-stack` - Tool suite status checker — shows which of the 9 AI tool suites are installed and ready
- `agency-status` - Agency dashboard — shows agency-wide status, pipeline metrics, installed tools, and recent activity

### GEO (15)
- `geo` - GEO-first SEO analysis tool. Optimizes websites for AI-powered search engines (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations. Performs full GEO audits, citability scoring, AI crawler analysis, llms.txt generation, brand mention scanning, platform-specific optimization, schema markup, technical SEO, content quality (E-E-A-T), and client-ready GEO report generation. Use when user says "geo", "seo", "audit", "AI search", "AI visibility", "optimize", "citability", "llms.txt", "schema", "brand mentions", "GEO report", or any URL for analysis.
- `geo-audit` - Full website GEO+SEO audit with parallel subagent delegation. Orchestrates a comprehensive Generative Engine Optimization audit across AI citability, platform analysis, technical infrastructure, content quality, and schema markup. Produces a composite GEO Score (0-100) with prioritized action plan.
- `geo-brand-mentions` - Brand mention and authority scanner for AI visibility. Analyzes brand presence across platforms that AI models rely on for entity recognition and citation decisions. Produces a Brand Authority Score (0-100) with platform-specific recommendations.
- `geo-citability` - AI citability scoring and optimization. Analyzes web page content to determine how likely AI systems (ChatGPT, Claude, Perplexity, Gemini) are to cite or quote passages from the page. Provides a citability score (0-100) with specific rewrite suggestions.
- `geo-compare` - Monthly delta tracking and progress reporting for GEO clients. Compares two GEO audits (baseline vs. current), calculates score improvements across all categories, tracks action item completion, and generates a "here's your progress" client report. Use when user says "compare", "delta", "monthly report", "progress", "confronta", "progressi", "report mensile", or when running a monthly client check-in.
- `geo-content` - Content quality and E-E-A-T assessment for AI citability — evaluate experience, expertise, authoritativeness, trustworthiness, and content structure
- `geo-crawlers` - AI crawler access analysis. Checks robots.txt, meta tags, and HTTP headers to determine which AI crawlers can access the site. Provides a complete access map and recommendations for maximizing AI visibility while maintaining appropriate control.
- `geo-llmstxt` - Analyzes and generates llms.txt files -- the emerging standard for helping AI systems understand website structure and content. Can validate existing llms.txt files or generate new ones from scratch by crawling the site.
- `geo-platform-optimizer` - Platform-specific AI search optimization — audit and optimize for Google AI Overviews, ChatGPT, Perplexity, Gemini, and Bing Copilot individually
- `geo-proposal` - Auto-generate a professional, client-ready GEO service proposal from audit data. Creates a full proposal in markdown and PDF including executive summary, findings, recommended service packages (Basic/Standard/Premium), pricing, timeline, and terms. Use when user says "proposal", "proposta", "offerta", "preventivo", "generate proposal", or after completing a GEO audit for a prospect.
- `geo-prospect` - CRM-lite for managing GEO agency prospects and clients. Track leads through the full sales pipeline: Lead → Qualified → Proposal Sent → Won → Lost. Store audit history, notes, deal values, and generate pipeline summaries. Use when user says "prospect", "lead", "client", "pipeline", "crm", "nuovo prospect", "aggiungi cliente", or when managing the business side of GEO services.
- `geo-report` - Generate a professional, client-facing GEO report combining all audit results into a single deliverable with scores, findings, and prioritized actions
- `geo-report-pdf` - Generate a professional PDF report from GEO audit data using ReportLab. Creates a polished, client-ready PDF with score gauges, bar charts, platform readiness visualizations, color-coded tables, and prioritized action plans.
- `geo-schema` - Schema.org structured data audit and generation optimized for AI discoverability — detect, validate, and generate JSON-LD markup
- `geo-technical` - Technical SEO audit with GEO-specific checks — crawlability, indexability, security, performance, SSR, and AI crawler access

### Legal (14)
- `legal`
- `legal-agreement`
- `legal-compare` - Side-by-side comparison of two contract versions or two different contracts with change tracking, favorability analysis, and risk assessment
- `legal-compliance`
- `legal-freelancer`
- `legal-missing` - Identifies critical clauses and protections that should be in a contract but are missing, with urgency ratings and ready-to-insert language
- `legal-nda` - Generates a complete, customized Non-Disclosure Agreement with plain English annotations, tailored to the specific parties and situation
- `legal-negotiate` - Generates specific counter-proposals for every unfavorable clause, with replacement language, negotiation talking points, and a ready-to-send email template
- `legal-plain` - Translates every clause of a contract from legalese into clear, plain English with flags for deliberately confusing or misleading language
- `legal-privacy`
- `legal-report-pdf`
- `legal-review`
- `legal-risks` - Clause-by-clause contract risk analysis with severity scoring, financial exposure estimates, and prioritized remediation guidance
- `legal-terms` - Generates complete, GDPR/CCPA-compliant Terms of Service for a website or SaaS product, with plain English summaries for each section

### Market (21)
- `market`
- `market-ads`
- `market-audit`
- `market-brand`
- `market-competitors`
- `market-copy`
- `market-dental`
- `market-emails`
- `market-funnel`
- `market-home-services`
- `market-landing`
- `market-launch`
- `market-medspa`
- `market-proposal`
- `market-real-estate`
- `market-report`
- `market-report-pdf`
- `market-robotics`
- `market-seo`
- `market-social`
- `market-veterinary`

### Reputation (15)
- `reputation`
- `reputation-alerts`
- `reputation-audit`
- `reputation-competitors`
- `reputation-crisis`
- `reputation-quick`
- `reputation-recover` - Multi-step recovery strategy to turn a specific negative review into a positive outcome
- `reputation-report-pdf`
- `reputation-request`
- `reputation-respond`
- `reputation-reviews`
- `reputation-sentiment`
- `reputation-seo`
- `reputation-social`
- `reputation-trends`

### Sales (39)
- `sales`
- `sales-competitors`
- `sales-contacts`
- `sales-followup`
- `sales-icp`
- `sales-icp-dental`
- `sales-icp-home-services`
- `sales-icp-medspa`
- `sales-icp-real-estate`
- `sales-icp-veterinary`
- `sales-objections`
- `sales-objections-dental`
- `sales-objections-home-services`
- `sales-objections-medspa`
- `sales-objections-real-estate`
- `sales-objections-veterinary`
- `sales-outreach`
- `sales-outreach-dental`
- `sales-outreach-home-services`
- `sales-outreach-medspa`
- `sales-outreach-real-estate`
- `sales-outreach-veterinary`
- `sales-prep`
- `sales-proposal`
- `sales-prospect`
- `sales-qualify`
- `sales-report`
- `sales-report-pdf`
- `sales-research`
- `sales-research-dental`
- `sales-research-home-services`
- `sales-research-medspa`
- `sales-research-real-estate`
- `sales-research-veterinary`
- `sales-robotics`
- `sales-robotics-icp`
- `sales-robotics-objections`
- `sales-robotics-outreach`
- `sales-robotics-research`

### Theme (2)
- `theme-dark`
- `theme-light`

### Other (3)
- `cro-advisor` - Revenue leadership for B2B SaaS companies. Revenue forecasting, sales model design, pricing strategy, net revenue retention, and sales team scaling. Use when designing the revenue engine, setting quotas, modeling NRR, evaluating pricing, building board forecasts, or when user mentions CRO, chief revenue officer, revenue strategy, sales model, ARR growth, NRR, expansion revenue, churn, pricing strategy, or sales capacity.
- `enmessara-blog`
- `heygen-video` - Runs the HeyGen Avatar Automation pipeline to produce a finished avatar video from a script. Use this skill any time the user wants to generate an avatar video, turn a script into a video, run the video pipeline, produce course content or training videos, or mentions HeyGen, ElevenLabs, or the script-to-video workflow. Trigger even if the user phrases it casually — e.g. "make a video from this", "run the pipeline on my script", "generate a video for lesson 3", or "process this doc".

## Usage
Install or reference any agent by copying the relevant folder from `skills/` into the target Codex skills directory. The full prompt body for every agent is also embedded in `IMPLEMENTATION_PLAN.md` for implementation review and audit.
