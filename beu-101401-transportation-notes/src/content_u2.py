"""UNIT 2 - Geometric design of highways."""
from kit import *


def build():
    S = H1("2", "Geometric Design of Highways", "5 hours \u2022 about 12 % of the paper, "
                                                "but the largest share of the numericals")

    # ------------------------------------------------------------------ 2.1
    S += H2("2.1  Introduction \u2014 what geometric design covers")
    S += DEF("Geometric design", "the design of the <b>visible dimensions</b> of a highway "
             "\u2014 the cross-section, the horizontal alignment, the vertical alignment "
             "and the intersections \u2014 so that the road gives the optimum efficiency in "
             "operation with maximum safety at reasonable cost.")
    S += P("Geometric design must be done <b>once and for all</b> at the planning stage, "
           "because it is very costly to improve later. The elements are:")
    S += BUL(["<b>Cross-section elements</b> \u2014 pavement surface characteristics, camber, "
              "width of pavement, shoulders, medians, kerbs, side slopes, right of way.",
              "<b>Sight distance</b> \u2014 stopping, overtaking and intermediate sight "
              "distance, and sight distance at intersections.",
              "<b>Horizontal alignment</b> \u2014 radius of curve, superelevation, extra "
              "widening, transition curve, set-back distance.",
              "<b>Vertical alignment</b> \u2014 gradients, grade compensation, summit curves, "
              "valley curves.",
              "<b>Intersection elements</b> \u2014 dealt with in Unit 4."])
    S += H3("2.1.1  Design speed and terrain \u2014 the starting point of everything")
    S += P("<b>Design speed is the single most important factor</b> in geometric design: "
           "sight distance, radius, superelevation, transition length and vertical curve "
           "length are all functions of it. IRC fixes the design speed from the "
           "<b>class of the road</b> and the <b>terrain</b>.")
    S += TBL([["Terrain classification", "Cross slope of the country"],
              ["Plain", "0 to 10 %"], ["Rolling", "10 to 25 %"],
              ["Mountainous", "25 to 60 %"], ["Steep", "greater than 60 %"]],
             widths=[2.2, 2.2], align=["l", "c"], fs=8.0, first_bold=True,
             total_width=FW * 0.55,
             caption="Table 2.1  Terrain is classified by the general cross slope of the "
                     "country, not by the road gradient.")
    S += TBL([["Road classification", "Plain\nruling / min", "Rolling\nruling / min",
               "Mountainous\nruling / min", "Steep\nruling / min"],
              ["National and State Highways", "100 / 80", "80 / 65", "50 / 40", "40 / 30"],
              ["Major District Roads", "80 / 65", "65 / 50", "40 / 30", "30 / 20"],
              ["Other District Roads", "65 / 50", "50 / 40", "30 / 25", "25 / 20"],
              ["Village Roads", "50 / 40", "40 / 35", "25 / 20", "25 / 20"]],
             widths=[2.6, 1.7, 1.7, 1.8, 1.7], align=["l", "c", "c", "c", "c"],
             fs=7.8, first_bold=True,
             caption="Table 2.2  IRC design speeds in km/h (ruling speed / minimum speed). "
                     "Design for the RULING speed; the minimum speed is used only where "
                     "site conditions make the ruling value impossible.")
    S += PYQ(["How is terrain classified for the purpose of geometric design? [2 marks]",
              "What is design speed? On what factors does it depend? [2 marks]"])

    # ------------------------------------------------------------------ 2.2
    S += H2("2.2  Cross-section elements")
    S += FIG("f2_xsection_embank",
             "Fig. 2.1  Typical cross-section of a two-lane highway in embankment, showing "
             "carriageway, shoulders, camber, side slopes, side drains, roadway width and "
             "right of way. <b>Learn to draw and label this from memory.</b>")
    S += FIG("f2_xsection_cut",
             "Fig. 2.2  Cross-section of a highway in cutting \u2014 note the side drain, the "
             "back (cut) slope and the catch-water drain.")
    S += H3("2.2.1  Right of way, building line and control line")
    S += BUL(["<b>Right of way (land width)</b> \u2014 the area of land acquired for the road "
              "along its alignment. It should be adequate for the ultimate development, "
              "not merely the present one.",
              "<b>Building line</b> \u2014 a line on either side of the road beyond which the "
              "buildings must be set back, to give space for future widening and to keep the "
              "sight line clear.",
              "<b>Control line</b> \u2014 a line still further away, up to which the nature of "
              "the buildings is controlled by regulation."])
    S += TBL([["Road class", "Plain and rolling terrain\nOpen area / Built-up area",
               "Mountainous and steep terrain\nOpen area / Built-up area"],
              ["National and State Highways", "45 m  /  30 m", "24 m  /  20 m"],
              ["Major District Roads", "25 m  /  20 m", "18 m  /  15 m"],
              ["Other District Roads", "15 m  /  15 m", "15 m  /  12 m"],
              ["Village Roads", "12 m  /  10 m", "9 m  /  9 m"]],
             widths=[2.6, 3.4, 3.4], align=["l", "c", "c"], fs=7.9, first_bold=True,
             caption="Table 2.3  Recommended land width (right of way) as per IRC \u2014 "
                     "normal values.")
    S += H3("2.2.2  Camber (cross slope)")
    S += DEF("Camber", "the transverse slope given to the road surface, to drain the rain "
             "water off the pavement quickly.")
    S += P("<b>Objects of camber:</b> (i) to drain off the rain water from the surface "
           "quickly, so that water does not enter the pavement layers and the subgrade; "
           "(ii) to prevent the entry of water into the bituminous layers, which would "
           "cause stripping; (iii) to keep the surface dry and thus preserve skid resistance.")
    S += P("Camber must be a compromise: <b>too little</b> camber leaves water standing on "
           "the surface, while <b>too much</b> camber makes the vehicles drift towards the "
           "edge, causes discomfort, wears the central portion of the tyres and makes the "
           "surface prone to erosion of the shoulders.")
    S += FIG("f2_camber",
             "Fig. 2.3  Shapes of camber \u2014 parabolic (barrel), straight-line and "
             "combination. The parabolic shape is comfortable for fast traffic; the "
             "straight-line shape is easier to construct and maintain.")
    S += FORMULA(["Parabolic (barrel) camber:  y = 2 x\u00b2 / (n W)",
                  "Total rise of the crown above the edge = W / (2 n)"],
                 label="Camber",
                 where=["y = the drop of the surface below the crown, at a distance x from "
                        "the crown (m)",
                        "W = total width of the pavement (m)",
                        "n = the camber expressed as 1 in n (so cross slope = 1/n)",
                        "Camber is stated either as 1 in n or as a percentage (1 in 50 = 2 %)"])
    S += TBL([["Type of road surface", "Camber \u2014 range", "Camber as 1 in n"],
              ["Cement concrete and high-type bituminous surfaces", "1.7 to 2.0 %",
               "1 in 60 to 1 in 50"],
              ["Thin bituminous surfaces", "2.0 to 2.5 %", "1 in 50 to 1 in 40"],
              ["Water-bound macadam and gravel roads", "2.5 to 3.0 %", "1 in 40 to 1 in 33"],
              ["Earth roads", "3.0 to 4.0 %", "1 in 33 to 1 in 25"]],
             widths=[4.4, 2.2, 2.4], align=["l", "c", "c"], fs=7.9, first_bold=True,
             caption="Table 2.4  IRC recommended values of camber. Within each range the "
                     "HIGHER value is adopted in areas of heavy rainfall and the LOWER value "
                     "in areas of light rainfall.")
    S += IRCBOX("Learn these four camber values \u2014 they are asked as a 2-mark question "
                "almost every year. Cement concrete / high-type bituminous 1.7\u20132 %, "
                "thin bituminous 2\u20132.5 %, WBM and gravel 2.5\u20133 %, earth roads "
                "3\u20134 %. Shoulders are given a cross slope 0.5 % steeper than the "
                "camber of the pavement, subject to a minimum of 3 %.")
    S += H3("2.2.3  Width of pavement (carriageway)")
    S += TBL([["Class of road", "Width of carriageway"],
              ["Single lane", "3.75 m"],
              ["Two lanes, without raised kerbs", "7.0 m"],
              ["Two lanes, with raised kerbs", "7.5 m"],
              ["Intermediate carriageway (between single and two lanes)", "5.5 m"],
              ["Multi-lane pavements", "3.5 m per lane"]],
             widths=[5.4, 2.4], align=["l", "c"], fs=8.0, first_bold=True,
             caption="Table 2.5  IRC recommended carriageway widths. "
                     "Note the intermediate width 5.5 m \u2014 a width between 3.75 m and "
                     "5.5 m is NEVER provided, because two vehicles would try to cross "
                     "and neither would have room.")
    S += H3("2.2.4  Other cross-section elements")
    S += TBL([["Element", "Function and recommended value"],
              ["<b>Shoulder</b>",
               "Serves as an emergency lane and as a lateral support to the pavement layers. "
               "Minimum width <b>2.5 m</b> for NH and SH. Cross slope 0.5 % steeper than the "
               "camber, minimum 3 %. It should be rougher than the pavement so that drivers "
               "do not use it as a running lane."],
              ["<b>Kerb</b>",
               "The boundary between the pavement and the shoulder or footpath. "
               "<b>Low or mountable</b> kerb (10 cm) \u2014 vehicles can climb it if needed; "
               "<b>semi-barrier</b> kerb (15 cm) \u2014 discourages encroachment; "
               "<b>barrier</b> kerb (20 cm) \u2014 in built-up areas, prevents vehicles from "
               "leaving the pavement; <b>submerged</b> kerb \u2014 used in rural roads to "
               "give lateral confinement to the pavement."],
              ["<b>Median (traffic separator)</b>",
               "Separates the two directions of traffic and so prevents head-on collisions "
               "and headlight glare. Desirable width 5 m in rural areas; minimum <b>1.2 m</b>, "
               "and where land is very restricted 0.6 m."],
              ["<b>Footpath</b>",
               "Provided in urban roads where the pedestrian volume is significant; "
               "minimum width <b>1.5 m</b>."],
              ["<b>Cycle track</b>", "Minimum width <b>2.0 m</b>, increased by 1 m for "
               "each additional cycle lane."],
              ["<b>Side slopes</b>",
               "Embankment slopes usually 2 : 1 (H : V); cut slopes depend on the soil, "
               "from 1 : 1 in ordinary soil to nearly vertical in hard rock."],
              ["<b>Guard rail / parapet</b>",
               "Provided at the edge of high embankments and on hill roads on the valley "
               "side, for safety."]],
             widths=[1.5, 8.3], align=["l", "l"], fs=7.7,
             caption="Table 2.6  Other cross-section elements.")
    S += PYQ(["What is camber? State its objects, the different shapes and the IRC "
              "recommended values for different surfaces. [7 marks]",
              "Draw a typical cross-section of a two-lane highway in embankment and label "
              "all the elements. [7 marks]",
              "Why is a carriageway width between 3.75 m and 5.5 m never provided? [2 marks]",
              "Differentiate between mountable, semi-barrier and barrier kerbs. [2 marks]"])
    S += REF("Khanna, Justo &amp; Veeraragavan, chapter 'Highway Geometric Design'; "
             "IRC 73\u20131980 (rural highways) and IRC 86\u20131983 (urban roads).")

    # ------------------------------------------------------------------ 2.3
    S += H2("2.3  Sight distance")
    S += DEF("Sight distance", "the length of road visible ahead to the driver at any instant.")
    S += P("Three sight distances are considered in design:")
    S += BUL(["<b>Stopping (absolute minimum) sight distance, SSD</b> \u2014 the distance "
              "required to bring a vehicle to a stop after the driver sights an object on the "
              "carriageway. It must be available on <b>every part</b> of the road.",
              "<b>Overtaking (safe passing) sight distance, OSD</b> \u2014 the distance "
              "required to overtake a slow vehicle safely against the traffic in the "
              "opposite direction.",
              "<b>Intermediate sight distance, ISD</b> \u2014 taken as <b>twice the SSD</b>; "
              "provided where the OSD cannot be economically provided, so that at least a "
              "partial overtaking opportunity exists.",
              "In addition, <b>sight distance at intersections</b> and <b>head-light sight "
              "distance</b> (used in the design of valley curves) are considered."])
    S += H3("2.3.1  Factors on which sight distance depends")
    S += BUL(["The <b>total reaction time</b> of the driver \u2014 explained by the "
              "<b>PIEV theory</b>; IRC takes t = <b>2.5 s</b> for SSD and 2.0 s for OSD.",
              "The <b>speed</b> of the vehicle.",
              "The <b>efficiency of the brakes</b> \u2014 100 % braking efficiency means the "
              "wheels are on the point of skidding.",
              "The <b>frictional resistance</b> between the tyre and the road, f "
              "(design value 0.35 to 0.40, decreasing with speed).",
              "The <b>gradient</b> of the road."])
    S += FIG("f3_piev",
             "Fig. 2.4  PIEV theory \u2014 Perception, Intellection, Emotion, Volition. "
             "The sum of the four is the total reaction time t.")
    S += H3("2.3.2  Stopping sight distance")
    S += P("SSD is the sum of two distances \u2014 the <b>lag (reaction) distance</b> covered "
           "during the reaction time, and the <b>braking distance</b> covered after the "
           "brakes are applied.")
    S += FIG("f2_ssd",
             "Fig. 2.5  Stopping sight distance = lag distance + braking distance. "
             "IRC criteria for measurement: driver's eye height H = 1.2 m, height of the "
             "object h = 0.15 m.")
    S += DERIV("<b>Braking distance.</b> The kinetic energy of the vehicle is destroyed by "
               "the work done against the skid resistance. If the vehicle of weight W moving "
               "at v m/s stops in a distance l, then <br/>"
               "&nbsp;&nbsp;&nbsp;work done against friction = f&middot;W&middot;l &nbsp;=&nbsp; "
               "kinetic energy = &frac12; (W/g) v\u00b2 <br/>"
               "&nbsp;&nbsp;&nbsp;\u21d2 &nbsp; <b>l = v\u00b2 / (2 g f)</b>. <br/>"
               "Adding the lag distance v&middot;t gives SSD = v t + v\u00b2/(2 g f). "
               "Converting v (m/s) to V (km/h) using v = V/3.6 gives the working formula.")
    S += FORMULA(["SSD = 0.278 V t + V\u00b2 / (254 f)                    [V in km/h]",
                  "SSD = v t + v\u00b2 / (2 g f)                              [v in m/s]",
                  "On a gradient:   SSD = 0.278 V t + V\u00b2 / [ 254 (f \u00b1 0.01 n) ]",
                  "Two-way traffic on a single-lane road:   SSD = 2 \u00d7 (SSD for one way)"],
                 label="Stopping sight distance",
                 where=["V = design speed in km/h;  v = design speed in m/s",
                        "t = total reaction time = 2.5 s (IRC)",
                        "f = design coefficient of longitudinal friction "
                        "(0.40 at 20\u201330 km/h, 0.38 at 40, 0.37 at 50, 0.36 at 60, "
                        "0.35 at 65 km/h and above)",
                        "n = gradient in per cent; use + for an ASCENDING gradient and "
                        "\u2212 for a DESCENDING gradient",
                        "g = 9.8 m/s\u00b2"])
    S += TIP("On a descending gradient the friction available is reduced, so the braking "
             "distance and hence the SSD is LONGER. Therefore always design for the "
             "<b>descending</b> gradient. This is the single commonest slip in this topic.")
    S += EX("SSD on a level road and on a single-lane two-way road",
            "Calculate the stopping sight distance for a design speed of 80 km/h for "
            "(a) two-lane two-way traffic and (b) two-way traffic on a single-lane road. "
            "Take t = 2.5 s and f = 0.35.",
            ["#Step 1 \u2014 lag (reaction) distance",
             "$= 0.278 V t = 0.278 \u00d7 80 \u00d7 2.5 = 55.6 m",
             "#Step 2 \u2014 braking distance",
             "$= V\u00b2 / (254 f) = 80\u00b2 / (254 \u00d7 0.35) = 6400 / 88.9 = 72.0 m",
             "#Step 3 \u2014 SSD",
             "$SSD = 55.6 + 72.0 = 127.6 m \u2248 128 m",
             "#Step 4 \u2014 two-way traffic on a single lane",
             "Both vehicles must stop, so twice the SSD is required:",
             "$= 2 \u00d7 127.6 = 255.2 m \u2248 255 m",
             "!(a) SSD for a two-lane road = 128 m  (b) for a single-lane two-way "
             "road = 255 m"])
    S += EX("SSD on a gradient",
            "Calculate the SSD on a highway at a descending gradient of 3 % and at an "
            "ascending gradient of 3 %, for a design speed of 65 km/h. Assume t = 2.5 s "
            "and f = 0.36.",
            ["#Step 1 \u2014 lag distance (the same in both cases)",
             "$= 0.278 \u00d7 65 \u00d7 2.5 = 45.18 m",
             "#Step 2 \u2014 descending gradient (n = \u22123 %)",
             "$Braking distance = 65\u00b2/[254(0.36 \u2212 0.03)] = 4225/(254 \u00d7 0.33) "
             "= 4225/83.82 = 50.41 m",
             "$SSD = 45.18 + 50.41 = 95.6 m",
             "#Step 3 \u2014 ascending gradient (n = +3 %)",
             "$Braking distance = 65\u00b2/[254(0.36 + 0.03)] = 4225/99.06 = 42.65 m",
             "$SSD = 45.18 + 42.65 = 87.8 m",
             "!SSD on the descending gradient = 95.6 m (governs the design); "
             "on the ascending gradient = 87.8 m"])
    S += H3("2.3.3  Overtaking sight distance")
    S += P("OSD is the minimum distance open to the vision of the driver of a vehicle "
           "intending to overtake a slow vehicle ahead, with safety against the traffic "
           "coming in the opposite direction. It is measured along the centre line of the "
           "road, with the height of the eye of the driver and the height of the object "
           "both taken as <b>1.2 m</b>.")
    S += FIG("f2_osd",
             "Fig. 2.6  Overtaking sight distance \u2014 OSD = d\u2081 + d\u2082 + d\u2083. "
             "A is the overtaking vehicle, B the slow vehicle and C the vehicle coming from "
             "the opposite direction.")
    S += P("The manoeuvre is in three parts. <b>d\u2081</b> is the distance travelled by the "
           "overtaking vehicle A during the reaction time t, while it closes up on B and "
           "decides to overtake. <b>d\u2082</b> is the distance travelled by A during the "
           "actual overtaking operation, which takes time T. <b>d\u2083</b> is the distance "
           "travelled in the same time T by the vehicle C coming from the opposite direction.")
    S += FORMULA(["OSD = d\u2081 + d\u2082 + d\u2083",
                  "d\u2081 = 0.278 V\u1d47 t                (t = 2 s)",
                  "d\u2082 = 0.278 V\u1d47 T + 2 s",
                  "d\u2083 = 0.278 V T",
                  "s = 0.7 v\u1d47 + 6              (v\u1d47 in m/s, s in m)",
                  "T = \u221a(4 s / a)   [a in m/s\u00b2]     or   T = \u221a(14.4 s / A)   "
                  "[A in km/h/s]"],
                 label="Overtaking sight distance",
                 where=["V = design speed of the overtaking vehicle in km/h",
                        "V\u1d47 = speed of the overtaken (slow) vehicle; if not given, "
                        "take V\u1d47 = V \u2212 16 km/h",
                        "s = the spacing of the vehicles, taken as 0.7 v\u1d47 + 6 metres",
                        "a = acceleration of the overtaking vehicle",
                        "On a DIVIDED highway or a one-way road, d\u2083 is not required, "
                        "so OSD = d\u2081 + d\u2082"],
                 color="teal")
    S += EX("Overtaking sight distance and the overtaking zone",
            "The design speed of a two-lane two-way highway is 80 km/h. Calculate the "
            "overtaking sight distance and the minimum and desirable lengths of the "
            "overtaking zone. Take the acceleration of the overtaking vehicle as "
            "0.92 m/s\u00b2 and the reaction time as 2 s.",
            ["#Step 1 \u2014 speed of the slow vehicle",
             "$V\u1d47 = V \u2212 16 = 80 \u2212 16 = 64 km/h = 64/3.6 = 17.78 m/s",
             "#Step 2 \u2014 spacing s",
             "$s = 0.7 v\u1d47 + 6 = 0.7 \u00d7 17.78 + 6 = 12.44 + 6 = 18.44 m",
             "#Step 3 \u2014 time of the overtaking operation T",
             "$T = \u221a(4 s / a) = \u221a(4 \u00d7 18.44 / 0.92) = \u221a80.17 = 8.95 s",
             "#Step 4 \u2014 the three distances",
             "$d\u2081 = 0.278 V\u1d47 t = 0.278 \u00d7 64 \u00d7 2 = 35.58 m",
             "$d\u2082 = 0.278 V\u1d47 T + 2 s = 0.278 \u00d7 64 \u00d7 8.95 + 2 \u00d7 18.44 "
             "= 159.27 + 36.88 = 196.15 m",
             "$d\u2083 = 0.278 V T = 0.278 \u00d7 80 \u00d7 8.95 = 199.05 m",
             "#Step 5 \u2014 OSD",
             "$OSD = 35.58 + 196.15 + 199.05 = 430.8 m \u2248 431 m",
             "#Step 6 \u2014 length of the overtaking zone",
             "$Minimum length = 3 \u00d7 OSD = 3 \u00d7 431 = 1293 m",
             "$Desirable length = 5 \u00d7 OSD = 5 \u00d7 431 = 2155 m",
             "!OSD = 431 m ;  overtaking zone \u2014 minimum 1293 m, desirable 2155 m"])
    S += NOTE("<b>Overtaking zone.</b> Where the OSD cannot be provided continuously, "
              "overtaking zones are provided at intervals. The zone is marked by "
              "sign posts SP1 and SP2 placed at a distance equal to the OSD "
              "<i>before</i> the beginning and <i>after</i> the end of the zone. "
              "Minimum length of the zone = 3 &times; OSD, desirable = 5 &times; OSD.")
    S += TBL([["Sight distance", "Height of the driver's eye", "Height of the object"],
              ["Stopping sight distance (SSD)", "1.2 m", "0.15 m"],
              ["Overtaking sight distance (OSD)", "1.2 m", "1.2 m"],
              ["Intermediate sight distance (ISD) = 2 &times; SSD", "1.2 m", "1.2 m"],
              ["Head-light sight distance", "0.75 m (head-light)",
               "0.15 m, with a beam divergence of 1\u00b0 upwards"]],
             widths=[4.2, 2.6, 3.0], align=["l", "c", "c"], fs=7.9, first_bold=True,
             caption="Table 2.7  IRC criteria for measuring sight distance \u2014 a "
                     "favourite 2-mark question.")
    S += PYQ(["Derive an expression for the stopping sight distance. Explain the effect of "
              "gradient on it. [7 marks \u2014 very frequently asked]",
              "Explain, with a neat sketch, the overtaking sight distance and derive the "
              "expression for it. [7 marks \u2014 very frequently asked]",
              "What is an overtaking zone? What are its minimum and desirable lengths? "
              "[2 marks]",
              "State the criteria for measuring SSD and OSD. [2 marks]"])

    # ------------------------------------------------------------------ 2.4
    S += H2("2.4  Design of horizontal alignment")
    S += H3("2.4.1  Centrifugal force and superelevation")
    S += P("A vehicle moving on a horizontal curve of radius R at speed v is acted upon by "
           "an outward <b>centrifugal force P = W v\u00b2/(g R)</b>, acting at the centre of "
           "gravity. The ratio P/W = v\u00b2/(gR) is called the <b>centrifugal ratio</b>. "
           "This force has two effects \u2014 it tends to <b>overturn</b> the vehicle about "
           "the outer wheels, and it tends to make the vehicle <b>skid</b> sideways. To "
           "counteract it, the outer edge of the pavement is raised with respect to the "
           "inner edge; this is called <b>superelevation</b> or <b>banking</b>, e = tan \u03b8 "
           "= E/B.")
    S += FIG("f2_super",
             "Fig. 2.7  Forces acting on a vehicle on a superelevated curve. Resolving "
             "along and perpendicular to the inclined surface gives e + f = V\u00b2/(127 R).")
    S += DERIV("Resolving the forces along the inclined pavement surface, for equilibrium at "
               "the point of impending skidding: <br/>"
               "&nbsp;&nbsp; P cos\u03b8 = W sin\u03b8 + F<sub>A</sub> + F<sub>B</sub> "
               "= W sin\u03b8 + f (R<sub>A</sub> + R<sub>B</sub>) <br/>"
               "&nbsp;&nbsp; and R<sub>A</sub> + R<sub>B</sub> = W cos\u03b8 + P sin\u03b8 <br/>"
               "&nbsp;&nbsp; \u21d2 P cos\u03b8 \u2212 W sin\u03b8 = f (W cos\u03b8 + P sin\u03b8) <br/>"
               "Dividing throughout by W cos\u03b8 and putting tan\u03b8 = e, P/W = v\u00b2/(gR): <br/>"
               "&nbsp;&nbsp; (v\u00b2/gR) \u2212 e = f (1 + e\u00b7v\u00b2/gR). "
               "The term e&middot;v\u00b2/gR is small and is neglected, giving <br/>"
               "&nbsp;&nbsp; <b>e + f = v\u00b2/(g R) = V\u00b2/(127 R)</b>.")
    S += FORMULA(["e + f = v\u00b2 / (g R) = V\u00b2 / (127 R)",
                  "Superelevation for mixed traffic (75 % of design speed, f neglected):",
                  "e = (0.75 V)\u00b2 / (127 R) = V\u00b2 / (225 R)",
                  "Total rise of the outer edge:  E = e \u00d7 B",
                  "Ruling minimum radius:  R = V\u00b2 / [ 127 (e + f) ]"],
                 label="Superelevation",
                 where=["e = rate of superelevation (a ratio, or \u00d7 100 for per cent)",
                        "f = coefficient of lateral friction = 0.15 for design",
                        "V = design speed in km/h, R = radius in m",
                        "B = width of the pavement (including extra widening) in m",
                        "Maximum e = 7 % (1 in 15) for plain and rolling terrain; "
                        "10 % for hill roads not bound by snow; 4 % for urban roads",
                        "Minimum e = the camber of the road, provided for drainage even on "
                        "very flat curves"])
    S += H4("The IRC four-step procedure for designing superelevation")
    S += NUMLIST(["Calculate <b>e for 75 % of the design speed</b>, neglecting friction: "
                  "e = V\u00b2/(225 R). If this is less than or equal to the maximum "
                  "(7 %), <b>provide it</b> (but not less than the camber).",
                  "If the value from step 1 exceeds 7 %, <b>provide e = 7 %</b> "
                  "and go to step 3.",
                  "Check the coefficient of friction actually required at the full design "
                  "speed with e = 0.07: f = V\u00b2/(127 R) \u2212 0.07. "
                  "If f \u2264 0.15, the curve is <b>safe at the full design speed</b> \u2014 "
                  "the design is finished.",
                  "If f &gt; 0.15, the curve is not safe at the design speed. Find the "
                  "restricted (allowable) speed from V\u2090 = \u221a[127 R (0.07 + 0.15)] "
                  "= \u221a(27.94 R) and either restrict the speed by regulatory signs or, "
                  "preferably, <b>increase the radius</b>."],
                 style=BULS)
    S += EX("Design of superelevation by the IRC method",
            "A two-lane highway of 7.0 m carriageway is to have a horizontal curve of "
            "radius 300 m. The design speed is 80 km/h. Design the superelevation and "
            "check whether the curve is safe at the design speed.",
            ["#Step 1 \u2014 e for 75 % of the design speed",
             "$e = V\u00b2/(225 R) = 80\u00b2/(225 \u00d7 300) = 6400/67500 = 0.0948 = 9.48 %",
             "This exceeds the permissible maximum of 7 %.",
             "#Step 2 \u2014 limit the superelevation",
             "$Provide e = 7 % = 0.07",
             "#Step 3 \u2014 check the friction required at the full design speed",
             "$f = V\u00b2/(127 R) \u2212 e = 6400/(127 \u00d7 300) \u2212 0.07",
             "$= 6400/38100 \u2212 0.07 = 0.168 \u2212 0.070 = 0.098",
             "Since f = 0.098 &lt; 0.15, the curve is safe at the full design speed of 80 km/h.",
             "#Step 4 \u2014 total rise of the outer edge",
             "$E = e \u00d7 B = 0.07 \u00d7 7.0 = 0.49 m",
             "(If the extra widening of 0.61 m found in Example 2.6 is included, "
             "B = 7.61 m and E = 0.07 \u00d7 7.61 = 0.53 m.)",
             "!Provide e = 7 % ; the curve is safe at 80 km/h ; rise of the outer edge "
             "E \u2248 0.49 m (0.53 m with extra widening)"])
    S += EX("Ruling minimum radius of a horizontal curve",
            "Calculate the ruling minimum radius and the absolute minimum radius of a "
            "horizontal curve for a national highway in plain terrain. Take e = 7 % and "
            "f = 0.15.",
            ["#Step 1 \u2014 design speeds (Table 2.2)",
             "For a NH in plain terrain: ruling design speed = 100 km/h, "
             "minimum design speed = 80 km/h.",
             "#Step 2 \u2014 ruling minimum radius (at the ruling design speed)",
             "$R = V\u00b2/[127(e+f)] = 100\u00b2/[127(0.07+0.15)] = 10000/27.94 = 357.9 m",
             "#Step 3 \u2014 absolute minimum radius (at the minimum design speed)",
             "$R = 80\u00b2/27.94 = 6400/27.94 = 229.1 m",
             "!Ruling minimum radius \u2248 360 m ; absolute minimum radius \u2248 230 m"])
    S += H3("2.4.2  Extra widening of the pavement on horizontal curves")
    S += P("The pavement is widened on a horizontal curve for two reasons, and the total "
           "extra widening is the sum of the two:")
    S += BUL(["<b>Mechanical widening</b> \u2014 because the rear wheels of a vehicle track "
              "on a smaller radius than the front wheels (<b>off-tracking</b>), so the "
              "vehicle occupies a greater width on a curve than on a straight.",
              "<b>Psychological widening</b> \u2014 extra width provided for psychological "
              "reasons: drivers tend to keep a greater clearance from other vehicles on a "
              "curve, and there is a greater difficulty in steering."])
    S += FIG("f2_widening",
             "Fig. 2.8  Off-tracking of a vehicle on a horizontal curve, which makes "
             "mechanical widening necessary.")
    S += FORMULA(["Mechanical widening:      W\u2098 = n l\u00b2 / (2 R)",
                  "Psychological widening:   W\u209a\u209b = V / (9.5 \u221aR)",
                  "Total extra widening:     W\u2091 = W\u2098 + W\u209a\u209b = "
                  "n l\u00b2/(2R) + V/(9.5 \u221aR)"],
                 label="Extra widening at curves",
                 where=["n = number of traffic lanes",
                        "l = length of the wheel base of the longest vehicle "
                        "(6.1 m for a commercial vehicle as per IRC)",
                        "R = radius of the curve in m,  V = design speed in km/h",
                        "The extra widening is provided half on the inside and half on the "
                        "outside of the curve on a two-lane road (fully on the inside for "
                        "hill roads)"],
                 color="teal")
    S += EX("Extra widening of the pavement at a curve",
            "Calculate the extra widening required for a two-lane pavement on a horizontal "
            "curve of radius 300 m. The design speed is 80 km/h and the longest wheel base "
            "is 6.1 m. What total width should be provided at the curve?",
            ["#Step 1 \u2014 mechanical widening",
             "$W\u2098 = n l\u00b2/(2R) = 2 \u00d7 (6.1)\u00b2/(2 \u00d7 300) "
             "= 2 \u00d7 37.21/600 = 0.124 m",
             "#Step 2 \u2014 psychological widening",
             "$W\u209a\u209b = V/(9.5 \u221aR) = 80/(9.5 \u00d7 \u221a300) "
             "= 80/(9.5 \u00d7 17.32) = 80/164.6 = 0.486 m",
             "#Step 3 \u2014 total extra widening",
             "$W\u2091 = 0.124 + 0.486 = 0.61 m",
             "#Step 4 \u2014 total width at the curve",
             "$= 7.0 + 0.61 = 7.61 m \u2248 7.6 m  (0.305 m on each side)",
             "!Extra widening = 0.61 m ; total width at the curve \u2248 7.6 m"])
    S += H3("2.4.3  Transition curves")
    S += P("A transition curve has a radius that decreases gradually from infinity at the "
           "straight to the radius R of the circular curve. Its <b>functions</b> are:")
    S += BUL(["To introduce the <b>centrifugal force gradually</b>, so that the vehicle and "
              "the passengers are not subjected to a sudden jerk.",
              "To enable the driver to <b>turn the steering gradually</b>, which is both "
              "easier and safer.",
              "To provide a convenient length over which the <b>superelevation and the extra "
              "widening can be introduced gradually</b>.",
              "To improve the <b>aesthetic appearance</b> of the road."])
    S += P("The <b>ideal shape is the spiral (clothoid)</b>, because in a spiral the rate of "
           "change of curvature is constant, which is exactly what is wanted. IRC recommends "
           "the spiral. A cubic parabola or a lemniscate may also be used; the cubic parabola "
           "is easier to set out but is satisfactory only for small deflection angles.")
    S += FIG("f2_transition",
             "Fig. 2.9  Transition curves inserted between the straight and the circular "
             "curve. T.S. = tangent\u2013spiral, S.C. = spiral\u2013circle, "
             "C.S. = circle\u2013spiral, S.T. = spiral\u2013tangent.")
    S += FIG("f2_shift",
             "Fig. 2.10  Inserting a transition pushes the circular curve inward by the "
             "shift S = L\u209b\u00b2/(24R), and the transition curve bisects the shift.")
    S += FORMULA(["The length of the transition curve is the GREATEST of the three:",
                  "(i)  Rate of change of centrifugal acceleration:   "
                  "L = 0.0215 V\u00b3 / (C R),   C = 80/(75 + V)",
                  "(ii) Rate of introduction of superelevation:   "
                  "L = e N (W + W\u2091)  [rotated about the inner edge]",
                  "        or  L = e N (W + W\u2091)/2  [rotated about the centre line]",
                  "     empirically  L = 2.7 V\u00b2/R (plain, rolling)  or  "
                  "L = V\u00b2/R (mountainous, steep)",
                  "(iii) IRC minimum length as specified for the class of road",
                  "Shift:   S = L\u00b2 / (24 R)          Total tangent length = "
                  "(R + S) tan(\u0394/2) + L/2"],
                 label="Length of transition curve",
                 where=["C = allowable rate of change of centrifugal acceleration in "
                        "m/s\u00b3; C = 80/(75+V), subject to 0.5 \u2264 C \u2264 0.8",
                        "N = rate of introduction of superelevation, expressed as 1 in N "
                        "(1 in 150 for plain and rolling terrain, 1 in 60 for mountainous "
                        "and steep terrain)",
                        "W = normal width of the pavement, W\u2091 = extra widening",
                        "\u0394 = deflection angle of the curve"])
    S += EX("Length of the transition curve and the shift",
            "A national highway in plain terrain has a horizontal curve of radius 300 m. "
            "The design speed is 80 km/h, the pavement is 7.0 m wide with an extra widening "
            "of 0.61 m and the superelevation is 7 %. The pavement is rotated about the "
            "centre line. Determine the length of the transition curve and the shift.",
            ["#Criterion (i) \u2014 rate of change of centrifugal acceleration",
             "$C = 80/(75 + V) = 80/(75 + 80) = 80/155 = 0.516 m/s\u00b3   "
             "(lies between 0.5 and 0.8, so acceptable)",
             "$L = 0.0215 V\u00b3/(C R) = 0.0215 \u00d7 80\u00b3/(0.516 \u00d7 300)",
             "$= 0.0215 \u00d7 512000/154.8 = 11008/154.8 = 71.1 m",
             "#Criterion (ii) \u2014 rate of introduction of superelevation",
             "Rotation about the centre line, so the outer edge is raised by E/2:",
             "$E = e (W + W\u2091) = 0.07 \u00d7 (7.0 + 0.61) = 0.07 \u00d7 7.61 = 0.533 m",
             "$Rise of the outer edge above the centre = 0.533/2 = 0.266 m",
             "$With a rate of 1 in 150,  L = 150 \u00d7 0.266 = 39.9 m",
             "(Check by the empirical formula: L = 2.7 V\u00b2/R = 2.7 \u00d7 6400/300 "
             "= 57.6 m)",
             "#Criterion (iii) \u2014 IRC minimum",
             "For a design speed of 80 km/h and R = 300 m the IRC minimum is of the order "
             "of 45\u201350 m, which is less than the value from criterion (i).",
             "#Choose the largest value",
             "$L = greatest of (71.1, 57.6, 39.9) = 71.1 m  \u2192  adopt L = 75 m "
             "(rounded up to a convenient multiple of 5 m)",
             "#Shift",
             "$S = L\u00b2/(24 R) = 75\u00b2/(24 \u00d7 300) = 5625/7200 = 0.78 m",
             "!Length of the transition curve L = 75 m ; shift S = 0.78 m"])
    S += H3("2.4.4  Set-back distance (clearance on horizontal curves)")
    S += P("On a horizontal curve the line of sight is a <b>chord</b>, while the road is an "
           "arc; obstructions such as buildings, trees or the cut slope on the inside of the "
           "curve therefore restrict the visibility. The <b>set-back distance m</b> is the "
           "clearance that must be kept free of obstruction, measured from the centre line "
           "of the road.")
    S += FIG("f2_setback",
             "Fig. 2.11  Set-back distance on a horizontal curve. The sight line is the "
             "chord of the inner-lane centre line.")
    S += FORMULA(["Single-lane road:   m = R \u2212 R cos( S / 2R )",
                  "Multi-lane road:    m = R \u2212 (R \u2212 d) cos[ S / (2 (R \u2212 d)) ]",
                  "When the length of the curve L\u1d9c is LESS than the sight distance S:",
                  "m = R \u2212 (R \u2212 d) cos(\u03b1/2) + "
                  "[(S \u2212 L\u1d9c)/2] sin(\u03b1/2),   \u03b1/2 = L\u1d9c / (2(R \u2212 d))"],
                 label="Set-back distance",
                 where=["m = set-back (clearance) from the centre line of the road, in m",
                        "R = radius of the centre line of the road, in m",
                        "d = distance between the centre line of the road and the centre "
                        "line of the inner lane (= 1.75 m for a 7.0 m two-lane road)",
                        "S = the sight distance to be provided (SSD, ISD or OSD)",
                        "The angle inside the cosine is in RADIANS \u2014 the commonest "
                        "mistake in this problem"],
                 color="plum")
    S += EX("Set-back distance on a horizontal curve",
            "A two-lane road of 7.0 m width has a horizontal curve of radius 300 m and "
            "length 250 m. Calculate the set-back distance required to provide a stopping "
            "sight distance of 128 m.",
            ["#Step 1 \u2014 check which case applies",
             "Length of the curve L\u1d9c = 250 m, which is greater than S = 128 m, "
             "so the first case (L\u1d9c &gt; S) applies.",
             "#Step 2 \u2014 distance of the inner lane centre line",
             "$d = 7.0/4 = 1.75 m,   so  R \u2212 d = 300 \u2212 1.75 = 298.25 m",
             "#Step 3 \u2014 the half angle",
             "$S/[2(R \u2212 d)] = 128/(2 \u00d7 298.25) = 128/596.5 = 0.2146 radian "
             "= 12.29\u00b0",
             "$cos(0.2146 rad) = 0.9771",
             "#Step 4 \u2014 set-back distance",
             "$m = R \u2212 (R \u2212 d) cos[S/(2(R\u2212d))] = 300 \u2212 298.25 "
             "\u00d7 0.9771",
             "$= 300 \u2212 291.42 = 8.58 m",
             "!Set-back distance m \u2248 8.6 m, measured from the centre line of the road. "
             "The area within this distance on the inside of the curve must be kept clear "
             "of obstructions."])
    S += PYQ(["Derive the expression e + f = V\u00b2/127R for superelevation. [7 marks \u2014 "
              "asked very often]",
              "Explain the IRC procedure for the design of superelevation, and design the "
              "superelevation for R = \u2026 and V = \u2026 [14 marks]",
              "Why is extra widening provided at horizontal curves? Derive/state the "
              "expressions for mechanical and psychological widening. [7 marks]",
              "What is a transition curve? State its functions and the three criteria for "
              "determining its length. [7 marks \u2014 asked very often]",
              "Define shift. Prove that the transition curve bisects the shift. [2\u20134 marks]",
              "What is set-back distance? Calculate it for the given data. [7 marks]"])

    # ------------------------------------------------------------------ 2.5
    S += H2("2.5  Design of vertical alignment")
    S += H3("2.5.1  Gradients")
    S += DEF("Gradient", "the rate of rise or fall along the length of the road with respect "
             "to the horizontal, expressed as 1 in n or as a percentage.")
    S += TBL([["Type of gradient", "Meaning"],
              ["<b>Ruling gradient</b>", "The maximum gradient within which the designer "
               "attempts to design the vertical profile of the road. Also called the "
               "<b>design gradient</b>."],
              ["<b>Limiting gradient</b>", "A steeper gradient which may be used where the "
               "topography compels it, and then only for short stretches."],
              ["<b>Exceptional gradient</b>", "A very steep gradient used only in "
               "extraordinary situations, and for stretches not exceeding about 100 m at "
               "a time."],
              ["<b>Minimum gradient</b>", "Needed from the point of view of DRAINAGE, "
               "not of traction: 1 in 500 for concrete drains and 1 in 200 for open soil "
               "drains, so that the water in the side drains flows away."],
              ["<b>Floating gradient</b>", "A gradient on which a vehicle moving with a "
               "certain speed continues to move at the same speed without any tractive "
               "effort."]],
             widths=[1.9, 7.9], align=["l", "l"], fs=7.8,
             caption="Table 2.8  Types of gradient.")
    S += TBL([["Terrain", "Ruling gradient", "Limiting gradient", "Exceptional gradient"],
              ["Plain and rolling", "3.3 % (1 in 30)", "5 % (1 in 20)", "6.7 % (1 in 15)"],
              ["Mountainous and steep terrain, at elevations above 3,000 m",
               "5 % (1 in 20)", "6 % (1 in 16.7)", "7 % (1 in 14.3)"],
              ["Mountainous and steep terrain, up to 3,000 m elevation",
               "6 % (1 in 16.7)", "7 % (1 in 14.3)", "8 % (1 in 12.5)"]],
             widths=[3.6, 2.1, 2.1, 2.1], align=["l", "c", "c", "c"], fs=7.8,
             first_bold=True,
             caption="Table 2.9  IRC recommended gradients \u2014 learn the plain-terrain "
                     "row (3.3 %, 5 %, 6.7 %) at least.")
    S += H3("2.5.2  Grade compensation at horizontal curves")
    S += P("At a horizontal curve the vehicle has to overcome the extra tractive resistance "
           "caused by the curve in addition to that caused by the gradient. To avoid "
           "overloading the vehicle, the gradient is <b>eased (reduced)</b> at the curve; "
           "this reduction is the grade compensation.")
    S += FORMULA(["Grade compensation = (30 + R) / R  per cent",
                  "subject to a maximum of  75 / R  per cent",
                  "Compensated gradient = ruling gradient \u2212 grade compensation"],
                 label="Grade compensation",
                 where=["R = radius of the horizontal curve in m",
                        "Grade compensation is NOT applied to gradients flatter than 4 %, "
                        "because such gradients are easy in any case",
                        "The compensated gradient should not be flatter than 4 %"],
                 color="gold")
    S += EX("Grade compensation at a horizontal curve",
            "The gradient of a road in mountainous terrain is 1 in 20. A horizontal curve of "
            "radius 60 m is to be provided at this location. Determine the compensated "
            "gradient.",
            ["#Step 1 \u2014 the ruling gradient as a percentage",
             "$1 in 20 = (1/20) \u00d7 100 = 5 %   (greater than 4 %, so compensation "
             "IS applicable)",
             "#Step 2 \u2014 grade compensation",
             "$(30 + R)/R = (30 + 60)/60 = 90/60 = 1.5 %",
             "$Maximum permissible = 75/R = 75/60 = 1.25 %",
             "$Therefore adopt the lower value, 1.25 %",
             "#Step 3 \u2014 compensated gradient",
             "$= 5.0 \u2212 1.25 = 3.75 %",
             "This is flatter than 4 %; hence limit the compensated gradient to 4 %.",
             "!Grade compensation = 1.25 % ; compensated gradient = 3.75 %, "
             "restricted to 4 % (= 1 in 25)"])
    S += H3("2.5.3  Vertical curves")
    S += P("A vertical curve is introduced at every change of grade to smooth out the "
           "vertical profile. A <b>summit curve</b> is one with convexity upwards and a "
           "<b>valley (sag) curve</b> one with convexity downwards. The <b>deviation "
           "angle N</b> is the algebraic difference of the two grades "
           "(an ascending grade is +, a descending grade is \u2212).")
    S += FIG("f2_curvetypes",
             "Fig. 2.12  Summit and valley curves produced by the different combinations "
             "of grades.")
    S += H4("Summit curves")
    S += P("The <b>simple parabola</b> is used, because it gives the best riding comfort "
           "(the rate of change of grade is constant) and is easy to lay out. The design "
           "criterion is entirely <b>sight distance</b>; comfort is not a problem on a "
           "summit curve because the centrifugal force acts upwards, opposing gravity.")
    S += FIG("f2_summit",
             "Fig. 2.13  Design of a summit curve, showing both cases. The formula to be "
             "used depends on whether the length of the curve is greater or less than the "
             "sight distance.")
    S += FORMULA(["Case 1 \u2014 the length of the curve is GREATER than the sight distance "
                  "(L &gt; S):",
                  "L = N S\u00b2 / [ 2 ( \u221aH + \u221ah )\u00b2 ]",
                  "      = N S\u00b2 / 4.4   for SSD  (H = 1.2 m, h = 0.15 m)",
                  "      = N S\u00b2 / 9.6   for OSD or ISD  (H = h = 1.2 m)",
                  "Case 2 \u2014 the length of the curve is LESS than the sight distance "
                  "(L &lt; S):",
                  "L = 2 S \u2212 2 ( \u221aH + \u221ah )\u00b2 / N",
                  "      = 2 S \u2212 4.4 / N   for SSD        = 2 S \u2212 9.6 / N   "
                  "for OSD or ISD"],
                 label="Length of a summit curve")
    S += TIP("<b>How to handle the two cases.</b> Assume Case 1 (L &gt; S) first, because it "
             "usually governs. Compute L. If the L you get is indeed greater than S, the "
             "assumption was right and that is the answer. If it comes out less than S, "
             "discard it and recompute with the Case 2 formula, then check again.")
    S += EX("Length of a summit curve for stopping sight distance",
            "A vertical summit curve is formed by an ascending gradient of 1 in 30 meeting a "
            "descending gradient of 1 in 20. Design the length of the summit curve to provide "
            "a stopping sight distance of 128 m for a design speed of 80 km/h. Also find the "
            "length required for an intermediate sight distance.",
            ["#Step 1 \u2014 deviation angle",
             "$n\u2081 = +1/30 = +0.0333,   n\u2082 = \u22121/20 = \u22120.05",
             "$N = n\u2081 \u2212 n\u2082 = 0.0333 \u2212 (\u22120.05) = 0.0833",
             "#Step 2 \u2014 assume L &gt; S and use the Case 1 formula for SSD",
             "$L = N S\u00b2/4.4 = 0.0833 \u00d7 128\u00b2/4.4 = 0.0833 \u00d7 16384/4.4",
             "$= 1364.8/4.4 = 310.2 m",
             "#Step 3 \u2014 check the assumption",
             "L = 310.2 m is greater than S = 128 m, so the assumption L &gt; S is correct.",
             "$Adopt L = 310 m",
             "#Step 4 \u2014 length for the intermediate sight distance",
             "$ISD = 2 \u00d7 SSD = 2 \u00d7 128 = 256 m",
             "$L = N S\u00b2/9.6 = 0.0833 \u00d7 256\u00b2/9.6 = 0.0833 \u00d7 65536/9.6",
             "$= 5459.2/9.6 = 568.7 m   (again greater than S = 256 m, so valid)",
             "!Length of the summit curve for SSD = 310 m ; for ISD = 569 m. "
             "The SSD value is the absolute minimum; provide the ISD length if the "
             "site and the cost permit."])
    S += H4("Valley (sag) curves")
    S += P("On a valley curve the centrifugal force acts <b>downwards</b>, in the same "
           "direction as gravity, so the total pressure on the springs is increased and "
           "<b>riding comfort</b> becomes a design criterion. Also, the critical condition "
           "is at <b>night</b>, when the visibility is limited to the length of road lit by "
           "the head-lights. Hence two criteria:")
    S += NUMLIST(["<b>Comfort criterion</b> \u2014 the allowable rate of change of "
                  "centrifugal acceleration is taken as 0.6 m/s\u00b3.",
                  "<b>Head-light sight distance criterion</b> \u2014 the length of road lit "
                  "by the head-lights must be at least equal to the SSD. Head-light "
                  "height h\u2081 = 0.75 m and the beam is assumed to diverge 1\u00b0 upwards "
                  "(\u03b2 = 1\u00b0)."], style=BULS)
    S += FIG("f2_valley",
             "Fig. 2.14  Valley curve \u2014 the head-light sight distance criterion.")
    S += FORMULA(["Comfort criterion:   L = 0.38 ( N V\u00b3 )^\u00bd",
                  "Head-light sight distance, L &gt; S:   "
                  "L = N S\u00b2 / [ 2 (h\u2081 + S tan \u03b2) ] = N S\u00b2 / "
                  "(1.50 + 0.035 S)",
                  "Head-light sight distance, L &lt; S:   "
                  "L = 2 S \u2212 (1.50 + 0.035 S) / N",
                  "DESIGN FOR THE GREATER OF THE TWO LENGTHS"],
                 label="Length of a valley curve",
                 where=["N = deviation angle, V = design speed in km/h, S = SSD in m",
                        "h\u2081 = 0.75 m (height of the head-light), \u03b2 = 1\u00b0 "
                        "so tan\u03b2 = 0.0175",
                        "The valley curve is made of two similar transitions (a cubic "
                        "parabola) of length L/2 each"],
                 color="teal")
    S += EX("Length of a valley curve",
            "A valley curve is formed by a descending gradient of 1 in 25 meeting an "
            "ascending gradient of 1 in 30. Design the length of the valley curve for a "
            "design speed of 80 km/h. Take the SSD as 128 m.",
            ["#Step 1 \u2014 deviation angle",
             "$n\u2081 = \u22121/25 = \u22120.04,   n\u2082 = +1/30 = +0.0333",
             "$N = n\u2082 \u2212 n\u2081 = 0.0333 + 0.04 = 0.0733",
             "#Step 2 \u2014 comfort criterion",
             "$L = 0.38 (N V\u00b3)^\u00bd = 0.38 \u00d7 (0.0733 \u00d7 80\u00b3)^\u00bd",
             "$= 0.38 \u00d7 (0.0733 \u00d7 512000)^\u00bd = 0.38 \u00d7 (37530)^\u00bd",
             "$= 0.38 \u00d7 193.7 = 73.6 m",
             "#Step 3 \u2014 head-light sight distance criterion (assume L &gt; S)",
             "$L = N S\u00b2/(1.50 + 0.035 S) = 0.0733 \u00d7 16384/(1.50 + 0.035 "
             "\u00d7 128)",
             "$= 1200.9/(1.50 + 4.48) = 1200.9/5.98 = 200.8 m",
             "Check: L = 200.8 m &gt; S = 128 m, so the assumption is correct.",
             "#Step 4 \u2014 adopt the greater value",
             "$L = greater of (73.6, 200.8) = 200.8 m  \u2192  adopt L = 200 m",
             "!Length of the valley curve = 200 m, governed by the head-light sight "
             "distance criterion (as is almost always the case)"])
    S += PYQ(["Design the length of a summit curve for the given gradients and sight "
              "distance. [7 marks \u2014 appears in almost every paper]",
              "What are the two criteria for the design of a valley curve? Design the "
              "length for the given data. [7 marks \u2014 appears very often]",
              "Why is riding comfort a criterion for valley curves but not for summit "
              "curves? [2 marks]",
              "Define ruling, limiting and exceptional gradient. What is grade "
              "compensation? [7 marks]"])

    # ------------------------------------------------------------------ 2.6
    S += H2("2.6  Design of intersections \u2014 an outline")
    S += P("An <b>intersection</b> is the area where two or more roads join or cross. It is "
           "the point at which the capacity of a road system and its safety are usually "
           "decided. Intersections are of two broad kinds:")
    S += BUL(["<b>At-grade intersections</b> \u2014 all the roads meet at the same level: "
              "T, Y, skew, cross, staggered, multi-leg and rotary intersections. The "
              "conflicts are managed by <b>channelization, traffic islands, markings, "
              "signs, signals</b> or a <b>rotary</b>.",
              "<b>Grade-separated intersections (interchanges)</b> \u2014 the crossing roads "
              "are at different levels, connected by ramps: trumpet, diamond, cloverleaf and "
              "rotary interchanges. There is no crossing conflict at all, but the cost and "
              "the land requirement are high."])
    S += P("The <b>objectives</b> of intersection design are to minimise the number and the "
           "severity of the points of conflict, to fix the angle and the point of merging, "
           "to control the speed of the turning traffic, to provide adequate sight distance "
           "(the <b>sight triangle</b>) and to give clear guidance to the driver. "
           "The detailed design of intersections, including the design of a rotary and the "
           "design of traffic signals, is dealt with in <b>Unit 4, \u00a7 4.4 and "
           "\u00a7 4.5</b>.")
    S += REF("Khanna, Justo &amp; Veeraragavan, chapter 'Highway Geometric Design'; "
             "Kadiyali, chapters on geometric design and intersections; "
             "IRC 73\u20131980, IRC 86\u20131983, IRC SP 23 (vertical curves).")
    return S
