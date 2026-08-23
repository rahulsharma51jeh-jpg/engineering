"""Cover page, how-to-use page, exam-pattern analysis and table of contents."""
from kit import *


def cover():
    S = [Spacer(1, 30 * mm)]
    S += [Paragraph("BIHAR ENGINEERING UNIVERSITY, PATNA", ParagraphStyle(
        "cv0", fontName="DJSans-Bold", fontSize=10.5, leading=14,
        alignment=TA_CENTER, textColor=BLUE))]
    S += [Paragraph("B.Tech &nbsp;&bull;&nbsp; Civil Engineering &nbsp;&bull;&nbsp; Course Code 101401",
                    ParagraphStyle("cv1", fontName="DJSans", fontSize=9.5, leading=13,
                                   alignment=TA_CENTER, textColor=GREY))]
    S += [Spacer(1, 13 * mm)]
    S += [Paragraph("TRANSPORTATION", TITLE), Paragraph("ENGINEERING", TITLE)]
    S += [Spacer(1, 5 * mm)]
    S += [Table([[""]], colWidths=[70 * mm], style=TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 2.2, GOLD)]), hAlign="CENTER")]
    S += [Spacer(1, 5 * mm)]
    S += [Paragraph("Complete Semester&nbsp;Examination Notes", ParagraphStyle(
        "cv2", parent=SUBTITLE, fontName="DJSans-Bold", fontSize=14))]
    S += [Spacer(1, 3 * mm)]
    S += [Paragraph("Theory with diagrams &nbsp;&bull;&nbsp; solved numericals &nbsp;&bull;&nbsp; "
                    "formula sheet &nbsp;&bull;&nbsp; previous-year question bank",
                    ParagraphStyle("cv3", fontName="DJSerif-It", fontSize=9.8,
                                   leading=13, alignment=TA_CENTER, textColor=GREY))]
    S += [Spacer(1, 11 * mm)]

    units = [["Unit", "Topic", "Hrs"],
             ["1", "Highway development and planning; classification of roads; road development "
                   "in India; current projects; highway alignment and project preparation", "8"],
             ["2", "Geometric design of highways \u2014 cross-section elements, sight distance, "
                   "horizontal and vertical alignment, intersections", "5"],
             ["3", "Traffic engineering and control \u2014 traffic characteristics, traffic "
                   "engineering studies, traffic flow and capacity", "6"],
             ["4", "Traffic regulation and control; design of road intersections; parking "
                   "facilities; highway lighting", "8"],
             ["5", "Pavement materials \u2014 soils, aggregates, bituminous binders and mixes, "
                   "cement and cement concrete", "5"],
             ["6", "Design of pavements \u2014 flexible and rigid pavements, stresses, IRC 37 "
                   "and IRC 58 design", "10"]]
    S += TBL(units, widths=[0.7, 8.0, 0.8], align=["c", "l", "c"],
             fs=8.0, first_bold=True, caption=None)
    S += [Spacer(1, 4 * mm)]
    S += [Paragraph("PRESCRIBED TEXT / REFERENCE BOOKS", ParagraphStyle(
        "cv4", fontName="DJSans-Bold", fontSize=8.6, leading=11,
        alignment=TA_CENTER, textColor=NAVY, spaceAfter=4))]
    refs = [
        "Khanna, S.K., Justo, C.E.G. and Veeraragavan, A. \u2014 <i>Highway Engineering</i>, "
        "Revised 10th Edition, Nem Chand &amp; Bros, 2017. &nbsp;<b>[primary book for this paper]</b>",
        "Kadiyali, L.R. \u2014 <i>Traffic Engineering and Transport Planning</i>, Khanna Publishers.",
        "Partha Chakraborty and Animesh Das \u2014 <i>Principles of Transportation "
        "Engineering</i>, PHI Learning.",
        "Mannering, F.L., Washburn, S.S. and Kilareski, W.P. \u2014 <i>Principles of Highway "
        "Engineering and Traffic Analysis</i>, 4th Edition, John Wiley.",
        "Srinivasa Kumar, R. \u2014 <i>Textbook of Highway Engineering</i>, Universities Press, 2011.",
        "Wright, P.H. and Dixon, K.K. \u2014 <i>Highway Engineering</i>, 7th Edition, "
        "Wiley Student Edition, 2009.",
        "IRC codes referred throughout: IRC 37\u20132018, IRC 58\u20132015, IRC 73\u20131980, "
        "IRC 86\u20131983, IRC 65\u20132017, IRC 93\u20131985, IRC 106\u20131990, IRC SP 41, "
        "IRC 67, IRC 35, IRC 3\u20131983.",
    ]
    inner = [Paragraph("%d. &nbsp;%s" % (i + 1, t), ParagraphStyle(
        "cvr", fontName="DJSerif", fontSize=7.9, leading=10.6, leftIndent=12,
        firstLineIndent=-12, spaceAfter=2.6)) for i, t in enumerate(refs)]
    S += [Table([[inner]], colWidths=[FW], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LGREY),
        ("LINEBEFORE", (0, 0), (-1, -1), 2.4, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))]
    return S


