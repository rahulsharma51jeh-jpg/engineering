"""Diagrams for Unit 5 (pavement materials) and Unit 6 (design of pavements)."""
from figbase import *


# =========================================================================== #
# UNIT 5
# =========================================================================== #
def f_cbr():
    fig, ax = axesplot(5.8, 3.0, "penetration  (mm)", "load  (kg)")
    p = np.linspace(0, 12.5, 600)
    with np.errstate(divide="ignore", invalid="ignore"):
        L = 340.0 * (1 - np.exp(-0.40 * p)) * (p ** 1.6) / (p ** 1.6 + 0.55)
    L = np.nan_to_num(L)
    ax.plot(p, L, color=INK, lw=2.1, zorder=6)
    # point of inflexion -> tangent -> corrected origin
    d2 = np.gradient(np.gradient(L, p), p)
    i = int(np.argmax(d2[5:] < 0)) + 5
    m = float(np.gradient(L, p)[i])
    x0 = float(p[i] - L[i] / m)
    ax.plot([x0, 3.7], [0, m * (3.7 - x0)], color=ACC, lw=1.0, ls=(0, (5, 3)), zorder=5)
    ax.scatter([x0], [0], s=24, color=ACC, zorder=8)
    ax.annotate("corrected origin", xy=(x0, 0), xytext=(x0 + 0.75, 42),
                fontsize=6.9, color=ACC,
                arrowprops=dict(arrowstyle="->", color=ACC, lw=0.8))
    ax.annotate("tangent at the point\nof inflexion", xy=(float(p[i]), float(L[i])),
                xytext=(1.35, 250), fontsize=6.8, color=ACC,
                arrowprops=dict(arrowstyle="->", color=ACC, lw=0.8))
    res = {}
    for pen, col, tx in [(2.5, RED, 3.15), (5.0, PUR, 7.05)]:
        pc = x0 + pen
        ld = float(np.interp(pc, p, L))
        res[pen] = ld
        ax.plot([pc, pc], [0, ld], color=col, lw=0.9, ls=(0, (3, 2)))
        ax.plot([0, pc], [ld, ld], color=col, lw=0.9, ls=(0, (3, 2)))
        ax.scatter([pc], [ld], s=22, color=col, zorder=9)
        ax.annotate("corrected %.1f mm\n\u2192 test load %.0f kg" % (pen, ld),
                    xy=(pc, ld), xytext=(tx, 88), fontsize=6.9, color=col,
                    ha="center", arrowprops=dict(arrowstyle="->", color=col, lw=0.7))
    ax.set_xlim(0, 12.0)
    ax.set_ylim(0, 435)
    ax.text(6.35, 176, "Normally CBR at 2.5 mm > CBR at 5.0 mm and the\n"
                       "2.5 mm value is reported. If the 5.0 mm value comes\n"
                       "out greater, the test is repeated; if it repeats, the\n"
                       "5.0 mm value is the one to be reported.",
            fontsize=6.8, color=TEA, va="top")
    ax.text(0.25, 430, "CBR = (test load / standard load) \u00d7 100\n"
                       "standard loads:  1370 kg at 2.5 mm,  2055 kg at 5.0 mm\n"
                       "here CBR$_{2.5}$ = %.0f/1370 = %.1f %%,   "
                       "CBR$_{5.0}$ = %.0f/2055 = %.1f %%"
            % (res[2.5], res[2.5] / 1370 * 100, res[5.0], res[5.0] / 2055 * 100),
            fontsize=6.9, color=INK, va="top", ha="left")
    ax.set_title("Load\u2013penetration curve of the CBR test and its correction",
                 fontsize=9.0, color=INK, fontweight="bold", pad=7)
    save(fig, "f5_cbr")


