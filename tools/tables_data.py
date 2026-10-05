# -*- coding: utf-8 -*-
"""Per-table content for tables/<n>-times-table.html.

Everything here is written per table. The grid of facts is generated (it is
arithmetic), but the patterns, tricks, hardest facts, contexts and FAQs are
specific to the table in question -- a 7 page and an 8 page have almost
nothing in common beyond their layout.

Schema
    n          int, the table
    year       school year it is expected in England
    nav        short label
    card       one-line blurb for the hub
    seo/desc/keywords
    intro      HTML, 2 paragraphs
    patterns   [(heading, html)]   things that are true of this table only
    trick      (heading, html)     the fastest reliable route to a fact
    hardest    [(fact, answer, help)]
    real       [(context, text)]
    checks     [(question, answer)]  quick self-test
    closing    HTML, a longer prose section
    related    [(n, why)]
    faqs       [(q, a)]
"""

TABLES = {}


def _t(**kw):
    TABLES[kw["n"]] = kw


# ------------------------------------------------------------------ 2
_t(
    n=2, year="Year 2", nav="2 times table",
    card="Doubling, and the first table nearly every child already half knows.",
    seo="The 2 times table \u2014 doubling, patterns and division facts | Math It!",
    desc="The 2 times table from 2 \u00d7 1 to 2 \u00d7 12, why it is the same as doubling, the even-number pattern, its division facts and free printable practice.",
    keywords="2 times table, two times table, doubling, even numbers, 2x table, year 2 times tables, times table practice",
    intro="""<p>The 2 times table is the first one taught in England, and most children arrive
      already knowing a fair chunk of it from counting in pairs. Multiplying by 2 is doubling, and
      doubling is something children do long before they have a word for it \u2014 two hands, two
      socks, two of everything.</p>
      <p>Every answer in the 2 times table is an even number. That single fact is worth as much as
      the table itself: it is the definition of even, and it underpins halving, sharing and the
      4 and 8 tables that follow.</p>""",
    patterns=[
        ("Every answer is even",
         """<p>The last digit of every multiple of 2 cycles through 2, 4, 6, 8, 0 and then starts
         again: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. A number is even precisely because it is a
         multiple of 2, so this table defines the word rather than merely illustrating it.</p>"""),
        ("The answers go up in the smallest useful step",
         """<p>Each answer is exactly 2 more than the one before. That makes the 2 times table the
         easiest to rebuild from scratch if a fact slips: counting on in twos from a fact you are
         sure of costs a second or two and never fails.</p>"""),
        ("It is half of the 4 times table",
         """<p>2 \u00d7 6 = 12 and 4 \u00d7 6 = 24. Every fact in the 4 times table is double the
         matching fact here, and every fact in the 8 times table is double that again. Learning
         2 properly buys you a head start on two more tables.</p>"""),
    ],
    trick=("Multiplying by 2 is doubling",
           """<p>There is no shortcut to find here, because multiplying by 2 <em>is</em> the
           shortcut. What helps is making doubling automatic beyond 12: double 15 is 30, double 25
           is 50, double 35 is 70.</p>
           <p>Split the number if it is awkward. Double 17 = double 10 + double 7 = 20 + 14 = 34.
           Children who can do that comfortably find the 4 and 8 tables almost free, because both
           are just doubling repeated.</p>"""),
    hardest=[
        ("2 \u00d7 7", "14", "The only one that ever hesitates, and usually only because 7 itself feels awkward. 7 + 7 = 14 \u2014 a number bond most children already own."),
        ("2 \u00d7 9", "18", "Think 2 \u00d7 10 = 20, then take away 2. One less lot of 2."),
        ("2 \u00d7 12", "24", "Double 12. Useful well beyond this table \u2014 24 hours, two dozen, 24 is everywhere."),
    ],
    real=[
        ("Shoes, socks and gloves", "Pairs are the everyday model of \u00d7 2. Six pairs of socks is twelve socks."),
        ("Wheels", "A bike has 2 wheels, so eight bikes have 16 wheels. A classic Year 2 word problem."),
        ("2p coins", "Counting a handful of 2p coins is 2 times table practice that happens to be useful."),
        ("Sharing fairly between two", "Every \u00d7 2 fact read backwards is a halving fact, which is how most children first meet division."),
    ],
    checks=[("2 \u00d7 8", "16"), ("2 \u00d7 11", "22"), ("18 \u00f7 2", "9"), ("2 \u00d7 ? = 14", "7")],
    closing="""<p>Because the 2 times table maps exactly onto doubling and halving, it is the one
      table worth practising in both directions from the very start. A child who answers
      \u201chalf of 18\u201d as readily as \u201c2 \u00d7 9\u201d has understood that multiplication
      and division are the same relationship viewed from opposite ends \u2014 and that idea is what
      makes every later table quicker to learn.</p>
      <p>If recall is still slow, the problem is almost never the 2 times table itself. It is
      usually counting fluency underneath it. Counting in twos out loud, forwards from 2 and
      backwards from 24, fixes it faster than drilling the facts.</p>""",
    related=[(4, "Double every answer here and you have the 4 times table."),
             (10, "The other table taught in Year 2, and the easiest of the lot."),
             (5, "Also built on counting, and pairs neatly with 10.")],
    faqs=[
        ("What is the 2 times table?",
         "2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 \u2014 the multiples of 2 up to 2 \u00d7 12. Multiplying by 2 is the same as doubling."),
        ("When should a child know the 2 times table?",
         "Year 2 in England. The national curriculum expects the 2, 5 and 10 times tables by the end of Year 2."),
        ("Why is every answer in the 2 times table even?",
         "Because that is what even means: a number that divides exactly by 2. The 2 times table lists the even numbers in order."),
        ("How do I help a child who is stuck on it?",
         "Practise counting in twos forwards and backwards rather than drilling facts. Fluent counting in twos makes the table almost automatic."),
    ],
)

