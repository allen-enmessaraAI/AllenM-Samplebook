# Enmessara AI — Dark Theme

## Skill Purpose
Apply the Enmessara AI dark theme branding to any document, one-pager, PDF report, or marketing asset currently being produced. When invoked, this skill activates the dark visual identity and instructs all downstream output to conform to it.

## Trigger
`/theme-dark`

## When to Use
- Marketing assets, reports, or one-pagers destined for dark-background presentation
- Client-facing PDF deliverables with the dark slide theme aesthetic
- Any document where the user wants the dark navy + electric cyan brand treatment
- Overrides any default color palette in PDF scripts or document templates

---

## Brand Identity — Dark Theme

### Visual Language
The dark theme draws from Enmessara's Mesopotamian-inspired identity: deep navy fields, glowing electric cyan accents, constellation/circuit-trace patterns, and cuneiform symbol motifs. The overall feel is **enterprise precision meets ancient intelligence** — confident, technical, premium.

### Logo
- **Source SVG:** `/Users/userliberty/Proposal Builder Agent/assets/logo.svg`
- **Design:** 4-pointed diamond star inside a hexagonal badge frame. Gradient: `#00D4FF` → `#A78BFA` (cyan to violet, top-left to bottom-right)
- **Wordmark:** "Enmessara" in Inter Bold, white `#FFFFFF`, placed to the right of the badge
- **On dark backgrounds:** Use full-color logo (gradient star + white wordmark)
- **Badge background:** Dark navy `#0F2235` or transparent overlay

### Color Palette

| Token | Name | Hex | Usage |
|---|---|---|---|
| `primary` | Electric Cyan | `#00D4FF` | Headlines, CTAs, key stats, accent lines, icon fills |
| `primary_dark` | Cyan Dark | `#00A8CC` | Hover states, secondary accents, borders |
| `secondary` | Violet | `#A78BFA` | Supporting highlights, tags, secondary data points |
| `accent` | Blush Pink | `#F472B6` | Rare accent — use for single emphasis item only |
| `background` | Deep Navy | `#071525` | Page/slide background |
| `surface` | Navy Surface | `#0F2235` | Cards, section blocks, table rows |
| `surface_elevated` | Navy Elevated | `#162E47` | Modals, call-out boxes |
| `border` | Navy Border | `#1A3A5C` | Dividers, table grid lines, input outlines |
| `text` | White | `#FFFFFF` | All primary body text |
| `text_muted` | Slate | `#A3B8CC` | Secondary labels, captions, footnotes |
| `success` | Green | `#00C853` | Positive scores, checkmarks |
| `warning` | Amber | `#FFB300` | Medium scores, flags |
| `danger` | Red | `#FF4444` | Low scores, critical findings |

### Score Color Logic (for report gauges)
- 80–100 → `#00C853` (green)
- 60–79 → `#00D4FF` (cyan)
- 40–59 → `#FFB300` (amber)
- 0–39 → `#FF4444` (red)

### Typography
- **Font family:** Inter (primary) → system-ui, -apple-system, sans-serif (fallbacks)
- **H1 / Cover title:** Inter Bold (700), `#FFFFFF`, 28–36pt
- **H2 / Section headers:** Inter SemiBold (600), `#00D4FF`, 18–22pt
- **H3 / Sub-headers:** Inter SemiBold (600), `#FFFFFF`, 14–16pt
- **Body:** Inter Regular (400), `#FFFFFF`, 10–11pt
- **Captions / Labels:** Inter Regular (400), `#A3B8CC`, 8–9pt
- **Data callouts / Stats:** Inter Bold (700), `#00D4FF`, 24–32pt

### Pattern & Texture Guidance
- Background image reference: `/Users/userliberty/Downloads/EnmessaraSlideTheme-Dark1.png`
- Geometric motif: hexagonal outlines, circuit trace lines, constellation dot-connect patterns
- Cuneiform symbol overlays at low opacity (5–10%) in `#1A3A5C`
- Glowing cyan wave/particle effect along upper-left diagonal — use as hero section texture only

---

## How to Apply

### Step 1 — Declare the theme
At the start of any document or asset being generated, state:
> **Theme: Enmessara Dark**
> All colors, typography, and visual elements follow the dark theme spec above.

### Step 2 — PDF Report Scripts
When generating a PDF using any `generate_pdf_report.py` script, override the color constants at the top of the script with:

```python
# Enmessara Dark Theme
PRIMARY       = HexColor("#071525")   # background
SURFACE       = HexColor("#0F2235")   # cards/tables
ACCENT        = HexColor("#00D4FF")   # headlines, accents
SECONDARY     = HexColor("#A78BFA")   # supporting highlights
TEXT_PRIMARY  = HexColor("#FFFFFF")   # body text
TEXT_MUTED    = HexColor("#A3B8CC")   # captions
BORDER        = HexColor("#1A3A5C")   # dividers
SUCCESS       = HexColor("#00C853")
WARNING       = HexColor("#FFB300")
DANGER        = HexColor("#FF4444")
```

Add to the header/footer function:
```python
# Footer: "Prepared by Enmessara AI" on left, page number on right
canvas.drawString(50, 28, "Prepared by Enmessara AI  |  enmessara.ai")
```

### PDF Generation (HTML → PDF)
After generating and reviewing the HTML output in the browser, convert to PDF using headless Chrome — never via File → Print (adds unwanted margin text):

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="OUTPUT.pdf" \
  --print-to-pdf-no-header \
  --no-margins \
  --run-all-compositor-stages-before-draw \
  "file:///ABSOLUTE/PATH/TO/OUTPUT.html"
```

Workflow: HTML → open in browser for review → approve → headless Chrome → final PDF.

### Step 3 — Markdown / One-Pagers
For Markdown documents, open with a brand block:

```
---
brand: Enmessara AI
theme: dark
primary: "#00D4FF"
secondary: "#A78BFA"
background: "#071525"
font: Inter
---
```

For HTML/CSS one-pagers, apply:
```css
:root {
  --color-bg: #071525;
  --color-surface: #0F2235;
  --color-primary: #00D4FF;
  --color-secondary: #A78BFA;
  --color-text: #FFFFFF;
  --color-text-muted: #A3B8CC;
  --color-border: #1A3A5C;
  --font-sans: 'Inter', system-ui, sans-serif;
}
```

### Step 4 — Logo Placement in Documents
- Top-right header: logo SVG + "Enmessara" wordmark (white, Inter Bold)
- Footer: "enmessara.ai" in `#A3B8CC`, small
- Cover page: Logo centered or top-right, large (48–64px badge)

### Step 5 — Confirm activation
After loading this theme, respond:
> ✓ Dark theme active — all outputs will use Enmessara dark branding (navy `#071525`, cyan `#00D4FF`, Inter).

---

## Asset References
| Asset | Path |
|---|---|
| Logo SVG | `/Users/userliberty/BuildSession_EnmessaraAIWebsite_Apr14/enmessara-website/assets/logo.svg` |
| Dark theme preview | `/Users/userliberty/Downloads/EnmessaraSlideTheme-Dark1.png` |
| Full deck theme (PPTX) | `/Users/userliberty/Downloads/Enmessara_Full_Deck_Theme.pptx` |