def f_marshall():
    bc = np.array([4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
    stab = np.array([760, 940, 1080, 1120, 1010, 850])
    flow = np.array([8.0, 9.2, 10.6, 12.4, 14.8, 18.0])
    dens = np.array([2.290, 2.324, 2.348, 2.356, 2.344, 2.320])
    vv = np.array([7.6, 6.1, 4.8, 3.7, 2.8, 2.0])
    vfb = np.array([62, 69, 75, 81, 86, 90])
    sets = [(stab, "Marshall stability (kg)", "peak", RED),
            (flow, "flow value (0.25 mm)", None, INK),
            (dens, "unit weight (g/cc)", "peak", RED),
            (vv, "air voids  V$_v$ (%)", "4%", PUR),
            (vfb, "VFB (%)", None, INK)]
    fig, axs = plt.subplots(1, 5, figsize=(7.15, 1.95))
    obs = []
    for a, (y, ylab, mark, col) in zip(axs, sets):
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
        a.spines["left"].set_color(INK)
        a.spines["bottom"].set_color(INK)
        a.tick_params(colors=INK, labelsize=6.0, width=0.6, length=2.5)
        xs = np.linspace(bc[0], bc[-1], 200)
        ys = np.interp(xs, bc, y)
        cf = np.polyfit(bc, y, 3)
        ys = np.polyval(cf, xs)
        a.plot(xs, ys, color=INK, lw=1.5)
        a.scatter(bc, y, s=9, color=INK, zorder=6)
        a.set_xlabel("bitumen  %", fontsize=6.4, color=INK)
        a.set_ylabel(ylab, fontsize=6.4, color=INK)
        if mark == "peak":
            k = int(np.argmax(ys))
            a.plot([xs[k], xs[k]], [min(ys), ys[k]], color=col, lw=0.8, ls=(0, (3, 2)))
            a.scatter([xs[k]], [ys[k]], s=16, color=col, zorder=8)
            a.set_title("peak at %.2f %%" % xs[k], fontsize=6.4, color=col, pad=3)
            obs.append(xs[k])
        elif mark == "4%":
            k = int(np.argmin(np.abs(ys - 4.0)))
            a.axhline(4.0, color=col, lw=0.8, ls=(0, (3, 2)))
            a.plot([xs[k], xs[k]], [min(ys), 4.0], color=col, lw=0.8, ls=(0, (3, 2)))
            a.scatter([xs[k]], [4.0], s=16, color=col, zorder=8)
            a.set_title("V$_v$=4 %% at %.2f %%" % xs[k], fontsize=6.4, color=col, pad=3)
            obs.append(xs[k])
        else:
            a.set_title(" ", fontsize=6.4, pad=3)
    obc = sum(obs) / len(obs)
    fig.suptitle("Marshall mix design \u2014 the five plots;  "
                 "OBC = mean of (max stability, max unit weight, 4 %% air voids) "
                 "= %.2f %%" % obc,
                 fontsize=8.0, fontweight="bold", color=INK, y=1.06)
    fig.tight_layout()
    save(fig, "f5_marshall")


def f_bittests():
    fig, axs = plt.subplots(1, 3, figsize=(7.15, 2.15))
    for a in axs:
        a.set_axis_off()
    # ---- penetration test ---- #
    a = axs[0]
    a.add_patch(Rectangle((1.0, 0.4), 3.0, 1.7, fc="#4A4A4A", ec=INK, lw=1.0))
    a.add_patch(Rectangle((0.75, 0.15), 3.5, 0.3, fc="#DCE7F2", ec=INK, lw=0.9))
    a.plot([2.5, 2.5], [2.1, 3.9], color=INK, lw=2.4)
    a.add_patch(Rectangle((2.2, 3.9), 0.6, 0.9, fc="#BFBFBF", ec=INK, lw=0.9))
    a.annotate("", xy=(2.5, 2.15), xytext=(2.5, 1.05),
               arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.4, mutation_scale=9))
    a.annotate("", xy=(4.6, 2.1), xytext=(4.6, 1.05),
               arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
    a.text(4.8, 1.55, "penetration\nin 1/10 mm", fontsize=6.6, color=ACC, ha="left")
    a.text(2.5, 5.05, "needle + 100 g weight,\n5 s, 25 \u00b0C", fontsize=6.7,
           color=INK, ha="center")
    a.text(2.5, -0.55, "PENETRATION TEST", fontsize=7.8, fontweight="bold",
           color=INK, ha="center")
    a.text(2.5, -1.05, "Measures HARDNESS / consistency.\n"
                       "Grade 80/100 means the needle\npenetrates 8\u201310 mm.",
           fontsize=6.6, color="#333333", ha="center", va="top")
    a.set_xlim(-0.4, 7.4)
    a.set_ylim(-3.0, 5.9)
    # ---- ductility test ---- #
    a = axs[1]
    a.add_patch(Polygon([(0.6, 2.2), (1.8, 2.2), (1.8, 2.8), (0.6, 2.8)],
                        fc="#4A4A4A", ec=INK, lw=1.0))
    a.add_patch(Polygon([(5.4, 2.2), (4.2, 2.2), (4.2, 2.8), (5.4, 2.8)],
                        fc="#4A4A4A", ec=INK, lw=1.0))
    xs = np.linspace(1.8, 4.2, 100)
    th = 0.30 - 0.22 * np.sin(np.pi * (xs - 1.8) / 2.4)
    a.add_patch(Polygon(list(zip(xs, 2.5 + th)) + list(zip(xs[::-1], (2.5 - th)[::-1])),
                        fc="#4A4A4A", ec=INK, lw=0.9))
    a.annotate("", xy=(5.9, 2.5), xytext=(5.4, 2.5),
               arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.3, mutation_scale=9))
    a.annotate("", xy=(0.1, 2.5), xytext=(0.6, 2.5),
               arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.3, mutation_scale=9))
    a.annotate("", xy=(1.8, 1.35), xytext=(4.2, 1.35),
               arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
    a.text(3.0, 0.95, "elongation at break (cm)", fontsize=6.6, color=ACC, ha="center")
    a.text(3.0, 3.75, "briquette pulled at 50 mm/min,\n27 \u00b0C, in a water bath",
           fontsize=6.7, color=INK, ha="center")
    a.text(3.0, -0.55, "DUCTILITY TEST", fontsize=7.8, fontweight="bold",
           color=INK, ha="center")
    a.text(3.0, -1.05, "Measures the ability to deform\nwithout cracking. IRC minimum\n"
                       "for paving bitumen = 50 cm.",
           fontsize=6.6, color="#333333", ha="center", va="top")
    a.set_xlim(-0.4, 6.4)
    a.set_ylim(-3.0, 4.9)
    # ---- softening point (ring and ball) ---- #
    a = axs[2]
    a.add_patch(Rectangle((0.5, 0.6), 5.0, 3.6, fc="#DCEAF6", ec=INK, lw=1.0))
    a.plot([0.5, 5.5], [3.9, 3.9], color="#4A90C0", lw=0.8)
    a.text(0.6, 4.35, "water / glycerine bath", fontsize=6.3, color="#2A6E9E", ha="left")
    a.add_patch(Rectangle((2.1, 2.5), 1.8, 0.42, fc="#4A4A4A", ec=INK, lw=0.9))
    a.add_patch(Rectangle((1.95, 2.4), 0.18, 0.62, fc="#BFBFBF", ec=INK, lw=0.8))
    a.add_patch(Rectangle((3.87, 2.4), 0.18, 0.62, fc="#BFBFBF", ec=INK, lw=0.8))
    a.add_patch(Circle((3.0, 3.18), 0.26, fc="#8A8A8A", ec=INK, lw=0.9, zorder=8))
    xs = np.linspace(2.1, 3.9, 60)
    sag = 2.5 - 0.55 * np.sin(np.pi * (xs - 2.1) / 1.8)
    a.plot(xs, sag, color="#4A4A4A", lw=2.0, zorder=6)
    a.add_patch(Circle((3.0, 1.72), 0.26, fc="#8A8A8A", ec=INK, lw=0.9,
                       alpha=0.45, zorder=7))
    a.annotate("", xy=(3.0, 1.5), xytext=(3.0, 2.9),
               arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.0, mutation_scale=8))
    a.annotate("", xy=(5.62, 1.46), xytext=(5.62, 2.46),
               arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
    a.text(5.65, 1.96, "25 mm", fontsize=6.4, color=ACC, ha="left")
    a.text(3.0, 4.75, "steel ball 3.5 g on a brass ring;\nbath heated at 5 \u00b0C/min",
           fontsize=6.7, color=INK, ha="center")
    a.text(3.0, -0.55, "SOFTENING POINT (Ring & Ball)", fontsize=7.8,
           fontweight="bold", color=INK, ha="center")
    a.text(3.0, -1.05, "Temperature at which the ball\ntouches the base plate 25 mm\n"
                       "below. Higher value = less\ntemperature susceptibility.",
           fontsize=6.6, color="#333333", ha="center", va="top")
    a.set_xlim(-0.2, 6.2)
    a.set_ylim(-3.0, 5.6)
    fig.suptitle("Standard tests on bituminous binders", fontsize=9.0,
                 fontweight="bold", color=INK, y=1.05)
    fig.tight_layout()
    save(fig, "f5_bittests")


def f_aggtests():
    fig, axs = plt.subplots(1, 3, figsize=(7.15, 2.1))
    for a in axs:
        a.set_axis_off()
    # impact test
    a = axs[0]
    a.add_patch(Rectangle((1.6, 0.3), 2.4, 2.0, fc="#DCE7F2", ec=INK, lw=1.1))
    for _ in range(26):
        x = 1.75 + np.random.rand() * 2.1
        y = 0.45 + np.random.rand() * 1.2
        a.add_patch(Circle((x, y), 0.11, fc="#B9AA92", ec="#6A5A3F", lw=0.5, zorder=5))
    a.plot([2.8, 2.8], [2.3, 5.0], color=INK, lw=1.6)
    a.add_patch(Rectangle((2.25, 2.55), 1.1, 0.75, fc="#8A8A8A", ec=INK, lw=1.0, zorder=6))
    a.annotate("", xy=(2.8, 2.45), xytext=(2.8, 4.55),
               arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.3, mutation_scale=9))
    a.annotate("", xy=(4.35, 2.6), xytext=(4.35, 4.6),
               arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
    a.text(4.5, 3.6, "380 mm\nfree fall\n\u00d7 15 blows", fontsize=6.5, color=ACC, ha="left")
    a.text(2.8, 5.35, "hammer 13.5\u201314 kg", fontsize=6.6, color=INK, ha="center")
    a.text(2.9, -0.35, "AGGREGATE IMPACT VALUE", fontsize=7.6, fontweight="bold",
           color=INK, ha="center")
    a.text(2.9, -0.95, "AIV = (W$_2$/W$_1$)\u00d7100 = % passing\n2.36 mm after the blows.\n"
                       "Toughness \u2014 resistance to\nsudden shock.",
           fontsize=6.5, color="#333333", ha="center", va="top")
    a.set_xlim(-0.3, 6.9)
    a.set_ylim(-3.0, 6.0)
    # LA abrasion
    a = axs[1]
    a.add_patch(Circle((3.0, 2.6), 1.95, fc="#DCE7F2", ec=INK, lw=1.3))
    a.add_patch(Circle((3.0, 2.6), 0.16, fc=INK, ec="none"))
    a.plot([1.05, 4.95], [2.6, 2.6], color="#9AA5AE", lw=0.7, ls=(0, (4, 3)))
    a.add_patch(Rectangle((2.85, 2.6), 0.30, 1.85, fc="#8A8A8A", ec=INK, lw=0.8, zorder=5))
    a.text(3.55, 3.75, "shelf", fontsize=6.3, color=INK, ha="left")
    for _ in range(16):
        ang = np.random.rand() * 2 * np.pi
        r = 1.0 + np.random.rand() * 0.7
        a.add_patch(Circle((3.0 + r * np.cos(ang), 2.6 + r * np.sin(ang) - 0.5),
                           0.12, fc="#B9AA92", ec="#6A5A3F", lw=0.5, zorder=6))
    for _ in range(8):
        ang = np.random.rand() * 2 * np.pi
        r = 1.1 + np.random.rand() * 0.55
        a.add_patch(Circle((3.0 + r * np.cos(ang), 2.6 + r * np.sin(ang) - 0.6),
                           0.19, fc="#8A8A8A", ec=INK, lw=0.6, zorder=7))
    a.add_patch(FancyArrowPatch((4.6, 4.0), (5.3, 2.9), arrowstyle="-|>",
                                mutation_scale=9, color=ACC, lw=1.2,
                                connectionstyle="arc3,rad=0.35"))
    a.text(5.45, 3.6, "30\u201333\nrev/min", fontsize=6.5, color=ACC, ha="left")
    a.text(3.0, 5.0, "abrasive charge = cast-iron spheres", fontsize=6.6,
           color=INK, ha="center")
    a.text(3.0, -0.35, "LOS ANGELES ABRASION", fontsize=7.6, fontweight="bold",
           color=INK, ha="center")
    a.text(3.0, -0.95, "LAA value = % passing 1.7 mm\nafter 500\u20131000 revolutions.\n"
                       "Hardness \u2014 resistance to\nwear by traffic.",
           fontsize=6.5, color="#333333", ha="center", va="top")
    a.set_xlim(-0.3, 7.2)
    a.set_ylim(-3.0, 5.7)
    # crushing test
    a = axs[2]
    a.add_patch(Rectangle((1.7, 0.35), 2.6, 2.3, fc="none", ec=INK, lw=1.4))
    for _ in range(30):
        x = 1.85 + np.random.rand() * 2.3
        y = 0.5 + np.random.rand() * 1.45
        a.add_patch(Circle((x, y), 0.11, fc="#B9AA92", ec="#6A5A3F", lw=0.5, zorder=5))
    a.add_patch(Rectangle((1.75, 1.95), 2.5, 0.42, fc="#8A8A8A", ec=INK, lw=1.0, zorder=6))
    a.add_patch(Rectangle((1.55, 0.1), 2.9, 0.28, fc="#BFBFBF", ec=INK, lw=1.0))
    for xx in (2.35, 3.0, 3.65):
        a.annotate("", xy=(xx, 2.45), xytext=(xx, 3.75),
                   arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.2, mutation_scale=8))
    a.text(3.0, 4.15, "compressive load 40 t\napplied in 10 min", fontsize=6.6,
           color=ACC, ha="center")
    a.text(3.0, -0.35, "AGGREGATE CRUSHING VALUE", fontsize=7.6, fontweight="bold",
           color=INK, ha="center")
    a.text(3.0, -0.95, "ACV = (W$_2$/W$_1$)\u00d7100 = % passing\n2.36 mm. Strength \u2014 "
                       "resistance to\ngradual crushing. \u2264 30 % for\nsurface courses.",
           fontsize=6.5, color="#333333", ha="center", va="top")
    a.set_xlim(-0.3, 6.3)
    a.set_ylim(-3.0, 4.9)
    fig.suptitle("Standard tests on road aggregates", fontsize=9.0,
                 fontweight="bold", color=INK, y=1.04)
    fig.tight_layout()
    save(fig, "f5_aggtests")


