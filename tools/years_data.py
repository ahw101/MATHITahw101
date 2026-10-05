# -*- coding: utf-8 -*-
"""Per-year content for years/year-<n>.html.

Objectives are summarised from the England national curriculum programmes of
study for mathematics (key stages 1 and 2), DfE, 2013 -- the statutory document
still in force. They are paraphrased for parents rather than quoted, and
grouped the way the curriculum groups them.

Schema
    n          school year
    ks         key stage label
    ages       typical ages
    nav / card / seo / desc / keywords
    intro      HTML
    new        [(heading, html)]   what changes from the year before
    strands    [(strand, [bullet, ...])]
    sticking   [(problem, fix)]
    settings   [(label, href, why)]
    tables     html, the times tables expectation for the year
    guides     [slug, ...]
    closing    html
    faqs       [(q, a)]
"""

YEARS = {}


def _y(**kw):
    YEARS[kw["n"]] = kw


# ------------------------------------------------------------------ Year 2
_y(
    n=2, ks="Key Stage 1", ages="ages 6\u20137", nav="Year 2 maths",
    card="Numbers to 100, the 2, 5 and 10 times tables, and the first fractions.",
    seo="Year 2 maths \u2014 what children learn, and how to practise it | Math It!",
    desc="What Year 2 maths covers in England: place value to 100, addition and subtraction facts to 20, the 2, 5 and 10 times tables, halves and quarters, measurement and the end-of-KS1 expectations.",
    keywords="year 2 maths, KS1 maths, year 2 curriculum, year 2 times tables, SATs year 2, key stage 1 maths, year 2 maths worksheets",
    intro="""<p>Year 2 is the end of Key Stage 1, and the year arithmetic starts to feel like a
      subject rather than counting. Children move from working with numbers to 20 to working
      confidently to 100, meet their first three times tables, and begin to see fractions as
      numbers rather than just shapes cut in half.</p>
      <p>The single biggest expectation is fluency in addition and subtraction facts to 20. Almost
      everything in Years 3 and 4 assumes those are automatic, so if only one thing gets practised
      this year, make it that.</p>""",
    new=[
        ("Two-digit place value",
         """<p>Year 1 counts to 100. Year 2 understands it \u2014 that 47 is four tens and seven
         ones, and that this is why 47 is bigger than 38. Partitioning numbers into tens and ones
         is the gateway to column methods later.</p>"""),
        ("The first times tables",
         """<p>The 2, 5 and 10 times tables, in both directions. Not just \u201ccount in
         fives\u201d but \u201c5 \u00d7 7 = 35\u201d asked out of order, and \u201c35 \u00f7 5 =
         7\u201d asked straight afterwards.</p>"""),
        ("Fractions as quantities",
         """<p>A half, a third and a quarter of a shape \u2014 but also of a set of objects and of
         a number. Finding a quarter of 12 counters is the first time a fraction behaves like an
         operation.</p>"""),
    ],
    strands=[
        ("Number and place value", [
            "Count in steps of 2, 3 and 5 from zero, and in tens from any number.",
            "Recognise the place value of each digit in a two-digit number.",
            "Compare and order numbers to 100 using &lt;, &gt; and =.",
            "Read and write numbers to at least 100 in numerals and in words.",
        ]),
        ("Addition and subtraction", [
            "Recall and use addition and subtraction facts to 20 fluently.",
            "Derive related facts up to 100 \u2014 if 7 + 3 = 10 then 70 + 30 = 100.",
            "Add and subtract a two-digit number and ones, and a two-digit number and tens.",
            "Add two two-digit numbers, and add three one-digit numbers.",
            "Understand that addition can be done in any order but subtraction cannot.",
        ]),
        ("Multiplication and division", [
            "Recall and use the 2, 5 and 10 multiplication tables, including division facts.",
            "Recognise odd and even numbers.",
            "Use the &times;, &divide; and = signs to write and solve problems.",
            "Know that multiplication can be done in any order but division cannot.",
        ]),
        ("Fractions", [
            "Find and write 1/3, 1/4, 2/4 and 3/4 of a length, shape, set of objects or quantity.",
            "Recognise that 2/4 and 1/2 are the same amount.",
        ]),
        ("Measurement", [
            "Use standard units: m and cm, kg and g, \u00b0C, ml and l.",
            "Recognise and use \u00a3 and p, combine amounts and give change.",
            "Tell the time to five minutes, including quarter past and quarter to.",
        ]),
        ("Shape and statistics", [
            "Name 2D and 3D shapes and describe their properties, including lines of symmetry.",
            "Interpret and construct tally charts, pictograms and simple tables.",
        ]),
    ],
    sticking=[
        ("Counting on to add instead of recalling",
         "A child who works out 8 + 6 by counting on their fingers has not learnt the fact. Practise bonds to 10 and 20 as recall, out of order, in short daily bursts."),
        ("Chanting a table instead of knowing it",
         "\u201cFive, ten, fifteen, twenty\u2026\u201d is counting, not the 5 times table. Ask 5 \u00d7 7 cold, with no run-up."),
        ("Reading 47 as \u2018four and seven\u2019",
         "Partition out loud: forty and seven. Tens and ones language fixes most two-digit place-value confusion."),
        ("Subtraction only ever read as \u2018take away\u2019",
         "14 \u2212 9 is quicker as \u201chow far from 9 to 14\u201d. Both readings are needed, and counting on is the one that scales."),
    ],
    settings=[
        ("Year 2, easy", "practice.html?year=2&amp;level=easy", "Addition and subtraction within 20, with number bonds. The right starting point for most of the autumn term."),
        ("Year 2, medium", "practice.html?year=2&amp;level=medium", "Two-digit addition and subtraction plus the 2, 5 and 10 tables."),
        ("2, 5 and 10 times tables", "tables.html?tables=2,5,10&amp;ops=mul", "The three tables expected by the end of Year 2, mixed and out of order."),
        ("Division facts", "tables.html?tables=2,5,10&amp;ops=div", "The same three tables the other way round \u2014 the part most children skip."),
    ],
    tables="""<p>By the end of Year 2 a child is expected to recall the <strong>2, 5 and 10 times
      tables</strong>, including the matching division facts, and to recognise odd and even
      numbers.</p>
      <p>\u201cRecall\u201d is the operative word. The expectation is answering out of order, not
      reciting the list.</p>""",
    guides=["number-bonds", "place-value", "times-tables", "fractions-explained",
            "telling-the-time", "money-and-change"],
    closing="""<p>There is no longer a statutory Key Stage 1 SATs test \u2014 it became optional
      from 2023\u201324 \u2014 but most schools still assess at the end of Year 2 and report a
      teacher judgement. The content expected has not changed.</p>
      <p>If you are supporting a Year 2 child at home, ten minutes a day on number facts is worth
      more than an hour at the weekend. Short, frequent and out of order is the formula.</p>""",
    faqs=[
        ("What maths should a Year 2 child know?",
         "Place value to 100, addition and subtraction facts to 20 by recall, the 2, 5 and 10 times tables with their division facts, halves, thirds and quarters, standard units of measure, telling the time to five minutes, and money."),
        ("Which times tables are expected in Year 2?",
         "The 2, 5 and 10 times tables, including the related division facts."),
        ("Are there SATs in Year 2?",
         "Key Stage 1 SATs became non-statutory from the 2023\u201324 school year. Many schools still use the optional papers to inform their teacher assessment."),
        ("How much maths practice is right at this age?",
         "Ten minutes a day, focused on recall of number facts, beats longer and less frequent sessions. Keep it short enough that it stays enjoyable."),
    ],
)

