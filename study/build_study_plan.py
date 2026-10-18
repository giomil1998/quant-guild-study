"""Builds study/Study_Plan.pdf. Edit the content below and re-run:

    .venv/bin/python study/build_study_plan.py
"""

from datetime import date, timedelta
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

OUT = Path(__file__).with_name("Study_Plan.pdf")
START = date(2026, 10, 19)  # Monday of week 1

ACCENT = colors.HexColor("#2a6fdb")
ACCENT_LIGHT = colors.HexColor("#e8f0fc")
INK = colors.HexColor("#1f2328")
MUTED = colors.HexColor("#5b6470")
RULE = colors.HexColor("#d0d7de")
WARM = colors.HexColor("#fff4e0")

# macOS system fonts: the PDF built-ins lack arrows, check marks and boxes
FONT_DIR = "/System/Library/Fonts/Supplemental/"
for name, file in [("Body", "Arial.ttf"), ("Body-Bold", "Arial Bold.ttf"), ("Body-Italic", "Arial Italic.ttf"),
                   ("Body-BoldItalic", "Arial Bold Italic.ttf"), ("Sym", "Arial Unicode.ttf")]:
    pdfmetrics.registerFont(TTFont(name, FONT_DIR + file))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic")


def sym(text):
    for ch in "✓☐":
        text = text.replace(ch, f"<font name='Sym'>{ch}</font>")
    return text


ss = getSampleStyleSheet()
S = {
    "title": ParagraphStyle("t", parent=ss["Title"], fontName="Body-Bold", fontSize=28, leading=34, textColor=INK, alignment=TA_LEFT, spaceAfter=6),
    "subtitle": ParagraphStyle("st", fontName="Body", fontSize=13, leading=18, textColor=MUTED, spaceAfter=18),
    "h1": ParagraphStyle("h1", fontName="Body-Bold", fontSize=17, leading=22, textColor=ACCENT, spaceBefore=6, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="Body-Bold", fontSize=12.5, leading=16, textColor=INK, spaceBefore=10, spaceAfter=4),
    "body": ParagraphStyle("b", fontName="Body", fontSize=10, leading=14.5, textColor=INK, spaceAfter=6),
    "small": ParagraphStyle("s", fontName="Body", fontSize=8.5, leading=11.5, textColor=INK),
    "smallb": ParagraphStyle("sb", fontName="Body-Bold", fontSize=8.5, leading=11.5, textColor=colors.white),
    "muted": ParagraphStyle("m", fontName="Body-Italic", fontSize=9, leading=12.5, textColor=MUTED, spaceAfter=6),
    "code": ParagraphStyle("c", fontName="Courier", fontSize=8.8, leading=12, textColor=INK, backColor=colors.HexColor("#f6f8fa"), borderPadding=(5, 6, 5, 6), spaceBefore=4, spaceAfter=8),
    "bullet": ParagraphStyle("bl", fontName="Body", fontSize=10, leading=14.5, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=2),
}


def P(text, style="body"):
    return Paragraph(sym(text), S[style])


def bullets(items):
    return [Paragraph(i, S["bullet"], bulletText="•") for i in items]


def table(rows, widths, header=True, zebra=True, valign="TOP"):
    data = [[c if not isinstance(c, str) else Paragraph(sym(c), S["smallb"] if header and r == 0 else S["small"]) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), ACCENT)]
    if zebra:
        for r in range(1 if header else 0, len(rows)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0, r), (-1, r), colors.HexColor("#f6f8fa")))
    t.setStyle(TableStyle(style))
    return t


def callout(text, bg=ACCENT_LIGHT):
    t = Table([[Paragraph(sym(text), S["body"])]], colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 10),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return t


def week_dates(n):
    mon = START + timedelta(weeks=n - 1)
    sat = mon + timedelta(days=5)
    return f"{mon:%d %b} – {sat:%d %b}"