def f_gradation():
    fig, ax = axesplot(5.6, 2.7, "sieve size (mm)  \u2014  log scale",
                       "percentage passing")
    s = np.array([0.075, 0.15, 0.3, 0.6, 1.18, 2.36, 4.75, 9.5, 13.2, 19.0, 26.5])
    dense = 100 * (s / 26.5) ** 0.45
    ax.semilogx(s, dense, color=INK, lw=2.0, marker="o", ms=3,
                label="dense / well graded (Fuller: p = 100(d/D)$^{0.45}$)")
    unif = np.array([2, 3, 5, 8, 14, 30, 72, 96, 99, 100, 100])
    ax.semilogx(s, unif, color=ACC, lw=1.7, marker="s", ms=3,
                label="uniformly (poorly) graded \u2014 one size dominates")
    gap = np.array([4, 5, 6, 7, 8, 9, 12, 55, 82, 96, 100])
    ax.semilogx(s, gap, color=PUR, lw=1.7, marker="^", ms=3,
                label="gap graded \u2014 intermediate sizes missing")
    opn = np.array([1, 2, 2, 3, 4, 6, 10, 30, 60, 90, 100])
    ax.semilogx(s, opn, color=TEA, lw=1.5, ls=(0, (5, 2)), marker="v", ms=3,
                label="open graded \u2014 little or no filler")
    ax.legend(fontsize=6.3, loc="upper left", frameon=False)
    ax.set_ylim(0, 105)
    ax.set_xticks([0.075, 0.3, 1.18, 4.75, 13.2, 26.5])
    ax.set_xticklabels(["0.075", "0.3", "1.18", "4.75", "13.2", "26.5"])
    ax.set_title("Aggregate gradation curves", fontsize=9.0, color=INK,
                 fontweight="bold", pad=7)
    save(fig, "f5_gradation")


