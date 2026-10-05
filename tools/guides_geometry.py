# -*- coding: utf-8 -*-
"""Guides: Shape and geometry."""

CAT = "Shape & geometry"

GUIDES = [

# ---------------------------------------------------------------- shapes
dict(
    slug="2d-and-3d-shapes", cat=CAT, nav="2D and 3D shapes", read=6,
    h1="2D and 3D shapes and their properties",
    card="Name them, count faces, edges and vertices, and sort them by the properties that matter.",
    years="Years 1\u20136",
    seo="2D and 3D shapes explained \u2014 properties, faces, edges and vertices | Math It!",
    desc="The 2D and 3D shapes primary children need to name, how to count faces, edges and vertices, what makes a polygon regular, and the quadrilateral family tree.",
    keywords="2d shapes, 3d shapes, faces edges vertices, properties of shapes, quadrilaterals, regular polygons, KS2 shape, year 5 shape",
    intro="""<p>Shape work at primary is mostly vocabulary and careful looking. The maths is not hard;
      the difficulty is that children are asked to sort shapes by properties they have never had
      named for them, and to distinguish between words that sound similar.</p>
      <p>Get the vocabulary precise and the rest follows. A square really is a rectangle, and
      knowing why is the point of the whole topic.</p>""",
    steps=[
        ("Count sides to name a polygon",
         "<p>3 triangle, 4 quadrilateral, 5 pentagon, 6 hexagon, 7 heptagon, 8 octagon, "
         "9 nonagon, 10 decagon. A polygon is any closed shape made of straight sides.</p>"),
        ("Regular means all sides and all angles equal",
         "<p>A regular hexagon has six equal sides and six equal angles. An irregular hexagon still "
         "has six sides \u2014 it is just not uniform. \u201cRegular\u201d is not a synonym for "
         "\u201cordinary\u201d.</p>"),
        ("For 3D shapes, count faces, edges and vertices",
         "<p>A <strong>face</strong> is a flat surface, an <strong>edge</strong> is where two faces "
         "meet, a <strong>vertex</strong> is a corner where edges meet. A cube has 6 faces, "
         "12 edges and 8 vertices.</p>"),
        ("Use a net to see a solid flat",
         "<p>Unfolding a 3D shape into its net makes the faces countable and is the standard way "
         "SATs asks about solids. A cube has eleven different possible nets.</p>"),
        ("Classify triangles two ways",
         "<p>By sides: equilateral (3 equal), isosceles (2 equal), scalene (none equal). By "
         "angles: right-angled, acute, obtuse. A triangle can be described by both at once.</p>"),
    ],
    examples=[
        ("How many faces, edges and vertices has a square-based pyramid?",
         ["Faces: 1 square base + 4 triangles = 5.",
          "Edges: 4 round the base + 4 rising to the apex = 8.",
          "Vertices: 4 at the base + 1 apex = 5."],
         "5 faces, 8 edges, 5 vertices"),
        ("Is a square a rectangle?",
         ["A rectangle is a quadrilateral with four right angles.",
          "A square has four right angles.",
          "It also happens to have four equal sides, which is an extra property, not a disqualifying one."],
         "Yes \u2014 every square is a rectangle"),
        ("Name a 3D shape with 2 faces, 1 edge and 1 vertex.",
         ["Curved surface plus a flat circular base.",
          "One circular edge where they meet, one point at the top."],
         "A cone"),
        ("A triangle has angles of 90\u00b0, 45\u00b0 and 45\u00b0. Describe it fully.",
         ["One angle is 90\u00b0, so it is right-angled.",
          "Two angles are equal, so two sides are equal."],
         "A right-angled isosceles triangle"),
    ],
    mistakes=[
        ("Saying a square is not a rectangle.",
         "It is. A square meets every condition for a rectangle and adds one more. Classification in maths is inclusive, not exclusive."),
        ("Counting a cylinder as having three faces.",
         "UK primary convention is 2 flat faces plus 1 curved surface, 2 edges and 0 vertices. Schools vary slightly on whether the curved surface counts as a face \u2014 follow the one your school uses."),
        ("Thinking \u2018regular\u2019 just means a normal shape.",
         "Regular has a precise meaning: all sides equal <em>and</em> all angles equal."),
        ("Mixing up a rhombus and a parallelogram.",
         "A rhombus is a parallelogram with four equal sides. Every rhombus is a parallelogram; not every parallelogram is a rhombus."),
    ],
    sections=[
        ("The quadrilateral family",
         """<p>Quadrilaterals nest inside one another, which is why \u201cwhich of these is a
         rectangle?\u201d questions trip children up:</p>
         <ul>
           <li><strong>Trapezium</strong> \u2014 at least one pair of parallel sides.</li>
           <li><strong>Parallelogram</strong> \u2014 two pairs of parallel sides.</li>
           <li><strong>Rhombus</strong> \u2014 a parallelogram with four equal sides.</li>
           <li><strong>Rectangle</strong> \u2014 a parallelogram with four right angles.</li>
           <li><strong>Square</strong> \u2014 both a rhombus and a rectangle.</li>
           <li><strong>Kite</strong> \u2014 two pairs of adjacent equal sides.</li>
         </ul>
         <p>A square sits at the bottom of the tree, inheriting every property above it.</p>"""),
        ("Faces, edges and vertices worth memorising",
         """<table>
           <thead><tr><th>Solid</th><th>Faces</th><th>Edges</th><th>Vertices</th></tr></thead>
           <tbody>
             <tr><td>Cube</td><td>6</td><td>12</td><td>8</td></tr>
             <tr><td>Cuboid</td><td>6</td><td>12</td><td>8</td></tr>
             <tr><td>Triangular prism</td><td>5</td><td>9</td><td>6</td></tr>
             <tr><td>Square-based pyramid</td><td>5</td><td>8</td><td>5</td></tr>
             <tr><td>Triangular pyramid (tetrahedron)</td><td>4</td><td>6</td><td>4</td></tr>
             <tr><td>Cylinder</td><td>2 + curved</td><td>2</td><td>0</td></tr>
             <tr><td>Cone</td><td>1 + curved</td><td>1</td><td>1</td></tr>
             <tr><td>Sphere</td><td>curved only</td><td>0</td><td>0</td></tr>
           </tbody>
         </table>
         <p>For every solid with flat faces, faces + vertices \u2212 edges = 2. A cube: 6 + 8 \u2212
         12 = 2. That is Euler's formula, and it makes a good self-check.</p>"""),
        ("Symmetry",
         """<p>A line of symmetry is a fold line where both halves match exactly. A square has
         four, a rectangle two, an equilateral triangle three, a regular hexagon six \u2014 a regular
         polygon always has as many lines of symmetry as it has sides.</p>
         <p>A circle has infinitely many. A scalene triangle and a general parallelogram have
         none, which surprises children who assume every tidy-looking shape must be
         symmetrical.</p>"""),
    ],
    faqs=[
        ("Is a square a rectangle?",
         "Yes. A rectangle is a quadrilateral with four right angles, and a square has four right angles plus four equal sides."),
        ("What is the difference between a face and a side?",
         "\u2018Side\u2019 belongs to 2D shapes \u2014 a straight edge of a polygon. \u2018Face\u2019 belongs to 3D shapes \u2014 a flat surface."),
        ("Does a cylinder have 2 or 3 faces?",
         "UK primary usually counts 2 flat faces and 1 curved surface. Some schemes say 3 faces. Both are defensible; follow your school's wording."),
        ("How many lines of symmetry has a regular polygon?",
         "The same number as it has sides. A regular pentagon has five, a regular octagon eight."),
    ],
    cta=("Practise shape and measures questions", "practice.html?year=5&level=medium&topics=area-perimeter,measures"),
    related=["angles", "perimeter-and-area", "coordinates-and-translation", "volume-and-capacity"],
),

# ---------------------------------------------------------------- angles
dict(
    slug="angles", cat=CAT, nav="Angles", read=6,
    h1="Angles: measuring, estimating and calculating",
    card="Acute, obtuse and reflex, using a protractor, and the angle facts that solve most questions.",
    years="Years 3\u20136",
    seo="Angles explained \u2014 types, protractors and angle facts | Math It!",
    desc="How to classify angles, measure them with a protractor without reading the wrong scale, and use the angle facts on a line, round a point and in triangles.",
    keywords="angles, types of angles, acute obtuse reflex, using a protractor, angles in a triangle, angles on a straight line, KS2 angles, year 6 angles",
    intro="""<p>An angle measures turn, not length. Two lines meeting at 40\u00b0 make the same angle
      whether they are 2 cm or 2 metres long \u2014 a point children find genuinely counter-intuitive
      the first time they meet a diagram drawn out of scale.</p>
      <p>Angles are measured in degrees. A full turn is 360\u00b0, a quarter turn is the right angle
      at 90\u00b0, and almost every angle question at primary is solved by one of four facts.</p>""",
    steps=[
        ("Learn the four names",
         "<p><strong>Acute</strong> is less than 90\u00b0. <strong>Right</strong> is exactly "
         "90\u00b0. <strong>Obtuse</strong> is between 90\u00b0 and 180\u00b0. "
         "<strong>Reflex</strong> is more than 180\u00b0. A straight line is 180\u00b0.</p>"),
        ("Estimate before you measure",
         "<p>Decide whether the angle is bigger or smaller than a right angle first. That tells "
         "you which protractor scale to read and catches the commonest error before it "
         "happens.</p>"),
        ("Line the protractor up properly",
         "<p>Centre hole exactly on the vertex, zero line exactly along one arm. If either is out, "
         "every reading afterwards is wrong.</p>"),
        ("Read the scale that starts at zero",
         "<p>A protractor has two scales running opposite ways. Follow the one where your starting "
         "arm reads 0, not 180.</p>"),
        ("Use the angle facts instead of measuring",
         "<p>Angles on a straight line total 180\u00b0. Angles round a point total 360\u00b0. Angles "
         "in a triangle total 180\u00b0. Angles in a quadrilateral total 360\u00b0. Most exam "
         "questions are solved by subtraction from one of these.</p>"),
    ],
    examples=[
        ("Two angles on a straight line. One is 47\u00b0. Find the other.",
         ["Angles on a straight line add to 180\u00b0.",
          "180 \u2212 47."],
         "133\u00b0"),
        ("A triangle has angles of 65\u00b0 and 48\u00b0. Find the third.",
         ["Angles in a triangle add to 180\u00b0.",
          "65 + 48 = 113.",
          "180 \u2212 113."],
         "67\u00b0"),
        ("Three angles meet at a point: 120\u00b0, 95\u00b0 and x. Find x.",
         ["Angles round a point add to 360\u00b0.",
          "120 + 95 = 215.",
          "360 \u2212 215."],
         "145\u00b0"),
        ("An isosceles triangle has one angle of 40\u00b0 between its two equal sides. Find the others.",
         ["The two base angles are equal.",
          "180 \u2212 40 = 140 left to share between them.",
          "140 \u00f7 2."],
         "70\u00b0 and 70\u00b0"),
    ],
    mistakes=[
        ("Reading the wrong protractor scale, giving 133\u00b0 instead of 47\u00b0.",
         "Estimate first. If the angle is clearly less than a right angle, an answer above 90\u00b0 is wrong \u2014 you read the outer scale instead of the inner one."),
        ("Thinking longer arms make a bigger angle.",
         "An angle measures turn only. Extending the arms changes nothing."),
        ("Assuming a diagram is drawn to scale.",
         "Unless it says so, it is not. Use the given numbers and the angle facts, never a ruler or a protractor on a printed exam diagram."),
        ("Forgetting that a reflex angle and its partner add to 360\u00b0.",
         "If the inner angle is 110\u00b0, the reflex angle outside it is 360 \u2212 110 = 250\u00b0."),
    ],
    sections=[
        ("The four facts that solve almost everything",
         """<ul>
           <li>Angles on a <strong>straight line</strong> add to 180\u00b0.</li>
           <li>Angles <strong>round a point</strong> add to 360\u00b0.</li>
           <li>Angles in a <strong>triangle</strong> add to 180\u00b0.</li>
           <li>Angles in a <strong>quadrilateral</strong> add to 360\u00b0.</li>
         </ul>
         <p>Vertically opposite angles \u2014 the pair across an X crossing \u2014 are equal, which
         follows from the straight-line fact. Between them these five cover the whole of KS2 and
         most of early KS3.</p>"""),
        ("Why a triangle is always 180\u00b0",
         """<p>Tear the three corners off a paper triangle and place them edge to edge. They always
         form a straight line. Any triangle, every time.</p>
         <p>It is one of the few primary facts with a demonstration a child can do themselves in
         thirty seconds, and it sticks far better than being told. A quadrilateral is 360\u00b0 for
         a related reason: any quadrilateral splits into two triangles.</p>"""),
        ("Angles and turns",
         """<p>Angle also describes rotation, which is where it meets compass directions and clock
         faces:</p>
         <ul>
           <li>Quarter turn = 90\u00b0, half turn = 180\u00b0, three-quarter turn = 270\u00b0,
           full turn = 360\u00b0.</li>
           <li>A clock's minute hand turns 360\u00b0 in an hour, so 6\u00b0 a minute.</li>
           <li>The hour hand turns 30\u00b0 an hour \u2014 the gap between two numbers.</li>
         </ul>
         <p>\u201cWhat is the angle between the hands at 3 o'clock?\u201d is 90\u00b0, and it is a
         favourite reasoning question precisely because it joins two topics.</p>"""),
    ],
    faqs=[
        ("What are the types of angle?",
         "Acute (under 90\u00b0), right (exactly 90\u00b0), obtuse (90\u00b0 to 180\u00b0), straight (180\u00b0) and reflex (over 180\u00b0)."),
        ("How do I stop reading the wrong protractor scale?",
         "Estimate whether the angle is acute or obtuse before you read it, and always follow the scale on which your starting arm reads zero."),
        ("Do angles in every triangle add to 180 degrees?",
         "Yes, for every flat triangle, whatever its shape or size."),
        ("When do children learn to use a protractor?",
         "Year 5 in England \u2014 drawing and measuring angles to the nearest degree. Year 4 compares and orders angles without measuring."),
    ],
    cta=("Practise reasoning and measures", "practice.html?year=6&level=medium&topics=measures,area-perimeter"),
    related=["2d-and-3d-shapes", "coordinates-and-translation", "perimeter-and-area", "telling-the-time"],
),

# ---------------------------------------------------------------- coordinates
dict(
    slug="coordinates-and-translation", cat=CAT, nav="Coordinates and translation", read=5,
    h1="Coordinates, translation and reflection",
    card="Along the corridor then up the stairs \u2014 plotting points and moving shapes about.",
    years="Years 4\u20136",
    seo="Coordinates explained \u2014 four quadrants, translation and reflection | Math It!",
    desc="How to read and plot coordinates in all four quadrants, translate a shape by a given vector, and reflect it in an axis without losing track of the signs.",
    keywords="coordinates, four quadrants, plotting points, translation, reflection, x and y axis, KS2 coordinates, year 6 coordinates",
    intro="""<p>Coordinates give every point on a grid a unique address: a pair of numbers in
      brackets, x first and y second. The point (3, 5) means three across and five up from the
      origin at (0, 0).</p>
      <p>The order is not negotiable, and getting it backwards is the single biggest source of lost
      marks in the topic. The standard mnemonic is <strong>along the corridor, then up the
      stairs</strong>.</p>""",
    steps=[
        ("Read x first, then y",
         "<p>(3, 5) is 3 along the horizontal x-axis and 5 up the vertical y-axis. Alphabetical "
         "order helps: x comes before y.</p>"),
        ("Start every reading at the origin",
         "<p>(0, 0) is where the axes cross. All coordinates are measured from there.</p>"),
        ("Count grid lines, not squares",
         "<p>Points sit on the intersections of the lines, not inside the boxes. Counting squares "
         "gives an answer one out.</p>"),
        ("Handle four quadrants with signs",
         "<p>Right and up are positive; left and down are negative. So (\u22124, 2) is four left "
         "and two up, and (\u22123, \u22125) is three left and five down.</p>"),
        ("Translate by adding to the coordinates",
         "<p>\u201c3 right and 2 down\u201d adds 3 to every x and subtracts 2 from every y. "
         "(5, 7) becomes (8, 5). The shape never changes size or orientation.</p>"),
        ("Reflect by flipping one sign",
         "<p>Reflecting in the y-axis negates x: (4, 3) \u2192 (\u22124, 3). Reflecting in the "
         "x-axis negates y: (4, 3) \u2192 (4, \u22123).</p>"),
    ],
    examples=[
        ("A square has corners at (2, 1), (6, 1) and (6, 5). Where is the fourth?",
         ["Three corners are known; the fourth sits opposite (6, 1).",
          "It shares its x with (2, 1), so x = 2.",
          "It shares its y with (6, 5), so y = 5."],
         "(2, 5)"),
        ("Translate the point (5, 7) by 3 right and 2 down.",
         ["Right adds to x: 5 + 3 = 8.",
          "Down subtracts from y: 7 \u2212 2 = 5."],
         "(8, 5)"),
        ("Reflect (\u22123, 4) in the y-axis.",
         ["Reflecting in the y-axis changes the sign of x only.",
          "\u22123 becomes 3; y stays as 4."],
         "(3, 4)"),
        ("A rectangle has corners (1, 2), (1, 6), (7, 6), (7, 2). What is its area?",
         ["Width: from x = 1 to x = 7 is 6 units.",
          "Height: from y = 2 to y = 6 is 4 units.",
          "6 \u00d7 4."],
         "24 square units"),
    ],
    mistakes=[
        ("Reading (3, 5) as 3 up and 5 across.",
         "x always comes first. Along the corridor, then up the stairs \u2014 and x is before y in the alphabet."),
        ("Counting squares rather than lines.",
         "Points lie on the intersections of grid lines. Counting the squares between them gives a value one too small."),
        ("Translating left or down by adding.",
         "Left and down are negative directions, so they subtract. Only right and up add."),
        ("Reflecting in the x-axis by changing x.",
         "Reflecting in the x-axis flips the shape vertically, so it is the <em>y</em> coordinate that changes sign."),
    ],
    sections=[
        ("The four quadrants",
         """<p>Extending the axes in both directions gives four regions, numbered anticlockwise
         from the top right:</p>
         <ul>
           <li><strong>First</strong> \u2014 x positive, y positive: (4, 3)</li>
           <li><strong>Second</strong> \u2014 x negative, y positive: (\u22124, 3)</li>
           <li><strong>Third</strong> \u2014 both negative: (\u22124, \u22123)</li>
           <li><strong>Fourth</strong> \u2014 x positive, y negative: (4, \u22123)</li>
         </ul>
         <p>Year 4 works in the first quadrant only. All four arrive in Year 6, which is also where
         negative numbers need to be secure \u2014 the two topics reinforce one another.</p>"""),
        ("Translation keeps everything but position",
         """<p>Translating a shape slides it. Lengths, angles, area and orientation are all
         unchanged \u2014 only the position moves. That is why you can translate by simply adding
         the same pair of numbers to every vertex.</p>
         <p>A useful check: after translating, the shape should look identical and sit the same way
         up. If it has flipped, you have reflected it by mistake.</p>"""),
        ("Where this is heading",
         """<p>Coordinates are the bridge between number and shape, and they lead directly into
         graphs at secondary. Plotting y = 2x + 1 is exactly the same skill: generate pairs of
         numbers, plot them, join them up.</p>
         <p>Children who are fluent with the four quadrants in Year 6 find straight-line graphs in
         Year 7 almost free, which makes this a topic worth over-practising.</p>"""),
    ],
    faqs=[
        ("Which number comes first in a coordinate pair?",
         "The x coordinate, which is the horizontal one. Along the corridor, then up the stairs."),
        ("What is the origin?",
         "The point (0, 0) where the two axes cross. Every coordinate is measured from it."),
        ("What is the difference between translation and reflection?",
         "Translation slides a shape without turning or flipping it. Reflection produces a mirror image across a line."),
        ("When are the four quadrants taught?",
         "Year 6 in England. Year 4 introduces coordinates in the first quadrant only."),
    ],
    cta=("Practise reasoning and negative numbers", "practice.html?year=6&level=medium&topics=negatives,sequences"),
    related=["negative-numbers", "2d-and-3d-shapes", "angles", "number-sequences"],
),

]
