"""UNIT 5 - Pavement materials."""
from kit import *


def build():
    S = H1("5", "Pavement Materials", "5 hours \u2022 about 12 % of the paper")

    S += H2("5.1  Materials used in highway construction")
    S += P("The four groups of materials used in a pavement are <b>soil</b> (the subgrade and "
           "the embankment), <b>stone aggregates</b> (the granular layers and the skeleton of "
           "every bound layer), <b>bituminous binders</b> (flexible pavements) and "
           "<b>cement and cement concrete</b> (rigid pavements and stabilised layers). "
           "For each material the examination asks the same three things: the "
           "<b>desirable properties</b>, the <b>tests</b> used to measure them, and the "
           "<b>specified limiting values</b>.")

    # ------------------------------------------------------------------ 5.2
    S += H2("5.2  Soil as a highway material")
    S += H3("5.2.1  Desirable properties of a subgrade soil")
    S += BUL(["<b>Stability</b> \u2014 adequate and sustained strength under the worst "
              "moisture condition it will meet in service.",
              "<b>Incompressibility</b> \u2014 freedom from excessive settlement and from "
              "consolidation under repeated loading.",
              "<b>Permanency of strength</b> \u2014 the strength should not change with "
              "changes in moisture and temperature.",
              "<b>Minimum change in volume</b> \u2014 low swelling and shrinkage; expansive "
              "clays are the worst subgrade material.",
              "<b>Good drainage</b> \u2014 the soil should drain freely, so that the "
              "moisture does not build up.",
              "<b>Ease of compaction</b> \u2014 it should be possible to compact it to a "
              "high density with the available plant."])
    S += H3("5.2.2  Tests on subgrade soil")
    S += TBL([["Test", "What it measures", "Where used"],
              ["<b>California Bearing Ratio (CBR)</b>",
               "The resistance of the soil to the penetration of a standard plunger, "
               "expressed as a percentage of the resistance of standard crushed stone",
               "The design input for flexible pavements (IRC 37); the most important "
               "test in this subject"],
              ["<b>Plate bearing test</b>",
               "The pressure\u2013settlement behaviour of the soil in the field; gives the "
               "<b>modulus of subgrade reaction K</b> (kg/cm\u00b3 or MPa/m)",
               "The design input for rigid pavements (IRC 58, Westergaard's analysis)"],
              ["<b>Dynamic cone penetration test</b>",
               "The number of blows required to drive a cone through a given depth",
               "A rapid field test for the relative strength profile of the subgrade"],
              ["<b>Triaxial compression test</b>",
               "The shear strength parameters c and \u03c6, and the modulus of elasticity",
               "The triaxial method of flexible pavement design; research work"],
              ["<b>Standard Proctor / modified Proctor</b>",
               "The optimum moisture content and the maximum dry density",
               "Field compaction control"],
              ["<b>Atterberg limits, sieve analysis</b>",
               "Liquid limit, plastic limit, plasticity index and the grain-size "
               "distribution", "Classification of the soil and the group index"],
              ["<b>Field density test</b> (sand replacement, core cutter)",
               "The dry density actually achieved in the field",
               "Quality control of compaction"]],
             widths=[2.2, 4.4, 3.2], align=["l", "l", "l"], fs=7.6,
             caption="Table 5.1  Tests on subgrade soil.")
    S += H3("5.2.3  The CBR test")
    S += P("A cylindrical plunger of 50 mm diameter is made to penetrate the compacted soil "
           "specimen at a uniform rate of <b>1.25 mm per minute</b>, and the load is recorded "
           "against the penetration. The <b>load\u2013penetration curve</b> is drawn; if its "
           "initial portion is <b>concave upwards</b> (which happens because of surface "
           "irregularities), a <b>tangent is drawn at the point of inflexion</b> and its "
           "intercept on the penetration axis is taken as the <b>corrected origin</b>. The "
           "loads at 2.5 mm and 5.0 mm penetration, measured from the corrected origin, are "
           "then read off.")
    S += FIG("f5_cbr",
             "Fig. 5.1  The CBR load\u2013penetration curve and its correction for the "
             "concave-upward initial portion.")
    S += FORMULA(["CBR = (load carried by the specimen / load carried by the standard "
                  "aggregate) \u00d7 100",
                  "Standard load at 2.5 mm penetration = 1370 kg  (pressure 70 kg/cm\u00b2)",
                  "Standard load at 5.0 mm penetration = 2055 kg  (pressure 105 kg/cm\u00b2)"],
                 label="California Bearing Ratio",
                 where=["Normally CBR at 2.5 mm is greater than CBR at 5.0 mm and the "
                        "<b>2.5 mm value is reported</b>",
                        "If the 5.0 mm value comes out greater, the test is repeated; if it "
                        "repeats, the 5.0 mm value is reported",
                        "The specimen is soaked for 4 days before testing, to represent the "
                        "worst moisture condition",
                        "Rate of penetration of the plunger = 1.25 mm/min; plunger diameter "
                        "= 50 mm"])
    S += EX("Determination of the CBR value",
            "In a CBR test on a soaked subgrade soil specimen, the loads corresponding to "
            "2.5 mm and 5.0 mm penetration (measured from the corrected origin) were 96 kg "
            "and 132 kg respectively. Determine the CBR value of the soil and comment on "
            "its suitability as a subgrade.",
            ["#Step 1 \u2014 CBR at 2.5 mm penetration",
             "$= (96/1370) \u00d7 100 = 7.01 %",
             "#Step 2 \u2014 CBR at 5.0 mm penetration",
             "$= (132/2055) \u00d7 100 = 6.42 %",
             "#Step 3 \u2014 which value to report",
             "CBR at 2.5 mm (7.01 %) is greater than CBR at 5.0 mm (6.42 %), which is the "
             "normal behaviour. Hence the 2.5 mm value is reported.",
             "!CBR of the soil = 7.0 %. This is a fair to good subgrade; with a CBR of 7 % "
             "a reasonable crust thickness can be designed by IRC 37. A CBR below about "
             "2 % would call for a capping layer or soil stabilisation."])

    S += H3("5.2.4  Group index of a soil")
    S += P("The <b>group index</b> is a single number, from 0 to 20, that expresses the "
           "suitability of a soil as a subgrade \u2014 the <b>lower the group index the "
           "better the soil</b>. It is computed from the amount of fine material and the "
           "plasticity characteristics.")
    S += FORMULA(["GI = 0.2 a + 0.005 a c + 0.01 b d"],
                 label="Group index",
                 where=["a = (percentage passing the 0.075 mm sieve) \u2212 35,  "
                        "limited to the range 0 to 40",
                        "b = (percentage passing the 0.075 mm sieve) \u2212 15,  "
                        "limited to the range 0 to 40",
                        "c = (liquid limit in %) \u2212 40,  limited to the range 0 to 20",
                        "d = (plasticity index in %) \u2212 10,  limited to the range 0 to 20",
                        "The group index is reported to the nearest whole number"],
                 color="teal")
    S += EX("Group index of a soil",
            "A soil has 60 % passing the 0.075 mm sieve, a liquid limit of 50 % and a "
            "plasticity index of 25 %. Determine its group index.",
            ["#Step 1 \u2014 evaluate a, b, c and d with their limits",
             "$a = 60 \u2212 35 = 25    (within 0\u201340, so a = 25)",
             "$b = 60 \u2212 15 = 45    (exceeds 40, so b is taken as 40)",
             "$c = 50 \u2212 40 = 10    (within 0\u201320, so c = 10)",
             "$d = 25 \u2212 10 = 15    (within 0\u201320, so d = 15)",
             "#Step 2 \u2014 substitute in the formula",
             "$GI = 0.2 a + 0.005 a c + 0.01 b d",
             "$= 0.2 \u00d7 25 + 0.005 \u00d7 25 \u00d7 10 + 0.01 \u00d7 40 \u00d7 15",
             "$= 5.00 + 1.25 + 6.00 = 12.25",
             "!Group index = 12 (to the nearest whole number). Since the group index is "
             "high (the scale runs 0 to 20), this is a POOR subgrade soil and will need a "
             "thick pavement crust or improvement of the subgrade."])
    S += PYQ(["Explain the CBR test with a sketch of the load\u2013penetration curve. Why is "
              "a correction applied to the curve? [7 marks \u2014 asked very often]",
              "What are the desirable properties of a subgrade soil? [7 marks]",
              "Define group index and compute it for the given data. [4 marks]",
              "What is the modulus of subgrade reaction and how is it determined? [2 marks]"])

    # ------------------------------------------------------------------ 5.3
    S += H2("5.3  Stone aggregates")
    S += H3("5.3.1  Desirable properties of road aggregates")
    S += TBL([["Property", "Why it is needed", "Test that measures it"],
              ["<b>Strength</b>", "To resist the crushing action of the wheel loads, "
               "especially in a thin surfacing where the stresses are high",
               "Aggregate crushing value; also the ten per cent fines value"],
              ["<b>Hardness</b>", "To resist the abrasive action of the tyres and of the "
               "grit trapped between the tyre and the surface",
               "Los Angeles abrasion test; Deval attrition test"],
              ["<b>Toughness</b>", "To resist the sudden shock or impact of the wheel loads",
               "Aggregate impact value"],
              ["<b>Durability</b>", "To resist weathering \u2014 alternate wetting and "
               "drying, freezing and thawing, and chemical attack",
               "Soundness test (with sodium or magnesium sulphate)"],
              ["<b>Proper shape</b>", "Flaky and elongated particles break easily under "
               "load and give poor interlock and workability",
               "Flakiness index, Elongation index, Angularity number"],
              ["<b>Adhesion to bitumen</b>", "The bitumen film must not be displaced by "
               "water, otherwise the aggregate strips and the mix fails",
               "Stripping value test; static and dynamic immersion tests"],
              ["<b>Low porosity / water absorption</b>", "A porous aggregate absorbs "
               "bitumen and is less durable", "Water absorption test (should be under 2 %)"],
              ["<b>Suitable specific gravity and cleanliness</b>",
               "Needed for the mix design calculations; clay coatings prevent bonding",
               "Specific gravity test; deleterious material test"]],
             widths=[1.9, 4.6, 3.3], align=["l", "l", "l"], fs=7.5,
             caption="Table 5.2  Desirable properties of road aggregates and the "
                     "corresponding tests \u2014 a standard 7-mark answer.")
    S += FIG("f5_aggtests",
             "Fig. 5.2  Three of the standard aggregate tests \u2014 impact, "
             "Los Angeles abrasion and crushing.")
    S += H3("5.3.2  The tests and their limiting values")
    S += TBL([["Test", "How it is expressed", "Commonly specified maximum"],
              ["<b>Aggregate crushing value (ACV)</b>",
               "Percentage of the sample passing the 2.36 mm sieve after a compressive load "
               "of 40 tonnes applied gradually in 10 minutes",
               "30 % for surface (wearing) courses; 45 % for base courses"],
              ["<b>Aggregate impact value (AIV)</b>",
               "Percentage passing the 2.36 mm sieve after 15 blows of a "
               "13.5\u201314 kg hammer falling 380 mm",
               "30 % for wearing courses; 35 % for bituminous macadam; 40 % for "
               "WBM base courses"],
              ["<b>Los Angeles abrasion value</b>",
               "Percentage passing the 1.7 mm sieve after 500 to 1000 revolutions of the "
               "drum with the abrasive charge of steel spheres",
               "30 % for wearing courses; 40\u201350 % for base courses"],
              ["<b>Flakiness index (FI)</b>",
               "Percentage by weight of particles whose LEAST dimension is less than "
               "0.6 times their mean dimension",
               "25 % (15 % for bituminous concrete)"],
              ["<b>Elongation index (EI)</b>",
               "Percentage by weight of particles whose GREATEST dimension is more than "
               "1.8 times their mean dimension", "15 % (combined FI + EI \u2264 30 %)"],
              ["<b>Water absorption</b>", "Percentage increase in weight on soaking for "
               "24 hours", "2 %"],
              ["<b>Soundness</b>", "Loss in weight after 5 cycles of immersion in sodium "
               "or magnesium sulphate solution", "12 % (sodium) / 18 % (magnesium)"],
              ["<b>Stripping value</b>", "Percentage of the aggregate surface from which the "
               "bitumen film is displaced after 24 h immersion in water at 40 \u00b0C",
               "25 %"]],
             widths=[2.2, 4.5, 3.1], align=["l", "l", "l"], fs=7.4,
             caption="Table 5.3  Aggregate tests and the values commonly specified. The exact "
                     "limit depends on the layer and on the MoRTH / IRC specification being "
                     "used, so quote the value given in the question if one is supplied.")
    S += NOTE("<b>Interpretation of the impact value:</b> below 10 % exceptionally strong, "
              "10\u201320 % strong, 20\u201330 % satisfactory for surfacing, and above 35 % "
              "weak and unsuitable for surfacing.")
    S += EX("Aggregate impact value and crushing value",
            "(a) In an aggregate impact test the total weight of the oven-dried sample was "
            "350 g and the weight of the material passing the 2.36 mm sieve after the test "
            "was 42 g. (b) In an aggregate crushing test on another sample of 2,500 g, "
            "the weight passing the 2.36 mm sieve after the test was 425 g. "
            "Determine both values and comment.",
            ["#(a) Aggregate impact value",
             "$AIV = (W\u2082/W\u2081) \u00d7 100 = (42/350) \u00d7 100 = 12.0 %",
             "Being between 10 % and 20 %, the aggregate is classified as <b>strong</b> and "
             "is satisfactory for a wearing course (limit 30 %).",
             "#(b) Aggregate crushing value",
             "$ACV = (W\u2082/W\u2081) \u00d7 100 = (425/2500) \u00d7 100 = 17.0 %",
             "This is well below the limit of 30 % for a surface course, so the aggregate "
             "is acceptable.",
             "!AIV = 12 % (strong) ; ACV = 17 % \u2014 both are within the specified "
             "limits and the aggregate is suitable even for a wearing course."])
    S += EX("Flakiness index, elongation index and the combined index",
            "A 2,000 g sample of aggregate was tested for shape. The weight of the flaky "
            "particles separated by the thickness gauge was 260 g. From the remaining "
            "non-flaky material, the elongated particles separated by the length gauge "
            "weighed 210 g. Determine the flakiness index, the elongation index and the "
            "combined index.",
            ["#Step 1 \u2014 flakiness index",
             "$FI = (weight of flaky particles / total weight of the sample) \u00d7 100",
             "$= (260/2000) \u00d7 100 = 13.0 %",
             "#Step 2 \u2014 elongation index",
             "The elongation index is determined on the material left after the flaky "
             "particles have been removed:",
             "$Weight of the non-flaky material = 2000 \u2212 260 = 1740 g",
             "$EI = (210/1740) \u00d7 100 = 12.07 %",
             "#Step 3 \u2014 combined index",
             "$= [(260 + 210)/2000] \u00d7 100 = (470/2000) \u00d7 100 = 23.5 %",
             "!FI = 13.0 % ; EI = 12.1 % ; combined index = 23.5 %. All three are within "
             "the usual limits (FI 25 %, EI 15 %, combined 30 %), so the shape of the "
             "aggregate is acceptable."])
    S += FIG("f5_gradation",
             "Fig. 5.3  Aggregate gradation curves. A DENSE (well) graded aggregate gives "
             "the lowest voids and the highest strength; an OPEN graded aggregate has little "
             "filler and high voids; a GAP graded aggregate lacks the intermediate sizes.")
    S += PYQ(["What are the desirable properties of road aggregates? Name the test for each. "
              "[7 marks \u2014 asked very often]",
              "Explain the aggregate impact test and state the IRC limiting values. "
              "[7 marks]",
              "Define flakiness index and elongation index. Why are flaky and elongated "
              "particles undesirable? [4 marks]",
              "Compute the AIV / ACV / FI for the given data. [4 marks]"])

    # ------------------------------------------------------------------ 5.4
    S += H2("5.4  Bituminous binders")
    S += H3("5.4.1  Types of bituminous binder")
    S += TBL([["Binder", "Description and use"],
              ["<b>Bitumen (paving bitumen)</b>",
               "A residue of the fractional distillation of crude petroleum; a "
               "thermoplastic material, soluble in carbon disulphide. Now graded by "
               "<b>viscosity</b> as <b>VG-10, VG-20, VG-30 and VG-40</b> (IS 73), the higher "
               "number being the harder and more viscous grade. VG-30 is the general-purpose "
               "paving grade; VG-40 is used for heavily trafficked and high-stress locations. "
               "The older system graded it by penetration (30/40, 60/70, 80/100)."],
              ["<b>Road tar</b>",
               "Obtained by the destructive distillation of coal or wood; graded RT-1 to "
               "RT-5. It has better adhesion to wet aggregate than bitumen but is more "
               "temperature-susceptible and is now little used because of health concerns."],
              ["<b>Cutback bitumen</b>",
               "Bitumen whose viscosity has been reduced by a volatile diluent, so that it "
               "can be used without heating. <b>RC</b> (rapid curing, cut back with "
               "gasoline), <b>MC</b> (medium curing, with kerosene) and <b>SC</b> (slow "
               "curing, with diesel or light oil). Used for surface dressing and patch "
               "repair in cold weather."],
              ["<b>Bitumen emulsion</b>",
               "Bitumen dispersed as fine globules in water with an emulsifying agent. "
               "<b>RS</b> (rapid setting), <b>MS</b> (medium setting) and <b>SS</b> "
               "(slow setting). Used for surface dressing, patch repair, tack coat and "
               "for maintenance in wet or cold weather, because no heating is needed."],
              ["<b>Modified bitumen</b>",
               "<b>Polymer modified bitumen (PMB)</b> and <b>crumb rubber modified bitumen "
               "(CRMB)</b> \u2014 the polymer or rubber improves the resistance to rutting "
               "at high temperature and to cracking at low temperature, and widens the "
               "useful temperature range. Used on heavily trafficked highways."]],
             widths=[1.9, 7.9], align=["l", "l"], fs=7.6,
             caption="Table 5.4  Types of bituminous binder.")
    S += H3("5.4.2  Tests on bitumen")
    S += FIG("f5_bittests",
             "Fig. 5.4  Three standard tests on bituminous binders \u2014 penetration, "
             "ductility and softening point.")
    S += TBL([["Test", "What is done", "What it tells us"],
              ["<b>Penetration test</b>",
               "The distance, in units of 0.1 mm, that a standard needle penetrates the "
               "sample in 5 s under a load of 100 g at 25 \u00b0C",
               "The <b>hardness or consistency</b> of the binder. A grade of 80/100 means "
               "the needle penetrates 8 to 10 mm"],
              ["<b>Ductility test</b>",
               "A briquette of standard shape is pulled apart at 50 mm/min at 27 \u00b0C in "
               "a water bath; the elongation at break is measured in cm",
               "The ability to <b>deform without cracking</b> \u2014 essential because the "
               "pavement flexes under every wheel load. Minimum 50 cm for paving bitumen"],
              ["<b>Softening point (Ring and Ball)</b>",
               "A steel ball of 3.5 g rests on the sample held in a brass ring; the bath is "
               "heated at 5 \u00b0C/min; the temperature at which the sample softens enough "
               "for the ball to fall 25 mm is recorded",
               "The <b>temperature susceptibility</b>. A higher softening point means less "
               "susceptibility to temperature and less risk of bleeding in hot weather"],
              ["<b>Viscosity test</b>",
               "Absolute viscosity at 60 \u00b0C (in poise) and kinematic viscosity at "
               "135 \u00b0C (in centistokes)",
               "The <b>resistance to flow</b>; it is now the basis of the grading system "
               "(VG grades) and decides the mixing and rolling temperatures"],
              ["<b>Flash and fire point</b>",
               "The lowest temperatures at which the vapour flashes momentarily and at which "
               "the material burns continuously",
               "The <b>safe heating temperature</b>. Minimum flash point 220 \u00b0C for "
               "paving grades"],
              ["<b>Specific gravity</b>",
               "By the pycnometer or the balance method at 27 \u00b0C",
               "Needed for the <b>mix design calculations</b>; usually 0.97 to 1.02"],
              ["<b>Solubility in trichloroethylene</b>",
               "The percentage soluble in the solvent",
               "The <b>purity</b> \u2014 the insoluble part is inert matter; minimum 99 %"],
              ["<b>Loss on heating / thin film oven test</b>",
               "The loss in weight and the change in penetration after heating",
               "The <b>volatility and the ageing (hardening)</b> of the binder in service"]],
             widths=[2.0, 4.4, 3.4], align=["l", "l", "l"], fs=7.4,
             caption="Table 5.5  Tests on bituminous binders.")
    S += TIP("The three tests asked most often are <b>penetration (hardness), ductility "
             "(ability to deform) and softening point (temperature susceptibility)</b>. "
             "Remember for each: the temperature, the load or the rate, and what the result "
             "signifies. Penetration \u2014 25 \u00b0C, 100 g, 5 s. Ductility \u2014 "
             "27 \u00b0C, 50 mm/min, minimum 50 cm. Softening point \u2014 ball 3.5 g, "
             "heating 5 \u00b0C/min, fall of 25 mm.")

    # ------------------------------------------------------------------ 5.5
    S += H2("5.5  Bituminous paving mixes")
    S += H3("5.5.1  Types of bituminous construction")
    S += TBL([["Type", "Where used", "Character"],
              ["<b>Surface dressing</b>", "A thin wearing surface or a renewal coat",
               "A layer of binder covered with a single layer of stone chips; "
               "not a structural layer"],
              ["<b>Premix carpet (PC) with seal coat</b>", "Thin wearing course, 20 mm",
               "Open graded, needs a seal coat to close the surface"],
              ["<b>Bituminous macadam (BM)</b>", "Base or binder course",
               "Open graded, high voids, low bitumen content"],
              ["<b>Dense bituminous macadam (DBM)</b>", "Binder course of heavy-duty "
               "pavements", "Dense graded, designed by the Marshall method"],
              ["<b>Semi-dense bituminous concrete (SDBC)</b>", "Wearing course, 25\u201340 mm",
               "Between BM and BC in density"],
              ["<b>Bituminous concrete (BC) / asphaltic concrete</b>",
               "The <b>highest quality wearing course</b>, 30\u201350 mm",
               "Dense graded, impervious, designed by the Marshall method"],
              ["<b>Mastic asphalt</b>", "Bridge decks, heavily trafficked junctions, "
               "toll plazas", "Very high binder content, void-less, laid hot and hand tamped"]],
             widths=[2.4, 3.4, 4.0], align=["l", "l", "l"], fs=7.6,
             caption="Table 5.6  Types of bituminous construction, in increasing order "
                     "of quality.")
    S += H3("5.5.2  Requirements of a good bituminous mix")
    S += BUL(["<b>Stability</b> \u2014 resistance to permanent deformation (rutting and "
              "shoving) under repeated loading, obtained from the aggregate interlock and "
              "the binder.",
              "<b>Durability</b> \u2014 resistance to weathering and to the ageing of the "
              "binder, obtained by a sufficient binder film thickness and low voids.",
              "<b>Flexibility</b> \u2014 the ability to deform with the underlying layers "
              "without cracking.",
              "<b>Adequate skid resistance</b> \u2014 a rough, harsh microtexture, "
              "particularly when wet.",
              "<b>Impermeability</b> \u2014 to keep water out of the pavement layers.",
              "<b>Workability</b> \u2014 the mix must be capable of being laid and compacted "
              "with the available plant.",
              "<b>Economy</b> \u2014 the minimum binder content that satisfies all the above."])
    S += H3("5.5.3  Marshall method of mix design")
    S += P("Marshall's method is the standard method of designing a dense bituminous mix. "
           "Cylindrical specimens 101.6 mm in diameter and 63.5 mm high are prepared at "
           "several bitumen contents, compacted with <b>75 blows on each face</b> for heavy "
           "traffic, and then tested at <b>60 \u00b0C</b> at a deformation rate of "
           "<b>50 mm per minute</b>. Two results are obtained from the test:")
    S += BUL(["<b>Marshall stability</b> \u2014 the maximum load the specimen carries before "
              "failure, in kg or kN.",
              "<b>Flow value</b> \u2014 the vertical deformation at the instant of failure, "
              "in units of 0.25 mm."])
    S += FIG("f5_marshall",
             "Fig. 5.5  The five Marshall plots. The optimum bitumen content is the average "
             "of the bitumen contents at (i) maximum stability, (ii) maximum unit weight and "
             "(iii) 4 % air voids.")
    S += FORMULA(["Bulk specific gravity of the compacted mix:",
                  "G\u2098 = W\u2090 / (W\u2090 \u2212 W\u1d64)",
                  "Theoretical maximum specific gravity (no air voids):",
                  "G\u209c = 100 / [ (W\u2081/G\u2081) + (W\u2082/G\u2082) + \u2026 + "
                  "(W\u1d47/G\u1d47) ]",
                  "Air voids:        V\u1d65 = [ (G\u209c \u2212 G\u2098) / G\u209c ] "
                  "\u00d7 100  %",
                  "Volume of bitumen:  V\u1d47 = (W\u1d47 \u00d7 G\u2098) / G\u1d47   %",
                  "Voids in the mineral aggregate:  VMA = V\u1d65 + V\u1d47   %",
                  "Voids filled with bitumen:  VFB = (V\u1d47 / VMA) \u00d7 100  %"],
                 label="Marshall mix design computations",
                 where=["W\u2090 = weight of the specimen in air, W\u1d64 = weight in water",
                        "W\u1d62, G\u1d62 = percentage by weight and the specific gravity of "
                        "each ingredient (aggregate fractions, filler, bitumen)",
                        "W\u1d47, G\u1d47 = percentage and specific gravity of the bitumen",
                        "Typical criteria: Marshall stability minimum 9 kN, flow 2\u20134 mm "
                        "(8\u201316 units), air voids 3\u20135 %, VFB 65\u201375 %"])
    S += EX("Marshall mix design computations",
            "A compacted Marshall specimen of a bituminous mix weighs 1,200 g in air and "
            "690 g in water. The bitumen content is 5.0 % by total weight of the mix. The "
            "specific gravity of the aggregate is 2.70 and that of the bitumen is 1.02. "
            "Determine the bulk specific gravity, the theoretical maximum specific gravity, "
            "the percentage air voids, the VMA and the VFB, and comment on the mix.",
            ["#Step 1 \u2014 bulk specific gravity of the mix",
             "$G\u2098 = W\u2090/(W\u2090 \u2212 W\u1d64) = 1200/(1200 \u2212 690) "
             "= 1200/510 = 2.353",
             "#Step 2 \u2014 theoretical maximum specific gravity",
             "Percentage of aggregate = 100 \u2212 5.0 = 95.0 %",
             "$G\u209c = 100/[(95/2.70) + (5/1.02)] = 100/(35.185 + 4.902)",
             "$= 100/40.087 = 2.495",
             "#Step 3 \u2014 percentage air voids",
             "$V\u1d65 = [(G\u209c \u2212 G\u2098)/G\u209c] \u00d7 100 = "
             "[(2.495 \u2212 2.353)/2.495] \u00d7 100",
             "$= (0.142/2.495) \u00d7 100 = 5.68 %",
             "#Step 4 \u2014 volume of bitumen",
             "$V\u1d47 = (W\u1d47 \u00d7 G\u2098)/G\u1d47 = (5.0 \u00d7 2.353)/1.02 "
             "= 11.765/1.02 = 11.53 %",
             "#Step 5 \u2014 VMA and VFB",
             "$VMA = V\u1d65 + V\u1d47 = 5.68 + 11.53 = 17.21 %",
             "$VFB = (V\u1d47/VMA) \u00d7 100 = (11.53/17.21) \u00d7 100 = 67.0 %",
             "#Step 6 \u2014 comment",
             "The VFB of 67 % lies within the usual range of 65\u201375 %, but the air "
             "voids of 5.68 % are slightly above the desirable range of 3\u20135 % for a "
             "bituminous concrete. The mix would be improved either by a small increase in "
             "the bitumen content or by heavier compaction.",
             "!G\u2098 = 2.353 ; G\u209c = 2.495 ; V\u1d65 = 5.68 % ; V\u1d47 = 11.53 % ; "
             "VMA = 17.21 % ; VFB = 67.0 %"])
    S += PYQ(["Explain the Marshall method of bituminous mix design. How is the optimum "
              "bitumen content determined? [14 marks \u2014 asked very often]",
              "Compute the air voids, VMA and VFB for the given Marshall specimen data. "
              "[7 marks]",
              "What are the requirements of a good bituminous mix? [7 marks]",
              "Differentiate between BM, DBM and BC. [4 marks]",
              "What is cutback bitumen and bitumen emulsion? When is each used? [7 marks]"])

    # ------------------------------------------------------------------ 5.6
    S += H2("5.6  Cement and cement concrete for pavements")
    S += H3("5.6.1  Desirable properties and tests on cement")
    S += TBL([["Test on cement", "What it checks"],
              ["Fineness (sieve or Blaine air permeability)",
               "The rate of hydration and the strength development"],
              ["Consistency (Vicat apparatus)",
               "The water required for the standard paste, needed for the other tests"],
              ["Setting time \u2014 initial and final (Vicat)",
               "Initial setting time not less than 30 minutes and final setting time not "
               "more than 600 minutes for OPC \u2014 governs the time available for "
               "placing and finishing"],
              ["Soundness (Le Chatelier, autoclave)",
               "Freedom from excessive expansion after setting, due to free lime or magnesia"],
              ["Compressive strength (mortar cubes at 3, 7 and 28 days)",
               "The grade of the cement (33, 43 or 53)"],
              ["Heat of hydration", "Important for thick slabs, where the temperature rise "
               "causes cracking"]],
             widths=[3.4, 6.4], align=["l", "l"], fs=7.7,
             caption="Table 5.7  Tests on cement.")
    S += H3("5.6.2  Requirements of concrete for a cement concrete pavement")
    S += P("The critical property of pavement quality concrete (PQC) is <b>flexural "
           "strength</b>, not compressive strength, because a rigid pavement slab carries "
           "the load essentially in <b>bending</b>.")
    S += TBL([["Requirement", "Value normally specified"],
              ["<b>Characteristic 28-day flexural strength</b>",
               "<b>4.5 MPa</b> minimum \u2014 the design input in IRC 58"],
              ["Grade of concrete", "M 40 (28-day characteristic compressive strength "
               "40 MPa) for PQC"],
              ["Minimum cement content", "About 350 kg/m\u00b3"],
              ["Maximum water\u2013cement ratio", "About 0.45 to 0.50"],
              ["Maximum size of coarse aggregate", "25 mm to 31.5 mm"],
              ["Workability (slump)", "Low \u2014 25 to 50 mm for slip-form or fixed-form "
               "paving, since a stiff mix is needed to hold the shape"],
              ["Air content, where freezing occurs", "4 to 6 % entrained air"]],
             widths=[3.4, 6.4], align=["l", "l"], fs=7.8,
             caption="Table 5.8  Requirements for pavement quality concrete (IRC 15 / "
                     "IRC 58). The relation between flexural strength f\u1d63 and "
                     "compressive strength f\u1d04\u1d0b is often taken as "
                     "f\u1d63 \u2248 0.7 \u221af\u1d04\u1d0b (in MPa).")
    S += P("<b>Other uses of cement in road works:</b> cement-stabilised soil sub-bases, "
           "<b>dry lean concrete (DLC)</b> sub-bases beneath the PQC slab, cement-treated "
           "granular bases, and roller-compacted concrete.")
    S += PYQ(["Why is flexural strength, and not compressive strength, the design criterion "
              "for a cement concrete pavement? [2 marks]",
              "State the requirements of concrete used in a cement concrete pavement. "
              "[7 marks]",
              "Enumerate the tests on cement and state the purpose of each. [7 marks]"])
    S += REF("Khanna, Justo &amp; Veeraragavan, chapter 'Highway Materials'; "
             "Partha Chakraborty &amp; Animesh Das \u2014 <i>Principles of Transportation "
             "Engineering</i> for the mix-design volumetrics; IS 2386 (tests on aggregates), "
             "IS 73 (paving bitumen), IS 1203\u20131220 (tests on bitumen), "
             "IRC 15 and IRC 58 (concrete pavements), MoRTH Specifications for Road and "
             "Bridge Works.")
    return S