# =========================================================================== #
# UNIT 6
# =========================================================================== #
def f_flexrigid():
    fig, axs = plt.subplots(1, 2, figsize=(7.15, 2.5))
    for a in axs:
        a.set_axis_off()
        a.set_xlim(-0.4, 10.4)
        a.set_ylim(-4.6, 4.4)
    # ---------- flexible ---------- #
    a = axs[0]
    lay = [("Bituminous surfacing", 0.55, "#4A4A4A", "white"),
           ("Base course", 0.85, "#B4C0CA", INK),
           ("Sub-base course", 0.85, "#CFD8DF", INK)]
    y = 0.0
    for name, t, c, tc in lay:
        a.add_patch(Rectangle((0, y - t), 10, t, fc=c, ec=INK, lw=0.9))
        a.text(5.0, y - t / 2, name, fontsize=6.8, color=tc, ha="center", va="center")
        y -= t
    a.add_patch(Rectangle((0, y - 1.5), 10, 1.5, fc="#E6DAC6", ec=INK, lw=0.9))
    a.text(5.0, y - 0.75, "Prepared subgrade (compacted soil)", fontsize=6.8,
           color=INK, ha="center", va="center")
    ysub = y - 1.5
    a.add_patch(Rectangle((4.1, 0.05), 1.8, 0.5, fc="#8A8A8A", ec=INK, lw=0.9))
    a.text(5.0, 0.85, "wheel load  P", fontsize=7.4, color=INK, ha="center",
           fontweight="bold")
    a.plot([4.1, 1.15], [0.0, ysub], color=ACC, lw=1.0, ls=(0, (4, 2)))
    a.plot([5.9, 8.85], [0.0, ysub], color=ACC, lw=1.0, ls=(0, (4, 2)))
    a.text(2.15, ysub + 0.55, "load spread\nat \u2248 45\u00b0", fontsize=6.4, color=ACC,
           ha="center")
    xs = np.linspace(1.15, 8.85, 120)
    pr = 0.85 * np.cos(np.pi * (xs - 5.0) / 7.7) ** 2
    a.add_patch(Polygon(list(zip(xs, ysub - pr)) + [(8.85, ysub), (1.15, ysub)],
                        fc="#F6CFCF", ec=RED, lw=1.0))
    a.text(5.0, ysub - 1.28, "pressure on the subgrade\n\u2014 LOW but spread over a\n"
                             "small width; each layer\ncarries the load by GRAIN\n"
                             "TO GRAIN transfer",
           fontsize=6.5, color=RED, ha="center", va="top")
    a.set_title("(a)  FLEXIBLE pavement", fontsize=8.4, color=INK,
                fontweight="bold", pad=4)
    # ---------- rigid ---------- #
    a = axs[1]
    a.add_patch(Rectangle((0, -0.95), 10, 0.95, fc="#E4E4E4", ec=INK, lw=1.1))
    a.text(5.0, -0.48, "Cement concrete slab  (M40, flexural strength 4.5 MPa)",
           fontsize=6.8, color=INK, ha="center", va="center")
    a.add_patch(Rectangle((0, -1.65), 10, 0.70, fc="#CFD8DF", ec=INK, lw=0.9))
    a.text(5.0, -1.30, "Granular / DLC sub-base", fontsize=6.8, color=INK,
           ha="center", va="center")
    a.add_patch(Rectangle((0, -3.15), 10, 1.5, fc="#E6DAC6", ec=INK, lw=0.9))
    a.text(5.0, -2.40, "Prepared subgrade", fontsize=6.8, color=INK,
           ha="center", va="center")
    a.add_patch(Rectangle((4.1, 0.05), 1.8, 0.5, fc="#8A8A8A", ec=INK, lw=0.9))
    a.text(5.0, 0.85, "wheel load  P", fontsize=7.4, color=INK, ha="center",
           fontweight="bold")
    xs = np.linspace(0.2, 9.8, 160)
    pr = 0.42 * np.exp(-((xs - 5.0) / 3.4) ** 2)
    a.add_patch(Polygon(list(zip(xs, -3.15 - pr)) + [(9.8, -3.15), (0.2, -3.15)],
                        fc="#F6CFCF", ec=RED, lw=1.0))
    a.plot(xs, -0.95 + 0.10 * np.exp(-((xs - 5.0) / 3.0) ** 2) * -1, color=ACC,
           lw=1.0, ls=(0, (4, 2)))
    a.text(1.5, -0.10, "slab bends as a\nBEAM (flexural\nrigidity)", fontsize=6.4,
           color=ACC, ha="center")
    a.text(5.0, -3.95, "pressure on the subgrade \u2014 VERY LOW and spread over a "
                       "WIDE area;\nthe slab itself carries most of the load in bending",
           fontsize=6.5, color=RED, ha="center", va="top")
    a.set_title("(b)  RIGID pavement", fontsize=8.4, color=INK,
                fontweight="bold", pad=4)
    fig.suptitle("How a flexible and a rigid pavement transmit the wheel load",
                 fontsize=9.0, fontweight="bold", color=INK, y=1.03)
    fig.tight_layout()
    save(fig, "f6_flexrigid")


