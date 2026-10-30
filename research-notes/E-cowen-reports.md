# E — Benjamin Cowen's written reports (benjamincowen.com/reports): full analysis

Research file for the course "practical-macro-economy". Compiled 2026-10-30. It complements `A-cowen-inventory.md` (abbreviated "the inventory" below).

Tags: **[V]** seen on the report page or in the report PDF itself; **[S]** secondary source (news write-up, search snippet, aggregator); **[I]** my inference or arithmetic.

---

## 0. Method, access, and what changed versus the inventory

**How the list was built.**
- The index page `https://benjamincowen.com/reports` lists **11 reports** in 2 series: "Crypto Macro Risk Memo" (8) and "Crypto Analysis" (3). The latest is dated 30 Sep 2026 [V].
- There is no pagination. `?page=2` returns the same page, and `/reports/page/2`, `/rss.xml` and `/feed.xml` return 404 [V].
- `sitemap.xml` lists the same 11 report URLs and nothing else [V].
- The Wayback Machine CDX index for `benjamincowen.com/reports*` shows no other report slugs. The domain has no reports archived before January 2026 (the only pre-2026 captures are a 2013 home page and Nov 2025 probe URLs) [V].
- So **11 reports is the complete set**. There are no older reports to add.

**Access.**
- All 11 web pages are open, with no login [V].
- Each page also offers an e-mail form ("Get the PDF report"). For **9 of the 11** reports, the page itself also embeds the full PDF in a "Read the full report" viewer, with an "Open in a new tab" link to a public Vercel blob URL. No e-mail, login or captcha is needed, because the link is in the page's own HTML [V].
- I read all 9 PDFs: 193 pages and about 59,000 words in total.
- The two 2020 reports (Bitcoin Letters, Ethereum Letters) have **no** embedded PDF; the PDF is only offered through the e-mail form. I did not submit any e-mail, so these two PDFs count as **gated**. Only their web-page summaries were used.

**Correction to the inventory.**
- Inventory §0 item 3 says "the full PDFs sit behind an e-mail form and were not accessed". That is not accurate for the 9 reports from 2026: their full PDFs are publicly embedded.
- The inventory therefore only used the short page blurbs. The PDFs contain about 130 numbered figures, several tables, explicit invalidation conditions and a self-scored track record. Sections 3–5 below come mostly from that material.

**Title discrepancies between page and PDF [V].** The page titles are used in the index; the PDF cover titles are noted.

| Page title | PDF cover title |
|---|---|
| Crypto Macro Risk Memo - Q1 2026 | "Crypto Risk Memo (Q1 2026)" |
| Macro Risk Memo February 2026 | "Macro Risk Memo (Q1 2026)" |
| How Risk Cascades Through Markets (March 2026) | adds the subtitle "From Speculative Assets to the Real Economy" |
| Macro Risk Memo (May 2026) | "The Fed's Late Business Cycle Trap (May 2026): Defending Two Weaknesses" |
| Bitcoin Cycle Memo - July 2026 | "Bitcoin Cycle Memo: The Analog Enters Its Timing Test" |
| The Balance of Risks (August 2026) | subtitle "Weighing a Maturing Cycle Into Q4" |
| The Triple Squeeze (September 2026) | subtitle "Rising Yields, Rising Oil and a Firming Dollar Into Q4" |

**Internal inconsistencies worth knowing [V].**
- *BTC 2025 peak.* The Q2 memo says "near $126k". The August memo says "$124,700 (daily close; the widely quoted intraday all-time high was near $126,000)".
- *2026 low.* The July memo says "early-summer low near $57,000". The August memo says "late-June low near $58,500", and its data note gives 30 Jun 2026 on a daily-close basis. The September memo says "early July low near $57.7K".
- *ITC Liquidity Risk inputs.* The March and July memos describe them as "policy rates, yields, dollar strength, central bank liquidity, and funding stress proxies". The inventory (from the app help text) lists effective FFR, 2Y, DXY, Δ Fed assets and ΔM2. The memos add "funding stress proxies". Course writers should say the published inputs differ slightly between sources.

---

## 1. Report index

| # | Title (page) | Date | URL | Accessible? | Main topics |
|---|---|---|---|---|---|
| 1 | The Triple Squeeze (September 2026) | 30 Sep 2026 | https://benjamincowen.com/reports/the-triple-squeeze-september-2026 | Page + full PDF (16 pp) [V] | 10Y/30Y rate shock; oil–yields–dollar loop; gold-first/long-end-next sequencing; midterm yield peaks vs equity lows; small-cap divergence; BTC "where we were wrong"; BTC after hikes |
| 2 | The Balance of Risks (August 2026) | 15 Aug 2026 | https://benjamincowen.com/reports/the-balance-of-risks-august-2026 | Page + full PDF (30 pp) [V] | Late-cycle vs recession; 65/20/15 scenario weights; NFCI; recession composite; NDXE/NDX breadth; housing; CAPE; midterm S&P seasonality; payrolls YoY; global policy rate and global unemployment; DXY presidential-term analog; XLE lag; gold reset; BTC bottom-watch; self-scored record |
| 3 | Bitcoin Cycle Memo - July 2026 | 15 Jul 2026 | https://benjamincowen.com/reports/bitcoin-cycle-memo-july-2026 | Page + full PDF (24 pp) [V] | 2019 analog timing test; risk scorecard (22 metrics); cycle-ROI peak/bottom overlays; day counts; midterm monthly table; 200W break and reclaim; realized/balanced price; quantile fan; supply P/L cross; breadth; ETF holdings; hawkish Warsh Fed; oil |
| 4 | Asymmetric Tail Curvature in Bitcoin Price Quantiles | 29 May 2026 | https://benjamincowen.com/reports/asymmetric-tail-curvature-in-bitcoin-price-quantiles | Page + full PDF (38 pp working paper) [V] | Quantile regression; asymmetric curvature; power law/S2F/S2FX out-of-sample bias; block bootstrap; structural-plus-reflexivity model |
| 5 | Macro Risk Memo (May 2026) | 18 May 2026 | https://benjamincowen.com/reports/macro-risk-memo-may-2026 | Page + full PDF (15 pp) [V] | Late-cycle resilience; supply-driven inflation (CPI 3.8%, PPI, transport); Fed "checkmate"; claims, openings, temp help, payroll YoY; 2Y and 10Y; liquidity, DXY, SPX/gold; 7-step recession feedback loop |
| 6 | Crypto Risk Memo (Q2 2026) | 15 Apr 2026 | https://benjamincowen.com/reports/crypto-risk-memo-q2-2026 | Page + full PDF (18 pp) [V] | ~50% BTC drawdown; time-based capitulation; liquidity risk; global liquidity proxy; BTC.D with/without stables; stablecoin dominance; A/D index; on-chain partial reset; ETF and company holdings |
| 7 | How Risk Cascades Through Markets (March 2026) | 15 Mar 2026 | https://benjamincowen.com/reports/how-risk-cascades-through-markets-march-2026 | Page + full PDF (11 pp) [V] | ITC Risk Cascade Framework (5 stages); Liquidity Risk Model; Business Cycles Model formula; social risk; BTC.D; SPX/gold; DXY > 100; oil; claims; unemployment; recession model |
| 8 | Macro Risk Memo February 2026 | 15 Feb 2026 | https://benjamincowen.com/reports/macro-risk-memo-feb-2026 | Page + full PDF (26 pp) [V] | Liquidity level vs direction; real yields; global M2; labor diffusion; equity durability → labor; midterm and presidential cycle; 2s10s, 3m10y, FF−2Y; Chicago Fed financial conditions; housing; EPU and international equities; SPX/gold, gold/silver; three recession sub-indices; BTC midterm YTD, cycle-bottom ROI, BTC/SPX, BTC.D ex-stables |
| 9 | Crypto Macro Risk Memo - Q1 2026 | 15 Jan 2026 | https://benjamincowen.com/reports/crypto-macro-risk-memo-q1-2026 | Page + full PDF (15 pp) [V] | Apathy top; 2019 analog; Fed balance sheet; cycle ROI; drawdown; 365-day running ROI; on-chain composite; HODL waves; A/D index; BTC.D; 180-day volatility; recession sub-risks; correlation heatmap; "What would change this view" |
| 10 | Ethereum Letters (2020) | 20 Feb 2020 | https://benjamincowen.com/reports/ethereum-letters-2020 | Page summary only. **PDF gated** (e-mail form only) | ETH as distinct from BTC; ETH/BTC; model uncertainty; risk dispersion |
| 11 | Bitcoin Letters (2020) | 5 Jan 2020 | https://benjamincowen.com/reports/bitcoin-letters-2020 | Page summary only. **PDF gated** (e-mail form only) | Diminishing returns; volatility compression; risk regimes; no price targets |

Every 2026 memo follows the same template [V]:
- **Reference levels** at the publication date.
- **Cycle status / Cycle assessment**, **Regime characteristics**, **Recommended posture**, and **Primary risk drivers**.
- **Scope & Limitations** and an **Executive summary / Quick read**.
- Numbered sections, then **"What would change this view"** or refutation conditions, then a **Bottom line**.

The Aug and Sep memos add a "What changed since the [previous] edition" box and a cross-asset table. The Aug memo also adds a self-scored "Framework's 2026 Record".

---

## 2. Per-report notes

Format for each report: **Indicators** (exact chart names as captioned), **Theses / causal chains**, **Numbers**, **Forecasts** (with timing). Everything is [V] unless tagged otherwise.

### 2.1 Crypto Macro Risk Memo – Q1 2026 (15 Jan 2026)

- **Header:** BTC ≈ $97,153. Cycle status "Risk-Off". Posture "Capital preservation and tactical positioning". Risk drivers: restrictive real monetary conditions; weak crypto breadth and participation; late-cycle distribution by long-term holders.
- **Indicators (figures):**
  1. Bitcoin price color-coded by social risk
  2. Bitcoin price vs Federal Reserve balance sheet
  3. Bitcoin cycle ROI from cycle lows
  4. BTC drawdown from prior cycle peaks in Q4 of post-halving years
  5. BTC drawdown from the 2025 peak vs 2019
  6. BTC 365-day running return
  7. On-chain composite risk model
  8. Bitcoin HODL waves
  9. Crypto advance-decline index vs total market cap
  10. Bitcoin dominance
  11. **180-day Bitcoin volatility**
  12. Employment recession risk
  13. National income & production risk
  14. Business & industrial activity risk
  15. **Crypto, equity, and metals correlation heatmap**
  - The text also uses a "composite Social Risk Index constructed from content consumption, exchange activity, and crypto-related social discourse".
