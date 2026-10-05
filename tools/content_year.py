# -*- coding: utf-8 -*-
"""Renderer for the year-group pages (years/year-<n>.html)."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shell import ad  # noqa: E402
from years_data import YEARS, ORDER  # noqa: E402
from guides_data import BY_SLUG  # noqa: E402

PRE = "../"


def _crumbs(d):
    return f"""    <nav class="breadcrumbs mb-6 flex flex-wrap items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
      <a href="{PRE}index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <a href="{PRE}resources.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Guides</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <span class="font-semibold text-strong" aria-current="page">{d['nav']}</span>
    </nav>"""


def _new(d):
    rows = []
    for h, html in d["new"]:
        rows.append(f"""        <div class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <h3 class="flex items-start gap-2.5 font-display text-lg font-bold text-strong">
            <span class="mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-accent-soft text-xs font-bold text-accent-soft-fg">+</span>
            <span>{h}</span>
          </h3>
          <div class="article mt-2.5 max-w-none text-body">{html}</div>
        </div>""")
    inner = "\n".join(rows)
    prev = d["n"] - 1
    return f"""
      <section id="new" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">What is new since Year {prev}</h2>
        <p class="mt-2 text-body">The parts of Year {d['n']} that are genuinely new, rather than a
        continuation of last year's work.</p>
        <div class="mt-6 grid gap-4">
{inner}
        </div>
      </section>"""


def _strands(d):
    blocks = []
    for strand, bullets in d["strands"]:
        items = "\n".join(
            f"""            <li class="flex gap-3">
              <span class="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-accent-line"></span>
              <span class="text-body">{b}</span>
            </li>""" for b in bullets
        )
        blocks.append(f"""        <div class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <div class="flex items-baseline justify-between gap-3 border-b border-line pb-3">
            <h3 class="font-display text-xl font-bold">{strand}</h3>
            <span class="font-mono text-xs text-faint">{len(bullets)} objectives</span>
          </div>
          <ul class="mt-4 space-y-2.5">
{items}
          </ul>
        </div>""")
    inner = "\n".join(blocks)
    total = sum(len(b) for _, b in d["strands"])
    return f"""
      <section id="objectives" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">What Year {d['n']} covers</h2>
        <p class="mt-2 text-body">{total} objectives, grouped as the national curriculum groups
        them. Paraphrased for parents &mdash; the statutory wording is in the Department for
        Education programmes of study.</p>
        <div class="mt-6 grid gap-4">
{inner}
        </div>
      </section>"""


def _tables(d):
    return f"""
      <section id="tables" class="mt-10 scroll-mt-24">
        <div class="rounded-2xl border-2 border-accent-line bg-accent-soft p-6 sm:p-8">
          <span class="kicker text-accent-soft-fg">Times tables</span>
          <h2 class="mt-2 font-display text-2xl font-bold tracking-tight text-strong sm:text-3xl">The tables expectation in Year {d['n']}</h2>
          <div class="article mt-3 max-w-none text-body">{d['tables']}</div>
          <a href="{PRE}tables.html" class="btn btn-primary mt-5">Open the tables generator</a>
        </div>
      </section>"""


def _sticking(d):
    rows = []
    for problem, fix in d["sticking"]:
        rows.append(f"""          <div class="rounded-xl border border-line bg-surface p-5">
            <p class="flex items-start gap-2.5 font-semibold text-strong">
              <span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-bad-soft text-xs font-bold text-bad-soft-fg">!</span>
              <span>{problem}</span>
            </p>
            <p class="mt-2.5 flex items-start gap-2.5 text-body">
              <span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-accent-soft text-xs font-bold text-accent-soft-fg">&#10003;</span>
              <span>{fix}</span>
            </p>
          </div>""")
    inner = "\n".join(rows)
    return f"""
      <section id="sticking" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Where Year {d['n']} usually sticks</h2>
        <p class="mt-2 text-body">The problems that come up most often at this stage, and what
        actually helps with each.</p>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{inner}
        </div>
      </section>"""


def _settings(d):
    rows = []
    for label, href, why in d["settings"]:
        rows.append(f"""          <a href="{PRE}{href}" class="group flex flex-col rounded-xl border border-line bg-surface p-5 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="font-display text-lg font-bold text-strong group-hover:text-accent-soft-fg">{label}</span>
            <span class="mt-1.5 text-sm text-soft">{why}</span>
            <span class="mt-3 text-sm font-semibold text-accent-text">Open this sheet &rarr;</span>
          </a>""")
    inner = "\n".join(rows)
    return f"""
      <section id="worksheets" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Worksheet settings for Year {d['n']}</h2>
        <p class="mt-2 text-body">Each link opens the generator already configured. Questions are
        different every time, so the same link stays useful all year.</p>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{inner}
        </div>
      </section>"""


def _guides(d):
    rows = []
    for s in d["guides"]:
        g = BY_SLUG[s]
        rows.append(f"""          <a href="{PRE}guides/{s}.html" class="group flex flex-col rounded-xl border border-line bg-surface p-5 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="kicker">{g['cat']}</span>
            <span class="mt-1.5 font-display text-base font-bold text-strong group-hover:text-accent-soft-fg">{g['nav']}</span>
            <span class="mt-1 text-sm text-soft">{g['card']}</span>
          </a>""")
    inner = "\n".join(rows)
    return f"""
      <section id="guides" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Guides for Year {d['n']} topics</h2>
        <p class="mt-2 text-body">Step-by-step explanations of the {len(d['guides'])} topics that
        matter most this year.</p>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{inner}
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
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Questions parents ask</h2>
        <div class="mt-6 grid gap-3">
{items}
        </div>
      </section>"""


def _year_nav(current):
    items = "\n".join(
        f"""          <a href="year-{n}.html" class="flex flex-col rounded-xl border p-4 transition-colors {'border-accent bg-accent-soft' if n == current else 'border-line bg-surface hover:border-accent hover:bg-accent-soft'}">
            <span class="font-display text-lg font-bold text-strong">Year {n}</span>
            <span class="mt-0.5 text-sm text-soft">{YEARS[n]['ages']}</span>
          </a>""" for n in ORDER
    )
    return f"""
      <section class="mt-12">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Other year groups</h2>
        <div class="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-5">
{items}
        </div>
      </section>"""


def _onpage_nav():
    links = [("#new", "What is new"), ("#objectives", "What it covers"),
             ("#tables", "Times tables"), ("#sticking", "Common problems"),
             ("#worksheets", "Worksheet settings"), ("#guides", "Topic guides"),
             ("#faq", "Questions")]
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


def _sidebar_years(current):
    inner = "\n".join(
        f'              <li><a href="year-{n}.html" class="link{" font-bold" if n == current else ""}">Year {n} &mdash; {YEARS[n]["ages"]}</a></li>'
        for n in ORDER
    )
    return f"""          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Every year group</h2>
            <ul class="mt-3 space-y-2 text-sm">
{inner}
            </ul>
          </div>"""


# --------------------------------------------------------------- page body
def body(d):
    n = d["n"]
    total = sum(len(b) for _, b in d["strands"])
    return f"""  <main id="main" class="mx-auto max-w-page px-4 py-8 sm:px-6 lg:px-8">
{_crumbs(d)}

    <div class="grid gap-10 lg:grid-cols-12">
      <article class="lg:col-span-8">
        <span class="kicker">{d['ks']} &middot; {d['ages']}</span>
        <h1 class="mt-2 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.6rem] lg:leading-[1.1]">Year {n} maths: what children learn</h1>
        <div class="mt-4 flex flex-wrap items-center gap-2 text-sm">
          <span class="chip">{d['ks']}</span>
          <span class="chip">{total} objectives</span>
          <span class="chip">England national curriculum</span>
          <a href="{PRE}practice.html?year={n}&amp;level=medium" class="chip hover:border-accent hover:bg-accent-soft hover:text-accent-soft-fg">Year {n} worksheet &rarr;</a>
        </div>

        <div class="article mt-6 max-w-none text-lg">
          {d['intro']}
        </div>

        <div class="mt-8">
          {ad("year-top", size="728 × 90", shape="leaderboard")}
        </div>
{_new(d)}
{_strands(d)}
{_tables(d)}
        <div class="mt-8">
          {ad("year-inarticle", size="728 × 90", shape="leaderboard")}
        </div>
{_sticking(d)}
{_settings(d)}
{_guides(d)}

      <section class="article mt-10 max-w-none">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Assessment and what to focus on</h2>
        {d['closing']}
      </section>
{_faq(d)}
{_year_nav(n)}

        <p class="mt-10 border-t border-line pt-5 text-sm text-soft">
          Objectives summarised from the England national curriculum programmes of study for
          mathematics (Department for Education), paraphrased for parents. Last reviewed by the
          Math It! team. Spotted an error?
          <a href="{PRE}contact.html" class="link">Tell us</a>.
        </p>
      </article>

      <aside class="lg:col-span-4" aria-label="Sidebar">
        <div class="space-y-6 lg:sticky lg:top-24">
{_onpage_nav()}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Year {n} worksheet</h2>
            <p class="mt-1.5 text-sm text-soft">36 questions pitched at Year {n}, marked instantly or printed on one A4 page.</p>
            <a href="{PRE}practice.html?year={n}&amp;level=medium" class="btn btn-primary mt-4 w-full">Make a sheet</a>
            <a href="{PRE}practice.html?year={n}&amp;level=easy" class="btn btn-ghost btn-sm mt-2 w-full">Easier version</a>
          </div>

          {ad("year-sidebar", size="300 × 250", shape="box")}

{_sidebar_years(n)}

          {ad("year-sidebar-bottom", size="300 × 600", shape="tall")}
        </div>
      </aside>
    </div>
  </main>"""


# --------------------------------------------------------------- hub cards
def hub_cards(pre=""):
    out = []
    for n in ORDER:
        d = YEARS[n]
        out.append(f"""          <a href="{pre}years/year-{n}.html" class="group flex items-start gap-4 rounded-xl border border-line bg-surface p-4 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-invert font-mono text-base font-bold text-invert-fg">Y{n}</span>
            <span class="min-w-0">
              <span class="block font-display font-bold text-strong group-hover:text-accent-soft-fg">Year {n}</span>
              <span class="mt-0.5 block text-sm leading-snug text-soft">{d['card']}</span>
            </span>
          </a>""")
    return "\n".join(out)