# ------------------------------------------------------------------ 3
_t(
    n=3, year="Year 3", nav="3 times table",
    card="The digit-sum test, the first table with no obvious shortcut, and why it matters.",
    seo="The 3 times table \u2014 patterns, the digit-sum trick and division facts | Math It!",
    desc="The 3 times table to 3 \u00d7 12, the digit-sum test for multiples of 3, its hardest facts, division facts and free printable practice sheets.",
    keywords="3 times table, three times table, multiples of 3, digit sum rule, 3x table, year 3 times tables, divisibility by 3",
    intro="""<p>The 3 times table is the first real piece of work. There is no doubling shortcut,
      the answers do not end in a tidy repeating pair of digits, and it arrives in Year 3 alongside
      the 4 and 8 tables.</p>
      <p>It does have one genuinely elegant property, though, and it is worth teaching early: add
      the digits of any multiple of 3 and the total is also a multiple of 3. That test works for
      numbers of any size, which makes it far more useful than a memory trick.</p>""",
    patterns=[
        ("The digit sum is always 3, 6 or 9",
         """<p>Add the digits of any multiple of 3 and keep going until one digit is left: 12
         \u2192 3, 15 \u2192 6, 18 \u2192 9, 21 \u2192 3, 24 \u2192 6, 27 \u2192 9. The cycle 3, 6, 9
         repeats forever.</p>
         <p>It scales to any number at all. Is 4\u202f731 a multiple of 3? 4 + 7 + 3 + 1 = 15, and
         1 + 5 = 6. Yes. No division needed.</p>"""),
        ("The last digits use all ten digits",
         """<p>3, 6, 9, 12, 15, 18, 21, 24, 27, 30 end in 3, 6, 9, 2, 5, 8, 1, 4, 7, 0. Every digit
         appears exactly once before the cycle repeats, which is precisely why the 3 times table
         has no \u201clook at the last digit\u201d shortcut the way 2, 5 and 10 do.</p>"""),
        ("Alternate answers are the 6 times table",
         """<p>3, <strong>6</strong>, 9, <strong>12</strong>, 15, <strong>18</strong> \u2014 every
         other multiple of 3 is a multiple of 6. Children who know their threes are two-thirds of
         the way to their sixes.</p>"""),
    ],
    trick=("Double it, then add one more lot",
           """<p>3 \u00d7 7: double 7 is 14, add another 7, giving 21. It sounds long-winded
           written down but it is quick in the head, and it works for every fact in the table.</p>
           <p>For the larger ones, go the other way. 3 \u00d7 9 = 3 \u00d7 10 \u2212 3 = 30
           \u2212 3 = 27. Bridging through a ten is usually faster than counting on in threes,
           which is where most children lose time.</p>"""),
    hardest=[
        ("3 \u00d7 7", "21", "Nothing about it is memorable, so attach it to something: 21 is three weeks of days."),
        ("3 \u00d7 8", "24", "24 appears everywhere \u2014 hours in a day, two dozen. Also 3 \u00d7 8 = 4 \u00d7 6, which is a useful cross-check."),
        ("3 \u00d7 12", "36", "Think 3 \u00d7 10 + 3 \u00d7 2 = 30 + 6. 36 is also 6 squared, which ties two tables together."),
    ],
    real=[
        ("Triangles", "Three sides, three angles, three vertices. Counting sides across several triangles is \u00d7 3 in disguise."),
        ("Feet in a yard", "Three feet to a yard \u2014 still used in sport and for fabric."),
        ("Three-for-two offers", "Supermarket pricing is a steady source of real \u00d7 3 and \u00f7 3 problems."),
        ("Music", "Three beats in a bar of a waltz. Counting bars is multiplying by 3."),
    ],
    checks=[("3 \u00d7 6", "18"), ("3 \u00d7 9", "27"), ("33 \u00f7 3", "11"), ("3 \u00d7 ? = 24", "8")],
    closing="""<p>The 3 times table is the one most worth over-practising, because so much later
      work leans on it. Simplifying fractions depends on spotting that both 9 and 12 divide by 3.
      Finding equivalent fractions, cancelling ratios, factorising \u2014 all of it starts with
      recognising a multiple of 3 on sight.</p>
      <p>The digit-sum test is the single most transferable thing in this table. Teach it as a
      tool rather than a curiosity: children who can glance at 147 and know instantly that it
      divides by 3 are doing something genuinely useful for the next ten years of maths.</p>""",
    related=[(6, "Every other multiple of 3 is a multiple of 6."),
             (9, "Also has a digit-sum test \u2014 the digits of a multiple of 9 add to 9."),
             (12, "12 is 3 \u00d7 4, so the two tables share a lot of answers.")],
    faqs=[
        ("What is the 3 times table?",
         "3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36 \u2014 the multiples of 3 up to 3 \u00d7 12."),
        ("How can you tell if a number divides by 3?",
         "Add its digits. If the total is a multiple of 3, so is the number. For 4\u202f731: 4 + 7 + 3 + 1 = 15, which divides by 3, so 4\u202f731 does too."),
        ("When is the 3 times table taught?",
         "Year 3 in England, alongside the 4 and 8 times tables."),
        ("Why is the 3 times table harder than the 2 or 5?",
         "Its last digits run through all ten digits before repeating, so there is no end-digit pattern to lean on. It has to be learnt as facts, supported by the digit-sum test."),
    ],
)

# ------------------------------------------------------------------ 4
_t(
    n=4, year="Year 3", nav="4 times table",
    card="Double, then double again \u2014 the table you can derive instead of memorising.",
    seo="The 4 times table \u2014 double-double, patterns and division facts | Math It!",
    desc="The 4 times table to 4 \u00d7 12, the double-double method, the even-digit pattern, its hardest facts and free printable practice.",
    keywords="4 times table, four times table, double double, multiples of 4, 4x table, year 3 times tables, quarters",
    intro="""<p>The 4 times table is the most derivable of them all. Multiplying by 4 is doubling
      twice, so a child who is fluent with doubling can reconstruct any fact in about a second,
      even before recall has set in.</p>
      <p>That makes it a confidence-building table to teach after the 2s, and a useful one to
      revisit when the 8 times table arrives \u2014 because 8 is simply one more doubling on
      top.</p>""",
    patterns=[
        ("Every answer is even, and the last digits cycle in five steps",
         """<p>4, 8, 12, 16, 20, 24, 28, 32, 36, 40 end in 4, 8, 2, 6, 0 and then repeat. Five
         endings, in that fixed order, forever.</p>"""),
        ("Every multiple of 4 is a multiple of 2 \u2014 twice over",
         """<p>Halve any multiple of 4 and you land on a multiple of 2. Halve it again and you get
         back to the number you multiplied by. 36 \u2192 18 \u2192 9, so 36 = 4 \u00d7 9.</p>"""),
        ("The last two digits decide divisibility",
         """<p>A number divides by 4 if its last two digits do. 1\u202f328 divides by 4 because 28
         does. 1\u202f330 does not, because 30 does not. The rest of the number is irrelevant,
         which makes this a quick test on large numbers.</p>"""),
    ],
    trick=("Double, then double again",
           """<p>4 \u00d7 7: double 7 is 14, double 14 is 28. 4 \u00d7 9: double 9 is 18, double 18
           is 36. It is reliable, it is fast, and it rehearses doubling at the same time.</p>
           <p>The reverse works for division: to divide by 4, halve twice. 52 \u00f7 4 \u2192 26
           \u2192 13. Children find this far easier than short division, and it is exactly how most
           adults do it.</p>"""),
    hardest=[
        ("4 \u00d7 7", "28", "Double 7 to 14, double again to 28. Also 28 days in February, and four weeks."),
        ("4 \u00d7 8", "32", "Double-double 8: 16 then 32. Worth knowing for its own sake \u2014 32 is a common answer across several tables."),
        ("4 \u00d7 6", "24", "Doubling 6 twice gives 12 then 24. Note that 4 \u00d7 6 = 3 \u00d7 8, two routes to the same answer."),
    ],
    real=[
        ("Wheels on a car", "Four wheels each \u2014 the standard Year 3 word problem, and genuinely how children first see \u00d7 4."),
        ("Quarters", "Four quarters make a whole, so dividing by 4 and finding a quarter are the same operation."),
        ("Weeks in a month", "Roughly four weeks, so 4 \u00d7 7 = 28 days turns up constantly in calendar questions."),
        ("Legs on a table or a chair", "Counting legs around a classroom is \u00d7 4 practice that children can actually do."),
    ],
    checks=[("4 \u00d7 7", "28"), ("4 \u00d7 12", "48"), ("36 \u00f7 4", "9"), ("4 \u00d7 ? = 32", "8")],
    closing="""<p>The double-double method is worth teaching explicitly rather than hoping it will
      be noticed, because it generalises. Multiplying by 8 is doubling three times. Multiplying by
      16 is four doublings. Children who internalise the chain 2 \u2192 4 \u2192 8 have a way
      through three tables, not one.</p>
      <p>It also quietly teaches associativity: 4 \u00d7 7 works as (2 \u00d7 2) \u00d7 7 =
      2 \u00d7 (2 \u00d7 7). Nobody needs the word at primary, but the idea that you can regroup a
      multiplication to make it easier is one of the most useful habits in arithmetic.</p>""",
    related=[(2, "Multiplying by 4 is doubling twice, so the 2 table comes first."),
             (8, "One more doubling on top of the 4s."),
             (12, "12 is 4 \u00d7 3, so the two tables overlap heavily.")],
    faqs=[
        ("What is the 4 times table?",
         "4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48 \u2014 the multiples of 4 up to 4 \u00d7 12."),
        ("What is the easiest way to multiply by 4?",
         "Double the number, then double the answer. 4 \u00d7 7 becomes 14, then 28."),
        ("How can you tell if a number divides by 4?",
         "Look at the last two digits only. If they form a number that divides by 4, the whole number does. 1\u202f328 works because 28 does."),
        ("When is the 4 times table taught?",
         "Year 3 in England, together with the 3 and 8 times tables."),
    ],
)