- **Theses / causal chains:**
  - The cycle topped on apathy, not euphoria (narrow pool of institutional and systematic capital), so rallies are structurally fragile, as in mid-2019.
  - Apathy peaks are not necessarily deeper or longer. In 2019 the drawdown phase was shorter than the ~12-month declines after the 2017 and 2021 peaks, but it was "choppier", with repeated countertrend rallies.
  - BTC peaked in early Oct 2025 and QT ended in early Dec 2025, mirroring 2019 (late-June top, QT end 1 Aug). "Bitcoin often leads liquidity cycles; liquidity tends to respond to macro stress."
  - The on-chain model never reached euphoric levels, so the top came from "demand exhaustion", not overheating. LTHs are distributing into strength (HODL waves).
  - "Low volatility at cycle highs is not stability, but rather fragility." Compression precedes either sharp repricing or long stagnation.
  - Fed balance-sheet growth "appears consistent with reserve management, funding operations, and financial-system stabilization", not crisis QE. Crypto needs **speculative liquidity**, meaning capital that is "both abundant and willing to take risk".
  - "Recessions typically do not begin with slower hiring, they begin when layoffs accelerate."
  - Correlation breakdown signals segmentation: the liquidity supporting stocks and metals is not the liquidity that fuels crypto. Capital is going to gold, silver, copper and platinum. 2019 also saw this decoupling.
  - "A recession is not strictly required" for crypto to stabilize if labor cools in an orderly way.
- **Forecasts:** "Rallies are likely to be tactical rather than structural"; posture is capital preservation.
- **Reversal conditions ("What Would Change This View"):** broader participation (A/D, altcoins, social engagement); on-chain reset (more supply at a loss, capitulation, LTH accumulation); constructive volatility re-expansion; decisive liquidity shift (collapse in real yields, balance-sheet expansion, emergency easing).

### 2.2 Macro Risk Memo February 2026 (15 Feb 2026; PDF titled "Macro Risk Memo (Q1 2026)")

- **Header:** S&P ≈ 6,836; gold ≈ $5,042; BTC ≈ $69,799. Assessment "Late-cycle restrictive digestion". Posture "Capital preservation with selective deployment".
  - Five risk drivers: policy restrictiveness relative to neutral; equity durability as a labor transmission mechanism; dollar direction as a global liquidity constraint; liquidity stabilization vs liquidity impulse; breadth of labor softness vs nonlinear break.
- **Indicators (figures):**
  1. US Liquidity Risk Score
  2. DXY
  3. 10-Year Real Yield
  4. **Global M2 Year-Over-Year Change**
  5. US Unemployment Rate
  6. Layoffs and Discharges
  7. Number of States Where Unemployment is Higher Than Six Months Ago
  8. State-Level Unemployment Change Map
  9. Initial Jobless Claims
  10. S&P 500 YTD vs Average Midterm Year
  11. Average Annual Returns by Presidential Cycle Year
  12. 10Y–2Y spread
  13. 10Y–3M spread
  14. Federal Funds Rate minus 2-Year Treasury Yield
  15. **Chicago Financial Conditions Index**
  16. **Housing Units Under Construction**
  17. **Purchase-Only House Price Index YoY**
  18. **Median Listing Prices**
  19. Economic Policy Uncertainty Index
  20. S&P 500/Gold Ratio
  21. Gold/Silver Ratio
  22. **Employment Risk Indicator**
  23. **National Income and Product Risk Indicator**
  24. **Production and Business Risk Indicator**
  25. Bitcoin YTD ROI vs Midterm Years (2014, 2018, 2022, ±1 SD band)
  26. Bitcoin Market Cycle Bottom ROI Across Cycles
  27. **BTC/SPX Overlay with S&P 500**
  28. Bitcoin Dominance excluding stablecoins
  - Appendix "Indicator Summary Table" (Current Regime / Risk Bias):
    - Liquidity: restrictive stabilization / neutral-defensive
    - Labor: cooling, not nonlinear / watch
    - Housing: slowing / late-cycle
    - Yield curve: restrictive / elevated risk
    - Crypto: cyclical contraction / defensive-selective
- **Theses / causal chains:**
  - Distinguish liquidity **direction** from liquidity **level**. The Liquidity Risk Score sits in "the upper quartile", in the "tight" to "very tight" regime.
  - Bull markets can occur in tight liquidity (2006–07, 2023–25), but they are "flight-to-quality bull markets": small → large caps, alts → BTC, speculative growth → cash-flow franchises.
  - A renewed dollar upswing "similar to 2018" would tighten global liquidity even without QT.
  - BTC "peaked before M2 rolled over and ultimately bottomed shortly after M2 peaked". Risk assets respond to slope changes, not aggregate peaks.
  - **Equity durability → labor:** "The magnitude of a correction matters less than its duration." Persistent weakness compresses earnings expectations and credit, which leads to layoffs, which leads to nonlinear unemployment. Early 2025 looked like 1998, not 2000.
  - Recession risk rises during re-steepening, not at peak inversion. The curve "can 'look healthier' while the underlying economy is worsening."
  - Housing is "slowing rather than breaking". Household balance sheets and underwriting are stronger than in 2006–08.
  - Elevated EPU plus a softer dollar favors international equities over US.
  - Energy has historically outperformed high-beta assets in midterm years. Structural themes are electrification, grid build-out and AI compute.
  - Silver often peaks before gold late in the cycle (1973–74, 2011).
  - "Stocks bleeding to gold reflects the same hierarchy of risk compression" as alts bleeding to BTC.
- **Forecasts:** crypto in "midterm digestion", with only tactical rallies; durable expansion needs a stronger liquidity impulse or equity stress forcing policy recalibration; international may keep outperforming while the dollar is benign.
- **Reversal conditions:** nonlinear labor deterioration (layoffs plus rising initial and continuing claims); durable equity suppression; structurally constraining dollar strength; a decisive pivot (real yields down, policy clearly below neutral, renewed balance-sheet expansion).

### 2.3 How Risk Cascades Through Markets (15 Mar 2026)

- **Header:** S&P ≈ 6,632; gold ≈ $5,018; BTC ≈ $71,214. Assessment "Late-cycle restrictive digestion with emerging supply-driven pressures"; regime adds "stronger dollar, oil-driven cost pressures".
- **Indicators:**
  1. ITC Liquidity Risk Model (0–1, higher = tighter)
  2. ITC Business Cycles Model
  3. ITC Social Risk Metric
  4. Bitcoin Dominance (excl. stablecoins)
  5. S&P 500 Relative to Gold
  6. DXY
  7. Oil price with recessions overlaid
  8. Initial Jobless Claims
  9. US Unemployment Rate
  10. ITC Macro Recession Risk Model
  - The Business Cycles Model formula is given exactly as **"(SPX / UNRATE²) × USINTR × USIRYY, normalized by M2"**. USINTR is "a short policy rate proxy" and USIRYY is "year-over-year CPI inflation".
- **Thesis:** the **ITC Risk Cascade Framework**, five stages:
  1. Speculative participation declines.
  2. Highly speculative assets weaken.
  3. Traditional risk assets deteriorate relative to gold.
  4. Financial conditions tighten further (dollar, energy) "even if central banks begin shifting toward easing".
  5. A labor-market feedback loop emerges.
  - "The current environment appears to be transitioning between Stage 3 and Stage 4."
  - The DXY "above 100" resembles early 2018.
  - Supply-driven oil spikes late in the cycle act as a tax.
- **Forecast:** no dated forecast. If financial weakness persists long enough, stage 5 follows; if it proves temporary, the cycle "could stabilize".

### 2.4 Crypto Risk Memo (Q2 2026) (15 Apr 2026)

- **Header:** BTC ≈ $74,822. Status "Late-cycle, liquidity-constrained adjustment". Risk drivers: incomplete reset; restrictive liquidity with delayed easing; weak breadth.
- **Indicators:**
  1. Bitcoin price
  2. ITC business cycle composite
  3. ITC liquidity risk model
  4. **Global liquidity proxy** ("major central bank balance sheets adjusted for RRP and TGA")
  5. BTC dominance including and excluding stablecoins
  6. Stablecoin dominance (top 10 stablecoins)
  7. Top-100 crypto advance-decline index
  8. BTC YTD ROI vs average midterm year (±1 SD)
  9. BTC ROI following prior cycle peaks
  10. BTC ROI from peak, 2019 tightening cycle vs 2026
  11. % supply in profit and loss
  12. MVRV Z-score
  13. Price vs realized and balanced price
  14. ITC on-chain risk metric
  15. ITC social risk metric (updated: Google Trends, Coinbase rankings, YouTube/X followers and subscribers)
  16. Bitcoin ETF holdings
  17. **Public company Bitcoin holdings**
- **Theses:**
  - "What the market confirmed": the late-2025 call for a Q4 peak; the Jan framework with BTC near $97k; a subsequent >50% drawdown ($126k → $60k).
  - BTC.D with stables is stable at 58–60%, but ex-stables it keeps rising. The "stability is misleading" because stablecoin share grew.
  - Midterm seasonality only matters in combination with late-cycle macro, and "multiple crypto cycles can occur within a single broader business cycle".
  - In 2019 the initial ~50% decline came from liquidity tightening. The deeper drop came from the COVID macro shock. So further downside "may require an additional catalyst" (labor, sustained equity decline, feedback loop).
  - Otherwise expect **time-based capitulation**: "Rather than forcing participants out through large losses, the market wears them out over time."
  - ETF holdings reached **6.77% of total supply** but are stabilizing, moving "from a driver of price appreciation to a stabilizing component". Company holdings keep rising and count as "structural demand".
- **Forecasts:** rallies tactical; "both extended consolidation and additional downside remain plausible"; favor quality, avoid chasing rallies.

### 2.5 Macro Risk Memo (May 2026) / "The Fed's Late Business Cycle Trap" (18 May 2026)

