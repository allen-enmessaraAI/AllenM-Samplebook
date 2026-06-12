# Enmessara AI — Light Theme

## Skill Purpose
Apply the Enmessara AI light theme branding to any document, one-pager, PDF report, or marketing asset currently being produced. When invoked, this skill activates the light visual identity and instructs all downstream output to conform to it.

## Trigger
`/theme-light`

## When to Use
- Print-friendly reports and one-pagers
- Client deliverables designed for reading in bright environments or printing
- Proposals and documents where white/light background is preferred
- Any document where the user wants the off-white + navy + cyan brand treatment
- Overrides any default color palette in PDF scripts or document templates

---

## Brand Identity — Light Theme

### Visual Language
The light theme carries the same Mesopotamian-inspired identity in an airy, professional register: near-white fields with subtle circuit-blueprint overlays, deep navy typography, and electric cyan geometric accents on the right margin. The overall feel is **enterprise-grade clarity** — clean, authoritative, easy to scan.

### Logo
- **Source SVG:** `/Users/userliberty/Proposal Builder Agent/assets/logo.svg`
- **Design:** 4-pointed diamond star inside a hexagonal badge frame. Gradient: `#00D4FF` → `#A78BFA` (cyan to violet, top-left to bottom-right)
- **Wordmark:** "Enmessara" in Inter Bold, deep navy `#071525`, placed to the right of the badge
- **On light backgrounds:** Use full-color gradient logo badge + dark navy wordmark
- **Badge background:** The hexagon frame renders in the gradient; no additional background needed

### Color Palette

| Token | Name | Hex | Usage |
|---|---|---|---|
| `primary` | Electric Cyan | `#00D4FF` | Accent lines, icon fills, geometric elements, key highlights |
| `primary_dark` | Cyan Dark | `#00A8CC` | Borders, hover states, underlines |
| `secondary` | Violet | `#A78BFA` | Supporting highlights, tags, badges |
| `accent` | Blush Pink | `#F472B6` | Rare accent — single emphasis item only |
| `background` | Cloud White | `#F0F2F8` | Page/document background |
| `surface` | White | `#FFFFFF` | Cards, section blocks, table rows |
| `surface_elevated` | Light Surface | `#E8ECF4` | Callout boxes, featured stat blocks |
| `border` | Periwinkle Border | `#C8D2E8` | Dividers, table grid lines, section rules |
| `text` | Deep Navy | `#071525` | All primary headings and body text |
| `text_muted` | Slate | `#6B7A99` | Secondary labels, captions, footnotes |
| `success` | Green | `#00C853` | Positive scores, checkmarks |
| `warning` | Amber | `#D97706` | Medium scores, flags (darker for light bg readability) |
| `danger` | Red | `#DC2626` | Low scores, critical findings (darker for light bg) |

### Score Color Logic (for report gauges)
- 80–100 → `#00C853` (green)
- 60–79 → `#00A8CC` (cyan dark — readable on white)
- 40–59 → `#D97706` (amber dark)
- 0–39 → `#DC2626` (red dark)

### Typography
- **Font family:** Inter (primary) → system-ui, -apple-system, sans-serif (fallbacks)
- **H1 / Cover title:** Inter Bold (700), `#071525`, 28–36pt
- **H2 / Section headers:** Inter SemiBold (600), `#00A8CC`, 18–22pt
- **H3 / Sub-headers:** Inter SemiBold (600), `#071525`, 14–16pt
- **Body:** Inter Regular (400), `#071525`, 10–11pt
- **Captions / Labels:** Inter Regular (400), `#6B7A99`, 8–9pt
- **Data callouts / Stats:** Inter Bold (700), `#071525`, 24–32pt (with `#00D4FF` accent underline)

### Pattern & Texture Guidance
- Background image reference: `/Users/userliberty/Downloads/EnmessaraSlideTheme-Light.png`
- Subtle circuit/blueprint pattern at 4–6% opacity in `#C8D2E8` — upper-left quadrant
- Right-margin geometric: cyan `#00D4FF` hexagonal bracket outline (decorative only)
- Cuneiform symbol overlays at very low opacity (3–5%) in `#C8D2E8` if decorative texture is needed

---

## How to Apply

### Step 1 — Declare the theme
At the start of any document or asset being generated, state:
> **Theme: Enmessara Light**
> All colors, typography, and visual elements follow the light theme spec above.

### Step 2 — PDF Report Scripts
When generating a PDF using any `generate_pdf_report.py` script, override the color constants at the top of the script with:

```python
# Enmessara Light Theme
PAGE_BG       = HexColor("#F0F2F8")   # page background
SURFACE       = HexColor("#FFFFFF")   # cards/tables
ACCENT        = HexColor("#00A8CC")   # headlines, accents (darker cyan for readability)
ACCENT_BRIGHT = HexColor("#00D4FF")   # geometric elements only
SECONDARY     = HexColor("#A78BFA")   # supporting highlights
TEXT_PRIMARY  = HexColor("#071525")   # body text
TEXT_MUTED    = HexColor("#6B7A99")   # captions
BORDER        = HexColor("#C8D2E8")   # dividers
HEADER_BG     = HexColor("#071525")   # table headers (dark navy inverted)
HEADER_TEXT   = HexColor("#FFFFFF")   # table header text
SUCCESS       = HexColor("#00C853")
WARNING       = HexColor("#D97706")
DANGER        = HexColor("#DC2626")
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
theme: light
primary: "#00D4FF"
secondary: "#A78BFA"
background: "#F0F2F8"
text: "#071525"
font: Inter
---
```

For HTML/CSS one-pagers, apply:
```css
:root {
  --color-bg: #F0F2F8;
  --color-surface: #FFFFFF;
  --color-primary: #00D4FF;
  --color-primary-dark: #00A8CC;
  --color-secondary: #A78BFA;
  --color-text: #071525;
  --color-text-muted: #6B7A99;
  --color-border: #C8D2E8;
  --font-sans: 'Inter', system-ui, sans-serif;
}
```

### Step 4 — Logo Placement in Documents
- Top-right header: logo SVG + "Enmessara" wordmark (deep navy `#071525`, Inter Bold)
- Footer: "enmessara.ai" in `#6B7A99`, small
- Cover page: Logo centered or top-right, large (48–64px badge)
- Table headers: dark navy `#071525` background with white text (inverted from page)

### Step 5 — Confirm activation
After loading this theme, respond:
> ✓ Light theme active — all outputs will use Enmessara light branding (cloud white `#F0F2F8`, cyan `#00D4FF`, navy `#071525`, Inter).

---

## Asset References
| Asset | Path |
|---|---|
| Logo SVG | `/Users/userliberty/BuildSession_EnmessaraAIWebsite_Apr14/enmessara-website/assets/logo.svg` |
| Light theme preview | `/Users/userliberty/Downloads/EnmessaraSlideTheme-Light.png` |
| Full deck theme (PPTX) | `/Users/userliberty/Downloads/Enmessara_Full_Deck_Theme.pptx` |