def f_layers():
    fig, ax = newfig(6.6, 2.85)
    lay = [("Surface course\n(wearing course + binder course)", 0.62, "#4A4A4A", "white",
            "resists abrasion & weather, gives a smooth skid-resistant riding surface, "
            "keeps water out"),
           ("Base course", 0.82, "#B4C0CA", INK,
            "the main load-spreading layer; WBM, WMM, DBM or crushed stone"),
           ("Sub-base course", 0.82, "#CFD8DF", INK,
            "spreads the load further, acts as a drainage & anti-capillary layer, "
            "prevents intrusion of subgrade soil"),
           ("Prepared subgrade (top 500 mm)", 0.72, "#E6DAC6", INK,
            "compacted natural soil; its CBR fixes the total crust thickness"),
           ("Natural soil / embankment", 0.55, "#D8CDB6", INK,
            "in-situ material, not a design layer")]
    y = 0.0
    W = 5.2
    for name, t, c, tc, role in lay:
        rect(ax, 0, y - t, W, t, fc=c, ec=INK, lw=1.0, z=4)
        lab(ax, W / 2, y - t / 2, name, size=7.0, color=tc)
        lab(ax, W + 0.28, y - t / 2, role, size=6.6, ha="left", color="#333333")
        line(ax, [W, W + 0.22], [y - t / 2, y - t / 2], c=GREY, lw=0.5)
        y -= t
    rect(ax, 2.05, 0.06, 1.1, 0.34, fc="#8A8A8A", ec=INK, lw=0.9, z=6)
    lab(ax, 2.6, 0.62, "wheel load", size=7.0, weight="bold")
    dim(ax, (-0.34, -2.26), (-0.34, 0.0), "total\ncrust\nthickness", off=0,
        size=6.8, rot=0)
    extline(ax, (0, -2.26), (-0.42, -2.26))
    extline(ax, (0, 0.0), (-0.42, 0.0))
    lab(ax, 2.6, y - 0.42, "Stress decreases with depth \u21d2 the strongest and most "
                           "expensive material is placed at the TOP",
        size=7.2, color=ACC, weight="bold")
    ax.set_xlim(-1.5, 12.6)
    ax.set_ylim(y - 0.75, 0.95)
    title(ax, "Components of a flexible pavement and the function of each layer",
          y=1.0, size=9.0, x=0.40)
    save(fig, "f6_layers")