- **Header:** S&P ≈ 7,378; gold ≈ $4,542; BTC ≈ $76,433. Assessment "Late-cycle resilience facing renewed inflationary pressure". Posture "Defensive positioning with tactical deployment during periods of weakness".
- **Indicators:**
  1. Macro recession risk
  2. Initial claims (211k)
  3. **Continued claims**
  4. Unemployment Rate
  5. Job openings
  6. Job openings per available worker
  7. **Temporary employment**
  8. **Payroll growth year-over-year change**
  9. Headline CPI (3.8%)
  10. Core inflation
  11. Producer price inflation
  12. Inflation by category
  13. Oil price
  14. Fed funds rate overlaid with the 2-year Treasury yield
  15. 10-year Treasury yield
  16. ITC Liquidity Risk Model
  17. DXY
  18. SPX-to-gold ratio
  19. ITC Business Cycles Model
  20. YTD ROI of SPX in 2018, 2022 and 2026
- **Theses:**
  - The inflation resurgence is supply-driven (energy, transport, producer costs); core has not re-accelerated.
  - "Fed policy tends to follow the direction implied by the front end." Financial conditions can tighten "even without formal rate hikes".
  - Employers hold on to staff because of "lingering labor shortages".
  - Temp help weakens first because firms cut flexible labor before permanent staff.
  - **Recession feedback loop, 7 steps:**
    1. Asset prices weaken.
    2. Financial conditions tighten.
    3. Business confidence deteriorates.
    4. Hiring slows and layoffs rise.
    5. Consumption weakens.
    6. Activity contracts.
    7. Further layoffs.
    - The economy is "stuck in the earlier stages".
  - **Checkmate:** supply-driven inflation plus softening labor puts "both sides of the Fed's mandate" under pressure at the same time.
- **Forecasts:**
  - Markets "pricing in the possibility of higher rates rather than cuts".
  - "The next meaningful period to reassess broader cyclical fragility may emerge later in Q3 or Q4."
  - "The end of the business cycle could still plausibly be one to two years away."

### 2.6 Asymmetric Tail Curvature in Bitcoin Price Quantiles (working paper, 29 May 2026)

- **Method:**
  - Quadratic quantile regression of log price on log time, with separate curvature for the upper and lower tail groups.
  - Non-crossing of quantile lines is enforced by the **rearrangement estimator** of Chernozhukov, Fernández-Val and Galichon (2010).
  - Inference uses a **block bootstrap** (block lengths 14–90 days).
  - Out-of-sample evaluation uses an **expanding window** with four cutpoints, scored by **check-loss** (quantile/pinball loss).
  - Data: 5,788 daily observations, 2010–2026.
- **Results:**
  - Δb = b_HI − b_LO = −0.302, with b_HI = −0.326 and b_LO = −0.024.
  - The difference is significant: full-bootstrap p = 0.012; concentrated bootstrap p ≤ 0.006.
  - b_LO is not distinguishable from 0 (p = 0.258). Upper-tail confidence interval: [−0.455, −0.072].
  - Upper-tail check-loss improves by +26.7% to +29.1% at Q75/Q95/Q99 versus a linear quantile power law.
- **Benchmarks:**
  - An OLS power law calibrated to 2018 overpredicted on 77.2% of later days (geometric mean error +32.1%, 2019–2026).
  - S2F overpredicted on 94.9% of days (+294.5%); S2FX +1,699%.
  - Lineage credited: Santostasi's power law (2018–2024), Trolololo's log regression, PlanB's S2F/S2FX, and "Plan C" stretched-exponential quantile models.
- **Mechanism:**
  - A "structural-plus-reflexivity" model: structural demand gives a straight power-law floor.
  - A speculative multiplier 1 + A·g(t), with g(t) = 1/(1+(t/t*)^k), decays as market cap grows. This gives "diminishing reflexivity", i.e. diminishing returns.
  - The authors call this a "sufficiency, not uniqueness" argument.
- **Caveats stated:** "not a forecast, a price floor, or a measure of portfolio loss risk". Curvature is identified on the full sample only.

### 2.7 Bitcoin Cycle Memo – July 2026 (15 Jul 2026)

- **Header:** BTC ≈ $65,300; WTI ≈ $79; FF 3.50–3.75%. Status "Late-stage crypto markdown, bottom-watch window open".
- **Terminology note in the memo:** "ROI denotes a normalized price ratio, calculated as current price divided by the stated reference price". So 0.520 from peak means −48%.
- **Risk Scorecard** (normalized 0–1 risk; current / 6M ago / 1Y ago / 4Y ago):

  | Metric | Now | 6M | 1Y | 4Y |
  |---|---|---|---|---|
  | Total market cap risk | 0.383 | 0.381 | 0.595 | 0.201 |
  | Bitcoin risk | 0.311 | 0.317 | 0.582 | 0.197 |
  | Total crypto market cap | 0.054 | 0.067 | 0.302 | 0.271 |
  | Running ROI | 0.349 | 0.385 | 0.674 | 0.329 |
  | On-chain risk | 0.188 | 0.193 | 0.584 | 0.119 |
  | MVRV | 0.314 | 0.320 | 0.728 | 0.157 |
  | MVRV Z-Score | 0.200 | 0.205 | 0.530 | 0.101 |
  | Supply profit/loss composite risk | 0.226 | 0.165 | 0.989 | 0.240 |
  | RHODL | 0.290 | 0.230 | 0.427 | 0.235 |
  | Puell | 0.347 | 0.308 | 0.680 | 0.119 |
  | Terminal price | 0.255 | 0.255 | 0.609 | 0.106 |
  | Market cap to thermocap | 0.148 | 0.168 | 0.636 | 0.096 |
  | Miner cap to thermocap | 0.054 | 0.068 | 0.777 | 0.146 |
  | Cowen corridor | 0.199 | 0.195 | 0.470 | 0.000 |
  | **Transaction fees** | 0.000 | 0.000 | 0.106 | 0.183 |
  | Social risk (composite) | 0.237 | 0.293 | 0.529 | 0.000 |
  | Fear & greed | 0.024 | 0.000 | 0.617 | 0.000 |
  | Google Trends | 0.146 | 0.212 | 0.147 | 0.278 |
  | App ranking (Coinbase) | 0.256 | 0.271 | 0.828 | 0.536 |
  | YouTube views | 0.059 | 0.154 | 0.352 | 0.547 |
  | X followers (analysts) | 0.374 | 0.361 | 0.322 | 0.492 |
  | X followers (exchanges) | 0.429 | 0.067 | 0.424 | 0.644 |
  | X followers (Layer 1s) | 0.404 | 0.307 | 0.392 | 0.417 |
  | Wikipedia page views | 0.154 | 0.153 | 0.353 | 0.401 |

  - His reading of the table: valuation and on-chain measures are *above* their July 2022 levels, while attention measures are *below* them. That means the market is "not yet as valuation-distressed as the mid-2022" selloff, with less attention.
  - He calls the X-follower series noisy and "low-conviction".
- **Other indicators:**
  1. BTC drawdowns from the QT-peak, 2019 vs 2025
  2. ROI from each cycle's peak
  3. Normalized price from each cycle's bottom (4.12×)
  4. BTC YTD ROI vs midterm average
  5. **Monthly returns in midterm years table**
  6. **Presidential term return paths (BTC rebased to 100 at each inauguration)**
  7. BTC weekly vs 200W SMA (≈$63,100)
  8. Price vs realized (≈$53,000) and balanced price (≈$37,700); terminal price ≈ $320,000
  9. Asymmetric quantile fan: 1st percentile ≈ $65,500, median ≈ $116,000, 99th ≈ $202,000
  10. MVRV Z raw 0.395
  11. Total on-chain risk 0.188
  12. % supply in profit 56.83% / loss 43.15%
  13. **New views across major crypto YouTube channels** (≈389,000 vs ≈4 million at the 2021 peak)
  14. New social risk 0.237
  15. 365-day running ROI 0.555
  16. A/D index top 100 ≈ −8.14K (record low)
  17. ITC Liquidity Risk 0.809
  18. BTC.D ex-stables 66.8% (from ~40% at the 2021 low)
  19. HODL waves
  20. ETF holdings (~640K → peak >1.25M BTC, now below)
  21. Headline inflation 3.46%
- **Theses and numbers:**
  - The 2019 analog: both tops came on apathy, before QT ended (~5 weeks before in 2019, ~8 weeks before in 2025), with no durable rotation. The current cycle is at day 282 since the top vs the analog's day-261 COVID low, so "the analog … is beginning to outlast" its window.
  - "Base case here is a reset completed through time rather than through a comparable flush."
  - **Cycle day counts from the 21 Nov 2022 low:** day 1,332 now; the prior two cycles bottomed at day 1,424 and day 1,432, so the low is due "roughly ninety to one hundred days out … in October". This cycle peaked at day 1,050 vs 1,061 and 1,068 before. [I: 1,424/1,432 days after 21 Nov 2022 = 15 Oct / 23 Oct 2026; 1,050 days = 6 Oct 2025 ✔.]
  - He states an earlier version wrongly anchored on the 9 Nov 2022 FTX low. This explains the inconsistent day counts in the inventory's §1.8.
  - **Midterm months:** Aug and Sep were negative in all three prior midterms (Aug ≈ −18%, −15%, −15%). July tends to be green.
  - The midterm decay gives a year-end ROI of about 0.49. With a 1 Jan anchor near $89,300, that is about **$43,800**, below realized price.
  - "The MVRV Z-Score cannot reset below zero while price holds above realized price." A time-only reset is "not sufficient" for the on-chain condition.
  - The 200W reclaim is "not a bottom signal" (in 2022 there was a break, a reclaim, and a second break).
  - A sustained reclaim of the **50W (two consecutive weekly closes)** gives stronger confirmation than a 200W reclaim.
  - The supply P/L cross "marks the window in which bottoms have historically formed", not the bottom itself.
  - "The series has been better on direction than on level": the February $60k "plausible floor" broke in June.
  - Gold rose while BTC fell, so "a single real-rate or liquidity story does not explain both".
  - The memo includes a section titled **"The Bull Case in Its Strongest Form"**.
- **Macro context:**
  - June core CPI 2.6% (vs 2.8% expected); PPI 5.5% (vs 6.2% expected).
  - Oil went from the high $50s (Dec) to a spring peak of $113–118, fell to the high $60s, and is back at ~$79. Brent topped $86 on tanker attacks.
  - The Warsh Fed cut its statement to about 130 words, removed the easing bias, and close to half of the 18 participants pencil in a hike.
  - Futures (10:00 ET, 15 Jul): July hold ≈ 90%; September 50/50; December ~70% for at least one hike.
- **Forecasts:**
  - "Primary bottom window: fourth quarter 2026", with a spill into January possible (2015 precedent). Cycle duration says October.
  - The bear framework stays intact unless BTC gets two weekly closes above the 50W (~$86,500).
  - Accelerant: a volume-spike capitulation.
  - "The low most likely a matter of months rather than weeks away."