# ------------------------------------------------------------------ 5
_t(
    n=5, year="Year 2", nav="5 times table",
    card="Ends in 5 or 0, lives on the clock face, and is half of the 10 times table.",
    seo="The 5 times table \u2014 the clock-face table, patterns and division facts | Math It!",
    desc="The 5 times table to 5 \u00d7 12, why every answer ends in 5 or 0, the clock-face connection, division facts and free printable practice.",
    keywords="5 times table, five times table, multiples of 5, counting in fives, 5x table, year 2 times tables, clock face minutes",
    intro="""<p>The 5 times table is the friendliest in the set. Every answer ends in 5 or 0, which
      gives children an instant check on whether an answer is even plausible, and the pattern holds
      without exception however far you go.</p>
      <p>It is also the table with the best real-world anchor: the clock face. Every number on a
      clock is a multiple of 5 minutes, so a child who can read an analogue clock is practising the
      5 times table several times a day without noticing.</p>""",
    patterns=[
        ("Every answer ends in 5 or 0",
         """<p>5, 10, 15, 20, 25, 30 \u2014 odd multiplier gives an answer ending in 5, even
         multiplier gives one ending in 0. That alternation never breaks, so an answer like 23 can
         be ruled out instantly.</p>"""),
        ("It is exactly half of the 10 times table",
         """<p>10 \u00d7 7 = 70, so 5 \u00d7 7 = 35. Multiply by 10 and halve \u2014 often faster
         than recalling the fact, and it keeps the two tables tied together in a child's head.</p>"""),
        ("The clock face is the 5 times table",
         """<p>The 3 on a clock is 15 minutes, the 7 is 35, the 11 is 55. Reading minutes from an
         analogue clock is pure 5 times table, which is why the two topics are usually taught in
         the same term.</p>"""),
    ],
    trick=("Multiply by 10, then halve",
           """<p>5 \u00d7 8: ten eights are 80, half of 80 is 40. 5 \u00d7 14: 140, halve to 70.
           This scales well past 12, which is why it is worth teaching even to children who already
           know the table by heart.</p>
           <p>It works in reverse for division too. 85 \u00f7 5: double 85 to 170, then divide by
           10 to get 17. Most adults who are quick at mental arithmetic are doing exactly
           this.</p>"""),
    hardest=[
        ("5 \u00d7 7", "35", "The one that hesitates most often. Odd multiplier, so the answer must end in 5 \u2014 that narrows it to 35 immediately."),
        ("5 \u00d7 9", "45", "Half of 90. Or count back one five from 50."),
        ("5 \u00d7 12", "60", "60 minutes in an hour, which is the most useful fact in the whole table."),
    ],
    real=[
        ("Minutes on a clock", "Every numeral on the dial is five minutes. Twenty-five past is the 5."),
        ("Fingers and toes", "Five on each hand \u2014 the oldest counting tool there is, and why base ten exists."),
        ("5p coins", "Counting 5p coins, and working out how many make a pound, is \u00d7 5 and \u00f7 5 at once."),
        ("Tally marks", "Tallies are grouped in fives precisely because multiples of five are easy to total."),
    ],
    checks=[("5 \u00d7 7", "35"), ("5 \u00d7 11", "55"), ("45 \u00f7 5", "9"), ("5 \u00d7 ? = 60", "12")],
    closing="""<p>Because the 5 times table is so easy, it is the right place to teach what fluency
      actually means. A child who recites \u201cfive, ten, fifteen, twenty\u2026\u201d to reach
      5 \u00d7 7 does not know the table \u2014 they know how to count in fives. Fluency means
      answering 5 \u00d7 7 in isolation, out of order, without the run-up.</p>
      <p>Testing out of order is the fix, and it takes about a week. It is also a useful
      conversation to have with the child: the goal is not to be able to chant the table, it is to
      have the facts available instantly so that attention can go on the actual problem.</p>""",
    related=[(10, "Double every answer here to get the 10 times table."),
             (2, "The other table learnt in Year 2, and the basis of halving."),
             (3, "Comes next, and is the first real test of memory.")],
    faqs=[
        ("What is the 5 times table?",
         "5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 \u2014 the multiples of 5 up to 5 \u00d7 12."),
        ("Why does the 5 times table end in 5 or 0?",
         "Two fives make ten, so every second multiple lands exactly on a ten. The ones in between sit halfway, ending in 5."),
        ("What is the quickest way to multiply by 5?",
         "Multiply by 10 and halve the answer. 5 \u00d7 14 becomes 140, then 70."),
        ("When is the 5 times table taught?",
         "Year 2 in England, alongside the 2 and 10 times tables."),
    ],
)

