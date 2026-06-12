#!/usr/bin/env python3
"""
AI Reputation Manager — PDF Report Generator
Generates professional client-facing reputation reports using ReportLab.
"""

import sys
import os
import re
import math
import argparse
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, HRFlowable, KeepTogether
    )
    from reportlab.graphics.shapes import Drawing, Circle, Wedge, String, Line, Rect
    from reportlab.graphics import renderPDF
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
except ImportError:
    print("ERROR: reportlab is required. Install with: pip3 install reportlab")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Color Palette
# ---------------------------------------------------------------------------
C = {
    "navy":       HexColor("#1a365d"),
    "blue":       HexColor("#2b6cb0"),
    "green":      HexColor("#276749"),
    "emerald":    HexColor("#38a169"),
    "amber":      HexColor("#d69e2e"),
    "orange":     HexColor("#c05621"),
    "red":        HexColor("#c53030"),
    "light_bg":   HexColor("#f7fafc"),
    "dark_text":  HexColor("#1a202c"),
    "gray":       HexColor("#718096"),
    "border":     HexColor("#e2e8f0"),
    "white":      white,
    "black":      black,
}


def grade_color(score):
    if score >= 85: return C["emerald"]
    if score >= 70: return C["emerald"]
    if score >= 55: return C["amber"]
    if score >= 40: return C["orange"]
    return C["red"]


def grade_label(score):
    if score >= 85: return ("A", "Excellent")
    if score >= 70: return ("B", "Good")
    if score >= 55: return ("C", "Average")
    if score >= 40: return ("D", "Below Average")
    return ("F", "Poor — Urgent")


# ---------------------------------------------------------------------------
# Score Gauge
# ---------------------------------------------------------------------------
def score_gauge(score, width=220):
    h = width * 0.6
    d = Drawing(width, h)
    cx, cy = width / 2, h * 0.85
    r = width * 0.38

    segments = [
        (0,   36,  C["red"]),
        (36,  72,  C["orange"]),
        (72,  108, C["amber"]),
        (108, 144, C["emerald"]),
        (144, 180, C["green"]),
    ]
    for start, end, color in segments:
        d.add(Wedge(cx, cy, r, 180 + start, 180 + end,
                    fillColor=color, strokeColor=white, strokeWidth=2))

    d.add(Circle(cx, cy, r * 0.62, fillColor=white, strokeColor=None))

    # Needle
    angle = math.radians(180 + (score / 100) * 180)
    nx = cx + r * 0.52 * math.cos(angle)
    ny = cy + r * 0.52 * math.sin(angle)
    d.add(Line(cx, cy, nx, ny, strokeColor=C["navy"], strokeWidth=2.5))
    d.add(Circle(cx, cy, 5, fillColor=C["navy"], strokeColor=None))

    d.add(String(cx, cy - 8, str(int(score)),
                 fontSize=34, fillColor=C["navy"],
                 textAnchor="middle", fontName="Helvetica-Bold"))
    d.add(String(cx, cy - 22, "/ 100",
                 fontSize=11, fillColor=C["gray"],
                 textAnchor="middle", fontName="Helvetica"))
    return d


# ---------------------------------------------------------------------------
# Score Bar
# ---------------------------------------------------------------------------
def score_bar(score, width=200, height=14):
    d = Drawing(width, height)
    bg_w = width * 0.85
    fill_w = bg_w * (score / 100)
    d.add(Rect(0, 2, bg_w, height - 4, fillColor=C["border"], strokeColor=None, rx=3, ry=3))
    d.add(Rect(0, 2, fill_w, height - 4, fillColor=grade_color(score), strokeColor=None, rx=3, ry=3))
    return d


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
def get_styles():
    s = getSampleStyleSheet()
    add = s.add
    add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=26,
                       textColor=C["navy"], alignment=TA_CENTER, spaceAfter=8))
    add(ParagraphStyle("CoverSub", fontName="Helvetica", fontSize=13,
                       textColor=C["gray"], alignment=TA_CENTER, spaceAfter=6))
    add(ParagraphStyle("SectionHead", fontName="Helvetica-Bold", fontSize=15,
                       textColor=C["navy"], spaceBefore=18, spaceAfter=8))
    add(ParagraphStyle("SubHead", fontName="Helvetica-Bold", fontSize=11,
                       textColor=C["blue"], spaceBefore=10, spaceAfter=4))
    add(ParagraphStyle("Body", fontName="Helvetica", fontSize=10,
                       textColor=C["dark_text"], spaceBefore=3, spaceAfter=3, leading=14))
    add(ParagraphStyle("Disclaimer", fontName="Helvetica-Oblique", fontSize=8,
                       textColor=C["gray"], alignment=TA_CENTER, spaceBefore=8))
    add(ParagraphStyle("Footer", fontName="Helvetica", fontSize=8,
                       textColor=C["gray"], alignment=TA_CENTER))
    add(ParagraphStyle("Quote", fontName="Helvetica-Oblique", fontSize=9,
                       textColor=C["gray"], leftIndent=16, spaceBefore=4, spaceAfter=4, leading=13))
    return s


