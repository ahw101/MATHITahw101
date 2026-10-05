# -*- coding: utf-8 -*-
"""Renderer for the individual times table pages (tables/<n>-times-table.html)."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shell import ad  # noqa: E402
from tables_data import TABLES, ORDER  # noqa: E402

PRE = "../"


def _crumbs(d):
    return f"""    <nav class="breadcrumbs mb-6 flex flex-wrap items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
      <a href="{PRE}index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <a href="{PRE}tables.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Times tables</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <span class="font-semibold text-strong" aria-current="page">{d['nav']}</span>
    </nav>"""


def _grid(n):
    """The table itself, 1 to 12, as a readable two-column list."""
    cells = []
    for i in range(1, 13):
        cells.append(
            f"""          <li class="flex items-baseline justify-between gap-3 rounded-lg border border-line bg-surface px-4 py-2.5">
            <span class="font-mono text-base text-body">{n} &times; {i}</span>
            <span class="font-mono text-lg font-bold text-strong">{n * i}</span>
          </li>"""
        )
    inner = "\n".join(cells)
    return f"""
      <section id="table" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">The {n} times table in full</h2>
        <p class="mt-2 text-body">Every fact from {n} &times; 1 to {n} &times; 12. Read it down the
        column once, then cover the answers and work back up &mdash; recall beats re-reading.</p>
        <ul class="mt-5 grid gap-2 sm:grid-cols-2">
{inner}
        </ul>
      </section>"""


def _division(n):
    rows = "\n".join(
        f"""            <tr>
              <td class="py-1.5 font-mono">{n * i} &divide; {n} = {i}</td>
              <td class="py-1.5 font-mono">{n * i} &divide; {i} = {n}</td>
            </tr>"""
        for i in range(1, 13)
    )
    return f"""
      <section id="division" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Division facts</h2>
        <p class="mt-2 text-body">Every multiplication fact is two division facts. A child who knows
        {n} &times; 7 but stalls on {n * 7} &divide; {n} has learnt the table in one direction only
        &mdash; which is exactly the gap that shows up later in fractions and simplifying.</p>
        <div class="article mt-5 max-w-none overflow-x-auto">
          <table class="w-full text-sm">
            <thead><tr><th class="text-left">Divide by {n}</th><th class="text-left">Divide by the other factor</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </section>"""


def _patterns(d):
    out = []
    for i, (h, html) in enumerate(d["patterns"], 1):
        out.append(f"""        <div class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <div class="flex items-start gap-3">
            <span class="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-lg bg-invert font-mono text-xs font-bold text-invert-fg">{i}</span>
            <h3 class="font-display text-lg font-bold text-strong">{h}</h3>
          </div>
          <div class="article mt-3 max-w-none text-body">{html}</div>
        </div>""")
    inner = "\n".join(out)
    return f"""
      <section id="patterns" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Patterns in the {d['n']} times table</h2>
        <div class="mt-6 grid gap-4">
{inner}
        </div>
      </section>"""


def _trick(d):
    h, html = d["trick"]
    return f"""
      <section id="trick" class="mt-10 scroll-mt-24">
        <div class="rounded-2xl border-2 border-accent-line bg-accent-soft p-6 sm:p-8">
          <span class="kicker text-accent-soft-fg">The fastest route</span>
          <h2 class="mt-2 font-display text-2xl font-bold tracking-tight text-strong sm:text-3xl">{h}</h2>
          <div class="article mt-3 max-w-none text-body">{html}</div>
        </div>
      </section>"""


def _hardest(d):
    rows = []
    for fact, ans, help_ in d["hardest"]:
        rows.append(f"""          <div class="rounded-xl border border-line bg-surface p-5">
            <p class="flex items-baseline gap-3">
              <span class="font-mono text-lg font-bold text-strong">{fact}</span>
              <span class="font-mono text-lg font-bold text-accent-text">= {ans}</span>
            </p>
            <p class="mt-2 text-body">{help_}</p>
          </div>""")
    inner = "\n".join(rows)
    return f"""
      <section id="hardest" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">The facts that stick</h2>
        <p class="mt-2 text-body">Not every fact needs the same amount of practice. These are the
        ones that slow children down in the {d['n']} times table, and what to do about each.</p>
        <div class="mt-6 grid gap-4">
{inner}
        </div>
      </section>"""


def _square(n):
    return f"""
      <section class="mt-10">
        <div class="flex flex-col gap-5 rounded-2xl border border-line bg-raise p-6 sm:flex-row sm:items-center sm:p-8">
          <div class="shrink-0 text-center">
            <p class="font-mono text-4xl font-bold text-strong">{n * n}</p>
            <p class="stat-cap mt-1">{n} squared</p>
          </div>
          <div class="text-body">
            <h2 class="font-display text-xl font-bold text-strong">{n} &times; {n} = {n * n}</h2>
            <p class="mt-2">The square number in this table. It is the area of a square with sides of
            {n} cm, and the one fact here that reappears in Year 6 work on
            <a href="{PRE}guides/square-cube-numbers.html" class="link">square and cube numbers</a> and
            in <a href="{PRE}guides/perimeter-and-area.html" class="link">area</a> questions.</p>
          </div>
        </div>
      </section>"""


def _real(d):
    rows = "\n".join(
        f"""          <li class="flex gap-3 rounded-xl border border-line bg-surface p-4">
            <span class="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-accent"></span>
            <span><strong class="font-semibold text-strong">{w}.</strong> <span class="text-body">{t}</span></span>
          </li>"""
        for w, t in d["real"]
    )
    return f"""
      <section id="real" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Where the {d['n']} times table turns up</h2>
        <p class="mt-2 text-body">Tables learnt in context are recalled faster than tables learnt as
        a list. These are the places a child will actually meet multiples of {d['n']}.</p>
        <ul class="mt-5 grid gap-3 sm:grid-cols-2">
{rows}
        </ul>
      </section>"""


def _checks(d):
    n = d["n"]
    items = "\n".join(
        f"""          <li class="rounded-xl border border-line bg-surface p-4 text-center">
            <p class="font-mono text-lg font-bold text-strong">{q}</p>
            <details class="mt-2">
              <summary class="cursor-pointer list-none text-sm text-soft hover:text-accent-text">Show answer</summary>
              <p class="mt-1.5 font-mono text-lg font-bold text-accent-text">{a}</p>
            </details>
          </li>"""
        for q, a in d["checks"]
    )
    return f"""
      <section id="check" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Quick check</h2>
        <p class="mt-2 text-body">Four questions, out of order, including a division and a missing
        number. If all four come back inside about ten seconds, the {n} times table is secure.</p>
        <ul class="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
{items}
        </ul>
        <p class="mt-4 text-sm text-soft">If not, generate a sheet below &mdash; the questions are
        different every time, so there is nothing to memorise except the facts themselves.</p>
      </section>"""


def _cta(n):
    return f"""
      <section class="mt-10 overflow-hidden rounded-2xl bg-invert p-7 text-invert-fg sm:p-9">
        <span class="kicker text-invert-soft">Practise it</span>
        <h2 class="mt-2 font-display text-2xl font-bold tracking-tight sm:text-3xl">Make a {n} times table worksheet</h2>
        <p class="mt-2.5 max-w-xl text-invert-soft">
          A fresh sheet of {n} times table questions, marked in the browser or printed on one clean
          A4 page. Switch to division or missing numbers with one click.
        </p>
        <div class="mt-6 flex flex-wrap gap-3">
          <a href="{PRE}tables.html?tables={n}&amp;ops=mul" class="btn btn-lg bg-canvas text-strong hover:bg-raise">Multiplication sheet</a>
          <a href="{PRE}tables.html?tables={n}&amp;ops=div" class="btn btn-lg border border-invert-soft/40 text-invert-fg hover:bg-white/10">Division sheet</a>
          <a href="{PRE}tables.html?tables={n}&amp;ops=missing" class="btn btn-lg border border-invert-soft/40 text-invert-fg hover:bg-white/10">Missing numbers</a>
        </div>
      </section>"""


def _faq(d):
    items = "\n".join(f"""          <details class="group rounded-xl border border-line bg-surface px-5 py-4 open:bg-raise">
            <summary class="flex cursor-pointer list-none items-center justify-between gap-4 font-semibold text-strong">
              <span>{q}</span>
              <svg viewBox="0 0 20 20" class="h-5 w-5 shrink-0 text-faint transition-transform group-open:rotate-180" fill="currentColor" aria-hidden="true"><path d="M10 13L4 7h12z"/></svg>
            </summary>
            <div class="mt-3 border-t border-line pt-3 text-body">{a}</div>
          </details>""" for q, a in d["faqs"])
    return f"""
      <section id="faq" class="mt-12 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Questions people ask</h2>
        <div class="mt-6 grid gap-3">
{items}
        </div>
      </section>"""


def _related(d):
    out = []
    for n, why in d["related"]:
        o = TABLES[n]
        out.append(f"""          <a href="{n}-times-table.html" class="group flex flex-col rounded-xl border border-line bg-surface p-5 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="kicker">{o['year']}</span>
            <span class="mt-1.5 font-display text-lg font-bold text-strong group-hover:text-accent-soft-fg">{o['nav']}</span>
            <span class="mt-1 text-sm text-soft">{why}</span>
          </a>""")
    inner = "\n".join(out)
    return f"""
      <section class="mt-12">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Tables that go with it</h2>
        <div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
{inner}
        </div>
      </section>"""


def _all_tables_nav(current):
    chips = "\n".join(
        f'              <li><a href="{n}-times-table.html" class="chip{" border-accent bg-accent-soft text-accent-soft-fg" if n == current else " hover:border-accent hover:bg-accent-soft"}"{" aria-current=&quot;page&quot;" if n == current else ""}>{n}&times;</a></li>'
        for n in ORDER
    )
    return f"""          <nav class="card p-5" aria-label="All times tables">
            <h2 class="font-display text-lg font-bold">Every table</h2>
            <ul class="mt-3 flex flex-wrap gap-2">
{chips}
            </ul>
          </nav>"""


def _onpage_nav():
    links = [("#table", "The full table"), ("#patterns", "Patterns"),
             ("#trick", "The fastest route"), ("#hardest", "Hard facts"),
             ("#division", "Division facts"), ("#real", "In real life"),
             ("#check", "Quick check"), ("#faq", "Questions")]
    inner = "\n".join(
        f'            <li><a href="{h}" class="block rounded-md px-3 py-1.5 text-sm text-soft transition-colors hover:bg-accent-soft hover:text-accent-soft-fg">{t}</a></li>'
        for h, t in links
    )
    return f"""          <nav class="card p-4" aria-label="On this page">
            <h2 class="label px-3">On this page</h2>
            <ul class="mt-1.5">
{inner}
            </ul>
          </nav>"""


# --------------------------------------------------------------- page body
def body(d):
    n = d["n"]
    return f"""  <main id="main" class="mx-auto max-w-page px-4 py-8 sm:px-6 lg:px-8">
{_crumbs(d)}

    <div class="grid gap-10 lg:grid-cols-12">
      <article class="lg:col-span-8">
        <span class="kicker">Times tables &middot; {d['year']}</span>
        <h1 class="mt-2 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.6rem] lg:leading-[1.1]">The {n} times table</h1>
        <div class="mt-4 flex flex-wrap items-center gap-2 text-sm">
          <span class="chip">{d['year']}</span>
          <span class="chip">12 facts</span>
          <span class="chip">{n} &times; {n} = {n * n}</span>
          <a href="{PRE}tables.html?tables={n}&amp;ops=mul" class="chip hover:border-accent hover:bg-accent-soft hover:text-accent-soft-fg">Practise this &rarr;</a>
        </div>

        <div class="article mt-6 max-w-none text-lg">
          {d['intro']}
        </div>

        <div class="mt-8">
          {ad("table-top", size="728 × 90", shape="leaderboard")}
        </div>
{_grid(n)}
{_patterns(d)}
{_trick(d)}
        <div class="mt-8">
          {ad("table-inarticle", size="728 × 90", shape="leaderboard")}
        </div>
{_hardest(d)}
{_division(n)}
{_square(n)}
{_real(d)}

      <section class="article mt-10 max-w-none">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Getting it secure</h2>
        {d['closing']}
      </section>
{_checks(d)}
{_cta(n)}
{_faq(d)}
{_related(d)}

        <p class="mt-10 border-t border-line pt-5 text-sm text-soft">
          Written by the Math It! team against the England national curriculum programmes of study
          for mathematics. Spotted a mistake?
          <a href="{PRE}contact.html" class="link">Tell us</a> and we will fix it.
        </p>
      </article>

      <aside class="lg:col-span-4" aria-label="Sidebar">
        <div class="space-y-6 lg:sticky lg:top-24">
{_onpage_nav()}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Worksheet in one click</h2>
            <p class="mt-1.5 text-sm text-soft">Fresh {n} times table questions, marked instantly or printed on one A4 page.</p>
            <a href="{PRE}tables.html?tables={n}&amp;ops=mul" class="btn btn-primary mt-4 w-full">Make a sheet</a>
            <a href="{PRE}tables.html?tables={n}&amp;ops=both" class="btn btn-ghost btn-sm mt-2 w-full">Mixed &times; and &divide;</a>
          </div>

          {ad("table-sidebar", size="300 × 250", shape="box")}