# ------------------------------------------------------------------ 6
_t(
    n=6, year="Year 4", nav="6 times table",
    card="Double the threes, plus the neat trick hiding in the even multipliers.",
    seo="The 6 times table \u2014 patterns, the even-number trick and division facts | Math It!",
    desc="The 6 times table to 6 \u00d7 12, how it relates to the 3 times table, the pattern in its even multiples, its hardest facts and free printable practice.",
    keywords="6 times table, six times table, multiples of 6, 6x table, year 4 times tables, times tables check",
    intro="""<p>The 6 times table arrives in Year 4, when the national curriculum expects all
      tables to 12 \u00d7 12 to be secure. It sits in the awkward middle of the set: too big to
      count up to comfortably, without the obvious hook that 5, 9 and 10 enjoy.</p>
      <p>It does have two solid routes in. It is double the 3 times table, and \u2014 less well
      known \u2014 every even multiplier produces an answer ending in that same digit.</p>""",
    patterns=[
        ("Even multipliers keep their own last digit",
         """<p>6 \u00d7 2 = 1<strong>2</strong>, 6 \u00d7 4 = 2<strong>4</strong>, 6 \u00d7 6 =
         3<strong>6</strong>, 6 \u00d7 8 = 4<strong>8</strong>. The answer ends in the digit you
         multiplied by, and the tens digit is half of it.</p>
         <p>So 6 \u00d7 8: half of 8 is 4, giving 48. Six of the twelve facts fall out of this
         immediately, and it is the single most useful thing to know about this table.</p>"""),
        ("Every answer is double a multiple of 3",
         """<p>3 \u00d7 7 = 21, so 6 \u00d7 7 = 42. If the threes are secure, the sixes are one
         doubling away.</p>"""),
        ("Multiples of 6 are divisible by both 2 and 3",
         """<p>A number divides by 6 exactly when it is even <em>and</em> its digits add to a
         multiple of 3. 114 is even, and 1 + 1 + 4 = 6, so 114 divides by 6. This combines the
         tests from the 2 and 3 tables.</p>"""),
    ],
    trick=("Halve the multiplier, stick it in front",
           """<p>For even multipliers only: halve the number, then write the number itself after
           it. 6 \u00d7 8 \u2192 half of 8 is 4 \u2192 48. 6 \u00d7 6 \u2192 3 \u2192 36. 6 \u00d7
           12 \u2192 6 \u2192 72. Correct every time for 2, 4, 6, 8 and 12.</p>
           <p>For odd multipliers, go via the nearest even one: 6 \u00d7 7 = 6 \u00d7 6 + 6 = 36 +
           6 = 42. Or double the 3 times table fact.</p>"""),
    hardest=[
        ("6 \u00d7 7", "42", "Consistently one of the two least-recalled facts in the whole grid. 6 \u00d7 6 = 36, add 6 more. Or double 21."),
        ("6 \u00d7 8", "48", "Use the even trick: half of 8 is 4, so 48. Much more reliable than trying to recall it cold."),
        ("6 \u00d7 9", "54", "6 \u00d7 10 = 60, take away 6. Or use the 9 table: the digits of 54 add to 9."),
    ],
    real=[
        ("Half a dozen", "Eggs come in sixes. Four boxes is 24 eggs \u2014 a genuine \u00d7 6 problem most children have seen."),
        ("Hexagons", "Six sides each. Honeycomb, bolt heads, floor tiles."),
        ("Dice", "Six faces, so two dice give 12 outcomes per face and 36 combinations in total \u2014 6 squared."),
        ("Six-packs and multipacks", "Supermarket packaging is a steady supply of \u00d7 6 and \u00f7 6 questions."),
    ],
    checks=[("6 \u00d7 7", "42"), ("6 \u00d7 9", "54"), ("72 \u00f7 6", "12"), ("6 \u00d7 ? = 48", "8")],
    closing="""<p>Research on the Year 4 Multiplication Tables Check consistently shows that
      6 \u00d7 7, 6 \u00d7 8, 7 \u00d7 8 and 8 \u00d7 9 are the slowest facts nationally. The
      sixes contain two of those four, which makes this table worth disproportionate practice
      time.</p>
      <p>The useful insight is that children do not need to recall every fact at the same speed.
      Six facts in this table come free from the even-digit trick. Concentrate the effort on
      6 \u00d7 7 and 6 \u00d7 9, and the table as a whole stops being a problem.</p>""",
    related=[(3, "Halve every answer here and you get the 3 times table."),
             (12, "Double the sixes."),
             (7, "Shares the hardest fact in the grid: 6 \u00d7 7 = 42.")],
    faqs=[
        ("What is the 6 times table?",
         "6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72 \u2014 the multiples of 6 up to 6 \u00d7 12."),
        ("What is the trick for the 6 times table?",
         "For even multipliers, halve the number and put it in front: 6 \u00d7 8 gives 4 then 8, so 48. It works for 2, 4, 6, 8 and 12."),
        ("How can you tell if a number divides by 6?",
         "It must be even and its digits must add to a multiple of 3. 114 is even and 1 + 1 + 4 = 6, so it divides by 6."),
        ("Why is 6 \u00d7 7 so hard to remember?",
         "Neither number has an end-digit pattern and the answer, 42, has no obvious link to either. It is reliably one of the slowest facts in national testing \u2014 it usually needs deliberate practice."),
    ],
)

