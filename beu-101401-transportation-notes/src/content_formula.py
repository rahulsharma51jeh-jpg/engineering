"""Condensed all-unit formula sheet + IRC standard-values sheet."""
from kit import *

CW = (FW - 10) / 2.0          # width of one column of the two-column layout


def _c(title, lines, color="blue"):
    return FCARD(title, lines, color=color, width=CW)


def build():
    S = H1("F", "Formula Sheet and IRC Standard Values",
           "read this last, on the morning of the paper",
           header="Formula sheet")

    # ================================================================== U1
    L = []
    L += _c("Unit 1 \u2014 planning", [
        "Road density = (road length / area) \u00d7 100",
        "     km per 100 km\u00b2",
        "Plan targets:  Nagpur 16,  Bombay 32,",
        "     Lucknow 82 km per 100 km\u00b2",
        "Saturation system:",
        "  utility per km = total utility units / length",
        "     (highest value gets first priority)",
    ], "teal")
    L += _c("Unit 2 \u2014 camber and width", [
        "Parabolic camber:  y = 2x\u00b2 / (n W)",
        "Rise of crown above edge = W / (2n)",
        "Camber 1 in n  \u2261  (100/n) %",
        "Lane widths: 3.75 single \u2022 7.0 two-lane",
        "     5.5 intermediate \u2022 3.5 per lane multi",
    ])
    R = []
    R += _c("Sight distance", [
        "SSD = 0.278 V t + V\u00b2/(254 f)",
        "SSD = v t + v\u00b2/(2 g f)        [v in m/s]",
        "On a grade:  V\u00b2/[254(f \u00b1 0.01n)]",
        "     + for ASCENDING, \u2212 for DESCENDING",
        "Single-lane two-way:  SSD\u2081\u208b\u2097\u2090\u2099\u2091 = 2 \u00d7 SSD",
        "ISD = 2 \u00d7 SSD",
        "t = 2.5 s (SSD), 2 s (OSD);  f = 0.35\u20130.40",
        "OSD = d\u2081 + d\u2082 + d\u2083",
        "  d\u2081 = 0.278 V\u1d47 t",
        "  d\u2082 = 0.278 V\u1d47 T + 2s",
        "  d\u2083 = 0.278 V T",
        "  s = 0.7 v\u1d47 + 6      [v\u1d47 in m/s]",
        "  T = \u221a(4s/a)  or  \u221a(14.4 s/A)",
        "  V\u1d47 = V \u2212 16 if not given",
        "Overtaking zone: min 3\u00d7OSD, desirable 5\u00d7OSD",
        "Divided highway: OSD = d\u2081 + d\u2082 only",
    ], "rust")
    S += TWOCOL(L, R)

    # ================================================================== U2
    L = []
    L += _c("Horizontal alignment", [
        "e + f = v\u00b2/(gR) = V\u00b2/(127 R)",
        "Mixed traffic:  e = V\u00b2/(225 R)",
        "     [ = (0.75V)\u00b2/(127R) ]",
        "Rise of outer edge  E = e \u00d7 B",
        "R\u2098\u1d62\u2099 = V\u00b2/[127(e + f)]",
        "e\u2098\u2090\u2093 = 7 % plain/rolling, 10 % hill,",
        "     4 % urban;  f = 0.15",
        "IRC steps: (1) e = V\u00b2/225R;  (2) if e > 7 %",
        "  take e = 7 %;  (3) check f = V\u00b2/127R \u2212 0.07",
        "  \u2264 0.15;  (4) else V\u2090 = \u221a(27.94 R)",
        "",
        "W\u2098 = n l\u00b2/(2R)     [l = 6.1 m]",
        "W\u209a\u209b = V/(9.5 \u221aR)",
        "W\u2091 = W\u2098 + W\u209a\u209b",
    ], "plum")
    L += _c("Transition curve", [
        "L = greatest of the three:",
        "(i)  L = 0.0215 V\u00b3/(C R),  C = 80/(75+V)",
        "        0.5 \u2264 C \u2264 0.8",
        "(ii) L = e N (W + W\u2091)   [about inner edge]",
        "     L = e N (W + W\u2091)/2 [about centre line]",
        "     empirical 2.7V\u00b2/R plain, V\u00b2/R hilly",
        "(iii) IRC minimum for the road class",
        "Shift  S = L\u00b2/(24 R)",
        "Tangent length = (R+S) tan(\u0394/2) + L/2",
    ])
    R = []
    R += _c("Set-back distance", [
        "L\u1d9c \u2265 S :  m = R \u2212 (R\u2212d) cos[S/(2(R\u2212d))]",
        "Single lane:  m = R \u2212 R cos(S/2R)",
        "L\u1d9c < S :  m = R \u2212 (R\u2212d) cos(\u03b1/2)",
        "        + [(S\u2212L\u1d9c)/2] sin(\u03b1/2)",
        "        \u03b1/2 = L\u1d9c/[2(R\u2212d)]",
        "d = 1.75 m for a 7 m two-lane road",
        "ANGLE IN RADIANS",
    ], "gold")
    R += _c("Vertical alignment", [
        "N = algebraic difference of grades",
        "Grade compensation = (30+R)/R %,",
        "     max 75/R %; none below 4 %",
        "",
        "SUMMIT (parabola), sight distance governs:",
        "L > S :  L = N S\u00b2/[2(\u221aH + \u221ah)\u00b2]",
        "        = N S\u00b2/4.4 (SSD), N S\u00b2/9.6 (OSD)",
        "L < S :  L = 2S \u2212 2(\u221aH + \u221ah)\u00b2/N",
        "        = 2S \u2212 4.4/N,  2S \u2212 9.6/N",
        "H = 1.2 m, h = 0.15 m (SSD); H = h = 1.2 (OSD)",
        "",
        "VALLEY \u2014 take the GREATER of:",
        "comfort:  L = 0.38 (N V\u00b3)^\u00bd   [c = 0.6 m/s\u00b3]",
        "head-light, L > S :  L = N S\u00b2/(1.5 + 0.035 S)",
        "head-light, L < S :  L = 2S \u2212 (1.5+0.035S)/N",
        "h\u2081 = 0.75 m,  \u03b2 = 1\u00b0",
    ], "teal")
    S += TWOCOL(L, R)

    # ================================================================== U3
    L = []
    L += _c("Unit 3 \u2014 traffic flow", [
        "q = k \u00d7 v\u0304\u209b        (use SPACE mean speed)",
        "v\u0304\u209c = (1/n)\u03a3v\u1d62      (arithmetic mean)",
        "v\u0304\u209b = n/\u03a3(1/v\u1d62)     (harmonic mean)",
        "v\u0304\u209c = v\u0304\u209b + \u03c3\u209b\u00b2/v\u0304\u209b  \u21d2  v\u0304\u209c \u2265 v\u0304\u209b",
        "Time headway  h = 3600/q  (s)",
        "Space headway  s = 1000/k  (m)",
        "",
        "Greenshields:  v = v_f (1 \u2212 k/k_j)",
        "q = v_f (k \u2212 k\u00b2/k_j)",
        "q_max = v_f k_j / 4  at  k_j/2 and v_f/2",
    ])
    L += _c("Capacity and volume", [
        "C = 1000 V / S     (veh/h per lane)",
        "C = 3600 / H\u209c",
        "S\u2098\u1d62\u2099 = SSD + length of vehicle",
        "PHF = peak hour vol /(4 \u00d7 peak 15-min vol)",
        "Design volume: 30th highest hourly volume",
    ], "gold")
    R = []
    R += _c("Moving observer method", [
        "q = (n\u2090 + n\u1d67 \u2212 n\u2092)/(t\u2090 + t\u1d69)",
        "t\u0304 = t\u1d69 \u2212 (n\u1d67 \u2212 n\u2092)/q",
        "v\u0304 = L/t\u0304       k = q/v\u0304",
        "n\u2090 met against stream in t\u2090",
        "n\u1d67 overtake the test vehicle",
        "n\u2092 overtaken by the test vehicle",
    ], "rust")
    S += TWOCOL(L, R)
    S += TWOCOL(_c("Speeds and accidents", [
        "85th percentile \u2192 safe speed LIMIT",
        "98th percentile \u2192 geometric DESIGN speed",
        "15th percentile \u2192 lower speed limit",
        "R per 100 million veh-km",
        "  = A \u00d7 10\u2078/(365 \u00d7 ADT \u00d7 N \u00d7 L)",
        "R per million entering vehicles",
        "  = A \u00d7 10\u2076/(365 \u00d7 ADT \u00d7 N)",
    ], "plum"), [])

    # ================================================================== U4
    L = []
    L += _c("Unit 4 \u2014 signal design", [
        "WEBSTER:",
        "y\u1d62 = q\u1d62/s\u1d62        Y = \u03a3y\u1d62   (need Y < 1)",
        "L = 2n + R    (n = phases, R = all-red)",
        "C\u2080 = (1.5 L + 5)/(1 \u2212 Y)",
        "g\u1d62 = (y\u1d62/Y)(C\u2080 \u2212 L)",
        "Round C\u2080 to the nearest 5 s",
        "",
        "IRC / pedestrian:  G\u209a = 7 + W/1.2",
        "G\u1d62 = [q\u1d62/\u03a3q] \u00d7 available green",
        "Offset = distance / speed  (mod C)",
        "Alternate system spacing = v C/2",
    ], "rust")
    L += _c("Rotary intersection", [
        "Q\u209a = 280 w (1 + e/w)(1 \u2212 p/3)/(1 + w/L)",
        "p = (b + c)/(a + b + c + d)",
        "Valid:  6 \u2264 w \u2264 18 m",
        "        0.4 \u2264 e/w \u2264 1.0",
        "        0.12 \u2264 w/L \u2264 0.4",
        "        0.4 \u2264 p \u2264 1.0",
        "e = (e\u2081 + e\u2082)/2",
        "R\u1d62\u209b\u2097\u2090\u2099\u1d48 \u2248 1.33 \u00d7 R\u2091\u2099\u209c\u1d63\u1d67",
        "Weaving length \u2265 45 m at 40 km/h",
    ], "teal")
    R = []
    R += _c("Parking", [
        "Parking load = \u03a3(accumulation \u00d7 interval)",
        "     [vehicle-hours]",
        "Average duration = load / volume",
        "Turnover = volume / number of bays",
        "Capacity = bays \u00d7 duration of study",
        "Index = (load / capacity) \u00d7 100 %",
        "",
        "Kerb length per car and N for kerb L:",
        "  parallel 5.9 m   N = L/5.9",
        "  30\u00b0      5.0 m   N = (L\u22121.77)/5.0",
        "  45\u00b0     3.54 m   N = (L\u22123.54)/3.54",
        "  60\u00b0     2.89 m   N = (L\u22124.6)/2.89",
        "  90\u00b0      2.5 m   N = L/2.5",
    ], "gold")
    S += TWOCOL(L, R)
    L, R = [], []
    R += _c("Highway lighting", [
        "E = (F \u00d7 CU \u00d7 MF)/(W \u00d7 S)",
        "S = (F \u00d7 CU \u00d7 MF)/(E \u00d7 W)",
        "E lux \u2022 F lumens \u2022 MF \u2248 0.8",
        "1 lux = 1 lumen/m\u00b2",
        "Layout: single side if W < h;",
        "  staggered if W = 1\u20131.5 h;",
        "  opposite if W > 1.5 h",
        "Mounting height 10\u201312 m, spacing 30\u201350 m",
    ], "plum")
    S += TWOCOL(L, R)

    # ================================================================== U5
    L = []
    L += _c("Unit 5 \u2014 soil and aggregate", [
        "CBR = (test load/standard load) \u00d7 100",
        "  standard 1370 kg at 2.5 mm",
        "           2055 kg at 5.0 mm",
        "  report the 2.5 mm value normally",
        "",
        "GI = 0.2a + 0.005ac + 0.01bd",
        "  a = (% passing 0.075) \u2212 35   [0\u201340]",
        "  b = (% passing 0.075) \u2212 15   [0\u201340]",
        "  c = LL \u2212 40                 [0\u201320]",
        "  d = PI \u2212 10                 [0\u201320]",
        "",
        "AIV, ACV, LAA = (W\u2082/W\u2081) \u00d7 100",
        "FI = flaky wt / total wt \u00d7 100",
        "EI = elongated wt / non-flaky wt \u00d7 100",
    ], "teal")
    R = []
    R += _c("Marshall mix design", [
        "G\u2098 = W\u2090/(W\u2090 \u2212 W\u1d64)",
        "G\u209c = 100/\u03a3(W\u1d62/G\u1d62)",
        "V\u1d65 = [(G\u209c \u2212 G\u2098)/G\u209c] \u00d7 100 %",
        "V\u1d47 = (W\u1d47 \u00d7 G\u2098)/G\u1d47  %",
        "VMA = V\u1d65 + V\u1d47",
        "VFB = (V\u1d47/VMA) \u00d7 100 %",
        "OBC = mean of the bitumen contents at",
        "  max stability, max unit weight, 4 % V\u1d65",
        "Criteria: stability \u2265 9 kN, flow 2\u20134 mm,",
        "  V\u1d65 3\u20135 %, VFB 65\u201375 %",
        "Test at 60 \u00b0C, 50 mm/min, 75 blows/face",
    ], "rust")
    S += TWOCOL(L, R)

    # ================================================================== U6
    L = []
    L += _c("Unit 6 \u2014 flexible pavement", [
        "a = \u221a(P/\u03c0p)      d = S \u2212 2a",
        "ESWL = P for z \u2264 d/2 ; 2P for z \u2265 2S",
        "log ESWL = log P",
        "   + 0.301 log(2z/d)/log(4S/d)",
        "Rigidity factor = contact/tyre pressure",
        "   ( = 1.0 at a tyre pressure of 7 kg/cm\u00b2)",
        "",
        "N = 365 A [(1+r)\u207f \u2212 1]/r \u00d7 D \u00d7 F",
        "A = P(1+r)\u02e3",
        "D = 1.0 single lane, 0.75 two-lane,",
        "    0.40 four-lane single carriageway",
        "Standard axle 8.16 t (80 kN); N in msa",
        "M\u1d63 = 10 CBR (CBR \u2264 5)",
        "M\u1d63 = 17.6 CBR^0.64 (CBR > 5)   [MPa]",
        "",
        "Boussinesq, circular load, on the axis:",
        "\u03c3\u1dbb = p[1 \u2212 z\u00b3/(a\u00b2+z\u00b2)^1.5]",
        "point load:  \u03c3\u1dbb = 3P/(2\u03c0z\u00b2)",
        "Burmister:  \u0394 = 1.5 p a F\u2082/E\u2082",
    ], "plum")
    R = []
    R += _c("Rigid pavement \u2014 Westergaard", [
        "l = [E h\u00b3/(12(1\u2212\u03bc\u00b2)K)]^\u00bc",
        "b = \u221a(1.6a\u00b2 + h\u00b2) \u2212 0.675h,  a < 1.724h",
        "b = a,                        a \u2265 1.724h",
        "\u03c3\u1d62 = (0.316P/h\u00b2)[4log\u2081\u2080(l/b) + 1.069]",
        "\u03c3\u2091 = (0.572P/h\u00b2)[4log\u2081\u2080(l/b) + 0.359]",
        "\u03c3\u1d04 = (3P/h\u00b2)[1 \u2212 (a\u221a2/l)^0.6]",
        "interior, edge \u2192 tension at the BOTTOM",
        "corner \u2192 tension at the TOP",
        "E = 3\u00d710\u2075 kg/cm\u00b2, \u03bc = 0.15",
    ], "teal")
    R += _c("Temperature, friction, joints", [
        "\u03c3\u209c\u1d62 = (E\u03b1t/2)[(C\u2093 + \u03bcC\u1d67)/(1\u2212\u03bc\u00b2)]",
        "\u03c3\u209c\u2091 = C E\u03b1t/2",
        "\u03c3\u209c\u1d04 = [E\u03b1t/(3(1\u2212\u03bc))]\u221a(a/l)",
        "\u03b1 = 10\u00d710\u207b\u2076/\u00b0C",
        "\u03c3\u2091 = W L f/(2\u00d710\u2074)   [h cancels]",
        "",
        "L\u2091 = \u03b4/(2\u03b1\u0394T)      (expansion joint)",
        "L\u1d04 = 2\u00d710\u2074 S\u1d04/(W f)   (contraction)",
        "A\u209b = b f h W/S\u209b       (tie steel)",
        "L\u209c = S\u209b d/(2 S\u1d47)      (tie bar length)",
        "Dowel:  P\u209b = 0.785 d\u00b2F\u209b",
        "  P\u2093 = 2d\u00b3F\u2093/(L\u1d48 + 8.8\u03b4)",
        "  P\u1d47 = F\u1d47L\u1d48d/[12.5(L\u1d48 + 1.5\u03b4)]",
        "  load transferred = 40 % of wheel load",
    ], "rust")
    S += TWOCOL(L, R)

    # ================================================================== values
    S += H2("Standard values worth memorising")
    S += TBL([["Quantity", "Value", "Quantity", "Value"],
              ["Reaction time for SSD", "2.5 s", "Max superelevation, plain/rolling", "7 %"],
              ["Reaction time for OSD", "2.0 s", "Max superelevation, hill roads", "10 %"],
              ["Coefficient of longitudinal friction f", "0.35\u20130.40",
               "Max superelevation, urban roads", "4 %"],
              ["Coefficient of lateral friction f", "0.15",
               "Coefficient of subgrade friction", "1.5"],
              ["Driver's eye height H", "1.2 m", "Wheel base of a design vehicle l", "6.1 m"],
              ["Object height for SSD h", "0.15 m", "Standard axle load", "8.16 t (80 kN)"],
              ["Head-light height h\u2081", "0.75 m", "Legal max single axle load", "10.2 t"],
              ["Head-light beam divergence \u03b2", "1\u00b0", "Max vehicle width / height",
               "2.5 m / 3.8 m"],
              ["Rate of change of centrifugal accn (valley)", "0.6 m/s\u00b3",
               "Flexural strength of PQC", "4.5 MPa"],
              ["Rate of introduction of e, plain terrain", "1 in 150",
               "Modulus of elasticity of concrete", "3 \u00d7 10\u2075 kg/cm\u00b2"],
              ["Rate of introduction of e, hilly terrain", "1 in 60",
               "Poisson's ratio of concrete", "0.15"],
              ["Ruling gradient, plain terrain", "3.3 % (1 in 30)",
               "Thermal expansion of concrete \u03b1", "10 \u00d7 10\u207b\u2076/\u00b0C"],
              ["Limiting gradient, plain terrain", "5 % (1 in 20)",
               "Unit weight of concrete", "2400 kg/m\u00b3"],
              ["Exceptional gradient, plain terrain", "6.7 % (1 in 15)",
               "Expansion joint gap / spacing", "20\u201325 mm / 50\u201360 m"],
              ["Camber, CC and high-type bituminous", "1.7\u20132.0 %",
               "Contraction joint spacing", "3.5\u20134.5 m"],
              ["Camber, thin bituminous", "2.0\u20132.5 %",
               "Design life, flexible pavement", "15 years"],
              ["Camber, WBM and gravel", "2.5\u20133.0 %",
               "Design life, rigid pavement", "30 years"],
              ["Camber, earth roads", "3.0\u20134.0 %",
               "Growth rate of commercial traffic", "5 % min, 7.5 % typical"],
              ["Minimum shoulder width (NH, SH)", "2.5 m",
               "Marshall stability, minimum", "9 kN"],
              ["Minimum median width", "1.2 m", "Marshall air voids", "3\u20135 %"],
              ["Minimum footpath width", "1.5 m", "Marshall VFB", "65\u201375 %"],
              ["ROW, NH/SH plain, open area", "45 m", "Aggregate impact value, wearing course",
               "30 % max"],
              ["Standard CBR load at 2.5 / 5.0 mm", "1370 / 2055 kg",
               "Flakiness index", "25 % max"]],
             widths=[3.0, 1.9, 3.0, 1.9], align=["l", "c", "l", "c"], fs=7.2,
             caption="Table F.1  The numbers that carry the 2-mark questions.")
    S += TIP("If you remember nothing else, remember these five: "
             "<b>SSD = 0.278Vt + V\u00b2/254f</b>, "
             "<b>e + f = V\u00b2/127R</b>, "
             "<b>L = NS\u00b2/4.4</b> for a summit curve, "
             "<b>C\u2080 = (1.5L + 5)/(1 \u2212 Y)</b> for a signal, and "
             "<b>N = 365 A[(1+r)\u207f\u22121]/r \u00d7 D \u00d7 F</b> for the design traffic. "
             "Between them they cover a numerical in almost every paper.")
    return S
