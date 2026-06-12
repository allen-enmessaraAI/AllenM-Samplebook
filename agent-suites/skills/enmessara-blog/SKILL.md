# Enmessara AI — Asset: Blog

## Skill Purpose
End-to-end blog content production pipeline. Scans email for AI/automation/infrastructure news, researches public company filings, produces a branded blog post + LinkedIn post + one-sheeter, and stages everything for publication.

## Trigger
`/enmessara-blog`

## Invocation Name
`enmessara-blog`

---

## Workflow — Step by Step

### STEP 1 — Source Gathering

**Email scan:**
- Search the user's inbox (allen@enmessara.ai) using the Gmail MCP tools.
- Look for messages received **since the last scan** (track date in `/Users/userliberty/.claude/skills/enmessara-blog/.last_scan`). If no `.last_scan` file exists, default to last 7 days.
- Search queries to run (combine results):
  - `"AI agents" OR "AI automation" OR "agentic" OR "LLM" OR "foundation model"`
  - `"cloud infrastructure" OR "data center" OR "GPU" OR "AI chip"`
  - `"AI startup" OR "Series A" OR "Series B" OR "funding round" AI`
  - `"earnings" OR "quarterly results" (AI OR cloud OR datacenter)`
- Filter for: articles, newsletters, promotions, blog digests, social post notifications — anything with substantive AI/automation/infrastructure content.
- Extract: subject, sender, date, key content/links.

**SEC / EDGAR research:**
- For any **public companies** mentioned in the email content, check the SEC EDGAR system (via web search/fetch) for earnings reports filed in the **last 30 days**.
- If found, pull key metrics: revenue, guidance, AI-specific commentary, capex related to AI/cloud.
- Only include EDGAR data if a filing exists within 30 days. Skip otherwise.

**Web enrichment:**
- For the top stories/themes surfaced from email, do a brief web search to get additional context, competing viewpoints, or data points that strengthen the eventual blog post.

**Output of Step 1:**
Present a numbered summary to the user:
```
## Source Scan Results — [Date]

1. [Topic/Headline] — Source: [sender/newsletter], Key insight: [1-2 sentences]
2. [Topic/Headline] — Source: [sender/newsletter], Key insight: [1-2 sentences]
...

### SEC/EDGAR Findings (if any)
- [Company]: [Filing type], [Date], [Key AI/cloud metrics]

Which topic(s) would you like to develop into a blog post?
```

After presenting, **update `.last_scan`** with today's date:
```bash
echo "YYYY-MM-DD" > /Users/userliberty/.claude/skills/enmessara-blog/.last_scan
```

---

### STEP 2 — Topic Selection

Wait for the user to confirm which topic(s) to proceed with. The user may:
- Pick one topic for a single blog post
- Pick multiple topics to combine into a single thematic post
- Ask for more detail on a specific item before deciding

Do NOT proceed to writing until the user explicitly confirms.

---

### STEP 3 — Blog Post + LinkedIn Copy