# ------------------------------------------------------------------ 7
_t(
    n=7, year="Year 4", nav="7 times table",
    card="The hardest table in the grid, and the handful of anchors that make it stick.",
    seo="The 7 times table \u2014 why it is hard, and how to actually learn it | Math It!",
    desc="The 7 times table to 7 \u00d7 12, why it has no shortcut, the 5-6-7-8 mnemonic for 7 \u00d7 8, its division facts and free printable practice.",
    keywords="7 times table, seven times table, multiples of 7, 7x table, 7 times 8, year 4 times tables, hardest times table",
    intro="""<p>The 7 times table is the one children and parents dread, and the reputation is
      deserved. It has no end-digit pattern, no digit-sum test, no finger trick and no doubling
      route in. 7 is prime, so nothing else in the grid generates it.</p>
      <p>What it does have is one excellent anchor \u2014 seven days in a week \u2014 and a small
      set of mnemonics for the two or three facts that genuinely resist. Everything else comes from
      the facts you already know, approached from the other side.</p>""",
    patterns=[
        ("There is no last-digit shortcut, and that is the point",
         """<p>7, 14, 21, 28, 35, 42, 49, 56, 63, 70 end in 7, 4, 1, 8, 5, 2, 9, 6, 3, 0 \u2014 all
         ten digits, in a scrambled order, before repeating. Unlike 2, 5 and 10, there is nothing
         to glance at.</p>
         <p>Being honest with children about this helps. The 7 times table is harder, they are not
         failing, and it needs more repetitions than the others.</p>"""),
        ("Half the table is already known",
         """<p>By the time the sevens are taught, a child who knows the 2, 3, 4, 5, 6 and 10 tables
         already knows 7 \u00d7 2, 7 \u00d7 3, 7 \u00d7 4, 7 \u00d7 5, 7 \u00d7 6 and 7 \u00d7 10
         \u2014 from the other direction. Commutativity means only 7 \u00d7 7, 7 \u00d7 8, 7 \u00d7
         9, 7 \u00d7 11 and 7 \u00d7 12 are genuinely new.</p>
         <p>Five facts. Framed that way, the table stops looking impossible.</p>"""),
        ("Seven days in a week does a lot of work",
         """<p>7 \u00d7 4 = 28 days in four weeks. 7 \u00d7 52 = 364, one day short of a year.
         Calendar questions give the sevens a context no other table has.</p>"""),
    ],
    trick=("Split 7 into 5 and 2",
           """<p>7 \u00d7 8 = (5 \u00d7 8) + (2 \u00d7 8) = 40 + 16 = 56. 7 \u00d7 9 = 45 + 18 =
           63. Both parts are easy tables, and the method is reliable when recall fails.</p>
           <p>For the top of the table, subtract instead: 7 \u00d7 9 = 70 \u2212 7 = 63, and
           7 \u00d7 12 = 70 + 14 = 84. Bridging through 7 \u00d7 10 is almost always the fastest
           route.</p>"""),
    hardest=[
        ("7 \u00d7 8", "56", "Say \u201cfive, six, seven, eight\u201d \u2014 56 = 7 \u00d7 8. The digits run in order. It is the best mnemonic in the whole grid and children never forget it."),
        ("7 \u00d7 9", "63", "Use the 9 trick: the tens digit is one less than 9, so 6, and the digits must add to 9, so 63."),
        ("7 \u00d7 7", "49", "Just under 50. It is also the square number, so it turns up in area questions \u2014 a 7 cm square has an area of 49 cm\u00b2."),
    ],
    real=[
        ("Days in a week", "The anchor for the whole table. Six weeks of school holiday is 6 \u00d7 7 = 42 days."),
        ("Colours in a rainbow", "Seven, conventionally \u2014 and a handy mental peg."),
        ("Weekly shopping and pocket money", "\u00a37 a week over nine weeks is 7 \u00d7 9 = \u00a363."),
        ("Days to hours", "7 \u00d7 24 = 168 hours in a week. A favourite extension question."),
    ],
    checks=[("7 \u00d7 8", "56"), ("7 \u00d7 6", "42"), ("63 \u00f7 7", "9"), ("7 \u00d7 ? = 84", "12")],
    closing="""<p>The most effective approach to the sevens is to stop treating them as a table to
      be chanted and start treating them as five individual facts to be learnt. Write 7 \u00d7 7,
      7 \u00d7 8, 7 \u00d7 9, 7 \u00d7 11 and 7 \u00d7 12 on five cards and work only on those.
      Everything else is a commuted fact from a table already known.</p>
      <p>Three minutes a day on five cards beats twenty minutes a week chanting the full list, and
      it beats it by a long way. Spaced retrieval is the best-evidenced technique in the whole of
      learning science, and times tables are about as pure a test of it as exists.</p>""",
    related=[(8, "Shares 7 \u00d7 8 = 56, the single most-missed fact nationally."),
             (6, "The other table containing a notoriously slow fact, 6 \u00d7 7."),
             (9, "Has a finger trick that rescues 7 \u00d7 9 = 63.")],
    faqs=[
        ("What is the 7 times table?",
         "7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84 \u2014 the multiples of 7 up to 7 \u00d7 12."),
        ("Why is the 7 times table the hardest?",
         "7 is prime, so no other table generates it, and its multiples run through all ten final digits before repeating. There is no pattern to lean on, so the facts have to be learnt directly."),
        ("How do I remember 7 \u00d7 8?",
         "Five, six, seven, eight \u2014 56 = 7 \u00d7 8. The four digits run in sequence, which makes it the most memorable mnemonic in the times tables."),
        ("How many facts actually need learning?",
         "Five. By Year 4 a child already knows 7 \u00d7 2 to 7 \u00d7 6 and 7 \u00d7 10 from earlier tables, so only 7 \u00d7 7, 7 \u00d7 8, 7 \u00d7 9, 7 \u00d7 11 and 7 \u00d7 12 are new."),
    ],
)

# ------------------------------------------------------------------ 8
_t(
    n=8, year="Year 3", nav="8 times table",
    card="Three doublings, a clean even pattern, and one notorious fact.",
    seo="The 8 times table \u2014 halving, doubling and division facts | Math It!",
    desc="The 8 times table to 8 \u00d7 12, the triple-doubling method, its last-digit pattern, the 8 \u00d7 7 problem and free printable practice.",
    keywords="8 times table, eight times table, multiples of 8, 8x table, year 3 times tables, doubling three times",
    intro="""<p>The 8 times table is taught in Year 3 alongside the 3s and 4s, which surprises
      people \u2014 it looks like one of the hard ones. It is placed there deliberately, because it
      follows directly from the 2s and 4s by doubling.</p>
      <p>Every fact in this table is three doublings away from the multiplier: 8 \u00d7 6 is 6
      \u2192 12 \u2192 24 \u2192 48. A child who can double reliably can produce any fact in the
      table while recall is still forming.</p>""",
    patterns=[
        ("The last digits count down in twos",
         """<p>8, 16, 24, 32, 40, 48, 56, 64, 72, 80 end in 8, 6, 4, 2, 0 \u2014 then repeat. The
         same five endings as the 4 times table, but running backwards.</p>"""),
        ("Every answer is in the 2 and 4 tables too",
         """<p>Multiples of 8 are multiples of 4, which are multiples of 2. 56 \u00f7 2 = 28,
         \u00f7 2 = 14, \u00f7 2 = 7 \u2014 so 56 = 8 \u00d7 7. Halving three times is a reliable
         way to divide by 8 in your head.</p>"""),
        ("The answers are powers of two in disguise",
         """<p>8 \u00d7 1, 8 \u00d7 2, 8 \u00d7 4 and 8 \u00d7 8 give 8, 16, 32 and 64 \u2014 the
         powers of two children meet again in computing. Bytes, memory sizes and screen resolutions
         all live in this table.</p>"""),
    ],
    trick=("Double three times",
           """<p>8 \u00d7 7: 7 \u2192 14 \u2192 28 \u2192 56. 8 \u00d7 9: 9 \u2192 18 \u2192 36
           \u2192 72. Three doublings, every time, no exceptions.</p>
           <p>Or come down from ten: 8 \u00d7 9 = 80 \u2212 8 = 72. For multipliers of 9 and above
           this is usually quicker, because subtracting one lot beats a third doubling.</p>"""),
    hardest=[
        ("8 \u00d7 7", "56", "The most-missed fact in national testing. Use the 5-6-7-8 mnemonic: 56 = 7 \u00d7 8."),
        ("8 \u00d7 6", "48", "Double 6 three times: 12, 24, 48. Or use the 6 table trick \u2014 half of 8 is 4, so 48."),
        ("8 \u00d7 9", "72", "80 \u2212 8. Or check with the 9 rule: 7 + 2 = 9, and the tens digit is one less than 8."),
    ],
    real=[
        ("Legs on a spider", "Eight each. Classic Year 3 fare, and children remember it."),
        ("Octagons", "Eight sides \u2014 a stop sign is the standard example."),
        ("Bits in a byte", "Eight. Which is why 8, 16, 32, 64, 128 and 256 run through all computing."),
        ("Slices of pizza", "Eight per pizza, so three pizzas is 24 slices \u2014 and sharing them is \u00f7 8."),
    ],
    checks=[("8 \u00d7 7", "56"), ("8 \u00d7 6", "48"), ("64 \u00f7 8", "8"), ("8 \u00d7 ? = 96", "12")],
    closing="""<p>Because 8 \u00d7 7 and 8 \u00d7 6 are two of the four slowest facts in the entire
      grid, the 8 times table repays targeted practice more than most. The good news is that the
      rest of it is genuinely straightforward once the doubling chain is automatic.</p>
      <p>A worthwhile exercise is to practise dividing by 8 by halving three times, because it
      shows a child that the table runs both ways. 96 \u00f7 8 \u2192 48 \u2192 24 \u2192 12. Most
      children find that easier than any written method, and it makes the inverse relationship
      concrete rather than theoretical.</p>""",
    related=[(4, "Halve every answer here to get the 4 times table."),
             (2, "Where the doubling chain starts."),
             (7, "Shares 7 \u00d7 8 = 56, the fact most often missed.")],
    faqs=[
        ("What is the 8 times table?",
         "8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96 \u2014 the multiples of 8 up to 8 \u00d7 12."),
        ("What is the easiest way to multiply by 8?",
         "Double the number three times. 8 \u00d7 7 becomes 14, 28, then 56."),
        ("How do you divide by 8 mentally?",
         "Halve three times. 96 \u00f7 8 becomes 48, 24, then 12."),
        ("When is the 8 times table taught?",
         "Year 3 in England, alongside the 3 and 4 times tables, because it follows from doubling the 4s."),
    ],
)

