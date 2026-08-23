"""figbase.py — shared matplotlib drawing helpers for schematic engineering diagrams."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Arc, Circle, Ellipse, FancyArrow,
                                FancyArrowPatch, Polygon, Rectangle, Wedge,
                                PathPatch)
from matplotlib.path import Path

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.4,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.linewidth": 0.8,
    "lines.solid_capstyle": "round",
})

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(OUT, exist_ok=True)

INK = "#12335C"      # main line colour
ACC = "#A8420E"      # accent / dimension
GRN = "#1F6B3B"
PUR = "#5B2A6B"
TEA = "#0F6E63"
ROAD = "#DDE7F1"
SOIL = "#E6DAC6"
GRAN = "#CFD8DF"
BIT = "#4A4A4A"
CONC = "#E4E4E4"
LGT = "#F2F6FA"
RED = "#C1272D"
GREY = "#5A5A5A"
GOLD = "#C9880B"


def newfig(w=7.2, h=3.2, equal=False, pad=0.0):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_axis_off()
    if equal:
        ax.set_aspect("equal", adjustable="datalim")
    return fig, ax


def save(fig, name, dpi=230):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=dpi, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return p


def title(ax, t, y=1.0, size=9.4, x=0.5, color=INK):
    ax.text(x, y, t, transform=ax.transAxes, ha="center", va="bottom",
            fontsize=size, fontweight="bold", color=color)


def lab(ax, x, y, t, size=8.0, ha="center", va="center", color=INK,
        weight="normal", rot=0, bbox=False, style=None):
    kw = {}
    if bbox:
        kw["bbox"] = dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.88)
    return ax.text(x, y, t, ha=ha, va=va, fontsize=size, color=color,
                   fontweight=weight, rotation=rot, rotation_mode="anchor",
                   fontstyle=style or "normal", zorder=20, **kw)


def line(ax, x, y, c=INK, lw=1.1, ls="-", z=5, **kw):
    return ax.plot(x, y, color=c, lw=lw, ls=ls, zorder=z, **kw)


def poly(ax, pts, fc=ROAD, ec=INK, lw=1.0, z=2, hatch=None, alpha=1.0):
    p = Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, lw=lw,
                zorder=z, hatch=hatch, alpha=alpha)
    ax.add_patch(p)
    return p


def rect(ax, x, y, w, h, fc=ROAD, ec=INK, lw=1.0, z=2, hatch=None, alpha=1.0):
    r = Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=lw, zorder=z,
                  hatch=hatch, alpha=alpha)
    ax.add_patch(r)
    return r


def arr(ax, p1, p2, c=INK, lw=1.0, style="-|>", ms=7, z=10, ls="-", conn=None):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                        color=c, lw=lw, zorder=z, linestyle=ls,
                        shrinkA=0, shrinkB=0,
                        connectionstyle=conn or "arc3,rad=0")
    ax.add_patch(a)
    return a


def dim(ax, p1, p2, text, off=0.0, c=ACC, size=7.6, side="above", tick=0.0,
        lw=0.8, tpad=0.0, rot=None):
    """Double-headed dimension line between p1 and p2 with centred label."""
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    L = (dx ** 2 + dy ** 2) ** 0.5
    if L == 0:
        return
    nx, ny = -dy / L, dx / L
    if side == "below":
        nx, ny = -nx, -ny
    ax1, ay1 = x1 + nx * off, y1 + ny * off
    ax2, ay2 = x2 + nx * off, y2 + ny * off
    ax.add_patch(FancyArrowPatch((ax1, ay1), (ax2, ay2), arrowstyle="<|-|>",
                                 mutation_scale=6, color=c, lw=lw, zorder=12,
                                 shrinkA=0, shrinkB=0))
    if tick:
        ax.plot([x1, ax1 + nx * tick], [y1, ay1 + ny * tick], color=c, lw=0.5, zorder=11)
        ax.plot([x2, ax2 + nx * tick], [y2, ay2 + ny * tick], color=c, lw=0.5, zorder=11)
    mx, my = (ax1 + ax2) / 2 + nx * tpad, (ay1 + ay2) / 2 + ny * tpad
    if rot is None:
        rot = np.degrees(np.arctan2(dy, dx))
        if abs(rot) > 90:
            rot += 180
    ax.text(mx, my, text, ha="center", va="center", fontsize=size, color=c,
            rotation=rot, rotation_mode="anchor", zorder=21,
            bbox=dict(boxstyle="round,pad=0.16", fc="white", ec="none", alpha=0.92))


def extline(ax, p1, p2, c="#888888", lw=0.5, ls=(0, (3, 2))):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=c, lw=lw, ls=ls, zorder=1)


def ground(ax, x1, x2, y, c=INK, lw=1.0, n=26, d=0.06, dirn=-1):
    """Hatched natural-ground line."""
    ax.plot([x1, x2], [y, y], color=c, lw=lw, zorder=6)
    for xx in np.linspace(x1, x2, n)[:-1]:
        ax.plot([xx, xx + d * 0.8], [y, y + dirn * d], color=c, lw=0.5, zorder=6)


def leader(ax, tp, tip, text, size=7.6, c=INK, ha="left", weight="normal"):
    ax.annotate(text, xy=tip, xytext=tp, fontsize=size, color=c, ha=ha,
                va="center", fontweight=weight, zorder=22,
                arrowprops=dict(arrowstyle="-", color=c, lw=0.6,
                                shrinkA=2, shrinkB=1))


def car(ax, x, y, L=0.9, H=0.34, c=INK, fc="#FFFFFF", dirn=1, lw=0.9):
    """Simple plan-view vehicle box with a nose."""
    body = [(x, y - H / 2), (x + dirn * (L - 0.18), y - H / 2),
            (x + dirn * L, y), (x + dirn * (L - 0.18), y + H / 2),
            (x, y + H / 2)]
    poly(ax, body, fc=fc, ec=c, lw=lw, z=8)
    return body


def wheelveh(ax, x, y, L=1.0, H=0.42, c=INK, fc="#F4F7FA"):
    """Elevation-view vehicle with wheels."""
    rect(ax, x, y + 0.10 * H, L, H, fc=fc, ec=c, lw=0.9, z=8)
    poly(ax, [(x + 0.18 * L, y + 1.1 * H), (x + 0.72 * L, y + 1.1 * H),
              (x + 0.64 * L, y + 1.55 * H), (x + 0.30 * L, y + 1.55 * H)],
         fc=fc, ec=c, lw=0.9, z=8)
    for fx in (0.20, 0.80):
        ax.add_patch(Circle((x + fx * L, y + 0.10 * H), 0.11 * H * 2.0,
                            fc=c, ec=c, zorder=9))


def gridpanel(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def axesplot(w=6.4, h=3.4, xlabel="", ylabel="", tsize=8.4):
    fig, ax = plt.subplots(figsize=(w, h))
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK, labelsize=7.4, width=0.7, length=3)
    ax.set_xlabel(xlabel, fontsize=tsize, color=INK)
    ax.set_ylabel(ylabel, fontsize=tsize, color=INK)
    return fig, ax


def curvearrow(ax, p1, p2, rad=0.3, c=ACC, lw=0.9, text=None, size=7.4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=7, color=c,
                        lw=lw, zorder=12, shrinkA=0, shrinkB=0,
                        connectionstyle="arc3,rad=%.3f" % rad)
    ax.add_patch(a)
    if text:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        ax.text(mx, my, text, fontsize=size, color=c, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