def howto():
    S = SETHDR("How to use these notes")
    S += H2("How to use these notes", toc=False)
    S += P("These notes are written strictly to the BEU 101401 syllabus printed on the cover. "
           "Every unit follows the same fixed sequence so that you always know where to look:")
    S += TBL([["Element", "What it contains", "How to use it in the exam"],
              ["Numbered sections", "The theory, in the order of the syllabus, with every "
               "definition and classification spelled out.",
               "This is your answer material for the long (14-mark) questions."],
              ["Figures", "47 labelled engineering diagrams \u2014 cross-sections, sight-distance "
               "diagrams, curve geometry, apparatus sketches, stress diagrams.",
               "Reproduce the labelled sketch first, then write the theory around it. "
               "A diagram alone often carries 3\u20135 marks."],
              ["Blue formula boxes", "The working formula with every symbol and its unit defined.",
               "Quote the formula, then substitute. Never substitute without writing "
               "the formula first."],
              ["Orange solved numericals", "Fully worked problems of exactly the type asked, "
               "solved step by step with the answer boxed.",
               "Practise these with the book closed. The numerical part of this paper is "
               "highly repetitive."],
              ["Gold PYQ flags", "The questions on that topic which recur in BEU / AKU papers.",
               "Use them to decide what to revise first when time is short."],
              ["Teal exam tips / IRC boxes", "Standard IRC values, common mistakes, and "
               "shortcuts.", "The IRC values are frequently asked as 2-mark questions."],
              ["Formula sheet", "Every formula in the paper condensed on to facing pages.",
               "This is the last thing to read before you enter the hall."]],
             widths=[1.5, 4.0, 3.6], align=["l", "l", "l"], fs=7.7, first_bold=True)

    S += H2("The BEU question-paper pattern for this subject", toc=False)
    S += P("The end-semester paper of Bihar Engineering University for a theory subject such as "
           "this one is normally set as follows:")
    S += TBL([["Question", "Nature", "Choice", "Marks"],
              ["Q.1", "Short-answer / objective questions covering the whole syllabus "
                      "(ten parts, roughly two per unit)",
               "Answer any seven of ten", "7 &times; 2 = 14"],
              ["Q.2 to Q.8", "Long questions. Each is usually split into two or three parts \u2014 "
                             "commonly one theory part plus one numerical or one diagram part",
               "Answer any four of seven", "4 &times; 14 = 56"],
              ["", "", "Total", "70 (3 hours)"]],
             widths=[1.0, 5.4, 1.9, 1.3], align=["c", "l", "l", "c"], fs=7.9,
             first_bold=True,
             caption="Table: the usual BEU / AKU B.Tech end-semester pattern. Always re-read "
                     "the instructions printed on your own question paper \u2014 the choice "
                     "pattern is occasionally varied.")
    S += NOTE("Because you answer only four long questions out of seven, you can leave roughly "
              "one-third of the syllabus thin \u2014 but Q.1 is compulsory and it samples the "
              "WHOLE syllabus. So: study four or five units in depth for the long questions, "
              "and make sure you know the definitions, IRC values and one-line facts from every "
              "unit for Q.1.", head="Strategy that follows from the pattern")

    S += H2("Unit-wise weightage and priority", toc=False)
    S += P("The syllabus allots 42 contact hours. The share of each unit in the timetable is a "
           "good proxy for its share in the paper, and it matches what the past papers show:")
    S += TBL([["Unit", "Topic", "Hrs", "Share", "Numericals?", "Priority"],
              ["6", "Design of pavements", "10", "24 %",
               "Very heavy \u2014 ESWL, MSA, Westergaard stresses, joints, dowel and tie bars",
               "HIGHEST"],
              ["1", "Highway development and planning", "8", "19 %",
               "Light \u2014 road density, saturation system", "High (theory-scoring)"],
              ["4", "Traffic regulation, intersections, parking, lighting", "8", "19 %",
               "Heavy \u2014 Webster signal design, rotary capacity, parking, lamp spacing",
               "HIGHEST"],
              ["3", "Traffic engineering and control", "6", "14 %",
               "Medium \u2014 moving observer, PCU, capacity, speed studies", "High"],
              ["2", "Geometric design", "5", "12 %",
               "Very heavy \u2014 SSD/OSD, superelevation, transition and vertical curves",
               "HIGHEST (marks per hour of study are the best here)"],
              ["5", "Pavement materials", "5", "12 %",
               "Light \u2014 CBR, aggregate test values, Marshall", "Medium"]],
             widths=[0.55, 3.0, 0.5, 0.6, 3.6, 1.75],
             align=["c", "l", "c", "c", "l", "l"], fs=7.6, first_bold=True)
    S += TIP("Units 2, 4 and 6 carry almost all the numerical marks and together account for "
             "over half the paper. If you have only three days, do Unit 2, Unit 6 and Unit 4 "
             "properly, then skim Units 1, 3 and 5 for the short-answer questions.")
    S += REF("Syllabus: BEU B.Tech Civil Engineering, Course Code 101401, Transportation "
             "Engineering (6 units, 42 hours).")
    return S


def toc():
    S = [PageBreak()]
    S += SETHDR("Contents")
    S += [Paragraph("Contents", TOCTITLE)]
    S += [Table([[""]], colWidths=[FW], style=TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 1.6, GOLD)]))]
    S += [Spacer(1, 7)]
    S += [make_toc()]
    return S