# ------------------------------------------------------------------ 9
_t(
    n=9, year="Year 4", nav="9 times table",
    card="The finger trick, the digit sum of nine, and the tidiest pattern in the grid.",
    seo="The 9 times table \u2014 the finger trick and the digit-sum pattern | Math It!",
    desc="The 9 times table to 9 \u00d7 12, the finger trick explained, why the digits of every multiple add to 9, division facts and free printable practice.",
    keywords="9 times table, nine times table, finger trick, multiples of 9, digit sum 9, 9x table, year 4 times tables",
    intro="""<p>The 9 times table looks intimidating and turns out to be the most pattern-rich in
      the whole grid. It has a finger trick that genuinely works, a digit-sum rule that never
      fails, and a structure so regular you can reconstruct the entire table from first principles
      in a few seconds.</p>
      <p>Because 9 is one less than 10, every fact is simply a ten-times fact with one lot taken
      away. That is the idea underneath all of the patterns below.</p>""",
    patterns=[
        ("The digits of every multiple add to 9",
         """<p>18 \u2192 1 + 8 = 9. 27 \u2192 9. 36 \u2192 9. 45, 54, 63, 72, 81 \u2014 all 9. Past
         99 you may need to add twice: 108 \u2192 9, 171 \u2192 9.</p>
         <p>It is both a memory aid and a divisibility test. Does 9 divide 4\u202f653? 4 + 6 + 5 +
         3 = 18, and 1 + 8 = 9. Yes.</p>"""),
        ("The tens digit is one less than the multiplier",
         """<p>9 \u00d7 7: the tens digit is 6, one less than 7. The units digit must make the pair
         add to 9, so it is 3. Answer 63.</p>
         <p>Those two rules together generate every fact from 9 \u00d7 1 to 9 \u00d7 10 with no
         memorisation at all.</p>"""),
        ("Tens count up while units count down",
         """<p>09, 18, 27, 36, 45, 54, 63, 72, 81, 90. The tens digit climbs 0 to 9 while the units
         digit falls 9 to 0. Written in a column it is strikingly symmetrical, and the second half
         is the first half with the digits reversed: 18 and 81, 27 and 72, 36 and 63.</p>"""),
    ],
    trick=("The finger trick",
           """<p>Hold both hands out, palms down, fingers spread. To find 9 \u00d7 7, count seven
           fingers from the left and fold that one down. Fingers to the left of the folded one give
           the tens (6), fingers to the right give the units (3). Answer: 63.</p>
           <p>It works for every multiplier from 1 to 10, and it works because folding a finger
           physically performs \u201cten lots minus one lot\u201d. Worth saying that out loud \u2014
           a trick that is explained is a trick that transfers; one that is merely performed stops
           working at 9 \u00d7 11.</p>
           <p>For 11 and 12, drop the fingers and subtract: 9 \u00d7 12 = 120 \u2212 12 = 108.</p>"""),
    hardest=[
        ("9 \u00d7 7", "63", "Tens digit is 6 (one less than 7), units must make 9, so 3."),
        ("9 \u00d7 8", "72", "Tens digit 7, units 2. Or 80 \u2212 8."),
        ("9 \u00d7 12", "108", "Past where the finger trick works. Use 120 \u2212 12. Check the digit sum: 1 + 0 + 8 = 9. \u2713"),
    ],
    real=[
        ("Prices ending in 99p", "\u00a39.99 \u00d7 4 is easier as \u00a340 \u2212 4p. The same \u201cone less than ten\u201d idea, applied to money."),
        ("Nine-a-side", "Baseball and rounders field nine. Three teams need 27 players."),
        ("Noughts and crosses", "A 3 \u00d7 3 grid has 9 squares \u2014 and 9 is the square number here."),
        ("Checking arithmetic", "\u2018Casting out nines\u2019 uses the digit-sum rule to check long multiplication. An old method, still a neat trick."),
    ],
    checks=[("9 \u00d7 7", "63"), ("9 \u00d7 8", "72"), ("54 \u00f7 9", "6"), ("9 \u00d7 ? = 108", "12")],
    closing="""<p>The 9 times table is the best illustration of why patterns beat drilling. A child
      who knows the two digit rules can derive any fact in the table faster than most people can
      recall it, and \u2014 crucially \u2014 can tell instantly when an answer is wrong. If the
      digits do not add to 9, it is not a multiple of 9.</p>
      <p>That self-checking property is rare and valuable. It is worth pointing out explicitly that
      the rule comes from 9 being one less than our base, which is also why 99, 999 and 9\u202f999
      behave the same way. Children who see the reason tend to keep the rule.</p>""",
    related=[(3, "Every multiple of 9 is a multiple of 3, and both have digit-sum tests."),
             (10, "Nine is ten minus one \u2014 the source of every pattern on this page."),
             (11, "The other table with an eye-catching digit pattern.")],
    faqs=[
        ("What is the 9 times table?",
         "9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108 \u2014 the multiples of 9 up to 9 \u00d7 12."),
        ("How does the 9 times table finger trick work?",
         "Spread both hands, fold down the finger matching the multiplier. Fingers to its left are the tens, fingers to its right are the units. For 9 \u00d7 7, fold the seventh: 6 left, 3 right, so 63."),
        ("Why do the digits of multiples of 9 add to 9?",
         "Because 9 is one less than 10. Each extra lot of 9 adds one to the tens and takes one from the units, so the digit total never changes."),
        ("Does the finger trick work beyond 9 \u00d7 10?",
         "No \u2014 you run out of fingers. For 9 \u00d7 11 and 9 \u00d7 12, multiply by 10 and subtract one lot: 120 \u2212 12 = 108."),
    ],
)