### 2.8 The Balance of Risks (15 Aug 2026)

- **Header:** S&P ≈ 7,786 (intraday record 7,815); gold ≈ $4,370; BTC ≈ $63,000; WTI ≈ $82; FF 3.50–3.75%. Status "Late-cycle expansion, resilient equities, midterm correction window approaching".
- **Snapshot table (current vs ~3 months ago):**

  | Reading | Now | ~3M ago |
  |---|---|---|
  | S&P YTD ROI | 1.137 | — |
  | ITC Liquidity Risk | 0.813 | ≈0.80 |
  | **NDXE/NDX** | ≈0.35 | ≈0.34 |
  | BTC ROI from cycle bottom | ≈4.0× | ≈5.0× |
  | BTC YTD ROI | 0.714 | — |
  | BTC.D ex-stables | 67.37% | — |
  | Gold YTD ROI | 1.010 | — |
  | WTI | $82.39 | ≈$109 (May) |
  | DXY | 99.9 | — |
  | **GDP-weighted global policy rate** | 3.42% | — |
  | CPI (July) | 3.4% | — |
  | Core CPI (July) | 2.5% | — |
  | Unemployment | 4.1% | — |
  | Payrolls YoY | +0.20% | — |
  | **GDP-weighted global unemployment** | 4.49% | — |
  | Macro recession risk | 0.024 | — |

- **Further figures:**
  1. **National Financial Conditions Index** (−0.549)
  2. Macro recession-risk composite with its four component legs
  3. 10Y–3M spread (+0.76%)
  4. NDXE/NDX
  5. **Case-Shiller national HPI YoY** (1.6%, peak ~21% in 2022)
  6. Housing under construction (~1.7M peak → ~1.26M)
  7. New-home for-sale-to-sold ratio / months' supply 9.3
  8. Median new home price ≈ $398,000
  9. S&P YTD vs midterm years
  10. **S&P 500 monthly returns for every midterm year since 1930**
  11. Shiller CAPE 41.2, trailing P/E ≈ 28, earnings yield 3.56%, excess CAPE yield ≈ 0.97% (published Shiller version ≈ 1.4%)
  12. Payrolls YoY
  13. Unemployment rate
  14. GDP-weighted unemployment (16 largest economies)
  15. Initial claims 209k
  16. Job openings per unemployed (~2.0 → ~1.0)
  17. CPI and core CPI with SPX
  18. Policy rates across major central banks
  19. GDP-weighted global policy rate (17 central banks; trough 0.82% Feb 2021, peak 4.60% Feb 2024)
  20. **US Dollar Index rebased to 100 at each presidential inauguration** (current term ≈ 91.5)
  21. **XLE**, with a table of energy peaks vs S&P peaks
  22. WTI monthly
  23. Gold YTD ROI vs midterm years
  24. Composite on-chain risk (0.181)
  25. BTC.D ex-stables (67%; ~41% at the 2021 peak)
  26. BTC ROI from cycle bottom
  27. BTC YTD ROI vs midterm average
- **Theses:**
  - Risk climbs the **quality ladder**: alts → BTC, speculative growth → cash flow, small → large caps. "New highs at the top of the quality ladder are what the late stage of the ladder looks like."
  - "Restrictive policy alongside loose financial conditions" is the "hallmark of a mature expansion". An NFCI move above zero would be the early warning.
  - The recession composite's interest-rate leg "tends to lead" but is "the noisiest … most prone to false positives" (late 1990s, 2022–26).
  - Recession tends to arrive after dis-inversion. The 10Y–3M has been positive since late 2024, which makes the re-steepening "unusually mature".
  - **Payrolls YoY turning negative** has coincided with recessions; it is a "particularly clean confirmation" but can lag.
  - The labor market is "low-hiring, low-firing". The unemployment fall to 4.1% is partly participation (−264k left the labor force; participation 61.4%). July payrolls −23k with −103k revisions.
  - The regime switch needs a **cluster**: negative YoY payrolls, rising claims, rising unemployment, and a rising composite.
  - The June SEP was split 9 (hike) / 8 (hold) / 1 (cut). July was a 9–3 hold with three hike dissents.
  - Warsh offers "little in the way of forward guidance" and frames inflation "as a choice rather than an accident".
  - The US is "lagging the global turn": Australia and South Korea hiked, Japan is normalizing, and the 2Y JGB is ≈ 1.70%.
  - Dollar: bullish lean from the 2017 first-term analog. He calls this "deliberately the lightest evidentiary leg". Falsifier: a decisive break to new lows for the term.
  - Energy tops after the index: S&P peak Mar 2000 → XLE May 2001 (~14 months); Oct 2007 → May 2008 (~7 months). "Two out of two is a tendency."
  - Gold: on average the midterm low comes in summer, but 2018 was late summer and 2022 was Sep–Nov. 2026 may be "a reset year" like 2022.
  - BTC: "has historically bottomed during the equity correction rather than ahead of it". This cycle's peak multiple was ~8× from the bottom vs ~22× in the prior cycle.
  - On-chain composite components are named: MVRV, MVRV-Z, Puell, RHODL, market-cap-to-thermocap, supply in profit.
  - Midterm drawdown magnitudes: ~7% (2014), ~20% (2018), ~25% (2022). Of the ~two dozen midterms since 1930, September is weakest, and October and November close as the two strongest, though October often prints the intra-month low.
- **Self-scored record:**
  - Q4-2025 top: confirmed.
  - January capital preservation: "confirmed (crypto), mixed (equities)", since the S&P was +13.7% YTD.
  - Feb–Mar equity weakness late-cycle, not recession: confirmed to date.
  - Trapped hawkish Fed: confirmed to date.
  - Equities-vs-gold transmission: open.
- **Forecasts (scenario weights):**
  - ~65%: midterm correction into Q4, then recovery.
  - ~20%: deeper policy-error correction (energy re-accelerates and the Fed hikes).
  - ~15%: recessionary transition.
  - Equity correction "begins in late Q3 and bottoms in the window from September into the fourth quarter".
  - BTC low in Q4 during that correction; bottom-watch near $63k.
  - Dollar to firm; gold near-term two-sided (a temporary retest is possible); energy constructive.
- **Refutation cluster for the correction call:** equal-weight/cap-weight ratio turning up; liquidity risk leaving the tight band; financial conditions staying loose; BTC reclaiming the longer weekly MAs; the dollar breaking to new lows.

### 2.9 The Triple Squeeze (30 Sep 2026)

- **Header:** S&P ≈ 7,710; gold ≈ $4,210; BTC ≈ $83,000; WTI ≈ $90 (Nov); 10Y ≈ 5.29%; 30Y ≈ 5.64%; DXY ≈ 101.35; FF 3.75–4.00%. Risk drivers: oil and Hormuz; the long end repricing; small caps rolling over; the October FOMC and the timing of the yield top.
- **Cross-asset snapshot:**
  - 10Y +50 bp in 4 weeks, +110 bp in 12 months; highest since Jun 2007.
  - 2Y ≈ 4.89%; 20Y ≈ 5.69% (the highest point on the curve).
  - Dec Brent ≈ $97 / Nov WTI ≈ $90 (spread ≈ $7).
  - DXY "higher lows since February" (low ≈ 96.5), July high ≈ 101.8.
  - Gold −3% YTD, ~24% below the January ≈ $5,560 high.
  - S&P +12.5% YTD with ~48% of stocks above their 200D, a combination "last seen around 1998 to 2000".
  - October hike odds 35–42% after PCE (from ~70%).
- **Indicators (figures):**
  1. US Treasury yield curve (25 Sep): 1-month bill ~3.93%, 6M ~4.34%, 1Y ~4.55%
  2. **US10Y YTD ROI 2026 vs 2018 and 2022**
  3. Headline PCE YoY vs S&P (revised series)
  4. WTI monthly vs S&P
  5. DXY vs S&P
  6. Effective FFR vs 2Y yield
  7. **XAUUSD YTD ROI 2026 vs 2018 and 2022**
  8. S&P YTD ROI 2026 vs 2018 and 2022
  9. **S&P 600 vs S&P 500, 2018**
  10. S&P 600 vs S&P 500, 2026
  11. BTC YTD ROI 2026 vs 2018 and 2022
  12. **BTC ROI in the year after the September rate hike in each midterm year** (2018, 2022, 2026)
  13. **BTC ROI in the year after the first hike of a tightening cycle** (Dec 2015, Mar 2022, Sep 2026)
  - Plus three tables, given in the next three items.
- **Table 1: 10Y peaks and what followed:**

  | 10Y peak | Level | What followed | Timing |
  |---|---|---|---|
  | Oct 2023 | ~5.0% | No growth scare | — |
  | Oct 2022 | ~4.3% | SVB | ~4.5 months |
  | Nov 2018 | ~3.2% | Selloff already underway | — |
  | Dec 2013 | ~3.0% | EM turmoil | ~1 month |
  | Feb 2011 | ~3.7% | Euro / debt-ceiling stress | ~2–6 months |
  | Jun 2007 | ~5.3% | Credit stress | ~2 months; recession ~6 months |
  | Jan 2000 | ~6.8% | Equity and tech peak | ~2 months; recession ~14 months |
  | Nov 1994 | ~8.1% | Peso crisis | ~1 month |

  He flags this as "a hand-picked set of peaks".
- **Table 2: gold, DXY and 10Y turning points.** Gold's initial low came 2–12 weeks before the 10Y peak, near DXY highs:

  | Episode | DXY peak | Gold low | 10Y peak | Gold lead |
  |---|---|---|---|---|
  | 2023 | ~107 | ~$1,810 | ~5.0% | ~2 weeks |
  | 2022 | ~115 | ~$1,615 | ~4.3% | ~3 weeks |
  | 2018 | ~97 | ~$1,160 | ~3.2% | ~12 weeks |

- **Table 3: midterm-year 10Y peaks vs SPX low and the Fed:**
  - 2022: yield top ≈ equity low; step-down signaled.
  - 2018: SPX −16% from yield top to 24 Dec; Fed hiked 19 Dec with "QT on autopilot".
  - 2006: yield top ≈ equity low after an ~8% correction; final hike 29 Jun, then a pause.
