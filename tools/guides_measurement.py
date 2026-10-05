# -*- coding: utf-8 -*-
"""Guides: Measurement."""

CAT = "Measurement"

GUIDES = [

# ---------------------------------------------------------------- metric
dict(
    slug="metric-units", cat=CAT, nav="Metric units & converting", read=5,
    h1="Metric units and how to convert them",
    card="mm, cm, m, km, g, kg, ml and litres \u2014 every conversion is a place-value shift.",
    years="Years 3\u20136",
    seo="Metric units explained \u2014 converting length, mass and capacity | Math It!",
    desc="The metric units children need, the conversion factors to memorise, how every conversion is a power-of-ten shift, and the imperial approximations on the KS2 curriculum.",
    keywords="metric units, converting units, cm to m, g to kg, ml to litres, metric conversions KS2, year 5 measures, imperial conversions",
    intro="""<p>The metric system is built on tens, which means every conversion is a place-value
      shift rather than a multiplication you have to think hard about. Converting 2.4 km to metres
      is the same operation as multiplying by 1,000 \u2014 shifting the digits three columns
      left.</p>
      <p>There are only about eight facts to know, and every one of them follows one of three
      patterns: \u00d7 10, \u00d7 100 or \u00d7 1,000.</p>""",
    steps=[
        ("Learn the prefixes",
         "<p><strong>milli-</strong> means a thousandth, <strong>centi-</strong> a hundredth and "
         "<strong>kilo-</strong> a thousand. So a millimetre is a thousandth of a metre, and a "
         "kilogram is a thousand grams.</p>"),
        ("Memorise the eight conversions",
         "<p>10 mm = 1 cm. 100 cm = 1 m. 1,000 mm = 1 m. 1,000 m = 1 km. 1,000 g = 1 kg. "
         "1,000 kg = 1 tonne. 1,000 ml = 1 litre. 1 ml = 1 cm\u00b3.</p>"),
        ("Decide whether the answer gets bigger or smaller",
         "<p>Going to a <em>smaller</em> unit means you need <em>more</em> of them, so multiply. "
         "Going to a bigger unit means fewer, so divide. Say this out loud before calculating.</p>"),
        ("Shift the digits",
         "<p>\u00d7 1,000 moves the digits three columns left; \u00f7 1,000 moves them three right. "
         "No written multiplication is ever needed.</p>"),
        ("Keep the unit attached to the number",
         "<p>An answer of \u201c2,400\u201d is incomplete. \u201c2,400 m\u201d is the answer.</p>"),
    ],
    examples=[
        ("Convert 2.4 km to metres.",
         ["km \u2192 m goes to a smaller unit, so multiply.",
          "1 km = 1,000 m, so \u00d7 1,000.",
          "Shift the digits three places left."],
         "2,400 m"),
        ("Convert 450 g to kilograms.",
         ["g \u2192 kg goes to a bigger unit, so divide.",
          "1,000 g = 1 kg, so \u00f7 1,000.",
          "Shift the digits three places right."],
         "0.45 kg"),
        ("Convert 7.5 cm to millimetres.",
         ["cm \u2192 mm is a smaller unit, so multiply by 10.",
          "Shift one place left."],
         "75 mm"),
        ("Add 1.2 litres and 650 ml.",
         ["Convert to the same unit first. 1.2 l = 1,200 ml.",
          "1,200 + 650 = 1,850 ml.",
          "Or expressed in litres: 1.85 l."],
         "1,850 ml (1.85 l)"),
    ],
    mistakes=[
        ("Multiplying when you should divide.",
         "Ask whether the answer ought to be a bigger or a smaller number first. 450 g in kilograms must be less than 1, so you divide."),
        ("Adding quantities that are in different units.",
         "1.2 l + 650 ml is not 651.2 of anything. Convert to a common unit before calculating."),
        ("Confusing centi- and milli-.",
         "Centi- is a hundredth (100 cm in a metre); milli- is a thousandth (1,000 mm in a metre). A centimetre is the bigger one."),
        ("Dropping the unit from the final answer.",
         "Measurement answers are wrong without units, and marks are routinely lost for this alone."),
    ],
    sections=[
        ("Area and volume units behave differently",
         """<p>This catches almost everybody. 1 m = 100 cm, but 1 m\u00b2 is
         <strong>10,000</strong> cm\u00b2, because a square metre is 100 cm by 100 cm.</p>
         <p>Similarly 1 m\u00b3 = 1,000,000 cm\u00b3. The rule: square the conversion factor for
         areas and cube it for volumes. Primary rarely tests this directly, but it is worth knowing
         why 1 m\u00b2 is not 100 cm\u00b2.</p>"""),
        ("Imperial approximations on the curriculum",
         """<p>Year 6 is expected to know rough equivalences between metric and imperial units:</p>
         <ul>
           <li>1 inch \u2248 2.5 cm</li>
           <li>1 foot \u2248 30 cm</li>
           <li>1 mile \u2248 1.6 km (so 5 miles \u2248 8 km)</li>
           <li>1 pound \u2248 450 g</li>
           <li>1 pint \u2248 568 ml, usually rounded to 570 ml</li>
           <li>1 gallon \u2248 4.5 litres</li>
         </ul>
         <p>These are approximations by design. Exam questions will say \u201cabout\u201d, or give
         the conversion factor in the question.</p>"""),
        ("Time is the odd one out",
         """<p>Time is not metric and never will be. 60 seconds in a minute, 60 minutes in an hour,
         24 hours in a day, 7 days in a week \u2014 none of these are powers of ten, which is why
         time calculations need a different approach, usually counting on through the next whole
         hour rather than subtracting.</p>
         <p>2 hours 45 minutes plus 1 hour 30 minutes: add the hours (3), add the minutes (75), then
         exchange 60 minutes for an hour. Answer: 4 hours 15 minutes.</p>"""),
    ],
    faqs=[
        ("How many centimetres are there in a metre?",
         "100. And 1,000 millimetres in a metre, since there are 10 mm in each centimetre."),
        ("Is 1 ml really the same as 1 cm\u00b3?",
         "Yes, exactly. A litre is defined as 1,000 cm\u00b3, which makes a millilitre exactly one cubic centimetre."),
        ("Do children need imperial units?",
         "Only the rough equivalences in Year 6 \u2014 miles to kilometres, pints to litres and so on. Calculations themselves are always set in metric."),
        ("What is the easiest way to remember which way to convert?",
         "A smaller unit means a bigger number. 1 m is 100 cm, so converting metres to centimetres makes the number larger."),
    ],
    cta=("Practise unit conversions", "practice.html?year=5&level=medium"),
    related=["powers-of-ten", "decimals-explained", "place-value", "simple-algebra"],
),

# ---------------------------------------------------------------- time
dict(
    slug="telling-the-time", cat=CAT, nav="Telling the time", read=6,
    h1="Telling the time, and calculating with it",
    card="Analogue, digital and 24-hour clocks, plus the counting-on method for durations.",
    years="Years 1\u20136",
    seo="Telling the time explained \u2014 analogue, 24-hour and durations | Math It!",
    desc="How to read an analogue clock, convert to and from the 24-hour clock, and work out durations by counting on through the next whole hour instead of subtracting.",
    keywords="telling the time, 24 hour clock, reading a clock face, time durations, time intervals, am pm, KS2 time, year 4 time",
    intro="""<p>Time is the one measurement on the primary curriculum that is not metric, and that is
      exactly why children find it hard. Everywhere else ten of something makes the next thing up.
      Here it is sixty seconds to a minute, sixty minutes to an hour, twenty-four hours to a day
      and seven days to a week.</p>
      <p>None of those are powers of ten, so the place-value shortcuts that make kilometres easy
      are no help at all. Time needs its own method, and that method is counting on.</p>""",
    steps=[
        ("Read the hour hand first",
         "<p>The short hand gives the hour. It moves continuously, so at twenty to four it sits "
         "<em>between</em> 3 and 4 \u2014 and the hour you say is the one it has passed, not the one "
         "it is approaching. This is the single commonest analogue error.</p>"),
        ("Then read the minute hand in fives",
         "<p>Each number on the face is five minutes. Count round in fives from the 12, then add "
         "the small marks. The 7 is 35 minutes.</p>"),
        ("Past to half, then to after half",
         "<p>Up to 30 minutes we say \u201cpast\u201d; after 30 we usually say \u201cto\u201d the next "
         "hour. 3:40 is \u201ctwenty to four\u201d, because there are twenty minutes left until "
         "4 o'clock.</p>"),
        ("Convert to 24-hour by adding 12 after midday",
         "<p>Morning times keep their number and gain a leading zero: 9:15 am is 09:15. Afternoon "
         "and evening times add 12: 3:40 pm is 15:40. Midnight is 00:00 and midday is 12:00.</p>"),
        ("Find durations by counting on, never by subtracting",
         "<p>Jump to the next whole hour, then in whole hours, then the remaining minutes. "
         "Column subtraction fails on times because the columns are not base ten.</p>"),
    ],
    examples=[
        ("A film starts at 14:35 and ends at 16:20. How long is it?",
         ["Count on from 14:35 to the next whole hour: 25 minutes gets you to 15:00.",
          "15:00 to 16:00 is 1 hour.",
          "16:00 to 16:20 is 20 minutes.",
          "Total: 1 hour and 25 + 20 = 45 minutes."],
         "1 hour 45 minutes"),
        ("Write 7:50 pm as a 24-hour time.",
         ["It is after midday, so add 12 to the hour.",
          "7 + 12 = 19."],
         "19:50"),
        ("A train leaves at 09:48 and the journey takes 2 hours 35 minutes. When does it arrive?",
         ["Add the hours first: 09:48 + 2 hours = 11:48.",
          "Add 12 minutes to reach 12:00.",
          "35 \u2212 12 = 23 minutes still to add."],
         "12:23"),
        ("How many minutes between quarter to eleven and twenty past eleven?",
         ["Quarter to eleven is 10:45; twenty past eleven is 11:20.",
          "10:45 to 11:00 is 15 minutes.",
          "11:00 to 11:20 is 20 minutes."],
         "35 minutes"),
    ],
    mistakes=[
        ("Using column subtraction: 16:20 \u2212 14:35 treated as 1620 \u2212 1435 = 185 minutes.",
         "Minutes are base 60, not base 100. Count on through the next whole hour instead \u2014 the answer is 1 h 45, which is 105 minutes."),
        ("Reading 3:40 as \u2018twenty to three\u2019.",
         "The hour hand has already passed 3 and is heading for 4, so it is twenty to <em>four</em>."),
        ("Adding 12 to a morning time when converting to 24-hour.",
         "Only times from 1 pm onwards gain 12. 9:15 am is simply 09:15."),
        ("Writing 2 hours 90 minutes.",
         "Exchange 60 minutes for an hour, exactly as you would exchange ten ones for a ten. It is 3 hours 30 minutes."),
    ],
    sections=[
        ("The number line is the right tool",
         """<p>Draw a line, mark the start time at the left and the end time at the right, then hop:
         to the next whole hour, along in hours, then the leftover minutes. Add the hops.</p>
         <p>It looks childish and it is the method secondary teachers still recommend, because it
         never produces the base-60 errors that subtraction does. For 09:48 to 12:23 the hops are
         12 minutes, 2 hours, 23 minutes \u2014 giving 2 hours 35 minutes.</p>"""),
        ("Timetables",
         """<p>Timetable questions are the most common time question in KS2 reasoning papers, and
         they are really three skills at once: reading a table accurately, converting between
         clock formats, and calculating a duration.</p>
         <p>Two things catch children out. First, a column may skip a stop \u2014 a dash means the
         train does not stop there, not that it takes no time. Second, journeys that cross midday
         or midnight: 23:40 to 00:15 is 35 minutes, not an error.</p>"""),
        ("What is expected, and when",
         """<p>Year 1 reads o'clock and half past. Year 2 adds quarter past and quarter to and
         counts in five-minute intervals. Year 3 reads to the nearest minute, uses Roman numeral
         clock faces and meets the 24-hour clock. Year 4 converts between analogue and digital
         including 12- and 24-hour formats. Years 5 and 6 solve multi-step duration and timetable
         problems.</p>
         <p>Analogue reading is worth maintaining even in a digital household \u2014 clock faces
         appear in every SATs paper, and a round clock also teaches fractions of a turn, which
         feeds straight into angles.</p>"""),
        ("Facts worth knowing by heart",
         """<ul>
           <li>60 seconds = 1 minute, 60 minutes = 1 hour, 24 hours = 1 day</li>
           <li>7 days = 1 week, 52 weeks \u2248 1 year, 365 days = 1 year (366 in a leap year)</li>
           <li>A leap year is any year divisible by 4, except century years not divisible by
           400 \u2014 so 2000 was a leap year and 1900 was not</li>
           <li>\u201cThirty days hath September, April, June and November\u201d</li>
         </ul>"""),
    ],
    faqs=[
        ("Why do children find telling the time so hard?",
         "Because a clock face shows two different scales at once \u2014 hours and minutes \u2014 using hands of different lengths on the same numbers, and because time is base 60 rather than base 10."),
        ("How do I work out a duration that crosses midnight?",
         "Count on to midnight, then on again from 00:00. From 23:40 to 00:15 is 20 minutes plus 15 minutes, so 35 minutes."),
        ("Is 12:00 am midday or midnight?",
         "Midnight. Midday is 12:00 pm. The ambiguity is real enough that timetables normally use 00:00 and 12:00 in 24-hour format instead."),
        ("When should a child read an analogue clock fluently?",
         "To the nearest minute by the end of Year 3 in England, with 12- and 24-hour conversion secure by the end of Year 4."),
    ],
    cta=("Practise time and measures questions", "practice.html?year=4&level=medium&topics=measures"),
    related=["metric-units", "money-and-change", "word-problems", "column-subtraction"],
),

# ---------------------------------------------------------------- money
dict(
    slug="money-and-change", cta=("Practise money problems", "practice.html?year=4&level=medium&topics=measures,decimal-add-sub"),
    nav="Money and change", cat=CAT, read=5,
    h1="Money problems and working out change",
    card="Pounds and pence as decimals, plus the shopkeeper's method for change.",
    years="Years 2\u20136",
    seo="Money problems explained \u2014 change, decimals and budgeting | Math It!",
    desc="How money works as a decimal, how to add and subtract amounts reliably, and the counting-on method for change that shopkeepers used before tills did it for them.",
    keywords="money problems, working out change, pounds and pence, money decimals, counting on change, KS2 money, year 4 money problems",
    intro="""<p>Money is the first decimal most children meet, and it is a forgiving one: there are
      always exactly two places, because a penny is a hundredth of a pound.</p>
      <p>That familiarity is useful and slightly dangerous. Children who only ever see decimals as
      money start believing every decimal has two digits, which causes trouble the first time they
      meet 2.5 metres. Worth mixing the contexts deliberately.</p>""",
    steps=[
        ("Pick one unit and stay in it",
         "<p>Either work entirely in pounds (\u00a33.45) or entirely in pence (345p). Mixing them "
         "inside one calculation is the main source of error.</p>"),
        ("Write amounts with two decimal places",
         "<p>\u00a33.50, not \u00a33.5. \u00a30.07, not \u00a3.07. The convention keeps columns "
         "aligned and makes slips visible.</p>"),
        ("Line up the decimal points to add or subtract",
         "<p>Exactly as for any decimal column work. Pad with zeros where one amount is "
         "shorter.</p>"),
        ("Find change by counting on, not subtracting",
         "<p>From the price, hop up to the next whole pound, then up to the amount handed over. "
         "Add the hops. This is how change was given by hand, and it avoids a row of "
         "exchanges.</p>"),
        ("Check the answer is sensible",
         "<p>Change from \u00a320 for something costing \u00a313.45 must be between \u00a36 and "
         "\u00a37. If you get \u00a37.55 or \u00a366.55, something slipped.</p>"),
    ],
    examples=[
        ("What change from \u00a320 for an item costing \u00a313.45?",
         ["Hop from \u00a313.45 to \u00a314.00: that is 55p.",
          "Hop from \u00a314 to \u00a320: that is \u00a36.",
          "Add the hops: \u00a36 + 55p."],
         "\u00a36.55"),
        ("Three notebooks cost \u00a31.85 each. What is the total?",
         ["1.85 \u00d7 3. Work it as 185 \u00d7 3 = 555.",
          "Two decimal places in the question, so two in the answer."],
         "\u00a35.55"),
        ("You have \u00a35. Pens cost 65p. How many can you buy?",
         ["Work in one unit: \u00a35 is 500p.",
          "500 \u00f7 65 = 7 remainder 45.",
          "You cannot buy part of a pen, so round down."],
         "7 pens, with 45p left"),
        ("A \u00a348 coat is reduced by 25%. What do you pay?",
         ["25% is a quarter, so the discount is 48 \u00f7 4 = \u00a312.",
          "48 \u2212 12 = 36. Or go straight to three quarters: 12 \u00d7 3."],
         "\u00a336"),
    ],
    mistakes=[
        ("Writing \u00a33.5 and reading it as three pounds five pence.",
         "It is three pounds fifty. Always write two decimal places for money: \u00a33.50."),
        ("Mixing units inside a calculation, e.g. \u00a32 + 50 = \u00a352.",
         "Convert first. \u00a32 + 50p is either 200p + 50p or \u00a32.00 + \u00a30.50."),
        ("Writing \u00a33.45p.",
         "Use the pound sign or the p, never both. It is either \u00a33.45 or 345p."),
        ("Giving the discount when the question asked for the price.",
         "Re-read it. \u2018Reduced by 25%\u2019 usually wants what you pay, which is the other 75%."),
    ],
    sections=[
        ("The shopkeeper's method",
         """<p>Before tills calculated change, assistants counted up out loud. For \u00a313.45 from
         \u00a320: \u201cthat's 13.45, 50, 14 pounds, 15, 16, 17, 18, 19, 20.\u201d They were adding
         5p, 50p, then six \u00a31 coins \u2014 and the coins they counted <em>were</em> the
         change.</p>
         <p>It is a genuinely better method than column subtraction for money, because it never
         requires exchanging across zeros, and because it produces the actual coins rather than
         just a number.</p>"""),
        ("Coins and notes children should recognise",
         """<p>UK coins: 1p, 2p, 5p, 10p, 20p, 50p, \u00a31, \u00a32. Notes: \u00a35, \u00a310,
         \u00a320, \u00a350.</p>
         <p>A classic Year 2 to 3 question asks for the fewest coins that make a given amount.
         The method is greedy \u2014 always take the largest coin that fits, then repeat. For 87p:
         50p, 20p, 10p, 5p, 2p, so six coins. Children who work up from 1p get the right total and
         the wrong answer.</p>"""),
        ("Where money questions get hard",
         """<p>The arithmetic is rarely the difficulty by Year 5. The difficulty is multi-step
         reasoning: \u201cbuy 3 of these and 2 of those, pay with \u00a320, how much change?\u201d
         Three operations, and a wrong order gives a plausible-looking wrong answer.</p>
         <p>The habit that helps most is writing one line per step with a unit on every number,
         rather than chaining it mentally. See
         <a href="word-problems.html" class="link">word problems</a> for the full approach.</p>"""),
    ],
    faqs=[
        ("Should children work in pounds or pence?",
         "Whichever keeps the numbers whole. Below a pound, pence is usually simpler; above it, pounds. The rule that matters is never to mix the two in one calculation."),
        ("How do I explain decimal money to a young child?",
         "A pound is split into 100 pennies, so the two digits after the point count pennies. \u00a33.45 is three whole pounds and 45 of the hundred parts of another."),
        ("What is the quickest way to find change?",
         "Count on from the price to the next whole pound, then on to the amount paid, and add the hops."),
        ("Do children need to know old or foreign currency?",
         "No. KS2 works in sterling. Currency conversion appears at secondary as a proportion topic."),
    ],
    related=["decimals-explained", "percentages-of-amounts", "word-problems", "column-subtraction"],
),

# ---------------------------------------------------------------- perimeter & area
dict(
    slug="perimeter-and-area", cat=CAT, nav="Perimeter and area", read=6,
    h1="Perimeter and area, and how to stop confusing them",
    card="Distance round versus space inside \u2014 with the formulas and compound shapes.",
    years="Years 3\u20136",
    seo="Perimeter and area explained \u2014 rectangles, triangles and compound shapes | Math It!",
    desc="The difference between perimeter and area, the formulas for rectangles, triangles and parallelograms, how to handle compound shapes, and why area uses squared units.",
    keywords="perimeter and area, area of a rectangle, area of a triangle, compound shapes, perimeter formula, KS2 area, year 6 perimeter",
    intro="""<p>Perimeter is the distance all the way round the outside of a shape. Area is the amount
      of flat space inside it. They are measured in different units and they answer different
      questions, yet they are confused constantly \u2014 largely because they are taught in the same
      week.</p>
      <p>The fix is a concrete pair of images: perimeter is the fence, area is the grass.</p>""",
    steps=[
        ("Perimeter: add every side",
         "<p>Walk round the shape and total the lengths. For a rectangle that is "
         "2 \u00d7 (length + width); for a regular shape it is one side \u00d7 the number of "
         "sides.</p>"),
        ("Area of a rectangle: length \u00d7 width",
         "<p>Because the shape is a grid: 8 rows of 5 squares is 40 squares.</p>"),
        ("Area of a triangle: base \u00d7 height \u00f7 2",
         "<p>Any triangle is exactly half of a rectangle drawn around it. The height must be the "
         "<em>perpendicular</em> height \u2014 straight up from the base \u2014 not a slanted "
         "side.</p>"),
        ("Area of a parallelogram: base \u00d7 perpendicular height",
         "<p>Slice the triangle off one end and slide it to the other and you have a rectangle. "
         "Again, not the sloping side.</p>"),
        ("Compound shapes: cut into rectangles",
         "<p>Split an L-shape into two rectangles, find each area, then add. Or box the whole thing "
         "in and subtract the missing piece \u2014 whichever gives easier numbers.</p>"),
        ("Use the right units",
         "<p>Perimeter is a length, so cm or m. Area is squares, so cm\u00b2 or m\u00b2. Marks are "
         "routinely lost for the unit alone.</p>"),
    ],
    examples=[
        ("A rectangle is 12 cm by 7 cm. Find its perimeter and area.",
         ["Perimeter: 12 + 7 + 12 + 7, or 2 \u00d7 (12 + 7) = 2 \u00d7 19.",
          "Area: 12 \u00d7 7."],
         "Perimeter 38 cm, area 84 cm\u00b2"),
        ("A triangle has base 10 cm and perpendicular height 6 cm. Find its area.",
         ["Area = base \u00d7 height \u00f7 2.",
          "10 \u00d7 6 = 60.",
          "60 \u00f7 2."],
         "30 cm\u00b2"),
        ("An L-shape: a 10 cm \u00d7 6 cm rectangle with a 4 cm \u00d7 3 cm corner removed. Area?",
         ["Box it in: the full rectangle is 10 \u00d7 6 = 60 cm\u00b2.",
          "The missing corner is 4 \u00d7 3 = 12 cm\u00b2.",
          "60 \u2212 12."],
         "48 cm\u00b2"),
        ("A square has an area of 49 cm\u00b2. What is its perimeter?",
         ["Area of a square = side\u00b2, so side = \u221a49 = 7 cm.",
          "Perimeter = 4 \u00d7 7."],
         "28 cm"),
    ],
    mistakes=[
        ("Using a sloping side as the height of a triangle.",
         "The height must be perpendicular to the base \u2014 straight up from it. On a diagram it is the dashed line, not the slanted edge."),
        ("Forgetting to halve when finding a triangle's area.",
         "A triangle is half its surrounding rectangle. If you forget, your answer is exactly double."),
        ("Giving an area in cm instead of cm\u00b2.",
         "Area counts squares. The unit is always squared, and omitting it loses the mark."),
        ("Assuming two shapes with the same perimeter have the same area.",
         "They rarely do. A 1 \u00d7 11 rectangle and a 6 \u00d7 6 square both have a perimeter of 24, but areas of 11 and 36."),
    ],
    sections=[
        ("Why area uses squared units",
         """<p>Area is measured by counting how many 1 cm squares fit inside. A rectangle 12 cm by
         7 cm fits 12 squares along each of 7 rows, which is 84 squares \u2014 84 cm\u00b2.</p>
         <p>That also explains a conversion that catches everybody: 1 m = 100 cm, but 1 m\u00b2 =
         <strong>10,000</strong> cm\u00b2, because a square metre is 100 cm by 100 cm.</p>"""),
        ("The same perimeter, very different areas",
         """<p>Give children 24 cm of string and ask for the biggest possible rectangle. They will
         usually try long thin ones first:</p>
         <ul>
           <li>1 \u00d7 11 \u2192 area 11 cm\u00b2</li>
           <li>3 \u00d7 9 \u2192 area 27 cm\u00b2</li>
           <li>5 \u00d7 7 \u2192 area 35 cm\u00b2</li>
           <li>6 \u00d7 6 \u2192 area 36 cm\u00b2</li>
         </ul>
         <p>The square always wins. It is a genuinely surprising result at age ten and it kills the
         \u201cperimeter and area are the same thing\u201d misconception for good.</p>"""),
        ("Missing-side problems",
         """<p>A standard Year 6 question gives the area and one side and asks for the other, or
         gives the perimeter and asks for a side. Both are inverse operations.</p>
         <p>Area 84 cm\u00b2 with one side 12 cm \u2192 the other side is 84 \u00f7 12 = 7 cm.
         Perimeter 38 cm with one side 12 cm \u2192 half the perimeter is 19 cm, so the other side
         is 19 \u2212 12 = 7 cm. Halving the perimeter first is the step children miss.</p>"""),
    ],
    faqs=[
        ("What is the difference between perimeter and area?",
         "Perimeter is the distance around the outside, measured in cm or m. Area is the space inside, measured in cm\u00b2 or m\u00b2. Fence versus grass."),
        ("What is the formula for the area of a triangle?",
         "Base \u00d7 perpendicular height \u00f7 2. The height must be measured at right angles to the base."),
        ("How do you find the area of an L-shape?",
         "Split it into two rectangles and add, or box it into one big rectangle and subtract the missing piece."),
        ("Why is 1 m\u00b2 not 100 cm\u00b2?",
         "Because a square metre is 100 cm along both sides, so it holds 100 \u00d7 100 = 10,000 square centimetres."),
    ],
    cta=("Practise area and perimeter", "practice.html?year=6&level=medium&topics=area-perimeter"),
    related=["volume-and-capacity", "2d-and-3d-shapes", "metric-units", "square-cube-numbers"],
),

# ---------------------------------------------------------------- volume
dict(
    slug="volume-and-capacity", cat=CAT, nav="Volume and capacity", read=5,
    h1="Volume and capacity",
    card="Counting cubes, the cuboid formula, and why 1 ml is exactly 1 cm\u00b3.",
    years="Years 5\u20136",
    seo="Volume and capacity explained \u2014 cuboids, cubes and litres | Math It!",
    desc="How to find the volume of a cuboid by counting cubes or using length times width times height, the difference between volume and capacity, and the millilitre to cubic centimetre link.",
    keywords="volume, capacity, volume of a cuboid, cubic centimetres, millilitres, volume formula, KS2 volume, year 6 volume",
    intro="""<p>Volume is how much three-dimensional space something takes up. Capacity is how much a
      container can hold. In practice the numbers are often the same, and at primary level the two
      words are used almost interchangeably \u2014 but the distinction is worth knowing: a brick has
      volume, a bucket has capacity.</p>
      <p>Volume is measured in cubic units, cm\u00b3 or m\u00b3. Capacity is usually measured in
      millilitres and litres. The two systems join at a neat point:
      <strong>1 ml = 1 cm\u00b3</strong> exactly.</p>""",
    steps=[
        ("Start by counting cubes",
         "<p>Before any formula, build or draw a cuboid from centimetre cubes and count them. "
         "A shape 4 long, 3 wide and 2 high holds 24 cubes, so its volume is 24 cm\u00b3.</p>"),
        ("Spot the layers",
         "<p>That same cuboid is two identical layers of 12. Seeing it as \u201carea of the base "
         "\u00d7 how many layers\u201d is what turns counting into a formula.</p>"),
        ("Use length \u00d7 width \u00d7 height",
         "<p>4 \u00d7 3 \u00d7 2 = 24 cm\u00b3. The order does not matter \u2014 multiplication is "
         "commutative \u2014 so start with whichever pair is easiest.</p>"),
        ("Keep every measurement in the same unit",
         "<p>You cannot multiply 30 cm by 2 m. Convert first: 30 cm \u00d7 200 cm, or "
         "0.3 m \u00d7 2 m.</p>"),
        ("Convert between cm\u00b3, ml and litres",
         "<p>1 cm\u00b3 = 1 ml, and 1,000 ml = 1 litre, so 1,000 cm\u00b3 = 1 litre. A litre bottle "
         "is a 10 cm cube.</p>"),
    ],
    examples=[
        ("Find the volume of a cuboid 8 cm \u00d7 5 cm \u00d7 3 cm.",
         ["Area of the base: 8 \u00d7 5 = 40 cm\u00b2.",
          "Three layers of 40.",
          "40 \u00d7 3."],
         "120 cm\u00b3"),
        ("A cube has edges of 6 cm. What is its volume?",
         ["All edges equal, so volume = 6\u00b3.",
          "6 \u00d7 6 = 36, then 36 \u00d7 6."],
         "216 cm\u00b3"),
        ("A fish tank measures 40 cm \u00d7 25 cm \u00d7 30 cm. How many litres does it hold?",
         ["Volume: 40 \u00d7 25 = 1,000, then \u00d7 30 = 30,000 cm\u00b3.",
          "1 cm\u00b3 = 1 ml, so that is 30,000 ml.",
          "\u00f7 1,000 to convert to litres."],
         "30 litres"),
        ("A cuboid has a volume of 60 cm\u00b3 and a base 5 cm \u00d7 4 cm. How tall is it?",
         ["Base area: 5 \u00d7 4 = 20 cm\u00b2.",
          "Height = volume \u00f7 base area.",
          "60 \u00f7 20."],
         "3 cm"),
    ],
    mistakes=[
        ("Multiplying lengths given in different units.",
         "Convert everything to one unit before multiplying. 30 cm \u00d7 2 m must become 30 cm \u00d7 200 cm."),
        ("Writing the answer in cm\u00b2.",
         "Volume multiplies three lengths, so the unit is cubed. Area is squared; volume is cubed."),
        ("Thinking 1 m\u00b3 is 100 cm\u00b3.",
         "It is 100 \u00d7 100 \u00d7 100 = 1,000,000 cm\u00b3. Cube the conversion factor, do not just copy it."),
        ("Adding the three dimensions instead of multiplying them.",
         "8 + 5 + 3 = 16 is not a volume. Volume is always a product."),
    ],
    sections=[
        ("Why 1 ml equals 1 cm\u00b3",
         """<p>It is a definition, not a coincidence. The litre was defined as the volume of a cube
         10 cm on each side \u2014 that is 10 \u00d7 10 \u00d7 10 = 1,000 cm\u00b3. Divide by a
         thousand and one millilitre is exactly one cubic centimetre.</p>
         <p>This makes a useful classroom demonstration: a litre jug of water poured into a 10 cm
         cube fills it exactly. Children remember the fact far better having seen it.</p>"""),
        ("Volume of compound solids",
         """<p>Year 6 extension work asks for the volume of shapes made from two cuboids stuck
         together. The approach is the same as compound area: split into cuboids, find each volume,
         add them. Or box the whole thing in and subtract the gap.</p>
         <p>The commonest error is double-counting the overlap, so label each piece's dimensions on
         the diagram before calculating anything.</p>"""),
        ("Displacement",
         """<p>An irregular object has a volume too, and you measure it by displacement: put it in
         a measuring cylinder of water and see how far the level rises. A rise of 35 ml means the
         object's volume is 35 cm\u00b3.</p>
         <p>This is the practical reason the ml-to-cm\u00b3 link matters, and it is a genuinely
         satisfying experiment for a child who has only ever multiplied three numbers together.</p>"""),
    ],
    faqs=[
        ("What is the formula for the volume of a cuboid?",
         "Length \u00d7 width \u00d7 height. Equivalently, the area of the base multiplied by the height."),
        ("What is the difference between volume and capacity?",
         "Volume is the space a solid occupies; capacity is how much a container can hold. A brick has volume, a jug has capacity."),
        ("How many cm\u00b3 are in a litre?",
         "1,000, because 1 ml is exactly 1 cm\u00b3 and there are 1,000 ml in a litre."),
        ("When is volume taught?",
         "Year 5 estimates volume by counting cubes; Year 6 calculates the volume of cuboids using a formula and converts between cubic units."),
    ],
    cta=("Practise volume and measures", "practice.html?year=6&level=hard&topics=measures,area-perimeter"),
    related=["perimeter-and-area", "metric-units", "2d-and-3d-shapes", "square-cube-numbers"],
),

]