# ------------------------------------------------------------------ 10
_t(
    n=10, year="Year 2", nav="10 times table",
    card="The place-value table \u2014 and why \u2018add a zero\u2019 is bad advice.",
    seo="The 10 times table \u2014 place value, not adding a zero | Math It!",
    desc="The 10 times table to 10 \u00d7 12, why multiplying by 10 shifts digits rather than adding a zero, division facts and free printable practice.",
    keywords="10 times table, ten times table, multiplying by 10, place value, add a zero, 10x table, year 2 times tables",
    intro="""<p>The 10 times table is the easiest to answer and the most important to understand.
      Every answer is the multiplier with a zero after it, which children spot immediately \u2014
      and that is exactly where the trouble starts.</p>
      <p>\u201cJust add a zero\u201d works for whole numbers and then fails completely. 2.5
      \u00d7 10 is 25, not 2.50. Teaching the place-value version from the beginning saves a lot of
      unpicking in Year 5.</p>""",
    patterns=[
        ("Every answer ends in zero",
         """<p>10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120. The multiplier sits in the tens
         column and the units column is empty.</p>"""),
        ("It is double the 5 times table",
         """<p>5 \u00d7 7 = 35, 10 \u00d7 7 = 70. Conversely, halving a ten-times fact gives the
         five-times one, which is the quickest route into the 5s.</p>"""),
        ("It is the hinge for every other table",
         """<p>9 \u00d7 8 = 80 \u2212 8. 11 \u00d7 8 = 80 + 8. 12 \u00d7 8 = 80 + 16. 5 \u00d7 8 =
         80 \u00f7 2. Vast numbers of mental strategies run through a ten-times fact, which is why
         this table is taught first and practised forever.</p>"""),
    ],
    trick=("Digits move one place to the left",
           """<p>Multiplying by 10 makes every digit ten times bigger, so each one shifts one
           column to the left. The 3 in 3 moves into the tens column to give 30. With whole numbers
           a zero appears in the units column to hold it \u2014 the zero is a <em>consequence</em>,
           not the method.</p>
           <p>Say it as \u201cthe digits move left\u201d from the start. Then 2.5 \u00d7 10 = 25 and
           0.07 \u00d7 10 = 0.7 need no new rule, and dividing by 10 is just the digits moving
           right.</p>"""),
    hardest=[
        ("10 \u00d7 7", "70", "No real difficulty \u2014 but worth checking a child says \u201cseventy\u201d rather than \u201cseven-ty\u201d uncertainly."),
        ("10 \u00d7 12", "120", "The first three-digit answer in the table, which occasionally throws children."),
        ("2.4 \u00d7 10", "24", "The one that actually catches people. Digits move left; 2.40 is wrong."),
    ],
    real=[
        ("Money", "Ten 10p coins make a pound. Pounds and pence are built on tens and hundreds."),
        ("The metric system", "10 mm in a cm, 100 cm in a metre, 1000 m in a km \u2014 all powers of ten."),
        ("Decades", "Ten years. A century is ten decades."),
        ("Place value itself", "Our whole number system groups in tens, which is why this table is the backbone of arithmetic."),
    ],
    checks=[("10 \u00d7 7", "70"), ("10 \u00d7 12", "120"), ("90 \u00f7 10", "9"), ("3.6 \u00d7 10", "36")],
    closing="""<p>The 10 times table is where place value becomes visible, so it is worth spending
      more time on it than its difficulty suggests. Ask a child <em>why</em> 10 \u00d7 6 is 60 and
      you find out quickly whether they understand the number system or have memorised a rule about
      zeros.</p>
      <p>Multiplying and dividing by 10, 100 and 1000 is formally assessed from Year 4 onwards and
      underpins decimals, metric conversion, percentages and standard form. Our
      <a href="../guides/powers-of-ten.html">powers of ten guide</a> takes it further.</p>""",
    related=[(5, "Half of every answer here."),
             (9, "One less lot than ten \u2014 the source of all the nines patterns."),
             (11, "One more lot than ten.")],
    faqs=[
        ("What is the 10 times table?",
         "10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 \u2014 the multiples of 10 up to 10 \u00d7 12."),
        ("Why should I not teach \u2018add a zero\u2019?",
         "Because it fails for decimals. 2.5 \u00d7 10 is 25, not 2.50. Teaching that digits move one place to the left works for every number."),
        ("When is the 10 times table taught?",
         "Year 2 in England, with the 2 and 5 times tables."),
        ("What happens when you divide by 10?",
         "The digits move one place to the right. 70 \u00f7 10 = 7, and 7 \u00f7 10 = 0.7."),
    ],
)

# ------------------------------------------------------------------ 11
_t(
    n=11, year="Year 4", nav="11 times table",
    card="Doubled digits up to 9 \u00d7 11, then the split-and-add trick takes over.",
    seo="The 11 times table \u2014 the repeated-digit pattern and the split trick | Math It!",
    desc="The 11 times table to 11 \u00d7 12, the repeated-digit pattern, the split-and-add method for two-digit numbers, division facts and free printable practice.",
    keywords="11 times table, eleven times table, multiples of 11, 11x table, year 4 times tables, 11 times trick",
    intro="""<p>The 11 times table is the one children learn fastest, because the first nine facts
      simply repeat a digit: 11, 22, 33, 44, 55, 66, 77, 88, 99. It takes about a minute to
      teach.</p>
      <p>Then 11 \u00d7 10 = 110 and the pattern appears to break. It has not \u2014 it has just
      become more interesting, and the rule that replaces it works on numbers far bigger than
      anything in the grid.</p>""",
    patterns=[
        ("Doubled digits up to 9",
         """<p>11 \u00d7 1 through 11 \u00d7 9 give 11, 22, 33, 44, 55, 66, 77, 88, 99. The
         multiplier simply appears twice.</p>"""),
        ("11 \u00d7 11 = 121 is a palindrome",
         """<p>And so are the powers above it for a while: 11\u00b2 = 121, 11\u00b3 = 1331,
         11\u2074 = 14641. Those are the rows of Pascal's triangle, which is a genuinely lovely
         thing to show a curious Year 6.</p>"""),
        ("Every multiple is one more lot than ten times",
         """<p>11 \u00d7 7 = 70 + 7 = 77. 11 \u00d7 12 = 120 + 12 = 132. That is the whole table in
         one rule, and it works for any number at all: 11 \u00d7 46 = 460 + 46 = 506.</p>"""),
    ],
    trick=("Split the digits and drop the sum in the middle",
           """<p>For a two-digit number, separate its digits and put their total between them.
           11 \u00d7 24: split 2 and 4, add them to get 6, giving 2<strong>6</strong>4.
           11 \u00d7 35 \u2192 3, 8, 5 \u2192 385.</p>
           <p>When the middle total reaches 10 or more, carry: 11 \u00d7 87 \u2192 8, 15, 7 \u2192
           carry the 1 into the hundreds \u2192 957. It is a party trick that happens to be real
           arithmetic \u2014 it is exactly what the column method does.</p>"""),
    hardest=[
        ("11 \u00d7 12", "132", "The only fact in the table that children reliably hesitate on. 120 + 12."),
        ("11 \u00d7 11", "121", "The square number. Also the first palindrome in the table."),
        ("11 \u00d7 10", "110", "Easy, but it is where the repeated-digit pattern stops, so it needs saying explicitly."),
    ],
    real=[
        ("A football team", "Eleven players a side, so two teams on the pitch is 22."),
        ("The 11-plus", "Taken in Year 6 in parts of England \u2014 and times tables fluency is assumed throughout it."),
        ("Cricket", "Also eleven a side. A touring squad of three elevens is 33."),
        ("Shoe and clothing sizes", "Adult shoe sizes reach 11 and 12, which is where multipack pricing questions come from."),
    ],
    checks=[("11 \u00d7 8", "88"), ("11 \u00d7 12", "132"), ("121 \u00f7 11", "11"), ("11 \u00d7 ? = 99", "9")],
    closing="""<p>Because the 11 times table is so quick to learn, it is a good place to show
      children that a pattern can have a reason. Multiplying by 11 is multiplying by 10 and then
      adding one more lot, which is why the digit repeats below ten and why the split-and-add trick
      works above it.</p>
      <p>Extending it to two-digit numbers also makes a nice bridge into
      <a href="../guides/long-multiplication.html">long multiplication</a>: the middle digit is
      literally the carry from adding the two partial products. Children who see that connection
      find the column method far less arbitrary.</p>""",
    related=[(10, "One lot fewer \u2014 the basis of every 11 fact."),
             (12, "The other table in the Year 4 pair above ten."),
             (9, "The other table with a striking digit pattern.")],
    faqs=[
        ("What is the 11 times table?",
         "11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132 \u2014 the multiples of 11 up to 11 \u00d7 12."),
        ("What is the trick for multiplying by 11?",
         "Split the digits of a two-digit number and put their sum in the middle. 11 \u00d7 24 gives 2, 6, 4 \u2014 264. Carry if the middle reaches ten."),
        ("Why does the 11 times table repeat digits?",
         "Because 11 \u00d7 n is 10n + n. Below ten that puts the same digit in the tens and the units column."),
        ("When is the 11 times table taught?",
         "Year 4 in England, as part of all tables to 12 \u00d7 12."),
    ],
)