{_all_tables_nav(n)}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Related guides</h2>
            <ul class="mt-3 space-y-2 text-sm">
              <li><a href="{PRE}guides/times-tables.html" class="link">Learning times tables</a></li>
              <li><a href="{PRE}guides/short-division.html" class="link">Short division</a></li>
              <li><a href="{PRE}guides/factors-multiples-primes.html" class="link">Factors, multiples and primes</a></li>
              <li><a href="{PRE}guides/square-cube-numbers.html" class="link">Square and cube numbers</a></li>
            </ul>
          </div>

          {ad("table-sidebar-bottom", size="300 × 600", shape="tall")}
        </div>
      </aside>
    </div>
  </main>"""


# --------------------------------------------------------------- hub cards
def hub_cards(pre=""):
    """Grid of links to every individual table page."""
    out = []
    for n in ORDER:
        d = TABLES[n]
        out.append(f"""          <a href="{pre}tables/{n}-times-table.html" class="group flex items-start gap-4 rounded-xl border border-line bg-surface p-4 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-invert font-mono text-base font-bold text-invert-fg">{n}&times;</span>
            <span class="min-w-0">
              <span class="block font-display font-bold text-strong group-hover:text-accent-soft-fg">{d['nav']}</span>
              <span class="mt-0.5 block text-sm leading-snug text-soft">{d['card']}</span>
            </span>
          </a>""")
    return "\n".join(out)
