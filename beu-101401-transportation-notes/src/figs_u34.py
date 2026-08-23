"""Diagrams for Unit 3 (traffic engineering) and Unit 4 (regulation, intersections,
parking, lighting)."""
from figbase import *


# =========================================================================== #
# UNIT 3
# =========================================================================== #
def f_piev():
    fig, ax = newfig(6.9, 2.15)
    segs = [("Perception", "P", "#DCE7F2",
             "the driver SEES the object \u2014 the stimulus reaches the brain through the eye"),
            ("Intellection", "I", "#CBDDEE",
             "he UNDERSTANDS the stimulus and correlates it with his earlier experience"),
            ("Emotion", "E", "#E3F0EE",
             "he DECIDES what to do \u2014 fear, anger, superstition and judgement all act here"),
            ("Volition", "V", "#FBEDE5",
             "he ACTS \u2014 the muscular movement of actually applying the brake")]
    W, H = 2.7, 0.95
    for i, (name, ltr, c, _d) in enumerate(segs):
        x = i * W
        rect(ax, x, 0, W, H, fc=c, ec=INK, lw=0.9, z=4)
        lab(ax, x + W / 2, H * 0.70, name, size=8.6, weight="bold")
        lab(ax, x + W / 2, H * 0.26, ltr, size=13.5, weight="bold", color=ACC)
    tot = 4 * W
    dim(ax, (0, H + 0.42), (tot, H + 0.42),
        "total reaction time  t   (IRC design value t = 2.5 s for SSD)", size=7.8)
    for xx in (0, tot):
        extline(ax, (xx, H), (xx, H + 0.48))
    arr(ax, (-1.25, H / 2), (-0.08, H / 2), c=ACC, lw=1.2, ms=9)
    lab(ax, -1.33, H / 2, "stimulus\n(object on\nthe road)", size=7.0, ha="right", color=ACC)
    arr(ax, (tot + 0.08, H / 2), (tot + 1.25, H / 2), c=ACC, lw=1.2, ms=9)
    lab(ax, tot + 1.33, H / 2, "response\n(brakes\napplied)", size=7.0, ha="left", color=ACC)
    for i, (name, ltr, c, d) in enumerate(segs):
        yy = -0.42 - i * 0.36
        lab(ax, -2.6, yy, "%s" % ltr, size=8.4, weight="bold", color=ACC, ha="left")
        lab(ax, -2.15, yy, "%s \u2014 %s" % (name, d), size=7.1, ha="left", color="#333333")
    lab(ax, -2.6, -2.12, "Lag (reaction) distance = 0.278 V t  \u2014  the vehicle covers this "
                         "distance BEFORE the brakes are applied",
        size=7.6, color=TEA, weight="bold", ha="left")
    ax.set_xlim(-2.9, tot + 3.1)
    ax.set_ylim(-2.4, H + 0.8)
    title(ax, "PIEV theory \u2014 the four components of driver reaction time",
          y=1.0, size=9.0, x=0.44)
    save(fig, "f3_piev")


