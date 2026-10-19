"""Checkpoints for project 02: statistics problems in trading."""

import numpy as np
from scipy import stats

from qgs.checks import call, close, is_todo, report, scalars, todo


def task1_1(estimate_p):
    name = "Task 1.1 estimate_p"
    rng = np.random.default_rng(0)
    out, err = call(estimate_p, 10, 0.5, rng)
    if err == "todo":
        return todo(name)
    if err:
        return report(name, False, err)
    if not (0 <= out <= 1) or not np.isclose(out * 10, round(out * 10)):
        return report(name, False, f"estimate_p(10, 0.5, rng) returned {out!r}",
                      "it should return the fraction of heads, a multiple of 1/10 between 0 and 1")
    many = [estimate_p(50, 0.3, rng) for _ in range(4000)]
    if not close(np.mean(many), 0.3, 0.01):
        return report(name, False, f"with p = 0.3 the average estimate is {np.mean(many):.3f}",
                      "a flip is heads with probability p; check you pass p through to the random draw")
    return report(name, True, "unbiased estimator of p")


def task1_2(p_hats_10):
    name = "Task 1.2 sampling distribution"
    if is_todo(p_hats_10):
        return todo(name)
    x = np.asarray(p_hats_10, dtype=float)
    if len(x) != 10_000:
        return report(name, False, f"expected 10,000 estimates, got {len(x)}")
    sd_theory = np.sqrt(0.25 / 10)
    if not close(x.std(), sd_theory, 0.01):
        return report(name, False, f"sd of estimates is {x.std():.3f}, theory says {sd_theory:.3f}",
                      "each estimate should use 10 flips of a fair coin")
    return report(name, True, f"sd = {x.std():.3f} vs theory {sd_theory:.3f}: 10 trades tell you almost nothing")


def task1_3(se_empirical, n_needed, ns=(10, 30, 100, 300, 1000, 3000)):
    name = "Task 1.3 standard error vs n"
    if is_todo(se_empirical) or is_todo(n_needed):
        return todo(name)
    se = np.asarray(se_empirical, dtype=float)
    theory = np.sqrt(0.25 / np.asarray(ns))
    if len(se) != len(ns) or np.max(np.abs(se / theory - 1)) > 0.1:
        return report(name, False, "se_empirical doesn't match sqrt(p(1-p)/n) within 10%",
                      "one empirical sd per n in ns, each from ~2,000 simulated estimates")
    target = (1.96 * 0.5 / 0.02) ** 2
    if not close(n_needed, target, 100):
        return report(name, False, f"n_needed = {n_needed}",
                      "solve 1.96 * sqrt(0.25 / n) = 0.02 for n")
    return report(name, True, f"you need ~{target:,.0f} trades to pin a 50% win rate to ±2%")


def task2_1(estimate_p_nonstationary):
    name = "Task 2.1 non-stationary estimator"
    rng = np.random.default_rng(1)
    out, err = call(estimate_p_nonstationary, 10, rng)
    if err == "todo":
        return todo(name)
    if err:
        return report(name, False, err)
    try:
        p_hat, p_true = out
    except (TypeError, ValueError):
        return report(name, False, "should return a tuple (p_hat, p_true)")
    draws = np.array([estimate_p_nonstationary(2000, rng) for _ in range(3000)])
    sd_true = draws[:, 1].std()
    if not close(sd_true, 0.1, 0.01) or not close(draws[:, 1].mean(), 0.5, 0.01):
        return report(name, False, f"p_true has mean {draws[:, 1].mean():.3f}, sd {sd_true:.3f}",
                      "draw p_true once per experiment from N(0.5, 0.1), clipped to [0, 1]")
    if not close(np.abs(draws[:, 0] - draws[:, 1]).mean(), np.sqrt(0.24 / 2000) * np.sqrt(2 / np.pi), 0.003):
        return report(name, False, "p_hat isn't tracking p_true",
                      "the flips must use the p_true drawn for that experiment")
    return report(name, True)


