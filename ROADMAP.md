# Learning roadmap

The original library is ordered by upload date. This roadmap groups it by concept, so each module builds on the last. Module 1 comes first on purpose: it sets out the problem (finding and surviving an edge) that the later tools serve.

**How to work through a project**

1. Watch the lecture (the link is in the original folder) and skim the original notebook.
2. Rebuild it from a blank notebook in `notebooks/NN_topic/`, in your own words. Copying cells teaches very little.
3. Add one extension the original doesn't have, ideally on real free data (yfinance, FRED, Ken French library).
4. Close with a **Takeaways** cell, then tick it off here and add a row to the README's project table.

Status: ✅ done · 🟡 in progress · ⬜ not started

## 1. Trading edge, randomness and ruin

Why most trading P&L is noise, what an edge actually is, and how bet sizing decides whether you survive it. Mostly simulation, with free equity/FX data to test the ideas.

| | # | Lecture |
|---|---|---|
| ✅ | 22 | [How to Trade](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/22.%20How%20to%20Trade) |
| 🟡 | 3 | [How to Make & Lose Money Trading](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/3.%20How%20to%20Make%20%26%20Lose%20Money%20Trading) |
| ⬜ | 4 | [Analyzing Trading Strategy Performance Over Time](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/4.%20Analyzing%20Trading%20Strategy%20Performance%20Over%20Time) |
| ⬜ | 26 | [Is Quant Trading Gambling - Roulette, Poker, and Trading](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/26.%20Is%20Quant%20Trading%20Gambling%20-%20Roulette%2C%20Poker%2C%20and%20Trading) |
| ⬜ | 28 | [Gambler's Ruin Problem in Quant Trading](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/28.%20Gambler%27s%20Ruin%20Problem%20in%20Quant%20Trading) |
| ⬜ | 34 | [How to Trade with an Edge](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/34.%20How%20to%20Trade%20with%20an%20Edge) |
| ⬜ | 36 | [How to Trade with the Kelly Criterion](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/36.%20How%20to%20Trade%20with%20the%20Kelly%20Criterion) |
| ⬜ | 81 | [Why Most Traders Lose Ergodicity for Quant Trading](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/81.%20Why%20Most%20Traders%20Lose%20Ergodicity%20for%20Quant%20Trading) |
| ⬜ | 136 | [How Volatility Drag Destroys (and Creates) Wealth](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/136.%20How%20Volatility%20Drag%20Destroys%20%28and%20Creates%29%20Wealth) |
| ⬜ | 46 | [Is Trading Luck or Skill Quant Debunks Trading Gurus with Math](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/46.%20Is%20Trading%20Luck%20or%20Skill%20Quant%20Debunks%20Trading%20Gurus%20with%20Math) |
| ⬜ | 60 | [Is Trading Gambling - Quant Proves It's Not With Math](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/60.%20Is%20Trading%20Gambling%20-%20Quant%20Proves%20It%27s%20Not%20With%20Math) |

## 2. Probability and simulation toolkit

The Monte Carlo and stochastic-process machinery everything else is built on.

| | # | Lecture |
|---|---|---|
| ⬜ | 1 | [Inverse Transform Method for Generating Random Variables](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/1.%20Inverse%20Transform%20Method%20for%20Generating%20Random%20Variables) |
| ⬜ | 2 | [Control Variates for Variance Reduction](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction) |
| ⬜ | 33 | [Why Monte Carlo Simulation Works](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/33.%20Why%20Monte%20Carlo%20Simulation%20Works) |
| ⬜ | 61 | [Central Limit Theorem for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/61.%20Central%20Limit%20Theorem%20for%20Quant%20Finance) |
| ⬜ | 59 | [Brownian Motion for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/59.%20Brownian%20Motion%20for%20Quant%20Finance) |
| ⬜ | 135 | [Arithmetic and Geometric Brownian Motion Masterclass](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/135.%20Arithmetic%20and%20Geometric%20Brownian%20Motion%20Masterclass) |
| ⬜ | 29 | [Itô's Lemma Clearly and Visually Explained](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/29.%20It%C3%B4%27s%20Lemma%20Clearly%20and%20Visually%20Explained) |
| ⬜ | 31 | [Itô Integration Clearly and Visually Explained](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/31.%20It%C3%B4%20Integration%20Clearly%20and%20Visually%20Explained) |
| ⬜ | 37 | [Stochastic Differential Equations for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/37.%20Stochastic%20Differential%20Equations%20for%20Quant%20Finance) |
| ⬜ | 71 | [Markov Property for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/71.%20Markov%20Property%20for%20Quant%20Finance) |
| ⬜ | 49 | [Markov Chains for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/49.%20Markov%20Chains%20for%20Quant%20Finance) |
| ⬜ | 82 | [Poisson Processes for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/82.%20Poisson%20Processes%20for%20Quant%20Finance) |
| ⬜ | 94 | [Hawkes Processes for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/94.%20Hawkes%20Processes%20for%20Quant%20Finance) |
| ⬜ | 25 | [How to Simulate Fractional Brownian Motion (fbM) via Davies-Harte](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/25.%20How%20to%20Simulate%20Fractional%20Brownian%20Motion%20%28fbM%29%20via%20Davies-Harte) |
| ⬜ | 85 | [Quant Derives Volterra Process Discretization and Simulation](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/85.%20Quant%20Derives%20Volterra%20Process%20Discretization%20and%20Simulation) |

## 3. Measuring performance and backtesting honestly

Sharpe, CAGR, luck vs skill, and the ways a backtest lies.

| | # | Lecture |
|---|---|---|
| ⬜ | 48 | [Why Trading Metrics are Misleading (Unless This is True)](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/48.%20Why%20Trading%20Metrics%20are%20Misleading%20%28Unless%20This%20is%20True%29) |
| ⬜ | 101 | [Stop Using the Sharpe Ratio Until You Watch This](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/101.%20Stop%20Using%20the%20Sharpe%20Ratio%20Until%20You%20Watch%20This) |
| ⬜ | 125 | [CAGR The Quantitative BS Test for Trading Performance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/125.%20CAGR%20The%20Quantitative%20BS%20Test%20for%20Trading%20Performance) |
| ⬜ | 96 | [I Bet You've Never Found Alpha (and I Can Prove It)](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/96.%20I%20Bet%20You%27ve%20Never%20Found%20Alpha%20%28and%20I%20Can%20Prove%20It%29) |
| ⬜ | 97 | [3 Backtesting Pitfalls That Ruin Your Strategy](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/97.%203%20Backtesting%20Pitfalls%20That%20Ruin%20Your%20Strategy) |
| ⬜ | 77 | [Profitable vs Tradable Why Most Strategies Fail Live](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/77.%20Profitable%20vs%20Tradable%20Why%20Most%20Strategies%20Fail%20Live) |
| ⬜ | 75 | [Quant Explains Backtesting with Poker](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/75.%20Quant%20Explains%20Backtesting%20with%20Poker) |
| ⬜ | 118 | [No You dont need to backtest a trading strategy](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/118.%20No%20You%20dont%20need%20to%20backtest%20a%20trading%20strategy) |
| ⬜ | 93 | [Non-Stationarity and Why Market Timing Fails](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/93.%20Non-Stationarity%20and%20Why%20Market%20Timing%20Fails) |
| ⬜ | 58 | [Why Quant Models Break](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/58.%20Why%20Quant%20Models%20Break) |
| ⬜ | 112 | [Why your Trading Strategy Sucks](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/112.%20Why%20your%20Trading%20Strategy%20Sucks) |

## 4. Option pricing

Black-Scholes from several angles: risk-neutral pricing, Monte Carlo, PDEs, Fourier methods, exotics.

| | # | Lecture |
|---|---|---|
| ⬜ | 18 | [Why Quant Traders Care About Pricing](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/18.%20Why%20Quant%20Traders%20Care%20About%20Pricing) |
| ⬜ | 6 | [How to Trade with the Black-Scholes Model](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/6.%20How%20to%20Trade%20with%20the%20Black-Scholes%20Model) |
| ⬜ | 19 | [Monte Carlo Simulation and Black-Scholes for Pricing Options](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/19.%20Monte%20Carlo%20Simulation%20and%20Black-Scholes%20for%20Pricing%20Options) |
| ⬜ | 73 | [How to Price Options with Monte Carlo Simulation](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/73.%20How%20to%20Price%20Options%20with%20Monte%20Carlo%20Simulation) |
| ⬜ | 83 | [Quant Explains Risk-Neutral Option Pricing](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/83.%20Quant%20Explains%20Risk-Neutral%20Option%20Pricing) |
| ⬜ | 67 | [How Physics Accidentally Proved the Black-Scholes Model](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/67.%20How%20Physics%20Accidentally%20Proved%20the%20Black-Scholes%20Model) |
| ⬜ | 38 | [Finite Differences Option Pricing for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/38.%20Finite%20Differences%20Option%20Pricing%20for%20Quant%20Finance) |
| ⬜ | 32 | [How to Price Exotic Options](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/32.%20How%20to%20Price%20Exotic%20Options) |
| ⬜ | 39 | [Heston Stochastic Volatility Model and Fast Fourier Transforms](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/39.%20Heston%20Stochastic%20Volatility%20Model%20and%20Fast%20Fourier%20Transforms) |
| ⬜ | 89 | [Black-Scholes Implied Volatility in 3 Minutes](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/89.%20Black-Scholes%20Implied%20Volatility%20in%203%20Minutes) |
| ⬜ | 107 | [How to Trade Options with the Black-Scholes Model](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/107.%20How%20to%20Trade%20Options%20with%20the%20Black-Scholes%20Model) |

## 5. Trading options and volatility

Greeks, hedging, implied vs realised volatility, the vol surface and the volatility risk premium. Free data: yfinance option chains (current snapshot), ^VIX history.

| | # | Lecture |
|---|---|---|
| ⬜ | 9 | [Delta Hedging and Black-Scholes Prices](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/9.%20Delta%20Hedging%20and%20Black-Scholes%20Prices) |
| ⬜ | 11 | [Managing Option Portfolios with Black-Scholes Greeks](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/11.%20Managing%20Option%20Portfolios%20with%20Black-Scholes%20Greeks) |
| ⬜ | 7 | [Martingale Volatility Trading](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/7.%20Martingale%20Volatility%20Trading) |
| ⬜ | 23 | [How to Trade Option Implied Volatility](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/23.%20How%20to%20Trade%20Option%20Implied%20Volatility) |
| ⬜ | 24 | [Trading with Violated Model Assumptions](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/24.%20Trading%20with%20Violated%20Model%20Assumptions) |
| ⬜ | 30 | [Trading with the Black-Scholes Implied Volatility Surface](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/30.%20Trading%20with%20the%20Black-Scholes%20Implied%20Volatility%20Surface) |
| ⬜ | 43 | [How to Trade Implied Volatility Crush](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/43.%20How%20to%20Trade%20Implied%20Volatility%20Crush) |
| ⬜ | 119 | [Volatility Risk Premium How Options Markets Price Fear](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/119.%20Volatility%20Risk%20Premium%20How%20Options%20Markets%20Price%20Fear) |
| ⬜ | 106 | [How to Trade the Covered Call](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/106.%20How%20to%20Trade%20the%20Covered%20Call) |
| ⬜ | 113 | [How to Trade the Cash Secured Puts](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/113.%20How%20to%20Trade%20the%20Cash%20Secured%20Puts) |
| ⬜ | 120 | [I Met a Jane Street Quant at the Gym (He Got This Wrong)](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/120.%20I%20Met%20a%20Jane%20Street%20Quant%20at%20the%20Gym%20%28He%20Got%20This%20Wrong%29) |

## 6. Time series and volatility models

Stationarity, GARCH, regime models and filtering.

| | # | Lecture |
|---|---|---|
| ⬜ | 44 | [Time Series Analysis for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/44.%20Time%20Series%20Analysis%20for%20Quant%20Finance) |
| ⬜ | 47 | [Master Volatility with ARCH & GARCH Models](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/47.%20Master%20Volatility%20with%20ARCH%20%26%20GARCH%20Models) |
| ⬜ | 51 | [Hidden Markov Models for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/51.%20Hidden%20Markov%20Models%20for%20Quant%20Finance) |
| ⬜ | 92 | [Kalman Filter for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/92.%20Kalman%20Filter%20for%20Quant%20Finance) |
| ⬜ | 95 | [Trading Mean Reversion with Kalman Filters](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/95.%20Trading%20Mean%20Reversion%20with%20Kalman%20Filters) |

## 7. Portfolio construction and risk

Mean-variance and why it breaks, Black-Litterman, factor exposure, tail risk and crash protection.

| | # | Lecture |
|---|---|---|
| ⬜ | 14 | [Quant Investing for Beginners](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/14.%20Quant%20Investing%20for%20Beginners) |
| ⬜ | 17 | [Analyzing Stock Returns with Principal Component Analysis in Python](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/17.%20Analyzing%20Stock%20Returns%20with%20Principal%20Component%20Analysis%20in%20Python) |
| ⬜ | 20 | [Why Portfolio Optimization Doesn't Work](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/20.%20Why%20Portfolio%20Optimization%20Doesn%27t%20Work) |
| ⬜ | 21 | [Expected Stock Returns Don't Exist](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/21.%20Expected%20Stock%20Returns%20Don%27t%20Exist) |
| ⬜ | 78 | [Trader Skill or Market Luck Quant Explains Alpha in 3 Minutes](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/78.%20Trader%20Skill%20or%20Market%20Luck%20Quant%20Explains%20Alpha%20in%203%20Minutes) |
| ⬜ | 100 | [Black-Litterman vs. Mean-Variance Portfolio Optimization in Python](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/100.%20Black-Litterman%20vs.%20Mean-Variance%20Portfolio%20Optimization%20in%20Python) |
| ⬜ | 88 | [How a Quant Manages a Portfolio](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/88.%20How%20a%20Quant%20Manages%20a%20Portfolio) |
| ⬜ | 115 | [How a Quant Engineers a Portfolio](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/115.%20How%20a%20Quant%20Engineers%20a%20Portfolio) |
| ⬜ | 127 | [The Ultimate Guide to Quant Portfolio Management](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/127.%20The%20Ultimate%20Guide%20to%20Quant%20Portfolio%20Management) |
| ⬜ | 128 | [How to Calculate Portfolio Alpha & Beta (Python + Interactive Brokers)](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/128.%20How%20to%20Calculate%20Portfolio%20Alpha%20%26%20Beta%20%28Python%20%2B%20Interactive%20Brokers%29) |
| ⬜ | 126 | [How to Model Tail-Risk A Quantitative Survival Guide](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/126.%20How%20to%20Model%20Tail-Risk%20A%20Quantitative%20Survival%20Guide) |
| ⬜ | 138 | [How to Protect your Stock Portfolio Against a Market Crash](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/138.%20How%20to%20Protect%20your%20Stock%20Portfolio%20Against%20a%20Market%20Crash) |
| ⬜ | 123 | [How a Quant would Invest 1,000,000](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2026%20Video%20Lectures/123.%20How%20a%20Quant%20would%20Invest%201%2C000%2C000) |

## 8. Machine learning and market microstructure

What neural nets and NLP can and can't learn about prices, plus market making.

| | # | Lecture |
|---|---|---|
| ⬜ | 13 | [Can AI Learn Black-Scholes](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/13.%20Can%20AI%20Learn%20Black-Scholes) |
| ⬜ | 16 | [Information and Stock Price Prediction](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/16.%20Information%20and%20Stock%20Price%20Prediction) |
| ⬜ | 35 | [What Does AI Actually Learn](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/35.%20What%20Does%20AI%20Actually%20Learn) |
| ⬜ | 63 | [Neural Networks for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/63.%20Neural%20Networks%20for%20Quant%20Finance) |
| ⬜ | 65 | [Natural Language Processing for Quant Finance](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/65.%20Natural%20Language%20Processing%20for%20Quant%20Finance) |
| ⬜ | 69 | [Quant Explains Algorithmic Market-Making](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/tree/main/2025%20Video%20Lectures/69.%20Quant%20Explains%20Algorithmic%20Market-Making) |