**Blog Post (Google Doc):**
- Create the blog post as a Google Doc in the **"Enmessara Blog Drafts"** folder (auto-create folder if it doesn't exist). Use Google Drive MCP tools (`create_file`).
- Writing guidelines:
  - **SEO-optimized**: Include target keywords naturally, use H2/H3 structure, meta description suggestion at top
  - **Product callouts**: Weave in natural mentions of tools, platforms, and products relevant to the topic — formatted as inline links where possible. These become backlink/affiliate opportunities. Flag them with a comment like `[AFFILIATE OPPORTUNITY: product_name]` in the doc.
  - **Tone**: Authoritative but accessible. Enmessara brand voice — practitioner-level insight, not hype.
  - **Length**: 1,200–2,000 words
  - **Structure**: Hook → Context → Analysis → Implications → Takeaway/CTA
  - **Include**: At least one data point or stat, one quote or reference to a specific source

**LinkedIn Post (in chat + Google Doc):**
- Write a LinkedIn post designed to:
  - Drive traffic to the blog (include placeholder `[BLOG LINK]`)
  - Spark engagement in comments with a thought-provoking question or contrarian take
  - 150–250 words max
  - Use line breaks for readability (no walls of text)
  - End with a clear call-to-action that invites discussion
  - NO hashtags in the body — add 3–5 relevant hashtags as a separate final line

**After user approves the LinkedIn post:**
- Append the LinkedIn post to the **master LinkedIn Posts Google Doc** (ID: `110PGXMII0CGP3fUJK1p6EeY5SnRDmXURUQyJZ8_1U3U`)
  - Add a section header matching the blog title
  - Include the `[BLOG LINK]` placeholder (replace with live URL when published)
  - Use the browser to navigate to the doc, scroll to the end, and type the content if the Drive MCP cannot update the doc directly
  - Leave a comment tagging `allen@enmessara.ai` that says: "LinkedIn post ready to publish — review and schedule"

Present both to the user for review. Wait for approval or revision requests.

---

### STEP 4 — Branding & HTML Generation

Once blog copy is approved:

1. **Download the Google Doc content** (use Drive MCP `read_file_content` or `download_file_content`).

2. **Generate the blog post HTML** as a standalone page with Enmessara Light Theme CSS variables.

3. **Apply `/theme-light`** — invoke the Enmessara AI Light Theme skill to ensure all colors, typography, and visual elements conform to brand spec:
   - Background: `#F0F2F8`
   - Text: `#071525`
   - Accent: `#00D4FF` / `#00A8CC`
   - Font: Inter
   - Include the header with logo reference and footer with "enmessara.ai"

4. **REQUIRED: Include the site-wide navigation bar** — Every blog post HTML MUST include the following nav bar immediately after `<body>` and before any post-specific content. This ensures readers can navigate to the rest of the Enmessara site. Do NOT omit this.

   ```html
   <!-- Site Navigation -->
   <style>
     .enmessara-site-nav { background:#071525;padding:14px 0;font-family:'Inter',system-ui,sans-serif;position:relative;z-index:100; }
     .enmessara-site-nav a { text-decoration:none; }
     .enmessara-site-nav .nav-inner { max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between; }
     .enmessara-site-nav .nav-brand { display:flex;align-items:center;gap:10px; }
     .enmessara-site-nav .nav-brand span { font-size:15px;font-weight:700;color:#fff; }
     .enmessara-site-nav .nav-links { display:flex;gap:24px; }
     .enmessara-site-nav .nav-links a { color:#b0b8cc;font-size:13px;font-weight:500;transition:color 0.2s; }
     .enmessara-site-nav .nav-links a:hover { color:#fff; }
     .enmessara-site-nav .nav-links a.active { color:#00D4FF; }
     @media (max-width: 640px) { .enmessara-site-nav .nav-links { gap:12px; } .enmessara-site-nav .nav-links a { font-size:11px; } }
     @media (max-width: 480px) { .enmessara-site-nav .nav-links a:not(.active) { display:none; } }
   </style>
   <nav class="enmessara-site-nav">
     <div class="nav-inner">
       <a href="../index.html" class="nav-brand">
         <img src="../assets/logo.svg" alt="Enmessara" width="32" height="32">
         <span>Enmessara</span>
       </a>
       <div class="nav-links">
         <a href="../use-cases.html">Use Cases</a>
         <a href="../blog.html" class="active">Blog</a>
         <a href="../partnerships.html">Partnerships</a>
         <a href="../careers.html">Careers</a>
         <a href="../contact.html">Contact Us</a>
       </div>
     </div>
   </nav>
   ```

   Note: Links use `../` prefix because blog posts live in the `blog/` subdirectory.

5. **Generate PDF** using headless Chrome:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-sandbox \
     --print-to-pdf="[output].pdf" \
     --print-to-pdf-no-header --no-margins \
     --run-all-compositor-stages-before-draw \
     "file:///[path-to-html]"
   ```

---

### STEP 5 — One-Sheeter

Using the blog post content, create a **one-sheeter HTML asset** that:
- Conveys the same information in a visual-first format
- Adapts layout components per topic — choose from: stat strips, icon callouts, comparison grids, process flows, timeline strips, quote blocks, data cards
- Prioritizes scannability: bold headlines, short bullets, visual hierarchy
- Applies Enmessara Light Theme
- Generates PDF via headless Chrome (same command as Step 4)

Save both the HTML and PDF alongside the blog post files.

---

### STEP 6 — Preview & Approval

Present both outputs to the user:
- Open the blog post HTML in Chrome for visual preview
- Open the one-sheeter HTML in Chrome for visual preview
- Ask: "Both assets are ready for review. Approve to stage, or let me know what to revise."

Wait for explicit approval before proceeding.

---

### STEP 7 — Stage & Publish Decision

**After approval:**

1. **Stage the blog post** in the website repo:
   - Save the HTML file to: `/Users/userliberty/BuildSession_EnmessaraAIWebsite_Apr14/enmessara-website/_drafts/blog-[slug].html`
   - Commit with message: `Stage blog draft: [title]`
   - Push to GitHub

2. **Ask the user:** "Want me to publish this live right now, or keep it in drafts for later?"

3. **If publish now:**
   - Move file from `_drafts/blog-[slug].html` to `blog/[slug].html`
   - Add a blog card to `blog.html` at the TOP of the `.grid-3` container (most recent first)
   - Card format (match existing pattern):
     ```html
     <article class="blog-card">
         <div class="blog-card-image">
             <div style="width:100%;height:100%;background:linear-gradient(135deg,#00D4FF 0%,#A78BFA 100%);border-radius:var(--radius-lg);display:flex;align-items:center;justify-content:center;">
                 <span style="font-size:2.5rem;">[EMOJI]</span>
             </div>
         </div>
         <div class="blog-card-content">
             <div class="blog-meta">
                 <span>[Month DD, YYYY]</span>
                 <span class="blog-tag">[Category]</span>
             </div>
             <h3><a href="blog/[slug].html">[Title]</a></h3>
             <p class="text-muted">[1-2 sentence preview/meta description]</p>
         </div>
     </article>
     ```
   - If a custom thumbnail image exists, use `<img>` instead of the gradient div
   - Commit and push. Live URL will be: `enmessara.ai/blog/[slug].html`

4. **If keep as draft:** Leave in `_drafts/`, confirm it's pushed and accessible from other devices. Provide instructions:
   ```
   To publish later, run /enmessara-blog and tell me which draft to publish,
   or manually: mv _drafts/blog-[slug].html blog/[slug].html
   Then add a card to blog.html and push.
   ```

---

## File Locations

| Asset | Path |
|---|---|
| Skill directory | `/Users/userliberty/.claude/skills/enmessara-blog/` |
| Last scan tracker | `/Users/userliberty/.claude/skills/enmessara-blog/.last_scan` |
| Website repo | `/Users/userliberty/BuildSession_EnmessaraAIWebsite_Apr14/enmessara-website/` |
| Drafts folder | `[repo]/_drafts/` |
| Published blog posts | `[repo]/blog/` |
| Blog aggregate page | `[repo]/blog.html` |
| Blog PDFs | `/Users/userliberty/Desktop/AI Operations & Strategy Series - All Entries/Blog Posts/BLOG POSTS_FINALDRAFT/` |
| One-sheeter PDFs | `/Users/userliberty/Desktop/AI Operations & Strategy Series - All Entries/Full EBook Build/One-Sheeters w:o 1$ offer/` |
| Google Drive folder | "Enmessara Blog Drafts" (auto-created) |
| Master LinkedIn Doc | Google Doc ID: `110PGXMII0CGP3fUJK1p6EeY5SnRDmXURUQyJZ8_1U3U` |
| Logo SVG | `/Users/userliberty/BuildSession_EnmessaraAIWebsite_Apr14/enmessara-website/assets/logo.svg` |

## Tools Used

- **Gmail MCP**: `search_threads`, `get_thread` — email scanning
- **Google Drive MCP**: `create_file`, `read_file_content`, `search_files` — doc creation
- **WebSearch / WebFetch**: SEC EDGAR research, web enrichment
- **Bash**: Headless Chrome PDF generation, git operations, file management
- **Theme Light skill**: Brand application (invoked internally)

## Notes

- Always present findings before writing — never skip the user confirmation step
- Track affiliate/backlink opportunities explicitly in the Google Doc
- The LinkedIn post goes in chat AND gets appended to the master LinkedIn Google Doc (ID: `110PGXMII0CGP3fUJK1p6EeY5SnRDmXURUQyJZ8_1U3U`)
- One-sheeter layout is flexible per topic — don't force components that don't fit the content
- If the email scan returns nothing relevant, say so and offer to broaden the search window or try manual topic input
- **EVERY blog post HTML must include the site-wide navigation bar** (see Step 4.4) — do not generate blog HTML without it
- Text inside `[]` brackets in the Google Doc draft (e.g. `[AFFILIATE OPPORTUNITY: product_name]`) are internal notes — do NOT include them in the published HTML
- When publishing, also update the `[BLOG LINK]` placeholder in the master LinkedIn doc with the live URL