def task2_2(sd_err_vs_half_1000, sd_theory_10):
    name = "Task 2.2 law of total variance"
    if is_todo(sd_err_vs_half_1000) or is_todo(sd_theory_10):
        return todo(name)
    v = scalars(name, sd_err_vs_half_1000=sd_err_vs_half_1000, sd_theory_10=sd_theory_10)
    if v is None:
        return False
    sd_err_vs_half_1000, sd_theory_10 = v["sd_err_vs_half_1000"], v["sd_theory_10"]
    ok1 = close(sd_err_vs_half_1000, np.sqrt(0.24 / 1000 + 0.01), 0.008)
    ok2 = close(sd_theory_10, np.sqrt(0.24 / 10 + 0.01), 0.003)
    if not ok1:
        return report(name, False, f"sd_err_vs_half_1000 = {sd_err_vs_half_1000:.3f}",
                      "the error vs 0.5 can't fall below sd(p_true) = 0.1, however much data you have")
    if not ok2:
        return report(name, False, f"sd_theory_10 = {sd_theory_10:.4f}",
                      "Var(p_hat) = E[p(1-p)]/n + Var(p), and E[p(1-p)] = 0.25 - Var(p)")
    return report(name, True, "more data shrinks noise, not the uncertainty from a moving target")


def task3_1(p_win, avg_win, avg_loss, edge_total_expectation, mean_pl):
    name = "Task 3.1 edge decomposition"
    vals = [p_win, avg_win, avg_loss, edge_total_expectation, mean_pl]
    if any(is_todo(v) for v in vals):
        return todo(name)
    v = scalars(name, p_win=p_win, avg_win=avg_win, avg_loss=avg_loss,
                edge_total_expectation=edge_total_expectation, mean_pl=mean_pl)
    if v is None:
        return False
    p_win, avg_win, avg_loss, edge_total_expectation, mean_pl = v.values()
    target = dict(p_win=4 / 7, avg_win=115.0, avg_loss=-150.0, edge=10 / 7)
    got = dict(p_win=p_win, avg_win=avg_win, avg_loss=avg_loss, edge=edge_total_expectation)
    wrong = [k for k in target if not close(got[k], target[k], 1e-6)]
    if wrong:
        return report(name, False, f"check {', '.join(wrong)}",
                      "avg_loss is the mean P/L of losing trades (negative); edge = p*W + (1-p)*L")
    if not close(edge_total_expectation, mean_pl, 1e-9):
        return report(name, False, "edge from the decomposition should equal the plain mean P/L")
    return report(name, True, f"edge = {edge_total_expectation:.2f} per trade, same as the plain mean")


def task3_2(edge, breakeven_p):
    name = "Task 3.2 edge() and breakeven_p()"
    e, err1 = call(edge, 0.6, 115, -150)
    b, err2 = call(breakeven_p, 115, -150)
    if "todo" in (err1, err2):
        return todo(name)
    if err1 or err2:
        return report(name, False, err1 or err2)
    if not close(e, 9.0, 1e-9):
        return report(name, False, f"edge(0.6, 115, -150) = {e}", "0.6*115 + 0.4*(-150)")
    if not close(b, 150 / 265, 1e-9):
        return report(name, False, f"breakeven_p(115, -150) = {b}", "solve p*W + (1-p)*L = 0 for p")
    return report(name, True, f"breakeven win rate {b:.1%}: you need to win more than half to make money here")


