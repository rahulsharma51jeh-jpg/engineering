"""UNIT 1 - Highway development and planning."""
from kit import *


def build():
    S = H1("1", "Highway Development and Planning", "8 hours \u2022 about 19 % of the paper")

    # ------------------------------------------------------------------ 1.1
    S += H2("1.1  Modes of transportation and the place of roads")
    S += P("Transportation is the movement of men and materials from one place to another. "
           "The four modes are <b>roadways, railways, waterways and airways</b>. Road transport "
           "is the only mode that offers complete <b>door-to-door service</b>, and every other "
           "mode ultimately depends on it for collection and distribution \u2014 which is why "
           "roads carry about 87 % of passenger traffic and 60 % of freight traffic in India.")
    S += TBL([["Point of comparison", "Road transport", "Rail transport"],
              ["Initial cost of the facility", "Low", "Very high"],
              ["Flexibility of route and time", "Complete \u2014 can be changed at will",
               "Fixed route, fixed timetable"],
              ["Door-to-door service", "Possible", "Not possible"],
              ["Economical lead (distance)", "Short and medium leads", "Long leads"],
              ["Suitability for hilly terrain", "Can negotiate steep gradients (up to 1 in 15)",
               "Needs very flat gradients (about 1 in 100)"],
              ["Energy per tonne-km", "Higher", "Lower"],
              ["Speed over long distance", "Lower", "Higher"],
              ["Accident rate", "High", "Low"]],
             widths=[2.6, 3.6, 3.2], align=["l", "l", "l"], first_bold=True,
             caption="Table 1.1  Road transport compared with rail transport.")
    S += PYQ(["State the different modes of transportation and bring out the advantages of "
              "road transport over rail transport. [2 marks / part of a 14-mark question]"])

    # ------------------------------------------------------------------ 1.2
    S += H2("1.2  History of road construction")
    S += H3("1.2.1  Roman roads (about 300 B.C. onwards)")
    S += BUL(["Built primarily for the movement of armies, therefore laid out as "
              "<b>straight lines</b> regardless of the gradient encountered.",
              "Very thick, 0.75 m to 1.2 m, built with heavy stone blocks in several courses.",
              "Constructed <b>below the natural ground level</b>, so surface water and "
              "sub-soil water were not drained \u2014 the great defect of Roman roads.",
              "Nevertheless extremely durable, because of the sheer thickness and the "
              "quality of the workmanship."])
    S += H3("1.2.2  Tresaguet construction, France, 1764")
    S += P("Pierre Tresaguet was the first engineer to develop a <b>cheaper method</b> of "
           "construction by using a smaller thickness of material, and the first to appreciate "
           "the importance of the <b>moisture content of the subgrade</b>. His cross-section "
           "was 30 cm thick in three layers with a cross slope of about 1 in 45, "
           "the camber being obtained by <b>sloping the subgrade itself</b>.")
    S += FIG("f1_tresaguet",
             "Fig. 1.1  Tresaguet's cross-section (1764) \u2014 total thickness 30 cm. "
             "Note that the camber of the finished surface is produced by giving the "
             "subgrade the same cross slope.")
    S += H3("1.2.3  Metcalf construction, England, about 1815")
    S += P("John Metcalf, a blind engineer, built about 290 km of road in England. His work was "
           "similar in principle to Tresaguet's and he insisted on good <b>drainage</b> \u2014 "
           "he provided side ditches and a cross slope to the surface.")
    S += H3("1.2.4  Telford construction, England, 1824")
    S += P("Thomas Telford, founder of the Institution of Civil Engineers, insisted on a "
           "<b>level subgrade</b> and obtained the camber by <b>varying the depth of the stone "
           "foundation</b> \u2014 17 cm at the edges increasing to 22 cm at the centre. He also "
           "specified a maximum gradient of 1 in 20 and fixed the maximum size and shape of "
           "the stones to be used.")
    S += FIG("f1_telford",
             "Fig. 1.2  Telford's cross-section (1824). The subgrade is FLAT; the camber "
             "comes from the varying depth of the hand-packed stone foundation.")
    S += H3("1.2.5  Macadam construction, England, 1827")
    S += P("John Macadam's method was the <b>first scientific method</b> of road construction "
           "and is the basis of the modern water-bound macadam. His two great contributions were:")
    S += BUL(["He recognised that it is the <b>subgrade soil that ultimately carries the "
              "wheel load</b>, and that it must therefore be kept dry and well compacted; the "
              "function of the stone layers is only to spread the load and protect the subgrade.",
              "He recognised that <b>broken stone of a proper size, angular in shape, will "
              "interlock</b> under traffic and form a strong, load-spreading mass. He therefore "
              "fixed the size of the stone in each layer (5 cm, 3.75 cm and 2 cm) and "
              "kept the total thickness down to only 25 cm.",
              "He gave the subgrade and the surface the same cross slope of 1 in 36 so that "
              "water would drain out of the pavement."])
    S += FIG("f1_macadam",
             "Fig. 1.3  Macadam's cross-section (1827) \u2014 total thickness only 25 cm, "
             "in three layers of decreasing stone size.")
    S += TBL([["Feature", "Roman", "Tresaguet", "Telford", "Macadam"],
              ["Year", "300 B.C.", "1764", "1824", "1827"],
              ["Total thickness", "0.75\u20131.2 m", "30 cm", "about 35 cm", "25 cm"],
              ["Subgrade", "Below ground level, undrained",
               "Sloped (gives the camber)", "Flat / level", "Sloped 1 in 36"],
              ["Camber obtained from", "Not provided", "Sloping the subgrade",
               "Varying the depth of the foundation", "Sloping the subgrade and surface"],
              ["Cross slope of surface", "Nil", "1 in 45", "1 in 45", "1 in 36"],
              ["Large foundation stones", "Yes, heavy blocks", "Yes, 17 cm, set on edge",
               "Yes, 17\u201322 cm, hand packed", "<b>NO</b> \u2014 the key difference"],
              ["Basic idea of load transfer", "Thickness alone",
               "Thickness + subgrade drainage", "Stone foundation carries the load",
               "The SUBGRADE carries the load; stones interlock and spread it"]],
             widths=[2.0, 1.9, 1.9, 2.0, 2.4], align=["l", "l", "l", "l", "l"],
             fs=7.4, first_bold=True,
             caption="Table 1.2  Comparison of the historic methods of road construction "
                     "\u2014 a very frequently asked question.")
    S += PYQ(["Describe, with neat sketches, the Tresaguet, Telford and Macadam methods of "
              "road construction and compare them. [14 marks \u2014 asked almost every year "
              "in some form]",
              "What was the most important contribution of Macadam to highway engineering? "
              "[2 marks]"])
    S += REF("Khanna, Justo &amp; Veeraragavan \u2014 <i>Highway Engineering</i>, chapter "
             "'Highway Development and Planning'.")

    # ------------------------------------------------------------------ 1.3
    S += H2("1.3  Highway development in India \u2014 the milestones")
    S += H3("1.3.1  Jayakar Committee, 1927")
    S += P("After the First World War motor traffic increased sharply and the existing roads "
           "proved quite inadequate. The Government of India appointed the <b>Indian Road "
           "Development Committee</b> in 1927 under the chairmanship of <b>Mr. M.R. Jayakar</b>, "
           "which submitted its report in 1928. Its four principal recommendations, and what "
           "each of them produced, are the most examined facts in this unit:")
    S += TBL([["Recommendation of the Jayakar Committee", "Outcome", "Year"],
              ["Road development in the country should be considered as a matter of "
               "<b>national interest</b>, because the provincial and local governments do not "
               "have the resources or the technical knowledge for it",
               "Led to the whole idea of a central road organisation and of national highways",
               "\u2014"],
              ["An <b>extra tax should be levied on petrol</b> from the road users to create "
               "a fund dedicated to road development",
               "<b>Central Road Fund (CRF)</b>", "1929"],
              ["A <b>semi-official technical body</b> should be formed to pool technical "
               "know-how and to act as an advisory body",
               "<b>Indian Roads Congress (IRC)</b>", "1934"],
              ["A <b>research organisation</b> should be instituted to carry out road research",
               "<b>Central Road Research Institute (CRRI)</b>, New Delhi", "1950"]],
             widths=[5.2, 3.4, 0.9], align=["l", "l", "c"], fs=7.8,
             caption="Table 1.3  The Jayakar Committee (1927) and its outcomes.")
    S += H3("1.3.2  Other important milestones")
    S += TBL([["Year", "Milestone"],
              ["1929", "Central Road Fund created (from the extra duty on petrol)."],
              ["1934", "Indian Roads Congress (IRC) formed \u2014 it frames the IRC standards "
                       "and specifications used throughout this subject."],
              ["1939", "Motor Vehicles Act passed (comprehensively revised in <b>1988</b>) \u2014 "
                       "governs registration, licensing, traffic regulation and liability."],
              ["1943", "<b>Nagpur Road Plan</b> \u2014 the first twenty-year road plan, framed "
                       "at the conference of chief engineers held at Nagpur."],
              ["1950", "Central Road Research Institute (CRRI), New Delhi, established."],
              ["1956", "<b>National Highways Act</b> \u2014 declared certain roads to be "
                       "national highways and vested their development in the Central Government."],
              ["1961", "Second twenty-year plan (Bombay Road Plan) begins."],
              ["1973", "National Transport Policy Committee."],
              ["1981", "Third twenty-year plan (Lucknow Road Plan) begins."],
              ["1988", "<b>National Highways Authority of India (NHAI)</b> constituted by an "
                       "Act of Parliament; it became operational in 1995. It develops, "
                       "maintains and manages the national highways."],
              ["1998", "<b>NHDP</b> \u2014 National Highways Development Project launched."],
              ["2000", "<b>PMGSY</b> launched (25 December 2000) and the Central Road Fund Act "
                       "passed, giving the fund statutory backing."],
              ["2017", "<b>Bharatmala Pariyojana</b> approved."]],
             widths=[0.75, 8.8], align=["c", "l"], fs=7.8, first_bold=True,
             caption="Table 1.4  Chronology of highway development in India.")
    S += PYQ(["Discuss the recommendations of the Jayakar Committee and their outcome. [7 marks]",
              "Write short notes on: (i) Central Road Fund (ii) IRC (iii) CRRI (iv) NHAI. "
              "[2 marks each]"])

    # ------------------------------------------------------------------ 1.4
    S += H2("1.4  The twenty-year road development plans")
    S += H3("1.4.1  First plan \u2014 Nagpur Road Plan (1943\u20131963)")
    S += BUL(["Framed at the conference of chief engineers at <b>Nagpur in 1943</b>; it was the "
              "first attempt at a co-ordinated national road programme.",
              "Roads were classified for the first time into <b>five categories</b> \u2014 "
              "National Highways, State Highways, Major District Roads, Other District Roads "
              "and Village Roads.",
              "The road lengths were worked out on the assumption of a <b>star-and-grid "
              "pattern</b> of roads (a rectangular grid of roads with radial roads "
              "superimposed, connecting the market centres).",
              "Target <b>road density = 16 km per 100 km\u00b2</b> of area, giving a total "
              "road length of about 5,32,700 km by 1963. The target was in fact achieved "
              "ahead of time.",
              "A further aim was accessibility \u2014 no village in a developed agricultural "
              "area should be more than about <b>3.2 km</b> from a metalled road."])
    S += FIG("f1_stargrid",
             "Fig. 1.4  The star-and-grid road pattern on which the Nagpur Road Plan "
             "formulae were based.", width=FW * 0.56)
    S += NOTE("Textbooks quote an empirical formula for the Nagpur plan of the form "
              "L = A/8 + B/32 + N + 1.6&nbsp;C + 8&nbsp;D, in which A is the developed "
              "(agricultural) area, B the undeveloped area, and N, C, D are counts of towns "
              "and villages in stated population ranges. <b>The symbols are defined "
              "differently in different books, so if such a formula is set in your paper the "
              "definitions will be printed with it \u2014 use those, and show the substitution "
              "clearly.</b> Numerical questions in BEU papers are far more often based simply "
              "on road density, as in Example 1.1 below.")
    S += H3("1.4.2  Second plan \u2014 Bombay Road Plan (1961\u20131981)")
    S += BUL(["Target <b>road density = 32 km per 100 km\u00b2</b> \u2014 double the "
              "first plan, giving a total of about 10,57,000 km.",
              "For the first time <b>expressways</b> were proposed as a separate category "
              "over and above the national highways.",
              "The plan also aimed at developing a nucleus of an all-India network of "
              "high-quality roads and at connecting all villages to the road system."])
    S += H3("1.4.3  Third plan \u2014 Lucknow Road Plan (1981\u20132001)")
    S += BUL(["Target <b>road density = 82 km per 100 km\u00b2</b>.",
              "Aimed that every village with a population above <b>500</b> be connected by an "
              "all-weather road, and that no part of the country be more than 50 km from a "
              "metalled road.",
              "Proposed an expressway network of about 2,000 km taken out of the "
              "national highway system.",
              "Introduced the idea of planning by the <b>saturation system</b> (maximum "
              "utility system) instead of by an arbitrary formula \u2014 see \u00a7 1.9."])
    S += H3("1.4.4  Road Development Plan \u2014 Vision 2021 and beyond")
    S += P("The <b>Road Development Plan Vision 2021</b> (and the parallel <b>Rural Roads "
           "Development Plan Vision 2025</b>) replaced the twenty-year plans. Their thrust is "
           "no longer merely length but <b>capacity, riding quality, safety and "
           "connectivity</b> \u2014 four-laning and six-laning of corridors, bypasses, "
           "expressways, and all-weather connectivity to every habitation.")
    S += TBL([["Plan", "Period", "Target road density", "Special feature"],
              ["First \u2014 Nagpur", "1943\u20131963", "16 km / 100 km\u00b2",
               "Star-and-grid pattern; five-fold classification of roads introduced"],
              ["Second \u2014 Bombay", "1961\u20131981", "32 km / 100 km\u00b2",
               "Expressways proposed for the first time"],
              ["Third \u2014 Lucknow", "1981\u20132001", "82 km / 100 km\u00b2",
               "Saturation system of planning; villages above population 500 to be connected"],
              ["Vision 2021 / 2025", "after 2001", "Not length-based",
               "Capacity, riding quality, safety, rural connectivity"]],
             widths=[1.7, 1.5, 1.8, 4.6], align=["l", "c", "c", "l"], fs=7.8,
             first_bold=True,
             caption="Table 1.5  The road development plans at a glance \u2014 learn the "
                     "three density figures 16, 32 and 82.")
    S += EX("Road density and the additional length required",
            "A district has a total area of 8,500 km\u00b2 and an existing road length of "
            "1,020 km. (a) Find the present road density. (b) Find the additional road length "
            "needed to achieve the target of the third twenty-year plan.",
            ["#Step 1 \u2014 present road density",
             "Road density is defined as the road length per 100 km\u00b2 of area.",
             "$Density = (1020 / 8500) \u00d7 100 = <b>12.0 km per 100 km\u00b2</b>",
             "#Step 2 \u2014 target length for the third (Lucknow) plan",
             "Target density for the third plan = 82 km per 100 km\u00b2.",
             "$Required length = (82/100) \u00d7 8500 = 6970 km",
             "#Step 3 \u2014 additional length",
             "$Additional length = 6970 \u2212 1020 = 5950 km",
             "!Present density = 12 km/100 km\u00b2 ; additional road length required = 5950 km"])
    S += PYQ(["Explain the three twenty-year road development plans of India and state the "
              "target road density of each. [7 marks]",
              "Define road density. The area of a state is \u2026 and the road length is \u2026 ; "
              "find the additional length needed to reach the third-plan target. [4 marks]"])

    # ------------------------------------------------------------------ 1.5
    S += H2("1.5  Classification of roads")
    S += H3("1.5.1  Classification based on traffic volume and on the load carried")
    S += BUL(["<b>By traffic volume:</b> heavy, medium and light traffic roads.",
              "<b>By load or tonnage:</b> Class I to Class IV, or class A, B, etc., "
              "depending on the tonnes per day carried.",
              "These divisions are arbitrary, because the limits of volume and tonnage are "
              "not standardised \u2014 which is why the functional classification below "
              "is used in practice."])
    S += H3("1.5.2  Nagpur Plan classification (five classes) \u2014 the standard answer")
    S += TBL([["Class", "Function", "Authority responsible"],
              ["<b>National Highways (NH)</b>",
               "Main highways running through the length and breadth of the country, "
               "connecting state capitals, ports, major cities and foreign highways; they are "
               "the arterial routes of the nation.",
               "Central Government / MoRTH, executed through NHAI, state PWDs and BRO"],
              ["<b>State Highways (SH)</b>",
               "Arterial routes of a state, connecting the district headquarters and important "
               "cities of the state with the national highways and with the highways of the "
               "adjacent states.",
               "State Government (PWD)"],
              ["<b>Major District Roads (MDR)</b>",
               "Important roads within a district, connecting the areas of production with the "
               "markets and connecting these with the state highways and national highways.",
               "State Government / Zilla Parishad"],
              ["<b>Other District Roads (ODR)</b>",
               "Roads serving rural areas of production, giving them outlets to the market "
               "centres, taluka headquarters, block development headquarters or other main roads.",
               "Zilla Parishad / district board"],
              ["<b>Village Roads (VR)</b>",
               "Roads connecting the villages, or a group of villages, with each other and "
               "with the nearest road of a higher category.",
               "Panchayat; funded largely through PMGSY"]],
             widths=[1.7, 5.4, 2.4], align=["l", "l", "l"], fs=7.6,
             caption="Table 1.6  The five classes of the Nagpur Plan classification. "
                     "ODR + VR together are called RURAL ROADS.")
    S += H3("1.5.3  Modified (Third Plan) classification \u2014 three classes")
    S += TBL([["Class", "Consists of", "Character"],
              ["<b>Primary system</b>", "Expressways and National Highways",
               "Highest design standards; through traffic at high speed; access controlled"],
              ["<b>Secondary system</b>", "State Highways and Major District Roads",
               "Collects traffic from the tertiary system and feeds it to the primary system"],
              ["<b>Tertiary system (rural roads)</b>", "Other District Roads and Village Roads",
               "Provides accessibility to the land; lowest standards, lowest volumes"]],
             widths=[2.1, 3.3, 4.6], align=["l", "l", "l"], fs=7.8,
             caption="Table 1.7  The modified three-fold classification.")
    S += H3("1.5.4  Classification of urban roads (IRC)")
    S += BUL(["<b>Expressways</b> \u2014 divided highways with full or partial control of "
              "access, for through traffic only; no access to abutting property.",
              "<b>Arterial streets</b> \u2014 for through traffic on a continuous route; "
              "parking, loading and pedestrian crossings are strictly controlled.",
              "<b>Sub-arterial streets</b> \u2014 like arterial streets but with a somewhat "
              "lower level of travel mobility and closer spacing of intersections.",
              "<b>Collector streets</b> \u2014 collect traffic from the local streets and feed "
              "it to the arterial system; some parking permitted.",
              "<b>Local streets</b> \u2014 give direct access to residences, shops and offices; "
              "through traffic is discouraged; free parking and pedestrian movement."])
    S += FIG("f1_roadclass",
             "Fig. 1.5  The two systems of classifying roads in India, and the "
             "IRC classification of urban roads.")
    S += PYQ(["Classify the roads as per the Nagpur Road Plan and state the function and "
              "the authority responsible for each class. [7 marks]",
              "Differentiate between an arterial street and a collector street. [2 marks]",
              "What are rural roads? Which classes constitute them? [2 marks]"])

    # ------------------------------------------------------------------ 1.6
    S += H2("1.6  Current road projects in India")
    S += TBL([["Project", "What it covers"],
              ["<b>NHDP</b> \u2014 National Highways Development Project (1998, NHAI)",
               "<b>Phase I:</b> the <b>Golden Quadrilateral</b>, about 5,846 km of four-laning "
               "connecting Delhi \u2013 Mumbai \u2013 Chennai \u2013 Kolkata.<br/>"
               "<b>Phase II:</b> the <b>North\u2013South corridor</b> (Srinagar to Kanyakumari) "
               "and the <b>East\u2013West corridor</b> (Silchar to Porbandar), about 7,300 km."
               "<br/><b>Phase III:</b> four-laning of about 12,100 km of high-density NH "
               "connecting state capitals and places of tourist and economic importance.<br/>"
               "<b>Phase IV:</b> two-laning with paved shoulders of about 20,000 km.<br/>"
               "<b>Phase V:</b> six-laning of about 6,500 km (mainly the GQ).<br/>"
               "<b>Phase VI:</b> about 1,000 km of expressways.<br/>"
               "<b>Phase VII:</b> ring roads, bypasses, flyovers, grade separators and "
               "other improvements on the NH network."],
              ["<b>Bharatmala Pariyojana</b> (2017)",
               "The umbrella programme that succeeded the NHDP. Phase I covers about "
               "34,800 km made up of <b>economic corridors, inter-corridor and feeder "
               "routes, national corridor efficiency improvement, border and international "
               "connectivity roads, coastal and port connectivity roads, expressways</b>, "
               "and the residual NHDP works."],
              ["<b>PMGSY</b> \u2014 Pradhan Mantri Gram Sadak Yojana (25 December 2000)",
               "A rural connectivity programme: an <b>all-weather road</b> to every "
               "unconnected habitation with a population of <b>500 and above</b> in the "
               "plains and <b>250 and above</b> in hill, tribal and desert areas. Later "
               "phases (PMGSY-II, III) deal with upgradation and consolidation of the "
               "existing rural network."],
              ["<b>Setu Bharatam</b> (2016)",
               "Replacement of level crossings on national highways by road over-bridges "
               "and under-bridges, and the inventory, rating and rehabilitation of old "
               "bridges, to make the NH network free of level crossings."],
              ["<b>Chardham Pariyojana</b>",
               "All-weather improvement of the roads to the four pilgrimage centres in "
               "Uttarakhand."],
              ["<b>SARDP-NE</b>",
               "Special Accelerated Road Development Programme for the North-Eastern region "
               "\u2014 connecting all state capitals and district headquarters of the "
               "north-east by at least two-lane roads."],
              ["<b>Sagarmala</b>",
               "Port-led development, including the road and rail connectivity of ports "
               "(coastal and port connectivity roads overlap with Bharatmala)."]],
             widths=[2.4, 7.4], align=["l", "l"], fs=7.6,
             caption="Table 1.8  Major road projects currently in progress in India.")
    S += TIP("For a 2-mark question, remember three numbers: Golden Quadrilateral \u2248 "
             "5,846 km; NS\u2013EW corridors \u2248 7,300 km; PMGSY threshold population 500 "
             "(250 in hill, tribal and desert areas).")
    S += PYQ(["Write short notes on NHDP and its phases. [7 marks]",
              "What is Bharatmala Pariyojana? [2 marks]",
              "State the objective and the eligibility criterion of PMGSY. [2 marks]"])

    # ------------------------------------------------------------------ 1.7
    S += H2("1.7  Highway alignment")
    S += DEF("Alignment", "the position or the layout of the centre line of the highway on "
                          "the ground. It has a <b>horizontal alignment</b> (the straights and "
                          "the curves in plan) and a <b>vertical alignment</b> (the gradients "
                          "and the vertical curves in profile).")
    S += NOTE("A wrong alignment cannot be corrected later without heavy expenditure on land "
              "acquisition and earthwork. Hence great care is needed at the alignment stage \u2014 "
              "this sentence is worth writing in any alignment answer.")
    S += H3("1.7.1  Requirements of an ideal alignment")
    S += P("The alignment between two terminal stations should be <b>short, easy, safe and "
           "economical</b>:")
    S += BUL(["<b>Short</b> \u2014 the shortest alignment is a straight line, but this is "
              "seldom possible; the aim is to keep the length as near to it as practicable.",
              "<b>Easy</b> \u2014 easy to construct and to maintain with the available "
              "resources, and easy for the vehicles to negotiate: easy gradients and easy curves.",
              "<b>Safe</b> \u2014 safe for traffic (adequate sight distance, gentle curves) "
              "and safe against the failure of embankment and cut slopes.",
              "<b>Economical</b> \u2014 the total cost (initial cost + maintenance cost + "
              "vehicle operation cost) taken together over the design life must be a minimum, "
              "not merely the initial cost."])
    S += H3("1.7.2  Factors controlling the alignment")
    S += TBL([["Factor", "How it controls the alignment"],
              ["<b>Obligatory points</b>",
               "Points <b>through which</b> the alignment must pass \u2014 an intermediate "
               "town, a bridge site, a mountain pass, an existing bridge; and points "
               "<b>through which it must not pass</b> \u2014 religious places, costly "
               "structures, a lake or pond, marshy land, unstable hill features. "
               "Obligatory points may increase the length considerably."],
              ["<b>Traffic</b>",
               "The alignment should be decided on the basis of the origin-and-destination "
               "study, so that it serves the desire lines of the traffic it is meant to carry."],
              ["<b>Geometric design</b>",
               "Gradient, radius of curve and sight distance govern the final alignment; for "
               "example the alignment must be changed if the ruling gradient cannot be "
               "maintained, and a bridge must be approached on a straight and level stretch."],
              ["<b>Economy</b>",
               "The alignment should follow the natural ground as far as possible to balance "
               "cutting and filling, and should avoid deep cuts, high banks and long bridges."],
              ["<b>Other considerations</b>",
               "Drainage and hydrological factors, the availability of construction materials "
               "along the route, the height of the water table, the possibility of subsidence "
               "or landslides, political and administrative boundaries, and the avoidance of "
               "long monotonous straights (which cause driver fatigue)."]],
             widths=[1.8, 8.0], align=["l", "l"], fs=7.8,
             caption="Table 1.9  Factors controlling highway alignment.")
    S += FIG("f1_alignment",
             "Fig. 1.6  Typical reasons for which an alignment departs from the straight "
             "line \u2014 obligatory points, poor soil, a square river crossing, and a "
             "hill feature to be skirted.")
    S += H3("1.7.3  Special considerations for hill roads")
    S += BUL(["<b>Stability of the slopes</b> \u2014 the alignment should be taken along the "
              "side of the hill that is stable; the hill side rather than the valley side.",
              "<b>Hill drainage</b> \u2014 the number of cross-drainage structures should be "
              "kept to a minimum; the alignment should cross streams at the narrowest point.",
              "<b>Geometric standards</b> \u2014 the special standards of gradient, radius "
              "and hairpin bends for hill roads must be observed.",
              "<b>Resisting length</b> \u2014 the alignment should be so chosen that the "
              "total resisting length (which is the sum of the actual length and the "
              "equivalent length of the rise and of the curves) is a minimum.",
              "Avoid <b>excessive rise and fall</b>, which wastes the effort of climbing."])
    S += PYQ(["What are the requirements of an ideal alignment? Discuss the factors that "
              "control the alignment of a highway. [14 marks \u2014 very frequently asked]",
              "What are obligatory points? Give two examples of each kind. [2 marks]",
              "State the special points to be considered in the alignment of hill roads. "
              "[7 marks]"])

    # ------------------------------------------------------------------ 1.8
    S += H2("1.8  Engineering surveys for highway location")
    S += P("The location of a new highway is fixed by four stages of survey, each more "
           "detailed and more expensive than the last, so that unsuitable routes are "
           "eliminated as early and as cheaply as possible.")
    S += TBL([["Stage", "What is done", "Instruments / output"],
              ["<b>1. Map study</b>",
               "Alternative routes are marked on the available topographic maps "
               "(1:50,000 Survey of India sheets). Contours reveal valleys, passes, saddles, "
               "ponds and permanent structures, so that alignments avoiding excessive rise "
               "and fall can be picked out <i>on paper</i>.",
               "Topo sheets; a set of alternative alignments"],
              ["<b>2. Reconnaissance</b>",
               "A rapid field inspection of the whole area between the terminals, to verify "
               "on the ground the alternatives chosen on the map and to collect information "
               "not available on maps \u2014 the nature of the soil and rock, the sources of "
               "materials, the number of cross-drainage works, the highest flood level, "
               "unusual features.",
               "Abney level / hand level, barometer, compass, pedometer, clinometer; "
               "unsuitable routes are rejected"],
              ["<b>3. Preliminary survey</b>",
               "A detailed survey of the two or three surviving alternatives: a rapid "
               "traverse of each, levelling along the centre line, cross-sections, soil "
               "survey, drainage and hydrological data, traffic survey. The alternatives are "
               "then <b>compared economically</b> and the best one chosen.",
               "Theodolite / total station, levelling instrument; plans and profiles of each "
               "alternative, and the economic comparison"],
              ["<b>4. Final location and detailed survey</b>",
               "The centre line of the chosen alignment is transferred from the paper to the "
               "ground and <b>staked out</b>. All the data needed for the working drawings and "
               "estimates are then collected \u2014 longitudinal section, cross-sections at "
               "close intervals, details of every drainage structure, soil profile, and "
               "the land to be acquired.",
               "Total station / theodolite, level; the working drawings and the estimate"]],
             widths=[1.6, 5.6, 2.6], align=["l", "l", "l"], fs=7.5,
             caption="Table 1.10  The four stages of engineering survey for highway location.")
    S += FIG("f1_surveys",
             "Fig. 1.7  The four stages of engineering survey, and the drawings and reports "
             "that make up the highway project.")

    # ------------------------------------------------------------------ 1.9
    S += H2("1.9  Highway project preparation")
    S += H3("1.9.1  Drawings to be prepared")
    S += NUMLIST(["<b>Key map</b> \u2014 shows the proposed road and the existing important "
                  "roads, railways, towns and rivers; scale not less than 1:50,000.",
                  "<b>Index map</b> \u2014 shows the general topography, the alternative "
                  "alignments considered and the one adopted.",
                  "<b>Preliminary survey plans</b> \u2014 showing the details of all the "
                  "alternatives investigated.",
                  "<b>Detailed plan and longitudinal section</b> \u2014 the plan shows the "
                  "alignment, the drainage works, the land width and the buildings; the "
                  "L-section shows the ground line, the formation line, the gradients and "
                  "the vertical curves (the vertical scale is exaggerated).",
                  "<b>Detailed cross-sections</b> \u2014 typical cross-sections plus "
                  "cross-sections at every 50 m to 100 m and at every change of the section.",
                  "<b>Land acquisition plans</b> \u2014 giving the property lines and the "
                  "areas to be acquired, for the revenue authorities.",
                  "<b>Drawings of cross-drainage and other structures</b> \u2014 culverts, "
                  "bridges, retaining walls, breast walls.",
                  "<b>Drawings of road intersections</b>.",
                  "<b>A land plan showing the quarries</b> from which the materials will "
                  "be obtained, with the lead."])
    S += H3("1.9.2  Reports and estimates")
    S += BUL(["The <b>project report</b> containing the necessity and the justification of "
              "the project, the alternatives considered and the reasons for the choice, the "
              "traffic forecast, the design standards adopted, the soil and materials report, "
              "the construction programme and the maintenance proposals.",
              "The <b>detailed estimate</b> of cost, item by item, with the rate analysis.",
              "The <b>economic evaluation</b> \u2014 benefit\u2013cost ratio, net present "
              "value or internal rate of return, to prove that the project is worth doing."])
    S += PYQ(["Enumerate the drawings and reports to be prepared for a new highway project. "
              "[7 marks]",
              "Explain the different engineering surveys carried out for a new highway "
              "alignment. [14 marks \u2014 very frequently asked]"])

    # ------------------------------------------------------------------ 1.10
    S += H2("1.10  Planning surveys and the saturation system")
    S += H3("1.10.1  Planning surveys")
    S += P("Before a road plan can be prepared, four studies are needed \u2014 an "
           "<b>economic study</b> (population, produce, industry, existing facilities), a "
           "<b>financial study</b> (sources of income and the funds available), a "
           "<b>traffic or road-use study</b> (volume, origin and destination, growth) and an "
           "<b>engineering study</b> (topography, soil, materials, drainage and the existing "
           "road condition).")
    S += H3("1.10.2  Saturation system (maximum utility system)")
    S += P("Introduced in the third twenty-year plan for deciding the <b>priority</b> of new "
           "road links. The principle is simple: the road network that gives the "
           "<b>maximum utility per unit length</b> of road is the optimum. Utility is measured "
           "by the population served and the productivity (agricultural and industrial) served. "
           "Utility units are assigned to each, the total for an alignment is divided by its "
           "length, and the alignments are then ranked.")
    S += FORMULA(["Utility per unit length = (total utility units served) / (length of the road)"],
                 label="Saturation system",
                 where=["Utility units are assigned for the population served and for the "
                        "tonnage of agricultural and industrial produce served",
                        "The rates of assignment are given in the question; they differ "
                        "from book to book",
                        "The alignment with the HIGHEST utility per km gets the highest priority"],
                 color="teal")
    S += EX("Choosing between two alignments by the saturation system",
            "Two alternative alignments A and B are proposed to connect the same pair of towns. "
            "Utility units are to be assigned at the rate of <b>1 unit per 1,000 of "
            "population served, 1 unit per 1,000 tonnes of agricultural produce and 1 unit "
            "per 1,000 tonnes of industrial produce</b>. The data are: <br/>"
            "Alignment A \u2014 length 20 km; villages served of population 2,000, 1,500, "
            "1,000 and 500; agricultural produce 6,000 t; industrial produce 2,000 t. <br/>"
            "Alignment B \u2014 length 15 km; villages served of population 1,200, 800 and "
            "1,000; agricultural produce 4,500 t; industrial produce 1,500 t. <br/>"
            "Which alignment should be given priority?",
            ["#Step 1 \u2014 utility units of alignment A",
             "$Population served = 2000 + 1500 + 1000 + 500 = 5000 \u21d2 5000/1000 = 5.0 units",
             "$Agricultural produce = 6000 t \u21d2 6000/1000 = 6.0 units",
             "$Industrial produce = 2000 t \u21d2 2000/1000 = 2.0 units",
             "$Total utility of A = 5.0 + 6.0 + 2.0 = 13.0 units",
             "$Utility per km = 13.0 / 20 = <b>0.65 unit/km</b>",
             "#Step 2 \u2014 utility units of alignment B",
             "$Population served = 1200 + 800 + 1000 = 3000 \u21d2 3.0 units",
             "$Agricultural produce = 4500 t \u21d2 4.5 units",
             "$Industrial produce = 1500 t \u21d2 1.5 units",
             "$Total utility of B = 3.0 + 4.5 + 1.5 = 9.0 units",
             "$Utility per km = 9.0 / 15 = <b>0.60 unit/km</b>",
             "#Step 3 \u2014 decision",
             "Alignment A gives 0.65 unit/km against 0.60 unit/km for B.",
             "!Alignment A has the greater utility per unit length and should be given "
             "priority. (Note that B has the greater total length efficiency in no other "
             "respect \u2014 always compare utility PER KILOMETRE, not the total.)"])
    S += PYQ(["Explain the saturation system of road planning. Two alignments have the "
              "following data \u2026 decide the priority. [7 + 7 marks]",
              "What are the four planning surveys required before preparing a road plan? "
              "[2 marks]"])
    S += REF("Khanna, Justo &amp; Veeraragavan, chapters 'Highway Development and Planning' "
             "and 'Highway Alignment and Engineering Surveys'; Kadiyali \u2014 "
             "<i>Traffic Engineering and Transport Planning</i> for the planning surveys.")
    return S