# ---------------------------------------------------------------------------
# Parse Markdown Input
# ---------------------------------------------------------------------------
def parse_audit_file(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        text = f.read()

    data = {"raw": text}

    # Business name
    m = re.search(r"#\s*Reputation Audit:\s*(.+)", text)
    data["business"] = m.group(1).strip() if m else "Business"

    # Score
    m = re.search(r"Reputation Score[:\s]+(\d+)", text)
    data["score"] = int(m.group(1)) if m else 0

    # Location
    m = re.search(r"\*\*Location:\*\*\s*([^\n|*]+)", text)
    data["location"] = m.group(1).strip() if m else ""

    # Category
    m = re.search(r"Business Type[:\s]+([^\n|*]+)", text)
    data["category"] = m.group(1).strip() if m else ""

    # Executive summary
    m = re.search(r"## Executive Summary\s*\n([\s\S]+?)(?=\n##)", text)
    data["summary"] = m.group(1).strip() if m else ""

    # Sub-scores: look for table rows with /100
    scores = re.findall(r"\|\s*([^|]+?)\s*\|\s*(\d+)/100\s*\|\s*(\d+)%", text)
    data["sub_scores"] = [(s[0].strip(), int(s[1]), int(s[2])) for s in scores]

    # Quick wins
    wins = re.findall(r"\d+\.\s*\[?\s*([^\[\]\n]{10,})", text)
    data["quick_wins"] = wins[:5] if wins else []

    # Services section
    m = re.search(r"## Recommended Services([\s\S]+?)(?=\n##|$)", text)
    data["services_raw"] = m.group(1).strip() if m else ""

    # Crisis level
    m = re.search(r"Crisis Level[:\s]+([A-Za-z]+)", text)
    data["crisis"] = m.group(1) if m else "Unknown"

    # Competitive rank
    m = re.search(r"#(\d+)\s*of\s*(\d+)", text)
    data["comp_rank"] = f"#{m.group(1)} of {m.group(2)}" if m else "N/A"

    return data


# ---------------------------------------------------------------------------
# PDF Builder
# ---------------------------------------------------------------------------
def build_pdf(data, output_path):
    styles = get_styles()
    doc = SimpleDocTemplate(
        output_path, pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch
    )
    story = []
    score = data.get("score", 0)
    grade, label = grade_label(score)
    gcolor = grade_color(score)
    business = data.get("business", "Business")
    location = data.get("location", "")
    today = datetime.now().strftime("%B %d, %Y")

    # ── Cover ──────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.6 * inch))
    story.append(Paragraph("REPUTATION ANALYSIS REPORT", styles["CoverTitle"]))
    story.append(Paragraph(business, styles["CoverSub"]))
    if location:
        story.append(Paragraph(location, styles["CoverSub"]))
    story.append(Spacer(1, 0.4 * inch))

    gauge = score_gauge(score)
    story.append(gauge)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph(
        f'<font color="{gcolor.hexval()}"><b>Reputation Score: {score}/100 — Grade {grade} ({label})</b></font>',
        styles["CoverSub"]
    ))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(f"Prepared: {today}", styles["CoverSub"]))
    story.append(Paragraph("Powered by AI Reputation Manager", styles["CoverSub"]))
    story.append(PageBreak())

    # ── Executive Summary ──────────────────────────────────────────────────
    story.append(Paragraph("Executive Summary", styles["SectionHead"]))
    story.append(HRFlowable(width="100%", thickness=1, color=C["border"]))

    # Snapshot table
    snap_data = [
        ["Business", business],
        ["Location", location or "—"],
        ["Category", data.get("category", "—")],
        ["Reputation Score", f"{score}/100 — Grade {grade} ({label})"],
        ["Competitive Rank", data.get("comp_rank", "—")],
        ["Crisis Level", data.get("crisis", "—")],
    ]
    snap_table = Table(snap_data, colWidths=[1.8 * inch, 4.7 * inch])
    snap_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TEXTCOLOR", (0, 0), (0, -1), C["navy"]),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, C["border"]),
    ]))
    story.append(snap_table)
    story.append(Spacer(1, 14))

    summary = data.get("summary", "")
    if summary:
        for para in summary.split("\n\n"):
            para = para.strip()
            if para:
                story.append(Paragraph(para, styles["Body"]))
    story.append(PageBreak())

    # ── Score Dashboard ────────────────────────────────────────────────────
    story.append(Paragraph("Reputation Score Dashboard", styles["SectionHead"]))
    story.append(HRFlowable(width="100%", thickness=1, color=C["border"]))
    story.append(Spacer(1, 6))

    sub_scores = data.get("sub_scores", [])
    if sub_scores:
        score_rows = [["Dimension", "Score", "Weight", "Visual"]]
        for name, sc, wt in sub_scores:
            bar = score_bar(sc, width=160, height=12)
            score_rows.append([name, f"{sc}/100", f"{wt}%", bar])
        score_rows.append(["TOTAL REPUTATION SCORE", f"{score}/100", "100%", score_bar(score, 160, 12)])

        sc_table = Table(score_rows, colWidths=[2.4 * inch, 0.9 * inch, 0.7 * inch, 2.5 * inch])
        sc_table.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("BACKGROUND", (0, 0), (-1, 0), C["navy"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), C["white"]),
            ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
            ("BACKGROUND", (0, -1), (-1, -1), C["light_bg"]),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, C["border"]),
        ]))
        story.append(sc_table)
    else:
        # Fallback: just show the total score
        story.append(Paragraph(f"Overall Reputation Score: {score}/100 — {grade} ({label})", styles["Body"]))

    story.append(PageBreak())

    # ── Quick Wins ─────────────────────────────────────────────────────────
    quick_wins = data.get("quick_wins", [])
    if quick_wins:
        story.append(Paragraph("Quick Wins — Next 30 Days", styles["SectionHead"]))
        story.append(HRFlowable(width="100%", thickness=1, color=C["border"]))
        for i, win in enumerate(quick_wins, 1):
            story.append(Paragraph(f"<b>{i}.</b> {win}", styles["Body"]))
        story.append(Spacer(1, 14))

    # ── Recommended Services ───────────────────────────────────────────────
    services_raw = data.get("services_raw", "")
    if services_raw:
        story.append(Paragraph("Recommended Services", styles["SectionHead"]))
        story.append(HRFlowable(width="100%", thickness=1, color=C["border"]))
        for line in services_raw.split("\n"):
            line = line.strip()
            if line and not line.startswith("|---"):
                line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
                story.append(Paragraph(line, styles["Body"]))
        story.append(Spacer(1, 14))

    # ── Full Raw Report ────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("Full Analysis", styles["SectionHead"]))
    story.append(HRFlowable(width="100%", thickness=1, color=C["border"]))

    raw = data.get("raw", "")
    current_section = []
    for line in raw.split("\n"):
        line_s = line.strip()
        if not line_s:
            if current_section:
                story.append(Paragraph(" ".join(current_section), styles["Body"]))
                current_section = []
            story.append(Spacer(1, 4))
        elif line_s.startswith("## "):
            if current_section:
                story.append(Paragraph(" ".join(current_section), styles["Body"]))
                current_section = []
            story.append(Paragraph(line_s[3:], styles["SectionHead"]))
            story.append(HRFlowable(width="100%", thickness=0.5, color=C["border"]))
        elif line_s.startswith("### "):
            if current_section:
                story.append(Paragraph(" ".join(current_section), styles["Body"]))
                current_section = []
            story.append(Paragraph(line_s[4:], styles["SubHead"]))
        elif line_s.startswith(">"):
            story.append(Paragraph(line_s[1:].strip(), styles["Quote"]))
        elif line_s.startswith("|"):
            # Skip table lines in raw — already handled in structured sections
            pass
        elif line_s.startswith("*Generated"):
            pass
        else:
            cleaned = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line_s)
            current_section.append(cleaned)

    if current_section:
        story.append(Paragraph(" ".join(current_section), styles["Body"]))

    # ── Disclaimer ─────────────────────────────────────────────────────────
    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C["border"]))
    story.append(Paragraph(
        f"Generated by AI Reputation Manager on {today}. "
        "This report is based on publicly available information and AI analysis. "
        "Results should be verified before making business decisions.",
        styles["Disclaimer"]
    ))

    # ── Page numbers via canvas ────────────────────────────────────────────
    page_count = [0]

    def add_footer(canvas, doc):
        page_count[0] += 1
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(C["gray"])
        w, h = letter
        canvas.drawString(0.75 * inch, 0.5 * inch, f"{business} — Reputation Analysis Report")
        canvas.drawCentredString(w / 2, 0.5 * inch, "CONFIDENTIAL")
        canvas.drawRightString(w - 0.75 * inch, 0.5 * inch, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    return output_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate AI Reputation Manager PDF report")
    parser.add_argument("--input", default="REPUTATION-AUDIT.md", help="Input markdown file")
    parser.add_argument("--output", default="REPUTATION-REPORT.pdf", help="Output PDF path")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        # Try to find any audit file
        for candidate in ["REPUTATION-AUDIT.md", "REVIEWS-ANALYSIS.md", "SENTIMENT-ANALYSIS.md"]:
            if os.path.exists(candidate):
                args.input = candidate
                break
        else:
            print(f"ERROR: Could not find {args.input}. Run /reputation-audit first.")
            sys.exit(1)

    print(f"Reading: {args.input}")
    data = parse_audit_file(args.input)
    print(f"Business: {data.get('business', 'Unknown')}")
    print(f"Score: {data.get('score', 0)}/100")

    result = build_pdf(data, args.output)
    print(f"\nPDF generated: {os.path.abspath(result)}")


if __name__ == "__main__":
    main()