def task3_3(curves, prob_losing_year):
    name = "Task 3.3 equity curves"
    if is_todo(curves) or is_todo(prob_losing_year):
        return todo(name)
    v = scalars(name, prob_losing_year=prob_losing_year)
    if v is None:
        return False
    prob_losing_year = v["prob_losing_year"]
    c = np.asarray(curves, dtype=float)
    if c.shape != (1000, 252):
        return report(name, False, f"curves has shape {c.shape}, expected (1000, 252)",
                      "one row per simulated year, cumulative P/L along the columns")
    if not close(c[:, -1].mean(), 252 * 9, 400):
        return report(name, False, f"mean final P/L is {c[:, -1].mean():.0f}, expected about {252 * 9}",
                      "cumulate the trade P/Ls with np.cumsum(..., axis=1)")
    sd = np.sqrt(252 * 0.24 * 265**2)
    theory = stats.norm.cdf(-252 * 9 / sd)
    if not close(prob_losing_year, theory, 0.04):
        return report(name, False, f"prob_losing_year = {prob_losing_year:.3f}, expected ~{theory:.3f}",
                      "fraction of curves whose final value is below zero")
    return report(name, True, f"~{theory:.0%} of years lose money even with a genuine edge")


def task3_4(prob_profitable):
    name = "Task 3.4 how sure can 7 trades make you?"
    if is_todo(prob_profitable):
        return todo(name)
    v = scalars(name, prob_profitable=prob_profitable)
    if v is None:
        return False
    prob_profitable = v["prob_profitable"]
    target = 1 - stats.beta.cdf(150 / 265, 5, 4)
    if not close(prob_profitable, target, 0.01):
        return report(name, False, f"prob_profitable = {prob_profitable:.3f}",
                      "posterior is Beta(1 + wins, 1 + losses); you want P(p > breakeven)")
    return report(name, True, f"P(strategy is profitable) ≈ {target:.0%}: about a coin toss")


def task4_1(rets, p_win, edge_bps):
    name = "Task 4.1 SPY edge decomposition"
    if any(is_todo(v) for v in (rets, p_win, edge_bps)):
        return todo(name)
    v = scalars(name, p_win=p_win, edge_bps=edge_bps)
    if v is None:
        return False
    p_win, edge_bps = v["p_win"], v["edge_bps"]
    r = np.asarray(rets, dtype=float)
    if np.isnan(r).any():
        return report(name, False, "rets contains NaN", "drop the first row after pct_change()")
    if np.abs(r).max() > 0.5:
        return report(name, False, "returns look too large", "use daily simple returns, e.g. 0.01 for +1%")
    if not close(edge_bps, r.mean() * 1e4, 1e-6):
        return report(name, False, f"edge_bps = {edge_bps:.3f}, mean daily return = {r.mean() * 1e4:.3f} bps",
                      "edge = p*avg_win + (1-p)*avg_loss; count zero-return days as losses (they earn nothing)")
    if not close(p_win, (r > 0).mean(), 1e-9):
        return report(name, False, "p_win doesn't match the share of up days")
    return report(name, True, f"{p_win:.1%} up days, edge {edge_bps:.2f} bps/day")


def task4_2(ci_low, ci_high, rets):
    name = "Task 4.2 bootstrap CI"
    if any(is_todo(v) for v in (ci_low, ci_high, rets)):
        return todo(name)
    v = scalars(name, ci_low=ci_low, ci_high=ci_high)
    if v is None:
        return False
    ci_low, ci_high = v["ci_low"], v["ci_high"]
    r = np.asarray(rets, dtype=float)
    se = r.std() / np.sqrt(len(r)) * 1e4
    mid = r.mean() * 1e4
    if not (ci_low < mid < ci_high):
        return report(name, False, "the interval should contain the sample mean")
    if not close(ci_high - ci_low, 2 * 1.96 * se, 0.25 * 2 * 1.96 * se):
        return report(name, False, f"CI width {ci_high - ci_low:.2f} bps, expected about {2 * 1.96 * se:.2f}",
                      "resample the returns with replacement (same length), take the mean each time, "
                      "then the 2.5% and 97.5% percentiles, in bps")
    return report(name, True, f"95% CI [{ci_low:.2f}, {ci_high:.2f}] bps/day")