- **Theses:**
  - The **squeeze loop, 6 steps:**
    1. Oil up → headline and breakevens up.
    2. Yields follow; the long end adds term premium.
    3. The dollar firms on relative real rates.
    4. Non-yielding assets de-rate (gold on opportunity cost, long-duration equities on discount rate).
    5. Costs bite (mortgages, autos, refinancing, fuel).
    6. Demand weakens.
    - Oil rolled over before the 10Y: ~5 weeks in 2018, ~4 months in 2022.
  - "When yields fall primarily because growth is breaking", that is worse for risk than yields falling because inflation cools.
  - A 10Y top can also reflect lower inflation expectations, Fed expectations, term premium or flight to quality, "so the signal is not specific to growth".
  - The gap between the 2Y and EFFR is ~100 bp. It "does not map one-for-one" onto hikes. CME FedWatch modal path: 4.50–4.75% by Mar 2027, 4.75–5.00% by Jul 2027.
  - The long end has topped before the gap closed (2018 ~75 bp, 2022 >100 bp).
  - "When [the 2Y] stops making new highs, the market is signaling that the tightening cycle is largely priced". It works "better as confirmation than as a lead".
  - The gold signal for a low: "the dollar failing to make new highs while the 10Y is still printing them" (**dollar-yield divergence**).
  - The Fed's stance near the yield peak decides whether the yield top marks the equity low (2022, 2006) or precedes a larger leg (2018). "2026 currently looks closer to the second case."
  - Small caps lead the S&P: in 2018 the S&P broke 4–5 weeks after the small-cap top. In 2026 we are "six weeks past" it.
  - The August PCE (3.4% headline / 3.0% core vs 3.7%/3.3% consensus) was distorted by the **BEA annual revision** (software, investment management and legal services re-measured).
  - The September hike "looks more like the resumption of an existing cycle, similar to 1999 after the 1998 insurance cuts", not a liftoff like 2015 or 2022.
  - First-hike lens:
    - After Dec 2015, BTC fell ~20% in two months, then rose ~70% over twelve.
    - After Mar 2022, BTC rose ~12% in two weeks, then fell >60%.
    - 2026 resembles early 2022.
- **"Bitcoin: Where We Were Wrong":** "We did not think BTC would take out its May high, and it has." "The burden of proof has shifted to the bears."
- **Forecasts / signals into Q4:**
  - Gold "likely closer to a low than a high, even if it undercuts prior lows first".
  - The long end "can still grind higher".
  - Any correction = "a growth scare … with the broader cycle intact".
  - BTC: holding above ~$83k keeps the breakout; "a weekly close back below that area would materially weaken the breakout case".
  - Midterm-hike analog: break around day 50 after 16 Sep, i.e. early November. A 2022-type −15% puts BTC near $64k; a 2018-type −50% near $38k.
  - DXY: a break above 101.8 tightens further.
  - October FOMC: a hike with hawkish guidance keeps the 2018 path; a hike with a step-down signal looks like 2022.

### 2.10 Ethereum Letters (2020, page dated 20 Feb 2020; PDF gated)

- Page summary only [V]. The text reads as a 2026 retrospective framing of the 2020 work.
- ETH is "fundamentally different from Bitcoin" and not just higher-beta BTC. "ETH/BTC dynamics … often provide more actionable information than absolute price levels."
- Emphasis on model uncertainty, risk dispersion, and wider outcome distributions in tightening regimes.
- No forecasts are visible.

### 2.11 Bitcoin Letters (2020, page dated 5 Jan 2020; PDF gated)

- Page summary only [V].
- Themes: diminishing returns; **volatility compression**; "marginal return per unit of risk declined".
- "The framework … deliberately omits price targets". It identifies **risk regimes** and challenges "rigid cycle narratives" in favor of probabilistic outcomes.
- No forecasts are visible.

---

## 3. NEW versus the inventory (not in the inventory's master table §1 or vocabulary §5)

"Platform only" means the series appears only in the inventory's §1b ITC catalogue list, not in the master table or vocabulary. Treat these as new for course coverage.

### 3.1 Indicators and charts