# ------------------------------------------------------------------ Year 3
_y(
    n=3, ks="Lower Key Stage 2", ages="ages 7\u20138", nav="Year 3 maths",
    card="Column methods arrive, along with the 3, 4 and 8 times tables and tenths.",
    seo="Year 3 maths \u2014 what children learn, and how to practise it | Math It!",
    desc="What Year 3 maths covers in England: three-digit place value, formal column addition and subtraction, the 3, 4 and 8 times tables, tenths, perimeter and telling the time.",
    keywords="year 3 maths, lower KS2, year 3 curriculum, year 3 times tables, column addition year 3, year 3 maths worksheets",
    intro="""<p>Year 3 is the first year of Key Stage 2 and the step up is real. Numbers go to
      1000, three new times tables arrive, and \u2014 most significantly \u2014 formal written
      column methods are introduced for the first time.</p>
      <p>It is also the year fractions stop being about pizza. Tenths appear, fractions get added
      and subtracted, and children have to start treating them as numbers on a line.</p>""",
    new=[
        ("Formal written methods",
         """<p>Column addition and subtraction with up to three digits, set out properly with the
         columns lined up. This is a notation change as much as a mathematical one, and neat
         layout genuinely matters \u2014 most errors at this stage are misaligned digits rather
         than wrong arithmetic.</p>"""),
        ("Three new times tables at once",
         """<p>The 3, 4 and 8 tables. They are grouped deliberately: 4 is double 2, 8 is double 4,
         so two of the three come from doubling. The 3s are the only genuinely new memory
         load.</p>"""),
        ("Tenths",
         """<p>Counting up and down in tenths, and recognising that tenths come from dividing an
         object into ten equal parts. This is the foundation of decimals in Year 4.</p>"""),
    ],
    strands=[
        ("Number and place value", [
            "Count in multiples of 4, 8, 50 and 100.",
            "Recognise the place value of each digit in a three-digit number.",
            "Compare and order numbers up to 1000; read and write them in numerals and words.",
            "Find 10 or 100 more or less than a given number.",
        ]),
        ("Addition and subtraction", [
            "Add and subtract mentally: three-digit numbers with ones, tens or hundreds.",
            "Add and subtract numbers with up to three digits using formal column methods.",
            "Estimate the answer and use the inverse operation to check it.",
        ]),
        ("Multiplication and division", [
            "Recall and use the 3, 4 and 8 multiplication tables.",
            "Multiply two-digit numbers by a one-digit number using mental and progressing to written methods.",
            "Solve scaling and correspondence problems \u2014 \u2018four times as tall\u2019.",
        ]),
        ("Fractions", [
            "Count up and down in tenths; recognise tenths as dividing by 10.",
            "Find fractions of a discrete set of objects with small denominators.",
            "Recognise and show equivalent fractions with small denominators.",
            "Add and subtract fractions with the same denominator within one whole.",
            "Compare and order unit fractions, and fractions with the same denominator.",
        ]),
        ("Measurement", [
            "Measure, compare, add and subtract lengths (m/cm/mm), mass (kg/g) and volume (l/ml).",
            "Measure the perimeter of simple 2D shapes.",
            "Add and subtract amounts of money, giving change.",
            "Tell the time from an analogue clock, including Roman numerals I to XII, and on 12- and 24-hour digital clocks.",
        ]),
        ("Shape and statistics", [
            "Identify right angles, and horizontal, vertical, perpendicular and parallel lines.",
            "Interpret and present data using bar charts, pictograms and tables.",
        ]),
    ],
    sticking=[
        ("Column methods with misaligned digits",
         "Squared paper, one digit per square. It removes most Year 3 column errors overnight."),
        ("Exchanging in subtraction",
         "\u2018Borrowing\u2019 is worth replacing with \u2018exchanging\u2019 and showing physically with base ten blocks or coins once. The notation makes far more sense afterwards."),
        ("The 3 times table",
         "The only one of the three with no doubling route. Teach the digit-sum test alongside it so there is a way to self-check."),
        ("Fractions treated as two separate numbers",
         "3/4 is one number, not a 3 and a 4. Put it on a number line between 0 and 1 and the idea lands."),
    ],
    settings=[
        ("Year 3, easy", "practice.html?year=3&amp;level=easy", "Mental addition and subtraction with the new tables mixed in."),
        ("Year 3, medium", "practice.html?year=3&amp;level=medium", "Three-digit column work plus tables and fraction basics."),
        ("3, 4 and 8 times tables", "tables.html?tables=3,4,8&amp;ops=mul", "Exactly the three tables expected this year."),
        ("Column practice", "practice.html?year=3&amp;level=medium&amp;topics=mental-add,mental-sub,place-value", "Addition, subtraction and place value only \u2014 useful when column methods are being taught."),
    ],
    tables="""<p>Year 3 adds the <strong>3, 4 and 8 times tables</strong> to the 2s, 5s and 10s
      from Year 2. That makes six tables by the end of the year.</p>
      <p>Teach 4 as double 2 and 8 as double 4, and the real work reduces to the 3 times
      table.</p>""",
    guides=["column-addition", "column-subtraction", "times-tables", "fractions-explained",
            "perimeter-and-area", "telling-the-time", "roman-numerals"],
    closing="""<p>Year 3 is where children who have not secured their number bonds start to
      struggle, because column methods expose any gap immediately. If written subtraction is
      going badly, check the bonds to 20 first \u2014 the problem is usually there rather than in
      the method.</p>
      <p>It is also the year to get times tables practice into a routine, because Year 4 ends with
      a national check and the gap between six tables and twelve is a lot to make up in one
      year.</p>""",
    faqs=[
        ("Which times tables are expected in Year 3?",
         "The 3, 4 and 8 times tables, on top of the 2, 5 and 10 tables from Year 2."),
        ("When do children learn column addition?",
         "Year 3 in England, for numbers with up to three digits. Year 4 extends it to four digits."),
        ("What is new in Year 3 maths compared with Year 2?",
         "Numbers to 1000, formal column addition and subtraction, three new times tables, tenths, perimeter, and telling the time to the minute."),
        ("Is Year 3 a big jump?",
         "Yes \u2014 it is the first year of Key Stage 2 and introduces formal written methods. Children who are fluent with number facts to 20 cope with it much more easily."),
    ],
)