# ------------------------------------------------------------------ content
PHASES = [
    ("Phase 1 · Edge, randomness and ruin", "What an edge is, how to measure it, and why bet size decides whether you survive it.", [
        (1, "P02 · Statistics problems in trading", "3", "Estimation error, non-stationarity, decomposing an edge. <i>Extension:</i> SPY's edge with a bootstrap confidence interval.", "4"),
        (2, "P03 · Gambler's ruin", "28, 26", "Ruin probability: formula vs simulation. <i>Extension:</i> ruin risk of a leveraged SPY / EUR/USD strategy.", "34"),
        (3, "P04 · Kelly, ergodicity, volatility drag", "36, 81, 136", "Growth-optimal sizing, time vs ensemble averages. <i>Extension:</i> Kelly leverage on SPY, full vs half Kelly.", "46, 60"),
    ], "M1 · 4 projects live, profile README published, repo pinned"),
    ("Phase 2 · Probability and simulation toolkit", "The Monte Carlo and stochastic-process tools every later module uses.", [
        (4, "P05 · Monte Carlo foundations", "1, 33, 61", "Inverse transform, law of large numbers, CLT, error bars on simulations.", "2"),
        (5, "P06 · Brownian motion and GBM vs reality", "59, 135, 29", "Simulate ABM/GBM, Itô's lemma. <i>Extension:</i> calibrate GBM to SPY & EUR/USD and test it against fat tails (QQ plots).", "31, 37"),
        (6, "P07 · Jumps and clustering", "82, 94", "Poisson and Hawkes processes. <i>Extension:</i> fit them to the arrival times of large-move days.", "71, 49"),
    ], None),
    ("Phase 3 · Measuring performance and backtesting honestly", "How to tell skill from luck, and why most backtests lie.", [
        (7, "P08 · Sharpe, CAGR, luck vs skill", "101, 125, 48, 96", "Sharpe ratio confidence intervals, deflated Sharpe, minimum track-record length.", "112"),
        (8, "P09 · Backtesting honestly", "97, 77, 93", "A small walk-forward backtester with costs; a demonstration of overfitting.", "58, 118"),
        (9, "Review and consolidation", "—", "Move reusable code into <font face='Courier'>qgs</font>, rewrite the README, mid-point portfolio review with Claude.", "—"),
        (10, "Holiday buffer", "—", "Catch up on unfinished tasks, or rest. Both count.", "—"),
    ], "M2 · 8 projects live, helpers refactored, README case-study style"),
    ("Phase 4 · Option pricing", "Black-Scholes from several angles, then beyond it.", [
        (11, "P10 · Black-Scholes three ways", "83, 19, 73", "Closed form, Monte Carlo, risk-neutral argument; convergence and error.", "18, 6, 67"),
        (12, "P11 · Finite differences and exotics", "38, 32", "Explicit / implicit / Crank-Nicolson; barrier and Asian options.", "—"),
        (13, "P12 · Heston and FFT pricing", "39, 89", "Carr-Madan FFT; the smile Heston generates; implied-vol inversion.", "107"),
    ], None),
    ("Phase 5 · Trading options and volatility (your home ground)", "Where your FX options research gives you an edge over most portfolios.", [
        (14, "P13 · Delta hedging and Greeks P&amp;L", "9, 11", "Hedging error vs rebalancing frequency; gamma/theta P&amp;L attribution.", "7"),
        (15, "P14 · Implied-vol surface from free data", "30, 23", "Build SPY's IV surface from yfinance chains: smile, skew, term structure.", "24"),
        (16, "P15 · Volatility risk premium", "119, 43", "VIX-implied vs realised SPY variance since 1990; implied-vol crush around earnings.", "106, 113"),
    ], "M3 · 15 projects; options section is the portfolio's centrepiece"),
    ("Phase 6 · Time series and portfolios", "Volatility models, regimes and portfolio construction.", [
        (17, "P16 · GARCH and regimes", "44, 47, 51", "GARCH on EUR/USD; hidden Markov regimes on SPY.", "92"),
        (18, "P17 · Portfolio construction", "20, 100, 17", "Why mean-variance is unstable; Black-Litterman; PCA on ETF returns.", "78, 128"),
    ], None),
    ("Capstone", "One original project that ties the pieces together and shows how you think.", [
        (19, "Capstone: design and build", "your choice", "Ideas: FX vs equity volatility risk premium · Kalman-filter mean reversion (95) · tail-risk hedging (126, 138).", "—"),
        (20, "Capstone: finish and write up", "—", "Polished notebook, README case study, short LinkedIn/blog post.", "—"),
    ], "M4 · Capstone published; portfolio ready to show recruiters"),
]

story = []

