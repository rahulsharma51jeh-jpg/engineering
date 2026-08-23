"""Diagrams for Unit 1 (development & planning) and Unit 2 (geometric design)."""
from figbase import *


# =========================================================================== #
# UNIT 1
# =========================================================================== #
def _band(ax, xs, ylow, th, fc, ec=INK, lw=0.8, hatch=None, z=3):
    yl = np.asarray(ylow, dtype=float)
    yu = yl + th
    pts = list(zip(xs, yl)) + list(zip(xs[::-1], yu[::-1]))
    poly(ax, pts, fc=fc, ec=ec, lw=lw, z=z, hatch=hatch)
    return yu


PL, PR = 2.6, 9.4              # pavement edges (all historic sections)


def _earthwork(ax, xs, ycrown, shdrop=3.0, xL=1.5, xR=10.5, base=-20,
               ditch_d=7.0, xLL=-1.6, xRR=12.6):
    """Earth body: flat ground -> V side ditch -> shoulder -> crowned subgrade."""
    ye = ycrown[0]
    yg = ye - shdrop
    top = ([(xLL, yg), (xL - 1.5, yg), (xL - 0.75, yg - ditch_d), (xL, yg)]
           + list(zip(xs, ycrown))
           + [(xR, yg), (xR + 0.75, yg - ditch_d), (xR + 1.5, yg), (xRR, yg)])
    poly(ax, top + [(xRR, base), (xLL, base)], fc=SOIL, ec=INK, lw=0.9, z=2)
    for a, b in ((xLL, xL - 1.55), (xR + 1.55, xRR)):
        for xx in np.linspace(a, b, 7):
            ax.plot([xx, xx + 0.22], [yg, yg + 2.0], color=INK, lw=0.45, zorder=3)
    leader(ax, (xLL - 2.9, yg + 8), ((xL + PL) / 2, yg + 1.2), "shoulder",
           size=7.0, ha="right")
    leader(ax, (xLL - 2.9, yg - ditch_d), (xL - 0.75, yg - ditch_d + 0.6),
           "side ditch", size=7.0, ha="right", c=TEA)
    return yg


def f_tresaguet():
    fig, ax = newfig(6.9, 2.2)
    xs = np.linspace(PL, PR, 160)
    cr = -8.0 * np.abs(xs - 6.0) / 3.4          # crowned subgrade, 8 cm drop
    _earthwork(ax, xs, cr, shdrop=3.0)
    y1 = _band(ax, xs, cr, 17, GRAN)            # foundation stones set on edge
    y2 = _band(ax, xs, y1, 8, "#C2CCD4")        # broken stone
    y3 = _band(ax, xs, y2, 5, "#9AA7B2")        # wearing course
    for xx in np.linspace(PL + 0.18, PR - 0.18, 17):
        i = int((xx - PL) / (PR - PL) * 159)
        ax.plot([xx, xx], [cr[i] + 1, cr[i] + 16], color=INK, lw=0.5, zorder=4)
    leader(ax, (13.6, 4), (9.3, 8), "large foundation stones\nplaced on edge, 17 cm", size=7.1)
    leader(ax, (13.6, 21), (9.2, y1[-1] + 4), "broken stone, 8 cm", size=7.1)
    leader(ax, (13.6, 32), (8.0, y3[70] - 2), "wearing course of small\nstones (\u2264 2.5 cm), 5 cm", size=7.1)
    dim(ax, (PL, 41), (PR, 41), "central carriageway 5.4 m", off=0, size=7.3)
    dim(ax, (10.5, cr[-1]), (10.5, y3[-1]), "30 cm", off=0, size=7.3, rot=0)
    extline(ax, (PR, cr[-1]), (10.9, cr[-1]))
    extline(ax, (PR, y3[-1]), (10.9, y3[-1]))
    lab(ax, 5.5, 48, "Cross slope of subgrade AND of surface \u2248 1 in 45 \u2014 camber obtained by sloping the subgrade",
        size=7.2, color=ACC, style="italic")
    ax.set_xlim(-8.4, 18.4)
    ax.set_ylim(-24, 54)
    title(ax, "(a) Tresaguet construction (1764)  \u2014  total thickness 30 cm", y=1.02, x=0.42)
    save(fig, "f1_tresaguet")


def f_telford():
    fig, ax = newfig(6.9, 2.2)
    xs = np.linspace(PL, PR, 160)
    flat = np.zeros_like(xs)
    _earthwork(ax, xs, flat, shdrop=1.0)
    th = 22.0 - 5.0 * np.abs(xs - 6.0) / 3.4    # 17 cm at edge -> 22 cm at centre
    yu = flat + th
    poly(ax, list(zip(xs, flat)) + list(zip(xs[::-1], yu[::-1])),
         fc=GRAN, ec=INK, lw=0.9, z=3)
    for xx in np.linspace(PL + 0.2, PR - 0.2, 15):
        i = int((xx - PL) / (PR - PL) * 159)
        ax.plot([xx, xx], [1, yu[i] - 1], color=INK, lw=0.5, zorder=4)
    y2 = _band(ax, xs, yu, 5, "#C2CCD4")
    y3 = _band(ax, xs, y2, 5, "#B0BCC6")
    y4 = _band(ax, xs, y3, 4, "#98A5B0")
    leader(ax, (13.6, 8), (9.3, 11), "large foundation stones hand-packed,\n17 cm at edge \u2192 22 cm at centre", size=7.1)
    leader(ax, (13.6, 25), (8.6, y2[60] - 2), "broken stone (\u2264 6.5 cm) in\ntwo layers, 5 cm + 5 cm", size=7.1)
    leader(ax, (13.6, 37), (7.4, y4[45] - 1.5), "binding layer of gravel, 4 cm", size=7.1)
    dim(ax, (11.2, 0), (11.2, y4[-1]), "\u2248 35 cm", off=0, size=7.3, rot=0)
    extline(ax, (PR, 0), (11.6, 0))
    extline(ax, (PR, y4[-1]), (11.6, y4[-1]))
    dim(ax, (PL, 46), (PR, 46), "central carriageway 5.5 m", size=7.3)
    lab(ax, 5.5, 53, "Subgrade kept FLAT; camber produced by varying the depth of the stone foundation "
                     "\u2014 surface slope \u2248 1 in 45", size=7.2, color=ACC, style="italic")
    ax.set_xlim(-8.4, 18.4)
    ax.set_ylim(-24, 59)
    title(ax, "(b) Telford construction (1824)", y=1.02, x=0.42)
    save(fig, "f1_telford")


def f_macadam():
    fig, ax = newfig(6.9, 2.2)
    xs = np.linspace(PL, PR, 160)
    cr = -9.5 * np.abs(xs - 6.0) / 3.4
    _earthwork(ax, xs, cr, shdrop=2.5)
    y1 = _band(ax, xs, cr, 10, "#C8D2DA")
    y2 = _band(ax, xs, y1, 10, "#B4C0CA")
    y3 = _band(ax, xs, y2, 5, "#9AA7B2")
    leader(ax, (13.6, 1), (9.3, cr[-1] + 5), "broken stone < 5 cm size,\ncompacted 10 cm", size=7.1)
    leader(ax, (13.6, 16), (9.2, y1[-1] + 5), "broken stone < 3.75 cm size,\ncompacted 10 cm", size=7.1)
    leader(ax, (13.6, 30), (7.8, y3[70] - 2.5), "broken stone < 2 cm size,\ncompacted 5 cm", size=7.1)
    dim(ax, (11.2, cr[-1]), (11.2, y3[-1]), "25 cm", off=0, size=7.3, rot=0)
    extline(ax, (PR, cr[-1]), (10.9, cr[-1]))
    extline(ax, (PR, y3[-1]), (10.9, y3[-1]))
    dim(ax, (PL, 39), (PR, 39), "carriageway", size=7.3)
    lab(ax, 5.5, 46, "Cross slope of subgrade = cross slope of surface = 1 in 36", size=7.2,
        color=ACC, style="italic")
    lab(ax, 5.5, -27.5, "First method to recognise that the SUBGRADE carries the load and must be kept drained",
        size=7.2, color=TEA, style="italic")
    ax.set_xlim(-8.4, 18.4)
    ax.set_ylim(-31, 52)
    title(ax, "(c) Macadam construction (1827)  \u2014  the basis of modern WBM", y=1.02, x=0.42)
    save(fig, "f1_macadam")


