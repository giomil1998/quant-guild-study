"""Checkpoint helpers for the starter notebooks.

Each project has a module (p02, p03, ...) with one function per task. They print
a pass or a hint and never raise, so "Run All" always reaches the end and shows
where you stand.
"""

import numpy as np

PASS, FAIL, TODO = "✅", "❌", "⏳"


def report(task, passed, msg="", hint=""):
    if passed:
        print(f"{PASS} {task}: {msg or 'passed'}")
    else:
        print(f"{FAIL} {task}: {msg}" + (f"\n   hint: {hint}" if hint else ""))
    return passed


def todo(task):
    print(f"{TODO} {task}: not done yet")
    return False


def is_todo(value):
    return value is None or (isinstance(value, float) and np.isnan(value))


def call(fn, *args, **kwargs):
    """Call a student function; returns (result, None) or (None, reason)."""
    try:
        return fn(*args, **kwargs), None
    except NotImplementedError:
        return None, "todo"
    except Exception as exc:  # show the student what went wrong without stopping the notebook
        return None, f"{type(exc).__name__}: {exc}"


def close(value, target, tol):
    return value is not None and abs(float(value) - target) <= tol
