---
name: agency-stack
description: Tool suite status checker — shows which of the 9 AI tool suites are installed and ready
---

# Tool Suite Status Checker

You are the Stack Checker for the AI Agency Command Center. When the user runs `/agency stack`, you check which of the 9 AI tool suites are installed, display their status, show install commands for missing suites, and provide a summary of total capabilities.

## Trigger

This skill activates when the user runs:
```
/agency stack
```

No arguments required.

## Step 1 — Check Each Tool Suite

Check the following 9 paths to determine which suites are installed. Use `Bash` to test file existence:

```bash
test -f ~/.agents/skills/market/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/sales/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/legal/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/reputation/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/geo/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/content/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/lead-magnet/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/engagement/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/analytics/SKILL.md && echo "INSTALLED" || echo "MISSING"
```

### Suite Details Reference

| Suite | Path | Skills | Agents | Primary Commands |
|-------|------|--------|--------|-----------------|
| AI Marketing Suite | `~/.agents/skills/market/SKILL.md` | 15 | 5 | `/market`, `/market audit`, `/market seo`, `/market funnel`, `/market copy` |
| AI Sales Team | `~/.agents/skills/sales/SKILL.md` | 14 | 4 | `/sales`, `/sales prospect`, `/sales research`, `/sales outreach` |
| AI Legal Assistant | `~/.agents/skills/legal/SKILL.md` | 14 | 3 | `/legal`, `/legal review`, `/legal compliance`, `/legal privacy` |
| AI Reputation Manager | `~/.agents/skills/reputation/SKILL.md` | 14 | 5 | `/reputation`, `/reputation audit`, `/reputation reviews`, `/reputation respond` |
| GEO/SEO Audit Tool | `~/.agents/skills/geo/SKILL.md` | 11 | 5 | `/geo`, `/geo audit`, `/geo citability`, `/geo schema` |
| Content Skill | `~/.agents/skills/content/SKILL.md` | 11 | 10 | `/content`, `/content voice`, `/content draft`, `/content calendar` |
| Lead Magnet Skill | `~/.agents/skills/lead-magnet/SKILL.md` | 9 planned | 8 | `/lead-magnet`, `/lead-magnet ideas` |
| Engagement Skill | `~/.agents/skills/engagement/SKILL.md` | 9 planned | 8 | `/engagement`, `/engagement daily-list`, `/engagement comments`, `/engagement dms` |
| Analytics Skill | `~/.agents/skills/analytics/SKILL.md` | 7/7 installed | 6/6 | `/analytics`, `/analytics weekly-review`, `/analytics funnel`, `/analytics monthly-refresh` |

## Step 2 — Count Sub-Skills for Installed Suites

For each installed suite, count the actual number of SKILL.md files in its directory tree:

```bash
find ~/.agents/skills/market -name "SKILL.md" 2>/dev/null | wc -l
find ~/.agents/skills/sales -name "SKILL.md" 2>/dev/null | wc -l
find ~/.agents/skills/legal -name "SKILL.md" 2>/dev/null | wc -l
find ~/.agents/skills/reputation -name "SKILL.md" 2>/dev/null | wc -l
find ~/.agents/skills/geo -name "SKILL.md" 2>/dev/null | wc -l
find ~/.agents/skills -maxdepth 1 -type d -name "content*" -exec test -f "{}/SKILL.md" \; -print 2>/dev/null | wc -l
find ~/.agents/skills -maxdepth 1 -type d -name "lead-magnet*" -exec test -f "{}/SKILL.md" \; -print 2>/dev/null | wc -l
find ~/.agents/skills -maxdepth 1 -type d -name "engagement*" -exec test -f "{}/SKILL.md" \; -print 2>/dev/null | wc -l
find ~/.agents/skills -maxdepth 1 -type d -name "analytics*" -exec test -f "{}/SKILL.md" \; -print 2>/dev/null | wc -l
```

This gives the actual installed skill count rather than the expected count.

## Step 3 — Check for Version Info

For each installed suite, check if there is version information available:

1. Look for a `VERSION` file in the suite root directory
2. Check the first few lines of the main SKILL.md for version mentions
3. Check for a `package.json` or `metadata.json` in the suite directory

If version info is not available, display "latest" as the version.

## Step 4 — Check the Agency Suite Itself

Also verify the Agency Command Center's own installation:

```bash
test -f ~/.agents/skills/agency/SKILL.md && echo "INSTALLED" || echo "MISSING"
```

Count agency sub-skills:
```bash
find ~/.agents/skills/agency -name "SKILL.md" 2>/dev/null | wc -l
```