def f_star_grid():
    fig, ax = newfig(5.0, 4.3, equal=True)
    # grid of squares (rectangular block pattern)
    for i in range(5):
        line(ax, [0, 8], [i * 2, i * 2], c="#9FB3C6", lw=0.7)
        line(ax, [i * 2, i * 2], [0, 8], c="#9FB3C6", lw=0.7)
    # the "star": radial roads from the central market town
    cx, cy = 4, 4
    for (px, py) in [(0, 0), (8, 0), (0, 8), (8, 8), (0, 4), (8, 4), (4, 0), (4, 8)]:
        line(ax, [cx, px], [cy, py], c=ACC, lw=1.5, z=6)
    # main grid highways (thicker)
    line(ax, [0, 8], [4, 4], c=INK, lw=2.4, z=7)
    line(ax, [4, 4], [0, 8], c=INK, lw=2.4, z=7)
    ax.add_patch(Circle((cx, cy), 0.42, fc=RED, ec="white", lw=1.0, zorder=12))
    lab(ax, cx, cy, "M", size=8.0, color="white", weight="bold")
    for (x, y) in [(0, 0), (8, 0), (0, 8), (8, 8), (0, 4), (8, 4), (4, 0), (4, 8),
                   (2, 2), (6, 2), (2, 6), (6, 6)]:
        ax.add_patch(Circle((x, y), 0.20, fc="white", ec=INK, lw=0.8, zorder=11))
    lab(ax, 4.0, 8.55, "M = central market / district town   \u25cb = village or production centre",
        size=7.2, color=GREY)
    leader(ax, (9.3, 6.6), (6.0, 6.0), "radial (star) roads", size=7.4, c=ACC)
    leader(ax, (9.3, 4.6), (7.2, 4.0), "grid highways", size=7.4, c=INK)
    leader(ax, (-1.4, 2.2), (1.0, 2.0), "grid of MDR / ODR", size=7.4, ha="right", c="#5A7794")
    ax.set_xlim(-4.2, 12.4)
    ax.set_ylim(-1.0, 9.4)
    title(ax, "Star-and-grid road pattern assumed in the Nagpur Road Plan", y=1.01, size=9.0)
    save(fig, "f1_stargrid")


def f_road_class():
    fig, ax = newfig(7.1, 3.5)
    def box(x, y, w, h, t, fc=LGT, ec=INK, fs=7.6, bold=False, tc=INK):
        rect(ax, x, y, w, h, fc=fc, ec=ec, lw=0.9, z=4)
        lab(ax, x + w / 2, y + h / 2, t, size=fs,
            weight="bold" if bold else "normal", color=tc)
    box(1.6, 8.6, 4.6, 0.95, "ROADS IN INDIA", fc=INK, tc="white", bold=True, fs=8.6)
    # left branch : Nagpur (1943) classification
    box(-2.4, 6.9, 4.3, 0.85, "Nagpur Plan classification\n(5 classes)", fc="#DCE7F2", bold=True)
    box(5.9, 6.9, 4.4, 0.85, "Third Plan / modified\nclassification (3 classes)", fc="#E3F0EE", bold=True)
    line(ax, [3.9, 3.9], [8.6, 8.35], lw=0.9)
    line(ax, [-0.25, 8.1], [8.35, 8.35], lw=0.9)
    line(ax, [-0.25, -0.25], [8.35, 7.75], lw=0.9)
    line(ax, [8.1, 8.1], [8.35, 7.75], lw=0.9)
    ncls = [("National Highways (NH)", "Central Govt / NHAI"),
            ("State Highways (SH)", "State PWD"),
            ("Major District Roads (MDR)", "Zilla Parishad / PWD"),
            ("Other District Roads (ODR)", "District board"),
            ("Village Roads (VR)", "Panchayat / PMGSY")]
    for i, (a, b) in enumerate(ncls):
        y = 5.75 - i * 1.02
        box(-2.9, y, 3.6, 0.78, a, fc="#EEF4FA", fs=7.3)
        lab(ax, 0.85, y + 0.39, b, size=6.7, color=GREY, ha="left", style="italic")
        line(ax, [-3.35, -2.9], [y + 0.39, y + 0.39], lw=0.7)
    line(ax, [-3.35, -3.35], [6.9, 5.75 + 0.39], lw=0.7)
    mcls = [("Primary", "Expressways + National Highways"),
            ("Secondary", "State Highways + Major District Roads"),
            ("Tertiary\n(rural roads)", "Other District Roads + Village Roads")]
    for i, (a, b) in enumerate(mcls):
        y = 5.4 - i * 1.55
        box(6.35, y, 2.1, 1.05, a, fc="#E8F4F1", fs=7.4, bold=True)
        lab(ax, 8.6, y + 0.52, b, size=6.9, color=GREY, ha="left", style="italic")
        line(ax, [6.0, 6.35], [y + 0.52, y + 0.52], lw=0.7)
    line(ax, [6.0, 6.0], [6.9, 5.4 + 0.52], lw=0.7)
    lab(ax, 2.9, 0.35, "Urban roads (IRC): Expressways \u2022 Arterial \u2022 Sub-arterial \u2022 Collector \u2022 Local streets",
        size=7.5, color=PUR, weight="bold")
    rect(ax, -3.5, 0.0, 13.2, 0.72, fc="#F3EAF6", ec=PUR, lw=0.8, z=2)
    ax.set_xlim(-4.0, 13.6)
    ax.set_ylim(-0.4, 10.1)
    save(fig, "f1_roadclass")


def f_alignment():
    fig, ax = newfig(7.0, 3.2)
    A, B = (0.4, 1.2), (12.6, 5.4)
    # obstacles
    ax.add_patch(Ellipse((5.2, 4.6), 3.6, 2.2, fc="#CFE3D5", ec=GRN, lw=0.9, zorder=2))
    lab(ax, 5.2, 4.6, "marshy /\nunstable land", size=7.0, color=GRN)
    ax.add_patch(Ellipse((9.4, 1.5), 2.4, 1.5, fc="#DCD3C4", ec="#7A6A4F", lw=0.9, zorder=2))
    lab(ax, 9.4, 1.5, "hillock", size=7.0, color="#6A5A3F")
    # river
    rv = np.linspace(0, 7.2, 100)
    rx = 7.4 + 0.55 * np.sin(rv * 0.9)
    poly(ax, list(zip(rx - 0.30, rv)) + list(zip((rx + 0.30)[::-1], rv[::-1])),
         fc="#CBE2F2", ec="#4A90C0", lw=0.8, z=1)
    lab(ax, 6.35, 6.8, "river", size=7.2, color="#2A6E9E", rot=72)
    # straight (ideal) line
    line(ax, [A[0], B[0]], [A[1], B[1]], c="#9AA5AE", lw=1.0, ls=(0, (5, 3)), z=3)
    lab(ax, 6.0, 2.75, "shortest straight line (obligatory only in theory)",
        size=7.0, color="#7A858E", rot=19)
    # actual alignment
    px = [0.4, 2.6, 4.2, 6.2, 7.6, 9.0, 10.6, 12.6]
    py = [1.2, 1.5, 2.5, 3.1, 3.35, 3.6, 4.6, 5.4]
    t = np.linspace(0, 1, 240)
    from numpy.polynomial import polynomial as Pn
    cs = np.polyfit(px, py, 5)
    xx = np.linspace(0.4, 12.6, 240)
    yy = np.polyval(cs, xx)
    line(ax, xx, yy, c=ACC, lw=2.2, z=6)
    # bridge at right angles to river
    line(ax, [7.05, 8.15], [3.28, 3.42], c=INK, lw=3.4, z=8)
    lab(ax, 7.6, 2.55, "bridge site \u22a5 to river\n(obligatory point)", size=7.0, color=INK)
    for (p, n, dx) in [(A, "A", -0.45), (B, "B", 0.4)]:
        ax.add_patch(Circle(p, 0.16, fc=INK, ec="white", lw=0.8, zorder=12))
        lab(ax, p[0] + dx, p[1], n, size=9.0, weight="bold")
    lab(ax, 2.1, 0.55, "alignment deviated to\navoid poor soil, to cross\nthe river squarely and to\nskirt the hillock",
        size=7.1, color=ACC, ha="left")
    ax.set_xlim(-0.6, 13.4)
    ax.set_ylim(-0.2, 7.6)
    title(ax, "Factors that force a highway alignment away from the straight line", y=0.99, size=9.0)
    save(fig, "f1_alignment")


def f_surveys():
    fig, ax = newfig(7.1, 3.5)
    stages = [
        ("1. MAP STUDY", "Topo-sheets 1:50 000 \u2022 alternative\nroutes, valleys, passes, ponds,\nsaddles marked on paper", "#DCE7F2"),
        ("2. RECONNAISSANCE", "Field inspection of the alternatives \u2022\nabney level, barometer, compass \u2022\nrejects unsuitable routes", "#E3F0EE"),
        ("3. PRELIMINARY SURVEY", "Rapid traverse, levelling, soil &\ndrainage survey, traffic study \u2022\ncompare alternatives economically", "#FBEDE5"),
        ("4. FINAL LOCATION &\n    DETAILED SURVEY", "Centre line staked on ground,\nL-section, cross-sections,\ndrainage & bridge details", "#F3EAF6"),
    ]
    y = 8.4
    for i, (h, b, c) in enumerate(stages):
        rect(ax, 0.4, y - 1.55, 4.6, 1.55, fc=c, ec=INK, lw=0.9, z=4)
        lab(ax, 0.75, y - 0.35, h, size=8.0, weight="bold", ha="left")
        lab(ax, 0.75, y - 1.05, b, size=6.9, ha="left", color="#333333")
        if i < 3:
            arr(ax, (2.7, y - 1.62), (2.7, y - 2.05), lw=1.1, ms=8)
        y -= 2.12
    outs = ["Drawings to be submitted:",
            "\u2022 Key map (1:50 000)", "\u2022 Index map", "\u2022 Preliminary survey plan",
            "\u2022 Detailed plan & L-section", "\u2022 Cross-sections (typical + at intervals)",
            "\u2022 Land acquisition plan", "\u2022 Drawings of cross-drainage works",
            "\u2022 Soil profile / borrow pit chart"]
    rect(ax, 5.6, 1.7, 4.9, 6.7, fc="#FAFCFE", ec=BIT, lw=0.9, z=3)
    yy = 7.95
    for i, o in enumerate(outs):
        lab(ax, 5.9, yy, o, size=7.2, ha="left",
            weight="bold" if i == 0 else "normal",
            color=INK if i == 0 else "#333333")
        yy -= 0.72
    rect(ax, 5.6, 0.15, 4.9, 1.25, fc="#FFF6E0", ec=GOLD if False else "#C9880B", lw=0.9, z=3)
    lab(ax, 6.05, 0.78, "Project report: cost estimate,\nsoil & materials report, traffic\nforecast, economic evaluation",
        size=7.1, ha="left", color="#7A5300")
    arr(ax, (5.05, 4.5), (5.55, 4.5), lw=1.1, ms=8)
    ax.set_xlim(0.0, 10.9)
    ax.set_ylim(0.0, 9.0)
    title(ax, "Engineering surveys for highway location and project preparation", y=0.99, size=9.0)
    save(fig, "f1_surveys")


