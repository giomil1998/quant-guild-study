"""Free market data with a local CSV cache.

Every notebook pulls data through `load_prices`, so the source and caching
behaviour live in one place. Data comes from Yahoo Finance via yfinance
(free, no API key). Cached files go in `data/`, which git ignores.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / "data"


def load_prices(
    tickers: str | list[str],
    start: str = "2005-01-01",
    end: str | None = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """Daily adjusted close prices, one column per ticker.

    Examples of free tickers: "SPY" (S&P 500 ETF), "EURUSD=X" (EUR/USD spot),
    "^VIX" (VIX index), "TLT" (long Treasuries), "GLD" (gold).
    """
    tickers = [tickers] if isinstance(tickers, str) else list(tickers)
    CACHE_DIR.mkdir(exist_ok=True)
    key = "_".join(t.replace("^", "").replace("=", "") for t in tickers)
    path = CACHE_DIR / f"{key}_{start}_{end or 'latest'}.csv"

    if path.exists() and not refresh:
        return pd.read_csv(path, index_col=0, parse_dates=True)

    raw = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
    prices = raw["Close"]
    if isinstance(prices, pd.Series):
        prices = prices.to_frame(tickers[0])
    prices = prices[tickers].dropna(how="all")
    prices.to_csv(path)
    return prices