# ------------------------------------------------------------------ Year 4
_y(
    n=4, ks="Lower Key Stage 2", ages="ages 8\u20139", nav="Year 4 maths",
    card="All tables to 12 \u00d7 12, the national check, decimals and negative numbers.",
    seo="Year 4 maths \u2014 the Multiplication Tables Check and the full curriculum | Math It!",
    desc="What Year 4 maths covers in England: all times tables to 12 \u00d7 12 and the national Multiplication Tables Check, four-digit place value, decimals to two places, rounding, area and coordinates.",
    keywords="year 4 maths, multiplication tables check, MTC, year 4 times tables, year 4 curriculum, times table test year 4, year 4 maths worksheets",
    intro="""<p>Year 4 is the times tables year. The national curriculum expects every table to
      12 \u00d7 12 by the end of it, and in June all Year 4 children in England sit the statutory
      <strong>Multiplication Tables Check</strong> \u2014 25 questions, six seconds each, on
      screen.</p>
      <p>Everything else in Year 4 is substantial too: four-digit numbers, decimals to two places,
      negative numbers, rounding, area and coordinates. But the tables are the thing that makes
      all of it easier or harder.</p>""",
    new=[
        ("The Multiplication Tables Check",
         """<p>Statutory since 2022, taken in a three-week window in June. Twenty-five randomly
         selected multiplication questions from the 2 to 12 tables, six seconds to answer each,
         with a three-second gap between. There is no pass mark published for parents and no
         consequence for the child \u2014 it is a school accountability measure.</p>
         <p>Practically, six seconds means recall. There is no time to work anything out.</p>"""),
        ("Decimals",
         """<p>Tenths and hundredths as decimals, decimal equivalents of 1/4, 1/2 and 3/4, rounding
         decimals with one decimal place to the nearest whole number, and comparing numbers with
         up to two decimal places.</p>"""),
        ("Negative numbers",
         """<p>Counting backwards through zero, usually introduced through temperature. Year 4
         meets them; Year 6 calculates intervals across zero.</p>"""),
        ("Area",
         """<p>Introduced by counting squares, before the formula arrives in Year 5. Perimeter
         extends to rectilinear \u2014 L-shaped \u2014 figures.</p>"""),
    ],
    strands=[
        ("Number and place value", [
            "Count in multiples of 6, 7, 9, 25 and 1000.",
            "Recognise the place value of each digit in a four-digit number.",
            "Round any number to the nearest 10, 100 or 1000.",
            "Count backwards through zero to include negative numbers.",
            "Read Roman numerals to 100 (I to C).",
        ]),
        ("Addition and subtraction", [
            "Add and subtract numbers with up to four digits using formal column methods.",
            "Estimate and use inverse operations to check answers.",
            "Solve two-step problems in context, deciding which operations to use and why.",
        ]),
        ("Multiplication and division", [
            "Recall multiplication and division facts for all tables up to 12 &times; 12.",
            "Use place value and known facts to multiply mentally, including by 0 and 1.",
            "Recognise and use factor pairs and commutativity.",
            "Multiply two-digit and three-digit numbers by a one-digit number using a formal written layout.",
        ]),
        ("Fractions and decimals", [
            "Count up and down in hundredths.",
            "Add and subtract fractions with the same denominator.",
            "Recognise and write decimal equivalents of tenths and hundredths, and of 1/4, 1/2, 3/4.",
            "Round decimals with one decimal place to the nearest whole number.",
            "Compare numbers with the same number of decimal places up to two places.",
        ]),
        ("Measurement", [
            "Convert between units: kilometres to metres, hours to minutes.",
            "Measure and calculate the perimeter of rectilinear figures in cm and m.",
            "Find the area of rectilinear shapes by counting squares.",
            "Read, write and convert time between analogue and digital 12- and 24-hour clocks.",
        ]),
        ("Geometry and statistics", [
            "Compare and classify shapes, including quadrilaterals and triangles.",
            "Identify acute and obtuse angles and order angles up to two right angles.",
            "Identify lines of symmetry in 2D shapes presented in different orientations.",
            "Describe positions on a 2D grid as coordinates in the first quadrant, and describe translations.",
            "Interpret and present discrete and continuous data using bar charts and time graphs.",
        ]),
    ],
    sticking=[
        ("Tables that are known but slow",
         "Six seconds is the MTC limit, and \u2018known but slow\u2019 fails it. Practise against a timer so speed becomes the target, not just accuracy."),
        ("6 \u00d7 7, 6 \u00d7 8, 7 \u00d7 8 and 8 \u00d7 9",
         "The four slowest facts nationally, year after year. Pull them out and drill them separately rather than running the whole grid."),
        ("Decimals read as two numbers",
         "3.45 is not \u2018three point forty-five\u2019. Say \u2018three point four five\u2019, and keep the place-value columns visible."),
        ("Negative numbers treated as ordinary numbers",
         "\u22125 is smaller than \u22122, which feels wrong. A vertical number line, or a thermometer, makes the order concrete."),
    ],
    settings=[
        ("All tables, 2 to 12", "tables.html?tables=2,3,4,5,6,7,8,9,10,11,12&amp;ops=mul", "The whole grid, in random order \u2014 the closest match to the MTC."),
        ("The tricky tables", "tables.html?tables=6,7,8,9,12&amp;ops=mul", "The five tables that account for nearly all lost time in the check."),
        ("Year 4, medium", "practice.html?year=4&amp;level=medium", "Mixed arithmetic at the expected standard for the year."),
        ("Mixed &times; and &divide;", "tables.html?tables=2,3,4,5,6,7,8,9,10,11,12&amp;ops=both", "Both directions, because division facts are assessed in school even though the MTC only tests multiplication."),
    ],
    tables="""<p>Year 4 expects <strong>all multiplication and division facts up to
      12 \u00d7 12</strong>. This is the year the grid is completed, and it is checked nationally
      in June by the Multiplication Tables Check.</p>
      <p>The MTC tests multiplication only, and leaves out the 1 and 10 tables, weighting towards
      6, 7, 8, 9 and 12. School assessment still covers division facts.</p>""",
    guides=["times-tables", "mental-strategies", "long-multiplication", "rounding",
            "decimals-explained", "negative-numbers", "angles", "coordinates-and-translation"],
    closing="""<p>If you do one thing in Year 4, make it short daily times tables practice. Three
      minutes a day from September is roughly twelve hours by June, and it is the difference
      between a child who finds Year 5 arithmetic straightforward and one who finds every topic
      slightly too hard.</p>
      <p>The check itself is low-stakes for the child and no result is reported to parents by
      default, though schools will usually tell you if you ask. Treat it as a deadline rather than
      an exam.</p>""",
    faqs=[
        ("What is the Multiplication Tables Check?",
         "A statutory on-screen check taken by all Year 4 children in England in June. It asks 25 multiplication questions from the 2 to 12 times tables, with six seconds to answer each."),
        ("Which times tables are expected in Year 4?",
         "All of them, up to 12 \u00d7 12, including the matching division facts."),
        ("Is there a pass mark for the MTC?",
         "No pass mark is published for parents. It is a school accountability measure, not a test the child can fail, though 25 out of 25 is the full score."),
        ("What else is new in Year 4?",
         "Four-digit place value, rounding to the nearest 1000, decimals to two places, negative numbers, Roman numerals to 100, area by counting squares, and coordinates in the first quadrant."),
    ],
)