def f_eswl():
    fig, ax = plt.subplots(figsize=(5.6, 3.15))
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    P, d, S = 2000.0, 11.0, 33.0
    z1, z2 = d / 2, 2 * S
    ax.plot([P, P], [3.2, z1], color=INK, lw=2.0)
    ax.plot([P, 2 * P], [z1, z2], color=ACC, lw=2.2)
    ax.plot([2 * P, 2 * P], [z2, 280], color=INK, lw=2.0)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.invert_yaxis()
    ax.minorticks_off()
    ax.set_yticks([5, 10, 20, 50, 100, 200])
    ax.set_yticklabels(["5", "10", "20", "50", "100", "200"])
    ax.set_xticks([2000, 2500, 3000, 3500, 4000])
    ax.set_xticklabels(["2000\n(= P)", "2500", "3000", "3500", "4000\n(= 2P)"])
    ax.tick_params(colors=INK, labelsize=6.8, width=0.7, length=3)
    ax.set_xlabel("ESWL  (kg)  \u2014 log scale", fontsize=7.6, color=INK, labelpad=1)
    ax.set_ylabel("depth  z  below the surface (cm)  \u2014 log scale",
                  fontsize=7.6, color=INK, labelpad=2)
    for xv, yv, col in [(P, z1, RED), (2 * P, z2, PUR)]:
        ax.scatter([xv], [yv], s=30, color=col, zorder=10)
        ax.plot([xv, xv], [yv, 3.2], color=col, lw=0.7, ls=(0, (3, 2)))
        ax.plot([1850, xv], [yv, yv], color=col, lw=0.7, ls=(0, (3, 2)))
    ax.annotate("z = d/2  \u21d2  ESWL = P\n(the two wheels act quite\nindependently)",
                xy=(P, z1), xytext=(2130, 3.9), fontsize=6.9, color=RED, va="top",
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))
    ax.annotate("z = 2S  \u21d2  ESWL = 2P\n(the two wheels act as a\nsingle wheel)",
                xy=(2 * P, z2), xytext=(1880, 100), fontsize=6.9, color=PUR,
                va="top", arrowprops=dict(arrowstyle="->", color=PUR, lw=0.8))
    ax.annotate("assumed STRAIGHT on the\nlog\u2013log plot \u2014 interpolate\n"
                "for any intermediate depth",
                xy=(2800, 19.5), xytext=(2900, 8.0), fontsize=6.9, color=ACC,
                ha="left", arrowprops=dict(arrowstyle="->", color=ACC, lw=0.8))
    ax.set_xlim(1850, 4400)
    ax.set_ylim(280, 3.2)
    ax.set_title("Graphical determination of the Equivalent Single Wheel Load (ESWL)",
                 fontsize=8.8, color=INK, fontweight="bold", pad=8)
    ax.text(1880, 180, "P = load on ONE wheel of the dual assembly\n"
                       "d = clear gap between the two tyres\n"
                       "S = centre-to-centre spacing of the two tyres",
            fontsize=6.8, color="#333333", va="top")
    fig.tight_layout()
    save(fig, "f6_eswl")


