"""UNIT 6 - Design of pavements."""
from kit import *


def build():
    S = H1("6", "Design of Pavements", "10 hours \u2022 about 24 % of the paper "
                                       "\u2014 the highest weightage")

    # ------------------------------------------------------------------ 6.1
    S += H2("6.1  Types of pavement")
    S += P("A pavement is a structure that <b>distributes the concentrated wheel load over a "
           "large area of the subgrade</b>, so that the pressure reaching the soil is within "
           "its safe bearing capacity, and provides a smooth, dust-free, skid-resistant "
           "riding surface. Pavements are of two kinds, distinguished by <b>the way they "
           "carry the load</b>.")
    S += FIG("f6_flexrigid",
             "Fig. 6.1  How a flexible pavement and a rigid pavement transmit the wheel load "
             "to the subgrade. <b>This diagram, and the comparison table below, together "
             "make a complete 7-mark answer.</b>")
    S += TBL([["Point of comparison", "Flexible pavement", "Rigid pavement"],
              ["Load transfer mechanism",
               "By <b>grain-to-grain transfer</b> through the points of contact of the "
               "aggregate, layer by layer",
               "By the <b>flexural (beam) action</b> of the slab, which has considerable "
               "flexural rigidity"],
              ["Design is based on", "The <b>strength of the subgrade</b> (CBR)",
               "The <b>flexural strength of the concrete</b> and the modulus of subgrade "
               "reaction K"],
              ["Stress on the subgrade", "Higher, spread over a small area",
               "Very low, spread over a wide area"],
              ["Effect of a weak spot in the subgrade",
               "Reflects at the surface as a depression \u2014 the pavement deforms",
               "The slab bridges over it; no surface depression, but the slab may crack"],
              ["Design life", "Usually 10 to 15 years", "Usually 30 to 40 years"],
              ["Initial cost", "Low", "High"],
              ["Maintenance cost", "High \u2014 frequent renewal of the surfacing",
               "Very low"],
              ["Joints", "No joints required", "Expansion, contraction and longitudinal "
               "joints are essential"],
              ["Temperature stresses", "Negligible", "Significant \u2014 warping and "
               "frictional stresses must be computed"],
              ["Night visibility, skid resistance", "Darker surface, poorer night visibility",
               "Lighter surface, better night visibility"],
              ["Suitability for stage construction", "Very suitable",
               "Not suitable"],
              ["Behaviour under water logging", "Loses strength badly",
               "Not much affected"]],
             widths=[2.4, 3.7, 3.7], align=["l", "l", "l"], fs=7.5, first_bold=True,
             caption="Table 6.1  Flexible pavement compared with rigid pavement.")

    # ------------------------------------------------------------------ 6.2
    S += H2("6.2  Components of a flexible pavement and their functions")
    S += FIG("f6_layers",
             "Fig. 6.2  Components of a flexible pavement. Since the stress decreases with "
             "depth, the strongest and costliest material is placed at the top.")
    S += TBL([["Layer", "Functions"],
              ["<b>Surface course</b> (wearing course + binder course)",
               "Provides a smooth, comfortable and skid-resistant riding surface; resists "
               "the abrasive action of traffic; is <b>impervious</b>, so it keeps surface "
               "water out of the lower layers; and takes the highest wheel-load stresses."],
              ["<b>Base course</b>",
               "The <b>main load-spreading layer</b>. It takes up the stress transmitted "
               "from the surfacing and distributes it to the sub-base; it also provides a "
               "stable platform on which the surfacing is laid."],
              ["<b>Sub-base course</b>",
               "Distributes the load further to the subgrade; acts as a <b>drainage layer</b> "
               "and as an <b>anti-capillary (filter) layer</b> that prevents the intrusion of "
               "the fine subgrade soil into the base course; and provides a working platform "
               "for construction traffic."],
              ["<b>Prepared subgrade</b> (top 500 mm)",
               "The <b>foundation</b> of the pavement. Its strength, measured by the CBR, "
               "decides the total thickness of the crust. It must be compacted to the "
               "specified density and protected from moisture."]],
             widths=[2.3, 7.5], align=["l", "l"], fs=7.7,
             caption="Table 6.2  Functions of each layer of a flexible pavement.")
    S += P("A <b>rigid pavement</b> has fewer layers: the <b>cement concrete slab</b> (the "
           "pavement quality concrete or PQC), a <b>dry lean concrete (DLC) or granular "
           "sub-base</b>, and the <b>prepared subgrade</b>. The slab itself performs the "
           "functions of the surface, base and sub-base of a flexible pavement.")

    # ------------------------------------------------------------------ 6.3
    S += H2("6.3  Factors affecting the design of a flexible pavement")
    S += NUMLIST(["<b>Design wheel load</b> \u2014 the magnitude and repetition of the wheel "
                  "load, the contact pressure, the load on a dual or multiple wheel assembly, "
                  "and the equivalent single wheel load.",
                  "<b>Subgrade soil</b> \u2014 its strength (CBR), its variation with "
                  "moisture, and its volume stability.",
                  "<b>Climatic factors</b> \u2014 rainfall (which raises the water table and "
                  "the subgrade moisture), temperature (which affects the stiffness of the "
                  "bituminous layers), and frost action.",
                  "<b>Pavement component materials</b> \u2014 the strength and stiffness of "
                  "each layer.",
                  "<b>Environmental factors</b> \u2014 the height of the embankment, the depth "
                  "of the water table, and the drainage conditions.",
                  "<b>Special factors</b> \u2014 the behaviour of the pavement under repeated "
                  "loading (fatigue) and the possibility of stage construction."],
                 style=BULS)
    S += H3("6.3.1  Contact pressure and rigidity factor")
    S += FORMULA(["Contact pressure = (load on the wheel) / (contact area)",
                  "Rigidity factor = (contact pressure) / (tyre pressure)",
                  "Radius of the equivalent circular contact area:  "
                  "a = \u221a( P / (\u03c0 p) )"],
                 label="Contact pressure",
                 where=["The rigidity factor is <b>1.0</b> when the tyre pressure is "
                        "7 kg/cm\u00b2",
                        "It is <b>greater than 1</b> for tyre pressures LOWER than "
                        "7 kg/cm\u00b2 and <b>less than 1</b> for HIGHER pressures",
                        "P = load on the wheel, p = tyre pressure, a = radius of the "
                        "contact area"])
    S += H3("6.3.2  Equivalent single wheel load (ESWL)")
    S += P("Heavy vehicles carry the load on a <b>dual wheel assembly</b>. Near the surface "
           "each wheel acts independently, while at a great depth the two overlap completely "
           "and act as one. The <b>ESWL</b> is the load on a single wheel that would produce "
           "the same magnitude of the chosen stress or deflection, at the given depth, as the "
           "dual wheel assembly does.")
    S += FIG("f6_eswl",
             "Fig. 6.3  Graphical determination of the ESWL on a log\u2013log plot.")
    S += FORMULA(["ESWL = P               for  z \u2264 d / 2      "
                  "(the wheels act independently)",
                  "ESWL = 2 P             for  z \u2265 2 S        "
                  "(the wheels act as a single wheel)",
                  "For any intermediate depth, by linear interpolation on the log\u2013log "
                  "plot:",
                  "log\u2081\u2080(ESWL) = log\u2081\u2080 P + "
                  "[ 0.301 \u00d7 log\u2081\u2080(2 z / d) ] / [ log\u2081\u2080(4 S / d) ]"],
                 label="Equivalent single wheel load",
                 where=["P = load on ONE wheel of the dual assembly",
                        "S = centre-to-centre spacing of the two tyres",
                        "d = clear gap between the two tyres = S \u2212 2a",
                        "z = depth below the surface at which the ESWL is required",
                        "0.301 = log\u2081\u2080 2, because the load doubles from P to 2P"])
    S += EX("Equivalent single wheel load at various depths",
            "A dual wheel assembly carries 2,000 kg on each wheel. The centre-to-centre "
            "spacing of the tyres is 30 cm and the tyre pressure is 7 kg/cm\u00b2. "
            "Determine the ESWL at depths of 5 cm, 15 cm, 30 cm and 60 cm.",
            ["#Step 1 \u2014 radius of the contact area",
             "$a = \u221a(P/\u03c0p) = \u221a(2000/(\u03c0 \u00d7 7)) = \u221a(2000/21.99) "
             "= \u221a90.94 = 9.54 cm",
             "#Step 2 \u2014 clear gap between the tyres",
             "$d = S \u2212 2a = 30 \u2212 2 \u00d7 9.54 = 30 \u2212 19.07 = 10.93 cm",
             "$d/2 = 5.46 cm    and    2S = 2 \u00d7 30 = 60 cm",
             "#Step 3 \u2014 the two limiting depths",
             "At z = 5 cm, which is less than d/2 = 5.46 cm:   "
             "<b>ESWL = P = 2000 kg</b>",
             "At z = 60 cm, which equals 2S:   <b>ESWL = 2P = 4000 kg</b>",
             "#Step 4 \u2014 interpolate for z = 15 cm",
             "$log(2z/d) = log(2 \u00d7 15/10.93) = log 2.744 = 0.4382",
             "$log(4S/d) = log(4 \u00d7 30/10.93) = log 10.979 = 1.0406",
             "$log(ESWL) = log 2000 + 0.301 \u00d7 (0.4382/1.0406) = 3.3010 + 0.301 "
             "\u00d7 0.4212",
             "$= 3.3010 + 0.1268 = 3.4278   \u21d2   ESWL = 10^3.4278 = <b>2678 kg</b>",
             "#Step 5 \u2014 interpolate for z = 30 cm",
             "$log(2z/d) = log(60/10.93) = log 5.4895 = 0.7391",
             "$log(ESWL) = 3.3010 + 0.301 \u00d7 (0.7391/1.0406) = 3.3010 + 0.301 "
             "\u00d7 0.7103",
             "$= 3.3010 + 0.2138 = 3.5148   \u21d2   ESWL = <b>3273 kg</b>",
             "!ESWL = 2000 kg at 5 cm ; 2678 kg at 15 cm ; 3273 kg at 30 cm ; "
             "4000 kg at 60 cm. The ESWL rises from P to 2P as the depth increases from "
             "d/2 to 2S."])
    S += H3("6.3.3  Design traffic \u2014 cumulative standard axles (msa)")
    S += P("A flexible pavement fails by <b>fatigue</b> under repeated loading, so the design "
           "traffic is expressed as the <b>cumulative number of standard axles</b> (of "
           "8.16 tonnes or 80 kN) expected during the design life, in <b>million standard "
           "axles (msa)</b>.")
    S += FORMULA(["N = 365 \u00d7 A \u00d7 [ (1 + r)\u207f \u2212 1 ] / r \u00d7 D \u00d7 F",
                  "A = P (1 + r)\u02e3"],
                 label="Design traffic (IRC 37)",
                 where=["N = cumulative number of standard axles during the design life "
                        "(convert to msa by dividing by 10\u2076)",
                        "A = number of commercial vehicles per day (CVPD) in the "
                        "<b>year of completion</b> of construction",
                        "P = present number of CVPD, x = number of years between the "
                        "last count and the year of completion",
                        "r = annual rate of growth of commercial vehicles (as a decimal; "
                        "IRC suggests 5 % minimum, commonly 7.5 %)",
                        "n = design life in years (15 years for NH and SH; 20 years for "
                        "expressways)",
                        "D = lane distribution factor \u2014 1.0 for a single lane; 0.75 for "
                        "a two-lane single carriageway; 0.40 for a four-lane single "
                        "carriageway; 0.75 of the directional traffic for a dual two-lane "
                        "carriageway",
                        "F = vehicle damage factor (VDF) \u2014 the number of standard axles "
                        "per commercial vehicle; it depends on the terrain and the traffic "
                        "volume (indicative values 1.5 to 4.5)"])
    S += EX("Cumulative standard axles for pavement design",
            "A two-lane single-carriageway national highway is to be strengthened. The "
            "present traffic is 1,500 commercial vehicles per day (two-way). The "
            "construction will be completed in 2 years, the annual growth rate of "
            "commercial traffic is 7.5 % and the design life is 15 years. Take the vehicle "
            "damage factor as 4.5. Determine the design traffic in msa.",
            ["#Step 1 \u2014 traffic in the year of completion",
             "$A = P (1 + r)\u02e3 = 1500 \u00d7 (1.075)\u00b2 = 1500 \u00d7 1.1556 "
             "= 1733.4 CVPD",
             "#Step 2 \u2014 the growth factor for the design life",
             "$(1.075)\u00b9\u2075 = 2.9591",
             "$[(1+r)\u207f \u2212 1]/r = (2.9591 \u2212 1)/0.075 = 1.9591/0.075 = 26.12",
             "#Step 3 \u2014 lane distribution factor",
             "For a two-lane single carriageway, D = 0.75",
             "#Step 4 \u2014 cumulative standard axles",
             "$N = 365 \u00d7 1733.4 \u00d7 26.12 \u00d7 0.75 \u00d7 4.5",
             "$= 365 \u00d7 1733.4 = 632,691",
             "$632,691 \u00d7 26.12 = 1.6527 \u00d7 10\u2077",
             "$\u00d7 0.75 = 1.2395 \u00d7 10\u2077",
             "$\u00d7 4.5 = 5.578 \u00d7 10\u2077 standard axles",
             "#Step 5 \u2014 express in msa",
             "$N = 5.578 \u00d7 10\u2077 / 10\u2076 = 55.8 msa",
             "!Design traffic = 55.8 msa. The pavement would be designed for the next "
             "standard step, i.e. 60 msa, using the IRC 37 catalogue or IITPAVE."])

    # ------------------------------------------------------------------ 6.4
    S += H2("6.4  Stresses in flexible pavements")
    S += TBL([["Theory", "Assumptions and result"],
              ["<b>Boussinesq's theory</b> (single layer)",
               "The pavement and the subgrade are treated as ONE homogeneous, isotropic, "
               "elastic half-space. For a point load P the vertical stress at depth z on the "
               "axis is \u03c3\u1dbb = 3P/(2\u03c0z\u00b2). For a circular load of radius a "
               "and pressure p the stress on the axis is "
               "\u03c3\u1dbb = p [1 \u2212 z\u00b3/(a\u00b2 + z\u00b2)^1.5]. "
               "Simple, but the assumption of a single layer is far from the truth."],
              ["<b>Burmister's two-layer theory</b>",
               "The pavement is an elastic layer of modulus E\u2081 and thickness h resting "
               "on a subgrade of modulus E\u2082, with E\u2081 &gt; E\u2082. The deflection "
               "is expressed as \u0394 = 1.5 p a F\u2082 / E\u2082, where the deflection "
               "factor F\u2082 depends on E\u2082/E\u2081 and h/a and is read from "
               "Burmister's charts. It also gives the interface stresses. "
               "Extended by Burmister to three layers."],
              ["<b>Odemark's method of equivalent thickness</b>",
               "A layered system is transformed into an equivalent single layer of the "
               "subgrade material, so that Boussinesq's equations can then be applied."],
              ["<b>Mechanistic\u2013empirical analysis (IRC 37\u20132018)</b>",
               "The pavement is analysed as a multi-layer elastic system (using the program "
               "IITPAVE) to obtain the <b>horizontal tensile strain at the bottom of the "
               "bituminous layer</b> (which controls fatigue cracking) and the "
               "<b>vertical compressive strain at the top of the subgrade</b> (which controls "
               "rutting). These strains are then limited by empirical performance equations."]],
             widths=[2.3, 7.5], align=["l", "l"], fs=7.5,
             caption="Table 6.3  Theories for the analysis of stresses in flexible pavements.")
    S += EX("Vertical stress under a circular load by Boussinesq's theory",
            "A wheel load transmits a pressure of 7 kg/cm\u00b2 over a circular contact area "
            "of radius 15 cm. Determine the vertical stress on the axis of loading at depths "
            "of 30 cm and 60 cm, and comment.",
            ["#Formula",
             "$\u03c3\u1dbb = p [ 1 \u2212 z\u00b3/(a\u00b2 + z\u00b2)^1.5 ]",
             "#At z = 30 cm",
             "$a\u00b2 + z\u00b2 = 15\u00b2 + 30\u00b2 = 225 + 900 = 1125",
             "$(1125)^1.5 = 1125 \u00d7 \u221a1125 = 1125 \u00d7 33.54 = 37,733",
             "$z\u00b3 = 27,000  \u21d2  ratio = 27000/37733 = 0.7155",
             "$\u03c3\u1dbb = 7 (1 \u2212 0.7155) = 7 \u00d7 0.2845 = 1.99 kg/cm\u00b2",
             "#At z = 60 cm",
             "$a\u00b2 + z\u00b2 = 225 + 3600 = 3825",
             "$(3825)^1.5 = 3825 \u00d7 61.85 = 236,565",
             "$z\u00b3 = 216,000  \u21d2  ratio = 216000/236565 = 0.9131",
             "$\u03c3\u1dbb = 7 (1 \u2212 0.9131) = 7 \u00d7 0.0869 = 0.61 kg/cm\u00b2",
             "!\u03c3\u1dbb = 1.99 kg/cm\u00b2 at 30 cm depth and 0.61 kg/cm\u00b2 at 60 cm "
             "depth. The stress falls to about 28 % of the contact pressure at a depth of "
             "2a and to about 9 % at a depth of 4a \u2014 which is exactly why the granular "
             "layers below can be of progressively poorer quality."])

    # ------------------------------------------------------------------ 6.5
    S += H2("6.5  Design methods for flexible pavements")
    S += TBL([["Method", "Basis"],
              ["<b>Group index method</b>",
               "Empirical. The total thickness is read from a chart against the group index "
               "of the subgrade soil and the traffic volume class. Does not use the strength "
               "of the soil directly, and is now obsolete."],
              ["<b>CBR method (IRC 37)</b>",
               "Semi-empirical. The thickness is obtained from design curves plotted "
               "between the CBR of the subgrade and the cumulative standard axles. "
               "<b>This is the method used in India.</b>"],
              ["<b>Triaxial test method</b>",
               "Uses the modulus of elasticity from a triaxial test in an elastic-theory "
               "based thickness equation, with corrections for traffic and saturation."],
              ["<b>McLeod method</b>",
               "Based on plate bearing test results and the logarithm of the number of "
               "load repetitions."],
              ["<b>Burmister's method</b>",
               "Based on the two-layer elastic theory, limiting the surface deflection."]],
             widths=[2.1, 7.7], align=["l", "l"], fs=7.6,
             caption="Table 6.4  Methods of flexible pavement design.")
    S += H3("6.5.1  The IRC 37 design procedure")
    S += NUMLIST(["Determine the <b>subgrade CBR</b> from soaked specimens compacted at the "
                  "field density; take the design value as the lower of the values along "
                  "the stretch.",
                  "Compute the <b>effective resilient modulus</b> of the subgrade: "
                  "M<sub>R</sub> = 10 \u00d7 CBR for CBR \u2264 5 %, and "
                  "M<sub>R</sub> = 17.6 \u00d7 CBR<super>0.64</super> for CBR &gt; 5 % "
                  "(M<sub>R</sub> in MPa).",
                  "Estimate the <b>design traffic in msa</b> from the axle-load survey and "
                  "the traffic count (\u00a7 6.3.3).",
                  "Select the <b>pavement composition</b> \u2014 the thickness of the "
                  "bituminous surfacing, the bituminous base (DBM), the granular base (WMM) "
                  "and the granular sub-base (GSB) \u2014 from the IRC 37 design catalogue, "
                  "or analyse a trial section with <b>IITPAVE</b>.",
                  "Check the trial section against the two performance criteria \u2014 "
                  "the <b>fatigue criterion</b> (horizontal tensile strain at the bottom of "
                  "the bituminous layer) and the <b>rutting criterion</b> (vertical "
                  "compressive strain at the top of the subgrade) \u2014 for the chosen "
                  "reliability.",
                  "Provide the specified <b>minimum thicknesses</b> of each layer and check "
                  "the drainage of the granular sub-base."],
                 style=BULS)
    S += FIG("f6_designchart",
             "Fig. 6.4  The shape of the IRC 37 design curves \u2014 the total thickness "
             "increases with the design traffic and decreases as the subgrade CBR improves.")
    S += TIP("For a numerical in the examination you will normally be asked only for the "
             "<b>design traffic in msa</b> (as in Example 6.2) and sometimes to read a "
             "thickness from a supplied chart. Learn the msa formula thoroughly \u2014 it "
             "is the single most likely numerical from this section.")

    # ------------------------------------------------------------------ 6.6
    S += H2("6.6  Stresses in rigid pavements \u2014 Westergaard's analysis")
    S += P("Westergaard treated the concrete slab as a <b>thin elastic plate resting on a "
           "dense liquid subgrade</b>, i.e. the reaction of the subgrade at any point is "
           "proportional to the deflection at that point (p = K\u0394). The three critical "
           "load positions are the <b>interior, the edge and the corner</b>.")
    S += FIG("f6_westergaard",
             "Fig. 6.5  Westergaard's three critical load positions.")
    S += FORMULA(["Radius of relative stiffness:",
                  "l = [ E h\u00b3 / ( 12 (1 \u2212 \u03bc\u00b2) K ) ]^\u00bc",
                  "Equivalent radius of the resisting section:",
                  "b = \u221a(1.6 a\u00b2 + h\u00b2) \u2212 0.675 h        "
                  "when  a &lt; 1.724 h",
                  "b = a                                          when  a \u2265 1.724 h"],
                 label="Westergaard's parameters",
                 where=["E = modulus of elasticity of the concrete (about 3 \u00d7 "
                        "10\u2075 kg/cm\u00b2)",
                        "h = thickness of the slab (cm)",
                        "\u03bc = Poisson's ratio of concrete (0.15)",
                        "K = modulus of subgrade reaction (kg/cm\u00b3), from the plate "
                        "bearing test",
                        "a = radius of the contact area of the wheel (cm)"])
    S += FORMULA(["Interior loading:   \u03c3\u1d62 = (0.316 P / h\u00b2) "
                  "[ 4 log\u2081\u2080(l/b) + 1.069 ]",
                  "Edge loading:       \u03c3\u2091 = (0.572 P / h\u00b2) "
                  "[ 4 log\u2081\u2080(l/b) + 0.359 ]",
                  "Corner loading:     \u03c3\u1d04 = (3 P / h\u00b2) "
                  "[ 1 \u2212 (a\u221a2 / l)^0.6 ]"],
                 label="Westergaard's stress equations (as modified)",
                 where=["P = design wheel load (kg);  h = slab thickness (cm)",
                        "The stresses come out in kg/cm\u00b2",
                        "For the INTERIOR and EDGE loads the critical tensile stress is at "
                        "the <b>BOTTOM</b> of the slab",
                        "For the CORNER load the critical tensile stress is at the "
                        "<b>TOP</b> of the slab"],
                 color="teal")
    S += EX("Westergaard's stresses at the interior, edge and corner",
            "A cement concrete pavement slab is 25 cm thick and rests on a subgrade of "
            "modulus of reaction K = 8 kg/cm\u00b3. The design wheel load is 5,100 kg with "
            "a contact radius of 15 cm. Take E = 3 \u00d7 10\u2075 kg/cm\u00b2 and "
            "\u03bc = 0.15. Compute the load stresses at the interior, the edge and the "
            "corner, and state which governs.",
            ["#Step 1 \u2014 radius of relative stiffness",
             "$l = [ E h\u00b3 / (12(1 \u2212 \u03bc\u00b2) K) ]^\u00bc",
             "$h\u00b3 = 25\u00b3 = 15,625 ;  1 \u2212 \u03bc\u00b2 = 1 \u2212 0.0225 "
             "= 0.9775",
             "$12 \u00d7 0.9775 \u00d7 8 = 93.84",
             "$E h\u00b3 = 3 \u00d7 10\u2075 \u00d7 15,625 = 4.6875 \u00d7 10\u2079",
             "$l = (4.6875 \u00d7 10\u2079 / 93.84)^\u00bc = (4.995 \u00d7 10\u2077)^\u00bc "
             "= 84.07 cm",
             "#Step 2 \u2014 equivalent radius of the resisting section",
             "$Check: 1.724 h = 1.724 \u00d7 25 = 43.1 cm ;  a = 15 cm &lt; 43.1 cm, "
             "so use the first expression",
             "$b = \u221a(1.6 a\u00b2 + h\u00b2) \u2212 0.675 h = \u221a(1.6 \u00d7 225 "
             "+ 625) \u2212 0.675 \u00d7 25",
             "$= \u221a(360 + 625) \u2212 16.875 = \u221a985 \u2212 16.875 = 31.38 "
             "\u2212 16.88 = 14.51 cm",
             "#Step 3 \u2014 the logarithmic term",
             "$l/b = 84.07/14.51 = 5.794    \u21d2   log\u2081\u2080(l/b) = 0.7630",
             "$4 log\u2081\u2080(l/b) = 3.052",
             "$P/h\u00b2 = 5100/625 = 8.16",
             "#Step 4 \u2014 interior load stress",
             "$\u03c3\u1d62 = 0.316 \u00d7 8.16 \u00d7 (3.052 + 1.069) = 2.579 \u00d7 4.121 "
             "= 10.63 kg/cm\u00b2",
             "#Step 5 \u2014 edge load stress",
             "$\u03c3\u2091 = 0.572 \u00d7 8.16 \u00d7 (3.052 + 0.359) = 4.667 \u00d7 3.411 "
             "= 15.92 kg/cm\u00b2",
             "#Step 6 \u2014 corner load stress",
             "$a\u221a2 / l = 15 \u00d7 1.4142/84.07 = 21.21/84.07 = 0.2523",
             "$(0.2523)^0.6 = 0.4376",
             "$\u03c3\u1d04 = 3 \u00d7 8.16 \u00d7 (1 \u2212 0.4376) = 24.48 \u00d7 0.5624 "
             "= 13.77 kg/cm\u00b2",
             "!\u03c3\u1d62 = 10.63, \u03c3\u2091 = 15.92 and \u03c3\u1d04 = 13.77 "
             "kg/cm\u00b2. The <b>edge load stress governs</b> here. All three are well "
             "below the flexural strength of 45 kg/cm\u00b2 (4.5 MPa), but the warping and "
             "frictional stresses must still be added in the critical combinations."])
    S += H3("6.6.1  Temperature (warping) stresses")
    S += P("The top and bottom of the slab are at different temperatures, so the slab tries "
           "to curl. Its own weight and the friction of the subgrade restrain the curling, "
           "and this restraint induces <b>warping stresses</b>.")
    S += FIG("f6_warping",
             "Fig. 6.6  Warping of a slab by day and by night, and the resulting location "
             "of the tensile stress.")
    S += FORMULA(["Interior:  \u03c3\u209c\u1d62 = (E \u03b1 t / 2) \u00d7 "
                  "[ (C\u2093 + \u03bc C\u1d67) / (1 \u2212 \u03bc\u00b2) ]",
                  "Edge:      \u03c3\u209c\u2091 = C E \u03b1 t / 2",
                  "Corner:    \u03c3\u209c\u1d04 = [ E \u03b1 t / (3 (1 \u2212 \u03bc)) ] "
                  "\u00d7 \u221a(a / l)"],
                 label="Warping stress (Bradbury's coefficients)",
                 where=["\u03b1 = coefficient of thermal expansion of concrete "
                        "\u2248 10 \u00d7 10\u207b\u2076 per \u00b0C",
                        "t = temperature differential between the top and the bottom of "
                        "the slab",
                        "C, C\u2093, C\u1d67 = Bradbury's coefficients, read from a chart "
                        "against L\u2093/l and L\u1d67/l",
                        "L\u2093, L\u1d67 = the two dimensions of the slab panel"],
                 color="plum")
    S += H3("6.6.2  Frictional stresses")
    S += P("As the slab contracts on cooling or on drying shrinkage, the friction of the "
           "subgrade resists the movement and induces a <b>tensile frictional stress</b> in "
           "the slab. It is a maximum at the mid-length of the slab and zero at the free ends.")
    S += FORMULA(["\u03c3\u2091 = W L f / (2 \u00d7 10\u2074)"],
                 label="Frictional stress",
                 where=["\u03c3\u2091 = frictional stress in kg/cm\u00b2",
                        "W = unit weight of concrete \u2248 2400 kg/m\u00b3",
                        "L = length of the slab in metres",
                        "f = coefficient of friction between the slab and the sub-base "
                        "\u2248 1.5",
                        "Note that the slab thickness cancels out \u2014 the frictional "
                        "stress does not depend on h"],
                 color="gold")
    S += H3("6.6.3  Critical combination of stresses")
    S += TBL([["Condition", "Stresses that combine", "Critical location"],
              ["<b>Summer, mid-day</b>",
               "Load stress + warping stress (the slab curls DOWN at the edges, so the "
               "warping tension is at the bottom) \u2212 frictional stress "
               "(the slab is expanding, so friction gives compression)",
               "Bottom of the slab at the EDGE or the INTERIOR"],
              ["<b>Winter, mid-day</b>",
               "Load stress + warping stress + frictional stress (the slab is contracting, "
               "so friction gives tension) \u2014 the <b>worst combination</b>",
               "Bottom of the slab at the EDGE"],
              ["<b>Mid-nights</b>",
               "Load stress + warping stress (the slab curls UP at the edges, so the "
               "warping tension is at the top)",
               "Top of the slab at the CORNER"]],
             widths=[1.7, 5.6, 2.5], align=["l", "l", "l"], fs=7.5,
             caption="Table 6.5  Critical combinations of stress in a rigid pavement.")

    # ------------------------------------------------------------------ 6.7
    S += H2("6.7  Design of joints in cement concrete pavements")
    S += FIG("f6_joints",
             "Fig. 6.7  Joints in a jointed plain concrete pavement, and a section through "
             "an expansion joint showing the dowel bar, the filler and the sealant.")
    S += TBL([["Joint", "Purpose", "Load transfer"],
              ["<b>Expansion joint</b>",
               "To allow the slab to EXPAND in hot weather without buckling; a gap of "
               "20\u201325 mm through the full depth, filled with a compressible filler "
               "board and sealed at the top. Spacing 50 to 60 m.",
               "By <b>dowel bars</b> \u2014 plain round bars, half the length bonded and "
               "half greased with an expansion cap"],
              ["<b>Contraction joint</b>",
               "To relieve the tensile stress caused by CONTRACTION and shrinkage, and so "
               "to control the location of the cracks; usually a dummy groove of one-third "
               "the slab depth. Spacing 3.5 to 4.5 m.",
               "By <b>dowel bars</b>, or by aggregate interlock in thin slabs"],
              ["<b>Longitudinal (warping) joint</b>",
               "Provided between the lanes to relieve the warping stress and to prevent "
               "longitudinal cracking; it also allows for a slight differential settlement.",
               "By <b>tie bars</b> \u2014 deformed bars, fully bonded, which do NOT "
               "transfer load but hold the two slabs together"],
              ["<b>Construction joint</b>",
               "Provided wherever the day's work stops, or at an obstruction.",
               "As for a contraction joint"]],
             widths=[1.8, 5.0, 3.0], align=["l", "l", "l"], fs=7.5,
             caption="Table 6.6  Joints in a cement concrete pavement. Note the key "
                     "difference: DOWEL bars transfer LOAD, TIE bars only hold the slabs "
                     "together.")
    S += FORMULA(["Spacing of expansion joints:      L\u2091 = \u03b4 / (2 \u03b1 \u0394T)",
                  "Spacing of contraction joints (plain slab):",
                  "L\u1d04 = 2 \u00d7 10\u2074 \u00d7 S\u1d04 / (W \u00d7 f)",
                  "Area of tie steel per unit length of the longitudinal joint:",
                  "A\u209b = b f h W / S\u209b",
                  "Length of the tie bar:      L\u209c = S\u209b d / (2 S\u1d47)"],
                 label="Design of joints",
                 where=["\u03b4 = width of the expansion joint gap (cm); "
                        "\u03b1 = 10 \u00d7 10\u207b\u2076/\u00b0C; \u0394T = maximum "
                        "temperature rise",
                        "S\u1d04 = allowable tensile stress in the concrete during curing "
                        "(0.8 kg/cm\u00b2); W = 2400 kg/m\u00b3; f = 1.5",
                        "b = half the width of the slab (i.e. the lane width) in cm, "
                        "h = slab thickness in cm, W = unit weight in kg/cm\u00b3",
                        "S\u209b = allowable tensile stress in the steel; "
                        "S\u1d47 = allowable bond stress; d = diameter of the tie bar"])
    S += EX("Spacing of expansion and contraction joints",
            "A cement concrete pavement is to be laid. (a) Determine the spacing of the "
            "expansion joints if the joint gap is 2.5 cm, the maximum temperature rise is "
            "25 \u00b0C and \u03b1 = 10 \u00d7 10\u207b\u2076 per \u00b0C. "
            "(b) Determine the spacing of the contraction joints for a plain slab, taking "
            "the allowable tensile stress in the concrete during curing as 0.8 kg/cm\u00b2, "
            "the unit weight of concrete as 2,400 kg/m\u00b3 and the coefficient of friction "
            "as 1.5.",
            ["#(a) Spacing of the expansion joints",
             "Each of the two slab ends meeting at the joint can move by \u03b4/2, so",
             "$L\u2091 \u00d7 \u03b1 \u00d7 \u0394T = \u03b4/2",
             "$L\u2091 = \u03b4 / (2 \u03b1 \u0394T) = 2.5 / (2 \u00d7 10 \u00d7 "
             "10\u207b\u2076 \u00d7 25)",
             "$= 2.5 / (5.0 \u00d7 10\u207b\u2074) = 5000 cm = <b>50 m</b>",
             "#(b) Spacing of the contraction joints",
             "The frictional stress at mid-length must not exceed S\u1d04:",
             "$\u03c3\u2091 = W L f/(2 \u00d7 10\u2074) \u2264 S\u1d04",
             "$L\u1d04 = 2 \u00d7 10\u2074 \u00d7 S\u1d04/(W f) = 2 \u00d7 10\u2074 "
             "\u00d7 0.8/(2400 \u00d7 1.5)",
             "$= 16,000/3,600 = 4.44 m",
             "!Expansion joints at 50 m centres; contraction joints at 4.44 m, "
             "adopted as <b>4.5 m</b> \u2014 which is exactly why concrete slab panels are "
             "normally about 4.5 m long. Note that the slab thickness cancels out of the "
             "contraction-joint formula."])
    S += EX("Design of tie bars for a longitudinal joint",
            "Design the tie bars for the longitudinal joint of a cement concrete pavement "
            "25 cm thick with a lane width of 3.5 m. Take the coefficient of friction as "
            "1.5, the unit weight of concrete as 2,400 kg/m\u00b3, the allowable tensile "
            "stress in steel as 1,250 kg/cm\u00b2 and the allowable bond stress as "
            "24.6 kg/cm\u00b2. Use 12 mm diameter deformed bars.",
            ["#Step 1 \u2014 frictional force to be resisted, per cm length of joint",
             "The tie steel must hold the frictional force developed under one lane width:",
             "$W = 2400 kg/m\u00b3 = 2400/10\u2076 = 2.4 \u00d7 10\u207b\u00b3 kg/cm\u00b3",
             "$Force per cm length = f \u00d7 W \u00d7 b \u00d7 h = 1.5 \u00d7 2.4 "
             "\u00d7 10\u207b\u00b3 \u00d7 350 \u00d7 25",
             "$= 1.5 \u00d7 2.4 \u00d7 10\u207b\u00b3 = 3.6 \u00d7 10\u207b\u00b3 ; "
             "\u00d7 350 = 1.26 ; \u00d7 25 = 31.5 kg per cm length",
             "#Step 2 \u2014 area of steel required",
             "$A\u209b = 31.5/1250 = 0.0252 cm\u00b2 per cm length",
             "$= 2.52 cm\u00b2 per metre length of joint",
             "#Step 3 \u2014 spacing of 12 mm bars",
             "$Area of one 12 mm bar = (\u03c0/4)(1.2)\u00b2 = 1.131 cm\u00b2",
             "$Number of bars per metre = 2.52/1.131 = 2.23",
             "$Spacing = 1000/2.23 = 448 mm  \u2192  adopt <b>440 mm centres</b>",
             "#Step 4 \u2014 length of the tie bar",
             "$L\u209c = S\u209b d/(2 S\u1d47) = 1250 \u00d7 1.2/(2 \u00d7 24.6) "
             "= 1500/49.2 = 30.5 cm",
             "Adding an allowance of about 50\u2013100 mm for inaccurate placement, "
             "adopt a length of <b>400 mm</b>.",
             "!Provide 12 mm diameter deformed tie bars, 400 mm long, at 440 mm centres "
             "(IRC 58 in practice specifies 12 mm bars, 480\u2013640 mm long, at "
             "300\u2013600 mm centres, so this design is of the right order)."])
    S += FORMULA(["Load transfer capacity of ONE dowel bar:",
                  "Shear:    P\u209b = 0.785 d\u00b2 F\u209b",
                  "Bending:  P\u2093 = 2 d\u00b3 F\u2093 / (L\u1d48 + 8.8 \u03b4)",
                  "Bearing:  P\u1d47 = F\u1d47 L\u1d48 d / [ 12.5 (L\u1d48 + 1.5 \u03b4) ]"],
                 label="Dowel bar capacity",
                 where=["d = diameter of the dowel bar (cm); L\u1d48 = total embedded "
                        "length; \u03b4 = width of the joint",
                        "F\u209b, F\u2093, F\u1d47 = permissible shear, flexural and "
                        "bearing stresses in the dowel",
                        "The LEAST of the three capacities governs",
                        "The load assumed to be transferred across the joint is taken as "
                        "40 % of the design wheel load, distributed over a length of "
                        "1.8 l on either side of the load"],
                 color="rust")

    # ------------------------------------------------------------------ 6.8
    S += H2("6.8  Design of cement concrete pavements as per IRC 58")
    S += NUMLIST(["Fix the <b>design period</b> (30 years) and compute the "
                  "<b>cumulative repetitions of each axle-load group</b> from the axle-load "
                  "spectrum and the traffic growth rate.",
                  "Determine the <b>effective modulus of subgrade reaction</b> K of the "
                  "subgrade with the sub-base (DLC or granular) in place.",
                  "Assume a <b>trial thickness</b> of the slab.",
                  "Compute the <b>flexural stress</b> for each axle-load group for the two "
                  "critical cases \u2014 <b>bottom-up cracking</b> (axle load at the edge "
                  "in the day, with a positive temperature differential) and "
                  "<b>top-down cracking</b> (axles at the corner at night, with a negative "
                  "temperature differential).",
                  "Compute the <b>stress ratio</b> SR = (flexural stress) / (modulus of "
                  "rupture, 4.5 MPa) and obtain the allowable number of repetitions from "
                  "the <b>fatigue equation</b>.",
                  "Sum the <b>cumulative fatigue damage</b>, CFD = \u03a3 (n\u1d62/N\u1d62). "
                  "The trial thickness is safe if <b>CFD \u2264 1.0</b> for both cracking "
                  "modes; otherwise increase the thickness and repeat.",
                  "Design the <b>joints, the dowel bars and the tie bars</b>, and check the "
                  "sub-base and the drainage layer."],
                 style=BULS)
    S += NOTE("<b>Dry lean concrete (DLC) sub-base.</b> Modern IRC 58 designs place the PQC "
              "slab on a 100\u2013150 mm DLC sub-base with a debonding layer between them. "
              "The DLC greatly increases the effective K value and therefore reduces the "
              "required slab thickness.")
    S += PYQ(["Compare flexible and rigid pavements. Explain how each transmits the wheel "
              "load. [7 marks \u2014 asked very often]",
              "Enumerate the components of a flexible pavement and state the function of "
              "each layer. [7 marks]",
              "What is ESWL? Determine the ESWL at the given depths for a dual wheel "
              "assembly. [14 marks \u2014 asked very often]",
              "Explain the factors affecting the design of a flexible pavement. [7 marks]",
              "Determine the design traffic in msa for the given data. [7 marks]",
              "State Westergaard's assumptions. Compute the interior, edge and corner "
              "stresses for the given data. [14 marks \u2014 asked very often]",
              "Define radius of relative stiffness and equivalent radius of the resisting "
              "section. [2 marks each]",
              "What are warping and frictional stresses? State the critical combinations of "
              "stress. [7 marks]",
              "Explain the different types of joint in a cement concrete pavement. "
              "Distinguish between dowel bars and tie bars. [7 marks]",
              "Design the spacing of expansion and contraction joints / design the tie bars "
              "for the given data. [7 marks]"])
    S += REF("Khanna, Justo &amp; Veeraragavan, chapter 'Design of Pavements'; "
             "Partha Chakraborty &amp; Animesh Das \u2014 <i>Principles of Transportation "
             "Engineering</i> for the analysis of layered systems; "
             "<b>IRC 37\u20132018</b> (flexible pavements), <b>IRC 58\u20132015</b> "
             "(rigid pavements), IRC 15 (construction of concrete roads), "
             "IRC SP 62 (rural roads).")
    return S
