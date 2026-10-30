# Cluster C — Growth & business cycle, liquidity & money, the dollar, equities & cross-asset, seasonality

Research file for the course "practical-macro-economy" (EN + PL). Data as of **30 Oct 2026**.
Claim tags: **[V]** verified from a primary/reputable source or computed by me from primary data (URL given), **[S]** secondary source or search snippet, **[I]** my own inference. Educational material, not financial advice.

**How the numbers were made.** Every FRED series named below was downloaded as CSV on 30 Oct 2026 from `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>` and processed with a small Python script (no smoothing unless stated). "Computed [V]" means the arithmetic is mine but the inputs are primary FRED data. BTC prices are the Coinbase daily series on FRED (`CBBTCUSD`, `CBETHUSD`). Third-party data (ISM, Conference Board, FactSet, DXY, gold) comes from the publisher or from press coverage, tagged as such.

---

## 0. Executive summary: ten findings an investor should leave with

1. **The 2026 setup is an oil-shock / late-cycle mix, not a textbook recession.** The US–Iran war began with US–Israeli strikes on 28 Feb 2026. Brent went from about $72 to about $119 in April and to about $127 (spot) in September–October. FRED Brent was $123.10 on 27 Oct 2026 [V/S]. The Fed **hiked** to 3.75–4.00% on 16 Sep 2026 (its first hike since 2023) and held on 28 Oct with two dissents in favour of another hike [S]. At the same time, real GDP grew **3.4% annualised in Q3 2026** [V BEA/FRED], ISM Manufacturing has been above 50 for nine months (54.5 in September) [V ISM], and the S&P 500 set a record at 7,818.93 on 6 Oct 2026 [V FRED]. Crypto is in a bear market: BTC fell from a close of $124.7k on 5 Oct 2025 to $58.6k on 30 Jun 2026 and was about $78k on 29 Oct 2026 [V FRED].
2. **The "ISM above 50 → alt season" thesis (Raoul Pal) failed its 2026 test.** ISM moved back above 50 in Jan 2026 (52.6, ending 26 months of contraction) and climbed to 54–55. ETH still fell 24% YTD, BTC dominance is about 60%, and the Altcoin Season Index is neutral [V/S]. Cowen never bought the thesis. His line was "Bitcoin is not the economy" [S], and he argues this is a *late*-cycle environment in which capital consolidates into BTC [S].
3. **Net liquidity (WALCL − TGA − RRP) explains BTC well in some regimes and not at all in others.** From 2019 to 2022 the correlation of log levels was **0.81** for BTC and **0.78** for the S&P. From 2023 to Oct 2026 it was **−0.26** for BTC and **−0.54** for the S&P, because both rallied while net liquidity went sideways or down [V computed]. A "10–12 week lead" exists only in short windows. In 2025–26 the best fit was a 12–16 week lag (r ≈ 0.66–0.74 in levels), while over 2016–2026 the lag profile is flat. That flatness is what you expect when two trending series share a trend, not when one predicts the other [V computed / I].
4. **Cowen's own position on global M2 has changed over time.** In 2025 he argued that BTC *leads* global M2 by 18–30 weeks at tops, so offset charts mislead [S, his X post]. In 2026 he said BTC tracks "global net liquidity" (central-bank balance sheets minus TGA/RRP-type drains), not M2. He put that measure at about $25T versus a $30T peak in 2021–22 [S].
5. **M2 matters as a regime variable, not as a timing tool.** US M2 fell **4.86% peak-to-trough** (Mar 2022 → Oct 2023). Its YoY bottomed at **−4.66% (Apr 2023)**, the first sustained YoY contraction in the post-1959 FRED record and the largest since the 1930s [V FRED / S]. M2 regained its old peak in May 2025 and was growing **+5.7% YoY** in Sep 2026, yet BTC is in a bear market [V].
6. **DXY peaks and BTC bottoms line up loosely, not tightly.** The cleanest case is 2022: the DXY peaked on 28 Sep at 114.78 [S] and the broad dollar on 26 Sep [V]. The S&P bottomed about two weeks later, and BTC bottomed about eight weeks later on 21 Nov, after FTX. In 2015 and 2018 BTC bottomed *before* or *independently of* the dollar's peak. In 2025 the dollar had its worst first half since 1973 (−10.8%) [S], yet BTC topped in Oct 2025 and halved [V].
7. **The BTC–equity correlation is regime-dependent and asymmetric.** Daily BTC–SPX correlation was about 0 before 2020, **0.56 in 2022**, **−0.02 in 2025** and **0.44 in 2026** [V computed]. In 2022 and 2026 BTC's beta to S&P *down* days (1.9 and 1.7) was well above its beta to *up* days (1.1 and 1.2). In plain terms, BTC took the downside of equities without the upside [V computed].
8. **Oil spikes have come before most US recessions, but 2026 is a live counter-example so far.** Five of the last eight recession starts (1973, 1980, 1990, 2001, 2008) followed or coincided with oil roughly doubling within two years [V computed from FRED `WTISPLC`]. Big spikes in 2021–22 (+113% YoY) and in 2026 (+58% YoY in April) have not yet produced an NBER recession. The US is now a net petroleum exporter, which changes the transmission [I].
9. **Midterm-year seasonality held for BTC in 2014, 2018 and 2022, but the sample is three cycles and the effect is entangled with the halving cycle.** BTC fell 58%, 73% and 64% in those years [V/S]. Every BTC cycle peak (Dec 2013, Dec 2017, Nov 2021, Oct 2025) landed in the year *before* a midterm, so the midterm effect and the halving cycle cannot be told apart [I]. In 2026 the S&P drew down only about 9% (average midterm drawdown ≈ 17–19%) [S/V]. Cowen's base case is a BTC cycle low in Q4 2026 [S].
10. **Equities usually peak before recessions and bottom before they end.** Across the eight recessions from 1969 to 2020, the S&P peak came on average about 5 months before the NBER start (median 5, range −1 to +12 months). The average peak-to-trough fall was about 36% (17% in 1980 to 57% in 2007–09) [S/I table in §4.9]. Other studies covering longer histories put the averages at about 7 months and 26–32% [S]. The market low came 1–6 months *before* the NBER trough in seven of eight cases. 2001–02 is the exception, with the low 11 months *after* the trough [S/I].

---

## 1. Growth and the business cycle

### 1.1 Real GDP, the "two negative quarters" myth, and NBER dating

**Definition and data.** Real GDP is the inflation-adjusted value of final goods and services produced in the US. The Bureau of Economic Analysis (BEA) publishes it quarterly as a seasonally adjusted annualised rate (SAAR). Each quarter gets three estimates: advance (about 4 weeks after quarter-end), second and third. Annual and comprehensive revisions follow. FRED IDs: `GDPC1` (level, chained 2017 $) and `A191RL1Q225SBEA` (% change, SAAR). Related series: real final sales to private domestic purchasers, which strips out inventories, government and trade and is the "core GDP" many economists prefer. GDI is the income-side twin (`A261RX1Q020SBEA`).

**Latest.** Q3 2026 advance estimate, released 29 Oct 2026: **+3.4% SAAR**, up from 2.2% in Q2. Real final sales to private domestic purchasers rose about 4.9% [V BEA release https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026; S IndexBox]. Quarterly path from FRED: 2025 Q1 +0.1, Q2 +4.0, Q3 +3.9, Q4 +0.2 (the government-shutdown quarter), 2026 Q1 +2.5, Q2 +2.2, Q3 +3.4 [V FRED].

**Revisions matter.** BEA reports that the mean absolute revision from the advance to the second estimate was about 0.5 pp over 1996–2024 [S BEA]. Q1 2025 is a good illustration. It was first reported as a contraction, driven by a tariff-front-running import surge, and after revisions FRED now shows +0.1% [V FRED, I note the sign flip]. Never anchor on one advance print.

**The "two negative quarters" myth.** In the US a recession is **not** defined as two consecutive quarters of negative GDP. The NBER Business Cycle Dating Committee dates peaks and troughs from a broad set of monthly indicators: real personal income less transfers, nonfarm payrolls, household employment, real consumer spending, real manufacturing-and-trade sales and industrial production. It judges *depth, diffusion and duration*. The committee announces months or even a year after the fact. The Dec 2007 peak was announced in Dec 2008, and the Feb 2020 peak was announced in June 2020 [S NBER]. Key episode: in H1 2022 the initial GDP prints were negative for two quarters running (Q1 and Q2 2022), yet payrolls grew by more than 400k a month. NBER declared no recession, and later revisions softened the GDP declines [S]. The reverse also happens. The 2001 recession never had two consecutive negative quarters in the then-current data [S]. FRED's `USREC` is the NBER monthly recession indicator; Sep 2026 = 0 [V].

**How to read it.** Use rates of change: the 2-quarter and 4-quarter annualised pace. Look at private final demand, not headline GDP, because inventories and net exports swing it. In 2025–26, tariff and SPR-release effects distorted trade, consumption and inventories [S IndexBox mentions an SPR effect on Q3 consumption]. GDP is a *lagging/coincident* indicator. Markets have usually moved before it prints.

**How Cowen uses it [S/I].** Cowen rarely trades off GDP prints. He uses NBER recession shading on long charts (S&P, unemployment, yields, BTC) to argue about sequences, for example "the Fed usually cuts into rising unemployment and the recession is dated after the fact." His recurring point is that recessions are recognised late, so by the time GDP confirms, risk assets have already moved [I, consistent with his standard macro framing; no single dated quote found].

**Relationships and asset effects.** GDP lags PMIs/LEI by 1–2 quarters and is coincident with payroll trends. Equities lead GDP: S&P peaks have come 0–13 months before recession starts (§4.9). Bonds rally when growth expectations fall. Crypto has no stable link to quarterly GDP [I].

**Takeaway.** Treat GDP as confirmation, not a signal. A strong 3.4% Q3 2026 print says the economy was not in recession over the summer. It says little about Q4–Q1 when an oil shock and tightening policy are working through.

### 1.2 Atlanta Fed GDPNow

**Definition.** GDPNow is a model-based "nowcast" of current-quarter real GDP growth (SAAR) from the Federal Reserve Bank of Atlanta. It updates after major data releases (ISM, retail sales, trade, housing, etc.), about 6–7 times a month, until the BEA advance estimate. It is not an official forecast and has no judgemental adjustment. Source: atlantafed.org/cqer/research/gdpnow. FRED: `GDPNOW`.

**How to read it.** Early-quarter readings are noisy, with errors of several pp, and they converge as data arrives. The final GDPNow before the advance release has historically had a root-mean-squared error of about 1.2 pp [S Atlanta Fed documentation]. The trend across updates matters more than any single number. In 2025 the "gold import" distortion produced a very negative Q1 nowcast. The Atlanta Fed later published a gold-adjusted version, which shows how one-off trade quirks can mislead [S].

**Latest.** For Q3 2026 the nowcast ran around 4–6% in Aug–early Oct (≈4.0% on 18 Aug, ≈3.7% on 6 Oct) before the 3.4% advance print [S investinglive/cryptobriefing]. I could not find a Q4 2026 nowcast on the web as of 30 Oct; it starts after the advance release [S].

**Cowen use.** I found no verified video centred on GDPNow [unverified].

**Takeaway.** GDPNow is the best free real-time estimate of the *current* quarter. It does not forecast recession turns, and like everything else it was high right up to the onset of past downturns [I].

### 1.3 ISM Manufacturing PMI (the 50 line, new orders)

**Definition.** The Institute for Supply Management's monthly survey of purchasing managers at more than 300 US manufacturers. It is released on the first business day of the month at 10:00 ET for the previous month. The headline PMI is a diffusion index: an equal-weighted composite of New Orders, Production, Employment, Supplier Deliveries (inverted logic: slower = higher) and Inventories. **50 separates expansion from contraction** in manufacturing. ISM states that a PMI above **47.5** over time is consistent with expansion of the *overall* economy. ISM updated that threshold from the older 42.x figures [V ISM Sept 2026 report]. Seasonal factors are revised every January, which can rewrite history (§1.12). Not on FRED, because ISM withdrew it. Free sources: ismworld.org monthly reports, TradingView `ISM:MAN_PMI` (some data vendors), tradingeconomics.

**How to read it.**
- The level relative to 50 gives the direction of manufacturing.
- The **New Orders − Inventories** spread leads the headline by about 3–6 months [S common practitioner rule].
- **Prices Paid** is an inflation pipeline gauge.
- Customers' Inventories "too low" (below 50) is bullish for future orders.
- Common misreading: manufacturing is only about 10% of US GDP, so a sub-50 ISM is not the same as a recession. Over Nov 2022–Dec 2024 the ISM printed below 50 for 26 straight months with no recession [V ISM/S].

