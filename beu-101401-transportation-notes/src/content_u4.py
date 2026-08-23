"""UNIT 4 - Traffic regulation and control, intersections, parking, highway lighting."""
from kit import *


def build():
    S = H1("4", "Traffic Regulation and Control \u00b7 Intersections \u00b7 Parking "
                "\u00b7 Highway Lighting",
           "8 hours \u2022 about 19 % of the paper \u2022 heavy on numericals")

    # ------------------------------------------------------------------ 4.1
    S += H2("4.1  Traffic regulation")
    S += P("Traffic regulations are the legal instruments by which traffic is controlled. In "
           "India the governing legislation is the <b>Motor Vehicles Act, 1988</b> (which "
           "replaced the Act of 1939) together with the Central Motor Vehicle Rules and the "
           "State rules. Regulations fall under three heads:")
    S += TBL([["Regulation of", "What is regulated"],
              ["<b>The driver</b>",
               "Minimum age; the <b>driving licence</b> and its renewal; medical fitness and "
               "eyesight; the professional driver's badge; the number of hours of continuous "
               "driving; prohibition of driving under the influence of drink or drugs; "
               "penalties and the suspension or cancellation of the licence."],
              ["<b>The vehicle</b>",
               "<b>Registration</b> and the certificate of fitness; the maximum "
               "<b>dimensions</b> (width 2.5 m, height 3.8 m, length 11 m for a single unit); "
               "the maximum <b>laden weight and axle load</b> (single axle 10.2 t); brakes, "
               "lights, horn, silencer, mirror, wipers and other essential equipment; "
               "insurance; pollution-under-control certificate."],
              ["<b>The flow of traffic</b>",
               "<b>Speed limits</b> (maximum and sometimes minimum, and separate limits for "
               "different classes of vehicle); <b>one-way</b> regulation; <b>keep-left</b> "
               "rule and lane discipline; the <b>right of way</b> at intersections; "
               "restrictions on <b>overtaking</b>, on <b>turning</b> and on the "
               "<b>use of horns</b>; <b>parking</b> regulations; restriction of the entry of "
               "heavy vehicles to certain hours; regulation of pedestrians and of "
               "slow-moving traffic."]],
             widths=[1.6, 8.2], align=["l", "l"], fs=7.8,
             caption="Table 4.1  The three heads of traffic regulation.")

    # ------------------------------------------------------------------ 4.2
    S += H2("4.2  Traffic control devices")
    S += P("A traffic control device conveys a message to the road user. The four devices are "
           "<b>traffic signs, road markings, traffic islands and traffic signals</b>. Every "
           "device must fulfil four requirements: it must <b>attract attention</b>, convey a "
           "<b>simple and clear meaning</b>, command <b>respect</b>, and give <b>adequate "
           "time</b> for the response.")
    S += H3("4.2.1  Traffic signs (IRC 67)")
    S += FIG("f4_signs",
             "Fig. 4.1  The three classes of traffic sign. The SHAPE identifies the class, "
             "so the driver knows the kind of message before he can read it.")
    S += TBL([["Class", "Shape and colour", "Examples"],
              ["<b>Mandatory / regulatory signs</b>",
               "Circular, with a red border (some are blue circles); the octagonal STOP sign "
               "and the inverted triangle GIVE WAY sign belong to this class",
               "Stop, Give way, No entry, One way, Speed limit, No parking, "
               "Compulsory turn left, Weight limit"],
              ["<b>Cautionary / warning signs</b>",
               "Equilateral triangle with the apex upwards and a red border",
               "Right hand curve, Cross road, Narrow bridge, Steep descent, "
               "Pedestrian crossing, School ahead, Falling rocks"],
              ["<b>Informatory / guide signs</b>",
               "Rectangular",
               "Direction and place identification signs, Destination and distance signs, "
               "Route markers, Public facility signs (petrol pump, hospital, parking, "
               "first aid)"]],
             widths=[2.2, 3.8, 3.8], align=["l", "l", "l"], fs=7.7,
             caption="Table 4.2  Classification of traffic signs. Disobeying a MANDATORY "
                     "sign is a legal offence; a cautionary sign only warns.")
    S += H3("4.2.2  Road markings (IRC 35)")
    S += BUL(["<b>Longitudinal markings</b> \u2014 <b>centre line</b> (a broken line on a "
              "two-lane road), <b>lane lines</b>, <b>no-passing zone markings</b> (a "
              "continuous line, or a continuous line with a broken line beside it, in which "
              "case the traffic on the side of the broken line may cross), "
              "<b>warning lines</b>, <b>edge lines</b> (marking the edge of the carriageway) "
              "and <b>carriageway-width transition markings</b>.",
              "<b>Transverse markings</b> \u2014 <b>stop lines</b>, <b>pedestrian crossings "
              "(zebra crossings)</b>, <b>give-way lines</b> and <b>parking space limits</b>.",
              "<b>Object markings</b> \u2014 markings on physical obstructions within or "
              "adjacent to the carriageway (piers, kerbs, islands), and hazard markers.",
              "<b>Word messages and arrows</b> \u2014 STOP, SLOW, BUS, and lane-use arrows.",
              "Markings are made in white, except no-parking and continuous-line "
              "prohibitions which use yellow."])
    S += H3("4.2.3  Traffic islands")
    S += TBL([["Type of island", "Purpose"],
              ["<b>Divisional island</b>", "Separates opposing flows of traffic, or separates "
               "the traffic on a minor road at a junction, discouraging wrong turns."],
              ["<b>Channelizing island</b>", "Guides the traffic into the proper channel "
               "through the intersection and controls the angle and point of merging."],
              ["<b>Pedestrian refuge island</b>", "Gives the pedestrian a safe place to wait "
               "part way across a wide road."],
              ["<b>Rotary island</b>", "The large central island of a rotary intersection "
               "around which all the traffic circulates."]],
             widths=[2.0, 7.8], align=["l", "l"], fs=7.8,
             caption="Table 4.3  Types of traffic island.")

    # ------------------------------------------------------------------ 4.3
    S += H2("4.3  Traffic signals")
    S += H3("4.3.1  Types, advantages and limitations")
    S += BUL(["<b>Fixed-time (pre-timed) signals</b> \u2014 the cycle and the splits are "
              "fixed in advance; simple and cheap, but cannot adjust to a change in flow.",
              "<b>Vehicle-actuated signals</b> \u2014 detectors in the carriageway extend the "
              "green as long as vehicles keep arriving, up to a maximum; efficient but costly.",
              "<b>Semi-actuated signals</b> \u2014 detectors only on the minor road; the "
              "major road gets the green until a vehicle demands it on the minor road.",
              "<b>Manually operated signals</b> \u2014 operated by a police officer."])
    S += TBL([["Advantages of signals", "Limitations of signals"],
              ["A definite and orderly movement is assured; the crossing conflicts are "
               "separated in TIME instead of in space", "Rear-end collisions may increase"],
              ["The capacity of the intersection is increased and the delay reduced "
               "compared with an uncontrolled junction", "Delay is caused even when the "
               "cross traffic is absent (in a fixed-time signal)"],
              ["Right-angled and pedestrian accidents are reduced", "Improper design or "
               "unwarranted installation causes disrespect and violation"],
              ["Cheaper than manual control or than grade separation; can give priority to "
               "the major road by co-ordination", "Failure of the equipment or a power cut "
               "creates confusion"]],
             widths=[5.0, 4.8], align=["l", "l"], fs=7.7,
             caption="Table 4.4  Advantages and limitations of traffic signals.")
    S += H3("4.3.2  Definitions \u2014 learn these exactly")
    S += TBL([["Term", "Definition"],
              ["<b>Cycle</b>", "One complete sequence of the signal indications."],
              ["<b>Cycle length (C)</b>", "The time in seconds for one complete cycle."],
              ["<b>Interval</b>", "Any part of the cycle during which the signal indication "
               "does not change."],
              ["<b>Change interval (amber)</b>", "The yellow interval between the green and "
               "the red, warning the driver of the impending change; usually 2 to 4 s."],
              ["<b>Clearance (all-red) interval</b>", "The interval during which all "
               "approaches get red, to clear the vehicles already in the intersection."],
              ["<b>Green interval (G)</b>", "The actual duration of the green indication."],
              ["<b>Effective green (g)</b>", "The time actually available for discharge at "
               "the saturation flow rate, after allowing for the lost time."],
              ["<b>Phase</b>", "The part of the cycle allotted to one or more movements "
               "receiving the right of way simultaneously."],
              ["<b>Lost time (L)</b>", "The time in a cycle that is not used for the "
               "effective discharge of traffic \u2014 the start-up delay of each phase "
               "(about 2 s) plus the all-red / inter-green intervals."],
              ["<b>Saturation flow (s)</b>", "The maximum rate of discharge from an approach "
               "during the green, in PCU/h. It depends mainly on the approach width."],
              ["<b>Offset</b>", "The time difference between the start of the green of one "
               "signal and that of the next signal in a co-ordinated system."]],
             widths=[2.0, 7.8], align=["l", "l"], fs=7.7,
             caption="Table 4.5  Signal terminology.")
    S += FIG("f4_signalphase",
             "Fig. 4.2  Two-phase and four-phase signal systems. A two-phase system is used "
             "where the right-turning volumes are small; more phases mean fewer conflicts "
             "but a longer cycle and more lost time.")
    S += H3("4.3.3  Webster's method \u2014 the optimum cycle time")
    S += P("Webster's method is a <b>rational method</b> that minimises the total delay to "
           "all the vehicles at the intersection. It is the method most often asked in the "
           "examination.")
    S += FORMULA(["y\u1d62 = q\u1d62 / s\u1d62               "
                  "Y = \u03a3 y\u1d62  (summed over the phases)",
                  "Total lost time per cycle:   L = 2 n + R",
                  "OPTIMUM CYCLE TIME:   C\u2080 = (1.5 L + 5) / (1 \u2212 Y)",
                  "Effective green of phase i:   g\u1d62 = (y\u1d62 / Y) (C\u2080 \u2212 L)"],
                 label="Webster's method",
                 where=["q\u1d62 = design (normal) flow on the critical approach of phase i, "
                        "in PCU/h",
                        "s\u1d62 = saturation flow of that approach, in PCU/h",
                        "n = number of phases;  the 2 s per phase is the start-up lost time",
                        "R = total all-red (inter-green) time per cycle, in seconds",
                        "C\u2080 is rounded off to the nearest 5 s for convenience of setting",
                        "The method is valid only while Y &lt; 1; if Y \u2265 1 the "
                        "intersection is oversaturated and signals alone cannot help"])
    S += EX("Design of a two-phase signal by Webster's method",
            "A four-arm intersection is to be signalised with a two-phase fixed-time signal. "
            "The design hourly flow and the saturation flow on the critical approach of each "
            "phase are: <br/>"
            "Phase 1 (north\u2013south): q\u2081 = 750 PCU/h, s\u2081 = 2,400 PCU/h <br/>"
            "Phase 2 (east\u2013west): q\u2082 = 600 PCU/h, s\u2082 = 2,000 PCU/h <br/>"
            "The amber (inter-green) time is 3 s per phase. Determine the optimum cycle "
            "time and the signal settings by Webster's method.",
            ["#Step 1 \u2014 the flow ratios",
             "$y\u2081 = q\u2081/s\u2081 = 750/2400 = 0.3125",
             "$y\u2082 = q\u2082/s\u2082 = 600/2000 = 0.3000",
             "$Y = y\u2081 + y\u2082 = 0.3125 + 0.3000 = 0.6125   "
             "(less than 1, so the design is feasible)",
             "#Step 2 \u2014 total lost time per cycle",
             "Number of phases n = 2 ; total inter-green (amber) R = 2 \u00d7 3 = 6 s",
             "$L = 2 n + R = 2 \u00d7 2 + 6 = 10 s",
             "#Step 3 \u2014 optimum cycle time",
             "$C\u2080 = (1.5 L + 5)/(1 \u2212 Y) = (1.5 \u00d7 10 + 5)/(1 \u2212 0.6125)",
             "$= (15 + 5)/0.3875 = 20/0.3875 = 51.6 s",
             "$Adopt a cycle time C = 50 s (rounded to the nearest 5 s)",
             "#Step 4 \u2014 apportion the effective green",
             "$Total effective green available = C \u2212 L = 50 \u2212 10 = 40 s",
             "$g\u2081 = (y\u2081/Y)(C \u2212 L) = (0.3125/0.6125) \u00d7 40 "
             "= 0.5102 \u00d7 40 = 20.4 s  \u2192  say 20 s",
             "$g\u2082 = (y\u2082/Y)(C \u2212 L) = (0.3000/0.6125) \u00d7 40 "
             "= 0.4898 \u00d7 40 = 19.6 s  \u2192  say 20 s",
             "#Step 5 \u2014 the signal setting",
             "$Phase 1:  green 20 s + amber 3 s = 23 s",
             "$Phase 2:  green 20 s + amber 3 s = 23 s",
             "$Total = 23 + 23 = 46 s, plus the start-up lost time of 2 \u00d7 2 = 4 s, "
             "giving the cycle of 50 s",
             "$Red time for phase 1 = C \u2212 (green\u2081 + amber\u2081) = 50 \u2212 23 "
             "= 27 s ;  similarly for phase 2",
             "!Optimum cycle time \u2248 52 s, adopted as C = 50 s. Settings \u2014 "
             "Phase 1: green 20 s, amber 3 s, red 27 s ;  Phase 2: green 20 s, amber 3 s, "
             "red 27 s."])
    S += H3("4.3.4  IRC (approximate) method and the pedestrian requirement")
    S += P("The IRC approximate method fixes the cycle from the <b>pedestrian crossing "
           "requirement</b> and then apportions the green times to the approaches in the "
           "<b>ratio of the approach volumes</b>.")
    S += FORMULA(["Pedestrian green time:  G\u209a = 7 + W / 1.2",
                  "Green time apportioned to an approach:",
                  "G\u2081 = [ q\u2081 / (q\u2081 + q\u2082) ] \u00d7 (total available green)"],
                 label="IRC approximate method",
                 where=["W = width of the carriageway to be crossed, in m",
                        "1.2 m/s = the assumed walking speed of a pedestrian",
                        "7 s = the initial interval, for the pedestrian to start off",
                        "q\u2081, q\u2082 = the approach volumes of the two phases"],
                 color="gold")
    S += EX("Pedestrian green time",
            "Determine the pedestrian green time required to cross a road 15 m wide.",
            ["#Step 1 \u2014 walking time",
             "$= W / 1.2 = 15 / 1.2 = 12.5 s",
             "#Step 2 \u2014 add the initial interval",
             "$G\u209a = 7 + 12.5 = 19.5 s",
             "!Pedestrian green time \u2248 20 s. The cycle must be long enough to "
             "accommodate this in the appropriate phase."])
    S += H3("4.3.5  Co-ordination of traffic signals")
    S += TBL([["System", "How it works", "Comment"],
              ["<b>Simultaneous system</b>",
               "All the signals along the road show the same indication at the same time.",
               "Simplest, but encourages speeding between the signals and gives poor "
               "progression"],
              ["<b>Alternate system</b>",
               "Alternate signals, or groups of signals, show opposite indications.",
               "Better than the simultaneous system, but needs nearly equal spacing "
               "of the signals"],
              ["<b>Simple progressive system</b>",
               "The green periods are offset one from the next in accordance with the "
               "intended speed of progression, but the cycle and the splits are fixed.",
               "Gives a genuine 'green wave' for the design speed"],
              ["<b>Flexible progressive system</b>",
               "The offsets, the cycle length and the splits can all be varied "
               "automatically by a master controller according to the traffic demand.",
               "The best system; used on important urban arterials"]],
             widths=[2.0, 4.8, 3.0], align=["l", "l", "l"], fs=7.6,
             caption="Table 4.6  The four systems of signal co-ordination.")
    S += FIG("f4_timespace",
             "Fig. 4.3  Time\u2013space diagram of a progressive (co-ordinated) signal "
             "system. The offset of each signal is set so that a vehicle travelling at the "
             "design speed meets a green at every signal.")
    S += FORMULA(["Offset of a signal in a progressive system = "
                  "(distance from the first signal) / (speed of progression)",
                  "Ideal spacing of signals for the alternate system:  "
                  "spacing = v \u00d7 C / 2"],
                 label="Signal co-ordination",
                 where=["v = speed of progression in m/s;  C = cycle time in s",
                        "The offset is taken modulo the cycle time"],
                 color="plum")
    S += PYQ(["Explain Webster's method of signal design and design a two-phase signal for "
              "the given data. [14 marks \u2014 appears in almost every paper]",
              "Define cycle, interval, phase, lost time and saturation flow. [7 marks]",
              "What are the different systems of signal co-ordination? Explain with a "
              "time\u2013space diagram. [7 marks]",
              "State the advantages and limitations of traffic signals. [7 marks]",
              "Classify traffic signs with examples. [7 marks]"])

    # ------------------------------------------------------------------ 4.4
    S += H2("4.4  Design of road intersections")
    S += H3("4.4.1  Types of intersection")
    S += FIG("f4_intersecttypes",
             "Fig. 4.4  Types of at-grade intersection. As the number of legs increases the "
             "number of conflict points rises steeply, and a rotary or a grade separation "
             "becomes necessary.")
    S += P("<b>Conflicts at an intersection</b> are of three kinds \u2014 <b>crossing, "
           "merging and diverging</b>. The crossing conflict is the most dangerous; the whole "
           "art of intersection design is to remove the crossing conflicts or to convert them "
           "into merging and diverging conflicts.")
    S += H3("4.4.2  Channelization")
    S += P("<b>Channelization</b> is the separation or the regulation of the conflicting "
           "traffic movements into definite paths of travel by means of traffic islands, "
           "pavement markings and turning roadways.")
    S += FIG("f4_channel",
             "Fig. 4.5  A channelized T-intersection.")
    S += P("<b>Objects of channelization:</b> to reduce the area of conflict; to fix the "
           "<b>angle and the point of merging or crossing</b>; to control the speed of the "
           "traffic entering the intersection; to protect the vehicles waiting to turn; to "
           "provide a refuge for pedestrians; to discourage the prohibited movements; and to "
           "provide a place for the signs and signals.")
    S += H3("4.4.3  Rotary intersection")
    S += DEF("Rotary (roundabout)", "an enlarged intersection in which the vehicles from the "
             "converging roads are compelled to move round a large central island in one "
             "direction (anticlockwise in India) before they can weave out into the road of "
             "their choice.")
    S += FIG("f4_rotary",
             "Fig. 4.6  Elements of a rotary intersection.")
    S += TBL([["Advantages of a rotary", "Disadvantages of a rotary"],
              ["All the crossing conflicts are converted into merging, weaving and "
               "diverging \u2014 the most dangerous conflict is eliminated",
               "Requires a very large area of land, so it is unsuitable in built-up areas"],
              ["Self-governing; needs no police control or signals, and hence no "
               "recurring cost", "Not suitable when the traffic volume is very high \u2014 "
               "the capacity is limited and long queues form"],
              ["Traffic proceeds at a uniform low speed, so accidents are less severe",
               "Not suitable when the pedestrian volume is high, or where any leg has a "
               "very heavy flow"],
              ["Suitable when the number of legs is between 4 and 7 and the traffic is "
               "fairly evenly distributed", "Unsuitable where a rail level crossing or a "
               "steep gradient is close by; needs a considerable amount of maintenance"]],
             widths=[4.9, 4.9], align=["l", "l"], fs=7.6,
             caption="Table 4.7  Rotary intersection \u2014 advantages and disadvantages.")
    S += H4("Design elements of a rotary (IRC 65)")
    S += TBL([["Element", "Recommended value"],
              ["Design speed", "40 km/h for rural roads, 30 km/h for urban roads"],
              ["Shape of the central island", "Circular for four equal legs; elliptical, "
               "tangent or turbine shapes where the legs are unequal"],
              ["Radius of the entry curve", "20 to 35 m for urban roads; 20 to 25 m "
               "for rural roads"],
              ["Radius of the exit curve", "Usually 1.5 to 2.0 times the entry radius, so "
               "that the vehicles leave quickly"],
              ["Radius of the central island", "About 1.33 times the radius of the "
               "entry curve"],
              ["Weaving angle", "Should be small \u2014 of the order of 15\u00b0 to "
               "20\u00b0; a small weaving angle means a longer, safer weaving section"],
              ["Weaving length", "Minimum 45 m for a design speed of 40 km/h and 30 m "
               "for 30 km/h"],
              ["Width of the carriageway at entry and exit",
               "Entry 5 to 7 m for a two-lane road; the exit is usually made wider "
               "than the entry"],
              ["Width of the rotary roadway (weaving section)",
               "The larger of (i) the width of the widest single entry + 3.5 m and "
               "(ii) the average of the entry widths + 3.5 m"]],
             widths=[3.0, 6.8], align=["l", "l"], fs=7.7,
             caption="Table 4.8  Design elements of a rotary as per IRC 65.")
    S += FORMULA(["Practical capacity of a weaving section of a rotary:",
                  "Q\u209a = 280 w [ 1 + e/w ] [ 1 \u2212 p/3 ] / [ 1 + w/L ]",
                  "p = (b + c) / (a + b + c + d)"],
                 label="Rotary capacity (TRL / Wardrop formula)",
                 where=["Q\u209a = practical capacity of the weaving section, in PCU per hour",
                        "w = weaving width in m  (valid for 6 \u2264 w \u2264 18 m)",
                        "e = average width of the entry and the exit "
                        "= (e\u2081 + e\u2082)/2  (valid for 0.4 \u2264 e/w \u2264 1.0)",
                        "L = length of the weaving section in m  "
                        "(valid for 0.12 \u2264 w/L \u2264 0.4)",
                        "p = proportion of the weaving traffic  "
                        "(valid for 0.4 \u2264 p \u2264 1.0)",
                        "a = traffic entering and leaving without weaving (left turning), "
                        "b and c = the two weaving streams, d = the non-weaving stream"])
    S += EX("Capacity of the weaving section of a rotary",
            "A rotary has a weaving section 12 m wide and 36 m long. The entry width is 8 m "
            "and the exit width 10 m. The traffic approaching the weaving section is: "
            "left-turning (non-weaving) a = 400 PCU/h, the two weaving streams b = 600 PCU/h "
            "and c = 500 PCU/h, and the non-weaving stream d = 300 PCU/h. "
            "Determine the practical capacity of the weaving section.",
            ["#Step 1 \u2014 the geometric parameters",
             "$w = 12 m ;  L = 36 m ;  e = (e\u2081 + e\u2082)/2 = (8 + 10)/2 = 9 m",
             "#Step 2 \u2014 check that the formula is applicable",
             "$w = 12 m  \u2014 lies between 6 and 18 m  (OK)",
             "$e/w = 9/12 = 0.75  \u2014 lies between 0.4 and 1.0  (OK)",
             "$w/L = 12/36 = 0.333  \u2014 lies between 0.12 and 0.4  (OK)",
             "#Step 3 \u2014 proportion of weaving traffic",
             "$p = (b + c)/(a + b + c + d) = (600 + 500)/(400 + 600 + 500 + 300)",
             "$= 1100/1800 = 0.611  \u2014 lies between 0.4 and 1.0  (OK)",
             "#Step 4 \u2014 substitute in the capacity formula",
             "$Q\u209a = 280 \u00d7 12 \u00d7 (1 + 0.75) \u00d7 (1 \u2212 0.611/3) / "
             "(1 + 0.333)",
             "$= 3360 \u00d7 1.75 \u00d7 (1 \u2212 0.2037) / 1.3333",
             "$= 3360 \u00d7 1.75 \u00d7 0.7963 / 1.3333",
             "$= 4682.2 / 1.3333 = 3511.7 PCU/h",
             "#Step 5 \u2014 compare with the demand",
             "$Total traffic through the weaving section = 1800 PCU/h, which is well below "
             "the capacity of 3512 PCU/h, so the rotary is adequate.",
             "!Practical capacity of the weaving section \u2248 3,512 PCU/h"])
    S += H3("4.4.4  Grade-separated intersections (interchanges)")
    S += FIG("f4_interchange",
             "Fig. 4.7  Common types of grade-separated interchange.")
    S += TBL([["Type", "Where used"],
              ["<b>Trumpet</b>", "Three-leg (T) junctions; one loop ramp and one direct ramp"],
              ["<b>Diamond</b>", "Four-leg junctions where land is limited and the minor road "
               "flow is light; the cheapest four-leg type, but some at-grade conflict remains "
               "on the minor road"],
              ["<b>Cloverleaf</b>", "Four-leg junctions carrying heavy traffic; four loop "
               "ramps eliminate every crossing conflict, but a large area is needed and "
               "weaving occurs on the loops"],
              ["<b>Rotary interchange</b>", "Where several roads meet; a rotary is provided "
               "on one level with the through road grade-separated"]],
             widths=[1.5, 8.3], align=["l", "l"], fs=7.8,
             caption="Table 4.9  Types of interchange.")
    S += PYQ(["What is a rotary intersection? State its advantages and disadvantages, and "
              "explain its design elements as per IRC. [14 marks \u2014 asked very often]",
              "Determine the capacity of the weaving section of a rotary for the given data. "
              "[7 marks]",
              "What is channelization? State its objects. [7 marks]",
              "Explain the different types of grade-separated interchange with sketches. "
              "[7 marks]",
              "What are the three types of conflict at an intersection? [2 marks]"])

    # ------------------------------------------------------------------ 4.5
    S += H2("4.5  Design of parking facilities")
    S += H3("4.5.1  Types of parking")
    S += BUL(["<b>On-street (kerb) parking</b> \u2014 parallel parking, and angle parking at "
              "30\u00b0, 45\u00b0, 60\u00b0 or 90\u00b0 to the kerb.",
              "<b>Off-street parking</b> \u2014 surface car parks, multi-storey parking "
              "garages, underground parking, mechanical (automated) parking."])
    S += FIG("f4_parking",
             "Fig. 4.8  On-street parking layouts, with the kerb length required per car "
             "and the formula for the number of cars N.")
    S += TBL([["Layout", "Kerb length per car", "Depth of the bay", "N for a kerb length L"],
              ["Parallel", "5.9 m", "3.0 m", "N = L / 5.9"],
              ["30\u00b0", "5.0 m", "4.3 m", "N = (L \u2212 1.77) / 5.0"],
              ["45\u00b0", "3.54 m", "5.0 m", "N = (L \u2212 3.54) / 3.54"],
              ["60\u00b0", "2.89 m", "5.4 m", "N = (L \u2212 4.6) / 2.89"],
              ["90\u00b0 (right angle)", "2.5 m", "5.0 m", "N = L / 2.5"]],
             widths=[1.8, 2.2, 1.8, 3.0], align=["l", "c", "c", "l"], fs=7.9,
             first_bold=True,
             caption="Table 4.10  Kerb parking \u2014 based on a design car 5.0 m \u00d7 "
                     "2.5 m. Parallel parking accommodates the FEWEST cars per metre of "
                     "kerb but obstructs the carriageway least; 90\u00b0 parking "
                     "accommodates the most but takes the greatest width.")
    S += EX("Number of cars that can be parked along a kerb",
            "A kerb length of 60 m is available for parking. Determine the number of cars "
            "that can be parked if the parking is (a) parallel, (b) at 45\u00b0 and "
            "(c) at 90\u00b0 to the kerb. Comment on the result.",
            ["#(a) Parallel parking",
             "$N = L/5.9 = 60/5.9 = 10.17  \u2192  <b>10 cars</b>",
             "#(b) 45\u00b0 angle parking",
             "$N = (L \u2212 3.54)/3.54 = (60 \u2212 3.54)/3.54 = 56.46/3.54 = 15.95  "
             "\u2192  <b>15 cars</b>",
             "#(c) 90\u00b0 (right-angle) parking",
             "$N = L/2.5 = 60/2.5 = <b>24 cars</b>",
             "#Comment",
             "Right-angle parking accommodates 2.4 times as many cars as parallel parking "
             "in the same kerb length, but it needs a bay depth of 5.0 m against 3.0 m and "
             "the reversing manoeuvre obstructs the through traffic. Parallel parking is "
             "therefore preferred on narrow but busy streets.",
             "!(a) 10 cars  (b) 15 cars  (c) 24 cars"])
    S += H3("4.5.2  Parking statistics")
    S += FORMULA(["Parking accumulation = number of vehicles parked at a given instant",
                  "Parking volume = total number of vehicles parked during a given period",
                  "Parking load = \u03a3 (accumulation \u00d7 time interval)   "
                  "[in vehicle-hours]",
                  "Average parking duration = parking load / parking volume",
                  "Parking turnover = parking volume / number of parking bays",
                  "Parking index (occupancy) = (parking load / parking capacity) \u00d7 100 %",
                  "Parking capacity = (number of bays) \u00d7 (duration of the study)   "
                  "[vehicle-hours]"],
                 label="Parking statistics", color="teal")
    S += EX("Parking load, duration, turnover and parking index",
            "An off-street parking facility with 20 bays was surveyed from 8 a.m. to 4 p.m. "
            "During the 8-hour period 160 vehicles used the facility and the parking load "
            "worked out to 120 vehicle-hours. Determine the average parking duration, the "
            "parking turnover, the parking capacity and the parking index.",
            ["#Step 1 \u2014 average parking duration",
             "$= parking load / parking volume = 120/160 = 0.75 hour = 45 minutes",
             "#Step 2 \u2014 parking turnover",
             "$= parking volume / number of bays = 160/20 = 8 vehicles per bay "
             "in the 8-hour period",
             "$= 8/8 = 1 vehicle per bay per hour",
             "#Step 3 \u2014 parking capacity (the space-hours available)",
             "$= number of bays \u00d7 duration of the study = 20 \u00d7 8 = "
             "160 vehicle-hours",
             "#Step 4 \u2014 parking index",
             "$= (parking load / parking capacity) \u00d7 100 = (120/160) \u00d7 100 = 75 %",
             "!Average duration = 45 min ; turnover = 8 vehicles per bay (1 per bay per "
             "hour) ; capacity = 160 vehicle-hours ; parking index = 75 %. An index of "
             "75 % indicates the facility is well used but not saturated."])
    S += NOTE("<b>Ill effects of on-street parking:</b> it reduces the effective width of "
              "the carriageway and hence the capacity; the manoeuvring vehicles cause delay "
              "and accidents; opening doors endanger cyclists and pedestrians; it obstructs "
              "the sight distance at intersections; and it hinders fire-fighting and "
              "ambulance access.")

    # ------------------------------------------------------------------ 4.6
    S += H2("4.6  Highway lighting")
    S += P("<b>Need:</b> about a quarter to a third of the accidents occur at night although "
           "the night traffic is much less; street lighting reduces night accidents, "
           "increases the night capacity, reduces crime and improves the appearance of the "
           "town. It is provided at intersections, on bridges, in tunnels, on curves, at "
           "pedestrian crossings, in built-up areas and at railway level crossings.")
    S += H3("4.6.1  Terms used in lighting")
    S += TBL([["Term", "Meaning", "Unit"],
              ["<b>Luminous flux</b>", "The light energy radiated per unit time by a source, "
               "measured in terms of its visual effect", "lumen"],
              ["<b>Luminous intensity</b>", "The luminous flux radiated per unit solid angle "
               "in a given direction", "candela (cd)"],
              ["<b>Illumination (illuminance)</b>",
               "The luminous flux received per unit area of the surface; "
               "1 lux = 1 lumen/m\u00b2", "lux"],
              ["<b>Luminance (brightness)</b>", "The luminous intensity per unit projected "
               "area of the surface, as seen by the eye", "cd/m\u00b2"],
              ["<b>Coefficient of utilization</b>", "The fraction of the luminous flux of "
               "the lamp that actually reaches the road surface", "a ratio"],
              ["<b>Maintenance factor</b>", "Allows for the depreciation of the light output "
               "due to ageing and to dirt on the fittings; usually 0.8", "a ratio"]],
             widths=[2.0, 6.4, 1.4], align=["l", "l", "c"], fs=7.7,
             caption="Table 4.11  Lighting terminology.")
    S += H3("4.6.2  Design of the spacing of lamps")
    S += FIG("f4_lighting",
             "Fig. 4.9  Layouts for highway lighting \u2014 single-side, staggered, "
             "opposite (paired) and central (span) mounting.")
    S += FORMULA(["Average illumination  E = (F \u00d7 CU \u00d7 MF) / (W \u00d7 S)",
                  "\u21d2  Spacing of the lamps  S = (F \u00d7 CU \u00d7 MF) / (E \u00d7 W)"],
                 label="Lamp spacing",
                 where=["E = average illumination required on the road surface, in lux",
                        "F = luminous flux output of one lamp, in lumens",
                        "CU = coefficient of utilization",
                        "MF = maintenance factor (about 0.8)",
                        "W = width of the roadway to be lit, in m",
                        "S = spacing of the lamp posts along the road, in m",
                        "For the OPPOSITE (paired) layout there are two lamps per spacing, "
                        "so the flux F is doubled; for the STAGGERED layout the successive "
                        "lamps are S/2 apart measured along the road"],
                 color="gold")
    S += TBL([["Layout", "When used"],
              ["<b>Single-side mounting</b>", "When the width of the road is less than the "
               "mounting height of the lamp"],
              ["<b>Staggered (zig-zag) mounting</b>", "When the road width is 1 to 1.5 times "
               "the mounting height"],
              ["<b>Opposite (paired) mounting</b>", "When the road width is more than "
               "1.5 times the mounting height"],
              ["<b>Central (span) mounting</b>", "On divided highways, with the poles in the "
               "median; also used for its good appearance"]],
             widths=[2.4, 7.4], align=["l", "l"], fs=7.8,
             caption="Table 4.12  Choice of lighting layout. Typical mounting height "
                     "10 to 12 m and spacing 30 to 50 m on main roads.")
    S += EX("Spacing of street-lighting lamps",
            "Design the spacing of the lamps for a road 7.5 m wide, using lamps of "
            "6,000 lumens mounted on one side only. The average illumination required is "
            "15 lux, the coefficient of utilization is 0.35 and the maintenance factor "
            "is 0.8. What would the spacing be if lamps of 9,000 lumens were used instead?",
            ["#Step 1 \u2014 spacing with 6,000-lumen lamps",
             "$S = (F \u00d7 CU \u00d7 MF)/(E \u00d7 W)",
             "$= (6000 \u00d7 0.35 \u00d7 0.8)/(15 \u00d7 7.5)",
             "$= 1680/112.5 = 14.93 m  \u2192  adopt <b>15 m</b>",
             "#Step 2 \u2014 spacing with 9,000-lumen lamps",
             "$S = (9000 \u00d7 0.35 \u00d7 0.8)/(15 \u00d7 7.5) = 2520/112.5 = 22.4 m  "
             "\u2192  adopt <b>22 m</b>",
             "#Step 3 \u2014 comment",
             "The spacing is directly proportional to the flux of the lamp. Using fewer, "
             "brighter lamps reduces the number of poles and the capital cost, but the "
             "uniformity of the illumination becomes poorer, so the spacing is usually "
             "limited to about 3 to 4 times the mounting height.",
             "!Spacing = 15 m with 6,000-lumen lamps and 22 m with 9,000-lumen lamps"])
    S += PYQ(["Explain the terms lumen, candela, lux and luminance. [2 marks each]",
              "Design the spacing of street lighting lamps for the given data. [7 marks]",
              "Explain the different layouts of highway lighting and state when each is "
              "used. [7 marks]",
              "Define parking accumulation, parking load, parking turnover and parking "
              "index. Solve the given parking survey data. [14 marks]",
              "Compare parallel and 90\u00b0 parking. How many cars can be parked in "
              "\u2026 m of kerb? [7 marks]"])
    S += REF("Kadiyali \u2014 <i>Traffic Engineering and Transport Planning</i>, chapters on "
             "traffic control devices, signals, intersections and parking; "
             "Khanna, Justo &amp; Veeraragavan, chapter 'Traffic Engineering'; "
             "IRC 67 (signs), IRC 35 (markings), IRC 93\u20131985 (signals), "
             "IRC 65\u20132017 (rotaries), IRC SP 41 (intersections), "
             "IRC SP 12 / IS 1944 (lighting).")
    return S