# =========================================================================== #
# UNIT 2
# =========================================================================== #
def f_xsection_embank():
    fig, ax = newfig(7.1, 2.9)
    cw, sh = 7.0, 2.5                    # carriageway 7 m, shoulder 2.5 m
    xc = 0.0
    top = 3.0
    cam = 0.16                           # camber drop (exaggerated)
    xs = np.linspace(-cw / 2, cw / 2, 120)
    ysurf = top - cam * (np.abs(xs) / (cw / 2)) ** 2 * 1.0
    # shoulders
    shl_y0 = ysurf[0]
    poly(ax, [(-cw / 2, shl_y0), (-cw / 2 - sh, shl_y0 - 0.34),
              (-cw / 2 - sh, shl_y0 - 0.62), (-cw / 2, ysurf[0] - 0.55)],
         fc=SOIL, ec=INK, lw=0.9, z=4)
    poly(ax, [(cw / 2, shl_y0), (cw / 2 + sh, shl_y0 - 0.34),
              (cw / 2 + sh, shl_y0 - 0.62), (cw / 2, ysurf[0] - 0.55)],
         fc=SOIL, ec=INK, lw=0.9, z=4)
    # pavement layers
    poly(ax, list(zip(xs, ysurf)) + list(zip(xs[::-1], (ysurf - 0.55)[::-1])),
         fc=BIT, ec=INK, lw=0.9, z=5)
    # embankment body
    H = 2.05
    base_y = top - cam - 0.62 - H
    toe = 2.0 * H                        # 2:1 side slope
    poly(ax, [(-cw / 2 - sh, shl_y0 - 0.62), (cw / 2 + sh, shl_y0 - 0.62),
              (cw / 2 + sh + toe, base_y), (-cw / 2 - sh - toe, base_y)],
         fc="#EFE7D8", ec=INK, lw=0.9, z=3)
    ground(ax, -14.5, 14.5, base_y, n=52, d=0.13)
    # side drains
    for s in (-1, 1):
        x0 = s * (cw / 2 + sh + toe + 0.5)
        poly(ax, [(x0 - 0.75, base_y), (x0, base_y - 0.55), (x0 + 0.75, base_y)],
             fc="#CBE2F2", ec=INK, lw=0.8, z=6)
        lab(ax, x0, base_y - 0.95, "side drain", size=6.9, color=TEA)
    # dimensions
    dim(ax, (-cw / 2, top + 0.95), (cw / 2, top + 0.95), "carriageway  7.0 m", size=7.4)
    dim(ax, (-cw / 2 - sh, top + 1.62), (cw / 2 + sh, top + 1.62),
        "roadway (formation) width  12.0 m", size=7.4)
    dim(ax, (-13.6, top + 2.35), (13.6, top + 2.35),
        "Land width / Right of Way (ROW)", size=7.6)
    for x in (-cw / 2, cw / 2):
        extline(ax, (x, ysurf[0]), (x, top + 1.0))
    for x in (-cw / 2 - sh, cw / 2 + sh):
        extline(ax, (x, shl_y0 - 0.34), (x, top + 1.67))
    for x in (-13.6, 13.6):
        extline(ax, (x, base_y), (x, top + 2.4))
    dim(ax, (cw / 2 + sh + toe + 2.6, base_y), (cw / 2 + sh + toe + 2.6, shl_y0 - 0.62),
        "height of\nembankment", size=7.0, rot=0)
    lab(ax, -cw / 2 - sh, top + 0.42, "shoulder\n2.5 m", size=7.0, color=INK)
    lab(ax, cw / 2 + sh, top + 0.42, "shoulder\n2.5 m", size=7.0, color=INK)
    leader(ax, (-13.4, 1.55), (-cw / 2 - sh - toe / 2, base_y + H / 2),
           "side slope 2 : 1", size=7.1, ha="left", c=ACC)
    lab(ax, 0, ysurf[60] - 0.28, "pavement", size=6.8, color="white")
    curvearrow(ax, (-3.2, top + 0.34), (-0.6, ysurf[55] + 0.05), rad=0.30,
               text="camber", size=7.0)
    ax.plot([0, 0], [base_y - 0.2, top + 2.9], color="#9AA5AE", lw=0.7, ls=(0, (6, 3, 1, 3)))
    lab(ax, 0.35, top + 2.75, "\u2104", size=8.0, color="#7A858E", ha="left")
    ax.set_xlim(-17.5, 17.5)
    ax.set_ylim(base_y - 1.6, top + 3.0)
    title(ax, "Typical cross-section of a two-lane highway in EMBANKMENT (vertical scale exaggerated)",
          y=1.0, size=8.6)
    save(fig, "f2_xsection_embank")


def f_xsection_cut():
    fig, ax = newfig(7.1, 2.7)
    cw, sh = 7.0, 2.0
    top = 0.0
    cam = 0.15
    xs = np.linspace(-cw / 2, cw / 2, 120)
    ysurf = top - cam * (np.abs(xs) / (cw / 2)) ** 2
    D = 2.6                                   # depth of cut
    bs = 1.0 * D                              # back slope 1:1
    xd = cw / 2 + sh + 1.4                    # drain outer edge
    # natural ground before cutting
    extline(ax, (-xd - bs - 3.2, D), (xd + bs + 3.2, D), c="#9AA5AE", lw=0.8)
    lab(ax, -xd - bs - 1.6, D + 0.28, "original ground level", size=7.0, color="#5A7794")
    # earth mass
    poly(ax, [(-xd - bs - 3.4, D), (-xd - bs - 3.4, -1.9), (xd + bs + 3.4, -1.9),
              (xd + bs + 3.4, D), (xd + bs, D), (xd, -0.62), (xd - 0.9, -0.62),
              (cw / 2 + sh, -0.55), (cw / 2, -0.5), (-cw / 2, -0.5),
              (-(cw / 2 + sh), -0.55), (-(xd - 0.9), -0.62), (-xd, -0.62),
              (-(xd + bs), D)],
         fc=SOIL, ec=INK, lw=0.9, z=3)
    poly(ax, list(zip(xs, ysurf)) + list(zip(xs[::-1], (ysurf - 0.5)[::-1])),
         fc=BIT, ec=INK, lw=0.9, z=6)
    poly(ax, [(-cw / 2, ysurf[0]), (-(cw / 2 + sh), -0.30),
              (-(cw / 2 + sh), -0.55), (-cw / 2, -0.5)], fc="#D8CDB6", ec=INK, lw=0.9, z=6)
    poly(ax, [(cw / 2, ysurf[0]), (cw / 2 + sh, -0.30),
              (cw / 2 + sh, -0.55), (cw / 2, -0.5)], fc="#D8CDB6", ec=INK, lw=0.9, z=6)
    for s in (-1, 1):
        poly(ax, [(s * (cw / 2 + sh), -0.30), (s * (xd - 0.45), -0.95),
                  (s * xd, -0.35)], fc="#CBE2F2", ec=INK, lw=0.9, z=7)
    lab(ax, -(xd - 0.4), -1.45, "longitudinal\nside drain", size=6.9, color=TEA)
    # catch water drain
    poly(ax, [(xd + bs + 1.5, D), (xd + bs + 1.95, D - 0.45), (xd + bs + 2.4, D)],
         fc="#CBE2F2", ec=INK, lw=0.9, z=8)
    leader(ax, (xd + bs + 3.6, D + 0.75), (xd + bs + 1.95, D - 0.15),
           "catch-water drain\n(intercepts hill run-off)", size=7.0, c=TEA)
    dim(ax, (-cw / 2, 0.85), (cw / 2, 0.85), "carriageway 7.0 m", size=7.4)
    dim(ax, (-(cw / 2 + sh), 1.5), (cw / 2 + sh, 1.5), "roadway width", size=7.4)
    leader(ax, (-xd - bs - 3.2, 1.35), (-(xd + bs / 2), D / 2),
           "back slope / cut slope\n(1 : 1 to 1 : 4 as per soil)", size=7.0, ha="left", c=ACC)
    dim(ax, (xd + 0.35, -0.62), (xd + 0.35, D), "depth of cutting", size=7.0)
    ax.set_xlim(-xd - bs - 4.4, xd + bs + 7.2)
    ax.set_ylim(-2.1, D + 1.9)
    title(ax, "Cross-section of a highway in CUTTING", y=1.0, size=8.8)
    save(fig, "f2_xsection_cut")