# --------------------------------------------------------------- cover
story += [
    Spacer(1, 30 * mm),
    P("Quant Guild Study Plan", "title"),
    P(f"20 weeks · 2 hours a day · 6 days a week · starts Monday {START:%d %B %Y}", "subtitle"),
    callout("<b>Goal.</b> By March 2027, a public GitHub portfolio of ~16 quant finance projects plus one original capstone, "
            "each rebuilt from first principles on free data. Along the way: fluency in simulation, option pricing, "
            "volatility modelling and honest backtesting."),
    Spacer(1, 10 * mm),
    P("What's inside", "h2"),
    *bullets([
        "1 · How you'll learn: the method",
        "2 · The daily 2-hour block and the weekly rhythm",
        "3 · Tools: PyCharm, Jupyter and git",
        "4 · Using Claude as your teacher",
        "5 · The 20-week plan",
        "6 · Definition of done and milestone tracker",
    ]),
    Spacer(1, 10 * mm),
    P("Repo: github.com/giomil1998/quant-guild-study · Source lectures: Quant Guild Library by Roman Paolucci", "muted"),
    PageBreak(),
]

# --------------------------------------------------------------- method
story += [
    P("1 · How you'll learn: the method", "h1"),
    P("Watching lectures feels productive but leaves little behind. Skill comes from <b>producing</b> things: "
      "predicting, coding, getting it wrong, and explaining. Every session in this plan is built on five rules."),
    table([
        ["Rule", "What it means in practice"],
        ["<b>1. Predict before you run</b>", "Before executing a cell, write one line: what do I expect to see? Being wrong is the moment learning happens."],
        ["<b>2. Type it, never paste it</b>", "Rebuild every idea from a blank cell. If you copy code from the original notebook, close it and redo it from memory."],
        ["<b>3. Struggle for 15 minutes, then climb the hint ladder</b>", "Docs → print/inspect variables → simplify the problem → ask Claude for a <i>hint</i> (not the answer) → only then look at a solution."],
        ["<b>4. Explain it in writing</b>", "Every result gets a markdown cell in your own words. If you can't explain a chart, you don't understand it yet."],
        ["<b>5. Recall beats re-reading</b>", "Start each day by answering yesterday's three questions <i>from memory</i>. Recall is what makes things stick."],
    ], [52 * mm, 118 * mm]),
    Spacer(1, 6),
    P("How each project is structured", "h2"),
    P("From project 02 on, you get a <b>starter notebook</b>: the story, the maths and a sequence of tasks with empty cells. "
      "After each task there is a <b>checkpoint cell</b> that tests your answer and prints ✓ or a hint, so you always know where you stand. "
      "When all tasks pass you add your own extension, write takeaways, and ask for a review."),
    table([
        ["Stage", "You do", "Time"],
        ["Learn", "Watch the lecture; pause and predict; take notes in your words", "~1 session"],
        ["Build", "Work through the tasks in the starter notebook until every checkpoint passes", "~3 sessions"],
        ["Extend", "One idea of your own, ideally on real data", "~1 session"],
        ["Ship", "Takeaways, review with Claude, update the README and ROADMAP, push", "~1 session"],
    ], [25 * mm, 115 * mm, 30 * mm]),
    PageBreak(),
]

# --------------------------------------------------------------- daily / weekly
story += [
    P("2 · The daily 2-hour block", "h1"),
    P("Same structure every day, so no time goes on deciding what to do. Use a timer."),
    table([
        ["Time", "Block", "What you do"],
        ["0:00 – 0:10", "<b>Recall</b>", "Answer yesterday's 3 questions from memory in LEARNING_LOG.md. Check yourself afterwards."],
        ["0:10 – 0:40", "<b>Learn</b>", "Lecture segment or reading. Pause before each result and predict it. Notes go into the notebook's markdown."],
        ["0:40 – 1:40", "<b>Build</b>", "Next task(s) in the starter notebook. Predict → type → run → fix. Phone in another room."],
        ["1:40 – 1:55", "<b>Explain</b>", "Write the interpretation cell for what you built. One-sentence takeaway."],
        ["1:55 – 2:00", "<b>Ship</b>", "Commit and push. Log entry: what I did, what confused me, 3 questions for tomorrow."],
    ], [25 * mm, 22 * mm, 123 * mm]),
    Spacer(1, 10),
    P("The weekly rhythm", "h2"),
    table([
        ["Day", "Focus"],
        ["Mon", "Learn the week's lecture(s) + first build task"],
        ["Tue – Thu", "Build: work through the tasks and checkpoints"],
        ["Fri", "Extension on real data + takeaways; ask Claude for a review"],
        ["Sat", "Portfolio day: fix review comments, update README/ROADMAP, push. Then watch the week's <i>study</i> lectures (no build needed)"],
        ["Sun", "Rest. Optional: 20-minute quiz with Claude on the week's material"],
    ], [25 * mm, 145 * mm]),
    Spacer(1, 10),
    callout("<b>Fell behind?</b> Don't skip ahead and don't try to double up. Shorten the extension, ship what you have, "
            "and use the next buffer week. A shipped 80% project teaches more than an abandoned perfect one.", WARM),
    PageBreak(),
]