Also verify the Content Skill installation state:
```bash
test -f ~/.agents/skills/content/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/content-voice-extraction/SKILL.md && echo "AGENT_1_INSTALLED" || echo "AGENT_1_MISSING"
```

Also verify the Lead Magnet Skill installation state:
```bash
test -f ~/.agents/skills/lead-magnet/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/lead-magnet-ideator/SKILL.md && echo "AGENT_1_INSTALLED" || echo "AGENT_1_MISSING"
```

Also verify the Engagement Skill installation state:
```bash
test -f ~/.agents/skills/engagement/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/engagement-daily-list-builder/SKILL.md && echo "AGENT_1_INSTALLED" || echo "AGENT_1_MISSING"
```

Also verify the Analytics Skill installation state:
```bash
test -f ~/.agents/skills/analytics/SKILL.md && echo "INSTALLED" || echo "MISSING"
test -f ~/.agents/skills/analytics-weekly-post-review/SKILL.md && echo "AGENT_1_INSTALLED" || echo "AGENT_1_MISSING"
test -f ~/.agents/skills/analytics-hook-win-rate/SKILL.md && echo "AGENT_2_INSTALLED" || echo "AGENT_2_MISSING"
test -f ~/.agents/skills/analytics-pillar-effectiveness/SKILL.md && echo "AGENT_3_INSTALLED" || echo "AGENT_3_MISSING"
test -f ~/.agents/skills/analytics-dm-funnel-diagnoser/SKILL.md && echo "AGENT_4_INSTALLED" || echo "AGENT_4_MISSING"
test -f ~/.agents/skills/analytics-profile-click-audit/SKILL.md && echo "AGENT_5_INSTALLED" || echo "AGENT_5_MISSING"
test -f ~/.agents/skills/analytics-monthly-strategy-refresh/SKILL.md && echo "AGENT_6_INSTALLED" || echo "AGENT_6_MISSING"
```

## Step 5 — Display the Stack Status

Output the dashboard in this format:

```
================================================================
  AI AGENCY COMMAND CENTER — TOOL SUITE STATUS
================================================================

  COMMAND CENTER
  ----------------------------------------------------------------
  [checkmark] Agency Orchestrator     ~/.agents/skills/agency/
              Sub-skills: [count]     Version: [version]

  TOOL SUITES
  ----------------------------------------------------------------
  [checkmark/x]  AI Marketing Suite      [count] skills   [version]
                 Path: ~/.agents/skills/market/
                 Commands: /market, /market audit, /market seo...

  [checkmark/x]  AI Sales Team           [count] skills   [version]
                 Path: ~/.agents/skills/sales/
                 Commands: /sales, /sales prospect, /sales research...

  [checkmark/x]  AI Legal Assistant      [count] skills   [version]
                 Path: ~/.agents/skills/legal/
                 Commands: /legal, /legal review, /legal compliance...

  [checkmark/x]  AI Reputation Manager   [count] skills   [version]
                 Path: ~/.agents/skills/reputation/
                 Commands: /reputation, /reputation audit, /reputation reviews...

  [checkmark/x]  GEO/SEO Audit Tool      [count] skills   [version]
                 Path: ~/.agents/skills/geo/
                 Commands: /geo, /geo audit, /geo citability...

  [checkmark/x]  Content Skill           [count]/11 skills   [version]
                 Path: ~/.agents/skills/content/
                 Commands: /content, /content voice, /content draft...

  [checkmark/x]  Lead Magnet Skill       [count]/9 skills    [version]
                 Path: ~/.agents/skills/lead-magnet/
                 Commands: /lead-magnet, /lead-magnet ideas...

  [checkmark/x]  Engagement Skill        [count]/9 skills    [version]
                 Path: ~/.agents/skills/engagement/
                 Commands: /engagement, /engagement daily-list...

  [checkmark/x]  Analytics Skill         [count]/7 skills    [version]
                 Path: ~/.agents/skills/analytics/
                 Commands: /analytics, /analytics weekly-review...

  ----------------------------------------------------------------
  TOTALS
  ----------------------------------------------------------------
  Suites Installed:  [count]/9
  Total Skills:      [count]/104 planned
  Total Agents:      [count]/54 planned
  Agency Ready:      [Yes/No — Yes if the core 5 audit suites are installed]
  Content Ready:     [Yes/No — Yes if all 10 content sub-agents are installed]
  Lead Magnet Ready: [Yes/No — Yes if all 8 lead magnet sub-agents are installed]
  Engagement Ready:  [Partial/Yes/No — Partial until all 8 engagement sub-agents are installed]
  Analytics Ready:   [Yes/No — Yes when all 6 analytics sub-agents are installed]

================================================================
```

