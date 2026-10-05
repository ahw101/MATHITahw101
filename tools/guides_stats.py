# -*- coding: utf-8 -*-
"""Guides: Statistics."""

CAT = "Statistics"

GUIDES = [

# ---------------------------------------------------------------- mean
dict(
    slug="averages-and-the-mean", cat=CAT, nav="Averages and the mean", read=5,
    h1="Averages and the mean",
    card="Add them up, divide by how many \u2014 plus the reverse questions that catch people out.",
    years="Years 5\u20136",
    seo="The mean explained \u2014 how to find an average | Math It!",
    desc="How to calculate the mean, work backwards from an average to a missing value, and understand when the mean is a misleading summary.",
    keywords="mean, average, how to find the mean, missing value average, KS2 statistics, year 6 mean, median mode range",
    intro="""<p>In the English primary curriculum, \u201caverage\u201d means the <strong>mean</strong>:
      add all the values and divide by how many there are. It is introduced in Year 6 and is the
      only average formally assessed at KS2.</p>
      <p>Finding a mean is easy. The questions that go wrong are the ones that run the process
      backwards \u2014 and those are exactly the ones SATs likes to ask.</p>""",
    steps=[
        ("Add every value",
         "<p>Include zeros. A zero is data; leaving it out changes the count and so changes the "
         "answer.</p>"),
        ("Count how many values there are",
         "<p>Count the items, not the categories. Five test scores means dividing by 5.</p>"),
        ("Divide the total by the count",
         "<p>mean = total \u00f7 number of values. That is the whole formula.</p>"),
        ("Sense-check against the range",
         "<p>The mean must lie between the smallest and largest value. If it does not, something "
         "has gone wrong in the addition or the division.</p>"),
        ("To work backwards, rebuild the total",
         "<p>total = mean \u00d7 number of values. Then subtract the values you know to find the "
         "missing one.</p>"),
    ],
    examples=[
        ("Find the mean of 4, 7, 9, 12 and 13.",
         ["Total: 4 + 7 + 9 + 12 + 13 = 45.",
          "Count: 5 values.",
          "45 \u00f7 5."],
         "9"),
        ("Four children have a mean height of 142 cm. Three of them are 138 cm, 145 cm and 140 cm. How tall is the fourth?",
         ["Total height: 142 \u00d7 4 = 568 cm.",
          "Known heights: 138 + 145 + 140 = 423 cm.",
          "568 \u2212 423."],
         "145 cm"),
        ("Jas scored 6, 8, 0 and 10. Find the mean.",
         ["The zero still counts as a score.",
          "Total: 6 + 8 + 0 + 10 = 24.",
          "24 \u00f7 4."],
         "6"),
        ("A team's mean score over 5 games is 3. After a 6th game the mean is 4. What did they score in game 6?",
         ["Total after 5 games: 3 \u00d7 5 = 15.",
          "Total after 6 games: 4 \u00d7 6 = 24.",
          "24 \u2212 15."],
         "9"),
    ],
    mistakes=[
        ("Dividing by the wrong number.",
         "Divide by how many values there are, not by the number of different values or the largest one."),
        ("Leaving zeros out of the count.",
         "A score of 0 is still a score. Drop it and you divide by one fewer, inflating the mean."),
        ("Forgetting the units.",
         "A mean height is in centimetres, a mean time in minutes. The average of a set of measurements carries the same unit."),
        ("Averaging the averages.",
         "The mean of two class means is only the overall mean if both classes are the same size. Otherwise rebuild the totals first."),
    ],
    sections=[
        ("Working backwards is the real skill",
         """<p>Almost every mark-heavy average question at KS2 is a reverse one. The move is always
         the same: turn the mean back into a total.</p>
         <p>If six numbers have a mean of 12, their total is 72 \u2014 no matter what the individual
         numbers are. From there it is ordinary subtraction. Children who learn
         <strong>total = mean \u00d7 count</strong> as a fact, rather than rearranging the formula
         each time, are much quicker.</p>"""),
        ("Mean, median, mode and range",
         """<p>Only the mean is required at KS2, but the others appear in Year 6 enrichment and at
         secondary:</p>
         <ul>
           <li><strong>Mean</strong> \u2014 total \u00f7 count.</li>
           <li><strong>Median</strong> \u2014 the middle value once sorted. With an even count,
           the mean of the middle two.</li>
           <li><strong>Mode</strong> \u2014 the most common value. There can be more than one, or
           none.</li>
           <li><strong>Range</strong> \u2014 largest \u2212 smallest. A measure of spread, not an
           average at all.</li>
         </ul>
         <p>For 2, 3, 3, 8: mean 4, median 3, mode 3, range 6.</p>"""),
        ("When the mean misleads",
         """<p>One extreme value drags the mean a long way. Five salaries of \u00a320k and one of
         \u00a3500k give a mean of \u00a3100k, which describes nobody in the room.</p>
         <p>This is worth a conversation with older children: the median \u2014 \u00a320k here \u2014
         is often the fairer summary, which is why house prices and incomes are usually reported as
         medians in the news. Noticing that a statistic can be true and misleading at the same time
         is a genuinely useful habit.</p>"""),
    ],
    faqs=[
        ("How do you find the mean?",
         "Add all the values together, then divide by how many values there are."),
        ("What does average mean at KS2?",
         "In the English primary curriculum, average means the mean. Median and mode are not formally assessed at KS2."),
        ("How do I find a missing value from an average?",
         "Multiply the mean by the number of values to get the total, then subtract the values you already know."),
        ("Can the mean be a decimal when all the data are whole numbers?",
         "Yes, and often it is. The mean of 3 and 4 is 3.5 \u2014 it does not have to be a value from the set."),
    ],
    cta=("Practise mixed reasoning questions", "practice.html?year=6&level=medium&topics=measures,decimal-add-sub"),
    related=["charts-and-tables", "short-division", "decimals-explained", "percentages-of-amounts"],
),

# ---------------------------------------------------------------- charts
dict(
    slug="charts-and-tables", cat=CAT, nav="Charts and tables", read=6,
    h1="Reading charts, tables and graphs",
    card="Bar charts, pictograms, line graphs, pie charts and timetables \u2014 and the traps in each.",
    years="Years 2\u20136",
    seo="Reading charts and tables \u2014 bar charts, line graphs, pie charts | Math It!",
    desc="How to read bar charts, pictograms, line graphs, pie charts and two-way tables accurately, including scales that do not go up in ones and the two-step questions that follow.",
    keywords="bar chart, pictogram, line graph, pie chart, two-way table, timetable, reading scales, KS2 statistics, year 6 data",
    intro="""<p>Data questions are rarely hard arithmetic. They are reading comprehension with
      numbers, and marks are lost to carelessness rather than to the maths: a scale going up in
      fives, a half symbol on a pictogram, a question that asks for a difference rather than a
      value.</p>
      <p>A fixed routine \u2014 title, axes, scale, then the question \u2014 removes most of those
      losses.</p>""",
    steps=[
        ("Read the title first",
         "<p>It tells you what is being counted. \u201cFavourite fruit in Class 4\u201d and "
         "\u201cFruit sold at the shop\u201d need different answers to the same-looking "
         "chart.</p>"),
        ("Read both axis labels",
         "<p>One axis names the categories, the other gives the quantity. Note the unit \u2014 "
         "people, pounds, millimetres of rain.</p>"),
        ("Work out the scale",
         "<p>Count the gridlines between two labelled numbers and divide. Four gaps between 0 and "
         "20 means each gridline is 5. This is the number-one source of error.</p>"),
        ("Answer exactly what is asked",
         "<p>\u201cHow many more\u201d needs a subtraction. \u201cHow many altogether\u201d needs "
         "an addition. Reading off a single bar answers neither.</p>"),
        ("Check the answer is plausible",
         "<p>A difference cannot exceed the tallest bar. A total must be bigger than any one "
         "part.</p>"),
    ],
    examples=[
        ("A bar chart's y-axis is labelled 0, 10, 20, 30 with four gridlines between each label. A bar sits two lines above 20. What does it show?",
         ["Four gaps between 0 and 10 means each gridline is 10 \u00f7 4 \u2026 no \u2014 count the gaps, not the lines: 10 \u00f7 5 = 2 per gap.",
          "Two gaps above 20 is 20 + 4."],
         "24"),
        ("A pictogram key says one apple symbol = 4 apples. One row shows three whole symbols and a half. How many apples?",
         ["Three whole symbols: 3 \u00d7 4 = 12.",
          "Half a symbol: 4 \u00f7 2 = 2.",
          "12 + 2."],
         "14 apples"),
        ("A pie chart of 60 people shows a quarter choosing football. How many is that?",
         ["A quarter of the circle is a quarter of the total.",
          "60 \u00f7 4."],
         "15 people"),
        ("A train leaves at 09:48 and arrives at 11:05. How long is the journey?",
         ["09:48 to 10:00 is 12 minutes.",
          "10:00 to 11:00 is 60 minutes.",
          "11:00 to 11:05 is 5 minutes.",
          "12 + 60 + 5 = 77 minutes."],
         "1 hour 17 minutes"),
    ],
    mistakes=[
        ("Assuming every gridline is one unit.",
         "Always derive the scale from two labelled values before reading anything off."),
        ("Ignoring half symbols on a pictogram.",
         "A half symbol is half the key value. If the key is 10, a half symbol is 5 \u2014 not 1."),
        ("Answering \u2018how many more\u2019 with a single reading.",
         "Comparison words need two readings and a subtraction. Underline the question word before you start."),
        ("Treating a pie chart as if it showed counts.",
         "A pie chart shows proportions. Without the total you cannot convert a slice into a number of items."),
    ],
    sections=[
        ("Which chart for which job",
         """<table>
           <thead><tr><th>Chart</th><th>Shows</th><th>Typical year</th></tr></thead>
           <tbody>
             <tr><td>Pictogram</td><td>Counts, using a symbol key</td><td>Years 2\u20133</td></tr>
             <tr><td>Bar chart</td><td>Comparing separate categories</td><td>Years 3\u20136</td></tr>
             <tr><td>Line graph</td><td>Change over time</td><td>Years 4\u20136</td></tr>
             <tr><td>Pie chart</td><td>Parts of a whole</td><td>Year 6</td></tr>
             <tr><td>Two-way table</td><td>Two variables at once</td><td>Years 5\u20136</td></tr>
           </tbody>
         </table>
         <p>Bar charts have gaps between the bars because the categories are separate. Line graphs
         join their points because the values in between are meaningful \u2014 which is why a line
         graph of favourite colours makes no sense.</p>"""),
        ("Timetables are tables with a trap",
         """<p>Timetables use the 24-hour clock, read down each column for one journey and across
         each row for one stop. The trap is duration: 09:48 to 11:05 is not 11.05 \u2212 9.48.</p>
         <p>Bridge through the hour instead \u2014 up to 10:00, then whole hours, then the
         remainder. Our <a href="telling-the-time.html">telling the time guide</a> works
         through several of these.</p>"""),
        ("Two-step data questions",
         """<p>Most Year 6 data marks come from questions that need two operations. \u201cHow many
         more children chose football than tennis, and what fraction of the class is that?\u201d is
         a subtraction followed by a fraction.</p>
         <p>Teach children to annotate the chart \u2014 writing each value next to its bar before
         doing any arithmetic. It costs ten seconds and prevents the misread that would otherwise
         sink both marks.</p>"""),
    ],
    faqs=[
        ("How do I work out the scale on a bar chart?",
         "Find two labelled values, count the gaps between them, and divide the difference by the number of gaps."),
        ("What does half a symbol mean on a pictogram?",
         "Half the value of the key. If one symbol stands for 10, half a symbol stands for 5."),
        ("When is the difference between a bar chart and a line graph taught?",
         "Bar charts from Year 3; line graphs for continuous data from Year 4, with time graphs interpreted in Years 5 and 6."),
        ("Do I need the total to read a pie chart?",
         "To convert a slice into a count, yes. Without it, a pie chart only tells you proportions."),
    ],
    cta=("Practise mixed reasoning questions", "practice.html?year=5&level=medium&topics=measures,frac-of-amount"),
    related=["averages-and-the-mean", "telling-the-time", "fractions-of-amounts", "percentages-of-amounts"],
),

]