def f_flow():
    vf, kj = 60.0, 120.0                      # free speed km/h, jam density veh/km
    fig, axs = plt.subplots(1, 3, figsize=(7.15, 2.35))
    k = np.linspace(0, kj, 300)
    v = vf * (1 - k / kj)
    q = k * v
    qmax, k0, v0 = vf * kj / 4.0, kj / 2.0, vf / 2.0
    for a in axs:
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
        a.spines["left"].set_color(INK)
        a.spines["bottom"].set_color(INK)
        a.tick_params(colors=INK, labelsize=6.6, width=0.7, length=3)
    # (a) speed vs density
    a = axs[0]
    a.plot(k, v, color=INK, lw=1.8)
    a.plot([0, k0], [v0, v0], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.plot([k0, k0], [0, v0], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.scatter([k0], [v0], s=16, color=RED, zorder=6)
    a.set_xlabel("density  k  (veh/km)", fontsize=7.2, color=INK)
    a.set_ylabel("speed  v  (km/h)", fontsize=7.2, color=INK)
    a.set_title("(a)  v = v$_f$ (1 \u2212 k/k$_j$)", fontsize=7.8, color=INK, pad=5)
    a.annotate("v$_f$", xy=(0, vf), xytext=(3, vf + 1.5), fontsize=7.4, color=ACC)
    a.annotate("k$_j$", xy=(kj, 0), xytext=(kj - 6, 4.5), fontsize=7.4, color=ACC)
    a.annotate("v$_o$= v$_f$/2", xy=(0, v0), xytext=(4, v0 + 3), fontsize=6.8, color=ACC)
    a.annotate("k$_o$= k$_j$/2", xy=(k0, 0), xytext=(k0 - 22, 3.5), fontsize=6.8, color=ACC)
    # (b) flow vs density
    a = axs[1]
    a.plot(k, q, color=INK, lw=1.8)
    a.plot([0, k0], [qmax, qmax], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.plot([k0, k0], [0, qmax], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.scatter([k0], [qmax], s=18, color=RED, zorder=6)
    a.set_xlabel("density  k  (veh/km)", fontsize=7.2, color=INK)
    a.set_ylabel("flow  q  (veh/h)", fontsize=7.2, color=INK)
    a.set_title("(b)  q = k v = v$_f$(k \u2212 k\u00b2/k$_j$)", fontsize=7.8, color=INK, pad=5)
    a.annotate("q$_{max}$ = v$_f$k$_j$/4", xy=(k0, qmax), xytext=(6, qmax + 60),
               fontsize=6.9, color=RED)
    a.annotate("free-flow\n(uncongested)", xy=(28, 1300), xytext=(6, 300),
               fontsize=6.4, color=GRN)
    a.annotate("congested", xy=(92, 1300), xytext=(70, 300), fontsize=6.4, color=RED)
    a.set_ylim(0, qmax * 1.32)
    # (c) speed vs flow
    a = axs[2]
    a.plot(q, v, color=INK, lw=1.8)
    a.plot([0, qmax], [v0, v0], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.plot([qmax, qmax], [0, v0], color=ACC, lw=0.7, ls=(0, (3, 2)))
    a.scatter([qmax], [v0], s=18, color=RED, zorder=6)
    a.set_xlabel("flow  q  (veh/h)", fontsize=7.2, color=INK)
    a.set_ylabel("speed  v  (km/h)", fontsize=7.2, color=INK)
    a.set_title("(c)  speed\u2013flow curve", fontsize=7.8, color=INK, pad=5)
    a.annotate("q$_{max}$ = capacity", xy=(qmax, v0), xytext=(qmax * 0.16, v0 + 6),
               fontsize=6.9, color=RED)
    a.annotate("upper (free) branch", xy=(1200, 45), xytext=(150, 52),
               fontsize=6.4, color=GRN)
    a.annotate("lower (forced) branch", xy=(1200, 12), xytext=(60, 6),
               fontsize=6.4, color=RED)
    fig.suptitle("Fundamental diagrams of traffic flow (Greenshields' linear model)",
                 fontsize=9.0, fontweight="bold", color=INK, y=1.05)
    fig.tight_layout()
    save(fig, "f3_flow")


def f_spotspeed():
    mids = np.array([17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5])
    freq = np.array([12, 18, 35, 62, 88, 76, 48, 30, 15, 6])
    fig, axs = plt.subplots(1, 2, figsize=(7.15, 2.6))
    for a in axs:
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
        a.spines["left"].set_color(INK)
        a.spines["bottom"].set_color(INK)
        a.tick_params(colors=INK, labelsize=6.8, width=0.7, length=3)
    a = axs[0]
    a.bar(mids, freq, width=4.4, color="#CBDDEE", edgecolor=INK, lw=0.7)
    a.plot(mids, freq, color=ACC, lw=1.6, marker="o", ms=3)
    a.set_xlabel("speed (km/h)", fontsize=7.4, color=INK)
    a.set_ylabel("frequency  (no. of vehicles)", fontsize=7.4, color=INK)
    a.set_title("(a)  Frequency distribution curve", fontsize=8.0, color=INK, pad=5)
    im = int(np.argmax(freq))
    a.annotate("modal speed\n(most frequent)", xy=(mids[im], freq[im]),
               xytext=(mids[im] + 8.5, freq[im] - 14), fontsize=6.8, color=RED,
               arrowprops=dict(arrowstyle="->", color=RED, lw=0.7))
    upper = mids + 2.5
    cum = np.cumsum(freq) / freq.sum() * 100.0
    a = axs[1]
    a.plot(np.concatenate(([15], upper)), np.concatenate(([0], cum)),
           color=INK, lw=1.8, marker="o", ms=3)
    for pc, name, col, ty in [(15, "15th percentile \u2192\nlower speed limit", GRN, 9),
                              (50, "50th percentile \u2192\nmedian speed", "#4A6D8C", 40),
                              (85, "85th percentile \u2192\nSAFE SPEED LIMIT", RED, 68),
                              (98, "98th percentile \u2192\ngeometric design speed", PUR, 95)]:
        sp = float(np.interp(pc, cum, upper))
        a.plot([15, sp], [pc, pc], color=col, lw=0.8, ls=(0, (3, 2)))
        a.plot([sp, sp], [0, pc], color=col, lw=0.8, ls=(0, (3, 2)))
        a.scatter([sp], [pc], s=20, color=col, zorder=6)
        a.annotate(name, xy=(sp, pc), xytext=(16.2, ty), fontsize=6.4, color=col,
                   va="center", arrowprops=dict(arrowstyle="->", color=col, lw=0.6,
                                                shrinkA=3, shrinkB=2))
    a.set_xlabel("speed (km/h)", fontsize=7.4, color=INK)
    a.set_ylabel("cumulative percentage of vehicles", fontsize=7.4, color=INK)
    a.set_title("(b)  Cumulative frequency (S-) curve", fontsize=8.0, color=INK, pad=5)
    a.set_ylim(0, 105)
    fig.suptitle("Presentation of spot-speed study data", fontsize=9.0,
                 fontweight="bold", color=INK, y=1.04)
    fig.tight_layout()
    save(fig, "f3_spotspeed")


def f_movingobs():
    fig, ax = newfig(6.9, 2.9)
    RH = 1.15
    for k, (ttl, note) in enumerate([
            ("Run 1 \u2014 test vehicle driven AGAINST the stream",
             "count  n\u2090 = number of vehicles MET (coming towards the observer)"),
            ("Run 2 \u2014 test vehicle driven WITH the stream",
             "count  n\u1d67 = vehicles that OVERTAKE the test vehicle ;   "
             "n\u2092 = vehicles OVERTAKEN by the test vehicle")]):
        y = 4.35 if k == 0 else 0.60
        rect(ax, 0, y, 11.4, RH, fc="#F3F7FB", ec=INK, lw=0.9, z=2)
        line(ax, [0, 11.4], [y + RH / 2, y + RH / 2], c="#C9A227", lw=0.8, ls=(0, (7, 5)))
        lab(ax, 0.0, y + RH + 0.42, "%s  \u2014  run time  t%s"
            % (ttl, "\u2090" if k == 0 else "\u1d69"),
            size=8.4, weight="bold", ha="left")
        lab(ax, 0.0, y - 0.52, note, size=7.1, ha="left", color="#333333")
        yl, yu = y + 0.28, y + RH - 0.28
        if k == 0:
            for x in (0.6, 2.1, 3.6, 5.1, 6.6):
                car(ax, x, yu, L=0.85, H=0.30, c=INK, fc="#DDE7F1", dirn=1)
            car(ax, 9.9, yl, L=1.0, H=0.34, c=RED, fc="#FBE3E3", dirn=-1)
            lab(ax, 8.55, yl, "test vehicle", size=6.9, color=RED, ha="right")
            arr(ax, (7.7, yu), (8.9, yu), c=INK, lw=1.0, ms=8)
            lab(ax, 10.1, yu, "stream", size=6.9, color=INK, ha="center")
        else:
            car(ax, 2.6, yl, L=1.0, H=0.34, c=RED, fc="#FBE3E3", dirn=1)
            lab(ax, 5.0, yl, "test vehicle", size=6.9, color=RED, ha="left")
            for x, tg, cc, fcc in [(1.0, "n\u2092", PUR, "#F2E9F5"),
                                   (4.8, "n\u1d67", GRN, "#E4F1E8"),
                                   (6.5, "n\u1d67", GRN, "#E4F1E8"),
                                   (8.2, "n\u1d67", GRN, "#E4F1E8")]:
                car(ax, x, yu, L=0.85, H=0.30, c=cc, fc=fcc, dirn=1)
                lab(ax, x - 0.12, yu, tg, size=7.0, color=cc, weight="bold", ha="right")
            arr(ax, (9.9, yl), (11.0, yl), c=INK, lw=1.0, ms=8)
            lab(ax, 10.45, yl + 0.40, "stream direction", size=6.6, color=INK)
    lab(ax, 0.0, 6.62, "Both runs are made over the SAME stretch of length L (in opposite directions)",
        size=7.2, ha="left", color=TEA, style="italic")
    rect(ax, 0, -2.15, 11.4, 1.35, fc="#E8F0F9", ec="#1B5E9E", lw=0.9, z=2)
    lab(ax, 5.7, -1.15, "q = (n\u2090 + n\u1d67 \u2212 n\u2092) / (t\u2090 + t\u1d69)"
                        "          t\u0304 = t\u1d69 \u2212 (n\u1d67 \u2212 n\u2092)/q"
                        "          v\u0304 = L / t\u0304",
        size=9.2, weight="bold", color="#12335C")
    lab(ax, 5.7, -1.82, "q = flow of the stream (veh/h)  \u2022  t\u0304 = mean travel time  \u2022  "
                        "v\u0304 = space mean speed of the stream", size=7.0, color="#333333")
    ax.set_xlim(-0.35, 11.75)
    ax.set_ylim(-2.5, 7.0)
    title(ax, "Moving-observer method of measuring traffic volume and speed", y=1.0, size=9.0)
    save(fig, "f3_movingobs")


def f_collision():
    fig, axs = plt.subplots(1, 2, figsize=(7.15, 2.75))
    for a in axs:
        a.set_axis_off()
        a.set_aspect("equal")
    # ---------- collision diagram ---------- #
    a = axs[0]
    a.add_patch(Rectangle((-0.65, -4.2), 1.3, 8.4, fc="#F1F4F7", ec=INK, lw=1.0))
    a.add_patch(Rectangle((-4.2, -0.65), 8.4, 1.3, fc="#F1F4F7", ec=INK, lw=1.0))
    a.plot([0, 0], [-4.2, 4.2], color="#C9A227", lw=0.7, ls=(0, (5, 4)))
    a.plot([-4.2, 4.2], [0, 0], color="#C9A227", lw=0.7, ls=(0, (5, 4)))
    def cw(p1, p2, c, ls="-"):
        a.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=7,
                                    color=c, lw=1.1, ls=ls, shrinkA=0, shrinkB=0,
                                    zorder=8))
    # rear-end
    cw((-3.6, 0.32), (-2.3, 0.32), INK)
    cw((-2.9, 0.32), (-1.9, 0.32), INK)
    a.text(-2.75, 0.95, "rear-end", fontsize=6.4, color=INK, ha="center")
    # right-angle
    cw((0.32, -3.4), (0.32, -0.3), INK)
    cw((3.4, -0.32), (0.3, -0.32), INK)
    a.scatter([0.32], [-0.32], marker="X", s=44, color=RED, zorder=12)
    a.text(2.45, -1.75, "right-angle\ncollision", fontsize=6.4, color=RED, ha="center")
    # head-on
    cw((-0.32, 3.5), (-0.32, 1.1), INK)
    cw((-0.32, 0.9), (-0.32, 2.6), INK, ls=(0, (2, 1)))
    a.scatter([-0.32], [1.6], marker="X", s=44, color=RED, zorder=12)
    a.text(-1.85, 1.65, "head-on", fontsize=6.4, color=RED, ha="center")
    # pedestrian
    a.scatter([2.1], [0.36], marker="o", s=26, facecolor="white", edgecolor=PUR,
              lw=1.0, zorder=12)
    cw((3.5, 0.36), (2.3, 0.36), INK)
    a.text(2.35, 1.05, "pedestrian\nknocked down", fontsize=6.4, color=PUR, ha="center")
    # side-swipe / overturn symbol
    a.scatter([-0.32], [-2.6], marker="s", s=34, color="#8A6A0B", zorder=12)
    a.annotate("collision with a\nparked vehicle", xy=(-0.32, -2.6), xytext=(-4.4, -2.9),
               fontsize=6.4, color="#8A6A0B", ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color="#8A6A0B", lw=0.6))
    a.text(0, 4.85, "(a)  COLLISION DIAGRAM", fontsize=8.2, fontweight="bold",
           color=INK, ha="center")
    a.text(0, -5.0, "Shows the MANNER of each accident: path of every\n"
                    "vehicle/pedestrian, type of collision, date, time,\n"
                    "severity (\u2715 = injury/fatality). Not to scale.",
           fontsize=6.6, color="#333333", ha="center")
    a.set_xlim(-4.6, 4.6)
    a.set_ylim(-5.9, 5.3)
    # ---------- condition diagram ---------- #
    a = axs[1]
    a.add_patch(Rectangle((-0.65, -4.2), 1.3, 8.4, fc="#F1F4F7", ec=INK, lw=1.0))
    a.add_patch(Rectangle((-4.2, -0.65), 8.4, 1.3, fc="#F1F4F7", ec=INK, lw=1.0))
    a.plot([0, 0], [-4.2, 4.2], color="#C9A227", lw=0.7, ls=(0, (5, 4)))
    a.plot([-4.2, 4.2], [0, 0], color="#C9A227", lw=0.7, ls=(0, (5, 4)))
    for (x, y) in [(-1.45, 1.45), (-1.45, -1.45), (1.45, -1.45)]:
        a.add_patch(Circle((x, y), 0.30, fc="#CFE3D5", ec=GRN, lw=0.8, zorder=6))
    a.annotate("trees at the corners", xy=(-1.45, 1.45), xytext=(-4.5, 3.15),
               fontsize=6.4, color=GRN, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=GRN, lw=0.6))
    a.add_patch(Rectangle((0.95, 0.95), 1.65, 1.65, fc="#DCD3C4", ec="#7A6A4F",
                          lw=0.8, zorder=5))
    a.text(1.78, 1.78, "building", fontsize=6.3, color="#5A4A2F", ha="center")
    a.plot([-3.55, -3.55], [0.75, 1.55], color=INK, lw=1.4)
    a.add_patch(Rectangle((-3.80, 1.55), 0.50, 0.40, fc="#FFF6E0", ec=INK, lw=0.8))
    a.annotate("warning sign", xy=(-3.55, 1.75), xytext=(-4.5, -2.35),
               fontsize=6.4, color=INK, ha="left", va="center",
               arrowprops=dict(arrowstyle="-", color=INK, lw=0.6))
    a.plot([-0.65, -0.65, -3.2, -0.65], [3.2, 0.65, 0.65, 3.2], color=PUR,
           lw=0.8, ls=(0, (4, 2)), zorder=7)
    a.text(-1.72, 1.18, "sight\ntriangle", fontsize=6.4, color=PUR, ha="center")
    a.annotate("", xy=(-3.95, -0.65), xytext=(-3.95, 0.65),
               arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
    a.text(-4.15, 0.0, "7.0 m", fontsize=6.3, color=ACC, ha="right", va="center")
    a.text(0, 4.85, "(b)  CONDITION DIAGRAM", fontsize=8.2, fontweight="bold",
           color=INK, ha="center")
    a.text(0, -5.0, "Drawn TO SCALE: road widths, kerbs, islands, signs,\n"
                    "signals, trees, buildings, drains, surface type \u2014 i.e.\n"
                    "the physical conditions at the accident site.",
           fontsize=6.6, color="#333333", ha="center")
    a.set_xlim(-4.6, 4.6)
    a.set_ylim(-5.9, 5.3)
    fig.suptitle("Accident study \u2014 collision and condition diagrams",
                 fontsize=9.0, fontweight="bold", color=INK, y=1.0)
    fig.tight_layout()
    save(fig, "f3_collision")


def f_los():
    fig, ax = axesplot(6.2, 2.7, "flow / capacity ratio  (v/c)", "operating speed  \u2192")
    v = np.linspace(0, 1.0, 300)
    s = 100 * (1 - 0.55 * v ** 3.2)
    ax.plot(v, s, color=INK, lw=2.0)
    bands = [(0.0, 0.20, "A", "#DFF0E2", "free flow"),
             (0.20, 0.38, "B", "#EAF3DC", "reasonably free"),
             (0.38, 0.55, "C", "#FBF6DC", "stable, restricted"),
             (0.55, 0.75, "D", "#FCEBDA", "approaching unstable"),
             (0.75, 0.92, "E", "#F9DEDA", "at capacity, unstable"),
             (0.92, 1.00, "F", "#EFD6E6", "forced / breakdown")]
    for x1, x2, n, c, d in bands:
        ax.axvspan(x1, x2, color=c, zorder=0)
        ax.text((x1 + x2) / 2, 104, n, ha="center", fontsize=9.0,
                fontweight="bold", color=INK)
        ax.text((x1 + x2) / 2, 56, d, ha="center", va="center", fontsize=5.8,
                color="#444444", rotation=90)
    ax.set_ylim(20, 112)
    ax.set_xlim(0, 1.0)
    ax.set_yticks([])
    ax.text(0.5, 116, "LEVEL OF SERVICE", ha="center", fontsize=7.6,
            fontweight="bold", color=INK)
    ax.annotate("capacity reached\n(LOS E \u2192 F)", xy=(0.95, float(100 * (1 - 0.55 * 0.95 ** 3.2))),
                xytext=(0.60, 46), fontsize=6.8, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))
    save(fig, "f3_los")


# =========================================================================== #
# UNIT 4
# =========================================================================== #
def f_signs():
    fig, ax = newfig(6.9, 1.85, equal=True)
    # mandatory / regulatory : circular
    ax.add_patch(Circle((1.0, 0.9), 0.66, fc="white", ec=RED, lw=3.0, zorder=5))
    lab(ax, 1.0, 0.9, "50", size=13.0, weight="bold")
    ax.add_patch(Circle((2.55, 0.9), 0.66, fc="#1F5FA8", ec="#1F5FA8", lw=1.0, zorder=5))
    arr(ax, (2.55, 0.55), (2.55, 1.25), c="white", lw=2.2, ms=11, z=8)
    lab(ax, 1.78, -0.30, "MANDATORY / REGULATORY\ncircular \u2014 must be obeyed;\n"
                         "violation is an offence\n(speed limit, no entry, one way, STOP)",
        size=6.9, color=INK)
    # cautionary / warning : triangular
    tri = [(5.0, 1.62), (4.30, 0.36), (5.70, 0.36)]
    poly(ax, tri, fc="white", ec=RED, lw=2.6, z=5)
    line(ax, [4.85, 5.0, 5.18, 5.05], [0.60, 0.95, 1.05, 1.28], c=INK, lw=1.4, z=8)
    poly(ax, [(6.55, 1.62), (5.85, 0.36), (7.25, 0.36)], fc="white", ec=RED, lw=2.6, z=5)
    lab(ax, 6.55, 0.86, "\u26a0", size=13.0)
    lab(ax, 5.78, -0.30, "CAUTIONARY / WARNING\nequilateral triangle, apex up \u2014\n"
                         "warns of a hazard ahead\n(curve, cross road, narrow bridge)",
        size=6.9, color=INK)
    # informatory : rectangular
    rect(ax, 8.6, 0.42, 1.75, 0.98, fc="#1F5FA8", ec=INK, lw=1.0, z=5)
    lab(ax, 9.48, 0.91, "HOSPITAL", size=8.0, color="white", weight="bold")
    rect(ax, 10.6, 0.42, 1.55, 0.98, fc="#2E7D32", ec=INK, lw=1.0, z=5)
    lab(ax, 11.38, 1.06, "PATNA", size=7.6, color="white", weight="bold")
    lab(ax, 11.38, 0.68, "18 km", size=6.8, color="white")
    lab(ax, 10.4, -0.30, "INFORMATORY / GUIDE\nrectangular \u2014 gives information\n"
                         "on route, destination, distance,\nfacilities, parking",
        size=6.9, color=INK)
    ax.set_xlim(0.05, 12.6)
    ax.set_ylim(-1.15, 2.05)
    title(ax, "Classification of traffic signs (IRC 67) \u2014 shape identifies the class",
          y=1.0, size=9.0)
    save(fig, "f3_signs" if False else "f4_signs")


def _xnode(ax, cx, cy, s=1.0, w=0.34):
    poly(ax, [(cx - w, cy - s), (cx + w, cy - s), (cx + w, cy + s), (cx - w, cy + s)],
         fc="#F1F4F7", ec=INK, lw=0.8, z=2)
    poly(ax, [(cx - s, cy - w), (cx + s, cy - w), (cx + s, cy + w), (cx - s, cy + w)],
         fc="#F1F4F7", ec=INK, lw=0.8, z=2)


def f_signalphase():
    fig, ax = newfig(6.9, 2.6)
    def ph(cx, cy, moves, ttl, s=0.95):
        _xnode(ax, cx, cy, s=s)
        for m in moves:
            if m == "N":
                arr(ax, (cx + 0.14, cy - s), (cx + 0.14, cy + s), c=GRN, lw=1.3, ms=8)
            elif m == "S":
                arr(ax, (cx - 0.14, cy + s), (cx - 0.14, cy - s), c=GRN, lw=1.3, ms=8)
            elif m == "E":
                arr(ax, (cx - s, cy - 0.14), (cx + s, cy - 0.14), c=GRN, lw=1.3, ms=8)
            elif m == "W":
                arr(ax, (cx + s, cy + 0.14), (cx - s, cy + 0.14), c=GRN, lw=1.3, ms=8)
            elif m == "NR":       # right turn from south approach
                arr(ax, (cx + 0.14, cy - s), (cx - s, cy + 0.30), c=ACC, lw=1.2,
                    ms=8, conn="arc3,rad=-0.35")
            elif m == "SR":
                arr(ax, (cx - 0.14, cy + s), (cx + s, cy - 0.30), c=ACC, lw=1.2,
                    ms=8, conn="arc3,rad=-0.35")
            elif m == "ER":
                arr(ax, (cx - s, cy - 0.14), (cx - 0.30, cy + s), c=ACC, lw=1.2,
                    ms=8, conn="arc3,rad=-0.35")
            elif m == "WR":
                arr(ax, (cx + s, cy + 0.14), (cx + 0.30, cy - s), c=ACC, lw=1.2,
                    ms=8, conn="arc3,rad=-0.35")
        lab(ax, cx, cy - s - 0.52, ttl, size=7.4, weight="bold")
    lab(ax, 2.6, 3.35, "TWO-PHASE SYSTEM", size=8.4, weight="bold", color=INK)
    ph(1.15, 1.85, ["N", "S"], "Phase 1\nN\u2013S through + left")
    ph(4.05, 1.85, ["E", "W"], "Phase 2\nE\u2013W through + left")
    lab(ax, 2.6, -0.12, "suitable only when the right-turning\nvolumes are small",
        size=6.9, color=GREY, style="italic")
    lab(ax, 10.35, 3.35, "FOUR-PHASE SYSTEM", size=8.4, weight="bold", color=INK)
    ph(7.35, 1.85, ["N", "NR"], "Phase 1\nS leg", s=0.80)
    ph(9.35, 1.85, ["E", "ER"], "Phase 2\nW leg", s=0.80)
    ph(11.35, 1.85, ["S", "SR"], "Phase 3\nN leg", s=0.80)
    ph(13.35, 1.85, ["W", "WR"], "Phase 4\nE leg", s=0.80)
    lab(ax, 10.35, -0.12, "one approach discharges at a time \u2014 no conflict at all,\n"
                          "but the cycle time becomes long",
        size=6.9, color=GREY, style="italic")
    line(ax, [5.95, 5.95], [-0.95, 3.5], c="#BFBFBF", lw=0.8, ls=(0, (4, 3)))
    lab(ax, 0.2, -1.45, "\u2192 green (through / left)          \u2192 green (right turn)          "
                        "Cycle time = \u03a3 (green + amber + all-red) of every phase",
        size=7.0, ha="left", color="#333333")
    line(ax, [0.24, 0.62], [-1.30, -1.30], c=GRN, lw=1.4)
    line(ax, [3.30, 3.68], [-1.30, -1.30], c=ACC, lw=1.4)
    ax.set_xlim(0.0, 14.5)
    ax.set_ylim(-1.75, 3.7)
    title(ax, "Signal phase diagrams", y=1.0, size=9.0)
    save(fig, "f4_signalphase")


def f_timespace():
    fig, ax = newfig(6.5, 3.05)
    sig = [0, 400, 800, 1200]
    C, g = 60.0, 34.0
    v = 40 * 1000 / 3600.0
    Tmax = 150.0
    for i, x in enumerate(sig):
        off = (x / v) % C
        t = off - 2 * C
        while t < Tmax:
            for (t0, t1, col) in [(t, t + g, "#CFE3D5"), (t + g, t + C, "#F6CFCF")]:
                lo, hi = max(t0, 0.0), min(t1, Tmax)
                if hi > lo:
                    rect(ax, x - 15, lo, 30, hi - lo, fc=col, ec="none", z=2)
            t += C
        line(ax, [x, x], [0, Tmax], c=INK, lw=0.9, z=5)
        lab(ax, x, -11, "Signal %d" % (i + 1), size=7.2, weight="bold")
        lab(ax, x, -21, "%d m" % x, size=6.6, color=GREY)
        if i:
            dim(ax, (sig[i - 1], Tmax + 17), (x, Tmax + 17), "400 m", size=6.8)
            extline(ax, (x, Tmax), (x, Tmax + 21))
    extline(ax, (0, Tmax), (0, Tmax + 21))
    for t0 in (2, 62, 122):
        ax.plot([0, 1200], [t0, t0 + 1200 / v], color=ACC, lw=1.4, zorder=9,
                clip_on=True)
    ax.plot([0, 1200], [2, 2 + 1200 / v], color=ACC, lw=2.5, zorder=10)
    leader(ax, (700, 22), (560, 2 + 560 / v), "vehicle trajectory;\nslope = 1 / speed",
           size=6.9, c=ACC, ha="left")
    off1 = (400 / v) % C
    dim(ax, (424, 0), (424, off1), "offset", off=0, size=6.8, rot=0)
    extline(ax, (400, 0), (436, 0))
    extline(ax, (400, off1), (436, off1))
    rect(ax, 1300, 122, 26, 13, fc="#CFE3D5", ec=INK, lw=0.5, z=4)
    lab(ax, 1336, 128, "green", size=6.7, ha="left")
    rect(ax, 1300, 102, 26, 13, fc="#F6CFCF", ec=INK, lw=0.5, z=4)
    lab(ax, 1336, 108, "red", size=6.7, ha="left")
    lab(ax, 1300, 72, "Cycle C = 60 s\ngreen g = 34 s\nspeed = 40 km/h\n\n"
                      "offset of a signal\n= distance / speed\n(mod C)", size=6.8, ha="left")
    lab(ax, -128, Tmax / 2, "time  (s)", size=7.6, rot=90, color=INK)
    for tv in range(0, int(Tmax) + 1, 30):
        lab(ax, -34, tv, "%d" % tv, size=6.4, color=GREY, ha="right")
        line(ax, [-20, 0], [tv, tv], c=GREY, lw=0.5)
    line(ax, [-20, -20], [0, Tmax], c=INK, lw=0.9)
    lab(ax, 600, -34, "distance along the road  \u2192", size=7.6, color=INK)
    ax.set_xlim(-165, 1560)
    ax.set_ylim(-42, Tmax + 30)
    title(ax, "Time\u2013space diagram of a linearly co-ordinated (progressive) signal system",
          y=1.0, size=8.8, x=0.40)
    save(fig, "f4_timespace")


def f_rotary():
    fig, ax = newfig(5.6, 4.1, equal=True)
    Rc, Rw = 2.0, 3.40
    th = np.linspace(0, 2 * np.pi, 400)
    poly(ax, list(zip(Rw * np.cos(th), Rw * np.sin(th))), fc="#F1F4F7", ec=INK, lw=1.1, z=2)
    poly(ax, list(zip(Rc * np.cos(th), Rc * np.sin(th))), fc="#CFE3D5", ec=GRN, lw=1.3, z=4)
    lab(ax, 0, 0.34, "CENTRAL\nISLAND", size=7.6, weight="bold", color="#1F6B3B")
    lab(ax, 0, -0.52, "radius R", size=7.0, color="#1F6B3B")
    LEG, W = 6.6, 0.66
    for ang in (0, 90, 180, 270):
        u = np.radians(ang)
        ux, uy = np.cos(u), np.sin(u)
        px, py = -uy, ux
        for s in (-1, 1):
            line(ax, [Rw * ux * 0.94 + s * W * px, LEG * ux + s * W * px],
                 [Rw * uy * 0.94 + s * W * py, LEG * uy + s * W * py], c=INK, lw=1.0)
        line(ax, [Rw * ux, LEG * ux], [Rw * uy, LEG * uy], c="#C9A227", lw=0.8,
             ls=(0, (5, 4)))
        arr(ax, ((LEG - 0.5) * ux + 0.33 * px, (LEG - 0.5) * uy + 0.33 * py),
            ((Rw + 0.35) * ux + 0.33 * px, (Rw + 0.35) * uy + 0.33 * py),
            c=INK, lw=0.9, ms=7)
        arr(ax, ((Rw + 0.35) * ux - 0.33 * px, (Rw + 0.35) * uy - 0.33 * py),
            ((LEG - 0.5) * ux - 0.33 * px, (LEG - 0.5) * uy - 0.33 * py),
            c=INK, lw=0.9, ms=7)
    for a0 in (38, 128, 218, 308):
        a1, a2 = np.radians(a0), np.radians(a0 + 24)
        r = (Rc + Rw) / 2
        arr(ax, (r * np.cos(a1), r * np.sin(a1)), (r * np.cos(a2), r * np.sin(a2)),
            c=ACC, lw=1.4, ms=10, conn="arc3,rad=-0.25", z=10)
    # weaving section: east entry -> north exit
    aw = np.linspace(np.radians(-16), np.radians(102), 140)
    line(ax, (Rw + 0.13) * np.cos(aw), (Rw + 0.13) * np.sin(aw), c=PUR, lw=2.6, z=11)
    leader(ax, (5.1, 5.3), (Rw * 1.02 * np.cos(np.radians(45)),
                            Rw * 1.02 * np.sin(np.radians(45))),
           "weaving length  L\n(entry to the next exit)", size=7.1, c=PUR, ha="left")
    # weaving width, radially at 160 deg
    aa = np.radians(158)
    dim(ax, (Rc * np.cos(aa), Rc * np.sin(aa)), (Rw * np.cos(aa), Rw * np.sin(aa)),
        "w", off=0, size=7.6, rot=0)
    leader(ax, (-6.9, 3.05), (Rc * 1.28 * np.cos(aa), Rc * 1.28 * np.sin(aa)),
           "weaving width  w\n(= width of the\nrotary roadway)", size=7.1, c=ACC, ha="left")
    # entry / exit widths on the north leg
    dim(ax, (-W, 5.25), (0.0, 5.25), "e\u2081", size=7.2)
    dim(ax, (0.0, 5.25), (W, 5.25), "e\u2082", size=7.2)
    leader(ax, (2.55, 6.15), (W * 0.5, 5.35), "entry width e\u2081 , exit width e\u2082",
           size=7.1, c=ACC, ha="left")
    ax.add_patch(Arc((0, 0), 2 * Rw * 1.0, 2 * Rw * 1.0, theta1=294, theta2=336,
                     lw=1.6, color=TEA, zorder=11))
    leader(ax, (5.1, -4.5), (Rw * np.cos(np.radians(315)), Rw * np.sin(np.radians(315))),
           "radius of the entry curve\n(20\u201335 m urban, 20\u201325 m rural)",
           size=7.1, c=TEA, ha="left")
    lab(ax, 0.0, -7.45, "Traffic circulates ANTICLOCKWISE (in India). Every CROSSING conflict is "
                        "converted into\nMERGING \u2192 WEAVING \u2192 DIVERGING, so no vehicle "
                        "has to cross another head-on.",
        size=7.3, color=ACC, weight="bold")
    ax.set_xlim(-7.6, 8.4)
    ax.set_ylim(-8.0, 7.0)
    title(ax, "Elements of a rotary intersection", y=1.0, size=9.2, x=0.46)
    save(fig, "f4_rotary")


def f_channel():
    fig, ax = newfig(5.6, 2.85, equal=True)
    poly(ax, [(-6.0, -0.75), (6.0, -0.75), (6.0, 0.75), (-6.0, 0.75)],
         fc="#F1F4F7", ec=INK, lw=1.0, z=2)
    poly(ax, [(-0.80, -4.2), (0.80, -4.2), (0.80, -0.75), (-0.80, -0.75)],
         fc="#F1F4F7", ec=INK, lw=1.0, z=2)
    line(ax, [-6.0, 6.0], [0, 0], c="#C9A227", lw=0.8, ls=(0, (6, 4)))
    line(ax, [0, 0], [-4.2, -0.75], c="#C9A227", lw=0.8, ls=(0, (6, 4)))
    poly(ax, [(-0.32, -3.6), (0.32, -3.6), (0.32, -1.25), (-0.32, -1.25)],
         fc="#CFE3D5", ec=GRN, lw=1.0, z=6)
    poly(ax, [(-2.75, -0.55), (-1.05, -0.55), (-1.05, -1.75)], fc="#CFE3D5",
         ec=GRN, lw=1.0, z=6)
    poly(ax, [(2.75, -0.55), (1.05, -0.55), (1.05, -1.75)], fc="#CFE3D5",
         ec=GRN, lw=1.0, z=6)
    arr(ax, (-5.3, 0.38), (5.3, 0.38), c=INK, lw=1.1, ms=8)
    arr(ax, (5.3, -0.38), (-5.3, -0.38), c=INK, lw=1.1, ms=8)
    arr(ax, (0.42, -2.75), (2.45, -0.28), c=ACC, lw=1.3, ms=8, conn="arc3,rad=0.14")
    arr(ax, (-2.45, 0.28), (-0.42, -2.75), c=ACC, lw=1.3, ms=8, conn="arc3,rad=0.14")
    leader(ax, (-6.9, 3.35), (-1.95, -0.85),
           "channelizing islands force\nthe traffic into definite paths",
           size=7.0, ha="left", c=ACC)
    leader(ax, (6.9, 3.35), (1.85, -1.05),
           "turning radius set by\nthe design vehicle",
           size=7.0, ha="right", c=TEA)
    leader(ax, (4.6, -3.4), (0.32, -2.4), "divisional island separates\nthe two directions",
           size=7.0, ha="left", c=GRN)
    lab(ax, -5.75, 1.15, "major road", size=7.2, ha="left", color=INK)
    lab(ax, 1.05, -3.95, "minor road", size=7.2, ha="left", color=INK)
    lab(ax, 0.0, -5.35, "CHANNELIZATION \u2014 regulating conflicting movements with islands, "
                        "markings and turning\nroadways; it reduces the conflict area and fixes "
                        "the angle and point of merging",
        size=7.2, color=ACC, weight="bold")
    ax.set_xlim(-7.0, 7.6)
    ax.set_ylim(-5.9, 4.5)
    title(ax, "Channelized T-intersection (at-grade)", y=1.0, size=9.2, x=0.46)
    save(fig, "f4_channel")


def f_interchange():
    fig, axs = plt.subplots(1, 3, figsize=(7.15, 2.35))
    for a in axs:
        a.set_axis_off()
        a.set_aspect("equal")
    th = np.linspace(0, 2 * np.pi, 300)
    # ---- trumpet ---- #
    a = axs[0]
    a.plot([-4.2, 4.2], [0.5, 0.5], color=INK, lw=2.0)
    a.plot([-4.2, 4.2], [-0.5, -0.5], color=INK, lw=2.0)
    a.plot([0, 0], [-0.5, -4.2], color=INK, lw=2.0)
    lp = 1.35
    a.plot(0.1 + lp * np.cos(th), 1.9 + lp * np.sin(th), color=ACC, lw=1.2)
    a.plot([-2.6, -0.9], [-0.5, -3.1], color=ACC, lw=1.2)
    t2 = np.linspace(np.pi, 2 * np.pi, 100)
    a.plot(2.0 + 1.5 * np.cos(t2), 0.5 + 1.5 * np.sin(t2) * 0.9, color=ACC, lw=1.2)
    a.set_title("(a)  Trumpet (T interchange)", fontsize=7.8, color=INK, pad=4)
    a.text(0, -5.2, "For a 3-leg (T) junction.\nOne loop + one direct ramp.",
           fontsize=6.5, ha="center", color="#333333")
    a.set_xlim(-4.6, 4.6)
    a.set_ylim(-5.9, 3.9)
    # ---- diamond ---- #
    a = axs[1]
    a.plot([-4.2, 4.2], [0.5, 0.5], color=INK, lw=2.0)
    a.plot([-4.2, 4.2], [-0.5, -0.5], color=INK, lw=2.0)
    a.plot([-0.5, -0.5], [-4.2, 4.2], color="#4A6D8C", lw=2.0)
    a.plot([0.5, 0.5], [-4.2, 4.2], color="#4A6D8C", lw=2.0)
    for sx, sy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        a.plot([sx * 0.5, sx * 2.9], [sy * 1.6, sy * 0.55], color=ACC, lw=1.2)
    a.scatter([0.5, -0.5, 0.5, -0.5], [1.6, 1.6, -1.6, -1.6], s=14, color=RED, zorder=8)
    a.set_title("(b)  Diamond", fontsize=7.8, color=INK, pad=4)
    a.text(0, -5.2, "Cheapest 4-leg type; needs least land.\nRed dots = at-grade conflict on the minor road.",
           fontsize=6.5, ha="center", color="#333333")
    a.set_xlim(-4.6, 4.6)
    a.set_ylim(-5.9, 3.9)
    # ---- cloverleaf ---- #
    a = axs[2]
    a.plot([-4.4, 4.4], [0.45, 0.45], color=INK, lw=2.0)
    a.plot([-4.4, 4.4], [-0.45, -0.45], color=INK, lw=2.0)
    a.plot([-0.45, -0.45], [-4.4, 4.4], color="#4A6D8C", lw=2.0)
    a.plot([0.45, 0.45], [-4.4, 4.4], color="#4A6D8C", lw=2.0)
    r = 1.35
    for cx, cy in [(1.85, 1.85), (1.85, -1.85), (-1.85, 1.85), (-1.85, -1.85)]:
        a.plot(cx + r * np.cos(th), cy + r * np.sin(th), color=ACC, lw=1.1)
    a.set_title("(c)  Cloverleaf", fontsize=7.8, color=INK, pad=4)
    a.text(0, -5.4, "Four loop ramps \u2014 NO crossing conflict at all,\n"
                    "but large land area and weaving on the loops.",
           fontsize=6.5, ha="center", color="#333333")
    a.set_xlim(-4.8, 4.8)
    a.set_ylim(-6.1, 4.1)
    fig.suptitle("Common types of grade-separated interchange", fontsize=9.0,
                 fontweight="bold", color=INK, y=1.03)
    fig.tight_layout()
    save(fig, "f4_interchange")


def f_intersect_types():
    fig, axs = plt.subplots(2, 3, figsize=(6.6, 3.0))
    axs = axs.ravel()
    for a in axs:
        a.set_axis_off()
        a.set_aspect("equal")
        a.set_xlim(-3.2, 3.2)
        a.set_ylim(-3.2, 3.2)
    W = 0.42
    def road(a, p1, p2, c=INK):
        (x1, y1), (x2, y2) = p1, p2
        L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        nx, ny = -(y2 - y1) / L * W, (x2 - x1) / L * W
        a.add_patch(Polygon([(x1 + nx, y1 + ny), (x2 + nx, y2 + ny),
                             (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)],
                            fc="#F1F4F7", ec=c, lw=0.9))
    # T
    road(axs[0], (-3, 1.2), (3, 1.2)); road(axs[0], (0, 1.2), (0, -3))
    axs[0].set_title("T (three-leg)", fontsize=7.2, color=INK, pad=2)
    # Y / skew
    road(axs[1], (-3, 1.4), (3, 1.4)); road(axs[1], (0, 1.4), (-1.9, -3))
    axs[1].set_title("Skew / Y", fontsize=7.2, color=INK, pad=2)
    # cross
    road(axs[2], (-3, 0), (3, 0)); road(axs[2], (0, -3), (0, 3))
    axs[2].set_title("Cross (four-leg)", fontsize=7.2, color=INK, pad=2)
    # staggered
    road(axs[3], (-3, 0), (3, 0))
    road(axs[3], (-1.3, 0), (-1.3, 3)); road(axs[3], (1.3, 0), (1.3, -3))
    axs[3].set_title("Staggered", fontsize=7.2, color=INK, pad=2)
    # multi-leg
    road(axs[4], (-3, 0), (3, 0)); road(axs[4], (0, -3), (0, 3))
    road(axs[4], (-2.4, -2.4), (2.4, 2.4))
    axs[4].set_title("Multi-leg (rotary needed)", fontsize=7.2, color=INK, pad=2)
    # rotary
    a = axs[5]
    for ang in (0, 90, 180, 270):
        u = np.radians(ang)
        road(a, (1.1 * np.cos(u), 1.1 * np.sin(u)), (3 * np.cos(u), 3 * np.sin(u)))
    tt = np.linspace(0, 2 * np.pi, 200)
    a.add_patch(Polygon(list(zip(1.55 * np.cos(tt), 1.55 * np.sin(tt))),
                        fc="#F1F4F7", ec=INK, lw=0.9))
    a.add_patch(Circle((0, 0), 0.78, fc="#CFE3D5", ec=GRN, lw=0.9))
    a.set_title("Rotary", fontsize=7.2, color=INK, pad=2)
    fig.suptitle("Types of at-grade intersection", fontsize=9.0, fontweight="bold",
                 color=INK, y=1.02)
    fig.tight_layout()
    save(fig, "f4_intersecttypes")


def f_parking():
    fig, ax = newfig(7.0, 2.45)
    data = [(0, "Parallel", "5.9", "3.0", "N = L / 5.9"),
            (30, "30\u00b0", "5.0", "4.3", "N = (L \u2212 1.77)/5.0"),
            (45, "45\u00b0", "3.54", "5.0", "N = (L \u2212 3.54)/3.54"),
            (60, "60\u00b0", "2.89", "5.4", "N = (L \u2212 4.6)/2.89"),
            (90, "90\u00b0", "2.5", "5.0", "N = L / 2.5")]
    PW_ = 4.15
    cl, cw_ = 1.05, 0.52
    for j, (ang, name, kerb, depth, formula) in enumerate(data):
        x0 = j * PW_
        xc = x0 + PW_ / 2 - 0.2
        line(ax, [x0 + 0.05, x0 + PW_ - 0.45], [0, 0], c=INK, lw=2.0)
        lab(ax, xc, -0.30, "kerb", size=6.2, color=INK)
        if ang == 0:
            for i in range(3):
                bx = x0 + 0.18 + i * 0.94
                poly(ax, [(bx, 0.08), (bx + 1.30, 0.08), (bx + 1.30, 0.60), (bx, 0.60)],
                     fc="#DDE7F1", ec=INK, lw=0.8, z=5)
        else:
            a_ = np.radians(ang)
            dx, dy = cl * np.cos(a_), cl * np.sin(a_)
            sx, cy = cw_ * np.sin(a_), cw_ * np.cos(a_)
            step = cw_ / np.sin(a_)
            for i in range(3):
                bx = x0 + 0.22 + sx + i * step
                poly(ax, [(bx, 0.07), (bx + dx, 0.07 + dy),
                          (bx + dx - sx, 0.07 + dy + cy), (bx - sx, 0.07 + cy)],
                     fc="#DDE7F1", ec=INK, lw=0.8, z=5)
        lab(ax, xc, 2.28, name, size=8.4, weight="bold")
        lab(ax, xc, 1.98, "%s m of kerb per car" % kerb, size=6.2, color=ACC)
        lab(ax, xc, 1.76, "bay depth %s m" % depth, size=6.2, color=TEA)
        lab(ax, xc, -0.70, formula, size=6.8, weight="bold", color=PUR)
    tot = 5 * PW_
    lab(ax, tot / 2 - 0.2, -1.22, "N = number of cars that can be parked along a kerb of "
                                  "length L ;  design car 5.0 m \u00d7 2.5 m",
        size=7.2, color="#333333")
    lab(ax, tot / 2 - 0.2, -1.62, "As the parking angle increases, MORE cars are parked per "
                                  "metre of kerb, but a GREATER width of carriageway is lost",
        size=7.2, color=ACC, weight="bold")
    ax.set_xlim(-0.25, tot - 0.15)
    ax.set_ylim(-1.95, 2.62)
    title(ax, "On-street (kerb) parking layouts", y=1.0, size=9.2)
    save(fig, "f4_parking")


def f_lighting():
    fig, axs = plt.subplots(2, 2, figsize=(6.6, 2.9))
    axs = axs.ravel()
    names = ["(a) Single-side mounting", "(b) Staggered (zig-zag)",
             "(c) Opposite (paired)", "(d) Central (span) mounting"]
    for i, a in enumerate(axs):
        a.set_axis_off()
        a.set_xlim(-0.6, 12.4)
        a.set_ylim(-2.2, 3.4)
        a.add_patch(Rectangle((0, 0), 11.8, 1.8, fc="#F1F4F7", ec=INK, lw=0.9))
        a.plot([0, 11.8], [0.9, 0.9], color="#C9A227", lw=0.7, ls=(0, (6, 4)))
        a.set_title(names[i], fontsize=7.4, color=INK, fontweight="bold", pad=3)
        S = 2.6
        def pole(x, y, up=True):
            a.plot([x, x], [y, y + (0.62 if up else -0.62)], color=INK, lw=1.3)
            a.add_patch(Circle((x, y + (0.62 if up else -0.62)), 0.15,
                               fc="#FFE9A8", ec="#8A6A0B", lw=0.8, zorder=8))
        if i == 0:
            for k in range(5):
                pole(0.7 + k * S, 1.8)
        elif i == 1:
            for k in range(5):
                if k % 2 == 0:
                    pole(0.7 + k * (S / 2 * 2) / 2 * 1.0 + 0, 1.8) if False else pole(0.7 + k * 1.3, 1.8)
                else:
                    pole(0.7 + k * 1.3, 0.0, up=False)
        elif i == 2:
            for k in range(5):
                pole(0.7 + k * S, 1.8)
                pole(0.7 + k * S, 0.0, up=False)
        else:
            for k in range(5):
                x = 0.7 + k * S
                a.plot([x, x], [0.9, 2.4], color=INK, lw=1.3)
                a.add_patch(Circle((x, 2.4), 0.15, fc="#FFE9A8", ec="#8A6A0B",
                                   lw=0.8, zorder=8))
        a.annotate("", xy=(0.7, -1.35), xytext=(0.7 + S, -1.35),
                   arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=0.8, mutation_scale=6))
        a.text(0.7 + S / 2, -1.90, "spacing S", fontsize=6.6, color=ACC, ha="center")
        if i == 1:
            a.annotate("", xy=(2.0, -0.75), xytext=(3.3, -0.75),
                       arrowprops=dict(arrowstyle="<|-|>", color=TEA, lw=0.7,
                                       mutation_scale=5))
            a.text(2.65, -1.15, "S/2", fontsize=6.2, color=TEA, ha="center")
    fig.suptitle("Layouts for highway lighting  (S = spacing of lamps, "
                 "h = mounting height, W = road width)",
                 fontsize=8.4, fontweight="bold", color=INK, y=1.03)
    fig.tight_layout()
    save(fig, "f4_lighting")


ALL = [f_piev, f_flow, f_spotspeed, f_movingobs, f_collision, f_los,
       f_signs, f_signalphase, f_timespace, f_rotary, f_channel,
       f_interchange, f_intersect_types, f_parking, f_lighting]

if __name__ == "__main__":
    for f in ALL:
        f()
        print("ok", f.__name__)
