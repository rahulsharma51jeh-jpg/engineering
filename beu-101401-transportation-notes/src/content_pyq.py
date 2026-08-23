"""Question bank in the BEU pattern + a full model question paper."""
from kit import *


def _qt(rows, caption):
    return TBL([["Question", "Where to revise"]] + rows,
               widths=[7.2, 2.6], align=["l", "l"], fs=7.5, caption=caption)


def build():
    S = H1("Q", "Question Bank and Model Question Paper",
           "compiled from the recurring pattern of BEU / AKU papers",
           header="Question bank")

    S += NOTE("The questions below are <b>compiled and reworded from the pattern that recurs "
              "in BEU and AKU papers for this subject</b>; they are not verbatim reproductions "
              "of any one paper. Every question is cross-referenced to the section, figure or "
              "worked example in these notes where the answer is to be found. Work through "
              "the two-mark bank first \u2014 it covers Q.1, which is compulsory.")

    # ============================================================== 2 marks
    S += H2("Part A \u2014 Two-mark question bank (for the compulsory Q.1)")
    S += H3("Unit 1")
    S += _qt([
        ["State the four modes of transportation. Give two advantages of road transport "
         "over rail transport.", "\u00a7 1.1, Table 1.1"],
        ["What was the most important contribution of Macadam to road construction?",
         "\u00a7 1.2.5"],
        ["How did Telford obtain the camber in his cross-section?", "\u00a7 1.2.4, Fig. 1.2"],
        ["State any two recommendations of the Jayakar Committee and their outcome.",
         "Table 1.3"],
        ["Write the full form of IRC and CRRI, and the year each was set up.", "Table 1.4"],
        ["State the target road density of each of the three twenty-year road plans.",
         "Table 1.5"],
        ["What road pattern was assumed in the Nagpur Road Plan?", "\u00a7 1.4.1, Fig. 1.4"],
        ["Name the five classes of road in the Nagpur classification.", "Table 1.6"],
        ["What are rural roads? Which two classes constitute them?", "Table 1.6"],
        ["Differentiate between an arterial street and a collector street.", "\u00a7 1.5.4"],
        ["What is the length of the Golden Quadrilateral? Which four cities does it connect?",
         "Table 1.8"],
        ["State the objective and the population criterion of PMGSY.", "Table 1.8"],
        ["What are obligatory points? Give one example of each kind.",
         "Table 1.9, Fig. 1.6"],
        ["Name the four stages of engineering survey for a highway.", "Table 1.10, Fig. 1.7"],
        ["What is the saturation system of road planning?", "\u00a7 1.10.2"],
        ["Define road density.", "Example 1.1"],
    ], "Unit 1 \u2014 two-mark questions.")

    S += H3("Unit 2")
    S += _qt([
        ["Define camber. State any two of its objects.", "\u00a7 2.2.2"],
        ["State the IRC recommended camber for a cement concrete surface and for an "
         "earth road.", "Table 2.4"],
        ["Why is a carriageway width between 3.75 m and 5.5 m never provided?", "Table 2.5"],
        ["Differentiate between mountable, semi-barrier and barrier kerbs.", "Table 2.6"],
        ["How is terrain classified for geometric design?", "Table 2.1"],
        ["What is design speed? State the ruling design speed for a NH in plain terrain.",
         "Table 2.2"],
        ["What is PIEV theory?", "\u00a7 2.3.1, Fig. 2.4"],
        ["State the criteria for measuring SSD and OSD.", "Table 2.7"],
        ["Why is the SSD greater on a descending gradient than on an ascending gradient?",
         "\u00a7 2.3.2"],
        ["What is intermediate sight distance? How is it obtained?", "\u00a7 2.3"],
        ["State the minimum and desirable length of an overtaking zone.", "\u00a7 2.3.3"],
        ["Define superelevation. State its maximum permissible value for plain terrain and "
         "for hill roads.", "\u00a7 2.4.1"],
        ["Why is extra widening provided at a horizontal curve? Name its two components.",
         "\u00a7 2.4.2"],
        ["What is the ideal shape of a transition curve and why?", "\u00a7 2.4.3"],
        ["Define shift of a curve. Write its expression.", "Fig. 2.10"],
        ["Define set-back distance.", "\u00a7 2.4.4"],
        ["Differentiate between ruling, limiting and exceptional gradient.", "Table 2.8"],
        ["What is grade compensation? Write its expression.", "\u00a7 2.5.2"],
        ["Why is a minimum gradient necessary?", "Table 2.8"],
        ["Why is riding comfort a design criterion for a valley curve but not for a "
         "summit curve?", "\u00a7 2.5.3"],
        ["Which shape of curve is used for a summit curve, and why?", "\u00a7 2.5.3"],
    ], "Unit 2 \u2014 two-mark questions.")

    S += H3("Unit 3")
    S += _qt([
        ["What is PCU? State the PCU value of a truck, a cycle and a cycle rickshaw.",
         "Table 3.3"],
        ["Differentiate between ADT and AADT.", "Table 3.4"],
        ["Define peak hour factor.", "Table 3.4, Example 3.2"],
        ["What is the 30th highest hourly volume and why is it used?", "Table 3.4"],
        ["State the significance of the 85th and the 98th percentile speed.", "Table 3.5"],
        ["Differentiate between running speed and journey speed.", "\u00a7 3.3.3"],
        ["Differentiate between time mean speed and space mean speed. Which is larger?",
         "\u00a7 3.4.1"],
        ["Write the fundamental relation between flow, density and speed.", "\u00a7 3.4.1"],
        ["What is jam density and free speed?", "\u00a7 3.4.2"],
        ["State Greenshields' expression for the maximum flow.", "\u00a7 3.4.2"],
        ["Differentiate between basic, possible and practical capacity.", "Table 3.6"],
        ["What is level of service? Name the LOS at capacity.", "Table 3.6, Fig. 3.5"],
        ["What is a desire line diagram?", "\u00a7 3.3.4"],
        ["Differentiate between a collision diagram and a condition diagram.", "Fig. 3.3"],
        ["State the 3 E's of accident prevention.", "\u00a7 3.3.5"],
        ["Name any four methods of an origin\u2013destination study.", "\u00a7 3.3.4"],
    ], "Unit 3 \u2014 two-mark questions.")

    S += H3("Unit 4")
    S += _qt([
        ["Name the four traffic control devices.", "\u00a7 4.2"],
        ["What shape identifies a mandatory sign, a cautionary sign and an informatory sign?",
         "Table 4.2, Fig. 4.1"],
        ["Give two examples each of a cautionary and an informatory sign.", "Table 4.2"],
        ["Name the four types of traffic island.", "Table 4.3"],
        ["Define cycle, cycle length and phase of a signal.", "Table 4.5"],
        ["What is lost time in a signal cycle? How is it estimated?", "Table 4.5"],
        ["What is saturation flow?", "Table 4.5"],
        ["Write Webster's expression for the optimum cycle time.", "\u00a7 4.3.3"],
        ["What is offset in a co-ordinated signal system?", "Table 4.5, \u00a7 4.3.5"],
        ["Name the four systems of signal co-ordination.", "Table 4.6"],
        ["State the three types of conflict at an intersection.", "\u00a7 4.4.1"],
        ["What is channelization? State any two of its objects.", "\u00a7 4.4.2"],
        ["Define weaving length and weaving angle of a rotary.", "Table 4.8, Fig. 4.6"],
        ["State any two advantages and two disadvantages of a rotary.", "Table 4.7"],
        ["Name any three types of grade-separated interchange.", "Table 4.9, Fig. 4.7"],
        ["Define parking accumulation and parking load.", "\u00a7 4.5.2"],
        ["Define parking turnover and parking index.", "\u00a7 4.5.2, Example 4.5"],
        ["How many cars can be parked in 30 m of kerb at 90\u00b0 and at parallel parking?",
         "Table 4.10"],
        ["Define lumen, candela and lux.", "Table 4.11"],
        ["What is the maintenance factor in lighting design? What is its usual value?",
         "Table 4.11"],
        ["When is staggered lighting layout preferred?", "Table 4.12"],
    ], "Unit 4 \u2014 two-mark questions.")

    S += H3("Unit 5")
    S += _qt([
        ["State any four desirable properties of a subgrade soil.", "\u00a7 5.2.1"],
        ["What is the modulus of subgrade reaction and how is it determined?", "Table 5.1"],
        ["State the standard loads used in the CBR test at 2.5 mm and 5.0 mm penetration.",
         "\u00a7 5.2.3"],
        ["Why is the CBR load\u2013penetration curve corrected? How?",
         "\u00a7 5.2.3, Fig. 5.1"],
        ["Which CBR value is normally reported and why?", "\u00a7 5.2.3"],
        ["Define group index. What is its range?", "\u00a7 5.2.4"],
        ["Name the test used to measure the toughness, the hardness and the strength of "
         "an aggregate.", "Table 5.2"],
        ["Define flakiness index and elongation index.", "Table 5.3, Example 5.4"],
        ["Why are flaky and elongated particles undesirable in a road aggregate?",
         "Table 5.2"],
        ["What is the stripping value of an aggregate?", "Table 5.3"],
        ["What is the maximum permissible aggregate impact value for a wearing course?",
         "Table 5.3"],
        ["What are VG grades of bitumen? Name them.", "Table 5.4"],
        ["What is cutback bitumen? Name its three types.", "Table 5.4"],
        ["What is a bitumen emulsion and when is it used?", "Table 5.4"],
        ["What does the penetration test measure? State its standard conditions.",
         "Table 5.5"],
        ["What does the softening point indicate?", "Table 5.5"],
        ["Why is the ductility test necessary? State the minimum value for paving bitumen.",
         "Table 5.5"],
        ["Differentiate between BM, DBM and BC.", "Table 5.6"],
        ["What is the flow value in the Marshall test?", "\u00a7 5.5.3"],
        ["How is the optimum bitumen content determined in Marshall's method?", "Fig. 5.5"],
        ["Why is flexural strength the design criterion for a concrete pavement?",
         "\u00a7 5.6.2"],
        ["State the minimum 28-day flexural strength of pavement quality concrete.",
         "Table 5.8"],
    ], "Unit 5 \u2014 two-mark questions.")

    S += H3("Unit 6")
    S += _qt([
        ["State two points of difference between a flexible and a rigid pavement.",
         "Table 6.1"],
        ["How does a flexible pavement transmit the wheel load to the subgrade?",
         "\u00a7 6.1, Fig. 6.1"],
        ["State any two functions of a sub-base course.", "Table 6.2"],
        ["Why is the strongest material placed at the top of a flexible pavement?",
         "Fig. 6.2"],
        ["Define ESWL.", "\u00a7 6.3.2"],
        ["What is rigidity factor? What is its value at a tyre pressure of 7 kg/cm\u00b2?",
         "\u00a7 6.3.1"],
        ["What is a standard axle? State its magnitude.", "\u00a7 6.3.3"],
        ["Define vehicle damage factor and lane distribution factor.", "\u00a7 6.3.3"],
        ["What is msa?", "\u00a7 6.3.3"],
        ["State Boussinesq's expression for the vertical stress under a point load.",
         "Table 6.3"],
        ["Name any three methods of flexible pavement design.", "Table 6.4"],
        ["State Westergaard's assumption regarding the subgrade.", "\u00a7 6.6"],
        ["Define radius of relative stiffness. Write its expression.", "\u00a7 6.6"],
        ["Define equivalent radius of the resisting section.", "\u00a7 6.6"],
        ["For a corner load, where is the critical tensile stress located?", "\u00a7 6.6"],
        ["What causes warping stress in a concrete slab?", "\u00a7 6.6.1, Fig. 6.6"],
        ["Why does the slab thickness not appear in the frictional stress formula?",
         "\u00a7 6.6.2"],
        ["State the most critical combination of stresses in a rigid pavement.",
         "Table 6.5"],
        ["Differentiate between a dowel bar and a tie bar.", "Table 6.6"],
        ["What is the usual spacing of an expansion joint and of a contraction joint?",
         "Table 6.6"],
        ["What is the function of the filler board and the sealant in an expansion joint?",
         "Fig. 6.7"],
        ["What is DLC and why is it used?", "\u00a7 6.8"],
    ], "Unit 6 \u2014 two-mark questions.")

    # ============================================================== long
    S += H2("Part B \u2014 Long-question bank (for Q.2 to Q.8)")
    S += P("Each long question in the paper carries 14 marks and is normally split into two "
           "or three parts \u2014 typically one theory part and one numerical or one "
           "diagram-based part. The questions marked \u00bb are the ones that recur most often.")
    S += _qt([
        ["\u00bb Describe with neat sketches the Tresaguet, Telford and Macadam methods of "
         "road construction, and compare them in a table.", "\u00a7 1.2, Table 1.2"],
        ["Discuss the recommendations of the Jayakar Committee and the organisations that "
         "resulted from them. Add the chronology of highway development in India.",
         "\u00a7 1.3"],
        ["Explain the three twenty-year road development plans, with their target road "
         "densities, and solve a road-density numerical.", "\u00a7 1.4, Example 1.1"],
        ["Classify the roads of India as per the Nagpur plan and as per the modified "
         "classification; give the function and the responsible authority of each class.",
         "\u00a7 1.5"],
        ["Write notes on NHDP and its phases, Bharatmala and PMGSY.", "\u00a7 1.6"],
        ["\u00bb What are the requirements of an ideal alignment? Discuss the factors "
         "controlling it, and the special considerations for hill roads.", "\u00a7 1.7"],
        ["\u00bb Explain the four engineering surveys for highway location, and enumerate "
         "the drawings and reports of a highway project.", "\u00a7 1.8, \u00a7 1.9"],
        ["Explain the saturation system and select between two given alignments.",
         "\u00a7 1.10, Example 1.2"],
        ["\u00bb Draw a typical cross-section of a two-lane highway in embankment and in "
         "cutting, and explain every element with its IRC value.", "\u00a7 2.2"],
        ["What is camber? Give its objects, shapes, expressions and IRC values. Also "
         "explain the width of the carriageway and of the shoulder.", "\u00a7 2.2.2, 2.2.3"],
        ["\u00bb Derive the expression for stopping sight distance and explain the effect "
         "of gradient. Solve the given numerical.", "\u00a7 2.3.2, Examples 2.1, 2.2"],
        ["\u00bb Explain overtaking sight distance with a sketch, derive the expression, "
         "and compute the OSD and the length of the overtaking zone.",
         "\u00a7 2.3.3, Example 2.3"],
        ["\u00bb Derive e + f = V\u00b2/127R. Explain the IRC procedure for the design of "
         "superelevation and design it for the given data.", "\u00a7 2.4.1, Example 2.4"],
        ["Why is extra widening required at a curve? Derive/state the two components and "
         "compute the total width at the curve.", "\u00a7 2.4.2, Example 2.6"],
        ["\u00bb What is a transition curve? State its functions and the three criteria for "
         "its length; compute the length and the shift for the given data.",
         "\u00a7 2.4.3, Example 2.7"],
        ["Explain set-back distance with a sketch and compute it for the given data.",
         "\u00a7 2.4.4, Example 2.8"],
        ["Define the types of gradient and give the IRC values. Explain grade compensation "
         "and compute the compensated gradient.", "\u00a7 2.5.1, 2.5.2, Example 2.9"],
        ["\u00bb Design the length of a summit curve for the given grades and sight "
         "distance, explaining both cases (L &gt; S and L &lt; S).",
         "\u00a7 2.5.3, Example 2.10"],
        ["\u00bb Explain the two criteria for the design of a valley curve and design its "
         "length for the given data.", "\u00a7 2.5.3, Example 2.11"],
        ["Discuss the road user and vehicular characteristics that affect traffic "
         "operation. What is PCU and why is it needed? Convert the given count into PCU.",
         "\u00a7 3.2, Example 3.1"],
        ["Explain the traffic volume study \u2014 the terms, the methods of counting and the "
         "methods of presenting the data.", "\u00a7 3.3.1"],
        ["Explain the spot-speed study, its uses and the methods, and determine the "
         "percentile speeds from the given data.", "\u00a7 3.3.2, Example 3.3"],
        ["\u00bb Explain the moving observer method, state its formulae and solve the "
         "given data.", "\u00a7 3.3.3, Example 3.4"],
        ["Explain the origin\u2013destination study \u2014 uses, methods and presentation.",
         "\u00a7 3.3.4"],
        ["Discuss the causes of road accidents and the measures for prevention. "
         "Distinguish between a collision diagram and a condition diagram.", "\u00a7 3.3.5"],
        ["\u00bb Derive q = k v. Explain the speed\u2013flow\u2013density diagrams and "
         "Greenshields' model; compute the capacity and the two possible speeds.",
         "\u00a7 3.4, Example 3.6"],
        ["Define basic, possible and practical capacity and level of service; compute the "
         "theoretical capacity of a lane.", "\u00a7 3.4.3, Example 3.7"],
        ["Explain traffic regulation under the three heads, and classify traffic signs and "
         "road markings with examples.", "\u00a7 4.1, \u00a7 4.2"],
        ["\u00bb Explain Webster's method of signal design and design a two-phase signal "
         "for the given data.", "\u00a7 4.3.3, Example 4.1"],
        ["Define all the signal terms, state the advantages and limitations of signals, and "
         "explain the four systems of co-ordination with a time\u2013space diagram.",
         "\u00a7 4.3.2, 4.3.5"],
        ["\u00bb What is a rotary? Give its advantages, disadvantages and design elements "
         "as per IRC, and compute the capacity of the weaving section.",
         "\u00a7 4.4.3, Example 4.3"],
        ["Explain channelization and the types of at-grade and grade-separated "
         "intersections with sketches.", "\u00a7 4.4.2, 4.4.4"],
        ["\u00bb Explain the types of parking and the parking statistics; solve the given "
         "parking survey and kerb-length problems.",
         "\u00a7 4.5, Examples 4.4, 4.5"],
        ["Explain the terms used in lighting and the layouts; design the spacing of the "
         "lamps for the given data.", "\u00a7 4.6, Example 4.6"],
        ["\u00bb State the desirable properties of road aggregates and the test for each; "
         "compute the AIV, ACV, FI and EI for the given data.",
         "\u00a7 5.3, Examples 5.3, 5.4"],
        ["Explain the CBR test with the load\u2013penetration curve and its correction; "
         "compute the CBR and the group index.", "\u00a7 5.2, Examples 5.1, 5.2"],
        ["Explain the types of bituminous binder and the tests on bitumen with their "
         "significance.", "\u00a7 5.4"],
        ["\u00bb Explain the Marshall method of mix design and the determination of the "
         "OBC; compute the air voids, VMA and VFB.", "\u00a7 5.5.3, Example 5.5"],
        ["State the requirements of concrete for a CC pavement and the tests on cement.",
         "\u00a7 5.6"],
        ["\u00bb Compare flexible and rigid pavements and explain how each transmits the "
         "load. Enumerate the components of a flexible pavement and their functions.",
         "\u00a7 6.1, \u00a7 6.2"],
        ["\u00bb What is ESWL and why is it needed? Determine the ESWL at the given depths "
         "for a dual wheel assembly.", "\u00a7 6.3.2, Example 6.1"],
        ["Explain the factors affecting the design of a flexible pavement and compute the "
         "design traffic in msa.", "\u00a7 6.3, Example 6.2"],
        ["Explain Boussinesq's and Burmister's theories and the IRC 37 design procedure; "
         "compute the vertical stress at the given depths.",
         "\u00a7 6.4, \u00a7 6.5, Example 6.3"],
        ["\u00bb State Westergaard's assumptions, define l and b, and compute the interior, "
         "edge and corner stresses for the given data.", "\u00a7 6.6, Example 6.4"],
        ["Explain warping and frictional stresses and the critical combinations of stress "
         "in a rigid pavement.", "\u00a7 6.6.1, 6.6.2, 6.6.3"],
        ["\u00bb Explain the types of joint in a CC pavement; distinguish dowel bars from "
         "tie bars and design the joint spacing / the tie bars for the given data.",
         "\u00a7 6.7, Examples 6.5, 6.6"],
    ], "Part B \u2014 long-question bank. \u00bb marks the most frequently repeated questions.")

    # ============================================================== model paper
    S += H2("Part C \u2014 Model question paper")
    hdr = [Paragraph("B.TECH. &nbsp;SEMESTER EXAMINATION", ParagraphStyle(
        "mp0", fontName="DJSans-Bold", fontSize=10, leading=13, alignment=TA_CENTER,
        textColor=NAVY)),
        Paragraph("TRANSPORTATION ENGINEERING &nbsp;&bull;&nbsp; Course Code 101401 "
                  "&nbsp;&bull;&nbsp; Civil Engineering", ParagraphStyle(
            "mp1", fontName="DJSans", fontSize=8.6, leading=12, alignment=TA_CENTER,
            textColor=BLUE)),
        Paragraph("Time : 3 hours &nbsp;&nbsp;|&nbsp;&nbsp; Full marks : 70",
                  ParagraphStyle("mp2", fontName="DJSans-Bold", fontSize=8.6, leading=12,
                                 alignment=TA_CENTER, textColor=colors.black)),
        Spacer(1, 3),
        Paragraph("<i>Instructions: Question No. 1 is compulsory. Answer any FOUR questions "
                  "from the remaining. Assume any missing data suitably and state it "
                  "clearly. Use of IS/IRC codes is permitted where indicated.</i>",
                  ParagraphStyle("mp3", fontName="DJSerif", fontSize=8, leading=11,
                                 alignment=TA_CENTER, textColor=GREY))]
    S += [Table([[hdr]], colWidths=[FW], style=TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.2, NAVY),
        ("LINEBELOW", (0, 0), (-1, -1), 0, NAVY),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F9FB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9)])), Spacer(1, 9)]

    S += H3("Q.1  Answer any SEVEN of the following. &nbsp;&nbsp;[7 \u00d7 2 = 14]", toc=False)
    S += NUMLIST(["Define camber and state its objects.",
                  "What is PIEV theory?",
                  "Differentiate between ruling gradient and limiting gradient.",
                  "What is PCU? Give the PCU value of a truck and of a cycle.",
                  "State the criteria for measuring stopping sight distance.",
                  "Distinguish between a dowel bar and a tie bar.",
                  "Define equivalent single wheel load.",
                  "What is the group index of a soil? State its range.",
                  "State the target road density of the third twenty-year road plan.",
                  "Define parking turnover and parking index."],
                 style=ParagraphStyle("mq", parent=QS, leftIndent=22))
    S += GAP(4)
    for q, parts in [
        ("Q.2", [("Describe, with neat labelled sketches, the Tresaguet, Telford and "
                  "Macadam methods of road construction.", 8),
                 ("Discuss the recommendations of the Jayakar Committee and state the "
                  "organisation that resulted from each.", 6)]),
        ("Q.3", [("Derive an expression for the stopping sight distance and explain the "
                  "effect of gradient on it.", 7),
                 ("Calculate the SSD for a design speed of 80 km/h on a descending gradient "
                  "of 3 %. Take t = 2.5 s and f = 0.35.", 7)]),
        ("Q.4", [("Explain the IRC step-by-step procedure for the design of superelevation.",
                  6),
                 ("A two-lane highway of 7.0 m width has a horizontal curve of radius 250 m "
                  "and a design speed of 80 km/h in plain terrain. Design the "
                  "superelevation, the extra widening and the length of the transition "
                  "curve, and find the shift.", 8)]),
        ("Q.5", [("Explain the two criteria used for the design of a valley curve.", 6),
                 ("A summit curve is formed by an ascending gradient of 1 in 40 meeting a "
                  "descending gradient of 1 in 30. Design the length of the summit curve "
                  "for a stopping sight distance of 180 m.", 8)]),
        ("Q.6", [("Explain the moving observer method of traffic study and state its "
                  "formulae.", 6),
                 ("In a moving observer study over a 2 km stretch, the test vehicle running "
                  "against the stream took 3 minutes and met 120 vehicles; running with the "
                  "stream it took 4 minutes, 8 vehicles overtook it and it overtook 20 "
                  "vehicles. Find the flow, the mean speed of the stream and the density.",
                  8)]),
        ("Q.7", [("Explain Webster's method of traffic signal design.", 6),
                 ("Design a two-phase fixed-time signal by Webster's method for an "
                  "intersection where the critical approach flows are 900 and 700 PCU/h and "
                  "the corresponding saturation flows are 2,700 and 2,500 PCU/h. Take the "
                  "amber period as 3 s per phase.", 8)]),
        ("Q.8", [("State Westergaard's assumptions, define the radius of relative stiffness "
                  "and the equivalent radius of the resisting section, and state the three "
                  "critical load positions.", 6),
                 ("A concrete slab 20 cm thick rests on a subgrade of K = 6 kg/cm\u00b3. "
                  "The design wheel load is 4,100 kg with a contact radius of 12 cm. "
                  "Taking E = 3 \u00d7 10\u2075 kg/cm\u00b2 and \u03bc = 0.15, compute the "
                  "interior, edge and corner load stresses.", 8)]),
    ]:
        inner = [Paragraph("<b>%s</b>" % q, ParagraphStyle(
            "mqn", fontName="DJSans-Bold", fontSize=9, leading=12, textColor=NAVY))]
        for i, (t, m) in enumerate(parts):
            inner.append(Paragraph("(%s) &nbsp;%s &nbsp;&nbsp;<b>[%d]</b>"
                                   % ("abc"[i], esc(t), m),
                                   ParagraphStyle("mqp", parent=BODY, fontSize=8.6,
                                                  leading=11.8, leftIndent=16,
                                                  firstLineIndent=-16, spaceAfter=3)))
        S += [Table([[inner]], colWidths=[FW], style=TableStyle([
            ("LINEBEFORE", (0, 0), (-1, -1), 2.0, colors.HexColor("#9DBBD8")),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5)])), Spacer(1, 5)]

    S += GAP(4)
    S += H3("Answers to the numerical parts of the model paper", toc=False)
    S += TBL([["Q", "Answer", "Method"],
              ["3 (b)", "SSD = 134.3 m \u2248 134 m",
               "0.278\u00d780\u00d72.5 = 55.6 ; 6400/[254(0.35\u22120.03)] = 78.7 ; "
               "sum = 134.3"],
              ["4 (b)", "e = 7 % (curve safe, f needed = 0.132) ; W\u2091 = 0.68 m ; "
               "L = 85.3 m \u2192 adopt 85 m ; shift S = 1.20 m",
               "e = V\u00b2/225R = 11.4 % &gt; 7 % \u21d2 e = 7 %, check "
               "f = V\u00b2/127R \u2212 0.07 = 0.132 &lt; 0.15 ; "
               "W\u2098 = 0.149, W\u209a\u209b = 0.533 ; L = 0.0215V\u00b3/CR with "
               "C = 0.516 ; S = L\u00b2/24R"],
              ["5 (b)", "N = 0.05833 ; L = 429.5 m \u2192 adopt 430 m",
               "Assume L &gt; S : L = N S\u00b2/4.4 = 0.05833\u00d7180\u00b2/4.4 ; "
               "429.5 &gt; 180, so the assumption holds"],
              ["6 (b)", "q = 926 veh/h ; t\u0304 = 4.78 min ; v\u0304 = 25.1 km/h ; "
               "k = 36.9 veh/km",
               "q = (120+8\u221220)/(3+4) = 15.43/min ; "
               "t\u0304 = 4 \u2212 (8\u221220)/15.43 = 4.78 ; v\u0304 = 2/4.78 ; k = q/v\u0304"],
              ["7 (b)", "Y = 0.6133 ; L = 10 s ; C\u2080 = 51.7 s \u2192 adopt 50 s ; "
               "g\u2081 = 21.7 s, g\u2082 = 18.3 s",
               "y\u2081 = 900/2700 = 0.3333, y\u2082 = 700/2500 = 0.28 ; "
               "C\u2080 = (1.5\u00d710+5)/(1\u22120.6133) ; "
               "g\u1d62 = (y\u1d62/Y)(C\u2212L)"],
              ["8 (b)", "l = 76.42 cm ; b = 11.61 cm ; \u03c3\u1d62 = 14.06, "
               "\u03c3\u2091 = 21.29, \u03c3\u1d04 = 18.28 kg/cm\u00b2 \u2014 the EDGE "
               "stress governs",
               "l = [Eh\u00b3/(12(1\u2212\u03bc\u00b2)K)]^\u00bc ; "
               "b = \u221a(1.6a\u00b2+h\u00b2) \u2212 0.675h ; "
               "4log\u2081\u2080(l/b) = 3.273 ; P/h\u00b2 = 10.25"]],
             widths=[0.6, 3.4, 5.8], align=["c", "l", "l"], fs=7.4, first_bold=True,
             caption="Check your working against these. Full worked solutions of the same "
                     "types are in Examples 2.2, 2.4, 2.6, 2.7, 2.10, 3.4, 4.1 and 6.4.")

    # ============================================================== strategy
    S += H2("Part D \u2014 Revision strategy")
    S += TBL([["If you have\u2026", "Do this"],
              ["<b>7 days</b>",
               "Two days on Unit 2 and Unit 6 (all the numericals, worked twice). One day "
               "each on Unit 4, Unit 3 and Unit 1. Half a day on Unit 5. The last day: the "
               "formula sheet, the two-mark bank and the model paper against the clock."],
              ["<b>3 days</b>",
               "Day 1 \u2014 Unit 2 completely (sight distance, superelevation, transition, "
               "summit and valley curves). Day 2 \u2014 Unit 6 (comparison table, ESWL, msa, "
               "Westergaard, joints) and Webster's method from Unit 4. Day 3 \u2014 the "
               "two-mark bank for all six units, plus the formula sheet. This covers four "
               "long questions and Q.1."],
              ["<b>1 day</b>",
               "The formula sheet, Table 6.1 (flexible vs rigid), Table 1.2 (historic "
               "methods), the two-mark bank, and the six worked numericals: SSD, "
               "superelevation, summit curve, moving observer, Webster and Westergaard."]],
             widths=[1.3, 8.5], align=["l", "l"], fs=7.8,
             caption="Table Q.1  What to study when time is short.")
    S += TIP("<b>How to write the answers.</b> (1) Draw the labelled sketch FIRST \u2014 it "
             "earns marks on its own and organises the rest of the answer. (2) Write the "
             "formula, then the substitution, then the answer with its UNIT, and box the "
             "answer. (3) In a design problem always state the code value you have assumed "
             "(t = 2.5 s, f = 0.35, e\u2098\u2090\u2093 = 7 %) \u2014 examiners give credit "
             "for it. (4) Where two cases exist (L &gt; S or L &lt; S, ascending or "
             "descending gradient), always show the CHECK. (5) Answer in points and tables "
             "rather than long paragraphs.")
    return S