def f_westergaard():
    fig, ax = newfig(6.6, 2.5, equal=True)
    W, H = 5.2, 3.6
    for k, (dx, name, col, note) in enumerate([
            (0.0, "INTERIOR (centre) loading", TEA, "load well inside the slab"),
            (6.0, "EDGE loading", ACC, "load on the edge, away from a corner"),
            (12.0, "CORNER loading", RED, "load at the corner of the slab")]):
        rect(ax, dx, 0, W, H, fc="#EDEFF1", ec=INK, lw=1.2, z=2)
        if k == 0:
            cx, cy = dx + W / 2, H / 2
        elif k == 1:
            cx, cy = dx + W / 2, 0.0
        else:
            cx, cy = dx + 0.0, 0.0
        ax.add_patch(Circle((cx, cy), 0.42, fc=col, ec="white", lw=1.0,
                            alpha=0.85, zorder=8))
        lab(ax, cx, cy, "P", size=8.4, color="white", weight="bold")
        lab(ax, dx + W / 2, H + 0.42, name, size=7.6, weight="bold", color=col)
        lab(ax, dx + W / 2, -0.62, note, size=6.7, color="#333333")
        if k == 2:
            line(ax, [dx, dx + 2.2], [2.2, 0], c=col, lw=0.9, ls=(0, (4, 2)), z=9)
            lab(ax, dx + 1.55, 1.30, "critical\ncrack", size=6.5, color=col, rot=-45)
    lab(ax, 8.7, -1.55, "Critical stress for a corner load acts at the TOP of the slab; "
                        "for edge and interior loads at the BOTTOM",
        size=7.2, color=INK, weight="bold")
    lab(ax, 8.7, -2.15, "l = radius of relative stiffness = [ E h\u00b3 / (12 (1\u2212\u03bc\u00b2) K) ]"
                        "^\u00bc     b = equivalent radius of the resisting section",
        size=7.2, color=PUR)
    ax.set_xlim(-0.6, 17.8)
    ax.set_ylim(-2.5, 4.5)
    title(ax, "Westergaard's three critical load positions on a rigid pavement slab",
          y=1.0, size=9.0)
    save(fig, "f6_westergaard")


def f_joints():
    fig, ax = newfig(6.9, 3.35)
    # ------------------------------ plan ---------------------------------- #
    x0, y0, LW, LH = 0.0, 5.0, 11.0, 3.6
    rect(ax, x0, y0, LW, LH, fc="#EDEFF1", ec=INK, lw=1.2, z=2)
    line(ax, [x0, x0 + LW], [y0 + LH / 2, y0 + LH / 2], c=PUR, lw=1.8, z=6)
    for xx in (2.6, 5.2, 7.8):
        line(ax, [xx, xx], [y0, y0 + LH], c=TEA, lw=1.5, z=6)
    line(ax, [10.1, 10.1], [y0, y0 + LH], c=RED, lw=2.8, z=6)
    for xx in (2.6, 5.2, 7.8, 10.1):
        for yy in np.linspace(y0 + 0.40, y0 + LH - 0.40, 5):
            line(ax, [xx - 0.32, xx + 0.32], [yy, yy], c=INK, lw=1.1, z=8)
    for xx in np.linspace(0.5, LW - 0.5, 11):
        line(ax, [xx, xx], [y0 + LH / 2 - 0.24, y0 + LH / 2 + 0.24], c=INK, lw=1.0, z=8)
    leader(ax, (11.6, 8.35), (10.1, y0 + LH - 0.45),
           "EXPANSION joint \u2014 20\u201325 mm gap, full\ndepth, compressible filler + sealant,\n"
           "DOWEL bars; spacing 50\u201360 m", size=6.8, ha="left", c=RED)
    leader(ax, (11.6, 6.75), (7.8, y0 + LH - 1.1),
           "CONTRACTION joints \u2014 dummy groove\nof \u2153 depth, DOWEL bars across;\n"
           "spacing = slab length 3.5\u20134.5 m", size=6.8, ha="left", c=TEA)
    leader(ax, (11.6, 5.15), (6.4, y0 + LH / 2),
           "LONGITUDINAL (warping) joint \u2014 TIE\nBARS across. They do NOT transfer\n"
           "load; they only hold the two lanes\ntogether and prevent the joint opening",
           size=6.8, ha="left", c=PUR)
    dim(ax, (0.0, y0 + LH + 0.40), (2.6, y0 + LH + 0.40), "slab length 3.5\u20134.5 m",
        size=6.8)
    lab(ax, 5.5, y0 + LH + 1.02, "PLAN OF A JOINTED PLAIN CONCRETE PAVEMENT",
        size=7.8, weight="bold")
    # --------------------- section of the expansion joint ------------------ #
    sx, sy, SW, SH = 0.0, 0.0, 6.4, 1.5
    gap = 0.32
    rect(ax, sx, sy, SW / 2 - gap / 2, SH, fc="#E4E4E4", ec=INK, lw=1.1, z=4)
    rect(ax, sx + SW / 2 + gap / 2, sy, SW / 2 - gap / 2, SH, fc="#E4E4E4",
         ec=INK, lw=1.1, z=4)
    rect(ax, sx + SW / 2 - gap / 2, sy, gap, SH * 0.74, fc="#C9A227", ec=INK, lw=0.7, z=5)
    rect(ax, sx + SW / 2 - gap / 2, sy + SH * 0.74, gap, SH * 0.26, fc="#4A4A4A",
         ec=INK, lw=0.7, z=5)
    rect(ax, sx, sy - 0.52, SW, 0.52, fc="#CFD8DF", ec=INK, lw=0.9, z=3)
    lab(ax, 1.4, sy - 0.26, "sub-base", size=6.6)
    rect(ax, sx + SW / 2 - 1.40, sy + SH * 0.44, 2.8, 0.16, fc="#8A8A8A", ec=INK,
         lw=0.8, z=9)
    rect(ax, sx + SW / 2 + 0.16, sy + SH * 0.42, 1.24, 0.20, fc="#B9AA92", ec=INK,
         lw=0.6, z=8)
    leader(ax, (6.85, sy + SH * 0.46), (sx + SW / 2 + 1.05, sy + SH * 0.52),
           "DOWEL BAR \u2014 plain round mild-steel bar. Half its length is\n"
           "bonded in one slab; the other half is greased and given an\n"
           "expansion cap so that the slab can move freely. It TRANSFERS\n"
           "the wheel LOAD from one slab to the next.",
           size=6.8, ha="left", c=INK)
    leader(ax, (4.05, sy + SH + 0.52), (sx + SW / 2 + 0.10, sy + SH * 0.90),
           "sealant", size=6.8, ha="left", c=INK)
    leader(ax, (0.30, sy + SH * 0.26), (sx + SW / 2 - 0.20, sy + SH * 0.32),
           "compressible\nfiller board", size=6.8, ha="right", c="#8A6A0B")
    lab(ax, 3.2, sy + SH + 1.05, "SECTION THROUGH AN EXPANSION JOINT",
        size=7.8, weight="bold")
    ax.set_xlim(-2.2, 17.6)
    ax.set_ylim(-1.0, 10.1)
    save(fig, "f6_joints")