def f_camber():
    fig, ax = newfig(7.1, 1.85)
    W = 3.4
    for k, (name, expr) in enumerate([
            ("(a) Parabolic (barrel) camber", "y = 2x\u00b2 / (nW)"),
            ("(b) Straight-line camber", "straight cross slope 1 in n"),
            ("(c) Combination camber", "parabola at crown + straight at edges")]):
        x0 = k * 4.6
        xs = np.linspace(-W / 2, W / 2, 160)
        if k == 0:
            ys = 0.62 - 0.62 * (xs / (W / 2)) ** 2
        elif k == 1:
            ys = 0.62 - 0.62 * np.abs(xs) / (W / 2)
        else:
            ys = np.where(np.abs(xs) < W / 4,
                          0.62 - 0.62 * 0.5 * (xs / (W / 4)) ** 2,
                          0.62 - 0.31 - 0.62 * 0.5 * (np.abs(xs) - W / 4) / (W / 4))
        poly(ax, list(zip(xs + x0, ys)) + list(zip((xs + x0)[::-1], (ys * 0 - 0.30)[::-1])),
             fc=BIT, ec=INK, lw=1.0, z=4)
        line(ax, [x0 - W / 2 - 0.3, x0 + W / 2 + 0.3], [0.62, 0.62],
             c="#9AA5AE", lw=0.6, ls=(0, (4, 3)))
        ax.plot([x0, x0], [-0.45, 1.05], color="#9AA5AE", lw=0.6, ls=(0, (6, 3, 1, 3)))
        lab(ax, x0, 1.42, name, size=7.6, weight="bold")
        lab(ax, x0, 1.14, expr, size=7.0, color=ACC, style="italic")
        if k == 0:
            dim(ax, (x0 + W / 2, ys[-1]), (x0 + W / 2, 0.62), "y", off=0.35, size=7.2)
            dim(ax, (x0, -0.55), (x0 + W / 2, -0.55), "W/2", size=7.2)
            dim(ax, (x0 + 1.0, ys[130]), (x0 + 1.0, 0.62), "", off=0, size=7.0)
            lab(ax, x0 + 1.25, 0.42, "x", size=7.2, color=ACC, ha="left")
            extline(ax, (x0 + 1.0, ys[130]), (x0 + 1.0, 0.75))
        lab(ax, x0, -0.75, "crown", size=6.8, color=GREY)
    ax.set_xlim(-2.2, 11.6)
    ax.set_ylim(-1.05, 1.6)
    save(fig, "f2_camber")


def f_ssd():
    fig, ax = newfig(7.1, 2.25)
    y = 1.0
    line(ax, [-0.6, 12.4], [y - 0.55, y - 0.55], c=INK, lw=1.4)
    line(ax, [-0.6, 12.4], [y + 0.85, y + 0.85], c=INK, lw=1.4)
    for xx in np.arange(-0.4, 12.4, 1.0):
        line(ax, [xx, xx + 0.55], [y + 0.15, y + 0.15], c="#C9A227", lw=1.4)
    wheelveh(ax, 0.6, y - 0.45, L=1.5, H=0.42, c=INK)
    # obstruction
    rect(ax, 10.3, y - 0.5, 0.55, 0.42, fc=RED, ec=INK, lw=0.9, z=9)
    lab(ax, 10.58, y - 0.85, "stationary\nobject", size=7.0, color=RED)
    # eye + object heights (elevation inset below)
    dim(ax, (1.5, y + 1.6), (5.2, y + 1.6), "lag distance = 0.278 V\u00b7t", size=7.6)
    dim(ax, (5.2, y + 1.6), (10.3, y + 1.6), "braking distance = V\u00b2 / (254 f)", size=7.6)
    dim(ax, (1.5, y + 2.35), (10.3, y + 2.35), "STOPPING SIGHT DISTANCE, SSD", size=8.0)
    for x in (1.5, 5.2, 10.3):
        extline(ax, (x, y - 0.6), (x, y + 2.4))
    lab(ax, 5.2, y - 1.35, "brakes applied here\n(after PIEV reaction time t = 2.5 s)", size=7.0, color=ACC)
    lab(ax, 1.5, y - 1.35, "driver perceives\nthe object", size=7.0, color=ACC)
    # small elevation showing sight line
    y2 = -2.4
    line(ax, [1.0, 11.2], [y2, y2], c=INK, lw=1.2)
    line(ax, [1.6, 1.6], [y2, y2 + 0.62], c=INK, lw=0.9)
    line(ax, [10.3, 10.3], [y2, y2 + 0.14], c=RED, lw=1.6)
    line(ax, [1.6, 10.3], [y2 + 0.62, y2 + 0.14], c=ACC, lw=0.9, ls=(0, (4, 2)))
    lab(ax, 1.15, y2 + 0.35, "driver eye\nheight\n1.2 m", size=6.9, ha="right", color=INK)
    lab(ax, 10.7, y2 + 0.20, "object height 0.15 m", size=6.9, ha="left", color=RED)
    lab(ax, 6.0, y2 + 0.62, "line of sight", size=6.9, color=ACC, style="italic")
    lab(ax, 6.0, y2 - 0.45, "IRC: eye height H = 1.2 m, object height h = 0.15 m for SSD",
        size=7.2, color=TEA)
    ax.set_xlim(-2.4, 13.6)
    ax.set_ylim(-3.4, y + 2.9)
    title(ax, "Stopping sight distance (SSD) \u2014 plan and sight-line elevation", y=1.0, size=8.8)
    save(fig, "f2_ssd")


def f_osd():
    fig, ax = newfig(7.1, 2.9)
    yl, yu = 0.0, 1.55                # lane divider positions
    line(ax, [-0.4, 15.4], [yl - 0.72, yl - 0.72], c=INK, lw=1.4)
    line(ax, [-0.4, 15.4], [yu + 0.72, yu + 0.72], c=INK, lw=1.4)
    line(ax, [-0.4, 15.4], [(yl + yu) / 2, (yl + yu) / 2], c="#C9A227", lw=1.0, ls=(0, (7, 5)))
    yA, yB, yC = 0.05, 0.05, 1.55     # A and B in the left lane, C opposing
    # B (slow vehicle) positions
    for (x, t) in [(3.4, "B\u2081"), (6.0, "B\u2082"), (9.0, "B\u2083")]:
        car(ax, x, yB, L=0.9, H=0.42, c=GRN, fc="#E4F1E8")
        lab(ax, x + 0.45, yB, t, size=7.4, color=GRN, weight="bold")
    # A (overtaking vehicle) positions
    for (x, yy, t) in [(1.5, yA, "A\u2081"), (5.0, yC, "A\u2082"), (10.4, yA, "A\u2083")]:
        car(ax, x, yy, L=0.95, H=0.42, c=INK, fc="#DDE7F1")
        lab(ax, x + 0.47, yy, t, size=7.4, weight="bold")
    # C (opposing vehicle)
    for (x, t) in [(14.6, "C\u2081"), (12.0, "C\u2082")]:
        car(ax, x, yC, L=0.95, H=0.42, c=RED, fc="#FBE3E3", dirn=-1)
        lab(ax, x - 0.47, yC, t, size=7.4, color=RED, weight="bold")
    # overtaking path
    tt = np.linspace(0, 1, 200)
    px = 1.5 + tt * 9.9
    py = yA + (yC - yA) * (np.sin(np.pi * tt) ** 2)
    line(ax, px, py + 0.0, c=ACC, lw=1.0, ls=(0, (5, 3)), z=7)
    # dimensions
    dim(ax, (2.4, 2.95), (4.3, 2.95), "d\u2081", size=7.8)
    dim(ax, (4.3, 2.95), (9.9, 2.95), "d\u2082", size=7.8)
    dim(ax, (9.9, 2.95), (14.9, 2.95), "d\u2083", size=7.8)
    dim(ax, (2.4, 3.7), (14.9, 3.7), "OVERTAKING SIGHT DISTANCE, OSD = d\u2081 + d\u2082 + d\u2083", size=8.0)
    for x in (2.4, 4.3, 9.9, 14.9):
        extline(ax, (x, -0.8), (x, 3.75))
    dim(ax, (4.3, -1.05), (6.0, -1.05), "s", size=7.4, side="below")
    dim(ax, (9.0, -1.05), (10.4, -1.05), "s", size=7.4, side="below")
    lab(ax, 7.2, -1.55, "d\u2081 = 0.278 v\u1d47 t  |  d\u2082 = 0.278 v\u1d47 T + 2s  |  d\u2083 = 0.278 V T   ;   s = 0.7 v\u1d47 + 6",
        size=7.4, color=ACC)
    lab(ax, 7.2, -2.1, "On divided highways with one-way traffic d\u2083 is not required \u21d2 OSD = d\u2081 + d\u2082",
        size=7.2, color=TEA)
    lab(ax, 8.6, 4.32, "A = overtaking vehicle    B = slow vehicle    C = vehicle from the opposite direction",
        size=7.2, color=GREY)
    ax.set_xlim(-1.4, 16.4)
    ax.set_ylim(-2.5, 4.75)
    title(ax, "Overtaking sight distance (OSD) on a two-lane two-way road", y=1.02, size=8.8)
    save(fig, "f2_osd")