| # | Indicator / chart (exact name used) | Definition | How Cowen uses it | Report(s) |
|---|---|---|---|---|
| 1 | **National Financial Conditions Index (NFCI)**, also "Chicago Financial Conditions Index" (platform only) | Chicago Fed weekly index of risk, credit and leverage conditions. 0 = average, <0 = looser than average | Contrasts *market* conditions (loose, −0.549) with *policy* liquidity (tight, 0.813). Tight policy plus loose FCI = mature expansion. A move above 0 is "the early warning". It is one of the observables defining his 3 scenario states | Feb (Fig 15), Aug (Fig 2, Bottom Line) [V] |
| 2 | **Nasdaq-100 equal-weight ÷ cap-weight (NDXE/NDX)** | Ratio of the equal-weighted to the cap-weighted Nasdaq-100. Falling = gains concentrated in mega-caps | Equity-side analog of BTC dominance: ~0.50 (2020) → ~0.35. "Equal-weight to cap-weight ratio turning up" is part of the refutation cluster | Aug [V] |
| 3 | **S&P 600 small caps vs S&P 500** (divergence as a lead) | Relative path of small caps vs large caps | In 2018 small caps topped late Aug and the S&P broke ~4–5 weeks later; both bottomed 24 Dec. In 2026 the S&P 600 is −9% since mid-Aug, a "warning". The inventory mentions the S&P 600 only as a breadth chart | Sep (Figs 9–10) [V] |
| 4 | **10Y (and gold, BTC, S&P) year-to-date ROI vs 2018 and 2022** | Each asset's price ÷ its 1 Jan price, overlaid on analog years | Applies his midterm-overlay method to *yields* and *gold*, not just BTC/SPX. The 10Y is +27% YTD and "converged on the 2018 path" | Sep (Figs 2, 7, 8, 11) [V] |
| 5 | **Full Treasury yield curve snapshot** (1M bill to 30Y) | Yield by maturity on one date | Reads the shape: steepening "from the long end"; 20Y highest point; bills climbing = front end pricing more hikes | Sep (Fig 1) [V] |
| 6 | **"10Y local and cycle peaks and what followed" table** (1994–2023) | Dated 10Y peaks with the stress episodes after them | "Sequence risk": watch for a growth scare "around and after the 10Y top". Flagged by him as hand-picked | Sep (Table 1) [V] |
| 7 | **Gold / DXY / 10Y turning-point table** and the **dollar-yield divergence** signal | Dates of DXY peak, gold low and 10Y peak per episode | Gold bottomed 2–12 weeks before the 10Y peak, near DXY highs. Watch for DXY failing to make new highs while the 10Y still does | Sep (Table 2) [V] |
| 8 | **Midterm-year 10Y peak vs SPX low and Fed stance table** (2006, 2018, 2022) | Whether the yield top coincided with the equity low | The Fed's posture near the peak decides it: step-down/pause → yield top ≈ equity low; still hiking → larger leg later | Sep (Table 3) [V] |
| 9 | **Breakeven inflation** (as a step of the squeeze loop) | Nominal minus TIPS real yield = market inflation expectation | Step 1 of the loop: oil up → breakevens reprice higher. The inventory lists breakevens as *missing* from ITC | Sep [V] |
| 10 | **2Y yield "stops making new highs"** | Peak in the 2Y Treasury | Confirmation that the tightening cycle "is largely priced". In 2018/2023 the 2Y and 10Y peaked together; in 2022 the 10Y peaked weeks earlier | Sep, May ("Fed policy tends to follow the front end") [V] |
| 11 | **BEA annual revision** (data-vintage effect) | Periodic re-measurement of national-accounts and PCE series | Part of the Aug PCE "surprise" came from revised series (July revised 3.7/3.3 → 3.4/3.0). Data literacy point | Sep [V] |
| 12 | **GDP-weighted unemployment rate** (16 largest economies, ITC) | National unemployment rates weighted by nominal GDP. Read for direction only, because definitions differ | 4.49% and falling, so global labor slack is not building. Recessions show as sharp rises (+2.6 pt 2008–09; +3.3 pt H1 2020) | Aug (Fig 12) [V] |
| 13 | **Policy rates across major central banks** and the **2Y JGB yield** | Individual central-bank policy rates; Japan's 2-year government bond yield | The US is "lagging the global turn": Australia and South Korea hiked, the BoJ is normalizing, 2Y JGB ≈ 1.70% (multi-year high) | Aug (Figs 17–18) [V] |
| 14 | **FOMC dissent count, SEP hike tally, statement length / forward-guidance removal** | Committee split signals beyond the dot-plot median | July 9–3 with 3 hike dissents; June SEP 9 hike / 8 hold / 1 cut; Warsh statement ≈ 130 words with the easing bias removed. He reads these as a hawkish reaction function | Jul, Aug [V] |
| 15 | **Temporary help services employment** | BLS payroll employment in temp agencies | An early-cycle labor tell: firms cut flexible labor first. "Softened … recent stabilization" | May (Fig 7) [V] |
| 16 | **Payrolls YoY turning negative** as the recession-confirmation line | 12-month % change in nonfarm payrolls | The "measure that matters most for cycle timing". Negative = recession confirmation, but it can lag. +0.20% in Aug 2026 | May (Fig 8), Aug (Fig 10) [V] |
| 17 | **Recession-composite legs**: Employment Risk Indicator; National Income and Product Risk Indicator; Production and Business Risk Indicator; interest-rate leg | ITC sub-scores (0–1) of the Macro Recession Risk composite | Each read separately. The interest-rate leg "tends to lead" but is the noisiest (false positives in the late 1990s and 2022–26). No single leg should carry the regime call | Q1 (Figs 12–14), Feb (Figs 22–24), Aug (Fig 3) [V] |
| 18 | **Housing set**: Case-Shiller national HPI YoY; purchase-only HPI YoY; housing units under construction; median listing prices; new-home for-sale/sold (months' supply); median new home price (platform only) | Standard housing price and activity series | "Cooling … not breaking": HPI +1.6% YoY (peak ~21% in 2022); under construction 1.7M → 1.26M; months' supply 9.3; median new home ≈ $398k. A break would need a labor shock | Feb (Figs 16–18), Aug (Fig 6) [V] |
| 19 | **International vs US equities** (relative performance) | Non-US index ÷ US index | With high US policy uncertainty and a softer dollar, internationals outperform. A 2018-style dollar rally would reverse that | Feb [V] |
| 20 | **Energy Select Sector SPDR (XLE) peak lag table** | Dates of XLE vs S&P cycle peaks | Energy topped ~14 months (2000→2001) and ~7 months (2007→2008) *after* the S&P. With the sample at two, energy at new highs alongside the index "is consistent with a cycle that still has room to run". The inventory only says "energy stocks top last" | Aug (Table 1, Fig 20) [V] |
| 21 | **US Dollar Index rebased to 100 at each presidential inauguration** (platform only: "presidential-term paths") | DXY path through each term, aligned at inauguration | 2025 term replicated 2017's year-1 decline; the turn in year 2 is "late" (≈91.5 rebased). His explicit "lightest evidentiary leg" | Aug (Fig 19) [V] |
| 22 | **Bitcoin rebased to 100 at each inauguration** | Same idea for BTC | Prior term's low came "near the midterm elections". Restates the midterm lens and is "not fresh evidence" | Jul (Fig 5) [V] |
| 23 | **S&P 500 monthly returns in every midterm year since 1930** (table with average and SD) | Month-by-month returns, ~24 midterm years | September weakest; October and November the two *strongest* closes, though October often prints the intra-month low (2014, 2022). The inventory only says "September weakest" | Aug (Fig 8) [V] |
| 24 | **BTC monthly returns in midterm years** (2014, 2018, 2022, 2026) | Calendar-month % returns | Aug and Sep negative in all three prior midterms; Aug ≈ −18/−15/−15%. July tends green | Jul [V] |
| 25 | **Gold YTD ROI vs midterm years / gold's midterm low window** | Gold path in midterm years | Long-run average low in summer; 2018 late summer, 2022 Sep–Nov. 2026 "may still prove to be a reset year" | Aug (Fig 22), Sep (Fig 7) [V] |
| 26 | **Trailing P/E (~28) and earnings yield (3.56%)**; excess CAPE yield definitional caveat | Index price ÷ trailing EPS; its inverse. ITC's excess CAPE yield uses an ex-post real yield (0.97%) vs Shiller's published ≈ 1.4% | Valuation "cushion" rather than a trigger. A CAPE of 41 "reached on positive earnings growth is a less fragile animal" | Aug (Fig 9) [V] |
| 27 | **180-day Bitcoin volatility** | Rolling 180-day realized volatility | "Low volatility at cycle highs is not stability, but rather fragility." Constructive re-expansion is one reversal condition. The 2020 letters also stress volatility compression | Q1 (Fig 11); Bitcoin Letters page [V] |
| 28 | **Crypto, equity and metals correlation heatmap** | Matrix of rolling correlations | Weak crypto–equity correlation while metals track macro assets = "segmentation of capital". The inventory's correlation row only covers single-pair coefficients | Q1 (Fig 15) [V] |
| 29 | **BTC/SPX overlay** | BTC priced in S&P terms, with the S&P overlaid | BTC weakens vs equities *before* equities show stress (2019). Evidence for the risk-down-the-curve order | Feb (Fig 27) [V] |
| 30 | **BTC drawdown from the QT-peak overlay, 2019 vs 2025** (aligned to QT-end framing) | ROI from peak with paths aligned by the QT-ending timeline | The core 2019-analog chart. The 2019 path ends at its day-261 COVID low (~0.29); 2025 at day 282 ≈ 0.52 | Q1 (Figs 4–5), Q2 (Fig 10), Jul (Fig 1) [V] |
| 31 | **BTC ROI after the first hike of a tightening cycle** (Dec 2015, Mar 2022, Sep 2026) | Price ÷ hike-day price | Wider spread than the midterm lens: 2015 −20% then +70%; 2022 +12% then −60%. 2026 resembled early 2022 | Sep (Fig 13) [V] |
| 32 | **Risk Scorecard** (normalized 0–1 risk for ~22 indicators, with 6M / 1Y / 4Y comparison) | Each indicator mapped to the ITC 0–1 risk scale and tabulated through time | Shows broad one-year de-risking. The split vs July 2022 (valuation higher, attention lower) is "the apathy signature stated in comparative terms" | Jul [V] |
| 33 | **Transaction fees (risk)**, **Miner cap to thermocap (risk)**, **Running ROI (risk)**, **Supply profit/loss composite risk** | Normalized risk versions of fee revenue, miner-revenue-based thermocap ratio, trailing return, and supply P/L | Scorecard rows: fees 0.000, miner cap/thermocap 0.054, running ROI 0.349, supply P/L composite 0.226. The inventory names MCTC only as a 2025 video topic and has no fee metric | Jul [V] |
| 34 | **New views across major crypto YouTube channels** (raw count) | Count of new views on a basket of crypto channels | ≈389k vs ≈4M at the 2021 peak, "an order of magnitude" lower. Raw evidence under social risk | Jul (Fig 12) [V] |
| 35 | **Public company Bitcoin holdings** (treasury companies) as "structural demand" | BTC held by listed companies | Still rising while ETF holdings plateau, so a "foundation for stability", not a catalyst. The inventory only mentions treasury-company narratives as unreliable timing tools | Q2 (Fig 17) [V] |
| 36 | **ETF holdings as % of supply / BTC count** | Spot-ETF BTC ÷ circulating supply | 6.77% of supply (Apr); ~640K → >1.25M BTC peak (late 2025), now falling. "From a driver of price appreciation to a stabilizing component" | Q2, Jul (Fig 19) [V] |
| 37 | **Global M2 year-over-year change** | YoY % change of aggregated global M2 | Slope matters more than level. BTC "peaked before M2 rolled over and … bottomed shortly after M2 peaked". The inventory has global M2 as a rare contrarian topic only | Feb (Fig 4) [V] |
| 38 | **Asymmetric quantile fan: current band values** | Fitted 1% / 50% / 99% quantiles | Jul 2026: price "essentially on" the 1st percentile (~$65.5k); median ~$116k; 99th ~$202k. The 1% band has been undercut before (late-2010 −12.2%; FTX 40 days) | Jul (Fig 8) [V] |

### 3.2 Concepts, terms and vocabulary (not in inventory §5)

| Term | Meaning as he uses it | Report(s) |
|---|---|---|
| **ROI as a normalized price ratio** | "Current price divided by the stated reference price", not a % return. 0.520 from peak = −48%; YTD 0.731 = −26.9%. Needed to read every ITC overlay | Jul (explicit), Aug, Sep [V] |
| **Quality ladder** | In tightening, capital moves *up quality within each asset class* (alts → BTC; small → large caps; speculative growth → cash flow). Index records are "the top of the ladder … not the edge of a cliff" | Feb, Jul, Aug [V] |
| **Flight-to-quality bull market** | A rally in tight liquidity with narrowing leadership (2006–07, 2023–25) | Feb [V] |
| **Restrictive digestion / post-cycle digestion phase** | His regime label for 2026: tightening has stopped but conditions are still restrictive, so excess is absorbed slowly | Q1, Feb, Mar [V] |
| **Liquidity level vs liquidity direction; liquidity stabilization vs liquidity impulse; slope of liquidity** | Less tightening ≠ easy conditions. Durable risk expansion needs an *impulse*, not stabilization | Feb, Jul [V] |
| **Speculative liquidity** | Capital "both abundant and willing to take risk", as opposed to aggregate liquidity. Reserve-management balance-sheet growth is not it | Q1 [V] |
| **Equity durability (as labor transmission mechanism)** | How *long* equities stay down determines whether firms cut jobs. "The magnitude of a correction matters less than its duration" | Feb [V] |
| **Nonlinear break / nonlinear phase / layoffs-first** | Unemployment can drift up for long periods; recession starts when layoffs accelerate and feed back. "Recessions typically do not begin with slower hiring" | Q1, Feb, Mar, May [V] |
| **Low-hiring, low-firing labor market** | Unemployment can fall while payroll momentum stalls | Aug [V] |
| **Recession cluster** | Regime change needs several signals at once: YoY payrolls < 0, rising claims, rising unemployment, composite up, NFCI toward/through 0 | Aug [V] |
| **Restrictive policy + loose financial conditions** | "Hallmark of a mature expansion"; makes "the eventual turn abrupt" | Aug [V] |
| **Triple squeeze** | Rising yields + rising oil + firming dollar as one tightening impulse | Sep [V] |
| **Rate shock / sequence risk** | Order of turns: gold first, long end next, stress around or after the yield top | Sep [V] |
| **Growth scare inside an intact cycle** | A correction that recovers without recession (2018 template) | Sep [V] |
| **Policy-error correction** | The 20% state: energy re-accelerates and the Fed hikes into stalling labor | Aug [V] |
| **Resumption hike vs liftoff; "insurance cuts"** | Sep 2026 reverses the last of ~175 bp of 2024–25 cuts within the same cycle, like 1999 after the 1998 insurance cuts. Not a liftoff from zero (2015, 2022) | Sep [V] |
| **Durable rotation** (into higher-risk crypto) | "A sustained decline in Bitcoin dominance excluding stablecoins, persisting over months rather than weeks". Isolated alt rallies do not count | Jul (sources note) [V] |
| **Demand exhaustion (vs overheating) top** | The 2025 top came as marginal buyers ran out, not as on-chain euphoria | Q1 [V] |
| **Cycle status / Regime characteristics / Recommended posture / Primary risk drivers** | Fixed memo header taxonomy. Postures used: "Capital preservation and tactical positioning", "… with selective deployment", "Defensive positioning with tactical deployment", "patience over aggressive deployment" | All 2026 memos [V] |
| **Risk asymmetry / tactical vs structural rally** | Whether the forward return distribution is skewed; rallies on positioning vs on improving liquidity and participation | Q1, Q2 [V] |
| **"What would change this view" / refutation cluster / falsifier** | Each memo lists observable conditions that would invalidate it | Q1, Feb, Jul, Aug, Sep [V] |
| **Scenario distribution with observable state definitions** | 65/20/15 weights ("subjective base rates") tied to measurable conditions | Aug [V] |
| **Framework scorecard ("confirmed / confirmed to date / open / mixed")** | Self-grading of prior calls, including forgone equity upside | Aug [V] |
| **"The Bull Case in Its Strongest Form" / "Where We Were Wrong"** | Steel-manning sections | Jul, Sep [V] |
| **ITC Risk Cascade Framework (5 stages)** | See §4 | Mar [V] |
| **Recession feedback loop (7 steps)** | Asset prices → financial conditions → confidence → hiring and layoffs → consumption → activity → more layoffs | May [V] |
| **Squeeze loop (6 steps)** | Oil → yields → dollar → non-yielding assets → costs → demand | Sep [V] |
| **Quantile-regression vocabulary** | *Conditional quantile*; *check-loss (pinball loss)*; *rearrangement estimator* (non-crossing quantiles); *block bootstrap*; *expanding-window out-of-sample*; *upper- vs lower-tail curvature (b_HI, b_LO)*; *structural support vs speculative excess*; *diminishing reflexivity*; *genesis-date sensitivity* | May (paper) [V] |
| **Structural vs speculative component** | The price floor follows a power law (monetization). The speculative multiplier decays as market cap grows. This is the formal version of diminishing returns | May (paper) [V] |
| **Risk regimes (2020)** | Periods when risk-adjusted returns favor exposure vs when downside dominates. He states the 2020 framework had no price targets | Bitcoin Letters page [V] |

---

## 4. Theses and causal chains that the inventory's §2 lacks or states differently

Dated by report. Status is versus inventory §2 (T1–T23).

1. **Risk cascade has five stages, not four, and he placed March 2026 "between Stage 3 and Stage 4"** (15 Mar 2026) [V].
   - The stages: participation ↓ → speculative assets ↓ → equities ↓ vs gold → financial conditions tighten via dollar/oil "even if central banks begin shifting toward easing" → labor feedback loop.
   - *Inventory T12 gives a 4-step chain without the explicit staging.*
   - *[I] Outcome:* SPX/gold went from ≈ 1.32 (6,632 / 5,018 on 15 Mar) to ≈ 1.91 (7,624 / ≈ 3,990 on 23 Oct). So stage 3 reversed sharply after March.
2. **Bull markets can run in tight liquidity, but only as flight-to-quality rallies; record highs are the top of the quality ladder** (15 Feb, 15 Aug 2026) [V].
   - This reconciles his restrictive-liquidity read with S&P records.
   - *Not in inventory §2.*
3. **Liquidity: direction ≠ level; QT ending ≠ easing; Fed balance-sheet growth was "reserve management", not QE** (15 Jan, 15 Feb, 15 Jul 2026) [V].
   - Crypto bull markets historically came "when liquidity expanded in response to economic or financial stress", not when tightening merely ended.
   - *The inventory says "the end of QT is not the same as a growing balance sheet"; the memos go further: even a growing balance sheet is not enough unless it is stress-driven.*
4. **Bitcoin leads liquidity: it topped before QT ended and before M2 rolled over, and bottomed shortly after M2 peaked** (15 Jan, 15 Feb 2026) [V].
   - The quantified lag is ~5 weeks before QT end in 2019 vs ~8 weeks in 2025 (Jul memo).
   - *The inventory says "about 2 months" for both cycles. The memo gives ~5 weeks for 2019.*
5. **Equity durability is the transmission channel to labor** (15 Feb 2026) [V]. "The magnitude of a correction matters less than its duration."
   - 1998 (fast recovery, no recession) vs 2000–01 (persistent weakness → layoffs). Early 2025 = 1998.
   - The May memo adds the 7-step loop. *Inventory T7 has "asset prices must fall first" only as a video snippet [S].*
6. **Layoffs, not slower hiring, start recessions** (15 Jan, 15 Feb 2026) [V].
   - Claims and layoffs are the trigger series. Payrolls YoY < 0 is the confirmation, though it can lag (Aug).
   - "Low-hire, low-fire" explains falling unemployment with stalling payrolls (Aug).
7. **The recession composite's interest-rate leg leads but is noisy; the slow legs confirm** (15 Aug 2026) [V]. *Not in the inventory.*
8. **Tight policy plus loose financial conditions (NFCI < 0) = mature expansion that can persist, then turns abruptly** (15 Aug 2026) [V]. *Not in the inventory.*
9. **Curve: recession risk rises during re-steepening; the 10Y–3M has been positive since late 2024, so the clock is "unusually mature" but offers "little precision"** (15 Feb, 15 Aug 2026) [V].
   - The timing horizon instead rests on the labor cluster and the recession composite.
   - *Consistent with inventory row 1.2, but adds that he no longer uses the curve as a clock.*
10. **Midterm seasonality only matters when it coincides with late-cycle macro; "multiple crypto cycles can occur within a single broader business cycle"** (15 Apr 2026) [V]. *A qualification absent from inventory T9.*
11. **2019's initial ~50% drop came from liquidity; the deeper flush needed an exogenous shock (COVID). Deeper downside "may require an additional catalyst"; otherwise "time-based capitulation"** (15 Apr, 15 Jul 2026) [V].
    - July adds the arithmetic link: a genuine on-chain reset (MVRV Z < 0) requires price below realized price. So a pure time reset is "not sufficient". The seasonal decay path points to ≈ $43,800.
    - *Inventory T8 notes the missing flush. It does not have the $43.8k derivation, which explains the BeInCrypto snippet "Q4 Bitcoin bottom near $44,000" listed in the inventory's sources.*
12. **50W reclaim (two consecutive weekly closes) is the real invalidation; a 200W reclaim is "not a bottom signal"** (15 Jul 2026) [V]. 2022 had a 200W break, a reclaim, and a second break. *The inventory lists the 50W reclaim; the two-close rule and the 200W caveat are new.*
13. **Supply-in-profit/loss cross marks entry into the bottoming *window*, not the bottom** (15 Jul 2026) [V]. Whipsaw around 50% is characteristic.
14. **Cycle-duration clock (correct anchors): day 1,332 at 15 Jul from the 21 Nov 2022 low; prior bottoms at day 1,424 and 1,432; low due in October** (15 Jul 2026) [V].
    - Supersedes the inconsistent [S] day counts in the inventory's §1.8. The memo explains the earlier error (FTX 9 Nov anchor).
15. **Energy tops after the index; energy at new highs alongside the S&P means the cycle has room to run** (15 Aug 2026) [V]. XLE lagged by 14 months (2000) and 7 months (2007). *Inventory: "energy stocks top last" without the dates or the inference.*
16. **Dollar: a presidential-term (2017) analog, explicitly his weakest leg** (15 Aug 2026) [V]. *Inventory T19 covers DXY channels and 2026 higher lows, but not this analog or the self-rating.*
17. **The US lags a global re-tightening** (AU, KR, JP; global policy rate ticking up) (15 Aug 2026) [V]. *The inventory notes "the global policy rate has stopped falling" only.*
18. **Gold: midterm "reset year"; gold bottoms 2–12 weeks before the 10Y peak and near the DXY peak; watch for the dollar-yield divergence** (15 Aug, 30 Sep 2026) [V].
    - *The inventory has "gold bottoms first, then the long end tops" with no mechanism or table.*
    - Feb adds: silver tops before gold late in the cycle (1973–74, 2011).
19. **The Fed's stance at the yield top decides whether the yield top = equity low (2022, 2006) or precedes a larger leg (2018)** (30 Sep 2026) [V]. *New.*
20. **Small caps lead large caps by ~4–5 weeks at tops (2018)** (30 Sep 2026) [V]. *New.*
21. **The Sep 2026 hike is a resumption (1999 after the 1998 insurance cuts), not a liftoff** (30 Sep 2026) [V].
    - *Inventory T23 cites a "March 1997 single hike" analog via CMC Academy [S]. In the written memo the analog is **1999**. Course writers should prefer the primary text.*
22. **First-hike lens (2015 vs 2022) as a second, wider-spread BTC analog** (30 Sep 2026) [V]. *New; the inventory has only the midterm-hike lens.*
23. **Gold–BTC divergence: "a single real-rate or liquidity story does not explain both"** (15 Jul 2026) [V]. *Nuances inventory T21 and the BTC/gold row.*
24. **Correlation segmentation: equity/metal liquidity ≠ crypto speculative liquidity** (15 Jan 2026) [V]. Seen in 2019 too. *New.*
25. **Volatility compression at highs = fragility** (15 Jan 2026; also the 2020 Bitcoin Letters theme) [V]. *New.*
26. **ETF flows shift from price driver to stabilizer; company holdings = structural demand** (15 Apr, 15 Jul 2026) [V]. *The inventory frames ETFs mainly as "rolled over / did not prevent losses".*
27. **Housing slowing, not breaking** (stronger balance sheets than 2006–08; HPI +1.6%) (15 Feb, 15 Aug 2026) [V]. *The inventory treats housing as peripheral.*
28. **International equities outperform when the dollar is soft and US policy uncertainty high** (15 Feb 2026) [V]. *New.*
29. **Recession not strictly required for crypto to stabilize** (orderly cooling path) (15 Jan 2026) [V]. *Nuance absent from inventory T7/T12.*
30. **Business-cycle end "one to two years away" (May) and "another year or more" (Aug)** [V]. *The inventory has the May line. The August restatement and the 65/20/15 observable state definitions are new.*
31. **Diminishing returns formalized as decaying speculative reflexivity over a straight power-law floor** (29 May 2026) [V]. *The inventory notes the paper exists, not the mechanism.*

---

## 5. Forecasts and outcomes (checked to 30 Oct 2026)

Verdict key: **Hit / Partial / Miss / Open / Unverified**. Outcome data come from the reports' own later editions [V] and web sources [S] (listed at the end). Prices on any one date vary by source, so use them as approximate.

| Report (date, ref. level) | Forecast / call (timing) | What happened by 30 Oct 2026 | Verdict |
|---|---|---|---|
| Q1 memo (15 Jan; BTC ≈ $97,153) | Rallies "tactical rather than structural"; capital preservation; post-cycle digestion like 2019 | BTC to ≈ $60k (5–6 Feb) and ≈ $57.7–58.5k (late Jun/early Jul) [V Aug/Sep memos]; ≈ $78k on 30 Oct [S]. The Aug memo self-grades this "Confirmed (crypto), mixed (equities)" because the S&P was +13.7% YTD [V] | Hit (crypto); Miss on the opportunity cost in equities |
| Feb memo (15 Feb; SPX 6,836, gold $5,042, BTC $69,799) | Dollar upside risk "similar to 2018"; energy/industrials favored; silver cooling; crypto "cyclical contraction"; international may outperform while the dollar is benign | DXY made higher lows from ≈ 96.5 (Feb) to ≈ 101.35 (30 Sep) [V Sep memo] and "toward 102" (1 Oct) [S]. XLE at new all-time highs mid-2026 [V Aug]; energy sector record on 23 Oct [S]. BTC lower to ≈ $58k [V]. Gold −21% to ≈ $3,970 (Jun) [V]. International vs US: unverified | Hit (dollar, energy, crypto); Unverified (international) |
| Mar memo (15 Mar; SPX 6,632, gold $5,018, BTC $71,214) | Cascade "between Stage 3 and Stage 4"; labor feedback not yet; no date | Stage 4 forces did arrive: oil spike, firm dollar, 10Y to ≈ 5.3% (24-year high, early Oct) [V/S]. But equities did *not* keep weakening vs gold: SPX/gold ≈ 1.32 → ≈ 1.9 by late Oct [I from S]. Labor: unemployment 4.1–4.3%, no nonlinear break; recession composite 0.024 (Aug) [V] | Partial (macro tightening right; equity-vs-gold leg reversed; stage 5 absent). The Aug memo marks it "Open" itself [V] |
| Q2 memo (15 Apr; BTC $74,822) | Incomplete reset; "further downside remains possible"; time-based capitulation; rallies tactical | Lower low ≈ $57.7–58.5k in late Jun/early Jul [V]. Then a rally to ≈ $83k (30 Sep) [V], ≈ $85–86k early Oct (inventory [S]), back to ≈ $78k (30 Oct) [S] | Hit on further downside; Partial on "rallies tactical" (the Sep rally beat the 50W) |
| May memo (18 May; SPX 7,378, gold $4,542, BTC $76,433) | Markets to price hikes, not cuts; "checkmate"; reassess fragility "later in Q3 or Q4"; cycle end 1–2 years away | Fed held 29 Jul (9–3, three hike dissents) [V Aug], hiked 25 bp on 16 Sep to 3.75–4.00% [V Sep], held 28 Oct at 3.75–4.00% (reported 10–2, two hike dissents) [S]. 10Y ≈ 5.36% intraday high around 7 Oct [S]. No recession signal. S&P record close 7,818.93 on 6 Oct [S] | Hit (hawkish path); Open (cycle-end timing) |
| Quantile paper (29 May) | Descriptive only ("not a forecast, a price floor"). Out-of-sample check-loss claims cover 2018–2026 | N/A. The Jul memo puts price on the 1% band (~$65.5k) in mid-July; price later rose above it [I] | No forecast |
| Jul memo (15 Jul; BTC $65,300) | (a) Q4 2026 primary bottom window; cycle-duration clock → October (≈ 15–23 Oct [I]) | No lower low through 30 Oct. BTC ≈ $81k on 23 Oct [S], ≈ $78k on 30 Oct [S], well above the ~$57.7–58.5k summer low | Open (Q4 runs to 31 Dec); October window Miss so far |
| | (b) August and September negative, as in all three prior midterms | Aug: ≈ $65.3k (15 Jul) → ≈ $63k (15 Aug) [V], roughly in line. Sep: ≈ $63k → ≈ $83k [V], strongly positive | Partial (Aug); Miss (Sep) |
| | (c) Illustrative year-end ROI ≈ 0.49 (≈ $43.8k) | ≈ $78k on 30 Oct [S] | Open (looks unlikely [I]) |
| | (d) Bear weakened only by two weekly closes above the 50W (≈ $86.5k) | The Sep memo says BTC "reclaimed its 50-week moving average" and calls it "a clear point for the bulls" [V]. Whether two consecutive weekly closes held above it was not verified | Partial (his own weakening condition was at least partly met) |
| | (e) MVRV Z to reset below zero before the low | No evidence it went below zero; price stayed above realized price (≈ $52–53k) | Open / Unverified |
| Aug memo (15 Aug; SPX 7,786, gold $4,370, BTC $63k, WTI $82, DXY 99.9) | (a) Base case 65%: equity correction beginning late Q3, bottoming Sep–Q4 | S&P ≈ 7,710 (30 Sep) [V]; record close 7,818.93 (6 Oct) [S]; ≈ 7,624 (23 Oct) [S]; ≈ 7,734 (29 Oct, possibly intraday) [S]. Max pullback ≈ 2–3% [I], not a correction so far | Open (Q4 not over); not happening so far |
| | (b) "Energy re-accelerates and the Fed hikes" = 20% policy-error state | Oil to ≈ $106 (Sep) [V], Brent ≈ $110–117 in Oct [S]; Fed hiked 16 Sep [V]. The trigger conditions of this state largely occurred, but no sharp equity drawdown followed | Partial (conditions met, outcome not) |
| | (c) Dollar firms (bullish lean) | 99.9 → 101.35 (30 Sep) [V] → "toward 102 … new 2026 highs" (1 Oct) [S] | Hit |
| | (d) Gold: near-term weakness, possible retest of the late-June low (≈ $3,970) | $4,370 → $4,210 (30 Sep) [V] → ≈ $3,990 intraday on 23 Oct, "below $4,000 for the first time since July" [S] → ≈ $4,054 on 28 Oct [S] | Hit (retest); whether it undercut $3,970 is unverified |
| | (e) Energy constructive, tops after the index | Energy sector record on 23 Oct [S] | Hit so far |
| | (f) BTC low forms *during* the equity correction (Q4); bottom-watch near $63k | BTC rallied to ≈ $83–86k without an equity correction, then fell to ≈ $78k [V/S] | Open; sequencing not yet confirmed |
| Sep memo (30 Sep; 10Y 5.29%, 30Y 5.64%, DXY 101.35, gold $4,210, BTC $83k, SPX 7,710, WTI $90) | (a) "The long end can still grind higher" | 10Y ≈ 5.31% close (5 Oct) and ≈ 5.36% intraday (7 Oct), highest since 2002; 30Y ≈ 5.73% [S]. Then −19 bp on 22 Oct, ≈ 5.0% on 23 Oct [S] | Hit; a possible yield top in early-to-mid Oct is unconfirmed |
| | (b) Gold "closer to a low than a high, even if it undercuts prior lows first" | Fell to ≈ $3,990 (23 Oct), ≈ $4,054 (28 Oct) [S] | Open; consistent so far |
| | (c) DXY above 101.8 would tighten further | DXY "toward 102 … new 2026 highs" on 1 Oct [S]; the late-Oct level was not verified | Partial / Unverified |
| | (d) Small caps: S&P following the S&P 600 lower would strengthen the 2018 analog; a small-cap recovery would defuse it | Russell 2000 −0.9% (week to 9 Oct), +2% (week to 23 Oct); S&P near records [S] | Leans "defused" [I]; Open |
| | (e) October FOMC: hike with hawkish guidance = 2018; hike with step-down = 2022 | Held 28 Oct at 3.75–4.00% (10–2, two hike dissents) [S]. Neither branch occurred | Not resolved |
| | (f) BTC: above ≈ $83k keeps the breakout; a weekly close below "would materially weaken" it | BTC ≈ $85–86k early Oct, then weekly closes below $83k; ≈ $81k (23 Oct), < $80k (26 Oct), ≈ $78k (30 Oct) (inventory [S]; [S] here) | Breakout weakened (the condition he named occurred) |
| | (g) Midterm-hike analog: flat about 7 weeks, break around day 50 (≈ 5 Nov [I]); 2022-type → ≈ $64k, 2018-type → ≈ $38k | Day 44 at 30 Oct; BTC ≈ $78k | Open (window not reached) |
| Ethereum / Bitcoin Letters (2020) | No forecasts visible (PDFs gated) | — | N/A |

**Summary [I]:**
- The 2026 memos were right on direction for crypto into mid-year, the hawkish Fed path, the dollar, energy leadership, the rising long end and gold's autumn weakness.
- They were wrong, or are still unconfirmed, on two things: equities transmitting stress (the equity-vs-gold leg reversed, and there was no Q4 correction by 30 Oct), and a BTC low in the October window.
- In September he publicly conceded that BTC had broken his August expectations. In July he admitted the series "has been better on direction than on level".
- Q4 is still open: equity correction, BTC lower low and gold low.

---

## Sources

**Primary (Cowen) [V]**
- Index: https://benjamincowen.com/reports ; sitemap: https://benjamincowen.com/sitemap.xml
- Report pages: the 11 URLs in §1.
- Publicly embedded PDFs (linked from each page's "Read the full report" viewer), all at the prefix https://jhdmn2wzmmz0dm21.public.blob.vercel-storage.com/reports/ :
  - `Crypto%20Macro%20Risk%20Memo%20Q1%202026-v2.pdf`
  - `Macro-Risk-Memo-Feb-2026.pdf`
  - `How-Risk-Cascades-Through-Markets-March-2026.pdf`
  - `Crypto-Risk-Memo-Q2-2026.pdf`
  - `Macro-Risk-Memo-May-2026.pdf`
  - `Assymetric-Tail-Curvature-in-Bitcoin-Price-Quantiles-4.pdf`
  - `Bitcoin-July-2026-Memo.pdf`
  - `The-Balance-of-Risks-August-2026.pdf`
  - `The-Triple-Squeeze-September-2026.pdf`
- Wayback CDX check: https://web.archive.org/cdx/search/cdx?url=benjamincowen.com/reports*

**Outcome checks [S]**
- Week of 5–9 Oct 2026 (S&P record 7,818.93 on 6 Oct; Russell): https://news.ifyouspent.com/en/news/week-in-markets-oct-5-2026 ; https://tapeboard.com/blog/weekly-recap-2026-10-09 ; https://www.kitco.com/news/off-the-wire/2026-10-07/sp-500-nasdaq-ease-record-highs-treasury-yields-climb ; https://investrade.com/?p=1610
- Week of 19–23 Oct 2026 (S&P 7,623.68; 10Y −19 bp on 22 Oct; gold < $4,000; BTC ≈ $81k; energy record): https://news.ifyouspent.com/en/news/week-in-markets-oct-19-2026
- 29 Oct 2026 snapshot (S&P ≈ 7,734): https://en.bloomingbit.io/feed/news/123140
- 10Y highest since 2002 (early Oct): https://www.chinapulse.com/data-news/2026/10/01/10-year-us-treasury-yield-hits-highest-level-since-2002/ ; https://news.ifyouspent.com/en/news/treasury-yields-above-5-percent-2026-explained ; https://political.org/2026/10/07/treasury-yields-climb-to-24-year-highs-as-markets-brace-for-39-billion-auction-and-fed-minutes/
- Dollar and gold, 1 Oct 2026: https://www.fxempire.com/forecasts/article/gold-forecast-the-usd-index-soars-to-new-2026-highs-1634558 ; gold Oct table: https://pricegold.net/2026/october/
- FOMC 28 Oct 2026 hold (10–2): https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates
- BTC ≈ $78k on 30 Oct and the 22–26 Oct moves: see the inventory's sources (Fortune 28–29 Oct; Coingabbar 30 Oct; BeInCrypto/Yahoo 26 Oct; Benzinga Oct 2026).