# --------------------------------------------------------------- tools
story += [
    P("3 · Tools: PyCharm, Jupyter and git", "h1"),
    P("<b>Recommendation:</b> use PyCharm for everything, since you already know it. Its notebook support gives you the inline charts, "
      "plus autocomplete, a variable viewer and a real debugger. If your PyCharm asks for a paid plan to run notebooks, use JupyterLab "
      "in the browser for the notebooks and keep PyCharm for the <font face='Courier'>.py</font> files and git."),
    P("One-time setup in PyCharm", "h2"),
    *bullets([
        "<b>File → Open</b> → <font face='Courier'>~/projects/quant-guild-study</font>",
        "<b>Settings → Project → Python Interpreter → Add Interpreter → Add Local → Select existing</b> → <font face='Courier'>.venv/bin/python</font>",
        "Open <font face='Courier'>notebooks/02_.../*.ipynb</font>. Run a cell with <b>Shift+Enter</b>. Choose the <b>.venv</b> interpreter if PyCharm asks for a kernel.",
        "Turn on the <b>Jupyter Variables</b> tool window: watching arrays change is the fastest way to debug.",
    ]),
    P("JupyterLab fallback (Terminal)", "h2"),
    P("cd ~/projects/quant-guild-study<br/>source .venv/bin/activate<br/>jupyter lab", "code"),
    P("The git loop: commit daily, it's your progress diary", "h2"),
    P("In PyCharm: <b>Cmd+K</b> to commit (tick the files, write a message) and <b>Cmd+Shift+K</b> to push. In the terminal:", "body"),
    P("git status &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# what changed?<br/>"
      "git add -A<br/>"
      "git commit -m \"P02: task 3, edge decomposition\"<br/>"
      "git push", "code"),
    P("A steady run of daily commits on your GitHub profile is itself a signal recruiters notice.", "muted"),
    P("Where code lives", "h2"),
    table([
        ["Location", "Put here"],
        ["<font face='Courier'>notebooks/NN_topic/</font>", "The project: story, maths, code, charts, takeaways"],
        ["<font face='Courier'>src/qgs/</font>", "Functions you reuse in 2+ projects (data loading, metrics, simulators). Edit these as .py files in PyCharm"],
        ["<font face='Courier'>study/</font>", "This plan and LEARNING_LOG.md"],
    ], [48 * mm, 122 * mm]),
    PageBreak(),
]

# --------------------------------------------------------------- claude
story += [
    P("4 · Using Claude as your teacher", "h1"),
    P("Open a Claude Code session in the project folder. These prompts cover almost everything you'll need:"),
    table([
        ["When", "Say"],
        ["Start of a session", "<i>\"Start my session: week 1, day 2.\"</i> → you get today's tasks and the 3 recall questions"],
        ["Stuck", "<i>\"I'm stuck on P02 task 3. Here's my code and the error. Give me a hint, not the answer.\"</i>"],
        ["Concept unclear", "<i>\"Explain the law of total expectation simply, then give me a 10-minute exercise.\"</i>"],
        ["Finished a project", "<i>\"Review my P02 notebook like a quant interviewer. Be strict.\"</i>"],
        ["New starter notebook", "<i>\"I've finished P02. Set up P03 for me.\"</i>"],
        ["Sunday quiz", "<i>\"Quiz me on this week's material: 5 questions, one at a time.\"</i>"],
        ["Off-track", "<i>\"I've missed 3 days. Re-plan the rest of this phase.\"</i>"],
    ], [38 * mm, 132 * mm]),
    Spacer(1, 8),
    callout("<b>The deal:</b> I write the starter notebooks, checkpoints, hints and reviews. "
            "<b>You write every line of project code.</b> If you ask for a full solution, I'll first ask what you've tried. "
            "Bypassing the struggle only cheats your future self."),
    PageBreak(),
]