**History (key values).** Dec 2015 trough about 48 (manufacturing recession tied to the oil and capex bust). Aug 2018 peak 61.3. Apr 2020 trough 41.5. **Mar 2021 peak 64.7, the highest since Dec 1983** [V FT Portfolios https://ftportfolios.com/Commentary/EconomicResearch/2021/4/1/the-ism-manufacturing-index-rose-to-64.7-in-march]. Then followed 26 months of contraction (Nov 2022–Dec 2024), a brief rise above 50 in Jan 2025, and contraction through Dec 2025 [S]. **Jan 2026: 52.6**, the first expansion in 12 months and the highest since Aug 2022. New Orders were 57.1 [V/S FT Portfolios https://www.ftportfolios.com/Commentary/EconomicResearch/2026/2/2/the-ism-manufacturing-index-rose-to-52.6-in-january].

**Latest (Sept 2026, released 1 Oct)** [V PR Newswire/ISM https://www.prnewswire.com/news-releases/manufacturing-pmi-at-54-5-september-2026-ism-manufacturing-pmi-report-302894520.html]:

| Component | Value |
|---|---|
| PMI | **54.5** (Aug 54.6), 9th consecutive month of expansion |
| New Orders | 55.3 (+1.6) |
| Production | 56.7 |
| Employment | 52.7 |
| **Prices** | **77.9** (+6.8; Mar 2026 = 78.3 when the Iran war began) |
| Inventories | 48.6 |
| Customers' inventories | 41.6 ("too low", bullish for orders) |

ISM's own read: the overall economy has expanded for 23 consecutive months. The October ISM is due 2 Nov 2026.

**How Cowen uses it.** When ISM went back above 50 in Feb 2026 and crypto commentators (Strive's Joe Burnett, Plan C) argued this was the "risk-on" turn, Cowen's quoted reply was **"Bitcoin is not the economy"** [S Cointelegraph via TradingView https://www.tradingview.com/news/cointelegraph:a453199ce094b:0-ism-manufacturing-pmi-at-highest-since-2022-as-analysts-debate-bitcoin-impact/]. In Mar 2026 he posted that "Liquidity conditions also reflect a late business cycle environment" [S X post 2036990935075016905]. His business-cycle chart is a normalised composite of S&P 500 performance, unemployment, interest rates, inflation and M2, not the ISM alone [S CryptoAdventure 18 Apr 2026].

**Relationships.**
- ISM leads S&P 500 EPS growth by about 3–6 months. YoY S&P returns correlate with the ISM level (r ≈ 0.5–0.6 historically) [S practitioner studies; I].
- ISM tends to move with the 10Y yield and with the copper/gold ratio (§4.8).
- ISM troughs often come 3–9 months after Fed easing begins and after the dollar peaks [I/S].
- Mechanism: new orders reflect inventory cycles and financing conditions (rates, the dollar, credit spreads).

**Effect on assets.** Rising ISM → cyclical equities, small caps, commodities and higher yields; historically also "risk-on" crypto (2016–17, 2020–21). Falling ISM → bonds rally, defensives outperform. Reliability for crypto: weak to moderate (see the test in §1.13).

**Takeaway.** The ISM is the best single monthly *cycle* gauge for manufacturing. Watch New Orders and Prices, not just the headline. In 2026 a rising ISM has come with *inflationary* pressure (Prices ≈ 78), which turns a cyclical upturn into a reason for the Fed to tighten rather than a pure risk-on signal [I].

### 1.4 ISM Services PMI

**Definition.** The ISM survey of non-manufacturing firms, about 75–90% of GDP. It is released on the third business day of the month. The headline Services PMI is a composite of Business Activity, New Orders, Employment and Supplier Deliveries. **50 = expansion.**

**Latest (Sep 2026, released 5 Oct).** **54.9** (Aug 55.4), the 27th straight month of expansion. **Prices 74.0, the highest since July 2022 and the sixth reading above 70 this year.** Fuel costs were cited twice as often as any other issue [V ISM/S https://www.ftportfolios.com/Commentary/EconomicResearch/2026/10/5/the-ism-non-manufacturing-index-declined-to-54.9-in-september].

**How to read it.** Services move with employment and consumption. Services prices track services CPI/PCE with about a 3–6 month lead [S]. A sub-50 services print is a stronger recession warning than a sub-50 manufacturing print because services dominate output [I]. In Apr–May 2025 services briefly dipped below 50 during the tariff shock [S].

**Takeaway.** Services strength plus 74 prices is a *stagflation-lite* signature: growth fine, inflation pressure rising. That is the mix that led the Fed to hike in Sep 2026 [I].

### 1.5 S&P Global (formerly IHS Markit) PMIs

**Definition.** Flash US Manufacturing, Services and Composite PMIs from S&P Global. Flash readings come out about 10 days before month-end and finals about 1–3 business days into the next month. Same 50 threshold. The S&P Global PMIs have a broader panel and different weights than ISM and are often smoother. Global and eurozone/China (Caixin/RatingDog) versions are used to read the *global* cycle.

**Latest flash (Oct 2026, 23 Oct).** Composite **57.6** (Sep 58.4), the second-sharpest expansion since Mar 2022. Services 57.9, Manufacturing **56.0** (a 53-month high). Chief economist Chris Williamson: the economy "continues to boom at the start of the fourth quarter." Output prices are rising the most since 2022 [S investinglive/newsquawk/thestreet].

**Takeaway.** Two independent survey families (ISM, S&P Global) agree that US activity was *accelerating* in Q3–Q4 2026, despite the oil shock. That weakens "imminent recession" narratives for the next 1–2 quarters [I].

### 1.6 Conference Board Leading Economic Index (LEI)

**Definition.** A composite of 10 leading indicators published monthly by the Conference Board, usually in the third week, for the prior month (2016 = 100):
- average weekly manufacturing hours
- initial jobless claims
- manufacturers' new orders for consumer goods
- ISM new orders
- manufacturers' new orders for nondefense capital goods ex-aircraft
- building permits
- S&P 500
- Leading Credit Index
- 10Y–fed funds spread
- consumer expectations

The Conference Board's recession rule is the "3Ds": a six-month annualised decline of about −4.1% (depth) together with a diffusion index below 50. FRED's `USSLIND` is a different (Philadelphia Fed) series and was discontinued in 2020 [V FRED], so it is not a substitute.

**Latest.** The Sep 2026 LEI (released 22 Oct, delayed) was **unchanged at 99.6** after −0.1% in August. The six-month growth rate improved, diffusion was slightly above 50, and the Conference Board said there was **no recession signal**. The Coincident Index was +0.3% to 115.3 and the Lagging Index +0.5% to 121.1 [S Conference Board technical notes/press via search].

**Famous failure.** The LEI fell continuously from early 2022 to early 2024, about 24 months, and triggered the 3Ds recession signal throughout 2022–23. No recession followed. The Conference Board dropped its recession call in 2024 [S]. Likely reasons:
- The index is overweighted to manufacturing and goods while the economy was services-led.
- The yield-curve component was distorted by post-COVID policy.
- Fiscal deficits of about 6% of GDP supported demand [I].

**Cowen use.** Not a core Cowen chart. He emphasises unemployment, the yield curve and the Fed instead [I; unverified].

**Takeaway.** The LEI is useful for direction but has given long false alarms. Treat a falling LEI as "rising risk", not a dated forecast.

### 1.7 Consumer confidence and Michigan sentiment

**Definitions.**
- *University of Michigan Consumer Sentiment* (FRED `UMCSENT`, 1966Q1 = 100). Preliminary mid-month, final at month-end. Includes 1-year and 5–10-year inflation expectations.
- *Conference Board Consumer Confidence* (1985 = 100). Last Tuesday of the month. More weighted to labour-market perceptions; the "jobs plentiful minus jobs hard to get" labour differential is a useful unemployment proxy.

**How to read them.** Sentiment is highly sensitive to *gasoline prices and inflation* and, since 2020, to partisan identity, so levels are poorly correlated with actual spending [S/I]. Extreme lows are historically *contrarian* bullish for equities. The June 2022 Michigan low of 50.0 came within days of the S&P's June 2022 interim low and four months before the Oct 2022 final low [S/I]. Inflation expectations from Michigan matter to the Fed.

**Latest.** Michigan **final Oct 2026 = 48.0** (preliminary 46.3; Sep 48.1). The lowest reading in the FRED history is **44.8 in May 2026** [V FRED]. Year-ahead inflation expectations were 4.6% in Sep, with 5-year at 3.4% [S]. Conference Board confidence in Oct 2026 was reported at 91.7, up from 84.2 [S, single secondary source; not verified against the release].

**Takeaway.** Record-low sentiment alongside 3.4% GDP growth shows sentiment measuring *inflation pain*, not output. Contrarian equity value has historically been real but unreliable for timing [I].

### 1.8 Retail sales and industrial production

**Retail sales.** Census Bureau Advance Monthly Retail Trade Report, mid-month, nominal $ (FRED `RSAFS`; real version `RRSFS`). The **control group** excludes autos, gasoline, building materials and food services and feeds GDP consumption. Sep 2026: headline **+0.8% m/m**, but more than 70% of the beat came from gasoline stations. The control group was +0.1% m/m (est. 0.3%) [S thestreet/advisorperspectives]. YoY nominal +6.3% [V FRED computed] against CPI +3.7% YoY [V FRED] means real growth of about 2.5% [I]. Lesson: in an oil shock, headline retail sales overstate real demand.

**Industrial production.** Federal Reserve G.17, mid-month (FRED `INDPRO`, 2017 = 100). Sep 2026: 103.95, **+2.2% YoY** [V FRED]. IP is one of the NBER's six core indicators. IP YoY turning negative has accompanied every post-war recession but also several non-recessions (1985–86, 1998, 2015–16, 2019, 2023) [I/S].

### 1.9 Housing: starts, permits, existing home sales, mortgage rates, Case-Shiller

**Data.** Housing starts `HOUST` and permits `PERMIT` (Census, about the 12th business day; SAAR thousands). Existing home sales (NAR, about the 20th; `EXHOSLUSM495S` on FRED is a short window). 30-year mortgage rate (Freddie Mac PMMS, weekly Thursday; `MORTGAGE30US`). S&P CoreLogic Case-Shiller national index (`CSUSHPINSA`, 2-month lag).

**Why it matters.** Edward Leamer's 2007 Jackson Hole paper, "Housing IS the Business Cycle", found that residential investment was the leading contributor to weakness before most post-war recessions [S]. Permits lead starts, starts lead residential investment, and residential investment leads the cycle by about 4–6 quarters. Mortgage rates transmit long-end yields into the real economy.

**Latest** [V FRED unless noted]:
- Starts **1,221k** SAAR in Sep 2026 (**−7.4% YoY**). The 2026 range is 1,182k (May) to 1,522k (Mar).
- Permits **1,398k** (−3.2% YoY).
- 30Y mortgage **7.24%** (29 Oct 2026), up from 6.26% in Nov 2025, because the 10Y went from about 4.1% to 5.05–5.31%.
- Case-Shiller national NSA **+2.1% YoY** (Aug 2026), with a slight m/m dip.
- Existing home sales **3.99M** SAAR in Sep 2026 (−2.2% YoY). Median price $417,500 (+1.3% YoY). Inventory about 1.6M, the highest since Nov 2019 [S NAR https://www.nar.realtor/newsroom/existing-home-sales-increased-1-5-in-september-according-to-nar-report].

**Reading.** Activity is depressed and prices are flat-to-slightly up. Owners locked into low mortgage rates create a supply freeze, so prices do not fall the way they did in 2007–09. Weak housing *volumes* with *no forced selling* is a 2023–26 pattern [I].

**Asset link.** Housing weakness feeds through to lower yields over 6–12 months and has historically preceded Fed easing. A re-spike in mortgage rates above 7% is a growth headwind and, if prolonged, raises recession odds into 2027 [I].

### 1.10 Corporate earnings

**Data.** FactSet "Earnings Insight" (weekly, free PDF), S&P Dow Jones Indices, LSEG I/B/E/S.

**Latest (FactSet, 23 Oct 2026; 24% reported).** Q3 2026 blended EPS growth **+29.5% YoY**, revenue **+12.7%**, net margin 14.9% (would be the second-highest since 2009), CY2026 EPS growth estimate **+33.1%**. **Forward 12-month P/E 18.7** versus a 5-year average of 19.8 and a 10-year average of 19.1. Energy upgrades from the oil shock contributed. Micron and NVIDIA were the top contributors to growth; the 493 non-Mag-7 grew 27.7% (16 Oct) [V FactSet https://insight.factset.com/sp-500-earnings-season-update-october-23-2026].

**Reading.** Earnings are *pro-cyclical and lagging*. EPS falls about 15–30% in recessions (2001 ≈ −30% operating, 2008–09 ≈ −50% GAAP) [S]. Strong earnings make a forward P/E of 18.7 look reasonable even with Shiller CAPE about 41. These two valuation lenses now disagree sharply (§4.7) [I].

### 1.11 Consumer credit, delinquencies, bankruptcies

**Data.**
- Fed G.19 consumer credit (`TOTALSL`, monthly, about 5-week lag): Aug 2026 $5.20T, +2.7% YoY [V FRED].
- NY Fed Household Debt and Credit Report (quarterly). Q2 2026: total household debt **$18.77T** (−$13B q/q, the first decline since 2020). 4.73% of debt is in some stage of delinquency. Flow into serious delinquency: credit cards 6.97%, auto 3.00%, mortgages 1.52% (rising from 1.29% a year earlier), student loans 7.83% (distorted by re-reporting) [V/S NY Fed https://www.newyorkfed.org/newsevents/news/research/2026/20260811].
- Fed charge-off and delinquency rates (`DRCCLACBS`, credit-card delinquency at commercial banks, 2.85% Q1 2026) [V FRED].
- S&P Global Market Intelligence corporate bankruptcies: 2025 full year **785**, the highest since 2010's 828. **H1 2026 = 372**, the most for a first half since 2010 [S].

**Reading.** Delinquencies and bankruptcies are *lagging* indicators. They rise into and through recessions and peak after them. Elevated bankruptcies with tight credit spreads describe 2025–26: high-yield OAS was 3.14% on 28 Oct 2026 [V FRED `BAMLH0A0HYM2`]. Distress is concentrated in small, floating-rate borrowers, not spreading system-wide [I]. Credit spreads widening above about 5–6% have historically accompanied recessions; they are about 3% now [V/I].

### 1.12 A note on data reliability in 2025–26

The Oct–Nov 2025 federal government shutdown left gaps: no Oct 2025 CPI on FRED (blank) [V FRED]. Several releases were delayed, the LEI in Oct 2026 among them. ISM's January seasonal revisions changed the count of contraction months. Teach students to check vintage (ALFRED) and to expect revisions.

### 1.13 The "ISM business cycle ↔ altcoin season" thesis: tested

**The thesis (Raoul Pal / Global Macro Investor / Real Vision).**
- The ISM is "our preferred barometer for the business cycle".
- Bitcoin and especially altcoins are high-beta expressions of the cycle: "Bitcoin goes up as the ISM goes up... If the ISM gets up to its normal cycle peak of somewhere between 56 and 65, that will give us the magnitude of the rise."
- Altcoins outperform late in the ISM upswing.
- In 2024–25 Pal argued that debt-maturity extension had stretched the cycle to about 5 years, putting the ISM and crypto peak in **Q2 2026** [S Benzinga/NewsBTC summaries].

**Historical fit (the case for):**

| Episode | ISM trough → peak | Alt season / BTC.D low | Fit |
|---|---|---|---|
| 2016–18 | ~48 (Dec 2015) → 60.8 (Sep 2017) / 61.3 (Aug 2018) | Alt season Q2 2017 and Dec 2017–Jan 2018. BTC dominance fell to about 33–35% (Jan 2018) [S] | Good: alts peaked as ISM approached about 60 |
| 2020–21 | 41.5 (Apr 2020) → 64.7 (Mar 2021) | Alt season Apr–May 2021. BTC.D about 40% (May 2021) [S]. ETH peak Nov 2021 | Good: ISM peak Mar 2021 ≈ start of the alt blow-off |
| 2022–24 | > 50 → < 50 for 26 months (Nov 2022–Dec 2024) | No alt season; BTC.D rose from about 40% to about 60%+ | Consistent: no ISM upswing, no alt season |

**Out-of-sample test (the case against), 2026.** ISM went above 50 in Jan 2026 (52.6) and rose to 54.5–54.6 by Aug–Sep, its highest since 2022, with New Orders at 55–57 [V ISM]. Over the same period:
- ETH fell from $2,950 (Jan) to $2,250 (29 Oct), about **−24% YTD** [V FRED computed].
- BTC fell from $87.6k to $78k (−11% YTD), after a June low of $58.6k [V].
- BTC dominance dipped to about 57.3% in June and is back at about 60%. The Altcoin Season Index is about 53, neutral; 75 or more is "alt season" [S coinstats/blockchainreporter].

So the ISM upswing happened and the alt season did not.

**Why it failed (competing explanations).**
1. *Composition.* The 2026 ISM upswing is partly a supply-shock and price effect: Prices 78, plus restocking ahead of tariffs and war disruptions. It is inflationary, so it brought rate hikes and a 10Y at 5%, not the falling-rate, rising-liquidity mix of 2016–17 and 2020–21 [I].
2. *Liquidity, not activity, drives crypto beta.* In 2016–17 and 2020–21 ISM upswings coincided with expanding global liquidity: the PBOC/ECB/BOJ in 2016–17, and Fed QE plus fiscal transfers in 2020–21. In 2026 the Fed hiked and central-bank balance sheets are roughly flat (§2) [I]. Cowen's 2026 framing fits this: BTC tracks global net liquidity, not M2 or activity [S].
3. *Cowen's late-cycle / apathy argument.* Alt seasons came out of euphoric tops (2017, 2021). Apathetic tops (2019, 2025) did not rotate. "There's just no one left to sell the altcoins to." He also noted that BTC topped about 2 months before QT ended in both 2019 and 2025 [S CryptoAdventure 18 Apr 2026 https://cryptoadventure.com/benjamin-cowen-reveals-why-the-altcoin-season-never-came/].
4. *Supply.* Token dilution: tens of millions of tokens and continuous unlocks mean "altcoins" no longer share one beta [I].
5. *Sample size.* The thesis rests on two episodes. Two observations cannot separate "ISM causes alt seasons" from "both respond to a third factor" (global easing, the post-halving cycle) [I].

**Verdict [I].** The ISM ↔ alt-season link is at best a *coincident* description of 2017 and 2021, when ISM, liquidity, the dollar and the halving cycle all lined up. It is not a standalone leading signal. Cowen's skepticism held up in 2026, though his alternative (the late-cycle / apathy-top story) is also built on a small sample (2019, 2025).

**Practical takeaway.** If you watch the ISM for crypto, condition on *why* it is rising. A disinflationary, easing-driven ISM upswing has historically helped risk and alts. An inflationary, tightening-accompanied one so far has not.

---

## 2. Liquidity and money

### 2.1 M2 money supply (US)

**Definition.** M2 = currency + checkable/demand deposits + savings deposits (including MMDAs) + small time deposits (< $100k) + retail money-market fund balances. Published by the Fed's H.6 release monthly (4th Tuesday, about a 4-week lag). Units: $ billions, seasonally adjusted. FRED `M2SL` (monthly SA). Weekly data was discontinued in 2021. Since May 2020, savings deposits are included in M1 (a definitional break in M1, not M2).

**How to read it.** Use **YoY growth**, not level, because the level almost always rises. Nominal M2 growth roughly equals real GDP growth plus inflation plus the change in velocity. Very high M2 growth (2020–21: +26.8% YoY peak in Feb 2021 [V FRED]) has historically preceded inflation by about 12–18 months (the 2021–22 inflation) [S/I]. M2 contraction signals tight money. Velocity is unstable, so the M2–inflation link is loose over short horizons.

**The 2022–23 contraction.**
- M2 peaked at **$21.77T (Mar 2022)** and troughed at **$20.71T (Oct 2023)**: **−4.86%** [V FRED computed].
- YoY growth turned negative in **Dec 2022** and stayed negative through **Feb 2024**, with a low of **−4.66% in Apr 2023** [V FRED computed].
- This is the first YoY contraction in the 1959+ FRED record and the largest since the early-1930s Great Depression, when the money stock fell almost 30% [S Motley Fool https://www.fool.com/investing/2024/02/25/us-money-supply-is-shrinking-the-most-since-the-gr].
- The popular phrase "first contraction since the 1930s" is roughly right in spirit. Pre-1959 data comes from Friedman–Schwartz and is not identical in definition [I].
- **What followed:** no recession. The S&P rose 24% in 2023 and BTC rose 156% [V FRED computed]. This is an important counter-example to "M2 down = crash".

**Recovery.** M2 regained its old peak in **May 2025** ($21.81T). By **Sep 2026 it was $23.41T, +5.7% YoY** [V FRED].

**How Cowen uses it.** Cowen argues that BTC does *not* reliably rise with M2. M2 hit new highs in 2014, 2018 and 2022, yet BTC fell sharply in each of those years. He prefers global net liquidity [S Yahoo/Benzinga Sept 2026 https://finance.yahoo.com/markets/crypto/articles/remember-bitcoin-supposed-rise-money-170010779.html]. Fact check [I/V]: M2 *levels* were at highs in 2014 and 2018. In 2022 M2 peaked in March and then fell, so "M2 hit record highs in 2022" is only true for Q1 2022. The broader point stands: M2 level is not a timing tool.

**Asset effects.** M2 growth is a slow *regime* variable. Above-trend growth (>7–8%) is historically associated with rising asset prices and later inflation. Contraction tightens conditions but, as 2023 showed, can coexist with rallies when the starting stock of excess savings is large [I].

**Takeaway.** Look at M2 YoY, not the level, and treat it as background. It cannot time BTC tops or bottoms.

### 2.2 Global M2 and the "BTC follows global M2 with ~10–12 week lag" narrative

**Definition.** There is no official "global M2". Practitioners (TradingView scripts, Lyn Alden, Raoul Pal, Joe Consorti, CoinGlass, BGeometrics) sum M2 or broad money for the US, euro area, China, Japan, UK and sometimes 10–20 more economies, converted to USD at spot FX. Because of the FX conversion, **a weaker dollar mechanically raises "global M2"**, so global M2 in USD is partly an inverted DXY [I]. FRED's international M2 series (e.g. `MYAGM2CNM189N`) are stale; the IMF IFS-based series end in 2017–2019 [V FRED]. Free proxies: TradingView `ECONOMICS:CNM2`, `ECONOMICS:EUM2`, `ECONOMICS:JPM2`, `ECONOMICS:USM2`, with FX tickers to convert.

**The narrative.** Overlay BTC on global M2 shifted forward by about 10–12 weeks (some use 70 or 90 days). Since about 2023 the curves "match", so global M2 leads BTC.

**Latest.** Global M2 (US + EA + China + Japan) is reported at a record of about **$103–104T in Aug 2026** (+8% YoY in USD, about +4.5% at constant FX) [S cryptorank/pluang, secondary]. BTC is about 35–40% below its Oct 2025 peak. The overlay has visibly failed in 2025–26 [S/V].

**Cowen's position (it has changed).**
- **May 2025:** "What if #Bitcoin leads liquidity, rather than lags it? A lot of people show this chart, where they offset global M2 by 3-4 months and show BTC following it. The problem is that in 2021, this offset shows M2 going up for 6 months after BTC topped." He reported that in the last three cycles BTC topped **18–30 weeks before** global M2 topped [S X post https://x.com/benjamincowen/status/1920560445712159145; tradersunion summary].
- **Sep 2026:** BTC tracks *global net liquidity* (major central-bank balance sheets minus drains like TGA/RRP), which he put at about **$25T versus about $30T at the 2021–22 peak**. He said this explains why BTC lagged stocks. His closest analogue is 2019 (M2 up, stocks at highs, BTC down) [S Yahoo/Benzinga].

**My test (US net liquidity as a proxy, because I lack a clean global series).** Weekly data, log levels and 13-week log changes, correlation of BTC(t) with net liquidity(t − lag) [V computed from FRED `WALCL`, `WTREGEN`, `RRPONTSYD`, `CBBTCUSD`]:

| Window | Measure | lag 0 | 4 w | 8 w | 10 w | 12 w | 16 w | 20 w |
|---|---|---|---|---|---|---|---|---|
| 2016–Oct 2026 | levels | 0.78 | 0.78 | 0.78 | 0.77 | 0.77 | 0.77 | 0.76 |
| 2016–Oct 2026 | 13-w changes | 0.15 | 0.17 | 0.17 | 0.17 | 0.16 | 0.11 | 0.07 |
| 2020–2022 | levels | 0.80 | 0.81 | 0.80 | 0.79 | 0.78 | 0.77 | 0.77 |
| 2020–2022 | 13-w changes | 0.24 | **0.26** | 0.24 | 0.22 | 0.18 | 0.11 | 0.10 |
| 2023–Oct 2026 | levels | **−0.26** | −0.18 | −0.13 | −0.09 | −0.06 | 0.01 | −0.01 |
| 2023–Oct 2026 | 13-w changes | 0.18 | 0.20 | 0.29 | **0.30** | 0.29 | 0.24 | 0.07 |
| 2025–Oct 2026 | levels | 0.26 | 0.44 | 0.60 | 0.65 | 0.66 | **0.74** | 0.72 |
| 2025–Oct 2026 | 13-w changes | −0.05 | 0.09 | 0.27 | 0.35 | 0.36 | **0.41** | 0.35 |

**Interpretation [I].**
- Level correlations over long windows (0.77–0.81) are inflated by shared trends. They barely change with the lag, which is evidence *against* a specific lead.
- On *changes*, which is the honest test, the explanatory power is small: r ≈ 0.15–0.4, so R² ≈ 2–17%. The "best lag" moves from about 4 weeks (2020–22) to about 10 weeks (2023–26) to about 16 weeks (2025–26). A lag that drifts like this is what overfitting looks like.
- In 2023–24, BTC rose from $16.5k to $100k while US net liquidity went *sideways* (about $5.9–6.3T). Spot ETF demand (approved Jan 2024), the halving and the RRP drain offsetting QT explain more than "liquidity up".
- **Conclusion:** liquidity is a meaningful *background* driver. Its direction over 3–6 months tilts the odds. A fixed 10–12 week lead is not a reliable forecasting rule. Teach it as a hypothesis with modest evidence.

**Takeaway.** Global M2 charts are partly dollar charts. Check the constant-FX version and net-of-drains liquidity, and be suspicious of any overlay whose offset was chosen after the fact.

### 2.3 Fed balance sheet (WALCL) and the QE/QT timeline

**Definition.** Total assets of the Federal Reserve (H.4.1 release, every Thursday at 16:30 ET, Wednesday values; FRED `WALCL`, $ millions). Main components: Treasuries, MBS, loans (discount window, BTFP), repo.

**Timeline** [V FRED for levels; S for policy dates]:

| Period | Policy | WALCL | Market context |
|---|---|---|---|
| Nov 2008–Oct 2014 | QE1, QE2, Twist, QE3 | ~$0.9T → ~$4.5T | Post-GFC bull |
| Oct 2017–Jul 2019 | **QT1** (caps up to $50B/mo) | ~$4.5T → ~$3.76T | Q4 2018 S&P −19.8%, BTC −73% (2018) |
| Sep 2019 | Repo spike (SOFR > 5%) → T-bill purchases "not QE" from Oct 2019 | ↑ | Reserves too scarce at ~$1.4–1.5T |
| Mar 2020–Mar 2022 | QE "unlimited", taper from Nov 2021 | $4.17T (Feb 2020) → **$8.965T peak (13 Apr 2022)** | 2020–21 everything rally |
| Jun 2022 | **QT2** begins (cap $47.5B, $95B from Sep 2022) | ↓ | 2022 bear market |
| Mar 2023 | **BTFP** (12 Mar) + discount window after SVB | +~$390B in weeks | BTC +70% in Q1 2023 |
| Jun 2024 | QT taper: UST cap $60B → $25B | ↓ slower | |
| Apr 2025 | UST cap → $5B | ↓ very slow | |
| **1 Dec 2025** | **QT ends**; MBS run-off reinvested into bills | low $6.536T (3 Dec 2025) | BTC already −25% from ATH |
| Dec 2025–mid 2026 | **Reserve management purchases** (RMPs) of T-bills, ~$40B/mo, cut to ~$10B by Jun 2026, paused Aug–Sep 2026 [S] | $6.746T (28 Oct 2026) | |

Sources: SVB and Brookings on the end of QT; Fed July 2026 Monetary Policy Report. The SOMA bought about $250B of bills since early Jan 2026, about $160B of it RMPs [S https://www.federalreserve.gov/monetarypolicy/2026-07-mpr-part2.htm via search].

**Policy now.** Chair Kevin Warsh, in office since 2026, has long argued the balance sheet is too large and has set up a task force on balance-sheet policy. Analysts note that shrinking much further would need changes to bank-liquidity regulation [S First Trust https://www.ftportfolios.com/Commentary/EconomicResearch/2026/8/13/can-warsh-shrink-the-feds-balance-sheet]. **Risk [I]:** a "QT3" or smaller-balance-sheet push under Warsh would be a liquidity headwind that the market has not had to price since 2025.

**Cowen use.** Cowen's recurring claims:
- "BTC dominance tends to go up until QT ends." [S Benzinga Nov 2024 quote: "My base case right now for Bitcoin dominance is that it will likely go higher until quantitative tightening is over."]
- BTC topped about 2 months before QT ended in both 2019 (top 26 Jun 2019, QT end 1 Aug 2019) and 2025 (top Oct 2025, QT end 1 Dec 2025) [S CryptoAdventure].

Check [V/I]: the dates fit. With n = 2, though, "QT end ⇒ top 2 months earlier" is a description, not a law. In 2019 the ensuing alt rotation never came either; ETH/BTC kept falling until 2020.

**Asset effects.** QE is associated with falling real yields, a weaker dollar, and rising equities, crypto and gold (2009–13, 2020–21). QT is associated with rising term premia and tighter liquidity, and hurts high-beta assets most (2018, 2022). Through the RRP/TGA channels, the *pace of QT* matters less than what happens to reserves (§2.6).

### 2.4 Reverse repo facility (ON RRP)

**Definition.** The Fed's overnight reverse repurchase facility. Money-market funds and GSEs lend cash to the Fed against Treasuries at the ON RRP rate (the floor of the funds range). FRED `RRPONTSYD` ($ billions, daily).

**History** [V FRED]:
- Near 0 until Mar 2021.
- Rose to a **record $2.554T on 30 Dec 2022**: excess liquidity from QE and fiscal transfers with nowhere to go.
- Drained to about $0.4–0.5T by 2024 and to near **zero from late 2025**: $0.35B on 29 Oct 2026.

**Why it mattered.** In 2023–24 the RRP drain *offset* QT. Money funds moved cash from the RRP into newly issued T-bills (the Treasury shifted issuance to bills after the June 2023 debt-ceiling resolution), so reserves *rose* even as the Fed shrank its balance sheet. This is the key to the "liquidity paradox" of 2023–24: QT happened, BTC and stocks still rallied, and US net liquidity went sideways rather than down [I/V FRED: reserves rose from $2.83T (Jan 2023) to $3.5T+ (Dec 2023)].

**Now.** With the RRP empty, that buffer is gone. Any further balance-sheet shrinkage or TGA rebuild comes straight out of bank reserves [I].

### 2.5 Treasury General Account (TGA)

**Definition.** The Treasury's cash account at the Fed. It is a liability of the Fed, so when the TGA rises, reserves fall, all else equal. FRED `WTREGEN` (weekly, $ millions). Daily Treasury Statement (fiscaldata.treasury.gov) has daily data.

**Dynamics.** Debt-ceiling standoffs run the TGA down (liquidity injection) and resolutions refill it (liquidity drain).
- 2023: the debt-ceiling deal in June 2023 led to a TGA rebuild of about $0.7T [V FRED].
- 2025: the TGA fell to **$296B on 16 Jul 2025**. After the July 2025 debt-limit increase it was rebuilt to **$958B by 29 Oct 2025** [V FRED].
- That roughly $660B drain coincided with the Aug–Oct 2025 stress: SOFR above IORB, record Standing Repo Facility usage on 31 Oct 2025 (≈$50B) and on 31 Dec 2025 (≈$75B) [S, not verified against NY Fed data]. BTC's Oct 2025 peak and subsequent fall also coincided [I].
- **Now:** about **$1.0T (28 Oct 2026)**, the highest since 2021 [V FRED].

### 2.6 Net liquidity = WALCL − TGA − RRP

**Construction.** Units differ. `WALCL` and `WTREGEN` are $ millions; `RRPONTSYD` is $ billions, so multiply by 1,000. Use Wednesday values. This is a practitioner construct, popularised by Max Anderson and others around 2022. It is **not** an official Fed measure.

**History** [V computed]:

| Date | Net liquidity | BTC | S&P 500 |
|---|---|---|---|
| 18 Mar 2020 | $4.31T | $5.4k | 2,398 |
| **15 Sep 2021 (peak)** | **$7.14T** | $48.1k | 4,481 |
| 10 Nov 2021 (BTC top) | $6.96T | $64.9k | 4,647 |
| 28 Sep 2022 (low) | $5.74T | $19.4k | 3,719 |
| 23 Nov 2022 (BTC low wk) | $6.07T | $16.6k | 4,027 |
| 15 Mar 2023 (BTFP) | $6.35T | $24.4k | 3,892 |
| 13 Mar 2024 | $6.25T | $73.1k | 5,165 |
| 18 Dec 2024 | $5.99T | $97.4k | 5,872 |
| 9 Apr 2025 | $6.25T | $79.6k | 5,457 |
| 8 Oct 2025 (BTC top wk) | $5.78T | $121.7k | 6,754 |
| **3 Dec 2025 (low)** | **$5.60T** | $93.2k | 6,850 |
| 1 Jul 2026 (BTC low wk) | $5.84T | $59.9k | 7,483 |
| 28 Oct 2026 | $5.75T | $81.2k | 7,744 |

**Episode reading [I/V]:**
- **2020–21.** Net liquidity +66% (Mar 2020 → Sep 2021). BTC ×12, S&P ×1.9. The net liquidity peak (Sep 2021) came about 2 months before the BTC top (Nov 2021) and about 4 months before the S&P top (Jan 2022). This is the episode that made the indicator famous.
- **2022.** Net liquidity −20% (Jan → Sep 2022). BTC −64%, S&P −19.4% for the year. Net liquidity bottomed in Sep 2022, about 2 months before the BTC low (Nov) and about 2 weeks before the S&P low (12 Oct 2022). Consistent with the narrative.
- **2023–24.** Net liquidity roughly flat (5.8–6.35T), with BTC ×6 and S&P +50%. **The narrative breaks.** The level correlation 2023–Oct 2026 is −0.26 for BTC and −0.54 for the S&P. Drivers: AI earnings, ETF flows, the halving and fiscal deficits.
- **2025–26.** Net liquidity fell from $6.25T (Apr 2025) to $5.60T (Dec 2025) on the TGA rebuild and late QT. BTC topped in Oct 2025 and fell to $58.6k by Jun 2026. Net liquidity recovered modestly to $5.99T (Jul 2026) and BTC rebounded to about $86k (early Oct). Since 2025 the fit has improved again, with r ≈ 0.74 at a 16-week lag. The S&P ignored the 2025–26 decline in net liquidity entirely.

**Takeaway.** Net liquidity is the right *concept*: reserves available to the system. As a *model* it explains crypto better in liquidity-dominated regimes (2020–22, 2025–26) than in earnings- or flow-dominated ones (2023–24). Equities decoupled first.

### 2.7 Bank reserves, SOFR and repo stress

**Data.**
- Reserve balances with Federal Reserve Banks: `WRESBAL` (weekly).
- SOFR (Secured Overnight Financing Rate, NY Fed, daily, `SOFR`).
- IORB (interest on reserve balances) is the administered ceiling-ish rate. Fed funds target range: `DFEDTARU`/`DFEDTARL`.
- Standing Repo Facility (SRF) usage: NY Fed website.

**How to read it.** When reserves are "ample", SOFR trades a few bp *below* IORB. When reserves approach "scarce", SOFR trades *above* IORB, repo spikes at month-, quarter- and tax-date ends, and the Fed must add reserves. That is what happened in Sep 2019 (SOFR reached 5.25%, reserves about $1.4T) [S] and again in Sep–Dec 2025 [S].

**Latest** [V FRED]:
- Reserves **$2.89T** (28 Oct 2026), versus a $3.0–3.3T range in 2024–mid 2026 and $3.98T at the 2021 peak.
- SOFR **3.94%** with the target range 3.75–4.00%. SOFR is near the top of the range: tight funding, partly the TGA at $1T [I].

**Bank Term Funding Program (2023).** Created 12 Mar 2023 after Silicon Valley Bank failed. The BTFP lent for up to 1 year against Treasuries/MBS valued **at par**, which removed the forced-sale risk from unrealised losses. Usage peaked at about $165–168B in early 2024. New lending stopped on 11 Mar 2024 [S]. Market effect: the March 2023 balance-sheet jump (≈+$390B) and net liquidity +$0.55T in 3 weeks coincided with BTC rallying from about $20k to about $28k and the "BTC as a bank-crisis hedge" narrative [V/I].

**Takeaway.** Reserves near $2.9T, an empty RRP and a $1T TGA mean the system has less slack than at any time since 2019. Funding-market hiccups are a plausible Q4 2026 risk channel for leveraged crypto [I].

### 2.8 QT taper and end of QT: what it did to markets [I]

From the June 2024 taper to the December 2025 end of QT, the S&P rose about 25%, BTC peaked (Oct 2025) and fell, and dominance rose. The "end of QT = bullish for alts" idea Cowen discussed (ETH/BTC bouncing after QT ends, with 2019–20 as the analogue) [S Benzinga Mar 2025 headline] did not produce an alt season by Oct 2026. Ending QT is a *necessary-ish* condition in Cowen's story, not a sufficient one.

---

## 3. The dollar and FX

### 3.1 DXY (ICE US Dollar Index)

**Definition.** A geometric-weighted index of USD against six currencies, unchanged since 1999 (euro introduction): **EUR 57.6%**, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%. Base Mar 1973 = 100 [S ICE methodology]. Trades nearly 24/5. Tickers: TradingView `TVC:DXY`, `ICEUS:DX1!` (futures). Not on FRED.

**How to read it.** With the euro at almost 58%, DXY is mostly the inverse of EURUSD. It omits CNY, MXN and KRW and so understates trade-relevant dollar moves. Above 100 is often called "strong" and moves of more than 10% in 12 months are "violent". The 2022 move (+19% from Jan to Sep) was the biggest in decades.

**Latest.** DXY ≈ **101.7** (30 Oct 2026) [S tradingeconomics]. EURUSD 1.12 (23 Oct) [V FRED `DEXUSEU`]. Context: DXY fell about **10.8% in H1 2025**, its worst first half since 1973 [S Business Insider/Yahoo https://finance.yahoo.com/news/dollar-posted-worst-first-half-153518559.html]. It made a 2026 low in late January and has been range-bound since, with a modest war-safe-haven bid [I/V broad index].

### 3.2 Broad trade-weighted dollar

**Definition.** Fed Nominal Broad U.S. Dollar Index, 26 currencies weighted by trade (China ≈ 13–15%, Mexico, Canada, the euro area, Japan…). Daily, `DTWEXBGS` (Jan 2006 = 100) [V FRED]. Also real (CPI-deflated) broad indices.

**Latest** [V FRED]: **121.32 (23 Oct 2026)**. Peaks 128.45 (26 Sep 2022) and 130.04 (13 Jan 2025); 2026 low 117.44 (29 Jan 2026).

**Takeaway.** Use the broad index to judge financial-conditions impact on the world and EM. Use DXY for market chatter and for EURUSD-driven moves.

### 3.3 Dollar vs BTC, gold and stocks: when the inverse correlation holds and when it breaks

**Mechanism.**
1. A strong dollar tightens *global* financial conditions, because about half of cross-border credit is dollar-denominated, and so pressures risk.
2. Assets priced in USD fall mechanically when the dollar rises.
3. A strong dollar usually reflects relatively tighter Fed policy or a risk-off safe-haven bid.

**Computed BTC vs broad dollar, daily return correlation by year** [V computed `CBBTCUSD` vs `DTWEXBGS`]: 2015 0.00, 2016 0.05, 2017 0.03, 2018 −0.01, 2019 −0.01, **2020 −0.30**, 2021 −0.15, **2022 −0.29**, 2023 −0.10, 2024 0.03, 2025 −0.14, **2026 −0.22**.
*Reading [I]:* the inverse link is real but *modest* and *regime-dependent*. It was strongest in the macro-dominated years (2020, 2022, 2026) and absent before institutional adoption (2015–19).

**Cowen's framing.** "Bitcoin bear markets have tended to correlate with the Dollar Index's sharp moves to the upside and vice versa" [S Daily Hodl/Informer]. In April 2022: "The parabolic rally by DXY does not bode well for risk-on assets like stocks and Bitcoin. Until the rally cools off, playing defense is the way to go" [S Cointelegraph https://cointelegraph.com/news/bitcoin-rejects-40k-as-us-dollar-strength-hits-20-year-high]. He also warns that DXY *weakness alone* is not a reason to turn bullish on BTC [S Informer Post, undated]. The 2025 episode bears that out.

**DXY peaks vs BTC cycle bottoms**:

| Episode | DXY peak | BTC low | Lag (BTC vs DXY) | Notes |
|---|---|---|---|---|
| 2015 | ~100.4 (13 Mar 2015) [S] | 14 Jan 2015 (~$170 close; Aug 2015 retest) | BTC **≈2 months before** | Dollar surge 2014–15 overlapped the BTC bear. DXY then ranged; BTC's 2016–17 bull coincided with DXY peaking (103.8, Dec 2016/Jan 2017) and falling ~10% in 2017 [S] |
| 2018–19 | DXY *rose* from 88 (Feb 2018) to ~97–98 (Nov–Dec 2018), kept rising to ~99 (Oct 2019) and 103 (Mar 2020) [S] | 15 Dec 2018 (~$3.2k) | No DXY peak near the BTC low | **Counter-example:** BTC bottomed and rallied ×4 in 2019 while the dollar was rising |
| Mar 2020 | 102.99 (19–20 Mar 2020, dash for cash) [S] | 12–13 Mar 2020 (~$3.8–4.9k) | BTC ≈1 week before | Liquidity crisis: everything was sold for dollars, then Fed swap lines and QE |
| 2022 | **114.78 (28 Sep 2022)** [S]; broad 128.45 on 26 Sep [V] | **21 Nov 2022 (~$15.5k)** | BTC **≈8 weeks after** | S&P low 12 Oct 2022 (2 wks after). BTC delayed by FTX (Nov). Cleanest supporting case |
| 2025 | ~110 (13 Jan 2025); broad 130.04 [V] | Local low 7 Apr 2025 (~$75–76k), then ATH Oct 2025 | BTC rallied as the dollar fell | Then **counter-example:** BTC −53% top-to-trough (Oct 2025–Jun 2026) while the dollar was *flat-to-weaker* |

**Verdict [I].** "Dollar peak → BTC bottom within ~0–3 months" fits 2020 and 2022, fails 2018, and is ambiguous in 2015. A falling dollar is supportive but not sufficient: in 2025–26 BTC fell despite it. The dollar is better read as a *financial-conditions* input alongside real yields and liquidity.

**Gold and the dollar.** Usually inverse, but in 2022–26 gold rose *with* a strong dollar at times because central-bank buying (de-dollarisation after Russia's reserves were frozen in 2022) dominated [S/I]. **Stocks and the dollar.** Usually inverse for US multinationals (≈40% of S&P revenue is foreign), but in global risk-off both the dollar and US stocks can rise relative to the rest of the world [I].

### 3.4 USDJPY, BOJ hikes and the yen carry trade (5 Aug 2024)

**Definition.** USDJPY = yen per dollar. FRED `DEXJPUS` (noon NY buying rate, daily). TradingView `FX:USDJPY`. Carry trade: borrow in a low-yield currency (JPY), invest in higher-yield assets (USD bonds, equities, EM, crypto). It is profitable while the funding currency is stable or weakening, and it unwinds violently when the funding currency spikes.

**The 2024 episode** [V FRED + S]:
- USDJPY peaked at **161.73 (10 Jul 2024)** [V FRED], a 38-year yen low. Japan's MoF intervened on 11–12 Jul.
- The **BOJ hiked to 0.25% on 31 Jul 2024** and signalled more. The Fed held the same day, but weak US data (2 Aug payrolls; the Sahm rule triggered) priced fast Fed cuts. The rate gap closed from both sides [S BIS Bulletin 90 https://www.bis.org/publ/bisbull90.pdf].
- **5 Aug 2024:** Nikkei −12.4%, its worst day since 1987. VIX intraday about 65.7 (close 38.57 [V FRED]). USDJPY fell to **143.95** [V FRED], about −11% in 4 weeks. BTC went from about $66.8k (29 Jul) to **$54.0k on 5 Aug (Coinbase daily)** [V FRED], about −19%, with an intraday low near $49k [S]. S&P 5,186 (5 Aug), −8.5% from its 16 Jul high [V FRED].
- **Recovery:** the S&P made new highs within about 6 weeks. BTC took until Nov 2024 (the US election) to break out.

**Cowen's link.** He has explicitly compared later BOJ-tightening setups to July 2024: "the Fed cut rates while the BOJ raised rates, leading to the unwind of the carry trade" [S aggregator, undated, unverified].

**2025–26.**
- BOJ: 0.5% (Jan 2025), **0.75% (Dec 2025)**, **1.0% (16 Jun 2026)**, **1.25% (18 Sep 2026)**, the highest since 1995. The September vote was 7–2. JGB purchase taper continues [S CNBC https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html].
- The yen nonetheless *weakened*: USDJPY reached **163.86 on 29 Jul 2026** [V FRED], prompting coordinated US–Japan intervention [S]. Now 156.87 (23 Oct) [V FRED].
- Why no 2024-style unwind [I]? The Fed was *hiking* too (Sep 2026), so the rate differential did not collapse from both sides. The 2024 crash needed the BOJ to tighten *and* the Fed to be expected to ease at the same time.

**Takeaway.** Watch the *change* in the US–Japan rate differential and the speed of yen appreciation. A 5–10% yen rally in weeks has been the danger signal, not the BOJ level itself.

### 3.5 China / PBOC liquidity

**What to watch.** PBOC policy rates (7-day reverse repo, LPR), reserve requirement ratio cuts, MLF/outright reverse-repo injections, China M2 and total social financing (TradingView `ECONOMICS:CNM2`), CNY fixing. China is the largest component of "global M2" in local currency, so CNY moves and PBOC easing move global-M2 charts.

**2026 state [S].** The PBOC guided to "moderately loose" policy with RRR and rate cuts "when appropriate". It cut structural relending rates by 25 bp (to 1.25%) in Jan 2026 and ran large MLF operations (¥900B). The 2025 policy-rate cut was only 10 bp. I could not verify further 2026 headline rate cuts [S MNI/investinglive/China Daily].

**History.** PBOC/China credit impulses helped the 2016–17 global reflation (and crypto boom) and the 2019 recovery [S/I]. Crypto links to China have weakened since the 2021 mining and trading ban [I].

**Takeaway.** China matters for global-M2 arithmetic and commodities (copper, oil demand). It is now an indirect driver for crypto.

---

## 4. Equities and cross-asset

### 4.1 S&P 500, Nasdaq 100, Russell 2000

**Definitions and tickers.**
- **S&P 500:** 500 large US companies, float-adjusted cap-weighted. FRED `SP500` covers only the last 10 years of daily data. TradingView `SP:SPX`; ETFs SPY/VOO/IVV.
- **Nasdaq 100:** the 100 largest non-financial Nasdaq-listed stocks, modified cap-weight, tech-heavy. FRED `NASDAQ100`; TradingView `NASDAQ:NDX`; ETF QQQ.
- **Russell 2000:** small caps, ranks 1001–3000 of the Russell 3000. TradingView `TVC:RUT`; ETF IWM. It is the most rate- and credit-sensitive US index: much floating-rate debt and many unprofitable firms.

**Latest** [V FRED unless noted]:
- S&P **7,743.98** (28 Oct 2026). ATH **7,818.93 (6 Oct 2026)**. 2026 low 6,343.72 (30 Mar 2026, the Iran-war shock low), a peak-to-trough fall of −9.1% from the 27 Jan high of 6,978.6. YTD +13.1%.
- Nasdaq 100 **29,402.51** (29 Oct). ATH 31,224.69 (6 Oct), so −5.8%.
- Russell 2000 made a record close of about **3,068 in mid-Aug 2026**. It was +22.7% YTD on 12 Aug versus the S&P's +13.2% [S Regards of Wall Street/investinglive]. Small caps leading in a year of rate *hikes* is unusual. The likely drivers are the manufacturing upswing (small caps track the ISM), energy and industrial exposure, and domestic revenue in a tariff world [I].

**How Cowen uses the S&P.**
- He regularly overlays BTC on the S&P to argue that BTC is a high-beta risk asset.
- He uses the S&P's 1962–1982 history to argue that an "apathetic" or quiet top does not prevent a bear market [S CoinMarketCap/BeInCrypto].
- He uses the S&P's midterm-year lows (often October, sometimes May, sometimes December) to time the BTC four-year-cycle low [S X post: "The SPX would often bottom in October, but occasionally it would occur earlier (May) and sometimes later (December)"].

### 4.2 Equal-weight S&P (RSP) vs cap-weight, and market breadth

**Definition.** The S&P 500 Equal Weight Index (TradingView `SP:SPXEW`; ETF RSP) rebalances quarterly to 0.2% each. The **RSP/SPY ratio** measures whether the "average stock" beats the megacaps.

**Breadth tools.** Percentage of S&P members above their 200-day moving average (TradingView `INDEX:S5TH`), the NYSE advance–decline line, new highs minus new lows, and Russell 2000 relative to the S&P.

**How to read it.** Narrow leadership (falling RSP/SPY while the index rises) is often called "unhealthy". Historically it has preceded corrections, for example 1999–2000 and 2021. Concentration can last for years, though: 2023–2026 [I]. Broad participation, with the advance–decline line making new highs, has historically argued against a major top within months [S practitioner rule].

**Latest.** Equal weight led for most of 2026 and the lead flipped in mid-September. The **RSP/SPY ratio hit a record low of 0.2710 on 7 Oct 2026**, about 31% below its 2015 peak [S openingbelldailynews]. On a total-return basis the two were roughly tied YTD through 21 Oct (RSP +14.4%, SPY +14.3%) [S]. The top 10 names are about **39%** of the S&P (30 Sep 2026) [S].

**Takeaway.** Record concentration makes the S&P effectively an AI/megacap earnings bet. Index-level valuation (CAPE) is dominated by about 10 companies.

### 4.3 VIX

**Definition.** CBOE Volatility Index: the 30-day implied volatility of S&P 500 options, in annualised %. FRED `VIXCLS`; TradingView `TVC:VIX`. VIX/16 ≈ the expected daily move in %.

**Levels.**
- Below about 13–15 signals complacency. Above about 30 signals stress.
- Closing records: **82.69 (16 Mar 2020)** and 80.86 (20 Nov 2008). Intraday record 89.53 (24 Oct 2008) [S].
- **5 Aug 2024**: intraday about 65.7 with a close of 38.57 [V FRED close].
- **8 Apr 2025** (tariff shock): close 52.33 [V FRED].
- **2026 max** close 31.05 on 27 Mar (Iran war) [V].
- **Now 16.91** (28 Oct) [V].

**Relationships.** VIX spikes are mean-reverting. Buying the S&P after VIX closes above 30 has historically produced positive 6–12 month returns in most cases, the 2008 crisis aside [S]. VIX term-structure inversion (VIX > VIX3M) marks acute stress. BTC tends to fall in VIX spikes: Mar 2020, Aug 2024, Apr 2025 [V FRED].

**Takeaway.** A VIX of 17 alongside Brent at $120+ and a Fed in hiking mode looks like complacency relative to the macro risk. Implied vol stays low until something breaks [I].

### 4.4 Shiller CAPE

**Definition.** Cyclically adjusted P/E: real S&P price divided by the 10-year average of real earnings. Robert Shiller's data runs back to 1871 (econ.yale.edu/~shiller/data.htm; multpl.com).

**Levels.** Long-run mean about 17. The 1929 peak was about 32, the Dec 1999 record **44.2**, the Nov 2021 peak about 38. Oct 2026 is about **40.7** (multpl daily about 41.6 on 8 Oct). Only readings from 1999–2000 have been higher [S GuruFocus/thetrading.tools/chartrow].

**How to read it.** High CAPE predicts *low 10-year real returns* (R² roughly 0.4–0.5 historically). It is nearly useless for 1-year timing. CAPE above 30 persisted for most of 2017–2026 [S/I]. Critics point to accounting changes (FAS 142 write-downs depressing past earnings), a structurally higher margin and tech share, and lower real rates. Their counterpoint now is that real rates are *not* low: the 10Y is at 5% [I].

### 4.5 Buffett indicator

**Definition.** Total US equity market cap (Wilshire 5000 or FRED's Z.1 nonfinancial corporate equities) divided by GDP or GNP. Warren Buffett (2001 Fortune) called it "probably the best single measure" of valuation and said that approaching 200% is "playing with fire" [S Motley Fool].

**Latest.** Readings vary widely by construction: **about 234–236%** (GuruFocus) versus **288–301%** (other trackers) in Oct 2026 [S]. All are record territory, above 2000 (about 140–150%) and 2021 (about 200%) [S/I]. Caveat: a rising foreign-revenue share and higher margins make market cap to *domestic* GDP drift upward structurally.

### 4.6 Forward P/E

**Definition.** Price divided by consensus next-12-month operating EPS (FactSet, LSEG).

**Latest.** **18.7** (FactSet, 23 Oct 2026), *below* the 5-year (19.8) and 10-year (19.1) averages, because 2026 EPS is growing about 30% [V FactSet]. LSEG reported about 19.1 [S].

**The disagreement [I].** CAPE about 41 says "very expensive on normalised earnings". Forward P/E of 18.7 says "fair if forecasts hold". The two reconcile only if the 2026 earnings surge (AI capex, energy, margins at 15%) is durable. Earnings forecasts are pro-cyclical, so forward P/E typically looks cheapest just *before* earnings roll over (2000, 2007).

### 4.7 Gold, silver and the gold/silver ratio

**Data.** LBMA gold price (FRED removed its LBMA series in 2022), TradingView `TVC:GOLD` / `OANDA:XAUUSD`, COMEX futures `GC1!`. Silver `TVC:SILVER`. Gold/silver ratio `TVC:GOLD/TVC:SILVER`.

**Drivers.**
1. Real yields (inverse; strong in 2006–2021).
2. The dollar (inverse).
3. **Central-bank buying.** It accelerated after Russia's reserves were frozen in 2022 and broke the real-yield relationship from 2022 onward [S/I].
4. Safe-haven and debasement fear.

**Recent path.**
- Gold made a parabolic run in 2025–Jan 2026. COMEX futures reached about **$5,627 on 29 Jan 2026** and fell more than $880 the next day (settle $4,745) [S Barchart]. Spot records were around $4,970–5,600 depending on source [S].
- Silver futures reached a record **$121.79 (29 Jan 2026)** and settled at $78.53 a day later [S].
- **Now (29–30 Oct 2026):** gold about **$4,024**, silver about **$51–52**, gold/silver ratio about **77** [S tradingeconomics/investing]. Gold is about −28% from the futures peak, during a war. That fits *real yields rising* (10Y 5.0–5.3%, Fed hiking) plus unwinding of a crowded parabola, not "the safe haven failed" [I].

**Gold/silver ratio.** The historical range is about 30–125 (125 in Mar 2020). High readings mean fear and deflation; low readings mean reflation and speculative excess. Silver is part monetary, part industrial (solar), so it outperforms gold in the late stages of metal bull runs and underperforms in busts [S/I].

**BTC–gold.** The 30-day correlation hit **−0.88 in Mar 2026** (CryptoQuant), then flipped to a **90-day correlation of about 0.5–0.86 by early Sep 2026**, a roughly 6-year high, as both fell together [S The Block https://www.theblock.co/news/markets/2026-09-03-bitcoin-gold-correlation-hits-six-year-high-but-analysts-question-whether-equity-decoupling-will-last-413437]. Over longer windows the correlation is close to zero and unstable. "Digital gold" is a narrative, not a stable statistical property [I].

### 4.8 Copper/gold ratio vs the 10-year yield

**Definition.** The price of copper ($/lb) divided by gold ($/oz). Copper is cyclical demand; gold is a haven. A rising ratio means reflation and growth. Popularised by Jeffrey Gundlach as a 10Y "fair value" guide. TradingView `COMEX:HG1!/COMEX:GC1!` against `TVC:US10Y`.

**Evidence.**
- The relationship held tightly from about 2000 to 2021: 60-day correlation averaged about 0.85 [S eco3min/AhaSignals].
- **It broke from 2022 to 2026.** Central-bank gold buying depressed the ratio while yields rose on inflation, deficits and term premium. The 60-day correlation was about 0.08 in early-to-mid 2026, and the 10Y was trading above its ratio-implied level [S].
- Gundlach has reportedly called the copper/gold–10Y model a failure and now prefers oil and the dollar [S].
- Copper itself reached record highs: about $6.4/lb in mid-2026, +36% YoY [S].

**Takeaway.** A broken intermarket relationship is itself information. Today's 10Y (5.05% [V FRED `DGS10`]) reflects inflation, supply and term premium more than growth.

### 4.9 Oil and recessions; equities before and after recessions

**Oil data.** WTI `DCOILWTICO` (daily) and `WTISPLC` (monthly from 1946); Brent `DCOILBRENTEU` [V FRED]. TradingView `TVC:USOIL`, `TVC:UKOIL`.

**Hamilton's finding.** James Hamilton found that 10 of 11 post-war US recessions (to 2008) were preceded by a sharp oil-price rise, while noting that oil was a contributing factor and not the sole cause [S NBER Reporter 2011 https://www.nber.org/reporter/2011number2/oil-price-shocks; Econbrowser].

**My check** [V computed from `WTISPLC`; max price within 18 months before to 3 months after the recession start, versus the 24-month-prior minimum]:

| Recession start | Oil rise into it | Verdict |
|---|---|---|
| Dec 1969 | +12% | No spike |
| Nov 1973 | **+184%** (OPEC embargo) | Yes |
| Jan 1980 | **+166%** (Iranian revolution) | Yes |
| Jul 1981 | (same 1979–80 spike) | Partial |
| Jul 1990 | **+160%** (Iraq invades Kuwait, Aug 1990; spike concurrent) | Yes |
| Mar 2001 | **+205%** (1999–2000 rebound; spike 12–18 months earlier) | Yes, long lag |
| Dec 2007 | **+93%** to Mar 2008, then $133 (Jul 2008 monthly) | Yes |
| Feb 2020 | +57% (2017–18), but the cause was the pandemic | No (exogenous) |

**Spikes without recessions** (12-month change ≥ +50%) [V computed]: 1987, 1999 (preceded 2001 by about 19 months), 2002–05, 2009–10 (rebound), 2017–18, **2021–22 (+113% YoY; WTI $123 in Jun 2022)**, **2026 (+58% YoY in Apr 2026; WTI $108.6 on 30 Apr, $103 now; Brent spot up to about $127–132)**.

**Reading [I].**
- Oil spikes are a *common ingredient* of recessions, not a sufficient cause.
- Spikes driven by supply shocks (1973, 1979, 1990, 2026) are more dangerous than demand-driven ones (2004–08 until the very end, 2021).
- The US shale revolution makes the US a net exporter, so higher oil now transfers income from consumers to producers within the US (energy capex, Texas) rather than abroad. That softens the GDP hit while still hurting real consumer income and sentiment. Hence the record-low Michigan reading alongside 3.4% GDP.
- The biggest recession channel in 2026 is the **policy response**: Fed hikes and 5% yields, as in 1973–74, 1979–81 and 2008 (the ECB in July 2008).

**Equities around recessions** [S: standard S&P history via Motley Fool, First Trust, Kathmere; dates and levels from the S&P record; I assembled the table]:

| NBER recession | S&P peak (date, level) | Peak vs start | Trough (date, level) | Decline | Trough vs NBER end |
|---|---|---|---|---|---|
| Dec 1969–Nov 1970 | 29 Nov 1968, 108.4 | 12 mo before | 26 May 1970, 69.3 | −36% | 6 mo before |
| Nov 1973–Mar 1975 | 11 Jan 1973, 120.2 | 10 mo before | 3 Oct 1974, 62.3 | −48% | 5 mo before |
| Jan–Jul 1980 | 13 Feb 1980, 118.4 | 1 mo **after** | 27 Mar 1980, 98.2 | −17% | 4 mo before |
| Jul 1981–Nov 1982 | 28 Nov 1980, 140.5 | 8 mo before | 12 Aug 1982, 102.4 | −27% | 3 mo before |
| Jul 1990–Mar 1991 | 16 Jul 1990, 369.0 | same month | 11 Oct 1990, 295.5 | −20% | 5 mo before |
| Mar–Nov 2001 | 24 Mar 2000, 1,527 | 12 mo before | 9 Oct 2002, 776.8 | −49% | **11 mo after** |
| Dec 2007–Jun 2009 | 9 Oct 2007, 1,565 | 2 mo before | 9 Mar 2009, 676.5 | −57% | 3 mo before |
| Feb–Apr 2020 | 19 Feb 2020, 3,386 | same month | 23 Mar 2020, 2,237 | −34% | 1 mo before |

- Averages: decline about **−36%** (median about −35%). Peak lead about 5 months (range −1 to +12).
- Bear markets *without* recession run shallower: 1962 (−28%), 1966 (−22%), 1987 (−34% crash, no recession), 1998 (−19%), 2011 (−19%), 2018 (−19.8%), **2022 (−25.4%)**. They average about −20% to −25% [S/I].
- **Lesson:** the size of an equity drawdown depends heavily on whether earnings fall, i.e. on recession.
- For crypto: BTC's 2018 and 2022 bear markets (−84%, −77%) happened *without* US recessions. Crypto cycles are not primarily recession-driven [V/I].

**What equities do around recession onset (pattern) [I/S]:**
1. The S&P often makes its high near the end of Fed tightening or at the first cuts.
2. A first leg down comes on growth scares.
3. The steepest declines come *inside* the recession, as earnings estimates are cut and unemployment rises.
4. The low arrives when the news is worst: unemployment still rising, often 3–6 months before the recession ends.
5. The recovery is led by small caps and cyclicals (and, in recent cycles, high-beta assets including crypto: BTC +305% in 2020).

### 4.10 BTC–SPX and BTC–Nasdaq rolling correlation

**Computed** [V; daily log returns on common trading days, `CBBTCUSD` vs `SP500`/`NASDAQ100`; also weekly Wednesday-to-Wednesday]:

| Year | BTC–SPX daily | BTC–NDX daily | BTC–SPX weekly | BTC return | S&P return |
|---|---|---|---|---|---|
| 2017 | 0.06 | 0.05 | 0.20 | +1,324% | +19.4% |
| 2018 | 0.07 | 0.07 | 0.21 | −73% | −6.2% |
| 2019 | −0.11 | −0.09 | −0.09 | +94% | +28.9% |
| 2020 | **0.43** | 0.43 | 0.59 | +306% | +16.3% |
| 2021 | 0.26 | 0.25 | 0.30 | +59% | +26.9% |
| 2022 | **0.56** | **0.58** | **0.71** | −64% | −19.4% |
| 2023 | 0.16 | 0.19 | −0.16 | +156% | +24.2% |
| 2024 | 0.28 | 0.24 | 0.39 | +123% | +23.3% |
| 2025 | **−0.02** | 0.00 | 0.44 | −7% | +16.4% |
| 2026 YTD | **0.44** | 0.42 | 0.32 | −11% | +13.1% |

Additional statistics [V computed]:
- 90-trading-day rolling BTC–SPX correlation: **max 0.62 (13 Jul 2022)**, **min −0.33 (18 Aug 2025)**, latest 0.38 (28 Oct 2026).
- **Asymmetry.** BTC beta to S&P on S&P *down* days versus *up* days: 2022 **1.90 vs 1.12**; 2026 **1.68 vs 1.20**; 2024 1.30 vs 1.27 (symmetric). In 2026, BTC averaged −1.04% on S&P down days and +0.88% on up days, while the S&P itself was up 13%.

**Caveat.** BTC trades 24/7. The Coinbase daily stamp is not synchronous with the 4 pm NYSE close, which biases daily correlations toward zero. Weekly figures are more robust but noisier.

**Interpretation [I].**
1. The BTC–equity link became material only with institutional participation and the 2020 macro regime.
2. It peaks during macro-driven bear markets (2022) and in rate-shock regimes (2026).
3. Correlation says nothing about *relative* performance. In 2025–26 BTC was correlated with the S&P on a daily basis yet underperformed it by about 25–35 pp per year. That fits Cowen's "BTC lags when global liquidity is not expanding; AI keeps the S&P up" [S].

### 4.11 Bitcoin spot ETF flows: macro role

**Data.** Farside Investors, SoSoValue, Bitbo and TFTC dashboards (daily net flows per ETF; IBIT, FBTC, etc.). The US spot ETFs launched on 11 Jan 2024.

**2026.** Monthly net flows (TFTC): Apr +$2.0B, **Jun −$4.5B** (around the BTC low), Aug +$3.5B, Sep +$2.6B, Oct about −$0.5B at mid-month. IBIT took in +$665M on 19 Oct (SoSoValue), its largest day since Oct 2025. IBIT assets are about $67B (29 Oct) [S TFTC/The Block/Yahoo].

**Macro role [I].**
- ETF flows are a *transmission channel* of macro risk appetite into BTC: advisers, RIAs and hedge-fund basis trades. They are not an independent driver.
- They are pro-cyclical and momentum-following: outflows clustered near the Jun 2026 low, as they did in early 2025.
- Part of the flow is the cash-and-carry basis trade (long ETF, short CME futures), which depends on funding rates (SOFR) and the futures basis, so it is a *rates* trade, not a directional bet.
- In 2024 ETF demand helped BTC rise while net liquidity was flat, the main reason the liquidity model broke then.

---

## 5. Seasonality and political cycles

### 5.1 The presidential (four-year) cycle in the S&P 500

**Claim.** Stock returns differ systematically by the year of the US presidential term: post-election (Y1), midterm (Y2), pre-election (Y3) and election (Y4). It was popularised by Yale Hirsch (Stock Trader's Almanac, from 1967).

**Commonly cited averages since 1950** (price returns; approximate, varying by source): Y1 about +6–7%, **Y2 about +4–5% (weakest)**, **Y3 about +16–17% (strongest)**, Y4 about +7% [S Almanac/CFRA/LPL summaries; I reconstructed the midterm mean as about +4.6% from published annual returns 1950–2022, so verify before publishing].

**Proposed mechanism.**
1. Administrations front-load painful policies early in the term and stimulate before re-election.
2. Midterm policy uncertainty: markets dislike not knowing which party controls Congress.
3. After the midterm, gridlock is priced and uncertainty resolves.

Evidence for a *causal* mechanism is weak. The pattern rests on about 19 cycles since 1950 [I].

### 5.2 The midterm year: drawdown and the rally from the low

- **Average intra-year peak-to-trough drawdown in midterm years:** about **17.5%** since 1950 (Carson/Plain Economy) [S], about 16.7% (Dreyer Wealth, 1950–2022) [S], about 19% (Longview, 25 cycles since 1926) [S], about 20% (First Trust) [S]. Use "about 17–20%" in teaching. Non-midterm years average roughly 13%.
- **Rally from the midterm low:** the S&P has averaged about **+32%** in the 12 months after the lowest close of a midterm year since 1950, positive in 19/19 cases (Silvia Insights). First Trust and MoneyFlows put it at about +36% [S https://plaineconomy.com/stock-market-after-midterm-elections/; https://www.ftportfolios.com/Commentary/Insights/2024/4/8/midterm-election-client-resource-kit---march-2024]. Hindsight bias: the "lowest close" is known only afterwards.
- **From election day:** the S&P was higher 12 months later after all 19 midterms since 1950, by an average of about 15% [S].
- **Timing of midterm lows:** most often in late Q3 or October (1962 June/Oct, 1966 Oct, 1974 Oct, 1990 Oct, 2002 Oct, 2022 Oct). Sometimes earlier: 2010 Jul, 2014 Oct (mini), 2018 Dec [S/I].
- **2026 so far:** the drawdown was only about **9.1%** (27 Jan 6,978.6 → 30 Mar 6,343.7), shallower than average, and the index then made new highs [V FRED]. Either the midterm "pain" came early and was mild, or the seasonal pattern is being overridden by a ~30% earnings boom [I].
- **Midterm elections** are on 3 Nov 2026. The Fed held on 28 Oct, with Warsh saying politics had "no role" [S].

### 5.3 "Sell in May", September weakness, Q4 strength

- **Sell in May / best six months.** Since 1950, Nov–Apr has delivered most of the S&P's price gains (about +7% average) versus May–Oct (about +2%) [S Stock Trader's Almanac, commonly cited]. A Bouman–Jacobsen (2002, AER) study found a "Halloween effect" in 36 of 37 countries [S]. The effect is weaker after its publication, and May–Oct is still positive on average. Selling means missing positive expected returns and paying taxes and costs [I].
- **September** is the worst month for the S&P since 1950, averaging about −0.5% to −0.7% and positive only about 44% of the time [S Almanac/Motley Fool/Advisor Perspectives]. September 2026: the S&P was roughly flat (7,708 on 19 Aug → 7,704 on 24 Sep) [V FRED].
- **Q4 strength.** Oct–Dec, and especially Nov–Dec plus the "Santa Claus rally" (last 5 trading days of the year and first 2 of the next), has been seasonally strong. Q4 of the *midterm* year through Q2 of the pre-election year is the "sweet spot" of the four-year cycle [S].

### 5.4 BTC seasonality

**Monthly** [V computed from Coinbase daily closes, 2015–Sep 2026; month-end to month-end; 11–12 observations each]:

| Month | Mean | Median | Positive |
|---|---|---|---|
| Jan | −1.7% | −0.3% | 5/12 |
| Feb | +10.6% | +12.4% | 9/12 |
| Mar | +0.7% | +2.2% | 6/12 |
| Apr | +10.3% | +12.2% | 8/12 |
| May | +7.7% | +9.1% | 6/12 |
| Jun | −0.3% | 0.0% | 6/12 |
| Jul | +8.9% | +8.1% | 9/12 |
| Aug | +2.3% | −5.0% | 4/12 |
| Sep | −1.2% | +2.8% | 6/12 |
| **Oct** | **+19.1%** | **+14.4%** | **9/11** |
| Nov | +6.7% | +6.6% | 6/11 |
| Dec | +9.7% | +0.3% | 6/11 |

**Q4 by year (BTC):** 2015 +81%, 2016 +60%, 2017 +220%, **2018 −44%**, 2019 −14%, 2020 +169%, 2021 +5%, **2022 −15%**, 2023 +57%, 2024 +55%, **2025 −26%** [V computed].

**Reading [I].** "Uptober" is real in-sample but driven by bull-cycle years. In both midterm years with Coinbase data (2018 and 2022), BTC's Q4 was *negative*: −44% and −15%. Q4 2014 (Bitstamp) was also negative, roughly −15–20% [S, approximate]. This matches Cowen's "Q4 drop in midterm years" roadmap. The sample is n = 3, and monthly seasonality across 11 years has huge standard errors.

### 5.5 Midterm years and BTC bear markets: testing the claim

| Midterm year | BTC full-year return | Prior cycle peak | Cycle low | Low inside the midterm year? | S&P that year |
|---|---|---|---|---|---|
| 2010 | Enormous gain (BTC traded from ~$0.06 in Jul 2010 to ~$0.30) | n/a | n/a | No bear (pre-market era) | +12.8% |
| 2014 | about **−58%** (≈$770 → ≈$320) [S] | 30 Nov / 4 Dec 2013 (≈$1,150) | **14 Jan 2015** (≈$170 close) | **No** (2 weeks after); retest Aug 2015 | +11.4% |
| 2018 | **−73.4%** [V] | 17 Dec 2017 (≈$19.6k) | **15 Dec 2018** (≈$3.2k) | **Yes** | −6.2% |
| 2022 | **−64.3%** [V] | 10 Nov 2021 (≈$69k) | **21 Nov 2022** (≈$15.5k) | **Yes** | −19.4% |
| 2026 | **−11.1% YTD** (to 29 Oct) [V] | **5–6 Oct 2025** ($124.7k close; ~$126k intraday) | So far **30 Jun 2026** ($58.6k close, −53%) | TBD | +13.1% YTD |

**Verdict [I].**
1. **Descriptively true:** 2014, 2018 and 2022 were BTC bear years, and two of three cycle lows fell inside the midterm year (the third two weeks after).
2. **Not independent of the halving cycle.** Halvings (Nov 2012, Jul 2016, May 2020, Apr 2024) lead to cycle peaks 12–18 months later (Q4 of the pre-midterm year) and bear years in the midterm. The political calendar and the halving calendar are *both* four-year cycles in phase. With three observations one cannot attribute the effect to politics. Cowen himself uses both clocks together [S].
3. **The S&P was not always weak in those years.** It was +11.4% in 2014 and +13% so far in 2026. The midterm effect on equities is mild on average, and BTC's midterm-year pain has been far larger than the equity midterm effect would imply. That suggests the halving cycle and crypto-internal leverage cycles matter more.
4. **2026 is fitting the pattern on price** (bear year, −53% drawdown) **but not yet on timing.** Cowen's base case is an October 2026 (Q4) low. He set a $60k level and had a 65% probability (September) that the cycle low still lay ahead. On 26 Oct 2026 he published a nine-step "bearish Q4 roadmap" and said he would follow it until BTC reclaimed and held $83k. The roadmap expects the Fed not to hike on 28 Oct (correct, it held), a hot PCE, oil about $120, the 10Y back to about 5.3%, falling stocks, BTC sliding in Q4, and then long yields falling by year-end [S Yahoo/BeInCrypto 26 Oct 2026 https://finance.yahoo.com/markets/crypto/articles/bitcoin-falls-below-80-000-032051576.html; 24/7 Wall St 6 Oct 2026].
5. Critics note that a three-cycle sample is a "narrow and potentially unreliable basis". 24/7 Wall St also points out that the actual 2026 low so far (30 Jun) came about three months *before* Cowen's October window [S].

### 5.6 How the equity cycle and the BTC halving cycle interact [I]

- **Pre-midterm (Y1) year:** BTC peaks (Q4: 2013, 2017, 2021, 2025). Equities are usually fine.
- **Midterm (Y2) year:** BTC bear market. The S&P has a weak first three quarters (2014, 2018 and 2026 shallow; 2022 deep). Both tend to bottom in Q3–Q4 (2018 Dec for both; 2022 Oct S&P / Nov BTC).
- **Pre-election (Y3) year:** the strongest S&P year. BTC recovers (2015, 2019 +94%, 2023 +156%).
- **Election (Y4) year:** halving year; BTC rallies into and after the election (2016, 2020, 2024).
- The alignment is striking, but it is **four data points for crypto**. The mechanisms (miner supply shock, political uncertainty) are different and only loosely related.

---

## 6. How it fits together: lead/lag sequences

### 6.1 Classic late-cycle → recession sequence (demand-driven; e.g. 1989–91, 2000–01, 2006–09) [I/S]

1. The Fed tightens. The yield curve inverts (10Y–3M), 6–18 months before the recession.
2. Housing turns down: permits and starts fall 4–6 quarters ahead (Leamer). The LEI falls. ISM New Orders drop below 50.
3. Liquidity tightens: M2 growth slows, the dollar firms, credit spreads start to widen.
4. Earnings expectations peak. Equities peak, on average about 5 months before the recession start. Breadth narrows first.
5. Initial claims rise. Unemployment turns up (the Sahm rule). **The Fed starts cutting.**
6. The curve **bull-steepens** (front-end yields fall fastest). The curve un-inverts as the recession begins.
7. Recession (NBER dated later). Equities fall 30–50%. The dollar often spikes (2008, Mar 2020), gold dips then rallies, and BTC sells off with risk.
8. Policy response: rate cuts, QE, fiscal measures. Net liquidity turns up, and a weaker dollar follows.
9. Equities bottom 3–6 months before the recession ends. ISM bottoms. Cyclicals and small caps lead.
10. Liquidity and ISM upswing → BTC → alts (2009–10 for equities; 2016–17 and 2020–21 for crypto).

### 6.2 Supply-shock / stagflation variant (1973–74, 1979–80, 1990, 2008 H1, and partly 2022 and 2026)

1. An oil or commodity shock sends headline inflation and inflation expectations up, and sentiment collapses (Michigan record lows: Jun 2022 and May 2026).
2. Central banks hike or delay cuts into the shock (Fed Sep 2026, ECB Jul 2008). Long yields rise (10Y 4.1% → 5.3% in 2026).
3. Initially growth holds, and *nominal* data (retail sales, earnings, especially energy) look strong. Surveys show high prices paid (ISM Prices about 78).
4. Real incomes erode. Housing weakens under higher mortgage rates (7.24%).
5. Whether this ends in recession depends on how long the shock lasts and on the policy response. 1973, 1980 and 1990 did; 2022 did not (no NBER recession). 2026 is undetermined.
6. Asset pattern during the shock: high-beta crypto underperforms. Equities are held up by earnings (energy, AI). Gold suffers when real yields rise faster than fear. The dollar is mixed: a haven bid offset by Fed credibility questions.

### 6.3 Liquidity regime map for crypto [I, from the evidence above]

| Regime | Net liquidity | Dollar | Real yields | Typical BTC | Typical alts | Examples |
|---|---|---|---|---|---|---|
| Reflation | ↑ | ↓ | ↓ | Strong up | Outperform late (alt season) | 2016–17, 2020–21 |
| Tightening | ↓ | ↑ | ↑ | Bear | Underperform badly | 2018, 2022 |
| Stealth easing / flow-driven | → | → | → / ↑ | Up (ETF, halving) | Underperform (BTC.D ↑) | 2023–24 |
| Late-cycle / supply shock | → / ↓ | → | ↑ | Bear, beta to S&P downside | Underperform | 2019 (partly), 2025–26 |

---

## 7. Current state dashboard (late October 2026)

| Indicator | Latest | Trend / reading | Source |
|---|---|---|---|
| Real GDP | +3.4% SAAR (Q3 2026 adv.) | Accelerating (Q2 2.2%) | [V] BEA/FRED `A191RL1Q225SBEA` |
| NBER recession | No (USREC = 0, Sep 2026) | — | [V] FRED |
| GDPNow | Q4 not yet published at time of search | Q3 nowcast ran 3.7–4.6% | [S] |
| ISM Manufacturing | 54.5 (Sep); New Orders 55.3; Prices 77.9 | 9 months > 50; inflationary | [V] ISM |
| ISM Services | 54.9 (Sep); Prices 74.0 (highest since Jul 2022) | Expanding, price pressure | [V/S] ISM |
| S&P Global flash PMI | Composite 57.6, Mfg 56.0 (53-mo high), Svcs 57.9 (Oct) | "Booming" | [S] |
| Conference Board LEI | 99.6, flat (Sep) | No recession signal | [S] |
| Michigan sentiment | 48.0 final Oct; record low 44.8 (May 2026) | Depressed by inflation | [V] FRED / [S] |
| Retail sales | +0.8% m/m headline, control +0.1% (Sep); +6.3% YoY nominal | Gasoline-inflated | [V/S] |
| Industrial production | +2.2% YoY (Sep) | Firming | [V] FRED |
| Housing starts / permits | 1,221k (−7.4% YoY) / 1,398k (−3.2%) | Weakening | [V] FRED |
| 30Y mortgage | 7.24% (29 Oct) | Up ~1 pp since Nov 2025 | [V] FRED |
| Case-Shiller national | +2.1% YoY (Aug) | Flat-ish | [V] FRED |
| Existing home sales | 3.99M SAAR; median $417.5k | Low volume, inventory up | [S] NAR |
| S&P 500 EPS (Q3) | +29.5% YoY blended; CY26 +33% | Boom | [V] FactSet |
| Household delinquency | 4.73% of debt delinquent (Q2) | Stable-high; mortgages rising | [V] NY Fed |
| Corporate bankruptcies | H1 2026 = 372, highest H1 since 2010 | Elevated | [S] S&P GMI |
| HY credit spread | 3.14% (28 Oct) | Tight, edging up | [V] FRED |
| CPI / core PCE | 3.7% / 3.1% YoY (Sep) | Re-accelerating | [V] FRED |
| Unemployment / payrolls | 4.2% / +0.3% YoY | Low hiring, low firing | [V] FRED |
| Fed funds | 3.75–4.00% (hiked 16 Sep; held 28 Oct, 2 hawkish dissents); Dec hike ~83% priced | Tightening | [V] FRED `DFEDTARU` / [S] |
| 10Y yield / curve | 5.05% (2026 high 5.31% on 5 Oct); 10Y–2Y +0.37, 10Y–3M +0.80 | Bear-steepened | [V] FRED |
| US M2 | $23.41T, +5.7% YoY (Sep) | Growing | [V] FRED |
| Global M2 (USD) | ~$103–104T record (Aug) | Up; BTC not following | [S] |
| Fed balance sheet | $6.746T (low $6.536T, 3 Dec 2025) | Slightly up; RMPs paused/slow | [V] FRED |
| TGA | $1.000T | Highest since 2021 → drain | [V] FRED |
| ON RRP | ~$0 | Buffer exhausted | [V] FRED |
| Net liquidity | $5.75T (range $5.60–5.99T in 2025–26) | Flat-to-down | [V] computed |
| Reserves | $2.89T | Near "ample/scarce" border | [V] FRED |
| SOFR | 3.94% (upper bound 4.00%) | Firm vs range | [V] FRED |
| DXY / broad dollar | ~101.7 / 121.3 | Range-bound | [S] / [V] |
| USDJPY / BOJ | 156.9 / 1.25% | Yen weak despite hikes | [V] FRED / [S] |
| S&P 500 / NDX / RUT | 7,744 (ATH 7,819 on 6 Oct) / 29,403 / record ~3,068 in Aug | Near highs; record concentration | [V] FRED / [S] |
| RSP/SPY | Record low 0.2710 (7 Oct) | Narrow | [S] |
| VIX | 16.9 | Calm | [V] FRED |
| Shiller CAPE / fwd P/E / Buffett | ~40.7 / 18.7 / 234–301% | Extreme vs fair-on-forward | [S] / [V] FactSet |
| Gold / silver / G-S ratio | ~$4,024 / ~$52 / ~77 | −28% from Jan futures peak | [S] |
| WTI / Brent | $103.37 / $123.10 (27 Oct) | War premium | [V] FRED |
| BTC / ETH | ~$78k / ~$2,250 (29 Oct) | −37% from ATH; bear | [V] FRED |
| BTC dominance / Alt index | ~60% / ~53 | No alt season | [S] |
| BTC–SPX 90d corr | 0.38 | Positive, asymmetric | [V] computed |
| BTC–gold 90d corr | ~0.5–0.86 (early Sep) | Unusually high | [S] |
| BTC ETF flows | Sep +$2.6B, Oct mixed (IBIT +$665M on 19 Oct) | Choppy | [S] |
| Midterm cycle | Elections 3 Nov; S&P midterm drawdown only −9% | Atypically mild | [V/S] |

**Synthesis [I].** Activity indicators are *strong*: GDP, PMIs, earnings. Price indicators are *hot*: ISM prices, CPI, oil. Policy is *tightening*: Fed hikes, 5% yields, a $1T TGA, an empty RRP. Sentiment is *depressed*. That is a late-cycle, supply-shock configuration. Historically it is hostile to high-beta, liquidity-sensitive assets (BTC, alts) well before it shows up in GDP. Equities are being carried by an extraordinary earnings cycle and record concentration.

Things that would change the picture:
- a break in oil (a ceasefire or the Strait reopening)
- a Fed pivot back to cuts as unemployment rises (the classic sequence in §6.1)
- renewed balance-sheet growth (RMPs resuming)
- a dollar breakdown

The downside risk is the opposite: a December hike, a 10Y above 5.3%, and a funding-market accident with reserves below $2.9T.

---

## 8. Practical investor takeaways (educational)

1. **Separate "activity" from "liquidity".** Crypto has responded more to liquidity, the dollar and real yields than to activity gauges like ISM or GDP. 2026 shows strong activity can coexist with a crypto bear market.
2. **Prefer rates of change and regimes to point forecasts.** M2 YoY, net-liquidity trend, ISM direction and the dollar trend tilt the odds over months. Fixed-lag overlays (10–12 weeks) are fragile.
3. **Check every popular chart for a hidden third variable.** Global M2 in USD is partly an inverted dollar. ISM upswings in 2017 and 2021 coincided with global easing. Midterm years coincide with halving-cycle bear years.
4. **Recessions decide the depth of equity bear markets** (≈ −36% with a recession vs ≈ −20–25% without). Crypto's −75–85% bears have not needed recessions.
5. **Seasonality is a weak prior**, useful for context and dangerous as a rule.

---

## Sources

**Primary data (FRED, downloaded 30 Oct 2026; base URL `https://fred.stlouisfed.org/series/<ID>`)**
WALCL, WTREGEN, RRPONTSYD, WRESBAL, SOFR, DFEDTARU, M2SL, GDPC1, A191RL1Q225SBEA, USREC, INDPRO, RSAFS, HOUST, PERMIT, MORTGAGE30US, CSUSHPINSA, UMCSENT, TOTALSL, DRCCLACBS, CPIAUCSL, PCEPILFE, UNRATE, PAYEMS, ICSA, DGS10, T10Y2Y, T10Y3M, BAMLH0A0HYM2, DTWEXBGS, DEXJPUS, DEXUSEU, DCOILWTICO, DCOILBRENTEU, WTISPLC, VIXCLS, SP500, NASDAQ100, CBBTCUSD, CBETHUSD, USSLIND (discontinued 2020), MYAGM2CNM189N (stale).

**Official / primary publications**
- BEA, GDP Advance Estimate Q3 2026: https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026 ; PDF https://www.bea.gov/sites/default/files/2026-10/gdp3q26-adv.pdf
- ISM Manufacturing PMI Sep 2026 (PR Newswire): https://www.prnewswire.com/news-releases/manufacturing-pmi-at-54-5-september-2026-ism-manufacturing-pmi-report-302894520.html ; ISM: https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/september/
- ISM Services Sep 2026 (First Trust summary): https://www.ftportfolios.com/Commentary/EconomicResearch/2026/10/5/the-ism-non-manufacturing-index-declined-to-54.9-in-september
- ISM Jan 2026 (First Trust): https://www.ftportfolios.com/Commentary/EconomicResearch/2026/2/2/the-ism-manufacturing-index-rose-to-52.6-in-january
- ISM Mar 2021 64.7 (First Trust): https://ftportfolios.com/Commentary/EconomicResearch/2021/4/1/the-ism-manufacturing-index-rose-to-64.7-in-march
- Conference Board LEI press/technical notes Oct 2026: https://www.conference-board.org/pdf_free/press/US LEI PRESS RELEASE- October 2026.pdf
- FOMC press conference 28 Oct 2026: https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20261028.pdf
- Fed Monetary Policy Report Jul 2026: https://www.federalreserve.gov/monetarypolicy/2026-07-mpr-part2.htm
- NY Fed Household Debt and Credit Q2 2026: https://www.newyorkfed.org/newsevents/news/research/2026/20260811
- NAR existing-home sales Sep 2026: https://www.nar.realtor/newsroom/existing-home-sales-increased-1-5-in-september-according-to-nar-report
- FactSet Earnings Insight 23 Oct 2026: https://insight.factset.com/sp-500-earnings-season-update-october-23-2026 ; PDF https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_102326.pdf
- BIS Bulletin 90 (Aug 2024 market turmoil): https://www.bis.org/publ/bisbull90.pdf
- EIA Today in Energy (Q3 2026 crude): https://www.eia.gov/todayinenergy/detail.php?id=68245
- NBER Reporter, Hamilton "Oil Price Shocks" (2011): https://www.nber.org/reporter/2011number2/oil-price-shocks

**News / secondary**
- CNBC Fed hike 16 Sep 2026: https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
- Fed 28 Oct 2026 hold: https://www.cnn.com/2026/10/28/business/live-news/federal-reserve-interest-rate-october ; https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-october-28-2026
- Al Jazeera, Fed hike and Iran war: https://www.aljazeera.com/economy/2026/9/16/us-fed-raises-interest-rates-as-inflation-weighs-on-economy
- CNBC oil and Iran-war timeline: https://www.cnbc.com/2026/04/21/oil-price-iran-war-middle-east.html ; Al Jazeera 28 Sep 2026: https://www.aljazeera.com/economy/2026/9/28/oil-prices-surge-after-trump-rejects-irans-plan-to-reopen-strait-of-hormuz
- BOJ Sep 2026 hike: https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html ; Jun 2026: https://www.cnbc.com/2026/06/16/boj-rate-hike-historic-inflation.html
- First Trust, "Can Warsh shrink the Fed's balance sheet?": https://www.ftportfolios.com/Commentary/EconomicResearch/2026/8/13/can-warsh-shrink-the-feds-balance-sheet
- SVB, Fed ends QT: https://www.svb.com/market-insights/market-analysis/the-federal-reserve-ends-qt-key-market-liquidity-insights/
- Wolf Street, SRF usage Oct 2025: https://wolfstreet.com/2025/10/20/repo-market-brushfires-doused-by-banks-use-of-the-feds-standing-repo-facility-srf/
- Reuters/Kitco, record SRF Sep 2025: https://www.kitco.com/news/off-the-wire/2025-09-15/us-banks-borrow-record-185-billion-feds-repo-facility-sign-funding
- Dollar worst H1 since 1973: https://finance.yahoo.com/news/dollar-posted-worst-first-half-153518559.html
- Motley Fool, M2 contraction: https://www.fool.com/investing/2024/02/25/us-money-supply-is-shrinking-the-most-since-the-gr
- S&P Global, US bankruptcies 2026: https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/3/us-corporate-bankruptcies-set-to-climb-again-in-2026-99159008
- Shiller CAPE trackers: https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio ; https://www.thetrading.tools/shiller-cape
- Buffett indicator: https://www.gurufocus.com/stock-market-valuations.php ; https://fool.com/investing/2026/10/29/3-indiciations-a-market-crash-could-be-coming-soon
- RSP/SPY record low: https://www.openingbelldailynews.com/p/equal-weight-sp-500-rsp-spy-ratio-record-low-chart
- Russell 2000 record Aug 2026: https://www.regardsofwallstreet.com/news/russell-2000-record-high-small-caps-beating-nasdaq-100
- Copper/gold vs 10Y breakdown: https://eco3min.fr/en/copper-gold-ratio-treasury-yields-macro-signal/ ; https://ahasignals.com/copper-gold-ratio-tracker/
- Gold/silver Jan 2026 records (Barchart): https://www.barchart.com/story/news/37362048/commodity-roundup-januarys-top-performers-and-underperformers
- Gold/DXY late Oct 2026: https://tradingeconomics.com/commodity/gold ; https://tradingeconomics.com/dxy:cur
- BTC–gold correlation (The Block): https://www.theblock.co/news/markets/2026-09-03-bitcoin-gold-correlation-hits-six-year-high-but-analysts-question-whether-equity-decoupling-will-last-413437
- BTC ETF flows: https://www.tftc.io/bitcoin-etf-flows ; https://www.theblock.co/news/markets/2026-10-20-blackrock-ibit-bitcoin-etf-665-million-421102
- BTC dominance Oct 2026: https://blockchainreporter.net/bitcoin-dominance/ ; https://coinstats.app/news/08a3068a50b3820e3354f9c3b9206cde8c9e79c031c206b68d36670bbdecca8d_Bitcoin-Dominance-Today-What-It-Is-and-How-to-Read-It/
- Global M2 record vs BTC: https://cryptorank.io/news/feed/44e74-global-money-supply-record-bitcoin-lags
- S&P Global flash PMI Oct 2026: https://investinglive.com/news/us-s-p-global-flash-october-services-pmi-57-9-vs-58-0-expected/
- Retail sales Sep 2026: https://www.advisorperspectives.com/dshort/updates/2026/10/15/september-retail-sales-better-than-expectations
- Midterm statistics: https://plaineconomy.com/stock-market-after-midterm-elections/ ; https://www.ftportfolios.com/Commentary/Insights/2024/4/8/midterm-election-client-resource-kit---march-2024 ; https://certuity.com/insights/midterm-elections-and-the-stock-market/ ; https://www.dreyerwealth.com/blog/midterm-elections-and-the-stock-market-what-history-shows-since-1950 ; https://www.inc.com/phil-rosen/stock-market-midterms-sp-500-index-investors/91414640
- September seasonality: https://stocktradersalmanac.com/Alert/20240815_1.aspx ; https://www.fool.com/research/september-effect-statistics
- Recessions and the S&P: https://www.fool.com/investing/2022/07/30/how-does-stock-market-perform-during-recession/ ; https://www.ftportfolios.com/Commentary/MarketCommentary/2025/2/20/recessions-and-the-sp-500-index ; https://www.kathmere.com/wp-content/uploads/2022/06/August-2022-Recessions-and-the-Stock-Market.pdf

**Benjamin Cowen and Raoul Pal (attributions)**
- Cowen X, "What if #Bitcoin leads liquidity…" (May 2025): https://x.com/benjamincowen/status/1920560445712159145
- Cowen X, "Liquidity conditions also reflect a late business cycle environment" (Mar 2026): https://x.com/benjamincowen/status/2036990935075016905
- Cowen X, four-year-cycle lows and SPX October bottoms (2026): https://x.com/benjamincowen/status/2101053560720863561 (text via search snippet; page paywalled to fetch)
- Cowen, "why altcoin season never came" (18 Apr 2026): https://cryptoadventure.com/benjamin-cowen-reveals-why-the-altcoin-season-never-came/ ; https://beincrypto.com/benjamin-cowen-altcoin-season-analysis/
- Cowen, "Bitcoin is not the economy" (Feb 2026, ISM): https://www.tradingview.com/news/cointelegraph:a453199ce094b:0-ism-manufacturing-pmi-at-highest-since-2022-as-analysts-debate-bitcoin-impact/
- Cowen, M2 vs global net liquidity (Sep 2026): https://finance.yahoo.com/markets/crypto/articles/remember-bitcoin-supposed-rise-money-170010779.html
- Cowen, 9-step Q4 2026 roadmap (26 Oct 2026): https://finance.yahoo.com/markets/crypto/articles/bitcoin-falls-below-80-000-032051576.html
- Cowen, Oct 2026 bottom thesis: https://coinmarketcap.com/academy/article/%20bitcoin-4-year-cycle-october-2026 ; https://beincrypto.com/ben-cowen-bitcoin-bear-market-53k/ ; https://247wallst.com/investing/cryptocurrency/2026/10/06/benjamin-cowen-said-the-cycle-would-bottom-bitcoin-near-60000-in-october-did-benjamin-cowen-predict-the-bitcoin-bottom-correctly/
- Cowen, BTC dominance until QT ends: https://www.benzinga.com/markets/cryptocurrency/24/11/41850110/federal-reserve-cuts-interest-ratesbitcoin-dominance-may-rise-as-a-result
- Cowen, DXY 2022: https://cointelegraph.com/news/bitcoin-rejects-40k-as-us-dollar-strength-hits-20-year-high ; https://theinformerpost.beehiiv.com/p/bitcoin-bulls-shouldnt-be-fooled-by-weakening-us-dollar-according-to-crypto-analyst-benjamin-cowen
- Raoul Pal, ISM/business cycle: https://benzinga.com/markets/cryptocurrency/23/11/35986621/raoul-pals-insights-on-business-cycle-impact-on-asset-classes-including-blue-chip-cryptos- ; https://www.tradingview.com/news/newsbtc:13a8574a9094b:0-raoul-pal-bitcoin-bull-market-could-extend-to-2026-here-s-why/

**Not verified / open items.** I did not find a Q4 2026 GDPNow figure, the October 2026 ISM (due 2 Nov), the October Michigan inflation expectations, 2026 PBOC headline rate cuts, a precise global net liquidity series matching Cowen's $25T, or a primary-source midterm-year return table. The midterm mean of about +4.6% is my reconstruction; verify it against S&P annual data before publishing.
