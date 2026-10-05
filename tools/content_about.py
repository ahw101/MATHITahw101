# -*- coding: utf-8 -*-
"""The About page: who writes this, how it is checked, how questions are made."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shell import CONTACT_EMAIL, SITE_NAME, ad  # noqa: E402
from guides_data import GUIDES, CATEGORIES  # noqa: E402
from tables_data import ORDER as TABLE_ORDER  # noqa: E402
from years_data import ORDER as YEAR_ORDER  # noqa: E402


def _stat(num, cap):
    return f"""        <div class="rounded-xl border border-line bg-surface p-5 text-center">
          <p class="stat-num">{num}</p>
          <p class="stat-cap mt-1">{cap}</p>
        </div>"""


_STATS = "\n".join([
    _stat(len(GUIDES), "topic guides"),
    _stat(len(TABLE_ORDER), "times table pages"),
    _stat(len(YEAR_ORDER), "year group pages"),
    _stat("0", "questions repeated"),
])


_PRINCIPLES = [
    ("Written for one reader at a time",
     """<p>Every guide is written for a specific person: a parent at a kitchen table at seven in
     the evening, trying to help with homework they last did thirty years ago. That constraint
     decides the structure &mdash; method first, worked examples second, the mistakes we see most
     often third.</p>"""),
    ("Checked against the statutory curriculum",
     """<p>Year-group expectations are taken from the England national curriculum programmes of
     study for mathematics, key stages 1 and 2. We paraphrase rather than quote, and we say which
     year an objective belongs to so you can tell whether something is early, on time or
     overdue.</p>"""),
    ("Arithmetic verified, not assumed",
     """<p>Every worked example on this site has had its arithmetic checked independently of the
     text it sits in. Generated worksheet questions are produced and marked by the same code, so a
     question and its answer cannot disagree.</p>"""),
    ("No filler, no spinning, no scraping",
     """<p>Nothing here is rewritten from another site, assembled from scraped material, or padded
     to hit a word count. Where two pages cover related ground &mdash; the 6 and 12 times tables,
     say &mdash; they say different things, because the useful facts about them genuinely
     differ.</p>"""),
]

_PROCESS = [
    ("Scope", "We decide what the page is for and who needs it, usually from a real question a parent or teacher has asked us."),
    ("Draft", "A subject specialist drafts the method, the worked examples and the misconceptions. AI tools may help with structure, phrasing and first drafts."),
    ("Edit", "Every draft is rewritten by a human editor. In practice very little of a first draft survives: the examples get replaced with better ones, the explanations get shorter, and anything vague gets cut."),
    ("Fact-check", "Arithmetic is recomputed. Curriculum claims are checked against the programmes of study. Anything we cannot verify is removed rather than hedged."),
    ("Publish and revisit", "Pages are reviewed when the curriculum changes, when we spot an error, or when a reader tells us something is unclear."),
]

_FAQS = [
    ("Who writes Math It!?",
     "A small team with classroom and tutoring experience in UK primary maths, working with a qualified editor. We are not a publisher or a tuition company, and nothing here is sponsored content."),
    ("Do you use AI to write the content?",
     "AI tools are used in drafting, in the same way a word processor or a style guide is used. No page is published as a machine draft: everything is rewritten, fact-checked and signed off by a person, and the worked examples and misconceptions come from real teaching experience."),
    ("How are the worksheet questions generated?",
     "By an open piece of JavaScript running in your browser. It picks a topic, builds a question inside the number ranges set for that year and difficulty, and computes the answer at the same moment. Nothing is drawn from a question bank, so sheets are never recycled."),
    ("Is the content copied from anywhere else?",
     "No. Every explanation, example and FAQ on this site was written for it. The national curriculum objectives are paraphrased from the Department for Education's published programmes of study, which is a public document, and we say so on the pages where we use it."),
    ("How do you make money?",
     "Advertising, through Google AdSense. There is no subscription, no paywall and no email capture. Advertisers have no influence over what we publish, and we do not accept paid links or guest posts."),
    ("What if you have made a mistake?",
     f"Tell us and we will fix it. Email {CONTACT_EMAIL} with the page and what is wrong. Corrections to maths errors are made the same week we can verify them."),
]


def _principles():
    rows = "\n".join(f"""        <div class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <h3 class="font-display text-lg font-bold text-strong">{h}</h3>
          <div class="article mt-2.5 max-w-none text-body">{html}</div>
        </div>""" for h, html in _PRINCIPLES)
    return rows


def _process():
    rows = []
    for i, (h, t) in enumerate(_PROCESS, 1):
        rows.append(f"""          <li class="relative pl-12">
            <span class="absolute left-0 top-0 flex h-8 w-8 items-center justify-center rounded-lg bg-invert font-mono text-sm font-bold text-invert-fg">{i}</span>
            <h3 class="font-display text-lg font-bold text-strong">{h}</h3>
            <p class="mt-1.5 text-body">{t}</p>
          </li>""")
    return "\n".join(rows)


def _faqs():
    return "\n".join(f"""          <details class="group rounded-xl border border-line bg-surface px-5 py-4 open:bg-raise">
            <summary class="flex cursor-pointer list-none items-center justify-between gap-4 font-semibold text-strong">
              <span>{q}</span>
              <svg viewBox="0 0 20 20" class="h-5 w-5 shrink-0 text-faint transition-transform group-open:rotate-180" fill="currentColor" aria-hidden="true"><path d="M10 13L4 7h12z"/></svg>
            </summary>
            <div class="mt-3 border-t border-line pt-3 text-body">{a}</div>
          </details>""" for q, a in _FAQS)


FAQS = _FAQS


BODY = f"""  <main id="main">
    <section class="border-b border-line bg-surface">
      <div class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
        <nav class="mb-5 flex items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
          <a href="index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
          <span aria-hidden="true" class="text-faint">/</span>
          <span class="font-semibold text-strong" aria-current="page">About</span>
        </nav>
        <span class="kicker">About</span>
        <h1 class="mt-4 font-display text-4xl font-bold leading-tight sm:text-5xl">About {SITE_NAME}</h1>
        <p class="mt-5 text-lg leading-relaxed text-body">
          Who makes this, how the maths gets checked, and how a worksheet question comes into
          existence. Written out properly, because you are trusting us with a child's homework.
        </p>
      </div>
    </section>

    <div class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid gap-4 sm:grid-cols-4">
{_STATS}
      </div>

      <article class="article mt-12">
        <h2>Why this site exists</h2>
        <p>
          Most free maths worksheets online are PDFs. You download one, your child does it, and the
          next day you need another &mdash; except the only other one at the right level is behind
          a sign-up form, or it is the same sheet with the numbers moved around.
        </p>
        <p>
          {SITE_NAME} generates a new sheet every time you press the button. The questions are
          built in your browser from the year group and difficulty you choose, marked instantly,
          and printed on exactly one side of A4. There is no account, no limit, and no point at
          which it asks for money.
        </p>
        <p>
          Around that generator we have written {len(GUIDES)} topic guides, {len(TABLE_ORDER)}
          times table pages and {len(YEAR_ORDER)} year-group overviews &mdash; because the sheet is
          only half of it. When a child gets stuck on short division, what you need is not another
          worksheet, it is someone explaining where the method goes wrong.
        </p>

        <h2>Who writes it</h2>
        <p>
          {SITE_NAME} is made by a small independent team with classroom and one-to-one tutoring
          experience in UK primary maths, working with an editor who has no maths background
          &mdash; which turns out to be the most useful person in the process. If an explanation
          does not survive contact with someone who has forgotten how long division works, it goes
          back for a rewrite.
        </p>
        <p>
          We are not a publisher, a tuition company or a lead generator for one. Nothing on this
          site is sponsored, and we do not accept paid links, guest posts or product placements in
          the guides.
        </p>
      </article>

      <div class="mt-10">
        {ad("about-inarticle", size="728 × 90", shape="leaderboard")}
      </div>

      <section class="mt-14">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Editorial standards</h2>
        <p class="mt-2 text-body">Four rules that decide what goes on a page and what gets cut.</p>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{_principles()}
        </div>
      </section>

      <section class="mt-14">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">How a page gets made</h2>
        <p class="mt-2 text-body">The same five steps for every guide, every table page and every
        year overview.</p>
        <ol class="mt-6 space-y-6">
{_process()}
        </ol>
      </section>

      <section class="mt-14">
        <div class="rounded-2xl border-2 border-accent-line bg-accent-soft p-6 sm:p-8">
          <span class="kicker text-accent-soft-fg">Methodology</span>
          <h2 class="mt-2 font-display text-2xl font-bold tracking-tight text-strong sm:text-3xl">How the questions are generated</h2>
          <div class="article mt-3 max-w-none text-body">
            <p>
              Every question is built in your browser by a generator we wrote, not pulled from a
              bank of pre-written sums. When you choose a year group and a difficulty, the
              generator does four things:
            </p>
            <ol>
              <li>Picks a topic from the set appropriate to that year &mdash; 34 topics are
              available, from number bonds to ratio and simple algebra.</li>
              <li>Chooses the numbers inside the range set for that year and level, with rules that
              keep the question sensible: no division that does not resolve, no subtraction that
              goes negative unless negatives are the topic.</li>
              <li>Computes the answer at the same moment it builds the question, from the same
              values, so the two cannot drift apart.</li>
              <li>Renders the question and keeps the answer aside until you ask to mark the sheet.</li>
            </ol>
            <p>
              Sheets are identified by a seed number, printed in the header. Enter the same seed and
              you get the same sheet back &mdash; useful for a class set, or for marking a sheet a
              week later. Everything happens on your device; no answers are sent anywhere.
            </p>
          </div>
        </div>
      </section>

      <section class="mt-14">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">What is on the site</h2>
        <div class="mt-6 grid gap-4 sm:grid-cols-3">
          <div class="rounded-xl border border-line bg-surface p-5">
            <h3 class="font-display text-lg font-bold">Generators</h3>
            <p class="mt-1.5 text-sm text-soft">Two of them &mdash; a mixed arithmetic worksheet
            generator covering Years 2 to 6, and a times tables generator covering any table from
            1 to 100.</p>
            <a href="practice.html" class="link mt-3 inline-block text-sm">Open the generator</a>
          </div>
          <div class="rounded-xl border border-line bg-surface p-5">
            <h3 class="font-display text-lg font-bold">{len(GUIDES)} topic guides</h3>
            <p class="mt-1.5 text-sm text-soft">Across {len(CATEGORIES)} categories, from place
            value to statistics. Method, worked examples, misconceptions and an FAQ on every
            one.</p>
            <a href="resources.html" class="link mt-3 inline-block text-sm">Browse the guides</a>
          </div>
          <div class="rounded-xl border border-line bg-surface p-5">
            <h3 class="font-display text-lg font-bold">Reference sheets</h3>
            <p class="mt-1.5 text-sm text-soft">Printable A4 wall charts &mdash; times tables grid,
            fraction equivalents, metric conversions and number facts. Each one fits a single
            page.</p>
            <a href="resources.html#downloads" class="link mt-3 inline-block text-sm">See the downloads</a>
          </div>
        </div>
      </section>

      <section class="mt-14">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Questions about this site</h2>
        <div class="mt-6 grid gap-3">
{_faqs()}
        </div>
      </section>

      <section class="mt-14 overflow-hidden rounded-2xl bg-invert p-7 text-invert-fg sm:p-9">
        <span class="kicker text-invert-soft">Found a problem?</span>
        <h2 class="mt-2 font-display text-2xl font-bold tracking-tight sm:text-3xl">Tell us and we will fix it</h2>
        <p class="mt-2.5 max-w-xl text-invert-soft">
          A wrong answer, an explanation that does not land, a question pitched at the wrong year
          &mdash; all of it is worth reporting. Corrections are made as soon as we can verify them.
        </p>
        <div class="mt-6 flex flex-wrap gap-3">
          <a href="contact.html" class="btn btn-lg bg-canvas text-strong hover:bg-raise">Contact us</a>
          <a href="privacy.html" class="btn btn-lg border border-invert-soft/40 text-invert-fg hover:bg-white/10">Privacy &amp; cookies</a>
        </div>
      </section>
    </div>
  </main>"""
