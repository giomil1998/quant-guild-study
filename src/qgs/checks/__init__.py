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


def as_scalar(value):
    """A number from a number, or from a one-element array/list (e.g. fsolve's output)."""
    arr = np.asarray(value, dtype=float)
    if arr.size != 1:
        raise ValueError(f"expected a single number, got an array of shape {arr.shape}")
    return float(arr.reshape(()))


def scalars(task, **values):
    """Convert each named value to a float; report and return None if any isn't a single number."""
    out = {}
    for var, value in values.items():
        try:
            out[var] = as_scalar(value)
        except (TypeError, ValueError):
            shape = f"length {len(value)}" if hasattr(value, "__len__") else type(value).__name__
            report(task, False, f"`{var}` should be a single number, got {type(value).__name__} ({shape})",
                   "compute one summary number across all experiments, not one per experiment")
            return None
    return out


def close(value, target, tol):
    try:
        return value is not None and abs(as_scalar(value) - target) <= tol
    except (TypeError, ValueError):
        return False