# ------------------------------------------------------------------ Year 5
_y(
    n=5, ks="Upper Key Stage 2", ages="ages 9\u201310", nav="Year 5 maths",
    card="Long multiplication, short division, percentages and numbers to a million.",
    seo="Year 5 maths \u2014 what children learn, and how to practise it | Math It!",
    desc="What Year 5 maths covers in England: numbers to a million, long multiplication, short division, mixed numbers, percentages, prime and square numbers, angles and area formulae.",
    keywords="year 5 maths, upper KS2, year 5 curriculum, long multiplication year 5, year 5 fractions, percentages year 5, year 5 maths worksheets",
    intro="""<p>Year 5 is the heaviest content year in primary maths. Numbers go to a million, long
      multiplication and short division arrive, fractions get genuinely difficult, and percentages
      appear for the first time.</p>
      <p>It is also the year that assumes everything before it. Long multiplication is unusable
      without fluent tables; adding fractions with different denominators is unusable without
      multiples. Gaps that were survivable in Year 4 become limiting here.</p>""",
    new=[
        ("Long multiplication",
         """<p>Four-digit numbers multiplied by a two-digit number, using the formal written
         method. It is the first algorithm with two layers of partial products and a placeholder
         zero, and it is unforgiving of shaky tables.</p>"""),
        ("Short division",
         """<p>Up to four digits divided by a one-digit number, with remainders interpreted in
         context. The \u2018bus stop\u2019 method, done formally.</p>"""),
        ("Percentages",
         """<p>Introduced as \u2018parts per hundred\u2019, with the equivalences for 50%, 25%,
         20% and 10%. Year 6 does the harder work, but the concept starts here.</p>"""),
        ("Fractions with related denominators",
         """<p>Adding and subtracting fractions where one denominator is a multiple of the other,
         plus mixed numbers and improper fractions, and multiplying proper fractions by whole
         numbers.</p>"""),
        ("Primes, squares and cubes",
         """<p>Prime numbers up to 19 by recall, composite numbers, prime factors, and the
         notation for square and cube numbers.</p>"""),
    ],
    strands=[
        ("Number and place value", [
            "Read, write, order and compare numbers to at least 1 000 000.",
            "Count forwards and backwards in steps of powers of 10.",
            "Interpret negative numbers in context.",
            "Round any number up to 1 000 000 to the nearest 10, 100, 1000, 10 000 or 100 000.",
            "Read Roman numerals to 1000 (M), including years.",
        ]),
        ("Addition and subtraction", [
            "Add and subtract whole numbers with more than four digits using column methods.",
            "Add and subtract numbers mentally with increasingly large numbers.",
            "Use rounding to check answers and decide on levels of accuracy.",
        ]),
        ("Multiplication and division", [
            "Identify multiples, factors, common factors and factor pairs.",
            "Know prime numbers up to 19; recognise prime and composite numbers.",
            "Multiply numbers up to four digits by a one- or two-digit number using formal written methods, including long multiplication.",
            "Divide numbers up to four digits by a one-digit number using short division, interpreting remainders appropriately.",
            "Recognise and use square numbers and cube numbers, and the notation \u00b2 and \u00b3.",
            "Multiply and divide whole numbers and decimals by 10, 100 and 1000.",
        ]),
        ("Fractions, decimals and percentages", [
            "Compare and order fractions whose denominators are multiples of the same number.",
            "Convert between mixed numbers and improper fractions.",
            "Add and subtract fractions with denominators that are multiples of the same number.",
            "Multiply proper fractions and mixed numbers by whole numbers.",
            "Read and write decimal numbers as fractions; recognise thousandths.",
            "Round decimals with two decimal places to the nearest whole number and to one decimal place.",
            "Recognise the percent symbol and write percentages as fractions and decimals.",
        ]),
        ("Measurement", [
            "Convert between metric units of length, mass and volume.",
            "Know approximate equivalences between metric and imperial units.",
            "Measure and calculate the perimeter of composite rectilinear shapes.",
            "Calculate the area of rectangles using cm\u00b2 and m\u00b2, and estimate the area of irregular shapes.",
            "Estimate volume and capacity.",
        ]),
        ("Geometry and statistics", [
            "Identify 3D shapes from 2D representations.",
            "Draw and measure angles in degrees; know angles at a point total 360\u00b0 and on a straight line 180\u00b0.",
            "Distinguish regular from irregular polygons.",
            "Identify, describe and represent reflections and translations.",
            "Complete, read and interpret information in tables, including timetables, and solve problems using line graphs.",
        ]),
    ],
    sticking=[
        ("Long multiplication without the placeholder zero",
         "The second row is multiplying by tens, so it needs a 0 in the units column. Writing it first, before multiplying, prevents the commonest error in the method."),
        ("Adding fractions by adding both parts",
         "1/2 + 1/3 is not 2/5. Find a common denominator first. If the denominators have nothing in common, multiply them together."),
        ("Short division stalling on the first digit",
         "When the divisor is bigger than the first digit, carry it across rather than skipping it. 3 into 1 is 0 remainder 1."),
        ("Percentages memorised as a procedure",
         "10% is a tenth. 25% is a quarter. If a child can only find a percentage by multiplying by 0.01, the understanding is missing."),
    ],
    settings=[
        ("Year 5, medium", "practice.html?year=5&amp;level=medium", "A balanced sheet at the expected standard \u2014 the best general-purpose setting for the year."),
        ("Long multiplication and short division", "practice.html?year=5&amp;level=medium&amp;topics=long-mult,short-div", "The two new written methods, on their own."),
        ("Fractions focus", "practice.html?year=5&amp;level=medium&amp;topics=frac-add-sub,mixed-improper,frac-mult-int", "Adding, converting and multiplying fractions \u2014 the hardest strand of the year."),
        ("Percentages and conversions", "practice.html?year=5&amp;level=medium&amp;topics=percent-of,fdp-convert", "Percentages of amounts plus fraction, decimal and percentage equivalences."),
    ],
    tables="""<p>No new tables \u2014 Year 5 assumes all of them. What changes is the use: long
      multiplication, short division, finding factors and simplifying fractions all require instant
      recall rather than working out.</p>
      <p>If tables are still slow at the start of Year 5, fixing them is the highest-value thing
      you can do, because it unblocks four separate topics at once.</p>""",
    guides=["long-multiplication", "short-division", "adding-subtracting-fractions",
            "mixed-numbers", "percentages-of-amounts", "fractions-decimals-percentages",
            "factors-multiples-primes", "square-cube-numbers", "angles", "perimeter-and-area"],
    closing="""<p>Year 5 is the year to be honest about gaps. The content is demanding enough that
      a child carrying weak tables or shaky column methods will find it genuinely hard rather than
      merely challenging, and the fix is almost always further back than the topic being
      taught.</p>
      <p>It is also the last year before SATs preparation starts to shape the timetable, which
      makes it the best remaining opportunity to build fluency properly rather than revise.</p>""",
    faqs=[
        ("What is the hardest topic in Year 5 maths?",
         "Fractions with different denominators, and long multiplication. Both require fluent times tables, so weak recall makes them much harder than they need to be."),
        ("Do Year 5 children learn long division?",
         "No \u2014 Year 5 covers short division by a one-digit number. Long division by a two-digit number is a Year 6 objective."),
        ("What percentages are expected in Year 5?",
         "Understanding percent as parts per hundred, and knowing the equivalences for 50%, 25%, 20% and 10% as fractions and decimals."),
        ("Are there tests in Year 5?",
         "No national tests. Most schools run internal assessments, and some use Year 5 results to set groups for Year 6."),
    ],
)