def f_setback():
    fig, ax = newfig(4.9, 3.4, equal=True)
    R = 4.0
    Cx, Cy = 0.0, 0.0
    th = np.linspace(28, 152, 200) * np.pi / 180
    for r, c, lw, ls in [(R, INK, 1.6, "-"), (R - 0.9, "#7A98B4", 1.0, (0, (5, 3))),
                         (R + 0.9, "#7A98B4", 1.0, (0, (5, 3)))]:
        line(ax, Cx + r * np.cos(th), Cy + r * np.sin(th), c=c, lw=lw, ls=ls)
    d = 1.75                              # distance of inner lane centre line
    ri = R - d
    line(ax, Cx + ri * np.cos(th), Cy + ri * np.sin(th), c=ACC, lw=1.3)
    a = 62 * np.pi / 180                  # half sight angle
    m = np.pi / 2
    P1 = (ri * np.cos(m - a), ri * np.sin(m - a))
    P2 = (ri * np.cos(m + a), ri * np.sin(m + a))
    line(ax, [P1[0], P2[0]], [P1[1], P2[1]], c=RED, lw=1.2)
    Mx, My = 0.0, ri * np.cos(a)
    line(ax, [Cx, 0], [Cy, ri], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    line(ax, [Cx, P1[0]], [Cy, P1[1]], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    line(ax, [Cx, P2[0]], [Cy, P2[1]], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    # obstruction
    poly(ax, [(-1.05, ri + 0.02), (1.05, ri + 0.02), (1.05, ri + 0.62), (-1.05, ri + 0.62)],
         fc="#DCD3C4", ec="#7A6A4F", lw=0.9, z=8)
    lab(ax, 0, ri + 0.32, "obstruction", size=6.9, color="#5A4A2F")
    dim(ax, (0.0, ri), (0.0, R + 0.9), "", off=0, size=7.0)
    lab(ax, 0.22, (ri + R + 0.9) / 2, "m", size=8.4, color=ACC, ha="left", weight="bold")
    ax.add_patch(Arc((Cx, Cy), 1.5, 1.5, theta1=90, theta2=90 + 62, lw=0.8,
                     color=ACC, zorder=9))
    lab(ax, -0.62, 0.86, "\u03b1/2", size=7.4, color=ACC)
    lab(ax, 0.30, 1.5, "R \u2212 d", size=7.2, color="#5A7794", rot=90)
    lab(ax, 2.5, -0.35, "R", size=8.0, color=INK)
    line(ax, [Cx, R * np.cos(-0.0)], [Cy, 0], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    ax.add_patch(Circle((Cx, Cy), 0.09, fc=INK, ec="none", zorder=12))
    lab(ax, 0, -0.35, "O", size=8.0)
    lab(ax, P1[0] + 0.15, P1[1] - 0.42, "line of sight = S (chord)", size=7.0, color=RED, ha="left")
    lab(ax, -3.7, 3.9, "For L\u1d9c \u2265 S :   m = R \u2212 (R \u2212 d) cos( S / (2(R\u2212d)) )",
        size=7.8, color=ACC, ha="left", weight="bold")
    ax.set_xlim(-4.4, 4.6)
    ax.set_ylim(-1.0, 5.4)
    title(ax, "Set-back (clearance) distance on a horizontal curve", y=0.995, size=8.8)
    save(fig, "f2_setback")


def f_super():
    fig, ax = newfig(5.3, 3.1)
    th = np.radians(13.0)
    L = 5.4
    x0, y0 = 0.0, 0.0
    dx, dy = L * np.cos(th), L * np.sin(th)
    poly(ax, [(x0, y0), (x0 + dx, y0 + dy), (x0 + dx, y0 + dy - 0.34), (x0, y0 - 0.34)],
         fc=BIT, ec=INK, lw=1.0, z=3)
    line(ax, [x0 - 0.5, x0 + dx + 0.9], [y0, y0], c="#9AA5AE", lw=0.8, ls=(0, (5, 3)))
    ax.add_patch(Arc((x0, y0), 3.0, 3.0, theta1=0, theta2=13, lw=0.9, color=ACC, zorder=9))
    lab(ax, 1.72, 0.16, "\u03b8", size=8.4, color=ACC)
    # vehicle at mid
    cx, cy = x0 + 0.52 * dx, y0 + 0.52 * dy + 0.30
    ang = np.degrees(th)
    rectp = [(-0.62, 0.0), (0.62, 0.0), (0.62, 0.52), (-0.62, 0.52)]
    ca, sa = np.cos(th), np.sin(th)
    pts = [(cx + px * ca - py * sa, cy + px * sa + py * ca) for px, py in rectp]
    poly(ax, pts, fc="#DDE7F1", ec=INK, lw=1.0, z=8)
    G = (cx + 0.0 * ca - 0.26 * sa, cy + 0.0 * sa + 0.26 * ca)
    ax.add_patch(Circle(G, 0.07, fc=RED, ec="none", zorder=14))
    lab(ax, G[0] - 0.30, G[1] + 0.05, "G", size=7.6, color=RED, weight="bold")
    # forces
    arr(ax, G, (G[0], G[1] - 1.85), c=INK, lw=1.3, ms=9)
    lab(ax, G[0] + 0.20, G[1] - 1.95, "W = m g", size=8.0, ha="left", weight="bold")
    arr(ax, G, (G[0] + 1.9, G[1]), c=RED, lw=1.3, ms=9)
    lab(ax, G[0] + 2.0, G[1] + 0.16, "P = W v\u00b2 / (g R)\n(centrifugal force,\nacts horizontally at G)",
        size=7.4, ha="left", color=RED)
    nx, ny = -np.sin(th), np.cos(th)
    arr(ax, (cx, cy - 0.02), (cx + nx * 1.5, cy + ny * 1.5), c=TEA, lw=1.2, ms=8)
    lab(ax, cx + nx * 1.6 - 0.05, cy + ny * 1.6 + 0.16, "N", size=8.0, color=TEA, weight="bold")
    arr(ax, (cx, cy - 0.02), (cx - ca * 1.35, cy - sa * 1.35), c=PUR, lw=1.2, ms=8)
    lab(ax, cx - ca * 1.5, cy - sa * 1.5 - 0.22, "F = f\u00b7N (friction)", size=7.4, color=PUR, ha="center")
    dim(ax, (x0 + dx, y0), (x0 + dx, y0 + dy), "E (rise)", off=0.75, size=7.2)
    extline(ax, (x0 + dx, y0 + dy), (x0 + dx + 1.1, y0 + dy))
    dim(ax, (x0, y0 - 0.95), (x0 + dx, y0 - 0.95), "B (width of pavement)", size=7.2, side="below")
    lab(ax, 2.7, -2.0, "e = tan \u03b8 = E / B ;  for small \u03b8, tan \u03b8 \u2248 sin \u03b8\n\u21d2  e + f = v\u00b2/(g R) = V\u00b2/(127 R)",
        size=8.0, color=ACC, weight="bold")
    ax.set_xlim(-1.4, 9.6)
    ax.set_ylim(-2.6, 3.3)
    title(ax, "Forces on a vehicle on a superelevated circular curve", y=1.0, size=8.8)
    save(fig, "f2_super")


def f_widening():
    fig, ax = newfig(5.1, 3.3, equal=True)
    R2 = 4.6
    th = np.linspace(20, 130, 200) * np.pi / 180
    line(ax, R2 * np.cos(th), R2 * np.sin(th), c=INK, lw=1.2)
    R1 = 3.55
    line(ax, R1 * np.cos(th), R1 * np.sin(th), c=INK, lw=1.2)
    line(ax, (R1 - 0.45) * np.cos(th), (R1 - 0.45) * np.sin(th), c=ACC, lw=1.2, ls=(0, (5, 3)))
    a = np.radians(74)
    # front (outer) and rear (inner) wheel positions
    F = (R2 * np.cos(a), R2 * np.sin(a))
    b = np.radians(56)
    Rr = (R1 - 0.45)
    Rear = (Rr * np.cos(b), Rr * np.sin(b))
    line(ax, [Rear[0], F[0]], [Rear[1], F[1]], c=INK, lw=1.6, z=9)
    ax.add_patch(Circle(F, 0.11, fc=INK, ec="white", lw=0.6, zorder=12))
    ax.add_patch(Circle(Rear, 0.11, fc=ACC, ec="white", lw=0.6, zorder=12))
    lab(ax, F[0] + 0.30, F[1] + 0.20, "front wheel\n(path R\u2082)", size=7.0, ha="left")
    lab(ax, Rear[0] - 0.20, Rear[1] - 0.42, "rear wheel\n(path R\u2081)", size=7.0, color=ACC, ha="center")
    line(ax, [0, F[0]], [0, F[1]], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    line(ax, [0, Rear[0]], [0, Rear[1]], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    ax.add_patch(Circle((0, 0), 0.08, fc=INK, ec="none", zorder=12))
    lab(ax, 0.02, -0.32, "O", size=8.0)
    dim(ax, Rear, F, "l  (wheel base)", off=0.32, size=7.2)
    lab(ax, 2.35, 1.05, "R\u2081", size=7.6, color=ACC, rot=25)
    lab(ax, 3.15, 1.55, "R\u2082", size=7.6, rot=25)
    dim(ax, ((R1 - 0.45) * np.cos(np.radians(24)), (R1 - 0.45) * np.sin(np.radians(24))),
        (R2 * np.cos(np.radians(24)), R2 * np.sin(np.radians(24))),
        "", off=0, size=7.0)
    lab(ax, -4.9, 4.6, "Mechanical widening   W\u2098 = n l\u00b2 / (2 R)",
        size=8.2, color=ACC, ha="left", weight="bold")
    lab(ax, -4.9, 4.05, "Psychological widening  W\u209a\u209b = V / (9.5 \u221aR)",
        size=8.2, color=PUR, ha="left", weight="bold")
    lab(ax, -4.9, 3.5, "Total extra widening  W\u2091 = W\u2098 + W\u209a\u209b",
        size=8.2, color=INK, ha="left", weight="bold")
    lab(ax, -4.9, 0.55, "The rear wheels track on a\nsmaller radius than the front\nwheels \u21d2 the vehicle occupies\na greater width on the curve\n(OFF-TRACKING).",
        size=7.2, ha="left", color="#333333")
    ax.set_xlim(-5.0, 5.2)
    ax.set_ylim(-0.6, 5.1)
    save(fig, "f2_widening")


def f_transition():
    fig, ax = newfig(6.4, 2.9)
    # straight
    line(ax, [-0.6, 3.0], [0, 0], c=INK, lw=1.5)
    # transition (cubic-ish spiral) then circular curve
    ts = np.linspace(0, 1, 120)
    Ls = 2.6
    tx = 3.0 + ts * Ls
    ty = -0.42 * ts ** 3
    line(ax, tx, ty, c=ACC, lw=1.8)
    # circular arc continuing
    R = 4.2
    x1, y1 = tx[-1], ty[-1]
    sl = -3 * 0.42 * 1.0 ** 2 / Ls
    phi0 = np.arctan(sl)
    cxx = x1 - R * np.sin(-phi0)
    cyy = y1 - R * np.cos(phi0)
    aa = np.linspace(phi0, np.radians(-52), 140)
    ax_ = cxx + R * np.sin(-aa)
    ay_ = cyy + R * np.cos(aa)
    line(ax, ax_, ay_, c=INK, lw=1.8)
    # second transition + straight (mirror, schematic)
    line(ax, [ax_[-1], ax_[-1] + 1.9], [ay_[-1], ay_[-1] - 2.35], c=ACC, lw=1.8)
    # original (unshifted) circular curve, dashed, to display shift
    cy2 = cyy + 0.30
    aa2 = np.linspace(np.radians(24), np.radians(-56), 160)
    line(ax, cxx + R * np.sin(-aa2), cy2 + R * np.cos(aa2), c="#8FA6BC", lw=1.0, ls=(0, (5, 3)))
    # tangent point markers
    for (x, y, t, dxx, dyy) in [(3.0, 0, "T.S.", -0.05, 0.30),
                                (x1, y1, "S.C.", 0.30, 0.18),
                                (ax_[-1], ay_[-1], "C.S.", 0.32, 0.05)]:
        ax.add_patch(Circle((x, y), 0.075, fc=RED, ec="white", lw=0.6, zorder=12))
        lab(ax, x + dxx, y + dyy, t, size=7.2, color=RED, weight="bold")
    line(ax, [-0.6, 8.4], [0, 0], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    dim(ax, (5.05, -0.30), (5.05, 0.0), "", off=0, size=7.0)
    lab(ax, 5.25, -0.16, "S = L\u00b2/(24R)  (shift)", size=7.4, color=PUR, ha="left")
    dim(ax, (3.0, 0.55), (x1, 0.55), "L\u209b (transition length)", size=7.2)
    for x in (3.0, x1):
        extline(ax, (x, 0.0), (x, 0.62))
    lab(ax, 1.0, 0.30, "straight", size=7.4, color=INK)
    lab(ax, 7.0, -1.15, "circular curve\nradius R", size=7.4, color=INK, ha="left")
    lab(ax, -0.6, -1.6, "Design length of transition curve = greatest of the three:\n"
                        "(i) rate of change of centrifugal acceleration  L = 0.0215 V\u00b3/(C R),  C = 80/(75+V)\n"
                        "(ii) rate of introduction of superelevation  L = 2.7 V\u00b2/R (plain/rolling), 1 V\u00b2/R (hilly)\n"
                        "(iii) IRC empirical: L = e N (W + W\u2091) or e N W/2 depending on rotation about edge / centre",
        size=7.2, ha="left", color=ACC)
    ax.set_xlim(-1.0, 11.4)
    ax.set_ylim(-3.5, 1.1)
    title(ax, "Straight \u2192 transition \u2192 circular curve, and the shift S", y=1.0, size=8.8)
    save(fig, "f2_transition")


def _sumcurve(n1, n2, L):
    """Return callables for the summit/valley alignment: tangents meet at origin."""
    N = n1 - n2
    def y(x):
        x = np.asarray(x, dtype=float)
        return np.where(np.abs(x) <= L / 2.0,
                        n1 * x - N * (x + L / 2.0) ** 2 / (2.0 * L),
                        np.where(x < 0, n1 * x, n2 * x))
    return N, y


def f_summit():
    fig, ax = newfig(7.1, 2.65)
    n1, n2 = 0.26, -0.22
    N = n1 - n2
    H, h = 0.20, 0.11
    EXT = 3.3
    for k, (L, cname) in enumerate([(5.2, "(a) Case 1 :  L > S"),
                                    (1.5, "(b) Case 2 :  L < S")]):
        x0 = k * 9.0
        _, yf = _sumcurve(n1, n2, L)
        # tangents
        line(ax, [x0 - EXT, x0], [n1 * -EXT, 0], c="#8FA6BC", lw=0.9, ls=(0, (5, 3)))
        line(ax, [x0, x0 + EXT], [0, n2 * EXT], c="#8FA6BC", lw=0.9, ls=(0, (5, 3)))
        ax.add_patch(Circle((x0, 0), 0.055, fc="#8FA6BC", ec="none", zorder=8))
        # the parabolic curve
        xc = np.linspace(-L / 2, L / 2, 220)
        line(ax, x0 + xc, yf(xc), c=INK, lw=2.1)
        # sight line, tangent to the curve at its apex-side tangent point
        if k == 0:
            xt = 0.0
            xA, xB = xt - np.sqrt(2 * L * H / N), xt + np.sqrt(2 * L * h / N)
        else:
            # the sight line touches the curve at u = L.sqrt(H)/(sqrt(H)+sqrt(h))
            u = L * np.sqrt(H) / (np.sqrt(H) + np.sqrt(h))
            xt = u - L / 2.0
            xA = xt - (H * L / (N * u) + u / 2.0)
            xB = xt + (h * L / (N * (L - u)) + (L - u) / 2.0)
        yA, yB = float(yf(xA)), float(yf(xB))
        line(ax, [x0 + xA, x0 + xB], [yA + H, yB + h], c=RED, lw=1.05, z=11)
        line(ax, [x0 + xA, x0 + xA], [yA, yA + H], c=INK, lw=1.4, z=11)
        line(ax, [x0 + xB, x0 + xB], [yB, yB + h], c=RED, lw=1.8, z=11)
        lab(ax, x0 + xA - 0.14, yA + H / 2, "H", size=7.8, ha="right", weight="bold")
        lab(ax, x0 + xB + 0.14, yB + h / 2, "h", size=7.8, ha="left", weight="bold", color=RED)
        ax.add_patch(Circle((x0 + xt, float(yf(xt))), 0.07, fc=RED, ec="white",
                            lw=0.5, zorder=13))
        # grade labels
        lab(ax, x0 - EXT + 0.30, n1 * (-EXT + 0.30) + 0.17, "+n\u2081", size=7.8, color=ACC)
        lab(ax, x0 + EXT - 0.30, n2 * (EXT - 0.30) + 0.17, "\u2212n\u2082", size=7.8, color=ACC)
        # dimensions
        dim(ax, (x0 + xA, 0.62), (x0 + xB, 0.62), "S", size=7.8)
        dim(ax, (x0 - L / 2, 1.02), (x0 + L / 2, 1.02), "L", size=7.8)
        for x in (xA, xB):
            extline(ax, (x0 + x, float(yf(x))), (x0 + x, 0.66))
        for x in (-L / 2, L / 2):
            extline(ax, (x0 + x, float(yf(x))), (x0 + x, 1.06))
        lab(ax, x0, 1.62, cname, size=8.6, weight="bold")
        if k == 0:
            lab(ax, x0, -1.78, "L = N S\u00b2 / [ 2(\u221aH + \u221ah)\u00b2 ]\n"
                               "= N S\u00b2/4.4  (SSD)   |   N S\u00b2/9.6  (OSD, ISD)",
                size=7.5, color=ACC)
            lab(ax, x0, -1.20, "line of sight lies wholly within the curve",
                size=7.0, color=GREY, style="italic")
        else:
            lab(ax, x0, -1.78, "L = 2S \u2212 2(\u221aH + \u221ah)\u00b2 / N\n"
                               "= 2S \u2212 4.4/N  (SSD)   |   2S \u2212 9.6/N  (OSD, ISD)",
                size=7.5, color=ACC)
            lab(ax, x0, -1.20, "sight line ends lie on the tangent grades",
                size=7.0, color=GREY, style="italic")
    lab(ax, 4.5, -2.52, "Deviation angle  N = n\u2081 \u2212 (\u2212n\u2082) = n\u2081 + n\u2082   \u2022   "
                        "IRC: H = 1.2 m (driver eye), h = 0.15 m (object)   \u2022   "
                        "adopt the case that satisfies L vs S",
        size=7.4, color=TEA, weight="bold")
    ax.set_xlim(-4.2, 13.2)
    ax.set_ylim(-2.85, 2.0)
    title(ax, "Design of summit curve (simple parabola) \u2014 two cases", y=1.0, size=9.0)
    save(fig, "f2_summit")


def _spiral(R, Ls, psi0=0.0, x0=0.0, y0=0.0, out=False, n=200):
    """Clothoid by numerical integration. out=False: curvature 0 -> 1/R;
    out=True: curvature 1/R -> 0.  Turns left. Returns x, y, end heading."""
    t = np.linspace(0.0, Ls, n)
    if out:
        psi = psi0 + t / R - t ** 2 / (2.0 * R * Ls)
    else:
        psi = psi0 + t ** 2 / (2.0 * R * Ls)
    dt = np.diff(t)
    x = x0 + np.concatenate(([0.0], np.cumsum(np.cos(psi[:-1]) * dt)))
    y = y0 + np.concatenate(([0.0], np.cumsum(np.sin(psi[:-1]) * dt)))
    return x, y, psi[-1]


def f_transition():
    fig, ax = newfig(6.6, 3.3, equal=True)
    R, Ls = 3.2, 2.3
    D = np.radians(60.0)
    Sh = Ls ** 2 / (24.0 * R)
    phis = Ls / (2.0 * R)
    # ---- alignment: T.S. at origin, heading +x --------------------------- #
    ex, ey, p1 = _spiral(R, Ls)
    SC = np.array([ex[-1], ey[-1]])
    line(ax, ex, ey, c=ACC, lw=2.4, z=8)
    O = SC + R * np.array([-np.sin(p1), np.cos(p1)])
    a0 = np.arctan2(SC[1] - O[1], SC[0] - O[0])
    sweep = D - 2 * phis
    aa = np.linspace(a0, a0 + sweep, 220)
    arcx, arcy = O[0] + R * np.cos(aa), O[1] + R * np.sin(aa)
    line(ax, arcx, arcy, c=INK, lw=2.4, z=8)
    CS = np.array([arcx[-1], arcy[-1]])
    ox, oy, p2 = _spiral(R, Ls, psi0=D - phis, x0=CS[0], y0=CS[1], out=True)
    line(ax, ox, oy, c=ACC, lw=2.4, z=8)
    ST = np.array([ox[-1], oy[-1]])
    # ---- straights -------------------------------------------------------- #
    Ix = ST[0] - ST[1] / np.tan(D)
    I = np.array([Ix, 0.0])
    line(ax, [-2.6, Ix], [0.0, 0.0], c=INK, lw=1.6)
    fwd = np.array([np.cos(D), np.sin(D)])
    Fend = ST + 1.5 * fwd
    line(ax, [Ix, Fend[0]], [0.0, Fend[1]], c=INK, lw=1.6)
    line(ax, [Ix, Ix + 2.1], [0, 0], c="#9AA5AE", lw=0.8, ls=(0, (5, 3)))
    ax.add_patch(Circle(I, 0.075, fc=INK, ec="white", lw=0.6, zorder=14))
    lab(ax, Ix + 0.10, -0.34, "I", size=8.4, weight="bold", ha="left")
    ax.add_patch(Arc(I, 1.75, 1.75, theta1=0, theta2=60, lw=0.9, color=TEA, zorder=10))
    lab(ax, Ix + 1.02, 0.40, "\u0394", size=8.6, color=TEA, weight="bold")
    # ---- radius, centre, markers ----------------------------------------- #
    ax.add_patch(Circle(O, 0.065, fc=GREY, ec="none", zorder=12))
    line(ax, [O[0], SC[0]], [O[1], SC[1]], c="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    lab(ax, (O[0] + SC[0]) / 2 - 0.22, (O[1] + SC[1]) / 2 + 0.12, "R", size=7.8, color=GREY)
    lab(ax, O[0] - 0.16, O[1] + 0.30, "O", size=8.0, color=GREY, weight="bold")
    for p, t, dx, dy, ha in [(np.array([0.0, 0.0]), "T.S.", 0.0, -0.36, "center"),
                             (SC, "S.C.", -0.16, 0.34, "right"),
                             (CS, "C.S.", 0.34, -0.10, "left"),
                             (ST, "S.T.", -0.30, 0.16, "right")]:
        ax.add_patch(Circle(p, 0.08, fc=RED, ec="white", lw=0.7, zorder=15))
        lab(ax, p[0] + dx, p[1] + dy, t, size=7.6, color=RED, weight="bold", ha=ha)
    dim(ax, (0.0, -0.62), (SC[0], -0.62), "L\u209b", size=7.4, side="below")
    for p in ([0.0, 0.0], SC):
        extline(ax, (p[0], p[1]), (p[0], -0.66))
    lab(ax, -2.5, 0.22, "straight (back tangent)", size=7.3, ha="left")
    lab(ax, -2.85, -1.60, "Orange = transition (clothoid) curves, in which the radius falls from \u221e to R;   "
                          "Blue = circular curve of radius R",
        size=7.2, ha="left", color="#333333")
    lab(ax, -2.85, -2.10, "T.S. tangent\u2013spiral    S.C. spiral\u2013circle    "
                          "C.S. circle\u2013spiral    S.T. spiral\u2013tangent    "
                          "\u0394 = deflection angle",
        size=7.0, ha="left", color=GREY)
    ax.set_xlim(-2.9, Ix + 3.4)
    ax.set_ylim(-2.5, 4.0)
    title(ax, "Transition curve set out between the straight and the circular curve",
          y=1.0, size=9.0)
    save(fig, "f2_transition")


def f_shift():
    """Shift caused by inserting a transition (exact cubic-parabola geometry,
    vertical scale exaggerated)."""
    fig, ax = newfig(6.2, 2.5)
    R, Ls = 9.0, 4.0
    S = Ls ** 2 / (24.0 * R)
    xb, xe = -Ls / 2, Ls / 2
    yend = -Ls ** 2 / (6.0 * R)
    oc = lambda x: -R + np.sqrt(R ** 2 - np.asarray(x, float) ** 2)
    sc = lambda x: -(R + S) + np.sqrt(R ** 2 - np.asarray(x, float) ** 2)
    line(ax, [-3.5, xb], [0, 0], c=INK, lw=1.9)
    line(ax, [xb, 2.55], [0, 0], c="#9AA5AE", lw=0.9, ls=(0, (6, 3)))
    lab(ax, -3.45, 0.022, "straight", size=7.6, ha="left")
    lab(ax, 1.30, 0.022, "tangent produced", size=6.9, ha="left", color="#7A858E")
    xc = np.linspace(0, 2.48, 200)
    line(ax, xc, oc(xc), c="#8FA6BC", lw=1.6, ls=(0, (5, 3)), z=6)
    line(ax, np.linspace(-1.0, xe, 90), sc(np.linspace(-1.0, xe, 90)),
         c="#7A9AB8", lw=0.9, ls=(0, (1, 2)), z=6)
    line(ax, np.linspace(xe, 2.30, 140), sc(np.linspace(xe, 2.30, 140)),
         c=INK, lw=2.3, z=7)
    u = np.linspace(0, Ls, 220)
    line(ax, xb + u, -u ** 3 / (6.0 * R * Ls), c=ACC, lw=2.5, z=8)
    ax.add_patch(Circle((0, 0), 0.010, fc="#4A6D8C", ec="none", zorder=12))
    lab(ax, 0.0, 0.024, "B", size=7.8, color="#4A6D8C", weight="bold")
    for p, t, dy, ha in [((xb, 0.0), "T.S.", -0.030, "right"),
                         ((xe, yend), "S.C.", -0.032, "center")]:
        ax.add_patch(Circle(p, 0.020, fc=RED, ec="white", lw=0.6, zorder=14))
        lab(ax, p[0] + (-0.06 if ha == "right" else 0), p[1] + dy, t,
            size=7.6, color=RED, weight="bold", ha=ha)
    dim(ax, (0.0, 0.0), (0.0, -S), "", off=0, c=PUR, size=7.0)
    leader(ax, (0.95, -0.028), (0.0, -S * 0.75), "shift  S = L\u209b\u00b2/(24 R)",
           size=7.6, c=PUR, ha="left")
    ax.add_patch(Circle((0, -S / 2), 0.018, fc=ACC, ec="white", lw=0.5, zorder=13))
    leader(ax, (-1.55, -0.098), (0.0, -S / 2),
           "the transition passes\nthrough S/2 at B, i.e. it\nBISECTS the shift",
           size=7.1, c=ACC, ha="right")
    dim(ax, (xb, 0.045), (0.0, 0.045), "L\u209b/2", size=7.2)
    dim(ax, (0.0, 0.045), (xe, 0.045), "L\u209b/2", size=7.2)
    leader(ax, (2.95, -0.140), (2.40, float(oc(2.40))),
           "circular curve of radius R tangent\nto the straight at B (no transition)",
           size=7.0, c="#4A6D8C", ha="left")
    leader(ax, (2.95, -0.330), (2.27, float(sc(2.27))),
           "shifted circular curve,\nsame radius R", size=7.0, c=INK, ha="left")
    lab(ax, -3.45, -0.245, "Total tangent length\n= (R + S) tan(\u0394/2) + L\u209b/2",
        size=7.6, color=ACC, weight="bold", ha="left")
    lab(ax, -3.45, -0.335, "Vertical scale exaggerated;\ndotted = virtual part of the\nshifted circle",
        size=6.9, color=GREY, style="italic", ha="left")
    ax.set_xlim(-3.7, 6.0)
    ax.set_ylim(-0.42, 0.085)
    title(ax, "Shift of the circular curve on inserting a transition curve", y=1.0, size=9.0)
    save(fig, "f2_shift")


def f_valley():
    fig, ax = newfig(6.6, 2.5)
    n1, n2 = -0.24, 0.26
    N = n2 - n1
    L = 5.0
    def yf(x):
        x = np.asarray(x, dtype=float)
        return np.where(np.abs(x) <= L / 2.0,
                        n1 * x + N * (x + L / 2.0) ** 2 / (2.0 * L),
                        np.where(x < 0, n1 * x, n2 * x))
    def yp(x):
        return n1 + N * (x + L / 2.0) / L if abs(x) <= L / 2 else (n1 if x < 0 else n2)
    EXT = 3.5
    line(ax, [-EXT, 0], [n1 * -EXT, 0], c="#8FA6BC", lw=0.9, ls=(0, (5, 3)))
    line(ax, [0, EXT], [0, n2 * EXT], c="#8FA6BC", lw=0.9, ls=(0, (5, 3)))
    xc = np.linspace(-L / 2, L / 2, 240)
    line(ax, xc, yf(xc), c=INK, lw=2.1)
    lab(ax, -EXT + 0.45, n1 * (-EXT + 0.45) + 0.15, "\u2212n\u2081", size=7.8, color=ACC)
    lab(ax, EXT - 0.45, n2 * (EXT - 0.45) + 0.15, "+n\u2082", size=7.8, color=ACC)
    # head-light beam
    xA = -1.85
    h1 = 0.26
    beta = np.radians(6.0)                    # exaggerated for clarity (actual 1 deg)
    yA = float(yf(xA))
    m = yp(xA) + np.tan(beta)
    xs = np.linspace(xA, L / 2 + 0.6, 400)
    beam = yA + h1 + m * (xs - xA)
    road = yf(xs)
    idx = np.where(beam <= road)[0]
    xB = xs[idx[0]] if len(idx) else 1.6
    yB = float(yf(xB))
    wheelveh(ax, xA - 0.42, yA, L=0.85, H=0.20, c=INK)
    line(ax, [xA, xB], [yA + h1, yB], c="#E8A33D", lw=1.6, z=12)
    line(ax, [xA, xA], [yA, yA + h1], c=INK, lw=1.3, z=12)
    xt = np.linspace(xA, xA + 1.55, 40)
    line(ax, xt, yA + h1 + yp(xA) * (xt - xA), c=RED, lw=0.8, ls=(0, (4, 2)), z=11)
    ax.add_patch(Arc((xA, yA + h1), 1.9, 1.9,
                     theta1=np.degrees(np.arctan(yp(xA))),
                     theta2=np.degrees(np.arctan(m)), lw=0.9, color="#8A5E00", zorder=13))
    lab(ax, xA + 1.24, yA + h1 + yp(xA) * 1.24 + 0.10, "\u03b2 = 1\u00b0", size=7.2, color="#8A5E00")
    leader(ax, (xA - 1.45, yA + 0.62), (xA, yA + h1 / 2),
           "h\u2081 = 0.75 m\n(head-light height)", size=7.0, ha="right")
    ax.add_patch(Circle((xB, yB), 0.07, fc=RED, ec="white", lw=0.5, zorder=14))
    lab(ax, xB + 0.16, yB - 0.22, "beam strikes\nthe road surface", size=7.0, color=RED, ha="left")
    dim(ax, (xA, 0.92), (xB, 0.92), "S  (= SSD)", size=7.6)
    dim(ax, (-L / 2, 1.32), (L / 2, 1.32), "L", size=7.6)
    for x in (xA, xB):
        extline(ax, (x, float(yf(x))), (x, 0.96))
    for x in (-L / 2, L / 2):
        extline(ax, (x, float(yf(x))), (x, 1.36))
    ax.add_patch(Circle((0, float(yf(0))), 0.06, fc=RED, ec="none", zorder=13))
    leader(ax, (-0.9, float(yf(0)) - 0.55), (0, float(yf(0))), "lowest point of the curve", size=6.9, c=GREY, ha="right")
    lab(ax, 0, -1.34, "Design for the GREATER of:  (i) comfort  L = 0.38 (N V\u00b3)^\u00bd    "
                      "(ii) head-light SD  L = N S\u00b2/(1.50 + 0.035 S) if L > S",
        size=7.4, color=ACC, weight="bold")
    ax.set_xlim(-4.4, 4.6)
    ax.set_ylim(-1.7, 1.75)
    title(ax, "Valley (sag) curve \u2014 head-light sight distance criterion", y=1.0, size=9.0)
    save(fig, "f2_valley")


def f_curve_types():
    fig, ax = newfig(7.1, 2.0)
    cases = [("+n\u2081 , \u2212n\u2082", 0.26, -0.24, "summit"),
             ("+n\u2081 , +n\u2082\n(n\u2082 < n\u2081)", 0.30, 0.10, "summit"),
             ("\u2212n\u2081 , \u2212n\u2082\n(n\u2082 > n\u2081)", -0.12, -0.30, "summit"),
             ("\u2212n\u2081 , +n\u2082", -0.26, 0.24, "valley"),
             ("\u2212n\u2081 , \u2212n\u2082\n(n\u2082 < n\u2081)", -0.30, -0.10, "valley"),
             ("+n\u2081 , +n\u2082\n(n\u2082 > n\u2081)", 0.12, 0.30, "valley")]
    for k, (t, a, b, kind) in enumerate(cases):
        x0 = k * 3.05
        L = 2.0
        N = a - b
        xs = np.linspace(-L / 2, L / 2, 120)
        ys = a * (xs + L / 2) - N * (xs + L / 2) ** 2 / (2 * L)
        ys = ys - ys.mean()
        line(ax, x0 - 1.55, 0, c="none")
        line(ax, [x0 - 1.55, x0 - L / 2], [a * (-1.55 + L / 2) + ys[0], ys[0]],
             c="#9AA5AE", lw=0.8, ls=(0, (4, 2)))
        line(ax, [x0 + L / 2, x0 + 1.55], [ys[-1], ys[-1] + b * (1.55 - L / 2)],
             c="#9AA5AE", lw=0.8, ls=(0, (4, 2)))
        line(ax, x0 + xs, ys, c=INK if kind == "summit" else TEA, lw=1.8)
        lab(ax, x0, 0.86, t, size=7.2, weight="bold",
            color=INK if kind == "summit" else TEA)
        lab(ax, x0, -0.92, kind.upper(), size=6.9,
            color=INK if kind == "summit" else TEA, style="italic")
    ax.set_xlim(-1.9, 17.4)
    ax.set_ylim(-1.15, 1.25)
    title(ax, "Types of summit and valley curves formed by different grade combinations",
          y=1.0, size=8.8)
    save(fig, "f2_curvetypes")


ALL = [f_shift, f_tresaguet, f_telford, f_macadam, f_star_grid, f_road_class, f_alignment,
       f_surveys, f_xsection_embank, f_xsection_cut, f_camber, f_ssd, f_osd,
       f_setback, f_super, f_widening, f_transition, f_summit, f_valley,
       f_curve_types]

if __name__ == "__main__":
    for f in ALL:
        f()
        print("ok", f.__name__)