# ------------------------------------------------------------------ 12
_t(
    n=12, year="Year 4", nav="12 times table",
    card="Ten lots plus two lots \u2014 the last table, and the one with the most history.",
    seo="The 12 times table \u2014 the ten-plus-two method and division facts | Math It!",
    desc="The 12 times table to 12 \u00d7 12, the ten-plus-two method, why a dozen matters, its hardest facts and free printable practice.",
    keywords="12 times table, twelve times table, multiples of 12, dozen, 12x table, year 4 times tables, 12 times 12",
    intro="""<p>The 12 times table completes the grid. It is the last one taught and the one that
      finishes the Year 4 expectation of all tables to 12 \u00d7 12 \u2014 which is also what the
      Multiplication Tables Check assesses.</p>
      <p>It looks like the biggest, but it is one of the most derivable: ten lots plus two lots,
      every time. 12 \u00d7 7 = 70 + 14 = 84. A child fluent in the 10s and 2s is already most of
      the way there.</p>""",
    patterns=[
        ("Ten lots plus two lots",
         """<p>12 \u00d7 8 = 80 + 16 = 96. 12 \u00d7 9 = 90 + 18 = 108. The partition into 10 + 2
         is the single most useful idea in the table, and it is the distributive law doing
         real work.</p>"""),
        ("It is double the 6 times table",
         """<p>6 \u00d7 7 = 42, so 12 \u00d7 7 = 84. And it is four times the 3s, and three times
         the 4s \u2014 12 has more factors than any other number in the grid, which is exactly why
         it crops up everywhere.</p>"""),
        ("Even multipliers end in the same digits as the 2 table",
         """<p>12 \u00d7 2 = 24, 12 \u00d7 4 = 48, 12 \u00d7 6 = 72, 12 \u00d7 8 = 96 \u2014 ending
         4, 8, 2, 6, the same five-step cycle as the 4 times table.</p>"""),
    ],
    trick=("Split 12 into 10 and 2",
           """<p>12 \u00d7 anything = (10 \u00d7 it) + (2 \u00d7 it). For 12 \u00d7 6: 60 + 12 = 72.
           For 12 \u00d7 11: 110 + 22 = 132.</p>
           <p>It keeps working past the grid, which is the point. 12 \u00d7 25 = 250 + 50 = 300.
           Children who learn the partition rather than just the twelve facts can multiply by 12 for
           the rest of their lives without thinking about it.</p>"""),
    hardest=[
        ("12 \u00d7 7", "84", "70 + 14. Or double 42 from the 6 times table."),
        ("12 \u00d7 8", "96", "80 + 16. Also 96 is 8 \u00d7 12 \u2014 the same fact approached from the 8s."),
        ("12 \u00d7 12", "144", "A gross. 120 + 24. It is the last fact in the grid and worth knowing cold."),
    ],
    real=[
        ("A dozen", "Eggs, buns, oysters. Three dozen is 36 \u2014 and a gross is 144, twelve dozen."),
        ("Months in a year", "12 \u00d7 \u00a330 a month is \u00a3360 a year. Budget questions are full of twelves."),
        ("Hours on a clock", "Twelve on the dial, twice a day. And 12 \u00d7 60 = 720 minutes in half a day."),
        ("Inches in a foot", "Still used for height and for timber. 5 feet is 60 inches."),
    ],
    checks=[("12 \u00d7 7", "84"), ("12 \u00d7 12", "144"), ("108 \u00f7 12", "9"), ("12 \u00d7 ? = 96", "8")],
    closing="""<p>The question of why we still teach to twelve rather than ten is a fair one. The
      answer is partly historical \u2014 twelve pennies to a shilling, twelve inches to a foot
      \u2014 and partly mathematical: 12 divides by 2, 3, 4 and 6, which makes it enormously
      convenient for splitting things up.</p>
      <p>Practically, the 12 times table is the one that unlocks time and money problems, and
      12 \u00d7 12 = 144 is the final fact in the Year 4 Multiplication Tables Check. Getting it
      secure is the last step in the whole grid \u2014 and from there, every later topic that
      depends on quick multiplication gets easier.</p>""",
    related=[(6, "Halve every answer here to get the 6 times table."),
             (3, "12 is 3 \u00d7 4, so the tables share many answers."),
             (11, "The other above-ten table taught in Year 4.")],
    faqs=[
        ("What is the 12 times table?",
         "12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144 \u2014 the multiples of 12 up to 12 \u00d7 12."),
        ("What is the easiest way to multiply by 12?",
         "Multiply by 10, multiply by 2, then add the two results. 12 \u00d7 7 is 70 + 14 = 84."),
        ("Why do we learn times tables to 12 and not 10?",
         "Partly history \u2014 twelve inches to a foot, twelve pence to a shilling \u2014 and partly because 12 divides by 2, 3, 4 and 6, which makes it very useful for sharing and for time."),
        ("What is 12 \u00d7 12?",
         "144, also called a gross. It is the final fact in the Year 4 Multiplication Tables Check."),
    ],
)

ORDER = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

assert set(ORDER) == set(TABLES), "tables data out of step with ORDER"
for _n in ORDER:
    _d = TABLES[_n]
    for _k in ("year", "nav", "card", "seo", "desc", "keywords", "intro",
               "patterns", "trick", "hardest", "real", "checks", "closing",
               "related", "faqs"):
        assert _d.get(_k), f"table {_n}: missing {_k}"
    for _r, _ in _d["related"]:
        assert _r in TABLES, f"table {_n}: related table {_r} does not exist"