# ------------------------------------------------------------------ Year 6
_y(
    n=6, ks="Upper Key Stage 2", ages="ages 10\u201311", nav="Year 6 maths",
    card="Long division, ratio, algebra, BIDMAS and the end of Key Stage 2 SATs.",
    seo="Year 6 maths \u2014 the full curriculum and SATs preparation | Math It!",
    desc="What Year 6 maths covers in England: long division, all four operations with fractions, ratio and proportion, algebra, BIDMAS, the mean, circles and the Key Stage 2 SATs papers.",
    keywords="year 6 maths, KS2 SATs, year 6 curriculum, long division year 6, BIDMAS, ratio and proportion year 6, algebra year 6, year 6 maths worksheets",
    intro="""<p>Year 6 completes primary maths and ends with the Key Stage 2 SATs in May: one
      arithmetic paper and two reasoning papers. The content is the broadest of any year, and two
      entirely new strands appear \u2014 ratio and proportion, and algebra.</p>
      <p>It is also the year the four operations finally cover fractions and decimals completely,
      and the year order of operations is formalised as BIDMAS.</p>""",
    new=[
        ("Long division",
         """<p>Four-digit numbers divided by a two-digit number, with remainders expressed as whole
         numbers, fractions or decimals depending on the context. The hardest written method in
         primary maths.</p>"""),
        ("Ratio and proportion",
         """<p>A brand new strand. Relative sizes, scale factors, unequal sharing, and using
         percentages for comparison. It leans heavily on multiplication and division fluency.</p>"""),
        ("Algebra",
         """<p>Also new. Simple formulae, linear sequences, missing-number problems written
         algebraically, and finding pairs of values that satisfy an equation with two
         unknowns.</p>"""),
        ("Order of operations",
         """<p>BIDMAS, formalised. Brackets, indices, division and multiplication left to right,
         then addition and subtraction left to right.</p>"""),
        ("The mean",
         """<p>The only average assessed at KS2 \u2014 calculated and interpreted, including
         working backwards from a mean to a missing value.</p>"""),
    ],
    strands=[
        ("Number and place value", [
            "Read, write, order and compare numbers up to 10 000 000.",
            "Round any whole number to a required degree of accuracy.",
            "Use negative numbers in context and calculate intervals across zero.",
        ]),
        ("The four operations", [
            "Multiply up to four digits by a two-digit number using long multiplication.",
            "Divide up to four digits by a two-digit number using long division, interpreting remainders as whole numbers, fractions or by rounding.",
            "Identify common factors, common multiples and prime numbers.",
            "Use the order of operations to carry out calculations \u2014 BIDMAS.",
            "Use estimation to check answers and determine accuracy in context.",
        ]),
        ("Fractions, decimals and percentages", [
            "Simplify fractions using common factors.",
            "Compare and order fractions, including fractions greater than 1.",
            "Add and subtract fractions with different denominators and mixed numbers.",
            "Multiply pairs of proper fractions, giving the answer in its simplest form.",
            "Divide proper fractions by whole numbers.",
            "Associate a fraction with division to calculate decimal equivalents.",
            "Multiply one-digit numbers with up to two decimal places by whole numbers.",
            "Recall and use equivalences between simple fractions, decimals and percentages.",
        ]),
        ("Ratio and proportion", [
            "Solve problems involving the relative sizes of two quantities.",
            "Solve problems involving percentages for comparison.",
            "Solve problems involving similar shapes where the scale factor is known.",
            "Solve problems involving unequal sharing and grouping.",
        ]),
        ("Algebra", [
            "Use simple formulae.",
            "Generate and describe linear number sequences.",
            "Express missing number problems algebraically.",
            "Find pairs of numbers that satisfy an equation with two unknowns.",
            "Enumerate possibilities of combinations of two variables.",
        ]),
        ("Measurement, geometry and statistics", [
            "Convert between standard units, including miles and kilometres.",
            "Calculate the area of parallelograms and triangles, and the volume of cuboids.",
            "Draw 2D shapes using given dimensions and angles; build and name 3D shapes from nets.",
            "Find unknown angles in triangles, quadrilaterals and regular polygons.",
            "Name parts of a circle and know the diameter is twice the radius.",
            "Describe positions on the full coordinate grid, all four quadrants.",
            "Interpret and construct pie charts and line graphs; calculate and interpret the mean.",
        ]),
    ],
    sticking=[
        ("Long division \u2014 everything about it",
         "Write the 1 to 10 multiples of the divisor down the side before starting. It converts the hardest method in primary maths into repeated subtraction and lookup."),
        ("BIDMAS read strictly left to right",
         "Division and multiplication rank equally and are done left to right; the same goes for addition and subtraction. 12 \u00f7 2 \u00d7 3 is 18, not 2."),
        ("Ratio confused with fractions",
         "In 2 : 3 there are five parts, so the first quantity is 2/5 of the total, not 2/3. Drawing the five parts fixes it."),
        ("Dividing fractions by flipping the wrong one",
         "Keep, change, flip \u2014 and it is always the second fraction that flips."),
        ("Reasoning marks lost to misread questions",
         "Underline what is actually being asked before calculating. Most lost reasoning marks in SATs are comprehension, not arithmetic."),
    ],
    settings=[
        ("Year 6, medium", "practice.html?year=6&amp;level=medium", "Mixed arithmetic at the expected standard \u2014 close in feel to SATs Paper 1."),
        ("Year 6, hard", "practice.html?year=6&amp;level=hard", "Stretch material for children aiming at greater depth."),
        ("Fractions, all four operations", "practice.html?year=6&amp;level=hard&amp;topics=frac-add-sub,frac-mult-frac,frac-div-int,frac-simplify", "The full fraction strand, which carries a lot of SATs marks."),
        ("BIDMAS, ratio and algebra", "practice.html?year=6&amp;level=medium&amp;topics=bidmas,ratio,algebra", "The three strands that are new or newly formalised this year."),
    ],
    tables="""<p>Tables are assumed completely. In Year 6 they are the engine behind long division,
      simplifying fractions, finding common denominators, scale factors and factorising \u2014 none
      of which work at speed without them.</p>
      <p>A child still counting up to find 7 \u00d7 8 in Year 6 will run out of time in the
      arithmetic paper regardless of how well they understand the methods.</p>""",
    guides=["long-division", "order-of-operations", "ratio-and-proportion", "simple-algebra",
            "dividing-fractions", "multiplying-fractions", "adding-subtracting-fractions",
            "percentages-of-amounts", "averages-and-the-mean", "coordinates-and-translation",
            "negative-numbers", "volume-and-capacity"],
    closing="""<p>The Key Stage 2 SATs are taken in May: Paper 1 is 30 minutes of arithmetic, 40
      marks; Papers 2 and 3 are 40 minutes each of reasoning, 35 marks apiece. The arithmetic paper
      rewards fluency directly, and it is the most improvable of the three with regular short
      practice.</p>
      <p>For the reasoning papers, the limiting factor is usually reading rather than maths.
      Practising the routine \u2014 read twice, underline the question, write the number sentence,
      estimate \u2014 earns more marks than another hour of calculation drill. Our
      <a href="../guides/word-problems.html">word problems guide</a> sets that out in full.</p>""",
    faqs=[
        ("What is in the Year 6 SATs maths papers?",
         "Three papers. Paper 1 is arithmetic, 30 minutes and 40 marks. Papers 2 and 3 are reasoning, 40 minutes and 35 marks each. They are taken in May."),
        ("What is new in Year 6 maths?",
         "Long division, ratio and proportion, algebra, the order of operations as BIDMAS, the mean, parts of a circle, area of triangles and parallelograms, and volume of cuboids."),
        ("How do I help with long division?",
         "Write the first ten multiples of the divisor down the side of the page before starting. It turns the method into subtraction and matching, and removes most of the difficulty."),
        ("What is the best way to prepare for the arithmetic paper?",
         "Short, frequent, timed practice. It tests fluency with methods already taught, so speed and accuracy improve measurably with ten minutes a day."),
    ],
)

ORDER = [2, 3, 4, 5, 6]

assert set(ORDER) == set(YEARS), "years data out of step with ORDER"
for _n in ORDER:
    _d = YEARS[_n]
    for _k in ("ks", "ages", "nav", "card", "seo", "desc", "keywords", "intro",
               "new", "strands", "sticking", "settings", "tables", "guides",
               "closing", "faqs"):
        assert _d.get(_k), f"year {_n}: missing {_k}"