# --------------------------------------------------------------- plan
story.append(P("5 · The 20-week plan", "h1"))
story.append(P("<b>Build</b> = full portfolio project with a starter notebook. <b>Study</b> = watch, plus an optional 20-minute scratch exercise; no portfolio entry. Numbers are Quant Guild lecture numbers (see ROADMAP.md for links).", "muted"))
for name, blurb, weeks, milestone in PHASES:
    rows = [["Wk", "Dates", "Build project", "Lectures", "Focus", "Study"]]
    for wk, proj, lec, focus, study in weeks:
        rows.append([f"<b>{wk}</b>", week_dates(wk), f"<b>{proj}</b>", lec, focus, study])
    block = [P(name, "h2"), P(blurb, "muted"), table(rows, [9 * mm, 24 * mm, 38 * mm, 18 * mm, 66 * mm, 15 * mm])]
    if milestone:
        block += [Spacer(1, 4), callout(f"<b>Milestone</b> {milestone}", WARM)]
    block.append(Spacer(1, 6))
    story.append(KeepTogether(block))

story += [
    KeepTogether([
        P("After week 20", "h2"),
        P("Module 8 (machine learning and market making: lectures 13, 16, 35, 63, 65, 69) and the remaining lectures in ROADMAP.md, "
          "at your own pace. By then you'll know the workflow well enough to plan it yourself."),
    ]),
    Spacer(1, 10),
]

# --------------------------------------------------------------- done + tracker
story += [
    P("6 · Definition of done", "h1"),
    P("A project counts as shipped only when every box is ticked. This is what makes it portfolio-grade rather than homework."),
    table([
        ["✓", "Check"],
        ["☐", "All checkpoint cells pass; the notebook runs top-to-bottom on a fresh kernel (<i>Restart &amp; Run All</i>)"],
        ["☐", "Opening cell: the question, a credit link to the lecture, a 'what's new vs the original' table"],
        ["☐", "Every chart has a title, axis labels, and a markdown cell interpreting it"],
        ["☐", "At least one extension on real free data, or a rigorous test the original lacks"],
        ["☐", "Takeaways section in your own words (3–5 points)"],
        ["☐", "Review by Claude done and comments addressed"],
        ["☐", "README project table + ROADMAP status updated; committed and pushed with outputs saved"],
    ], [10 * mm, 160 * mm]),
    Spacer(1, 12),
    P("Milestone tracker", "h2"),
    table([
        ["", "Milestone", "Target", "Done on"],
        ["☐", "<b>M1</b> · 4 projects live, profile README, repo pinned", week_dates(3).split(" – ")[1], ""],
        ["☐", "<b>M2</b> · 8 projects, helpers refactored, README rewritten", week_dates(9).split(" – ")[1], ""],
        ["☐", "<b>M3</b> · 15 projects, options section complete", week_dates(16).split(" – ")[1], ""],
        ["☐", "<b>M4</b> · Capstone published, portfolio ready for recruiters", week_dates(20).split(" – ")[1], ""],
    ], [10 * mm, 110 * mm, 25 * mm, 25 * mm]),
    Spacer(1, 12),
    P("Skills you'll be able to show at the end", "h2"),
    table([
        ["Area", "Skills"],
        ["Python", "Vectorised NumPy/pandas, clean plotting, reusable modules, git workflow, reproducible notebooks"],
        ["Probability", "Monte Carlo with error bars, stochastic processes (BM, GBM, Poisson, Hawkes), Itô calculus intuition"],
        ["Options", "BS / MC / PDE / FFT pricing, Greeks and hedging P&amp;L, implied-vol surfaces, volatility risk premium"],
        ["Statistics", "Estimation error, non-stationarity, bootstrap, Sharpe inference, GARCH, HMMs"],
        ["Research", "Honest backtesting, luck-vs-skill tests, written communication of results"],
    ], [30 * mm, 140 * mm]),
]


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Body", 8)
    canvas.setFillColor(MUTED)
    if doc.page > 1:
        canvas.drawString(20 * mm, 12 * mm, "Quant Guild Study Plan")
        canvas.drawRightString(190 * mm, 12 * mm, f"{doc.page}")
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(3)
    canvas.line(0, A4[1] - 1.5, A4[0], A4[1] - 1.5)
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
                        title="Quant Guild Study Plan")
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("wrote", OUT)