def f_warping():
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 2.15))
    for k, a in enumerate(axs):
        a.set_axis_off()
        a.set_xlim(-0.6, 10.6)
        a.set_ylim(-2.5, 3.2)
        xs = np.linspace(0, 10, 200)
        if k == 0:
            shape = -0.42 * np.cos(np.pi * (xs - 5) / 10.0) ** 0 * 0
            shape = -0.42 * (((xs - 5) / 5.0) ** 2 - 0.33)
            ttl = "(a)  DAY  \u2014 top of the slab hotter"
            note = ("Top expands more \u21d2 the slab tries to curl DOWN at the edges.\n"
                    "Its own weight and the subgrade restrain it \u21d2 TENSION at the "
                    "BOTTOM\nat mid-slab; this adds to the load stress at the edge/interior.")
            col = RED
        else:
            shape = 0.42 * (((xs - 5) / 5.0) ** 2 - 0.33)
            ttl = "(b)  NIGHT \u2014 top of the slab cooler"
            note = ("Top contracts \u21d2 the slab tries to curl UP at the edges.\n"
                    "Restraint \u21d2 TENSION at the TOP of the slab; this is critical for "
                    "the\ncorner region, where the corner load stress is also at the top.")
            col = "#1F5FA8"
        a.add_patch(Polygon(list(zip(xs, shape + 0.85)) + list(zip(xs[::-1], (shape)[::-1])),
                            fc="#E4E4E4", ec=INK, lw=1.1))
        a.plot([0, 10], [-0.35, -0.35], color=INK, lw=1.0)
        for xx in np.linspace(0, 9.6, 22):
            a.plot([xx, xx + 0.2], [-0.35, -0.62], color=INK, lw=0.45)
        for xx in (1.2, 5.0, 8.8):
            a.annotate("", xy=(xx, shape[int(xx * 19.9)] - 0.30),
                       xytext=(xx, shape[int(xx * 19.9)] + 1.55),
                       arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0,
                                       mutation_scale=7))
        a.text(5.0, 2.72, ttl, fontsize=7.8, fontweight="bold", color=col, ha="center")
        a.text(5.0, 2.28, "self weight + subgrade restraint", fontsize=6.4,
               color=col, ha="center")
        a.text(5.0, -1.15, note, fontsize=6.5, color="#333333", ha="center", va="top")
    fig.suptitle("Warping (curling) stresses in a cement concrete slab caused by "
                 "the temperature gradient",
                 fontsize=8.8, fontweight="bold", color=INK, y=1.04)
    fig.tight_layout()
    save(fig, "f6_warping")


def f_designchart():
    fig, ax = axesplot(5.6, 2.9, "Subgrade CBR  (%)", "Total pavement thickness  (mm)")
    cbr = np.linspace(2, 15, 200)
    for msa, col, lsy in [(1, "#8FA6BC", (0, (5, 2))), (5, TEA, "-"),
                          (10, ACC, "-"), (30, PUR, "-"), (50, RED, "-")]:
        t = (330 + 145 * np.log(msa + 1)) * (2.0 / cbr) ** 0.32
        ax.plot(cbr, t, color=col, lw=1.7, ls=lsy, label="%d msa" % msa)
    ax.legend(fontsize=6.6, title="design traffic", title_fontsize=6.6,
              frameon=False, loc="upper right")
    ax.set_xlim(2, 15)
    ax.set_ylim(200, 1000)
    ax.set_title("Shape of the IRC 37 flexible-pavement design curves (schematic)",
                 fontsize=8.8, color=INK, fontweight="bold", pad=7)
    ax.text(2.15, 960, "Enter with the design CBR and the cumulative standard axles "
                       "(msa);\nread the total crust thickness and the composition "
                       "of each layer.",
            fontsize=6.7, color="#333333", va="top")
    save(fig, "f6_designchart")


ALL = [f_cbr, f_marshall, f_bittests, f_aggtests, f_gradation,
       f_flexrigid, f_layers, f_eswl, f_westergaard, f_joints, f_warping,
       f_designchart]

if __name__ == "__main__":
    np.random.seed(7)
    for f in ALL:
        f()
        print("ok", f.__name__)