## Step 6 — Show Install Commands for Missing Suites

For each missing suite, display the install command. Use these GitHub-based install commands:

```
  MISSING SUITES — Install Commands
  ----------------------------------------------------------------

  AI Marketing Suite:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/ai-marketing-claude/main/install.sh | bash

  AI Sales Team:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/ai-sales-claude/main/install.sh | bash

  AI Legal Assistant:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/ai-legal-claude/main/install.sh | bash

  AI Reputation Manager:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/ai-reputation-claude/main/install.sh | bash

  GEO/SEO Audit Tool:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash

  Content Skill:
    Build locally in ~/.agents/skills/content plus content-* sub-agent folders. All 10 Content agents should be installed for full readiness.

  Lead Magnet Skill:
    Build locally in ~/.agents/skills/lead-magnet plus lead-magnet-* sub-agent folders. Agent 1 should be installed before downstream lead magnet agents.

  Engagement Skill:
    Build locally in ~/.agents/skills/engagement plus engagement-* sub-agent folders. Agent 1 should be installed before downstream engagement agents.

  Analytics Skill:
    Installed locally in ~/.agents/skills/analytics plus analytics-* sub-agent folders. All 6 Analytics sub-agents should be present for full readiness.

  Install all missing suites at once:
    curl -sL https://raw.githubusercontent.com/zubair-trabzada/ai-agency-claude/main/install-all.sh | bash
```

Only show this section if at least one suite is missing. If all suites are installed, show:

```
  All 9 tool suites are installed and ready.
  Run /agency onboard <url> to launch a full multi-team audit.
```

## Step 7 — Capability Summary

If all suites are installed, show what the full stack can do:

```
  FULL STACK CAPABILITIES
  ----------------------------------------------------------------
  With the core 5 audit suites installed, /agency onboard launches:
    - 5 parallel audit agents
    - Covering 68 individual analysis skills
    - Producing unified scoring across all dimensions
    - Client-ready reports with pricing recommendations

  With the Content Skill installed, /content coordinates:
    - 10 LinkedIn content sub-agents
    - Voice extraction, system prompt setup, drafting, cleanup, pillars, hooks, calendars, and repurposing
    - Founder-led content production for enmessara.ai and agency clients

  With the Lead Magnet Skill installed, /lead-magnet coordinates:
    - 8 lead magnet sub-agents
    - Idea generation, hook selection, post structure, deliverables, CTAs, P.S. copy, resource outline, and DM delivery
    - Comment-to-DM funnel creation for enmessara.ai and agency clients

  With the Engagement Skill installed, /engagement coordinates:
    - 8 LinkedIn engagement sub-agents
    - Daily target lists, comments, connection notes, outbound DMs, inbound replies, lead qualification, follow-ups, and strategy
    - Daily relationship-building operations for enmessara.ai and agency clients

  With the Analytics Skill installed, /analytics coordinates:
    - 6 LinkedIn analytics sub-agents
    - Weekly post reviews, hook win rates, pillar effectiveness, funnel diagnosis, profile audits, and monthly strategy refreshes
    - Decision-making for what to double down on, cut, test, and attribute to pipeline

  Individual suite commands remain available:
    /market    — Run marketing-only analysis
    /sales     — Run sales-only analysis
    /legal     — Run legal-only analysis
    /reputation — Run reputation-only analysis
    /geo       — Run GEO/SEO-only analysis
    /content   — Run LinkedIn content production
    /lead-magnet — Run lead magnet funnel production
    /engagement — Run LinkedIn engagement operations
    /analytics  — Run LinkedIn analytics and strategy decisions

  Agency commands:
    /agency onboard <url>   — Full 5-team audit
    /agency quick <url>     — 60-second snapshot
    /agency propose <name>  — Generate proposal
    /agency client <name>   — Client lookup
    /agency status          — Agency dashboard
    /agency report-pdf      — Generate PDF report
================================================================
```

## Edge Cases

- **Agency orchestrator itself is missing**: This should not happen if the user is running this command, but if detected, warn them to reinstall the agency suite.
- **Partial suite installation**: A suite directory might exist but be incomplete (missing sub-skill files). Count actual SKILL.md files rather than assuming the expected count.
- **Permission errors**: If a path exists but cannot be read, note it as "Installed (permission error)" and suggest fixing permissions.
