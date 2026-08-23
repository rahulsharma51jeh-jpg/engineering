"""
kit.py — Layout / typography toolkit for the BEU Transportation Engineering notes PDF.
Provides styles, headings, formula boxes, worked-example boxes, tables, figures,
PYQ tags and reference tags, plus a BaseDocTemplate with running header/footer,
PDF bookmarks and an auto Table of Contents.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame,
                                Image, KeepTogether, ListFlowable, ListItem,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

import matplotlib

# --------------------------------------------------------------------------- #
# Fonts
# --------------------------------------------------------------------------- #
FDIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")


def _reg():
    pairs = [
        ("DJSerif", "DejaVuSerif.ttf"),
        ("DJSerif-Bold", "DejaVuSerif-Bold.ttf"),
        ("DJSerif-It", "DejaVuSerif-Italic.ttf"),
        ("DJSerif-BoldIt", "DejaVuSerif-BoldItalic.ttf"),
        ("DJSans", "DejaVuSans.ttf"),
        ("DJSans-Bold", "DejaVuSans-Bold.ttf"),
        ("DJSans-It", "DejaVuSans-Oblique.ttf"),
        ("DJSans-BoldIt", "DejaVuSans-BoldOblique.ttf"),
        ("DJMono", "DejaVuSansMono.ttf"),
        ("DJMono-Bold", "DejaVuSansMono-Bold.ttf"),
    ]
    for name, fn in pairs:
        pdfmetrics.registerFont(TTFont(name, os.path.join(FDIR, fn)))
    pdfmetrics.registerFontFamily(
        "DJSerif", normal="DJSerif", bold="DJSerif-Bold",
        italic="DJSerif-It", boldItalic="DJSerif-BoldIt")
    pdfmetrics.registerFontFamily(
        "DJSans", normal="DJSans", bold="DJSans-Bold",
        italic="DJSans-It", boldItalic="DJSans-BoldIt")
    pdfmetrics.registerFontFamily(
        "DJMono", normal="DJMono", bold="DJMono-Bold",
        italic="DJMono", boldItalic="DJMono-Bold")


_reg()

# --------------------------------------------------------------------------- #
# Palette
# --------------------------------------------------------------------------- #
NAVY = colors.HexColor("#12335C")
BLUE = colors.HexColor("#1B5E9E")
LBLUE = colors.HexColor("#E8F0F9")
TEAL = colors.HexColor("#0F6E63")
LTEAL = colors.HexColor("#E4F2F0")
RUST = colors.HexColor("#A8420E")
LRUST = colors.HexColor("#FBEDE5")
GOLD = colors.HexColor("#8A6A0B")
LGOLD = colors.HexColor("#FCF5DF")
GREY = colors.HexColor("#5A5A5A")
LGREY = colors.HexColor("#F2F2F2")
MGREY = colors.HexColor("#BFBFBF")
PLUM = colors.HexColor("#5B2A6B")
LPLUM = colors.HexColor("#F2E9F5")

# --------------------------------------------------------------------------- #
# Page geometry
# --------------------------------------------------------------------------- #
PW, PH = A4
LM = RM = 15 * mm
TM = 17 * mm
BM = 14 * mm
FW = PW - LM - RM            # frame width  ~ 510 pt
FH = PH - TM - BM - 10 * mm  # frame height

# --------------------------------------------------------------------------- #
# Styles
# --------------------------------------------------------------------------- #
_ss = getSampleStyleSheet()

ST = {}


def _s(name, **kw):
    ST[name] = ParagraphStyle(name, **kw)
    return ST[name]


BODY = _s("body", fontName="DJSerif", fontSize=9.1, leading=13.0,
          alignment=TA_JUSTIFY, textColor=colors.black,
          spaceBefore=0, spaceAfter=4.5)

BODYC = _s("bodyc", parent=BODY, alignment=TA_CENTER, spaceAfter=3)

SMALL = _s("small", fontName="DJSerif", fontSize=8.1, leading=11.4,
           alignment=TA_JUSTIFY, spaceAfter=3.5)

TINY = _s("tiny", fontName="DJSans", fontSize=7.1, leading=9.6,
          alignment=TA_LEFT, textColor=GREY)

H1S = _s("H1", fontName="DJSans-Bold", fontSize=15.5, leading=19,
         textColor=colors.white, spaceBefore=0, spaceAfter=0)

H1SUB = _s("H1sub", fontName="DJSans", fontSize=8.6, leading=11,
           textColor=colors.HexColor("#C9DCEF"))

H2S = _s("H2", fontName="DJSans-Bold", fontSize=11.6, leading=14.5,
         textColor=NAVY, spaceBefore=11, spaceAfter=4)

H3S = _s("H3", fontName="DJSans-Bold", fontSize=9.9, leading=12.6,
         textColor=BLUE, spaceBefore=7.5, spaceAfter=3)

H4S = _s("H4", fontName="DJSans-BoldIt", fontSize=9.2, leading=11.8,
         textColor=TEAL, spaceBefore=5.5, spaceAfter=2)

BULS = _s("bul", parent=BODY, leftIndent=13, bulletIndent=3,
          spaceAfter=2.4, alignment=TA_JUSTIFY,
          bulletFontName="DJSans", bulletFontSize=7.4)

BULS2 = _s("bul2", parent=BODY, fontSize=8.7, leading=12.0, leftIndent=26,
           bulletIndent=15, spaceAfter=1.8,
           bulletFontName="DJSans", bulletFontSize=7.0)

MATH = _s("math", fontName="DJSans", fontSize=9.9, leading=15.5,
          alignment=TA_CENTER, textColor=colors.HexColor("#0B2A4A"),
          spaceAfter=2, spaceBefore=2)

MATHL = _s("mathl", parent=MATH, alignment=TA_LEFT)

FLAB = _s("flab", fontName="DJSans-Bold", fontSize=7.6, leading=9.6,
          textColor=RUST, alignment=TA_LEFT, spaceAfter=1.5)

EXH = _s("exh", fontName="DJSans-Bold", fontSize=9.2, leading=12,
         textColor=RUST, spaceAfter=3)

EXB = _s("exb", fontName="DJSerif", fontSize=8.7, leading=12.4,
         alignment=TA_JUSTIFY, spaceAfter=3)

EXM = _s("exm", fontName="DJSans", fontSize=8.9, leading=13.2,
         alignment=TA_LEFT, leftIndent=8, spaceAfter=2.2,
         textColor=colors.HexColor("#12335C"))

TH = _s("th", fontName="DJSans-Bold", fontSize=8.0, leading=10.4,
        textColor=colors.white, alignment=TA_CENTER)

TC = _s("tc", fontName="DJSerif", fontSize=7.9, leading=10.6,
        alignment=TA_LEFT)

TCC = _s("tcc", parent=TC, alignment=TA_CENTER)

TCB = _s("tcb", fontName="DJSans-Bold", fontSize=7.9, leading=10.6,
         alignment=TA_LEFT, textColor=NAVY)

CAP = _s("cap", fontName="DJSans-It", fontSize=7.9, leading=10.4,
         alignment=TA_CENTER, textColor=GREY, spaceBefore=2.5, spaceAfter=7)

REFS = _s("refs", fontName="DJSans-It", fontSize=7.4, leading=9.6,
          alignment=TA_LEFT, textColor=TEAL, spaceBefore=1, spaceAfter=6)

PYQS = _s("pyqs", fontName="DJSans", fontSize=8.1, leading=11.4,
          alignment=TA_LEFT, textColor=colors.HexColor("#4A2A00"))

PYQH = _s("pyqh", fontName="DJSans-Bold", fontSize=7.8, leading=10,
          textColor=colors.HexColor("#8A4B00"), spaceAfter=2)

TOCTITLE = _s("toct", fontName="DJSans-Bold", fontSize=17, leading=21,
              textColor=NAVY, spaceAfter=10)

TITLE = _s("title", fontName="DJSans-Bold", fontSize=27, leading=32,
           alignment=TA_CENTER, textColor=NAVY)

SUBTITLE = _s("subtitle", fontName="DJSans", fontSize=12.5, leading=17,
              alignment=TA_CENTER, textColor=BLUE)

QS = _s("qs", parent=BODY, fontSize=8.8, leading=12.2, leftIndent=17,
        bulletIndent=2, spaceAfter=3, bulletFontName="DJSans")


# --------------------------------------------------------------------------- #
# Text sanitiser: escape bare ampersands, keep intended markup
# --------------------------------------------------------------------------- #
_AMP = re.compile(r"&(?![A-Za-z][A-Za-z0-9]*;|#\d+;|#x[0-9A-Fa-f]+;)")


def esc(t):
    return _AMP.sub("&amp;", str(t))


# --------------------------------------------------------------------------- #
# Section registry (populated as flowables are laid out) -> header text
# --------------------------------------------------------------------------- #
STATE = {"unit": "", "seq": 0}


class _Mark(Flowable):
    """Zero-height marker that records outline/TOC/header info at layout time."""

    def __init__(self, level, text, key, header=None):
        Flowable.__init__(self)
        self.level = level
        self.text = text
        self.key = key
        self.header = header
        self.width = 0
        self.height = 0

    def wrap(self, *a):
        return (0, 0)

    def draw(self):
        pass

    def drawOn(self, canv, x, y, _sW=0):
        canv.bookmarkPage(self.key)
        canv.addOutlineEntry(self.text, self.key, level=self.level, closed=(self.level == 0))
        if self.header is not None:
            canv.__dict__["_kit_hdr"] = self.header
        self.canv = canv
        # notify TOC
        try:
            self._doctemplateAttr = None
        except Exception:
            pass


def _key(prefix):
    STATE["seq"] += 1
    return "%s%d" % (prefix, STATE["seq"])


# --------------------------------------------------------------------------- #
# Headings
# --------------------------------------------------------------------------- #
def H1(number, title, hours=None, header=None):
    """Unit banner. Starts a new page."""
    sub = ""
    if hours:
        sub = ("Syllabus allotment: %s" % hours) if str(number).isdigit() else str(hours)
    numbered = str(number).isdigit()
    banner = ("UNIT %s &nbsp;&nbsp;|&nbsp;&nbsp; %s" % (number, title)) if numbered else title
    inner = [Paragraph(esc(banner), H1S)]
    if sub:
        inner.append(Paragraph(esc(sub), H1SUB))
    t = Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LINEBELOW", (0, 0), (-1, -1), 3, GOLD),
    ]))
    label = ("Unit %s \u2014 %s" % (number, title)) if numbered else title
    hdr = header or label
    k = _key("u")
    return [PageBreak(), _TOCMark(0, label, k, hdr), t, Spacer(1, 9)]


def H2(title, toc=True):
    k = _key("h2")
    out = [_TOCMark(1, title, k) if toc else Spacer(0, 0)]
    bar = Table([[Paragraph(esc(title), H2S)]], colWidths=[FW], style=TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.9, colors.HexColor("#9DBBD8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    out += [CondPageBreak(46), bar, Spacer(1, 3.5)]
    return out


def H3(title, toc=False):
    out = []
    if toc:
        out.append(_TOCMark(2, title, _key("h3")))
    out += [CondPageBreak(34), Paragraph(esc(title), H3S)]
    return out


def H4(title):
    return [Paragraph(esc(title), H4S)]


# --------------------------------------------------------------------------- #
# Body text
# --------------------------------------------------------------------------- #
def P(text, style=None):
    return [Paragraph(esc(text), style or BODY)]


def SP(text):
    return [Paragraph(esc(text), SMALL)]


def BUL(items, sub=False):
    st = BULS2 if sub else BULS
    bt = "\u2013" if sub else "\u25aa"
    return [Paragraph(esc(t), st, bulletText=bt) for t in items]


def NUMLIST(items, start=1, style=None):
    st = style or BULS
    return [Paragraph(esc(t), st, bulletText="%d." % (start + i))
            for i, t in enumerate(items)]


def GAP(h=6):
    return [Spacer(1, h)]


def DEF(term, text):
    return [Paragraph("<b>%s</b> &nbsp;&mdash;&nbsp; %s" % (esc(term), esc(text)), BODY)]


# --------------------------------------------------------------------------- #
# Formula box
# --------------------------------------------------------------------------- #
def FORMULA(lines, label=None, where=None, color="blue"):
    """lines: list of formula strings (centred). where: list of 'symbol = meaning'."""
    pal = {"blue": (LBLUE, BLUE), "teal": (LTEAL, TEAL),
           "gold": (LGOLD, GOLD), "rust": (LRUST, RUST),
           "plum": (LPLUM, PLUM)}[color]
    inner = []
    if label:
        inner.append(Paragraph(esc(label.upper()), ParagraphStyle(
            "fl", parent=FLAB, textColor=pal[1])))
    for ln in lines:
        inner.append(Paragraph(esc(ln), MATH))
    if where:
        inner.append(Spacer(1, 2))
        for w in where:
            inner.append(Paragraph(esc(w), ParagraphStyle(
                "wh", fontName="DJSerif", fontSize=7.8, leading=10.4,
                textColor=colors.HexColor("#333333"), leftIndent=6,
                bulletIndent=0, spaceAfter=0.8,
                bulletFontName="DJSans"), bulletText="\u00b7"))
    t = Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), pal[0]),
        ("LINEBEFORE", (0, 0), (-1, -1), 2.6, pal[1]),
        ("BOX", (0, 0), (-1, -1), 0.4, pal[1]),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [Spacer(1, 2.5), t, Spacer(1, 6)]


def MEQ(lines, indent=8):
    """Left-aligned free-standing maths lines (used inside solutions)."""
    st = ParagraphStyle("meq", parent=EXM, leftIndent=indent)
    return [Paragraph(esc(x), st) for x in lines]


# --------------------------------------------------------------------------- #
# Worked example box
# --------------------------------------------------------------------------- #
def EX(title, problem, solution, keep=True, tag="SOLVED NUMERICAL"):
    """problem: str.  solution: list of strings; strings starting with '$' are maths."""
    inner = [Paragraph("%s &nbsp;&mdash;&nbsp; %s" % (esc(tag), esc(title)), EXH),
             Paragraph("<b>Q.</b> " + esc(problem), EXB),
             Paragraph("<b>Solution:</b>", ParagraphStyle(
                 "sol", parent=EXB, spaceAfter=1.5))]
    for s in solution:
        if s.startswith("$"):
            inner.append(Paragraph(esc(s[1:]), EXM))
        elif s.startswith("#"):
            inner.append(Paragraph("<b>%s</b>" % esc(s[1:]), ParagraphStyle(
                "solh", parent=EXB, textColor=RUST, spaceBefore=2.5, spaceAfter=1.5)))
        elif s.startswith("!"):
            inner.append(Table([[Paragraph("<b>%s</b>" % esc(s[1:]), ParagraphStyle(
                "ans", fontName="DJSans-Bold", fontSize=8.9, leading=12,
                textColor=colors.HexColor("#7A2E00")))]], colWidths=[FW - 46],
                style=TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6DFCE")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("BOX", (0, 0), (-1, -1), 0.4, RUST)])))
        else:
            inner.append(Paragraph(esc(s), EXB))
    t = Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FDF6F1")),
        ("LINEBEFORE", (0, 0), (-1, -1), 2.6, RUST),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#D9A98D")),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    blk = [Spacer(1, 3), t, Spacer(1, 7)]
    return [KeepTogether(blk)] if keep else blk


# --------------------------------------------------------------------------- #
# Callout boxes
# --------------------------------------------------------------------------- #
def _callout(head, text, bg, fg, style=None):
    inner = []
    if head:
        inner.append(Paragraph(esc(head.upper()), ParagraphStyle(
            "coh", fontName="DJSans-Bold", fontSize=7.6, leading=9.8,
            textColor=fg, spaceAfter=2)))
    body = style or ParagraphStyle("cob", fontName="DJSerif", fontSize=8.4,
                                   leading=11.8, alignment=TA_JUSTIFY,
                                   bulletFontName="DJSans", bulletFontSize=7.2)
    if isinstance(text, str):
        inner.append(Paragraph(esc(text), body))
    else:
        for i, x in enumerate(text):
            inner.append(Paragraph(esc(x), body, bulletText="\u25aa"))
            body = ParagraphStyle("cob%d" % i, parent=body, leftIndent=12,
                                  bulletIndent=2, spaceAfter=2,
                                  bulletFontName="DJSans", bulletFontSize=7.2)
    t = Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (-1, -1), 2.6, fg),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 6)]


def NOTE(text, head="Note"):
    return _callout(head, text, LGREY, GREY)


def TIP(text, head="Exam tip"):
    return _callout(head, text, LTEAL, TEAL)


def IRCBOX(text, head="IRC standard values"):
    return _callout(head, text, LGOLD, GOLD)


def DERIV(text, head="Derivation asked in exam"):
    return _callout(head, text, LPLUM, PLUM)


# --------------------------------------------------------------------------- #
# PYQ tag
# --------------------------------------------------------------------------- #
def PYQ(items, head="BEU / AKU repeat question"):
    if isinstance(items, str):
        items = [items]
    inner = [Paragraph(esc(head.upper()), PYQH)]
    for x in items:
        inner.append(Paragraph(esc(x), ParagraphStyle(
            "pq", parent=PYQS, leftIndent=11, bulletIndent=1, spaceAfter=1.8,
            bulletFontName="DJSans", bulletFontSize=7.6),
            bulletText="\u25b8"))
    t = Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF6E0")),
        ("LINEBEFORE", (0, 0), (-1, -1), 2.6, colors.HexColor("#C9880B")),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#E0BE7A")),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 6)]


class _SetHdr(Flowable):
    """Sets the running-header text at LAYOUT time (works across multiBuild passes)."""

    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text
        self.width = self.height = 0

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        HDR["cur"] = self.text


def SETHDR(text):
    return [_SetHdr(text)]


def REF(text):
    return [Paragraph("\u25b8 Reference: " + esc(text), REFS)]


# --------------------------------------------------------------------------- #
# Tables
# --------------------------------------------------------------------------- #
def TBL(rows, widths=None, header=True, align=None, fs=7.9, hdr_bg=None,
        zebra=True, first_bold=False, caption=None, total_width=None):
    """rows: list of lists of raw strings. align: list of 'l'/'c' per column."""
    tw = total_width or FW
    ncol = max(len(r) for r in rows)
    if widths is None:
        widths = [tw / float(ncol)] * ncol
    else:
        s = float(sum(widths))
        widths = [w / s * tw for w in widths]
    align = align or (["l"] + ["c"] * (ncol - 1))
    cs = ParagraphStyle("cs", parent=TC, fontSize=fs, leading=fs * 1.35)
    csc = ParagraphStyle("csc", parent=cs, alignment=TA_CENTER)
    csb = ParagraphStyle("csb", parent=TCB, fontSize=fs, leading=fs * 1.35)
    data = []
    for i, r in enumerate(rows):
        row = []
        for j, c in enumerate(r):
            if i == 0 and header:
                row.append(Paragraph(esc(c), ParagraphStyle(
                    "thx", parent=TH, fontSize=fs, leading=fs * 1.35)))
            else:
                st = csb if (first_bold and j == 0) else (
                    csc if align[min(j, len(align) - 1)] == "c" else cs)
                row.append(Paragraph(esc(c), st))
        data.append(row)
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.35, MGREY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), hdr_bg or NAVY),
                 ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i - (1 if header else 0)) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F7F9FB")))
    t = Table(data, colWidths=widths, style=TableStyle(cmds),
              repeatRows=1 if header else 0, hAlign="CENTER")
    out = [Spacer(1, 3), t]
    if caption:
        out.append(Paragraph(esc(caption), CAP))
    else:
        out.append(Spacer(1, 7))
    return out


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")


def FIG(name, caption, width=None, keep=True):
    path = os.path.join(FIGDIR, name if name.endswith(".png") else name + ".png")
    if not os.path.exists(path):
        return [Paragraph("[missing figure: %s]" % name, CAP)]
    iw, ih = ImageReader(path).getSize()
    asp = ih / float(iw)
    w = width or (FW * 0.86 if asp < 0.45 else FW * 0.70)
    w = min(w, FW)
    h = w * ih / float(iw)
    maxh = FH * 0.66
    if h > maxh:
        h = maxh
        w = h * iw / float(ih)
    img = Image(path, width=w, height=h)
    img.hAlign = "CENTER"
    blk = [Spacer(1, 4), img, Paragraph(esc(caption), CAP)]
    return [KeepTogether(blk)] if keep else blk


def FIGROW(items, caption, width=None):
    """items: list of (name) placed side by side."""
    cells = []
    tw = width or FW
    each = tw / len(items) - 6
    for n in items:
        path = os.path.join(FIGDIR, n if n.endswith(".png") else n + ".png")
        iw, ih = ImageReader(path).getSize()
        h = each * ih / float(iw)
        im = Image(path, width=each, height=h)
        cells.append(im)
    t = Table([cells], colWidths=[tw / len(items)] * len(items),
              style=TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                ("LEFTPADDING", (0, 0), (-1, -1), 1),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 1)]))
    return [KeepTogether([Spacer(1, 4), t, Paragraph(esc(caption), CAP)])]


# --------------------------------------------------------------------------- #
# Two-column helper (formula sheet)
# --------------------------------------------------------------------------- #
def TWOCOL(left, right, gap=10):
    w = (FW - gap) / 2.0
    t = Table([[left, right]], colWidths=[w, w],
              style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("LEFTPADDING", (0, 0), (0, 0), 0),
                                ("RIGHTPADDING", (0, 0), (0, 0), gap / 2.0),
                                ("LEFTPADDING", (1, 0), (1, 0), gap / 2.0),
                                ("RIGHTPADDING", (1, 0), (-1, -1), 0)]))
    return [t]


def FCARD(title, lines, color="blue", width=None):
    """Compact formula card used on the formula sheet."""
    pal = {"blue": (LBLUE, BLUE), "teal": (LTEAL, TEAL), "gold": (LGOLD, GOLD),
           "rust": (LRUST, RUST), "plum": (LPLUM, PLUM), "grey": (LGREY, GREY)}[color]
    st = ParagraphStyle("fc", fontName="DJSans", fontSize=7.9, leading=11.2,
                        alignment=TA_LEFT, spaceAfter=1.4,
                        textColor=colors.HexColor("#10233A"))
    inner = [Paragraph(esc(title.upper()), ParagraphStyle(
        "fct", fontName="DJSans-Bold", fontSize=7.7, leading=9.8,
        textColor=colors.white, spaceAfter=0))]
    hdr = Table([[inner]], colWidths=[(width or FW) - 2], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), pal[1]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    body = [Paragraph(esc(x), st) for x in lines]
    box = Table([[hdr], [body]], colWidths=[(width or FW)], style=TableStyle([
        ("BACKGROUND", (0, 1), (-1, 1), pal[0]),
        ("BOX", (0, 0), (-1, -1), 0.5, pal[1]),
        ("LEFTPADDING", (0, 0), (-1, 0), 0), ("RIGHTPADDING", (0, 0), (-1, 0), 0),
        ("TOPPADDING", (0, 0), (-1, 0), 0), ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
        ("LEFTPADDING", (0, 1), (-1, 1), 7), ("RIGHTPADDING", (0, 1), (-1, 1), 5),
        ("TOPPADDING", (0, 1), (-1, 1), 5), ("BOTTOMPADDING", (0, 1), (-1, 1), 5)]))
    return [box, Spacer(1, 6)]


# --------------------------------------------------------------------------- #
# TOC-aware marker
# --------------------------------------------------------------------------- #
class _TOCMark(Flowable):
    def __init__(self, level, text, key, header=None):
        Flowable.__init__(self)
        self.level, self.text, self.key, self.header = level, text, key, header
        self.width = self.height = 0

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        canv = self.canv
        canv.bookmarkPage(self.key)
        canv.addOutlineEntry(self.text, self.key, level=self.level,
                             closed=(self.level == 0))
        if self.header is not None:
            HDR["cur"] = self.header


HDR = {"cur": ""}


# --------------------------------------------------------------------------- #
# Document template
# --------------------------------------------------------------------------- #
class NotesDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="BEU 101401 Transportation Engineering — Semester Exam Notes",
                                 author="Kiro — exam notes compilation",
                                 subject="Bihar Engineering University, B.Tech Civil Engineering",
                                 **kw)
        fr = Frame(LM, BM + 6 * mm, FW, PH - TM - BM - 8 * mm, id="main",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        g = 10
        cw = (FW - g) / 2.0
        f1 = Frame(LM, BM + 6 * mm, cw, PH - TM - BM - 8 * mm, id="c1",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        f2 = Frame(LM + cw + g, BM + 6 * mm, cw, PH - TM - BM - 8 * mm, id="c2",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        plain = Frame(LM, BM, FW, PH - TM - BM, id="plain",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate("cover", [plain], onPage=self._cover),
            PageTemplate("main", [fr], onPageEnd=self._deco),
            PageTemplate("two", [f1, f2], onPageEnd=self._deco),
        ])
        self._toc_entries = []

    # -- chrome ------------------------------------------------------------- #
    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, PH - 26 * mm, PW, 26 * mm, stroke=0, fill=1)
        canv.setFillColor(GOLD)
        canv.rect(0, PH - 27.6 * mm, PW, 1.6 * mm, stroke=0, fill=1)
        canv.setFillColor(NAVY)
        canv.rect(0, 0, PW, 15 * mm, stroke=0, fill=1)
        canv.setFillColor(GOLD)
        canv.rect(0, 15 * mm, PW, 1.4 * mm, stroke=0, fill=1)
        canv.restoreState()

    def _deco(self, canv, doc):
        canv.saveState()
        # header rule + text
        y = PH - TM + 3.5 * mm
        canv.setStrokeColor(colors.HexColor("#B9CBDD"))
        canv.setLineWidth(0.6)
        canv.line(LM, y, PW - RM, y)
        canv.setFont("DJSans", 6.9)
        canv.setFillColor(GREY)
        canv.drawString(LM, y + 2.4, "BEU 101401 \u2022 TRANSPORTATION ENGINEERING \u2022 SEMESTER EXAM NOTES")
        canv.setFont("DJSans-Bold", 6.9)
        canv.setFillColor(NAVY)
        canv.drawRightString(PW - RM, y + 2.4, (HDR["cur"] or "").upper()[:72])
        # footer
        fy = BM + 1.5 * mm
        canv.setStrokeColor(colors.HexColor("#B9CBDD"))
        canv.line(LM, fy + 8, PW - RM, fy + 8)
        canv.setFont("DJSans", 6.9)
        canv.setFillColor(GREY)
        canv.drawString(LM, fy, "Compiled from Khanna & Justo, Kadiyali, Partha Chakraborty & IRC codes")
        canv.setFont("DJSans-Bold", 8.2)
        canv.setFillColor(NAVY)
        canv.drawRightString(PW - RM, fy - 0.5, "Page %d" % doc.page)
        canv.restoreState()

    # -- TOC hookup --------------------------------------------------------- #
    def afterFlowable(self, flowable):
        if isinstance(flowable, _TOCMark):
            self.notify("TOCEntry", (flowable.level, flowable.text, self.page, flowable.key))


def build(story, out):
    doc = NotesDoc(out)
    doc.multiBuild(story)
    return out


def make_toc():
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("t0", fontName="DJSans-Bold", fontSize=10, leading=15,
                       textColor=NAVY, spaceBefore=7, leftIndent=0,
                       firstLineIndent=0, endDots=" ."),
        ParagraphStyle("t1", fontName="DJSerif", fontSize=8.6, leading=12.4,
                       leftIndent=15, firstLineIndent=0, endDots=" .",
                       textColor=colors.HexColor("#222222")),
        ParagraphStyle("t2", fontName="DJSerif", fontSize=8.0, leading=11,
                       leftIndent=30, firstLineIndent=0, endDots=" .",
                       textColor=GREY),
    ]
    return toc
