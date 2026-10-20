# Learning log

One entry per session, newest first. Takes 5 minutes and pays off: the recall questions open the next session, and the log shows your progress over the months.

**Template** (copy for each day):

```markdown
## YYYY-MM-DD · Week W, day D · Project PNN
**Recall (from memory, before checking):**
1. Q: ... → A: ...
2. Q: ... → A: ...
3. Q: ... → A: ...

**Did:** tasks completed, checkpoints passed
**Confused by:** what didn't click (bring this to Claude)
**Questions for tomorrow:**
1.
2.
3.
```

---

## 2026-10-18 · Week 0, day 0 (bonus Sunday, 90 min) · Project P02

**Recall:** first session, so nothing to recall yet.

**Today's tasks (90-minute version of the daily block):**
| Time | Block | Task |
|---|---|---|
| 0:00 – 0:05 | Setup | Open the P02 notebook, *Run All*, confirm 11 ⏳, open the Jupyter Variables window |
| 0:05 – 0:35 | Learn | Watch lecture #3 (link at the top of the notebook). Pause before each result and predict it |
| 0:35 – 1:15 | Build | Task 1.1 and Task 1.2, until both checkpoints show ✅. Write your prediction in Task 1.2 *before* simulating |
| 1:15 – 1:30 | Ship | Write a sentence under your Task 1.2 histogram, commit (don't push yet), fill in this entry |

**Did: watched the lecture #3 "How to Make & Lose Money Trading" and completed the tasks 1.1. and 1.2.**
**Confused by: histogram binning, keyword arguments and rng**
**Questions for tomorrow:**
1. How do you print the number of heads and tails in a coin flip simulation?
2. How do you set the random seed in numpy to ensure reproducibility?
3. How do you interpret the histogram of returns in Task 1.2?

---

## 2026-10-19 · Week 1, day 1 · Project P02

**Recall (from memory, before checking):**
1. Q: How do you print the number of heads and tails in a coin flip simulation? → A:
2. Q: How do you set the random seed in numpy to ensure reproducibility? → A:
3. Q: How do you interpret the histogram of p̂ in Task 1.2? → A:
4. Bonus: If I want to halve the standard error of my win-rate estimate, how many more trades do I need, and why? → A:

**Today's tasks:**
| Time | Block | Task |
|---|---|---|
| 0:00 – 0:10 | Recall | Answer the 4 questions above from memory, then check them |
| 0:10 – 0:20 | Leftovers | Centred bins, legend, delete the dead `raise`, one-sentence interpretation under the histogram |
| 0:20 – 1:20 | Build | Task 1.3 (standard error vs n, log-log plot, `n_needed`) + its ✍️ interpretation |
| 1:20 – 1:45 | Build | Task 2.1 (`estimate_p_nonstationary`), if time allows |
| 1:45 – 2:00 | Ship | Commit, fill in below |

**Did:**
**Confused by:**
**Questions for tomorrow:**
1.
2.
3.

---

## 2026-10-20 · Week 1, day 2 · Project P02

**Recall (from memory, before checking):**
1. Q: Why can't more data push the error of p̂ (vs 0.5) below 0.1 when p_true moves? Which term of the law of total variance is responsible? → A:
2. Q: A strategy wins +115 or loses −150. What win rate does it need to break even, and how do you derive it? → A:
3. Q: Why does the edge from the law of total expectation equal the plain average P/L? → A:

**Today's tasks:**
| Time | Block | Task |
|---|---|---|
| 0:00 – 0:10 | Recall | Answer the 3 questions above from memory, then check |
| 0:10 – 0:15 | Catch-up | Fill in yesterday's *Did / Confused by*, then commit your Task 3.1–3.2 work |
| 0:15 – 1:00 | Build | Task 3.3 (1,000 simulated years; **predict the losing-year share first**) and Task 3.4 (Beta posterior) + the Part 3 ✍️ answer |
| 1:00 – 1:45 | Build | Task 4.1 (SPY edge decomposition) and Task 4.2 (bootstrap CI) |
| 1:45 – 2:00 | Ship | Commit, fill in below. Task 4.3 + leftovers (Task 1.2 bins/legend, Task 1.3 numbers) go to tomorrow |

**Did:**
**Confused by:**
**Questions for tomorrow:**
1.
2.
3.
