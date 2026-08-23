"""UNIT 3 - Traffic engineering and control."""
from kit import *


def build():
    S = H1("3", "Traffic Engineering and Control", "6 hours \u2022 about 14 % of the paper")

    # ------------------------------------------------------------------ 3.1
    S += H2("3.1  Scope of traffic engineering")
    S += DEF("Traffic engineering", "that branch of engineering which deals with the "
             "improvement of traffic performance of road networks and terminals \u2014 the "
             "planning, geometric design and traffic operation of roads, streets and "
             "highways, their networks, terminals and abutting lands, and their relationship "
             "with other modes of transportation.")
    S += P("The scope of traffic engineering covers <b>traffic characteristics</b>, "
           "<b>traffic studies and analysis</b>, <b>traffic operation, regulation and "
           "control</b>, <b>planning and analysis of traffic facilities</b>, "
           "<b>geometric design</b>, and <b>accident analysis and prevention</b>.")

    # ------------------------------------------------------------------ 3.2
    S += H2("3.2  Traffic characteristics")
    S += P("The three components of the traffic system are the <b>road user</b>, the "
           "<b>vehicle</b> and the <b>road</b>. Traffic characteristics are the "
           "characteristics of the first two.")
    S += H3("3.2.1  Road user characteristics")
    S += TBL([["Group of characteristics", "What it includes"],
              ["<b>Physical</b>", "Vision (acuity, peripheral vision, glare recovery), "
               "hearing, strength, and the general state of health. Vision is the most "
               "important \u2014 the <b>acute cone of vision</b> is about 3\u00b0 to 10\u00b0 "
               "and the wider peripheral vision is about 120\u00b0 to 180\u00b0."],
              ["<b>Mental</b>", "Knowledge, skill, intelligence, experience and literacy \u2014 "
               "these decide how quickly and how correctly a driver responds."],
              ["<b>Psychological</b>", "Emotions such as anger, fear, impatience, "
               "superstition and anxiety, which affect the reaction of the road user."],
              ["<b>Environmental</b>", "The conditions in which the road user is placed \u2014 "
               "traffic stream characteristics, facilities to the traffic, atmospheric "
               "conditions and the surrounding land use."]],
             widths=[2.1, 7.7], align=["l", "l"], fs=7.8,
             caption="Table 3.1  Road user characteristics.")
    S += P("<b>Reaction time and the PIEV theory.</b> The total reaction time of a driver is "
           "the time from the instant the object comes into his sight to the instant the "
           "brakes are actually applied. It is split into four parts \u2014 "
           "<b>Perception, Intellection, Emotion and Volition</b>. IRC takes the total "
           "reaction time as <b>2.5 s</b> for the design of stopping sight distance "
           "(see Fig. 2.4 in Unit 2).")
    S += H3("3.2.2  Vehicle characteristics")
    S += TBL([["Characteristic", "Design significance", "IRC / typical value"],
              ["<b>Width</b>", "Decides the lane width and the extra widening",
               "Maximum 2.5 m"],
              ["<b>Height</b>", "Decides the clearance under structures and overhead cables",
               "3.8 m (4.75 m for double-deck buses)"],
              ["<b>Length</b>", "Decides the extra widening (through the wheel base), the "
               "capacity, the parking bay size and the turning radius at intersections",
               "Single unit truck 11 m; articulated / tractor-trailer 16 m; "
               "wheel base of a commercial vehicle 6.1 m"],
              ["<b>Weight and axle load</b>", "Decides the pavement thickness and the "
               "bridge loading", "Legal maximum single axle load 10.2 tonnes; "
               "standard axle for pavement design 8.16 tonnes (80 kN)"],
              ["<b>Power and speed</b>", "Decides the gradient that can be negotiated, "
               "the overtaking sight distance and the capacity",
               "Design speed as per Table 2.2"],
              ["<b>Braking and acceleration</b>", "Decides the stopping and overtaking "
               "sight distances", "Design f = 0.35\u20130.40 longitudinal, 0.15 lateral"]],
             widths=[1.6, 4.4, 3.8], align=["l", "l", "l"], fs=7.7,
             caption="Table 3.2  Vehicular characteristics and their design significance "
                     "(IRC 3\u20131983 for dimensions).")
    S += P("Because the traffic on Indian roads is <b>highly heterogeneous</b>, vehicles of "
           "very different sizes and speeds share the same carriageway. To add them up "
           "meaningfully they are converted into a common unit \u2014 the "
           "<b>Passenger Car Unit (PCU)</b>.")
    S += TBL([["Type of vehicle", "PCU", "Type of vehicle", "PCU"],
              ["Motor cycle or scooter", "0.50", "Truck, bus or tractor-trailer", "3.00"],
              ["Passenger car, tempo, auto-rickshaw, tractor", "1.00",
               "Horse-drawn vehicle", "4.00"],
              ["Cycle", "0.50", "Small bullock cart or hand cart", "6.00"],
              ["Cycle rickshaw", "2.00", "Large bullock cart", "8.00"]],
             widths=[3.4, 0.8, 3.0, 0.8], align=["l", "c", "l", "c"], fs=7.9,
             caption="Table 3.3  Commonly used PCU equivalency factors. IRC 106\u20131990 "
                     "gives these as RANGES which depend on the percentage composition of "
                     "the vehicle type in the stream; use the values given in the question "
                     "if any are supplied.")
    S += EX("Converting a classified volume count into PCU",
            "The classified traffic volume count on an urban road for the peak hour is: "
            "cars 600, two-wheelers 800, buses 90, trucks 110, auto-rickshaws 150, "
            "cycles 200 and cycle rickshaws 40. Determine the traffic volume in vehicles "
            "per hour and in PCU per hour.",
            ["#Step 1 \u2014 total number of vehicles",
             "$600 + 800 + 90 + 110 + 150 + 200 + 40 = 1990 vehicles/hour",
             "#Step 2 \u2014 convert each class to PCU (Table 3.3)",
             "$Cars:            600 \u00d7 1.0 = 600 PCU",
             "$Two-wheelers:    800 \u00d7 0.5 = 400 PCU",
             "$Buses:            90 \u00d7 3.0 = 270 PCU",
             "$Trucks:          110 \u00d7 3.0 = 330 PCU",
             "$Auto-rickshaws:  150 \u00d7 1.0 = 150 PCU",
             "$Cycles:          200 \u00d7 0.5 = 100 PCU",
             "$Cycle rickshaws:  40 \u00d7 2.0 =  80 PCU",
             "#Step 3 \u2014 total",
             "$Total = 600+400+270+330+150+100+80 = 1930 PCU/hour",
             "!Traffic volume = 1990 vehicles/hour = 1930 PCU/hour. "
             "The design and capacity checks must be done in PCU, not in vehicles."])
    S += PYQ(["What is PCU? Why is it necessary on Indian roads? Convert the given "
              "classified count into PCU. [7 marks]",
              "Discuss the road user and vehicular characteristics that influence "
              "geometric design and traffic operation. [7 marks]",
              "What is PIEV theory? [2 marks]"])

    # ------------------------------------------------------------------ 3.3
    S += H2("3.3  Traffic engineering studies")
    S += P("The five basic traffic studies are the <b>volume</b> study, the <b>speed</b> "
           "study (spot speed, and speed and delay), the <b>origin and destination</b> study, "
           "the <b>parking</b> study and the <b>accident</b> study.")

    S += H3("3.3.1  Traffic volume study")
    S += DEF("Traffic volume", "the number of vehicles crossing a section of the road per "
             "unit time at a given period. It is expressed in vehicles per day or vehicles "
             "per hour, or in PCU per hour.")
    S += TBL([["Term", "Definition"],
              ["<b>ADT</b> (average daily traffic)",
               "The average of 24-hour counts taken over a period shorter than a year."],
              ["<b>AADT</b> (annual average daily traffic)",
               "The average of 24-hour counts taken over a <b>full year</b>, i.e. the total "
               "yearly volume divided by 365. Used for the economic analysis and for "
               "pavement design."],
              ["<b>Peak hour volume</b>",
               "The maximum number of vehicles that pass in one hour of the day."],
              ["<b>Design hourly volume</b>",
               "The volume adopted for the geometric design. Designing for the absolute peak "
               "is uneconomical, so the <b>30th highest hourly volume</b> of the year is "
               "commonly used for rural highways in India."],
              ["<b>Peak hour factor, PHF</b>",
               "A measure of how uniformly the traffic flows within the peak hour: "
               "PHF = (peak hour volume) / (4 \u00d7 peak 15-minute volume). "
               "It approaches 1.0 for a uniform flow."],
              ["<b>Traffic density</b>",
               "The number of vehicles occupying a unit length of the road, in veh/km."]],
             widths=[1.9, 7.9], align=["l", "l"], fs=7.8,
             caption="Table 3.4  Volume terminology.")
    S += H4("Methods of volume count")
    S += BUL(["<b>Manual count</b> \u2014 field enumerators with tally sheets. The only method "
              "that gives a <b>classified</b> count and turning movements, but it is "
              "labour-intensive and cannot be run continuously.",
              "<b>Mechanical / automatic count</b> \u2014 pneumatic tubes, inductive loop "
              "detectors, magnetic and photo-electric detectors, video image processing. "
              "Runs continuously but usually does not classify vehicles.",
              "<b>Moving observer (moving car) method</b> \u2014 gives the volume, the mean "
              "speed and the density from a single pair of test runs (see \u00a7 3.3.3).",
              "<b>Photographic and video methods</b> \u2014 a permanent record is obtained "
              "which can be analysed later at leisure."])
    S += H4("Presentation of volume data")
    S += BUL(["<b>Traffic flow (volume) diagram</b> \u2014 a plan of the network with bands "
              "drawn along each link, the width of the band being proportional to the volume.",
              "<b>Traffic volume count / turning movement diagram</b> \u2014 an intersection "
              "diagram with the volume of each movement written on the arrow.",
              "<b>Trend charts</b> \u2014 volumes plotted against the year, used for "
              "forecasting future traffic.",
              "<b>Variation charts</b> \u2014 hourly, daily, monthly and seasonal variation, "
              "used to fix the design hour and to plan maintenance and enforcement.",
              "<b>The 30th highest hourly volume curve</b> \u2014 the hourly volumes of the "
              "year arranged in descending order and plotted, from which the design "
              "hourly volume is read."])
    S += EX("Peak hour factor and design hourly volume",
            "The volume counted in the peak hour on a road is 1,800 vehicles, and the "
            "highest 15-minute count within that hour is 550 vehicles. Determine the peak "
            "hour factor and comment on the uniformity of the flow.",
            ["#Step 1 \u2014 peak hour factor",
             "$PHF = (peak hour volume) / (4 \u00d7 peak 15-minute volume)",
             "$= 1800 / (4 \u00d7 550) = 1800 / 2200 = 0.818",
             "#Step 2 \u2014 comment",
             "The flow rate during the busiest 15 minutes is 4 \u00d7 550 = 2,200 veh/h, "
             "against an average of 1,800 veh/h for the hour.",
             "A PHF of 0.82 shows an appreciable degree of peaking within the hour; the "
             "facility must be checked against the rate of 2,200 veh/h, not 1,800 veh/h.",
             "!PHF = 0.82 ; the design flow rate within the peak hour = 2,200 veh/h"])

    S += H3("3.3.2  Spot speed studies")
    S += DEF("Spot speed", "the instantaneous speed of a vehicle at a specified location.")
    S += P("<b>Uses:</b> to fix speed limits, to design geometric elements, to decide the "
           "location of signs and signals, to study accident-prone spots, and to check "
           "the effect of a traffic improvement measure.")
    S += P("<b>Methods:</b> the <b>enoscope</b> (mirror box) with a stop-watch, the "
           "<b>pressure-pad</b> and other electronic detectors, the <b>Doppler radar "
           "speedmeter</b>, and <b>photographic / videographic</b> methods.")
    S += FIG("f3_spotspeed",
             "Fig. 3.1  Presentation of spot-speed data \u2014 the frequency distribution "
             "curve and the cumulative frequency (S-) curve from which the percentile "
             "speeds are read.")
    S += TBL([["Percentile speed", "What it is used for"],
              ["<b>85th percentile</b>",
               "The <b>safe speed limit</b> at the location. 85 % of the drivers travel at or "
               "below this speed; the remaining 15 % are considered to be driving "
               "unreasonably fast."],
              ["<b>98th percentile</b>",
               "The <b>design speed for geometric design</b> \u2014 the elements of the road "
               "are designed so that even the fast 98th-percentile driver is safe."],
              ["<b>15th percentile</b>",
               "The <b>lower speed limit</b>, to weed out the very slow drivers who obstruct "
               "the stream and cause accidents."],
              ["<b>50th percentile</b>", "The median speed, used for general comparison."],
              ["<b>Modal speed</b>", "The most frequently observed speed \u2014 the peak of "
               "the frequency distribution curve."]],
             widths=[1.7, 8.1], align=["l", "l"], fs=7.8,
             caption="Table 3.5  Use of the percentile speeds \u2014 85th, 98th and 15th "
                     "are the ones asked in the exam.")
    S += EX("Percentile speeds from a spot-speed study",
            "A spot-speed study at a section gave the following data. Determine the 15th, "
            "50th, 85th and 98th percentile speeds and state the use of each. <br/>"
            "Speed range (km/h) : 15\u201320, 20\u201325, 25\u201330, 30\u201335, "
            "35\u201340, 40\u201345, 45\u201350, 50\u201355, 55\u201360, 60\u201365 <br/>"
            "Number of vehicles : 12, 18, 35, 62, 88, 76, 48, 30, 15, 6",
            ["#Step 1 \u2014 cumulative frequency and cumulative percentage",
             "Total number of observations = 12+18+35+62+88+76+48+30+15+6 = <b>390</b>",
             "$Upper limit  20    25    30    35    40    45    50    55    60    65",
             "$Cumulative   12    30    65   127   215   291   339   369   384   390",
             "$Cum. %     3.08  7.69 16.67 32.56 55.13 74.62 86.92 94.62 98.46 100.00",
             "#Step 2 \u2014 15th percentile (between 25 and 30 km/h)",
             "$V\u2081\u2085 = 25 + 5 \u00d7 (15 \u2212 7.69)/(16.67 \u2212 7.69) "
             "= 25 + 5 \u00d7 7.31/8.98 = 29.1 km/h",
             "#Step 3 \u2014 50th percentile (between 35 and 40 km/h)",
             "$V\u2085\u2080 = 35 + 5 \u00d7 (50 \u2212 32.56)/(55.13 \u2212 32.56) "
             "= 35 + 5 \u00d7 17.44/22.57 = 38.9 km/h",
             "#Step 4 \u2014 85th percentile (between 45 and 50 km/h)",
             "$V\u2088\u2085 = 45 + 5 \u00d7 (85 \u2212 74.62)/(86.92 \u2212 74.62) "
             "= 45 + 5 \u00d7 10.38/12.30 = 49.2 km/h",
             "#Step 5 \u2014 98th percentile (between 55 and 60 km/h)",
             "$V\u2089\u2088 = 55 + 5 \u00d7 (98 \u2212 94.62)/(98.46 \u2212 94.62) "
             "= 55 + 5 \u00d7 3.38/3.84 = 59.4 km/h",
             "!V\u2081\u2085 = 29.1 km/h (lower speed limit) ; V\u2085\u2080 = 38.9 km/h "
             "(median) ; V\u2088\u2085 = 49.2 km/h \u2192 adopt a speed limit of 50 km/h ; "
             "V\u2089\u2088 = 59.4 km/h \u2192 use 60 km/h as the design speed for the "
             "geometric elements"])

    S += H3("3.3.3  Speed and delay study \u2014 the moving observer method")
    S += P("A speed and delay study gives the <b>running speed, overall (journey) speed, "
           "the amount of delay and the causes of delay</b> over a stretch of road. The "
           "methods are the <b>floating car (moving observer) method</b>, the "
           "<b>licence-plate (vehicle number) method</b>, the <b>elevated observation "
           "method</b> and the <b>interview technique</b>.")
    S += DEF("Running speed", "the length of the stretch divided by the time the vehicle was "
             "actually <b>in motion</b> (stopped time excluded).")
    S += DEF("Journey (overall) speed", "the length of the stretch divided by the "
             "<b>total</b> time taken, including all stopped delays. "
             "Journey speed is therefore always less than or equal to the running speed.")
    S += FIG("f3_movingobs",
             "Fig. 3.2  The moving-observer method. Two runs are made over the same stretch "
             "\u2014 one against the stream and one with the stream.")
    S += FORMULA(["q = (n\u2090 + n\u1d67 \u2212 n\u2092) / (t\u2090 + t\u1d69)",
                  "t\u0304 = t\u1d69 \u2212 (n\u1d67 \u2212 n\u2092) / q",
                  "v\u0304 = L / t\u0304                  and     k = q / v\u0304"],
                 label="Moving observer method",
                 where=["q = flow of the stream (veh per unit time)",
                        "n\u2090 = number of vehicles MET by the test vehicle while running "
                        "AGAINST the stream, in time t\u2090",
                        "n\u1d67 = number of vehicles that OVERTAKE the test vehicle while "
                        "it runs WITH the stream, in time t\u1d69",
                        "n\u2092 = number of vehicles OVERTAKEN BY the test vehicle in the "
                        "same run",
                        "t\u0304 = mean travel time of the stream over the stretch",
                        "v\u0304 = space mean speed of the stream ; k = density",
                        "Keep the units consistent \u2014 if t is in minutes, q comes out in "
                        "vehicles per minute"],
                 color="teal")
    S += EX("Moving observer method",
            "In a moving-observer study over a stretch of road 1.0 km long, the test vehicle "
            "running <b>against</b> the stream took 1.5 minutes and met 80 vehicles. Running "
            "<b>with</b> the stream it took 2.0 minutes, during which 5 vehicles overtook it "
            "and it overtook 15 vehicles. Determine the flow, the mean travel time, the mean "
            "speed of the stream and the traffic density.",
            ["#Step 1 \u2014 list the data",
             "$n\u2090 = 80,  t\u2090 = 1.5 min ;  n\u1d67 = 5,  n\u2092 = 15,  "
             "t\u1d69 = 2.0 min ;  L = 1.0 km",
             "#Step 2 \u2014 flow of the stream",
             "$q = (n\u2090 + n\u1d67 \u2212 n\u2092)/(t\u2090 + t\u1d69) "
             "= (80 + 5 \u2212 15)/(1.5 + 2.0)",
             "$= 70/3.5 = 20 vehicles per minute = 20 \u00d7 60 = <b>1200 veh/h</b>",
             "#Step 3 \u2014 mean travel time of the stream",
             "$t\u0304 = t\u1d69 \u2212 (n\u1d67 \u2212 n\u2092)/q = 2.0 \u2212 "
             "(5 \u2212 15)/20 = 2.0 \u2212 (\u221210/20)",
             "$= 2.0 + 0.5 = 2.5 minutes",
             "#Step 4 \u2014 mean (space mean) speed of the stream",
             "$v\u0304 = L/t\u0304 = 1.0/2.5 = 0.4 km/min = 0.4 \u00d7 60 = "
             "<b>24 km/h</b>",
             "#Step 5 \u2014 density",
             "$k = q/v\u0304 = 1200/24 = <b>50 veh/km</b>",
             "The test vehicle itself took 2.0 min for 1 km, i.e. 30 km/h; since it "
             "overtook more vehicles (15) than overtook it (5), it was travelling faster "
             "than the stream \u2014 which is consistent with the stream speed of 24 km/h.",
             "!q = 1200 veh/h ;  t\u0304 = 2.5 min ;  v\u0304 = 24 km/h ;  k = 50 veh/km"])

    S += H3("3.3.4  Origin and destination (O\u2013D) study")
    S += P("An O\u2013D study finds out <b>where the trips begin and where they end</b>, and "
           "hence the <b>desire lines</b> of travel.")
    S += P("<b>Uses:</b> to plan the road network and to judge the need for a bypass or a "
           "new link; to locate terminals, parking areas and bus stops; to plan for "
           "improvement of an existing route; and to establish the desire lines of travel "
           "for transport planning.")
    S += P("<b>Methods:</b> <b>roadside interview</b>; <b>licence-plate (registration "
           "number) method</b>; <b>return post-card method</b>; <b>tag-on-vehicle method</b>; "
           "and the <b>home-interview method</b>.")
    S += P("<b>Presentation:</b> as an <b>O\u2013D table (matrix)</b> giving the number of "
           "trips from each zone to every other zone, and as a <b>desire-line diagram</b>, "
           "in which straight lines are drawn between the origin and destination zones with "
           "the width of each line proportional to the number of trips. The desire-line "
           "diagram shows immediately where a new facility is most needed.")

    S += H3("3.3.5  Accident studies")
    S += P("<b>Objects:</b> to study the causes of accidents and to suggest remedial "
           "measures; to evaluate the improvements already carried out; to support the "
           "design of the geometric and control elements; and to compute the accident cost.")
    S += P("The <b>causes</b> of accidents are grouped under the <b>road user</b> "
           "(excessive speed, overtaking violations, carelessness, fatigue, intoxication, "
           "jumping signals), the <b>vehicle</b> (brake or tyre failure, defective lights, "
           "steering failure), the <b>road</b> (poor alignment, inadequate sight distance, "
           "poor skid resistance, poor lighting, potholes), the <b>traffic conditions</b> "
           "(mixed traffic, encroachment, inadequate control) and the "
           "<b>environment</b> (rain, fog, glare).")
    S += FIG("f3_collision",
             "Fig. 3.3  The two accident diagrams. A <b>collision diagram</b> records the "
             "MANNER of each accident and is NOT to scale; a <b>condition diagram</b> "
             "records the physical conditions of the site and IS drawn to scale.")
    S += FORMULA(["Accident rate per 100 million vehicle-kilometres:",
                  "R = (A \u00d7 10\u2078) / (365 \u00d7 ADT \u00d7 N \u00d7 L)",
                  "Accident rate per million entering vehicles (for an intersection):",
                  "R = (A \u00d7 10\u2076) / (365 \u00d7 ADT \u00d7 N)"],
                 label="Accident rates",
                 where=["A = total number of accidents in the period",
                        "ADT = average daily traffic (vehicles per day)",
                        "N = number of years of the study period",
                        "L = length of the stretch in km"],
                 color="rust")
    S += NOTE("The <b>3 E's</b> of accident prevention: <b>Engineering</b> (better geometric "
              "design, skid-resistant surfaces, road furniture, lighting), "
              "<b>Enforcement</b> (speed limits, licensing, the Motor Vehicles Act) and "
              "<b>Education</b> (road safety education and publicity). Some authors add a "
              "fourth E \u2014 <b>Environment</b> or <b>Emergency care</b>.")
    S += PYQ(["Distinguish between a collision diagram and a condition diagram. [7 marks]",
              "Explain the moving observer method and derive/state its formulae; solve the "
              "given data. [14 marks \u2014 asked very often]",
              "Explain the significance of the 85th and 98th percentile speeds. [2 marks]",
              "What is a desire line diagram? What are the uses of an O\u2013D study? "
              "[7 marks]",
              "State the causes of road accidents and the measures for their prevention. "
              "[7 marks]"])

    # ------------------------------------------------------------------ 3.4
    S += H2("3.4  Traffic flow characteristics and capacity")
    S += H3("3.4.1  The three fundamental parameters")
    S += FORMULA(["q = k \u00d7 v\u0304\u209b            (the fundamental relation of "
                  "traffic flow)",
                  "Time mean speed:    v\u0304\u209c = (1/n) \u03a3 v\u1d62      "
                  "(arithmetic mean of the spot speeds)",
                  "Space mean speed:   v\u0304\u209b = n / \u03a3 (1/v\u1d62)      "
                  "(harmonic mean of the spot speeds)",
                  "v\u0304\u209c = v\u0304\u209b + \u03c3\u209b\u00b2 / v\u0304\u209b       "
                  "\u21d2 time mean speed \u2265 space mean speed, always",
                  "Time headway  h = 3600 / q  (s)        Space headway (spacing)  "
                  "s = 1000 / k  (m)"],
                 label="Fundamental relations",
                 where=["q = flow or volume in veh/h",
                        "k = density in veh/km",
                        "v\u0304\u209b = space mean speed in km/h \u2014 THIS is the speed "
                        "that must be used in q = k v",
                        "\u03c3\u209b\u00b2 = variance of the spot speeds about the space "
                        "mean speed"])
    S += EX("Time mean speed and space mean speed",
            "The spot speeds of five vehicles observed at a section are 30, 40, 50, 60 and "
            "70 km/h. Compute the time mean speed and the space mean speed. If the density "
            "is 25 veh/km, find the flow.",
            ["#Step 1 \u2014 time mean speed (arithmetic mean)",
             "$v\u0304\u209c = (30 + 40 + 50 + 60 + 70)/5 = 250/5 = 50.0 km/h",
             "#Step 2 \u2014 space mean speed (harmonic mean)",
             "$\u03a3(1/v\u1d62) = 1/30 + 1/40 + 1/50 + 1/60 + 1/70",
             "$= 0.03333 + 0.02500 + 0.02000 + 0.01667 + 0.01429 = 0.10929",
             "$v\u0304\u209b = n / \u03a3(1/v\u1d62) = 5 / 0.10929 = 45.75 km/h",
             "#Step 3 \u2014 flow",
             "$q = k \u00d7 v\u0304\u209b = 25 \u00d7 45.75 = 1143.8 \u2248 1144 veh/h",
             "!v\u0304\u209c = 50.0 km/h ;  v\u0304\u209b = 45.75 km/h ;  q \u2248 1144 veh/h. "
             "Note that the space mean speed is the smaller of the two, as it always must be."])
    S += H3("3.4.2  Greenshields' model and the fundamental diagrams")
    S += P("Greenshields assumed the simplest possible relation \u2014 a <b>linear</b> one "
           "\u2014 between speed and density. From it the flow\u2013density and "
           "speed\u2013flow relations follow as parabolas.")
    S += FIG("f3_flow",
             "Fig. 3.4  The three fundamental diagrams of traffic flow for Greenshields' "
             "linear speed\u2013density model.")
    S += FORMULA(["v = v_f (1 \u2212 k / k_j)                    [linear speed\u2013density]",
                  "q = k v = v_f ( k \u2212 k\u00b2 / k_j )        [parabolic flow\u2013density]",
                  "Maximum flow (capacity):   q_max = v_f k_j / 4",
                  "which occurs at   k_o = k_j / 2   and   v_o = v_f / 2"],
                 label="Greenshields' model",
                 where=["v_f = free (mean) speed, i.e. the speed as the density tends to zero",
                        "k_j = jam density, i.e. the density when the vehicles are bumper to "
                        "bumper and the speed is zero",
                        "The upper branch of the speed\u2013flow curve is free flow, the "
                        "lower branch is congested (forced) flow; the same flow can occur "
                        "at two different speeds"])
    S += EX("Greenshields' model \u2014 capacity and the two possible speeds",
            "The free speed on a road is 60 km/h and the jam density is 120 veh/km. "
            "Assuming Greenshields' linear model, determine (a) the maximum flow and the "
            "speed and density at which it occurs, and (b) the two possible speeds and "
            "densities at which the flow is 1,500 veh/h.",
            ["#Step 1 \u2014 maximum flow",
             "$q_max = v_f k_j / 4 = (60 \u00d7 120)/4 = 7200/4 = <b>1800 veh/h</b>",
             "$It occurs at k_o = k_j/2 = 60 veh/km and v_o = v_f/2 = 30 km/h",
             "#Step 2 \u2014 express the flow in terms of speed",
             "From v = v_f(1 \u2212 k/k_j):   k = k_j(1 \u2212 v/v_f) = 120(1 \u2212 v/60)",
             "$q = k v = 120 v (1 \u2212 v/60) = 120 v \u2212 2 v\u00b2",
             "#Step 3 \u2014 put q = 1500 and solve the quadratic",
             "$120 v \u2212 2 v\u00b2 = 1500  \u21d2  2v\u00b2 \u2212 120 v + 1500 = 0  "
             "\u21d2  v\u00b2 \u2212 60 v + 750 = 0",
             "$v = [60 \u00b1 \u221a(3600 \u2212 3000)]/2 = [60 \u00b1 \u221a600]/2 "
             "= (60 \u00b1 24.49)/2",
             "$v = 42.25 km/h   or   v = 17.75 km/h",
             "#Step 4 \u2014 the corresponding densities",
             "$k = q/v = 1500/42.25 = 35.5 veh/km   (free-flow branch)",
             "$k = q/v = 1500/17.75 = 84.5 veh/km   (congested branch)",
             "!q_max = 1800 veh/h at v = 30 km/h and k = 60 veh/km. "
             "A flow of 1500 veh/h occurs either at 42.25 km/h with k = 35.5 veh/km "
             "(free flow) or at 17.75 km/h with k = 84.5 veh/km (congested flow)."])
    S += H3("3.4.3  Capacity and level of service")
    S += TBL([["Term", "Definition"],
              ["<b>Basic capacity</b>",
               "The maximum number of vehicles that can pass a point in unit time under the "
               "<b>most ideal</b> roadway and traffic conditions. It is a theoretical value "
               "and is the same for all roads of the same type."],
              ["<b>Possible capacity</b>",
               "The maximum number of vehicles that can pass under the <b>prevailing</b> "
               "roadway and traffic conditions. It may be far lower than the basic capacity."],
              ["<b>Practical (design) capacity</b>",
               "The maximum number of vehicles that can pass without unreasonable delay or "
               "restriction to the driver's freedom \u2014 the value actually used in design. "
               "It lies between the possible and the basic capacity."],
              ["<b>Level of service (LOS)</b>",
               "A qualitative measure, on a scale A to F, of the operating conditions "
               "experienced by the driver. A = free flow, E = at capacity, F = forced or "
               "breakdown flow. It is measured by the volume-to-capacity ratio (v/c) and by "
               "the operating speed."]],
             widths=[1.9, 7.9], align=["l", "l"], fs=7.8,
             caption="Table 3.6  Types of capacity and the level of service.")
    S += FIG("f3_los",
             "Fig. 3.5  Levels of service A to F against the volume-to-capacity ratio.")
    S += FORMULA(["Theoretical (basic) capacity from the spacing of vehicles:",
                  "C = 1000 V / S       (vehicles per hour per lane)",
                  "Capacity from the time headway:   C = 3600 / H\u209c",
                  "Minimum safe space headway:   S = SSD + length of the vehicle"],
                 label="Capacity",
                 where=["C = capacity in veh/h per lane",
                        "V = speed in km/h",
                        "S = average centre-to-centre spacing (space headway) of the "
                        "vehicles in m",
                        "H\u209c = average time headway in seconds"],
                 color="gold")
    S += EX("Theoretical capacity of a lane from the safe stopping distance",
            "Calculate the theoretical maximum capacity of a single lane if the speed is "
            "60 km/h, the average length of a vehicle is 6 m, the reaction time is 2.5 s "
            "and f = 0.36. Also find the capacity if the observed average time headway "
            "is 2.0 s.",
            ["#Step 1 \u2014 stopping sight distance at 60 km/h",
             "$Lag distance = 0.278 \u00d7 60 \u00d7 2.5 = 41.70 m",
             "$Braking distance = 60\u00b2/(254 \u00d7 0.36) = 3600/91.44 = 39.37 m",
             "$SSD = 41.70 + 39.37 = 81.07 m",
             "#Step 2 \u2014 minimum safe space headway",
             "$S = SSD + length of the vehicle = 81.07 + 6.0 = 87.07 m",
             "#Step 3 \u2014 capacity from the spacing",
             "$C = 1000 V / S = (1000 \u00d7 60)/87.07 = 60000/87.07 = 689 veh/h per lane",
             "#Step 4 \u2014 capacity from the observed time headway",
             "$C = 3600 / H\u209c = 3600/2.0 = 1800 veh/h per lane",
             "!Theoretical capacity based on the safe stopping distance = 689 veh/h/lane; "
             "based on the observed headway of 2 s = 1800 veh/h/lane. The huge difference "
             "shows that drivers in practice keep far shorter headways than the "
             "safe-stopping criterion would allow."])
    S += IRCBOX("Design service volumes commonly quoted for rural roads (IRC): "
                "single-lane road 2,000 PCU/day; intermediate lane 6,000 PCU/day; "
                "two-lane road 15,000 PCU/day. For urban roads IRC 106\u20131990 gives the "
                "capacity of a two-lane one-way road as about 2,400 PCU/h and of a "
                "two-lane two-way road as about 1,500 PCU/h.")
    S += PYQ(["Define basic, possible and practical capacity. [7 marks]",
              "Explain the terms level of service, time mean speed and space mean speed. "
              "[7 marks]",
              "Derive the relation q = k v and explain the speed\u2013flow\u2013density "
              "diagrams. [7 marks]",
              "Using Greenshields' model, find the capacity for the given free speed and "
              "jam density. [7 marks]"])
    S += REF("Kadiyali \u2014 <i>Traffic Engineering and Transport Planning</i>, chapters on "
             "traffic characteristics, traffic studies and traffic flow theory; "
             "Khanna, Justo &amp; Veeraragavan, chapter 'Traffic Engineering'; "
             "IRC 9\u20131972 (traffic census) and IRC 106\u20131990 (capacity of urban roads).")
    return S
