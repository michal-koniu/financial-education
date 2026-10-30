# A — Complete inventory of what Benjamin Cowen uses (indicators, charts, theses, calls, vocabulary)

Research file for the course "practical-macro-economy". Compiled 2026-10-30.
Claim tags: **[V]** verified from a primary or reputable source (URL in text or Sources), **[S]** secondary or snippet (news write-up, AI summary of a video, search-engine snippet), **[I]** my inference.

---

## 0. Method and source quality (read this first)

Four bodies of evidence were used. They have different reliability, and the course writers should keep the difference.

1. **The Into The Cryptoverse (ITC) web app chart catalogue [V].** The public JavaScript bundle of `app.intothecryptoverse.com` (fetched 2026-10-30, no login) contains the catalogue of every published chart: slug, title, category, sub-category, "universe" (crypto / macro / tradfi) and minimum subscription tier, plus long help texts that describe the dashboards (Crypto Indicator Risk Dashboard, Macro Recession Risk Dashboard, Macro Liquidity Risk Dashboard, etc.). 380 chart entries were extracted. The full grouped list is saved next to this file as `A-itc-chart-catalogue.txt`. This is the most complete answer to "what charts does he have", but having a chart on the platform does not mean he talks about it often. Section 1b covers this.
2. **The complete video list, 2019 to 11 June 2026 [S].** rosetta.to indexes the channel @intothecryptoverse/@benjaminjcowen. It lists **2,385 videos** with title, date, view count and an AI-written summary of each. Saved as `A-cowen-videos-2019-2026.json`. The titles and dates are reliable. The summaries are machine-written: mostly accurate, but they contain occasional errors (for example, one says "Biden administration" in a January 2026 video, and one says "Q4 2025" where 2026 was meant). I used the summaries for frequency counts (section 1c) and to locate claims, and cite them as [S]. Videos from 12 June to 30 October 2026 come from the channel's own YouTube RSS feed (last 15 uploads, [V] for titles and dates) and from news coverage.
3. **Cowen's own written memos at benjamincowen.com/reports [V].** Eleven reports: two from 2020 and nine from January to September 2026 (monthly or quarterly "Crypto/Macro Risk Memo"). The web pages give the thesis and, in the newer ones, many numbers. The full PDFs sit behind an e-mail form and were not accessed.
4. **Interviews and news write-ups [S].** These include the Bankless podcast of 23 Dec 2025 (full transcript on the page, close to primary), Cointelegraph Magazine, Benzinga, BeInCrypto (via Yahoo mirrors), CoinMarketCap Academy, 24/7 Wall St., and The Informer Post. X/Twitter posts could not be opened directly (HTTP 402). Post text was taken from search snippets, and post dates were decoded from the post IDs.

Not used: anything behind a login, the ITC premium area, paid PDFs, and YouTube transcripts. YouTube's search page sits behind a cookie-consent gate, and I did not get around it.

Identity notes [V/S]: YouTube channel "Benjamin Cowen" (handle @benjaminjcowen). The channel passed 1 million subscribers on 9 Jun 2026, per the video "Bitcoin: The Beauty of Mathematics (Part 71) – 1 Million Subscriber Milestone!". Current video descriptions link X as `twitter.com/benjamincowen`, so the brief's @intocryptoverse appears to be the older handle; Telegram is still `t.me/intocryptoverse`. Other properties: ITC site/app, ITC newsletter (newsletter.intothecryptoverse.com), a free monthly newsletter and memo series at benjamincowen.com, a "Cowen AI Chatbot" (cowenai.com, linked from the app menu), and the first ITC Conference ("Investing Through The Cycles", Miami, 20–22 Nov 2026). Background, per Cointelegraph Magazine of 19 Nov 2024 [S]: PhD on molecular-dynamics simulations of radiation damage in ceramics, then a national-laboratory job. He started the channel in 2019, says "Sometimes I am wrong, sometimes right", and calls himself a "BTC bull with 2 panda bears".

---

## 1. Master table — every indicator / chart / concept he uses

How to read "Frequency": **frequent** means it appears in more than about 100 video titles or summaries 2019–2026, or is a recurring named series. **Occasional** means about 15–100. **Rare** means fewer than 15. Section 1c gives the counts behind these labels. The "Evidence" column cites video titles with dates (rosetta [S] for title and summary) or memos and articles. "Platform" means the chart exists in the ITC catalogue [V].

### 1.1 Fed & interest rates

| Indicator / chart | Category | How he uses it (typical claim) | Evidence | Freq. |
|---|---|---|---|---|
| Fed funds target range / effective rate; FOMC decisions (he posts "Pre-FOMC" and "Post-FOMC" videos) | Fed & rates | Monetary policy, not news, drives risk appetite. BTC has historically bottomed near the Fed's *terminal* rate. "The real bull market often begins after the **last** rate cut, not the first." | "Bitcoin and Interest Rates" 24 Jan 2023 [S]; "Bitcoin Pre-FOMC" 9 Dec 2025; "Bitcoin: Post-FOMC" 29 Oct 2026 (RSS) [V]; platform: Federal Funds Target Range, Effective Federal Funds Rate | frequent (~270 summaries mention Fed/FOMC) |
| Rate cuts / "the pivot" | Fed & rates | The first cut is not the most bullish event, because risk assets often top around the start of cuts (2000, 2007, 2019). The Fed pivots when something breaks. In 2024 he argued that without a recession, yields and the dollar rise after the first cut. | "The Rate Cutting Cycle Has Begun" 19 Sep 2024; "The Yield Curve & Bitcoin" 23 Oct 2024 [S]; The Informer Post, "Fed rate cuts may not be bullish…" [S] | frequent (142) |
| Rate hikes | Fed & rates | 2022: hikes push investors from risk-on to risk-off. Feb 2022: "a hike is not necessarily doom and gloom" (Daily Hodl) [S]. Sep 2026: argued the Fed "really should" hike and that a hike would lift the dollar and sink BTC. After BTC rallied he admitted the thesis "was not rooted in the data": "None of the data suggests that a rate hike has ever been immediately bearish for Bitcoin" (looked at Dec 2015, Mar 2022, Sep 2018, Sep 2022). | Benzinga 9/2026 via TradingView mirror [S]; CMC Academy (March-1997 one-and-done hike analogy) [S] | occasional (56) |
| Market-implied path (CME FedWatch, Polymarket odds) | Fed & rates | Reads what is priced. A hot print that "prices out cuts" hurts altcoins most. | "Unemployment Rate Drops to 4.1%" 3 Jul 2025 [S]; "The Market Doesn't Seem To Think There Will Be A Rate Hike In October" 22 Oct 2026 (RSS) [V] | occasional |
| SEP / dot plot / FOMC minutes | Fed & rates | Checks whether the Fed projects recession or hikes. | "Fed Projecting a Mild Recession" 13 Apr 2023 [S]; "Powell Steps Down…" 15 May 2026 [S] | occasional |
| Fed funds rate vs 2-year Treasury yield (how restrictive policy is; "neutral") | Fed & rates / bonds | "ETH performs best when the Fed funds rate is near or below the 2-year." In Dec 2025 FFR was 3.75% vs 2Y 3.5%, "one more cut to neutral". In Feb 2026 he wrote the policy rate was "above market-implied neutral". | Bankless 23 Dec 2025 [S]; Macro Risk Memo Feb 2026 [V] | occasional |
| QT / QE, Fed total assets, QT taper and QT end | Fed & rates / liquidity | Central thesis. BTC dominance rises and alts bleed during QT. "Last cycle the transition from QT to QE marked the top for BTC dominance." BTC topped about 2 months before QT ended, both in 2019 and in 2025. The end of QT is not the same as a growing balance sheet. | "The Fed Slows Quantitative Tightening" 19 Mar 2025; "The Fed Announces QT Will End in December" 30 Oct 2025; "Bitcoin and the End of Quantitative Tightening" 1 Dec 2025 [S]; Cointelegraph Mag 19 Nov 2024 [S]; Bankless [S]; platform: FED Total Assets; "QT Ending Bear Markets" chart | frequent (111) |
| Fed chair, independence and politics (DOJ probe of Powell, Powell's exit, Warsh) | Fed & rates | Institutional risk raises uncertainty. A new chair "cannot cut unilaterally". | "A Line Has Been Crossed" 12 Jan 2026; "FOMC: The End of an Era" 29 Apr 2026; "Jerome Powell: 'I Won't See You Next Time'" 1 May 2026; "Powell Steps Down…" 15 May 2026 [S] | occasional (2026) |
| Other central banks (BoC ending QT, BoJ hikes and the yen, GDP-weighted global policy rate) | Fed & rates / liquidity | BoJ hikes are a risk for BTC (Jun 2026). The global policy rate "has stopped falling". | "Bank of Canada to End Quantitative Tightening" 29 Jan 2025; "Bitcoin Falls to the 200W Moving Average" 5 Jun 2026 [S]; Balance of Risks memo Aug 2026 [V] | rare (≈10) |
| Real interest rates / real yields | Fed & rates / bonds | Real yields are "elevated versus prior expansions". The Fed's hawkish turn "keeps real rates elevated". It is a supporting argument and almost never a video topic. | Feb 2026 and July 2026 memos [V]; platform: Real Interest Rates / Spreads / Curve | rare |

### 1.2 Bonds & yield curve

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| 10-year Treasury yield (US10Y) | bonds | BTC "generally rises when the 10Y declines". Local *bottoms* in yields mark BTC uptrends more reliably than yield peaks. In Jan 2025, "good news is bad news": strong jobs → higher long yields → BTC down. In 2026 the 10Y returning to 5.3% is a step in his bearish Q4 roadmap. A peak in long yields sometimes precedes growth or financial stress (2000, 2007, 2011). | "Bitcoin Vs. 10 Year Treasury Yields" 4 Jan 2022; "Bitcoin Responds to the Labor Market" 11 Jan 2025 [S]; Triple Squeeze memo 30 Sep 2026 [V]; X post 26 Oct 2026 [S] | occasional (86 incl. curve) |
| Yield curve: 10Y–2Y and 10Y–3M; inversion → recession, with the recession usually coming at or after **un-inversion** | bonds | The curve inverts long before a recession. The recession typically comes "upon the uninversion rather than during the inversion". The market can keep rallying for more than a year after inversion. | "Recessions and The Yield Curve" 17 Sep 2022; "The Yield Curve & Recessions" 20 Oct 2022 and 6 Oct 2023; "Bitcoin and the Yield Curve" 14 May 2023; "S&P 500 ROI After Yield Curve Inversion" 21 Jun 2023; "A Line Has Been Crossed" 12 Jan 2026 [S]; Coin Edition (3M–10Y) [S]; platform: Treasury Yield Spreads/Curve, Days After Inversion, Days After Uninversion, ROI (to Low) After Yield Curve Inversion | occasional |
| Bull steepener vs bear steepener | bonds | 2023 was a *bear* steepener (long end up). He wrote that re-steepening "has historically coincided with rising recession probability more often than with growth acceleration". Sep 2026: "steepening from the long end" (term premium, fiscal supply). | "The Yield Curve & Recessions" 6 Oct 2023 [S]; Feb 2026 memo [V]; Sep 2026 memo [V] | occasional |
| 30-year yield, term premium, fiscal supply | bonds | 2026 rate shock: 10Y ~5.29% (highest since 2007), 30Y ~5.64% (highest since 2002). The sequence to watch: gold bottoms, then the long end tops, then stress. | Triple Squeeze memo [V] | rare (2026) |
| Credit spreads (ICE BofA OAS) | bonds | On the platform as a card on the Recession Risk Dashboard, deliberately left out of the summary score. I found **no** video built around credit spreads. | platform help text [V]; 0 hits in video summaries [S] | rare |

### 1.3 Inflation

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| CPI headline and core (monthly videos titled "Inflation Rises/Drops to X%") | inflation | A hot CPI means fewer or later cuts, higher yields and a stronger dollar, which is worst for altcoins. In 2026 he called the inflation "mostly supply-driven" (energy, geopolitics) rather than demand-driven. | "Inflation Rises to 3%" 13 Feb 2025 … "Inflation Rises to 3.0%" 25 Oct 2025; "Inflation Soars to 3.3%" 10 Apr 2026; "Inflation Rises to 3.8%" 12 May 2026 [S]; platform: CPI, Core CPI, Inflation YoY per category / contributions | frequent (188) |
| PCE and core PCE | inflation | "PCE comes in hot (Oct 29)" is a step in the Oct 2026 roadmap. The Sep 2026 memo cites Aug PCE at 3.4% headline / 3.0% core. | X post 26 Oct 2026 [S]; Triple Squeeze memo [V]; platform: PCEPI, Core PCEPI | occasional |
| PPI (producer prices) | inflation | Producer prices and transport costs "leading the inflation move" in 2026. | "PPI Surges" 14 Aug 2025 [S]; Macro Risk Memo May 2026 [V]; platform PPI, PPIAC | occasional |
| 1970s inflation-waves analogy | inflation | 2022–2025: there is a risk of a second inflation wave like the 1970s, but it is not his base case (Benzinga [S]). Inflationary periods force sustained hikes and cluster recessions. 2026: an energy shock puts the Fed in a "checkmate". | "S&P 500 Bear Markets with High Inflation" 10 Oct 2022; "Smoothed Recession Probabilities" 10 Jan 2023; "Inflation & Bitcoin" 11 Dec 2024; "Bitcoin, Stocks, and Inflation" 14 Mar 2025 [S] | occasional (38) |
| Oil (WTI/Brent) and energy equities (XLE) | inflation / cross-asset | Oil spikes historically precede recessions. The *speed* of an oil move matters more than its level (WTI $67→$91 in a week in Mar 2026, "largest weekly rally since 1983"). Energy stocks top last in a cycle. Oil rolled over before the 10Y in 2018 (by ~5 weeks) and 2022 (by ~4 months). | "Oil Spikes 35%" 8 Mar 2026; "The Mechanism That Ends Business Cycles" 28 Feb 2026; "FOMC: The End of an Era" 29 Apr 2026 [S]; Sep 2026 memo [V]; platform: Crude Oil (WTI) | occasional (2026-heavy) |
| Tariffs | inflation / growth | 2025: tariffs as an inflation risk that could delay cuts. He covered the S&P's 20% drop and the 90-day pause. | "S&P 500: What Is Happening?" 3 Apr 2025; "Trump 90-Day Tariff Pause" 10 Apr 2025 [S] | occasional (2025) |

### 1.4 Labor market

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| Unemployment rate U-3 (monthly "Unemployment Rate Rises/Drops to X%") | labor | His most important macro variable since 2023. Unemployment bottoms before recessions and then rises *non-linearly*. Recessions start once that uptrend begins. Equity and crypto bottoms come *during* recessions, and unemployment peaks *after* the market bottom (it lags). The Q4 2025 BTC top was driven by rising unemployment (4.6%), unlike the inflation-driven 2021 top. The long-term crypto bull case needs unemployment to fall again, as in 2009–2020. | "Unemployment, Recessions, and Stock Market Bottoms" 29 Sep 2022; "When Will The Stock Market Bottom?" 14 Jun 2022; "The Unemployment Rate Rises to 4.6%" 17 Dec 2025; "Bitcoin in a Late Business Cycle Environment" 27 Mar 2026 [S]; Bankless [S]; platform: Unemployment Rate, Unemployment Level by Reason, Alternative Measures (U-1…U-6), Duration | frequent (159) |
| Sahm rule (3-month average unemployment ≥ 0.5 pp above its 12-month low) | labor | A good recession signal, less useful for timing market bottoms or tops. He noted it triggered in Aug 2024, with mixed history for risk assets. | "Sahm Rule Recession Indicator" 20 Jan 2023 and 5 Nov 2023; "The Sahm Rule Recession Indicator has Signaled" 3 Aug 2024 [S]; platform: Sahm Rule, Sahm per State, number and map of states triggered | rare by count (3), but a core reference |
| Initial and continued jobless claims | labor | "Layoffs subdued". Continued claims rising is an early flag. Initial claims ≈ 209k in Aug 2026. | "Recession Risk in 2024" 1 Dec 2023 [S]; Balance of Risks memo [V]; platform: claims per state, maps, "number of states with YoY rises" | occasional |
| Nonfarm payrolls and revisions | labor | Payroll growth slowing ("employment growth collapsed to 156k annually", Mar 2026). Jul 2026: −23k with −103k revisions. YoY payroll growth ≈ 0.2%. | "Total Nonfarm Employees" 14 Jan 2023; "Bitcoin in a Late Business Cycle Environment" 27 Mar 2026 [S]; Aug 2026 memo [V] | occasional |
| JOLTS: openings, quits, layoffs, hires; openings per unemployed | labor | Softening but not collapsing. Openings per unemployed ≈ 1.0 is "normalized rather than collapsed". | "JOLTS" 3 May 2023; "The Labor Market and Bitcoin" 3 Oct 2025 [S]; Aug 2026 memo [V]; platform: Job Openings, Quits, Layoffs, Hires | occasional |
| Unemployment composition (permanent job losers, new entrants, youth 16–19) | labor | Permanent job losers rising is a late-cycle sign. Youth unemployment at 15.7% (Jan 2026) is a "secondary warning sign". | "The Labor Market (and Bitcoin)" 2 Nov 2024; "A Deeply Concerning Chart for Stocks" 20 Jan 2026 [S] | occasional |
| State-level diffusion (unemployment rising in N states, Sahm per state) | labor | "Weakness diffusing across states" while the aggregate looks stable. | Feb 2026 memo [V]; platform charts [V] | rare |
| Labor force participation / labor supply | labor | Part of the 2024 rise in unemployment came from labor-force growth. In Jul 2026, 264k people left the labor force, which "accounts for part of the unemployment drop". | "The Sahm Rule … has Signaled" 3 Aug 2024 [S]; Aug 2026 memo [V] | rare |
| KC Fed Labor Market Conditions Index, ADP, ISM services employment | labor | Supporting checks. | "Jobs Report" 6 Jan 2024; "Labor Market Holds Steady" 8 May 2026 [S]; platform: KC Fed LMCI | rare |

### 1.5 Growth & business cycle

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| **ITC Business Cycle metric**, presented as S&P 500 ÷ (unemployment rate²) × inflation × interest rate, divided by M2 | growth | His 2026 workhorse. Recessions bring "extended valuations back to baseline". Cycles are getting larger in amplitude. In 2026 we are in a "late business cycle like 2007 and 2019". His base case is a hard landing within 2–3 years (Feb 2026). | "Visualizing the Business Cycle" 22 Feb 2026; "Business Cycles Ends With Recessions" 25 Feb 2026; "The Mechanism That Ends Business Cycles" 28 Feb 2026; "Oil Spikes 35%" 8 Mar 2026; "Bitcoin in a Late Business Cycle Environment" 27 Mar 2026 [S]; platform: "ITC Business Cycles" (Pro) [V] | occasional (2026 core) |
| ISM Manufacturing PMI ("Main Street") | growth | Nov 2025: major BTC peaks line up with ISM peaks, and ISM below 50 means Main Street is struggling, hence no retail euphoria this cycle. Mar 2026: the "news cycle, ISM, oil and labor reports are irrelevant" when the price chart keeps matching the midterm-year average. Feb 2026: "Bitcoin is not the economy", since BTC rose in 2025 while the ISM stalled. The popular "ISM above 50 → alt season" thesis belongs mainly to other analysts, not to him. | "Bitcoin and Main Street" 19 Nov 2025; "Bitcoin: Simulation Confirmed" 9 Mar 2026; "Bitcoin Crash Continues" 5 Feb 2026 [S]; Cointelegraph Feb 2026 via search snippet [S]. Note: ISM is **not** in the ITC catalogue (it carries the OECD "Manufacturing Confidence Index" and the "Composite Leading Indicator" instead) [V] | rare–occasional |
| GDP, GDI, average of GDP and GDI, real GNP/GNI | growth | Real GDI shows slowdowns more clearly than nominal GDP. Negative GDP quarters in 2022 were not a recession because unemployment stayed low. | "Gross Domestic Income" 2 Jun 2023; "Smoothed Recession Probabilities" 10 Jan 2023 [S]; platform | occasional (12) |
| Smoothed recession probabilities (Chauvet–Piger, FRED RECPROUSM156N) | growth | More predictive than NBER dating. It was at 1.16% in late 2022. | "Smoothed Recession Probabilities" 10 Jan 2023 [S]; platform | rare |
| Macro Recession Risk dashboard (employment, national income, production & business, interest rates; 17 FRED series; 0–1 score) | growth | "Recession risk low for now". The composite was 0.024 in Aug 2026, "near the floor". | "Recession Risk in 2024" 1 Dec 2023 [S]; Aug 2026 memo [V]; platform help text [V] | occasional |
| Uncertainty indices (Economic Policy Uncertainty, World Uncertainty, Equity Market Volatility tracker) | growth / sentiment | Elevated uncertainty is a late-cycle feature. | "Bitcoin in a Late Business Cycle Environment" 27 Mar 2026 [S]; platform | rare |
| Soft / hard / no landing framing | growth | Defined by S&P drawdown: a soft landing ≈ −30% to the pre-pandemic high, a hard landing ≈ −50% (2022 framing). In 2024 he applied the three scenarios to BTC, with the 100-week MA as support in soft cases. | "Stocks: Hard or Soft Landing?" 28 Aug 2022; "Bitcoin: Hard Landing Vs. Soft Landing" 5 Sep 2024 [S] | occasional |
| Housing (houses for sale/sold ratio, real estate outlook, mortgage rates) | growth | 2022–23 interviews with Jordan Wirsz; "How to Fix the Real Estate Market" 8 Aug 2025. Peripheral to crypto calls. | rosetta [S]; platform (Real Estate category, 19 charts) | occasional (25) |
| Consumer sentiment (Michigan), retail sales, industrial production, capacity utilization | growth | On the platform. **Not** found as video topics (0 summary hits for consumer sentiment). | platform [V] | rare |

### 1.6 Liquidity, money & the dollar

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| M2 money supply; "accounting for the money supply" (asset ÷ M2) | liquidity | BTC/M2: the 2021 "new ATH" was not a new high after adjusting for M2. S&P/M2 has oscillated in a range for about 30 years, so much of the long-run trend is monetary. Dec 2025: S&P/M2 suggested "about one more year of upside", like 1996–2000. Mar 2026: he prefers stock-to-gold over S&P/M2. | "Bitcoin: Accounting For The Money Supply" 29 Oct 2021 and 18 Nov 2021; "S&P 500: Accounting For the Money Supply" 11 Oct 2022 and 12 Jul 2025; "Stocks Have Dropped 9%" 30 Mar 2026 [S]; Bankless [S]; platform M1, M2 | occasional |
| Net liquidity (sum of major central-bank balance sheets − TGA − ON RRP) | liquidity | Correlates with the S&P. More useful for *relative* performance (higher-risk vs lower-risk assets) than for USD prices. In late cycle and QT, alts underperform BTC. | "Net Liquidity" 30 Jun 2023; "Net Liquidity: S&P 500 and Bitcoin" 28 Jul 2023; "Bitcoin: Net Liquidity" 8 Feb 2024 [S]; platform: ON RRP, Treasury Deposits with Fed | occasional |
| Global liquidity / "global M2" | liquidity | Contrarian: "What if Bitcoin *leads* liquidity (and not lags)?" Dollar strength mechanically moves global-M2 aggregates. | 8 May 2025 [S] | rare |
| ITC Macro Liquidity Risk score (effective FFR, 2Y yield, DXY, Δ Fed assets, ΔM2; first principal component, 6-month smoothing, percentile rank since 2003) | liquidity | "Why alt season never happened": tight liquidity forces flight-to-quality rotations (alts → BTC → stocks → gold). The next alt season needs significantly looser policy, possibly 2027–2029. "Liquidity risk falls out of its tight band" is one of his invalidation signals (Aug 2026). | "Why Alt Season Never Happened" 20 Feb 2026 [S]; Aug 2026 memo [V]; platform help text [V] | occasional (2026) |
| DXY (dollar index) and the broad dollar | liquidity / dollar | A long-term parallel channel. After the first cut the dollar and long yields tend to rally unless a recession is imminent (Oct 2024; correct for Oct 2024–Jan 2025). "Altcoin season is unlikely while the dollar strengthens." The BTC–DXY inverse correlation breaks down in high inflation. 2026: DXY near 101.35, watch a break above 101.8; "a dollar breaking to new lows" would invalidate the bearish view. | "Bitcoin vs. DXY" 10 Dec 2022; "The Yield Curve & Bitcoin" 23 Oct 2024; "Is DXY Nearing A Low?" 7 Jul 2025 [S]; Sep 2026 memo [V]; platform: DXY, "BTC vs. DXY" | frequent (223 incl. "dollar") |
| Treasury General Account (TGA), reverse repo (ON RRP), bank reserves | liquidity | Mainly as inputs to net liquidity; not standalone video topics. | platform [V]; "Net Liquidity" 2023 [S] | rare |

### 1.7 Equities & cross-asset

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| S&P 500 (outlooks, bear-market comparisons, ROI in bull and bear markets) | equities | BTC "tops earlier and bottoms earlier than stocks". A serious BTC leg down "would likely need a 10–20% equity selloff". Midterm-year BTC lows came with equity corrections. A 20% S&P drop is a key line between "correction" and "recession bear" (1998 analog in Apr 2025). | "S&P 500 Bear Markets" (2022–23 series); "The S&P500 Has Dropped 20%" 8 Apr 2025; "S&P 500: Outlook for the Rest of 2026" 27 May 2026 [S]; CMC Academy (Sep 2026) [S]; platform: ROI During S&P 500 Bear/Bull Markets, S&P 500 Risk | frequent (239) |
| S&P/Gold ratio (and gold/stocks) | cross-asset | A break below about 1.4 preceded major downturns in 1973 and 2008. Gold up 46% vs stocks since 2021. The "rotation trap" is selling gold to buy lagging stocks. The S&P vs gold looks "more like the 1970s than 2000". | "A Deeply Concerning Chart for Stocks" 20 Jan 2026; "Gold and the Rotation Trap" 21 Jan 2026; "Gold Breaks out against Stocks!" 22 Jan 2026 [S]; Bankless [S] | occasional (2026) |
| BTC/Gold ratio | cross-asset | In late cycle and tight liquidity, hard assets beat speculative ones. "Bitcoin to drop another 30–40% vs gold" (Apr 2026), framed as a relative call. His improved social-risk metric tracks BTC/gold. | "Bitcoin to Drop Another 30% against Gold?" 3 Apr 2026; "Bitcoin: An Improved Social Risk Metric" 31 Mar 2026 [S] | occasional |
| Gold, silver, palladium, platinum, copper, uranium; gold/silver ratio | cross-asset | 2025–26: many "Gold/Silver/Palladium: Dubious Speculation" videos. Gold/silver ratio analogs (1973, 1987, 1998, 2006, 2011): silver likely topped while gold could make new highs (Feb 2026). "Gold bottoms first, then the long end tops" (Sep 2026). He says he holds metals and uranium. | "Gold: Dubious Speculation" 6 Feb 2026; "Silver Drops 38%" 31 Jan 2026; "Gold Drops Nearly 30%" 23 Mar 2026 [S]; Sep 2026 memo [V]; Bankless [S]; platform (metals) | frequent (2025–26; gold 80, silver 27) |
| Correlation coefficients (rolling 365-day) | cross-asset | Total crypto market cap vs gold 0.23, vs S&P 0.61 (Dec 2025). "Bitcoin has never traded like gold." High inflation raises cross-asset correlation. | Bankless [S]; "Bitcoin Vs. 10 Year Treasury Yields" 4 Jan 2022 [S]; platform: Correlation Coefficients | occasional (126) |
| Risk-curve / "risk cascade" ordering | cross-asset | In tightening, risk flows *down* the curve: altcoins → BTC → stocks → gold, with energy holding longest. In easing it flows *up*. The labor market is the last domino. | "How Risk Cascades Through Markets" memo 15 Mar 2026 [V]; "Business Cycles Ends With Recessions" 25 Feb 2026 [S] | frequent (2025–26 theme) |
| Valuation: Shiller CAPE, excess CAPE yield, trailing P/E | equities | CAPE 41.2 in Aug 2026, "second-highest in a century after 2000". Excess CAPE yield ≈ 0.97%. | Aug 2026 memo [V]; platform: S&P Statistics | rare |
| Breadth (S&P % above 200-day MA, S&P 600 small caps, crypto advance-decline for the top 100, coins above/below MAs) | equities / crypto | Narrowing breadth means late cycle. In Sep 2026 only ~48% of S&P constituents were above their 200-day. "Breadth broadens materially" is an invalidation signal for his bear case. | "Measuring The Breadth of Crypto Rallies" 14 May 2025 [S]; Q2 2026 and Sep 2026 memos [V]; platform: Advance Decline Ratios/Index, Coins Above/Below MA | occasional |
| Nasdaq/QQQ 1999 analog, Dow, Tesla, Hang Seng, palladium pattern analogs | equities | Spot ETF launch vs QQQ history (2024–25). ETH vs Tesla drawdown path (Dec 2025). Breakout-pullback patterns on palladium, HSI and BTC dominance applied to stablecoin dominance (2026). | "Bitcoin Market Cycles" 21 Nov 2024; "Right Translated or Left Translated?" 7 Mar 2025; "Bitcoin: An Unfortunate Pattern" 7 Jan 2026 [S]; Bankless [S] | occasional |
| Political regimes (party control and returns), presidential terms | equities / seasonality | Markets trend up under any party; averages and medians differ, and samples are small. | "Market Returns by Political Party" 13 May 2026 [S]; platform: Political Market Regimes tool, ~30 Politics charts | rare–occasional |

### 1.8 Seasonality & cycles

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| Four-year (halving) cycle: pre-halving year, halving year, post-halving year (top), midterm (bear) year | cycles | BTC tops in Q4 of the post-halving year (2013, 2017, 2021, 2025) and bottoms about a year later, around the US midterm. "The cycle is primarily about the timing of lows, not exact prices." In his 2026 view the cycle is "not dead". | "The Four Year Cycle Did Not Die" 12 Mar 2026; "…Is Not Dead" 26 May 2026; "The Unemployment Rate Rises to 4.6%" 17 Dec 2025 [S]; CMC Academy [S]; X post 6 Feb 2026 [S] | frequent (709 "cycle"; 243 "halving") |
| Midterm-year pattern / "window of weakness" | seasonality | 2014, 2018 and 2022 averages: a February low, an early-March rally (peak ~2–5 Mar), April–June weakness, a July pop, a weak Aug–Sep, and a final low in Q4. BTC was −15% from the yearly open by early March on average, and 2026 matched this ("simulation confirmed"). In 2026 he cited day counts (low ~day 56, rally into ~day 62). | "Bitcoin: Midterm Year Returns" 26 Feb 2026; "…Are We In A Simulation?" 5 Mar 2026; "Simulation Confirmed" 9 Mar 2026; "The Window of Weakness is Open" 28 Mar 2026; "The Window of Weakness" 29 May 2026 [S]; Jul 2026 memo [V] | frequent in 2026 (35 of 116 H1-2026 videos) |
| Presidential cycle / pre-election year (S&P), recession starts by presidential year | seasonality | Pre-election years tend to see a Q3 correction (2023). Midterm years are the weakest. September is the weakest month across ~24 midterm years since 1930. Recent midterm drawdowns: ~7% (2014), ~20% (2018), ~25% (2022). | "S&P 500 Outlook" 15 Dec 2023 [S]; Aug 2026 memo [V]; platform: Presidential Cycles and Recessions charts | occasional (65) |
| Monthly returns / September effect ("Wake Me Up When September Ends", yearly) | seasonality | September averages about −5% for BTC. In post-halving years a green July–August is followed by a red September, then a Q4 top. August–September are the weakest pair. | "Wake Me Up When September Ends" 2021–2025; "Bitcoin Monthly Returns" 18 Aug 2024 and 7 Aug 2025 [S]; platform: Monthly / Quarterly / Historical Monthly Average ROI | frequent |
| Post-halving-year template: summer rally → September pullback to the BMSB → Q4 top | cycles | Seen in 2013, 2017 and 2021, with "diminishing percentage returns". | "The Pattern That Historically Ended The Bull Market" 12 Aug 2025 [S] | occasional |
| "Summer lull" / "boring summer" | seasonality | Summer chop is normal; ATHs can still come later in the year. | "Bitcoin: Bull Market Support Band" 19 May 2025 [S] | occasional |
| Yearly-open percentage and year-to-date ROI by cycle year | seasonality | Pre-halving years: about half up and half down, so "bulls and bears both get wrecked". Recovery years (2015, 2019, 2023) show a mix of green and red months. | "Bitcoin Monthly Returns" 6 Jan 2023; "Pre-Halving Year Returns" 2023 series [S]; platform: Year-To-Date ROI | occasional |
| Day counts: bottom → top, top → bottom | cycles | Dec 2025: about 1,062 days low-to-top this cycle vs about 1,059 and 1,067 before (Bankless). May 2026 (CMC write-up): 1,162 vs 1,059 and 1,168. The two sets are **inconsistent** in the write-ups; treat the specific numbers as [S]. The 2019 analog bottomed on day 261 after its top; the July 2026 memo puts this cycle at day 282 "without the flush". | Bankless [S]; CMC Academy [S]; Jul 2026 memo [V] | occasional |
| Right- vs left-translated cycles | cycles | Macro (inflation, unemployment) can pull a top earlier (left-translated). | "Right Translated or Left Translated?" 7 Mar 2025; "Bitcoin: Market Cycles" 7 Mar 2024 [S] | occasional |
| Three psychological stages of a bear market (disbelief → partial acceptance → broad acceptance) | cycles / sentiment | Stage 1: Oct 2025–Feb 2026. Stage 2: Feb–Jun 2026. Stage 3: possibly Jun–Oct 2026. | "Bitcoin Enters the 3rd Stage of the Bear Market" 7 Jun 2026 [S] | rare |
| Midterm hike-year behavior | seasonality / Fed | In the two prior midterm hike years, BTC held near its hike-day level for about 7 weeks before breaking lower. In Oct 2026 he described "Bitcoin typically flat ~50 days, then drops" and put BTC at about day 43. | Sep 2026 memo [V]; Benzinga Oct 2026 via search snippet [S] | rare (2026) |

### 1.9 BTC valuation & cycle models (price-based)

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| **Risk metric** (0–1; "blue" low to "red" high; per asset and per denomination, i.e. USD, BTC and ETH risk) | BTC valuation | Flagship since 2019. It is price-based and accounts for time, volatility and diminishing returns. Used for **dynamic DCA**: accumulate at 0–0.2 (or below a chosen band), scale out from 0.8–1, with bigger buys the lower the risk. He says "No model is perfect." The platform describes it as a position on the asset's own historical ladder, not a probability. | "Bitcoin: Validating the risk model" 21 Dec 2019; "Bitcoin Risk Analysis – Have a plan!" 7 May 2020; "Bitcoin Risk Metric" (2021–2024 series) [S]; platform: Historical/Current Risk Levels, Price Color-Coded by Risk, Time in Risk Bands; DCA Simulator, Exit Strategies [V] | frequent (122) |
| Total / composite indicator risk (price + on-chain + social, each 0–1, equal weights) | BTC valuation | Avoids single-indicator false bottoms. Social risk kept the composite from showing a "deep value zone" in late 2022. | "Bitcoin Total Indicator Risk" 29 Nov 2022, 22 Dec 2022, 8 Feb 2023 [S]; platform: Crypto Indicator Risk Dashboard (Summary = mean of Price, On-Chain, Social; about two dozen indicators; band-position scores) [V] | occasional |
| Logarithmic regression bands; "fair value logarithmic regression" (fit to non-bubble data); regression rainbow | BTC valuation | Price reverts to fair value around halvings and bear lows, and tops come in upper bands that compress each cycle. ETH fair value near $2,100 in 2026 (Bankless). The ITC app labels the old charts "(Legacy)". | "Bitcoin Logarithmic Regression" 16 Jun 2022 and 25 Aug 2021; "Ethereum: Logarithmic Regression" 31 Dec 2025 [S]; platform [V] | frequent (277) |
| Total crypto market cap vs its log-regression trendline ("The Beauty of Mathematics", monthly series, Part 71 by Jun 2026) | BTC valuation / crypto | Measures extension of the whole market. In Feb 2021 it was "not close to a peak". | "Why I DO NOT think we are close to a market cycle peak" 20 Feb 2021; Beauty of Mathematics parts 1–71 [S]; platform: Total Crypto Market Cap & Trendline (free) | frequent (series) |
| Asymmetric quantile regression fan (2026 study) | BTC valuation | The upper tail compresses across cycles while lower support stays close to a power law. He calls it descriptive, not a forecast. Out-of-sample average errors since publication: OLS power law ≈ +32%, stock-to-flow ≈ +295%, S2FX ≈ +1,699%. | Report "Asymmetric Tail Curvature in Bitcoin Price Quantiles" 29 May 2026 [V]; video 30 May 2026 [S]; platform: Asymmetric Quantile Regression Fan [V] | rare (new) |
| Diminishing returns; lengthening-cycles theory (LCT) | BTC valuation | Each cycle's ROI is smaller. 2019–2021: he argued cycles were lengthening, so the top would come after 2021. That was wrong: BTC topped on 10 Nov 2021. From 2023 he went back to four-year timing and kept diminishing returns. | "Bitcoin Lengthening Cycles And Diminishing Returns" 19 Jul 2021; "Market Cycle Has Now *Unofficially* Lengthened" 19 Nov 2021; "Bitcoin Re-accumulation" 23 Nov 2021; "Bitcoin Market Cycle" 6 Dec 2021 [S] | frequent 2019–22 (114), rare after |
| Market-cycle ROI (from bottom, halving or peak); running 1-year ROI; ROI bands; ROI after halving / bottom / peak | BTC valuation | Shows where the current cycle sits relative to past ones. Diminishing multiples. | "Bitcoin Market Cycle ROI" (many); "Bitcoin: ROI After Halving" 14 Jul 2025 [S]; platform: ~20 ROI charts | frequent (167) |
| Drawdown from ATH | BTC valuation | Bear markets linger at 60–70% drawdowns before bottoms (2022). In 2026: "~50% down", "bear market not over". | "Bitcoin Percentage Drawdown from the All Time High" 22 Nov 2022 [S]; platform | occasional |
| Short-term bubble risk (price extension above the 20-week SMA) | BTC valuation | Flags local overheating (Dec 2021, Jan 2024). | "Bitcoin: Short-Term Bubble Risk" 29 Mar 2023, 23 Jan 2024 [S]; platform (Basic) | rare (11) |
| Terminal price, balanced price (on-chain-derived price bands) | BTC valuation / on-chain | Tops come near terminal price ($188k in Dec 2024, not reached in 2025, because the top came "on apathy"). Every bear has broken below balanced price (~$37.7–40k in 2026). | "Bitcoin: Terminal Price" 4 Dec 2024; "How low will Bitcoin go?" 12 Feb 2026 [S]; Jul 2026 memo [V]; platform | occasional |
| Stock-to-flow (S2F) and S2FX | BTC valuation | Discussed with PlanB (2021–22) as one theory among several. 2026 study: S2F's error was +295% since publication. | "…Stock-To-Flow, Lengthening Cycles…" 11 Aug 2021 [S]; 2026 quantile report [V] | rare |
| Cowen Corridor (ratio of two moving averages and its slope; weekly) | BTC valuation | An upper/lower bound band. Community re-creations on TradingView describe it as approximate. | platform (Standard) [V]; TradingView repost [S] | rare |
| Cycles Deviation; Benford's Law; Price Milestone Crossings ("How many times has BTC crossed $100k?") | BTC valuation | Niche or educational. | platform [V]; videos 3 Mar 2025, 13 Nov 2025 [S] | rare |

### 1.10 Technical analysis

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| **Bull Market Support Band (BMSB)** = 20-week SMA + 21-week EMA | TA | Weekly closes above it mean bull market; below it means bear. Rallies back to it from below in a bear market are lower highs ("bear market resistance band"). It is often lost and regained in September of post-halving years. "Two consecutive weekly closes" confirm. | weekly series "Bitcoin: Bull Market Support Band" since 2020; "Bitcoin Bull Market Support Band" 22 Oct 2026 (RSS) [V]; platform (Basic) | frequent (307; plus 20W/21W 500) |
| Bear Market Resistance Band (the same band seen from below) | TA | 2022 and 2026: rallies to the band (~$82–83k in Apr–May 2026) are rejected. Losing it again confirms the bear. | "Bitcoin Bear Market Resistance Band Update" 24 Jan 2022; "Bitcoin Rallies to the Bear Market Resistance Band" 20 Apr 2026; "Bitcoin Closes Below the Bear Market Resistance Band" 1 Jun 2026 [S] | occasional (13, 2022 and 2026) |
| 50-week SMA | TA | A rally to the 50W in a bear "confirms" the bear (~$102k in Dec 2025). Losing the 50W in Nov 2025 marked the turn. Jul 2026: a sustained weekly reclaim (~$86.5k) would weaken the bear thesis; in Sep 2026 BTC cleared it. | "Bitcoin Falls Below the 50 Week Moving Average" 17 Nov 2025; "The Importance of the 50 Week Moving Average" 6 Jul 2025 [S]; Bankless [S]; Jul and Sep 2026 memos [V] | occasional (83) |
| 100-week, 200-week ("a date with destiny"), 300-week SMA | TA | The 200W is the classic bear-market floor and midterm accumulation zone ($60–70k estimated in Dec 2025; tagged 5 Jun 2026). Bears break the 50W, then 100W, then 200W. A break and reclaim of the 200W also preceded the 2022 low. When the 200W crosses above the prior ATH it lines up with cycle tops (a lagging signal). | "Bitcoin: A Date With Destiny" (2022, 2025, 2026); "Bitcoin: An Indicator For Market Cycle Tops" 12 Jun 2025; "Bitcoin Crash Continues" 5 Feb 2026; "Bitcoin Falls to the 200W Moving Average" 5 Jun 2026 [S]; Jul 2026 memo [V] | occasional (86 for 200W) |
| 200-day SMA; 50/100-day SMA; 8-week SMA | TA | The 200D was resistance in the 2018, 2022 and 2026 bears ("Bitcoin Rejected off the 200D", 19 May 2026). Breaking the 8W SMA leads to tests of the BMSB. | rosetta [S]; platform: Moving Averages | occasional (76) |
| Golden cross / death cross (50D vs 200D) | TA | "The golden cross dump" (May 2025) and "the death cross rally" (Apr 2025): crosses are often contrarian in the short term. | "Bitcoin: Upcoming Golden Cross" 20 May 2025; "The Golden Cross Dump" 23 May 2025; "The Death Cross Rally" 22 Apr 2025 [S]; platform | occasional (64) |
| Pi Cycle Top (111D SMA vs 2×350D SMA) | TA | Signaled in Apr 2021. He revisited it in 2024. | "The Pi Cycle Top Has Signaled" 12 Apr 2021; "Bitcoin: Pi Cycle Top Indicator" 22 Mar, 21 Aug, 26 Nov 2024 [S]; platform: Pi Cycle Bottom/Top | rare (10) |
| RSI (daily, weekly, monthly); MACD; Bollinger Bands; Supertrend | TA | RSI is used to compare corrections in context. The others are on the platform and rarely discussed. | "Bitcoin Correction In Context (Relative Strength Index)" 11 Apr 2022; "Bitcoin Relative Strength Index" 9 Nov 2025 [S] | RSI occasional (63); others rare |
| Fibonacci retracements (0.382, 0.5) | TA | ETH/BTC 0.053 = 0.5 retracement and the pre-Merge low (Dec 2025). BTC rallies stall near 0.382 in bears (May 2026). | Bankless [S]; "Bitcoin: Dubious Speculation" 14 May 2026 [S] | rare–occasional |
| Heikin-Ashi candles | TA | Smoothed trend view. | "Bitcoin: Heikin-Ashi Candles" 26 Apr 2026 [S] | rare |
| Weekly, monthly, daily and 3-day closes | TA | "Wicks don't matter, closes do". Roadmap conditions are written as weekly closes (e.g., "weekly close below $83k"). | "An Important Weekly Close" 17 Oct 2021 [S]; X post 26 Oct 2026 [S] | occasional (67) |
| Market structure: lower highs / lower lows, counter-trend rallies, "fakeouts", harmonic "butterfly" | TA | Bears "trend up for weeks before sharp breakdowns". Macro lower high, then lower low. | "Bitcoin: The Structure of a Bear Market" 10 Mar 2026; "Ethereum: The Butterfly Effect" 4 Mar 2025 [S]; Bankless [S] | occasional (84) |
| "Hold the line" conjecture | TA | Once BTC holds the 20W SMA as support in a cycle, it does not revisit that level. He tested this at $40k in Jan 2022; it failed. | "Bitcoin: The 'Hold The Line' Conjecture" 20 Jan 2022 [S] | rare |
| Fear & Greed Index | sentiment / TA | A recurring check. Extreme fear is not by itself a bottom. | "Bitcoin: Fear & Greed" 28 Jan 2025, 12 Nov 2025 [S]; platform (free) | occasional |

### 1.11 On-chain

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| Realized price ("the cost basis of the network") | on-chain | Every prior bear market bottomed *below* realized price (2011, 2014–15, 2018, 2020 crash, 2022). It was ~$53–54k in Jun–Sep 2026, untested, which is why he kept a 65% probability that the low was still ahead. | "Bitcoin: The Cost Basis of the Network" 11 Jun 2026 [S]; Jul 2026 memo [V]; CMC Academy Sep 2026 [S] | occasional (2026) |
| MVRV Z-score | on-chain | A drop below zero = accumulation zone and cycle bottoms. In 2026 it was "bouncing rather than resetting below zero", so the reset was incomplete. | "Bitcoin On-Chain Analysis: MVRV Z-Score" (2022–2024); "Bitcoin: MVRV Z-Score" 22 Jan 2025 [S]; Jul 2026 memo [V]; platform | occasional (13) |
| Percentage of supply in profit vs in loss (crossing) | on-chain | Cycle lows came about 1–4 months after the profit and loss lines crossed (2011, 2014, 2018, 2022). The lines crossed at the June 2026 low. The bottom zone is about 35–45% in profit. | "Bitcoin: Timing Cycle Bottoms" 19 Jan 2026; "Bitcoin: A Beautiful Chart" 10 Jun 2026 [S]; Jul 2026 memo [V]; platform | occasional |
| On-chain risk composite | on-chain | A separate 0–1 gauge. It read 0.181 in Aug 2026. | "Bitcoin On-Chain Risk" (Nov 2022 … 8 Dec 2025) [S]; Aug 2026 memo [V] | occasional |
| Puell Multiple, hash ribbons, hash rate, miner flows; Thermocap ratios (MCTC, mCTC, RCTC); SOPR; NUPL; HODL waves, RHODL; Coin Days Destroyed, dormancy; whale watching | on-chain | Mostly 2020–2023 educational series ("Identifying Macro Bottoms"). In 2025–26 they appear only as background checks. | "Puell Multiple (Identifying Macro Bottoms)" 26 Nov 2022; "Hash Ribbons" 23 Apr 2022; "MinerCap To ThermoCap Ratio" 16 May 2025; "SOPR" 9 Jan 2022; "Bitcoin HODL Waves" 9 Jul 2025 [S]; platform (~50 on-chain charts, Whale Watching dashboard) | rare–occasional |
| Stablecoin Supply Ratio (SSR) and its oscillator | on-chain / liquidity | Stablecoin "dry powder" relative to BTC market cap. | "Bitcoin: Stablecoin Supply Ratio (Oscillator)" 2023–2025 [S]; platform | occasional |
| Spot ETF holdings and flows | on-chain / flows | ETF holdings "absorbed supply on the way up but have rolled over" (Jul 2026). ETF and treasury-company narratives "did not prevent Bitcoin from losing roughly half its value". In Sep 2026 he suggested ETFs may have tightened BTC's link to TradFi. | Jul 2026 memo [V]; "The Structure of a Bear Market" 10 Mar 2026 [S]; Benzinga Sep 2026 [S]; platform: Crypto ETF Flows, Crypto Treasuries | occasional |

### 1.12 Sentiment & social

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| **Social risk** (built from YouTube subscribers and views of crypto channels, plus X followers of analysts, exchanges and Layer-1s; the 2026 "improved" version adds Google Trends and the Coinbase app ranking) | sentiment | A proxy for retail participation and liquidity entering the space. In downtrend since mid-2021 / Nov 2024. Alt seasons need social risk to turn up. Bottoms come in apathy. This cycle's top came "on apathy", and crypto became a "ghost town" with social interest at ~16% of 2021 levels (Jan 2026). | "Bitcoin: Social Risk" 13 Nov 2022 (introduced) … 29 Nov 2023; "Why Retail Never Returned" 24 Apr 2025; "Has Retail Arrived Yet?" 29 Jul 2025; "Crypto Ghost Town" 13 Jan 2026; "An Improved Social Risk Metric" 31 Mar 2026 [S]; platform: YouTube Subscribers/Views, X Followers (Analysts/Exchanges/L1s), X Posts, Google Trends, Wikipedia Page Views, App Ranking (Coinbase), Social Volume/Dominance, Sentiment | occasional–frequent (60 + series) |
| Apathy vs euphoria at the top | sentiment / cycles | "When you top on apathy, like in 2019, you don't get that rotation… there's just no one left to sell the altcoins to." "Topping on apathy doesn't mean you don't have a bear market." Apathy-driven bears are choppier, with repeated counter-trend rallies, and are not necessarily deeper. | Crypto Macro Risk Memo Q1 2026 [V]; Cointelegraph via search snippet [S]; 24/7 Wall St. [S] | frequent (2025–26) |
| Memecoins / capital misallocation | sentiment | Memecoin scams and influencer pumps drained retail. The industry needs real revenue models. | "The Misallocation of Capital in Crypto (Memecoins)" 12 Feb 2025; "Investors Should Rebuke Memecoins" 18 Feb 2025 [S]; Bankless [S] | occasional |

### 1.13 Dominance & altcoins

| Indicator / chart | Category | How he uses it | Evidence | Freq. |
|---|---|---|---|---|
| **Bitcoin dominance** (BTC.D), shown both **including and excluding stablecoins** | dominance | Rises in bear markets, pre-halving years and QT. Peaks at the QT→QE transition. A BTC-heavy portfolio gives better risk-adjusted returns while dominance rises. Rising dominance "is not inherently negative" and happens whether BTC/USD goes up or down. Long-held target 60% (from 2023), reached on 30 Oct 2024. Then 66% (2025). Ex-stablecoins it was 67% in Feb and Aug 2026. | "Bitcoin Dominance" (2022–2026, dozens); "Bitcoin Dominance Hits 60%!" 30 Oct 2024; "Bitcoin Dominance Breaks 65%!" 6 May 2025; "The Final Rotation" 31 Aug 2025; "Bitcoin Dominance" 15 Feb 2026 [S]; Aug 2026 memo [V]; platform: Dominance (free) | frequent (281) |
| Stablecoin dominance (USDT.D + USDC.D) | dominance / sentiment | 2026 "unfortunate pattern": stablecoin dominance broke out from a multi-year base and pulled back, like earlier BTC.D, HSI and palladium breakouts, which is bearish for crypto. Target 14–15% later in 2026. Rising stables explain why headline BTC.D stalled. | "Bitcoin: An Unfortunate Pattern" 7 Jan 2026 and updates 18 Mar, 20 May 2026; "Stablecoin Dominance" 26 Jan 2024 [S] | occasional (19) |
| **ETH/BTC** | dominance / alts | ETH is "the altcoin index" (2023, Coin Bureau [S]). ETH/BTC bled from 2022. He targeted 0.03–0.04 (2024); it fell further, to about 0.018 in Apr 2025 [I]. "ETH going home" to $1,500–1,600 (hit Apr 2025). He then called an ETH/BTC bottom and bought ETH in Apr 2025. Upside target ≈0.053 (Dec 2025). ETH does best when FFR ≤ 2Y. | "ETH/BTC Outlook" (2023–24); "ETH / BTC: Is the Bottom In?" 9 Nov 2024; "Welcome Home, Ethereum" 7 Apr 2025; "Eth / Btc" (Jun–Aug 2025) [S]; Bankless [S] | frequent (146) |
| Altcoin pairs vs BTC; "all BTC pairs to range lows"; altcoin market cap ÷ BTC market cap (target 0.25) | alts | Alt season requires alts to capitulate to historical range lows against BTC first. The ratio went 0.32 (Jun 2025) → 0.31 (Jul) → 0.29 (Oct 2025; "already reached" 0.25 if USDC is included). "Altcoins are oscillators at best and bleeders at worst." | "Altcoins Hit 0.32/0.31/0.29" 14 Jun, 4 Jul, 14 Oct 2025; "Bitcoin Dominance: The Final Stretch" 12 Aug 2024; "SOL/BTC: Dealing With Emotions" 27 Feb 2025 [S] | occasional |
| TOTAL, TOTAL2, TOTAL3, OTHERS, "Total Market Cap excl. BTC, ETH and stables" | alts | Market-wide or alt-only capitalization. On ITC this is a synthetic asset with its own risk metric. | "Total Cryptocurrency Market Capitalization Risk Metric" 5 Oct 2021 [S]; platform asset list (TOTAL, BTC.D synthetic assets) [V] | occasional (50) |
| Alt season definition; Altcoin Season Index; "Bitcoin season vs altcoin season" (90-day ROI of BTC vs the top 50) | alts | Alt season = falling BTC dominance *while* alts rise in USD. It needs (1) looser monetary policy, (2) high retail social interest, (3) a BTC top on euphoria. None were present in 2024–25, so there was "no alt season". | "Bitcoin Season Vs. Altcoin Season" 11 Dec 2022; "Why Has Alt Season Not Happened Yet?" 7 Feb 2025 and Part 2 27 Jun 2025; "Why ALT Season Has Not Happened" 4 Nov 2025; "Why So Many People Were Wrong About Altcoins" 22 Dec 2025 [S]; platform: Altcoin Season Index | frequent (98) |
| "Final rotation" | dominance | In the late post-halving year, BTC dominance rises again into Sep–Oct as alts give back gains. | "Bitcoin Dominance: The Final Rotation" 31 Aug, 29 Sep, 10 Oct, 21 Oct, 26 Oct 2025 [S] | occasional (2025) |
| Flippening Index, Market Cap Hypotheticals | alts | Platform tools. | platform [V] | rare |

### 1.14 Portfolio and process tools (they appear in almost every video's framing)

| Tool / concept | How he uses it | Evidence | Freq. |
|---|---|---|---|
| DCA and dynamic DCA by risk band; lump sum vs DCA; "Best Day To DCA" | Accumulate in low-risk zones and in the second half of midterm years, rather than trying to time the exact low. | "Investing $1,000 Into Crypto?" 22 Jul 2025; "Bitcoin: Dubious Speculation" 8 Jun 2026 [S]; DCA Simulator help text [V] | frequent (118) |
| Exit strategies (selling in slices as risk rises through 0.4…1.0; preset profiles from "Conservative" to "Sea of Tranquility") | Scale out instead of calling the top. | platform help text [V]; "Bitcoin Risk Metric" 31 Aug 2024 [S] | occasional |
| Modern Portfolio Theory simulation; portfolio-weighted risk; "Portfolios Weighted by Market Cap" | Risk-adjusted returns. A BTC-heavy portfolio while dominance rises. | "Cryptocurrency Portfolio Weighting Strategies" 3 Jan 2025 [S]; platform [V] | occasional |
| "Dubious Speculation" | A named series of explicitly speculative scenario videos for BTC, ETH, gold, etc. | 106 videos 2021–2026 [S] | frequent |
| Diversification beyond crypto (cash, metals, energy, index funds, uranium) | "Don't marry one asset class." "Wealth preservation is the name of the game in a midterm bear." | Bankless [S]; "Visualizing the Business Cycle" 22 Feb 2026; "Simulation Confirmed" 9 Mar 2026 [S] | frequent (2025–26) |

---

## 1b. What the ITC platform actually contains (catalogue extracted 2026-10-30) [V]

Tiers, from the platform's own help text: **Lite** (free: logarithmic regression chart, dominance chart, feed, total market cap trendline), **Basic**, **Standard** (crypto risk, on-chain, social, most technical charts), **Pro** (all macro charts, Macro Recession Risk dashboard, Macro Liquidity Risk dashboard, macro calendar, premium video).

Dashboards and tools: Dashboard (favourite assets + crypto and macro risk gauges + calendar); **Crypto Indicator Risk Dashboard** (Summary = equal-weighted mean of Price Metrics, On-Chain Metrics and Social Metrics; about two dozen indicators; each scored 0–1 as its position between a lower and an upper band on a log scale; weightless indicators: Running ROI, RHODL Ratio, Supply in Profit/Loss, Wikipedia Page Views); **TradFi Indicator Risk Dashboard** (Google Trends for six metals); **Whale Watching Dashboard** (Whale Activity Score from 25 Santiment/CryptoQuant inputs; Hyperliquid positioning via CoinGlass); **Macro Recession Risk Dashboard** (four categories: Employment, National Income & Product, Production & Business, Interest Rates at weight 0.2; 17 FRED series; each metric turned into a rate of change and scored by how well it fits recession vs expansion distributions since 1947; Credit Spreads card with 3 ICE BofA OAS series kept out of the summary); **Macro Liquidity Risk Dashboard** (five monthly inputs: effective FFR, 2Y yield, dollar index, MoM change in Fed total assets, MoM change in M2; combined via first principal component, 6-month smoothing, percentile rank since Jan 2003); Crypto Screener; Workbench; Metric Analyzer (MA crosses of any metric); DCA Simulator; Exit Strategies; MPT Simulation; Portfolio Weighted Risk; Political Market Regimes; Investment Backtest; asset pages (Risk / Supply / Metrics / Fundamentals tabs); TradFi indexes, sectors, stocks, ETFs, metals; Crypto ETF Flows; Crypto Treasuries; Macro Calendar & Indicators (TradingEconomics + FRED, 19 countries); Studies; Premium Reports; Cowen AI Chatbot.

Chart counts by category (380 entries): Price Metric 67; On-Chain 52; Money, Banking & Finance 44; People, Employment & Labor 43; Politics 30; National Income & Product 29; Prices 21; Real Estate 19; Fundamentals 16; S&P Statistics 16; Social Media 12; Production & Business 8; Derivatives 4; NFT 3; uncategorized 16.

The macro charts listed in the catalogue, all Pro tier and condensed here, form the course's coverage checklist:
- **Interest rates:** Fed Funds Target Range; Effective FFR; Global Interest Rate Map; Constant Maturity Treasury; Treasury Yield Spreads; Treasury Yield Curve; Days After Inversion; Days After Uninversion; Real Interest Rates / Spreads / Curve.
- **Dollar:** DXY.
- **Monetary data:** Currency in Circulation; M1; M2; Retail Money Market Funds; Fed Total Assets; ON RRP; Treasury Deposits with Fed (TGA).
- **Recessions:** Past Recession Statistics; ITC Business Cycles; Smoothed Recession Probabilities; Sahm Rule (national, per state, number/map of states triggered); RGDP Recession Indicator; Composite Leading Indicator (CLI); NFCI; St. Louis Fed Financial Stress Index; Coincident Economic Activity Index; Economic Policy Uncertainty (incl. categorical); World Uncertainty Index; Equity Market Volatility Tracker.
- **Banking:** deposits; consumer loans; consumer credit; delinquency rates; loans & leases; bank assets/liabilities; SLOOS (net % of banks tightening standards / reporting stronger loan demand).
- **Fiscal:** federal debt; federal surplus/deficit; global debt-to-GDP.
- **Output:** GDP, GDI, average of GDP/GDI, GNP, GNI, GDP per capita, world GDP, imports/exports/net exports.
- **Income:** average hourly earnings; hours; real median weekly earnings; real personal income (incl. ex-transfers); real disposable income; tax receipts; personal saving rate; GPDI; corporate profits; net saving.
- **Labor:** participation; employment level; private payrolls; temp help; multiple jobholders; Indeed postings; employment-population ratio; job openings; quits level and rate; layoffs; hires; initial and continued claims (per state and maps); KC Fed LMCI (level and momentum); unemployment level/rate (incl. per state, number of states rising, global map, by reason, alternative measures, not in labor force, duration); population; net-worth/asset distribution.
- **Sentiment:** Michigan sentiment; Manufacturing Confidence Index (OECD).
- **Prices:** CPI, core CPI, CPI contributions by category; PCE, core PCE, PCEPI, core PCEPI; PPI, PPIAC; global inflation map; WTI crude; eggs, dairy, meat.
- **Production & business:** business inventories; manufacturers' new orders; inventories-to-sales; industrial production; capacity utilization; vehicle sales; real manufacturing & trade sales; advance retail sales.
- **Real estate:** purchase-only HPI; Zillow ZHVI; price cuts count; listing prices; housing starts and under construction; mortgage rates; RE loan delinquency; homeownership; owners' equity; rental vacancy; new home sales; for-sale/sold ratio; months to sell.
- **S&P statistics:** trailing PE; Shiller CAPE; total-return CAPE; real price/dividends/earnings; S&P risk and time in risk bands; dividend yield; earnings yield; excess CAPE yield; ROI in S&P bear/bull markets; ROI after yield-curve inversion.
- **Politics:** House/Senate heatmaps; regime returns, drawdowns and Sharpe; presidential-term paths; inauguration event study; recession starts by presidential year; recession duration vs drawdown; recovery speed after troughs.
- **AI-capex block:** Major Tech Capex; US Data Center Investment; US Semiconductor Production; AI-related GDP contributions; AI adoption by firm size.

Notable gaps in the catalogue, which matter for the course [V/I]: the **ISM PMIs**, **Conference Board LEI**, **VIX/MOVE**, **inflation breakevens/expectations**, **term-premium models**, **GDPNow**, **global M2** and **funding rates** do not appear as named catalogue charts. Some may exist in Workbench metrics. Where Cowen shows ISM or VIX in videos he uses other sources (TradingView or FRED) [I].

---

## 1c. Frequency evidence (keyword hits in 2,385 video titles + AI summaries, 2019 → 11 Jun 2026) [S]

Counts are videos whose title or summary matches the keyword. 2026 covers only 1 Jan–11 Jun. Regexes are approximate; use the counts for relative weight only.

| Keyword group | '19 | '20 | '21 | '22 | '23 | '24 | '25 | '26H1 | total |
|---|---|---|---|---|---|---|---|---|---|
| **Videos in year** | 55 | 422 | 679 | 336 | 276 | 247 | 254 | 116 | 2385 |
| 20W/21W MA (BMSB family) | 4 | 183 | 203 | 34 | 25 | 26 | 20 | 5 | 500 |
| Bull market support band | 0 | 13 | 113 | 58 | 34 | 48 | 33 | 8 | 307 |
| Bitcoin dominance | 3 | 10 | 14 | 26 | 59 | 95 | 63 | 11 | 281 |
| Log regression / fair value | 13 | 88 | 67 | 39 | 21 | 15 | 23 | 11 | 277 |
| Fed / FOMC / Powell / Warsh | 0 | 2 | 0 | 65 | 63 | 66 | 57 | 17 | 270 |
| Seasonality (months, Q4, "window of weakness") | 0 | 13 | 51 | 20 | 38 | 36 | 64 | 45 | 267 |
| Halving | 8 | 24 | 24 | 11 | 75 | 64 | 30 | 7 | 243 |
| S&P 500 / stocks | 2 | 15 | 5 | 63 | 53 | 20 | 35 | 46 | 239 |
| 2019 analog | 1 | 8 | 16 | 9 | 57 | 76 | 34 | 25 | 226 |
| DXY / dollar | 8 | 55 | 50 | 49 | 26 | 23 | 7 | 5 | 223 |
| Inflation (CPI/PCE/PPI) | 0 | 1 | 2 | 65 | 43 | 22 | 37 | 18 | 188 |
| ROI | 16 | 38 | 49 | 18 | 16 | 19 | 9 | 2 | 167 |
| Unemployment / labor | 0 | 0 | 0 | 21 | 34 | 45 | 37 | 22 | 159 |
| Recession | 1 | 7 | 0 | 27 | 69 | 13 | 11 | 21 | 149 |
| ETH/BTC | 1 | 39 | 28 | 8 | 14 | 33 | 22 | 1 | 146 |
| Rate cuts / pivot | 0 | 0 | 0 | 16 | 26 | 62 | 29 | 9 | 142 |
| Risk metric | 5 | 47 | 27 | 4 | 16 | 17 | 5 | 1 | 122 |
| DCA | 7 | 43 | 16 | 16 | 21 | 9 | 4 | 2 | 118 |
| Diminishing returns | 2 | 32 | 49 | 15 | 3 | 5 | 8 | 0 | 114 |
| QT / balance sheet / QE | 0 | 0 | 1 | 7 | 7 | 45 | 50 | 1 | 111 |
| Liquidity / M2 | 0 | 1 | 18 | 7 | 41 | 14 | 15 | 15 | 111 |
| Alt season / alts vs BTC | 0 | 5 | 13 | 7 | 10 | 21 | 39 | 3 | 98 |
| Yield curve / 10Y / 2Y | 1 | 2 | 3 | 19 | 29 | 19 | 12 | 1 | 86 |
| 200-week MA | 2 | 33 | 18 | 17 | 3 | 0 | 6 | 7 | 86 |
| 50-week MA | 3 | 23 | 25 | 7 | 5 | 0 | 17 | 3 | 83 |
| Gold | 0 | 9 | 5 | 6 | 4 | 9 | 16 | 31 | 80 |
| Midterm / presidential / election | 0 | 2 | 0 | 0 | 16 | 6 | 6 | 35 | 65 |
| Golden/death cross | 1 | 12 | 15 | 2 | 15 | 3 | 16 | 0 | 64 |
| RSI | 1 | 10 | 23 | 9 | 5 | 5 | 9 | 1 | 63 |
| Social risk / apathy / Google Trends / YouTube views | 0 | 1 | 3 | 6 | 12 | 10 | 13 | 15 | 60 |
| 1970s analog | 0 | 0 | 0 | 5 | 11 | 7 | 5 | 10 | 38 |
| Business cycle / ISM / PMI / manufacturing | 0 | 0 | 0 | 0 | 6 | 5 | 2 | 17 | 30 |
| Stablecoin dominance / SSR | 0 | 0 | 0 | 1 | 6 | 5 | 1 | 6 | 19 |
| Oil | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 9 | 15 |
| MVRV | 0 | 0 | 0 | 4 | 2 | 3 | 2 | 2 | 13 |
| Realized price / cost basis | 0 | 1 | 0 | 2 | 0 | 1 | 0 | 6 | 10 |
| Pi Cycle | 0 | 0 | 7 | 0 | 0 | 3 | 0 | 0 | 10 |
| Sahm rule | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 3 |
| Real rates | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| Credit spreads / consumer sentiment | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

How his toolset evolved [I from the table]:
- **2019–2021:** technical-quantitative. Log regression, the BMSB, the risk metric, ROI, lengthening cycles, the DXY and DCA. Almost no macro.
- **2022–2024:** macro enters with the Fed hiking cycle. CPI, the Fed, the yield curve, recession, unemployment, S&P bear markets. Then from 2023, BTC dominance, the 2019 analog, QT and social risk.
- **2025–2026:** labor market, QT end, "why no alt season", apathy top, the midterm-year template, gold, the late business cycle, oil and the Fed "checkmate", and on-chain bottoming tools (realized price, supply in profit/loss, MVRV).

---

## 2. Recurring theses and playbooks (his framing, with dates, checked)

Each entry gives his framing, the evidence, and a check. My critique is marked [I].

**T1. The four-year cycle; tops in Q4 of the post-halving year; bottoms around the midterm Q4.**
- *His framing:* "The most likely low for BTC is October 2026, based on the 4 year cycle. Under some circumstances it could happen as early as May. BTC does not have a monopoly on the four-year cycle" (X, 6 Feb 2026, per search snippet [S]). "The cycle is primarily about the timing of lows, not exact prices" (26 May 2026 [S]).
- *Check [V]:* BTC cycle tops were 4 Dec 2013 (≈$1.1k), 17 Dec 2017 (≈$19.8k), 10 Nov 2021 (≈$69k) and 6 Oct 2025 (≈$126.1–126.2k per CoinDesk/24/7 Wall St.). All fell in Q4 of a post-halving year. Lows were 14 Jan 2015, 15 Dec 2018 and 21 Nov 2022, i.e. around Q4 of the midterm year (2014's low slipped into January 2015). His Jul 2026 memo says "two of the three prior cycles bottomed in that quarter" [V].
- *Critique [I]:* this rests on three or four observations. The halving, the US election calendar and global liquidity cycles are entangled, so you cannot tell which one drives the pattern.

**T2. Diminishing returns (kept), and lengthening cycles (abandoned).**
- *His framing:* 2019–2021 "lengthening cycles theory" (LCT). In Nov 2021 he wrote the cycle "has now *unofficially* lengthened" and argued against a parabolic Q4 2021 [S].
- *Check:* the 2021 top came on four-year schedule, on 10 Nov 2021, so LCT failed. Diminishing returns did hold: peak multiples from the prior cycle low were roughly ×500+ (2011 low → 2013 top), ×130 (Jan 2015 → Dec 2017), ×22 (Dec 2018 → Nov 2021) and ×8 (Nov 2022 → Oct 2025) [I, computed from approximate prices]. The 2026 quantile-regression report formalizes the compression of the upper tail [V].

**T3. Bitcoin dominance rises during QT, hiking and pre-halving phases; it peaks around the QT → QE transition.**
- *His framing:* "Last cycle the transition from QT to QE marked the top for BTC dominance." "I expect the Fed to transition from QT to QE next year" (Cointelegraph Mag, 19 Nov 2024 [S]).
- *Targets and dates:* 60% (repeated from mid-2023, e.g. 23 Aug and 8 Oct 2023 [S]). He expected it "by end of summer or September" (May 2024) and "September or December" (Aug 2024) (Benzinga [S]). It hit 60% on 30 Oct 2024 [S]. He then expected dominance to "go down in 2025" (Nov 2024 [S]). Instead dominance kept rising, and he moved the target to 66% (25 Feb 2025, "The Bitcoin Dominance Train (To 66%?)"; 21 Apr 2025 [S]). It broke 65% on 6 May 2025 and made a new cycle high on 22 Jun 2025 [S]. It dropped in Jul–Aug 2025 during the ETH run, and he then called a "final rotation" back up into Sep–Oct 2025 [S]. In Nov 2025: "Bitcoin Dominance To Surge Into December" [S].
- *2026:* headline dominance stalled near 58–61% because stablecoins' share rose. Ex-stables it was 67% (15 Feb 2026 [S]; Aug 2026 memo [V]).
- *Critique [I]:* QT ended on 1 Dec 2025, but no QE followed in 2026; the Fed hiked in Sept 2026. So the "QT→QE marks the dominance top" rule went untested this cycle. The mechanism (tight dollar liquidity → flight to quality within crypto) is plausible, but there are few cycles to check it against.

**T4. "Altcoins bleed against Bitcoin" / why there was no alt season.**
- *His framing:* "Altcoins are oscillators at best and bleeders at worst" (Aug 2024 [S]). Alt season needs "(1) looser monetary policy, (2) high retail social interest, (3) Bitcoin topping on euphoria rather than apathy" (22 Dec 2025 [S]). "Altcoin rotations have historically followed stock market sell-offs that prompted Fed easing. The Fed doesn't rescue crypto directly" (Bankless, 23 Dec 2025 [S]). The next alt season will come "only when monetary conditions become significantly looser, potentially in 2027–2029" (20 Feb 2026 [S]).
- *Check:* no broad alt season came in 2024–25. Alts were "back at 2022 lows" by Feb 2026 [S], and the alt/BTC ratio fell to 0.29 in Oct 2025 [S]. He held this call against the crowd for about two years, and it was correct.

**T5. ETH/BTC: bleed, then "going home", then a bottom.**
- *Earlier:* "ETH/BTC could crash to 0.032" (Benzinga, Sep 2023 [S]); ETH/BTC target 0.03–0.04 and "all BTC pairs to 0.25" (25 Oct 2024 [S]).
- *Spring 2025:* "Welcome Home, Ethereum": ETH at $1,500–1,600 (7 Apr 2025) [S]. The ETH low was ≈$1,386 on 9 Apr 2025 [S]. He says he bought ETH in Apr 2025 and that ETH/BTC bottomed then (Bankless [S]).
- *What followed:* ETH set an ATH of ≈$4,946–4,955 on 24 Aug 2025 [V: CNBC/Coinbase]. Dec 2025: possible ETH/BTC target ≈0.053; "fair value log regression could be near $2,100 in 2026"; reaching $5k in early 2026 would likely be a bull trap [S].
- *State in Oct 2026:* ETH ≈$2,230, ETH/BTC ≈0.0286 [S, computed from reported prices].

**T6. "Rate cuts are not bullish at first"; the real bull comes after the *last* cut.**
- *His framing:* BTC "historically bottomed around the Fed's terminal rate", and "the real bull market often begins after the last rate cut, not the first, especially when the Fed pivots due to economic damage" (24 Jan 2023 [S]). Risk assets often top around the first cut (2000, 2007; 2019 for BTC) [S]. Oct 2024: unless a recession is imminent, the long end and the dollar rally after the first cut [S].
- *Check [I]:* after the Fed's first cut on 18 Sep 2024, the 10Y rose from about 3.6% to about 4.8% by mid-Jan 2025 and the DXY from about 100 to about 110. This matches his call, though BTC also rallied to $100k+, which shows the claim is about yields and the dollar, not BTC.
- *Counter-cases [I]:* 1995 and 1998 cuts without a recession were bullish for equities. 2019 was bullish for stocks but not for BTC after June 2019.

**T7. Unemployment-led recession playbook (Sahm, un-inversion, "non-linear" rise).**
- *His framing:* unemployment bottoms first and then rises non-linearly; the Sahm rule triggers; the curve un-inverts (bull steepens) as the Fed cuts; the recession is dated late; equities and crypto bottom *during* the recession; unemployment peaks after the market low (videos of 14 Jun 2022, 29 Sep 2022, 14 May 2023, 3 Aug 2024, 12 Jan 2026 [S]). In 2026: "once unemployment begins its nonlinear uptrend, recession typically follows" (27 Mar 2026 [S]). Asset prices must fall first to trigger broad layoffs (8 May 2026 [S]).
- *Check:* the Sahm rule triggered in Aug 2024 (4.3%) without an NBER recession as of Oct 2026. Unemployment peaked at 4.6% in Nov 2025 and fell back to 4.1–4.3% through Mar–Sep 2026 (BLS [V]). He expected a recession "late 2023 or early 2024, likely mild" (13 Apr 2023 [S]); none came.

**T8. The 2019 analog.**
- *His framing:* 2019 = rally on apathy, BTC top in June 2019 about 2 months before QT ended (Aug 2019), no alt season, lower highs into 2020. 2025 = top on apathy on 6 Oct 2025, about 2 months before QT ended on 1 Dec 2025 (Bankless; "Bitcoin and the End of QT" 1 Dec 2025 [S]; Q1 2026 memo [V]). He applied it to summer 2024 (lower highs and lows, rising dominance) and to 2026 ("Bitcoin could continue bleeding for months even after QT ends", Cointelegraph [S]). In July 2026 he noted the 2019 path had passed its day-261 low "without the flush that ended the 2019 episode" (the March 2020 COVID crash) [V].
- *Critique [I]:* the analogy fit 2025's top well. As a bottom template it needs an exogenous shock that may not come.

**T9. Midterm year / presidential cycle; the "window of weakness".**
- *His framing:* "The midterm year is typically the worst year. Buying from mid-to-late midterm year is historically a good time to accumulate" (Bankless [S]). 2026 path: a February low, a March pop (~2–5 Mar), April–June weakness, a July rally, a weak Aug–Sep, and a Q4 low. "Investors historically have done better fading Bitcoin in the first half of midterm years and looking for deals in the second half" (29 May 2026 [S]).
- *What happened in 2026:* low on 5–6 Feb (~$60k); a March rally rejected; 200D rejection in May; 200W tag on 5 Jun; low on 30 Jun (≈$57.7k intraday / $58.6k close per 24/7 Wall St.; "just below $59,000" per CoinDesk); then a rally to ≈$85–86k by 6 Oct (above the May high and the 50W) [V/S].
- He admitted the rally was stronger than in prior midterms ("about 50% vs roughly 40% in 2018/2022"; a higher high, not a lower high) and said the "burden of proof has shifted to the bears" (Sep 2026 [S]). He reverted to a bearish Q4 roadmap on 24–26 Oct 2026 [S].

**T10. 1990s analogies (1996–2000, 1997, 1998), not 1995.**
- *Found:* S&P/M2 "resembles the 1996–2000 pattern", meaning about one more year of upside (Bankless Dec 2025 [S]). The 1998 analog for a 20% S&P drop followed by new highs (8 Apr and 3 Jul 2025 [S]). A March 1997 single hike followed by an 18-month hold, applied to Sep 2026 (CMC Academy [S]). The Nasdaq 1999 / QQQ analog for the ETF era (2024–25 [S]).
- *Not found:* a Cowen "1995 soft landing" thesis. Searches turned up no Cowen video or quote built on 1995; the 1995 soft landing is other analysts' framing [S]. Course writers should not attribute "1995" to him without a source.

**T11. Inflation waves (1970s) → energy shock → the Fed's "checkmate" (2026).**
- *His framing:* 1970s-style recurring waves are a risk but not his base case (2022–2025, Benzinga [S]). 2026: supply-driven inflation (oil, the Iran war, Hormuz) plus a softening labor market means the Fed "can't cut, can't hike aggressively". He called this a "checkmate" that typically ends business cycles ("Inflation Soars to 3.3%" 10 Apr 2026 [S]; May 2026 memo [V]). "Oil spikes precede recessions" (28 Feb 2026 [S]).

**T12. Late business cycle and the risk cascade (2026 core framework).**
- *His framing:* "crypto speculation unwinds first → risk spreads to equities (stocks weaken vs gold) → dollar and oil tighten conditions → the labor market is the final stage" (March 2026 memo [V]). Expected order of declines: altcoins, then BTC, then equities, with energy last (25 Feb 2026 [S]).
- *Base case (Aug 2026):* a late-cycle expansion with a midterm correction (65%), a policy-error correction (20%), a recessionary transition (15%) [V]. End of the cycle "plausibly one to two years away" (May 2026 memo [V]).

**T13. Logarithmic regression fair value and bands.**
- Price oscillates around a log-time fair-value line, with tops in compressing upper bands and bottoms near or below fair value. It runs in the "Beauty of Mathematics" monthly series from 2020 to 2026, applied to BTC, ETH and total market cap [S]. ITC now labels the classic regression charts "(Legacy)" and promotes the quantile fan [V].

**T14. Bull Market Support Band as the bull/bear switch.**
- "A bear market for Bitcoin is weekly closes below the 20-week SMA" (22 Jun 2021 [S]). Systematic rejections at the band are a red flag (7 Mar 2022 [S]). In bear markets BTC rallies to the band or to the 50W and fails, e.g. "Bitcoin historically rallies to the 50-week moving average to confirm a bear market" (Bankless [S]).
- 2026: the band was resistance at ≈$82–83k in Apr–May; BTC lost it on 28 May / 1 Jun; it was regained in Sep–Oct; on 22 Oct 2026 "Bitcoin breaks $82K support" [S/V].

**T15. The 200-week SMA as the midterm-year accumulation zone ("a date with destiny").**
- Dec 2025: "Accumulation for BTC in the midterm year is typically near the 200-week moving average", estimated at $60–70k (Bankless [S]). It was tagged on 5 Jun 2026, and price broke below and reclaimed it in June–July 2026 (memo [V]).

**T16. Risk metric and dynamic DCA.**
- In use since 2019. Accumulate at low risk (0–0.2), scale out at 0.8–1. "High-risk levels are historically rare and brief" (6 Jun 2024 [S]). In 2026 risk sat "in the low zone historically associated with accumulation" (Jul 2026 memo [V]).
- *Course caution:* the formula is proprietary. Explain the concept (normalized, de-trended price oscillator on a log scale) without copying it.

**T17. Social risk, apathy, and "retail never returned".**
- See 1.12. Key dated lines: social risk was in downtrend from May 2021 (Jun 2023 [S]); "Why Retail Never Returned" (24 Apr 2025); crypto a "ghost town" at about 16% of 2021 social interest (13 Jan 2026 [S]); "topping on apathy doesn't mean you don't have a bear market" (May 2026, 24/7 Wall St. [S]).

**T18. Seasonality: September, the summer lull, the post-halving September dip then a Q4 top.**
- "The Pattern That Historically Ended The Bull Market" (12 Aug 2025): July–Aug up, Sept pullback to the BMSB, Q4 top. In 2025 BTC dipped in late Sep, made a new ATH on 6 Oct, and then crashed from 10 Oct. That was a correct call [S/V].

**T19. The dollar.**
- Strong-dollar regimes hurt alts. DXY channel analysis. "The DXY collapsed after a predicted rally following rate cuts" (Jul 2025 [S]). In 2026 a firmer dollar (higher lows since February) fed the "triple squeeze" [V]. In Sept 2026 BTC rose *with* the dollar, and he said "something clearly changed" [S].

**T20. Stablecoin dominance "unfortunate pattern" (2026).**
- USDT+USDC dominance broke out of a base and pulled back, like earlier BTC.D, palladium and HSI breakouts, which implies crypto downside. Target 14–15% later in 2026 (7 Jan, 18 Mar, 20 May 2026 [S]).

**T21. Gold and the S&P/gold ratio; the "rotation trap".**
- See 1.7. Jan 2026: S&P/gold near the 1.4 line that preceded 1973 and 2008 declines. "Don't sell winners to buy losers" [S]. Gold peaked near $5,560 in late Jan 2026 and fell about 30% by late March ("Gold Drops Nearly 30%" 23 Mar 2026 [S]). The June low was about $3,970 [V].

**T22. Narratives follow price; "Bitcoin is not the economy"; patience over prediction.**
- "Market narratives follow price action, not the other way around" (4 Nov 2025 [S]). ETF and treasury-company narratives are "unreliable timing tools" (10 Mar 2026 [S]). Short-term prediction is "comparable to random walk physics" (8 Jan 2026 [S]).

**T23. Rate hikes are not immediately bearish (2022), contradicted by his own call (2026), and then reaffirmed.**
- Feb 2022: "Interest Rate Hike Not Necessarily Doom and Gloom" (Daily Hodl [S]). Sep 2026: he expected a hike to be bearish via the dollar, then recanted: "None of the data suggests that a rate hike has ever been immediately bearish for Bitcoin" [S]. He then cited a March 1997-style single hike [S].

---

## 3. His calls and track record, 2021 – Oct 2026

Verdicts: **Hit**, **Partial**, **Miss**, **Open** (unresolved). Outcomes use [V] market data where available. This list is not exhaustive. It covers his most widely reported, checkable calls.

| # | Date of call | Call (his framing) | What happened | Verdict |
|---|---|---|---|---|
| 1 | Feb 2021 | Total crypto market cap "not close to a cycle peak" (log regression) [S] | The market rose further and peaked in Nov 2021 (BTC $69k, 10 Nov 2021) | Hit |
| 2 | Jul–Dec 2021 | Lengthening cycles: the top likely after 2021, "re-accumulation" (Nov 23), no parabolic Q4 [S] | BTC topped 10 Nov 2021 and fell 77% to Nov 2022 | Miss |
| 3 | Dec 2021–Jan 2022 | Below the BMSB = bear; the "hold the line" test at ~$40k [S] | BTC lost $40k (Jan 2022), and the bear was confirmed | Hit on the bear signal; Miss on the hold-the-line conjecture |
| 4 | Mar–Jun 2022 | Downside to the 200W SMA ≈ $20k, which matches "non-bubble" fair value [S] | BTC fell to $17.6k (Jun 2022) and $15.5k (Nov 2022) | Hit (went slightly deeper) |
| 5 | 2022–2023 | BTC dominance would bottom and trend up (charts with and without stables) [S] | BTC.D rose from ~39–40% (late 2022) to 60% (Oct 2024) | Hit |
| 6 | Jan 2023 | 2023 = "recovery year": choppy, half green and half red months, ATHs only in 2024–25 [S] | BTC +155% in 2023; ATH Mar 2024 | Partial (the timing was right, but 2023 was stronger than "choppy") |
| 7 | Apr 2023 / Dec 2023 | US recession "late 2023 or early 2024, likely mild"; inverted curve "most elevated risk" [S] | No NBER recession through Oct 2026 | Miss |
| 8 | Sep 2023 | Pre-halving-year pullback toward ~$23k [S] | Sept 2023 low ≈ $24.9k, then a rally | Partial |
| 9 | 2023–Aug 2024 | BTC.D to 60%, timed for "end of summer/Sept" (May 2024) and "Sept or Dec" (Aug 2024) [S] | It reached 60% on 30 Oct 2024 [S] | Hit (the level was exact; the timing was close) |
| 10 | Sep–Oct 2024 | After the first cut, absent a recession, the 10Y and the dollar rally [S] | 10Y ~3.6% → ~4.8%, DXY ~100 → ~110 (Sep 2024–Jan 2025) [I] | Hit |
| 11 | Nov 2024 | BTC.D will "go down in 2025"; Fed QT → QE in 2025 [S] | BTC.D rose to about 65–66% by mid-2025. QT ended Dec 2025 with no QE | Miss (he revised to 66% in Feb 2025) |
| 12 | Feb–Apr 2025 | BTC.D to 66%; ETH "going home" to $1,500–1,600 [S] | BTC.D broke 65% (6 May 2025), with a cycle high in June. ETH low ≈ $1,386 on 9 Apr 2025 | Hit |
| 13 | 2024–2025 | No alt season while QT continues and social risk is low; alts/BTC ratio toward 0.25 [S] | No broad alt season. Alts/BTC 0.29 (Oct 2025), alts at 2022 lows by Feb 2026 | Hit |
| 14 | Apr–Jul 2025 | ETH/BTC bottomed; he bought ETH ("Butterfly effect"); ETH/BTC to rise [S] | ETH rose ~3.5× from $1,386 to its ATH of ~$4,950 on 24 Aug 2025; ETH/BTC rose to roughly 0.04 [I] | Hit |
| 15 | Jan–Aug 2025 | Post-halving year: cycle top in Q4 2025, a Sept dip to the BMSB first, then a Q4 high [S] | ATH ≈ $126.1k on 6 Oct 2025; 10 Oct liquidation cascade (>$19B); bear from Nov 2025 | Hit |
| 16 | Aug–Oct 2025 | "Final rotation": BTC.D up into Sep–Oct, alts underperform [S] | Alts fell hardest in the 10 Oct 2025 crash; alts/BTC 0.29 on 14 Oct | Hit |
| 17 | Nov–Dec 2025 | Bear market. BTC rallies to the 50W (~$100–102k) as a lower high in early 2026. Lows "60–70K by May/June 2026", and an October 2026 bottom if Oct 2025 was the top [S] | No rally to $100k; BTC crashed to ~$60k on 5–6 Feb 2026 and ~$57.7–59k on 30 Jun 2026 | Partial (the bear and the level were right; the expected rally to the 50W didn't happen; the low came earlier than the October base case) |
| 18 | Dec 2025 | Powell won't cut aggressively before leaving; macro headwinds through summer 2026 [S] | No cuts in 2026; Powell's last meeting 29 Apr; a hike in Sep 2026 | Hit |
| 19 | Jan–Feb 2026 | Midterm template: Feb low, early-March rally rejected ("simulation confirmed", 9 Mar 2026) [S] | Feb 5–6 low; early-March bounce faded; lower prices into June | Hit |
| 20 | Feb 2026 | S&P 500 ~10% correction coming ("Stocks to 10% Drop Soon?" 3 Feb 2026) [S] | S&P fell ~9% into late March 2026, then made new highs (≈7,786 in Aug 2026) | Hit on the correction; the bigger drop expected later did not come by Oct |
| 21 | Jan 2026 | Gold/stocks: don't rotate out of gold; S&P/gold breakdown risk [S] | Gold peaked in late Jan (~$5,560), then fell ~30%; S&P hit records | Miss on the near term (the call came at gold's peak) |
| 22 | Mar–May 2026 | Stablecoin dominance to 14–15% later in 2026 (bearish crypto) [S] | Not verified. BTC rallied Jul–Oct | Open / unverified |
| 23 | May–Jul 2026 | Base case: final BTC low in Q4 2026 (October), possibly via the realized price ~$53k; "reset completed through time" [S/V] | The 30 Jun low (~$57.7k) held through 30 Oct; BTC rallied to ~$85k (6 Oct), then fell to ~$78k (30 Oct) | Open (Q4 runs to 31 Dec) |
| 24 | Aug 2026 | 65% late-cycle expansion with a midterm correction; BTC to form its low *during* the equity correction; BTC "bottom-watch" near $63k [V] | No equity correction of note by late Oct; BTC rallied without one | Open |
| 25 | Sep 2026 (before the FOMC) | The Fed "really should" hike; the hike → stronger dollar → BTC lower [S] | The Fed hiked to 3.75–4.00% on 16 Sep; the dollar rose but BTC rallied (~$63k → ~$83k). He conceded the thesis was "not rooted in the data" [S] | Miss (he admitted it publicly) |
| 26 | 24–26 Oct 2026 | Bearish Q4 roadmap: weekly close < $83k ✔; fakeout ✔ (25 Oct); Fed doesn't hike (28 Oct); hot PCE (29 Oct); oil ~$120 (Iran war); 10Y back to 5.3%; then stocks and BTC drop in Q4; void above $83k [S] | The Fed held on 28 Oct (3.75–4.00%), so step 3 ✔ per Benzinga [S]. BTC < $80k; ~$78k on 30 Oct. Brent $116.72 on 23 Oct [S] | Open |
| 27 | Sep 2026 | 65% odds the cycle low is still ahead; "If no lower low through October, odds shift to bulls"; expects to "be a bull again going into 2027" [S] | No lower low as of 30 Oct 2026 | Open; by his own time test, it is leaning toward the bulls |

**Fair summary [I]:**
- His strongest record is *crypto-internal, relative* calls: BTC dominance, alts bleeding vs BTC, the ETH/BTC bottom, and fading alt season. Cycle timing of tops also scored well (2025 Q4 top), and so did knowing when a bear is confirmed (BMSB, 50W).
- His weakest record is *macro-economic* calls: the US recession expected in 2023–24 did not come, and the 2026 rate-hike thesis failed. *Exact timing of bottoms* is also weak: the 2026 low came earlier than his October base case, and the lengthening-cycle theory failed in 2021.
- He publicly revises and admits misses (LCT abandoned; Sept 2026 "not rooted in the data"). He often hedges with probabilities and explicit invalidation levels ("void above $83k").

---

## 4. Markets and macro, Jan 2025 → 30 Oct 2026 (current-state context he discussed)

### 4.1 Fed and liquidity
| Date | Event | Source |
|---|---|---|
| Dec 2024 → Jul 2025 | Fed funds held at 4.25–4.50% (Cowen video "The Fed Holds Interest Rates at 4.5%", 31 Jul 2025) | [S] |
| 19 Mar 2025 | QT slowed (Treasury redemption cap cut) | "The Fed Slows Quantitative Tightening" [S] |
| 17 Sep 2025 | Cut 25 bp to 4.00–4.25% | [S/I] |
| 29 Oct 2025 | Cut to 3.75–4.00%; QT to end on 1 Dec 2025 | Cowen video 30 Oct 2025 [S]; HSBC FX note [S] |
| 1 Dec 2025 | QT ends | iTrustCapital / E*Trade notes [S] |
| 10 Dec 2025 | Cut to 3.50–3.75% (third cut of 2025), with dissents both ways; reserve-management purchases begin | ACBS / E*Trade [S] |
| 12 Jan 2026 | DOJ criminal probe of Powell reported; Cowen: "A Line Has Been Crossed" | [S] |
| Jan, Mar, Apr 2026 | Holds at 3.50–3.75%. 29 Apr = Powell's last meeting as chair | Trading Economics / CNBC via search [S]; Cowen videos [S] |
| 15 May 2026 | Powell steps down as chair; Kevin Warsh succeeds | Cowen video [S] |
| 17 Jun 2026 | Warsh's first meeting: hold 12–0; easing-bias language removed; median dot implies a hike | Chase, StockTitan [S] |
| 29 Jul 2026 | Hold (fifth in a row); 3 dissents for a hike | Yahoo / Chase [S] |
| Aug 2026 | Treasury expands its bond-buyback program; BTC jumps from ~$64k toward ~$80k | CoinDesk 6 Oct 2026 [S] |
| 16 Sep 2026 | **Hike 25 bp to 3.75–4.00%**, vote 12–0; first hike since 2023; median sees one more 2026 hike (~4.1%) | Federal Reserve statement PDF; CNBC [V] |
| 28 Oct 2026 | Hold at 3.75–4.00%. Reports differ on dissents (2 vs 3, some for a hike). Warsh signals fewer meetings in future years and no forward guidance absent a crisis | CNBC recap; Benzinga [S] |

### 4.2 Inflation, labor, growth
- **CPI YoY (from Cowen's monthly video titles [S]):** Jan 2025 3.0%; Mar 2.4%; Apr 2.3%; May 2.4%; Aug 2.9%; Sep 3.0%; Nov 2.7%. Mar 2026 3.3% ("Inflation Soars", energy); Apr 2026 3.8%; Jul 2026 3.4% (Aug memo [V]). Aug 2026 PCE 3.4% headline / 3.0% core (Sep memo [V]).
- **Unemployment U-3:** Jan 2025 4.0%; Apr–May 4.2%; Jun 4.1%; Jul 4.2%; Aug 4.3%; Sep 4.4%; Oct missing (shutdown); **Nov 4.6% (cycle high, highest since 2021; later revised to 4.5% per one source)**; Dec 4.4%; Jan 2026 4.3%; Apr 4.3%; Jul 4.1%; Aug 4.1%; **Sep 2026 4.2%**, with payrolls +29k (forecast ~84k), August revised to 133k, average of 68k/month through September 2026 (BLS TED 2026 [V]; Cowen video titles [S]).
- **Recession status:** no NBER recession as of Oct 2026. ITC macro recession composite 0.024 in Aug 2026 [V].
- **Oil:** Brent ~$72 before the US/Israel strikes on Iran (28 Feb 2026). WTI $67 → $91 in one week (early Mar 2026). Brent near $120 at the spring peak; $118.03 on 29 Apr. $69.63 on 24 Jun after a June 17 Hormuz MoU. Back above $100 on 23 Jul after strikes resumed on 7 Jul. Front-month peak $109 on 15 Sep (spot ~$132). $116.72 on 23 Oct (CNBC, EIA, Admiral Markets, Wikipedia oil chronology [S]).
- **Yields and dollar:** 10Y 5.10% on 15 Oct 2026 (FRED, per BeInCrypto [S]); ~5.29% in late Sep 2026 (highest since 2007); 30Y ~5.64–5.7% (highest since 2002); 2Y ~4.89%; DXY ~101.35 with higher lows since Feb 2026, July high ~101.8 (Sep 2026 memo [V]; CoinDesk [S]).
- **Equities:** S&P fell ~20% into 8 Apr 2025 (tariffs), then recovered to new highs. In 2026 a ~9–10% correction ran Feb → late Mar, then records: ~7,786 in mid-Aug, ~7,710 in late Sep (Aug and Sep memos [V]). Breadth was weak: ~48% of members above their 200-day; S&P 600 down ~9% from its mid-Aug high (Sep memo [V]). Shiller CAPE 41.2 (Aug 2026 [V]). Dow 50,000 (Feb 2026, Cowen title [S]).
- **Metals:**
  - Gold: $3,300 (Apr 2025), $3,600 (Sep), $3,900 (6 Oct), $4,200 (16 Oct 2025), >$4,800 (21 Jan 2026), then a ~$5,560 peak in late Jan 2026. It fell ~30% by late Mar, hit a ~$3,970 late-Jun low, and stood at ~$4,210–4,370 in Aug–Sep 2026 [V/S].
  - Silver: ATHs Oct–Dec 2025, then −38% by 31 Jan 2026 [S].

### 4.3 Crypto
- **BTC 2025:**
  - New ATH on 21 Jan 2025 (>$100k).
  - Drop below the BMSB in Mar 2025.
  - April 2025 low ~$74–76k (tariff shock) [I/S].
  - New ATH on 21 May 2025.
  - **Cycle ATH ≈ $126.1–126.2k on 6 Oct 2025** [V CoinDesk/24/7].
  - 10 Oct 2025 macro-driven crash with >$19B of derivatives liquidations [V CoinDesk].
  - Lost the 50W SMA on 17 Nov 2025.
  - Low ~$81–82k on 21 Nov 2025, Fear & Greed 11 [S]. November −17.7%.
  - ~$87.5k at the 2026 yearly open (per a Cowen video [S]).
- **BTC 2026:**
  - Rally to the 21W EMA (mid-Jan).
  - **Crash to ~$60k on 5–6 Feb 2026** (−52% from the ATH) [S CoinDesk/Backpack].
  - ~$63k on 28 Feb (Iran strikes), then $68k on 1 Mar [V CoinDesk/Boston Globe].
  - March rally rejected.
  - Rally to the bear-market resistance band (~$82–83k) in Apr–May.
  - Rejected at the 200D on 19 May; fell to ~$73k (late May); ~$75.65k on 27 May.
  - Tagged the 200W on 5 Jun; swept the Feb low on 6 Jun.
  - **Cycle low (so far) on 30 Jun 2026: ~$57.7k intraday, ~$58.6k close** [S 24/7 Wall St.; CoinDesk "just below $59,000"].
  - ~$65.3k on 15 Jul (memo [V]); ~$63k in mid-Aug [V]; ~$64k → ~$80k after the Treasury buyback.
  - ~$83k by late Sep, above the May high and the 50W SMA [V memo].
  - **$85,453 on 6 Oct 2026** (−32% YoY) [S CoinDesk].
  - Broke $82k on 22 Oct; weekly close < $83k (25 Oct); < $80k on 24–25 Oct (~$191M of long liquidations).
  - **~$78.0k on 30 Oct 2026**, with total crypto market cap ~$2.67T [S].
- **Realized price:** ~$53–54k (Jun–Sep 2026); **balanced price** ~$37.7–40k [V/S].
- **BTC dominance:** 60% (30 Oct 2024) → >65% (6 May 2025) → cycle high (Jun 2025) → dip in Jul–Aug 2025 (ETH run) → rise in the Sep–Oct 2025 "final rotation". In 2026 it moved between ~58% and ~61% (incl. stables). The 2026 high was ~60.6% on 5 May (CMC per search [S]); ~60.1% on 23–29 Oct; ~58.5% (CoinGecko, 30 Oct) [S]. **Ex-stablecoins ~67%** (Feb and Aug 2026, Cowen [S/V]).
- **ETH:** low ~$1,386 on 9 Apr 2025; ATH ~$4,946–4,955 on 24 Aug 2025 [V]; −30% in Oct 2025 ("Ethereum Drops 30% – Now What?" 12 Oct 2025 [S]); "back home" again in Feb 2026 ("Welcome Back Home, Ethereum!" 9 Feb 2026 [S]); ~$2,363 on 28 Oct and ~$2,232 on 30 Oct 2026 [S]. **ETH/BTC ≈ 0.029** (Oct 2026, computed [I]).
- **Alts:** altcoin market cap / BTC market cap 0.32 (Jun 2025) → 0.29 (Oct 2025) [S]. Alts back at 2022 lows by Feb 2026 [S]. Altcoins fell harder than BTC in Oct 2026 [S].
- **Late Oct 2026 headlines:** a ~$6B Binance hack reported; ~$1.5B of leveraged bets wiped out (CoinDesk headline list [S], not independently verified).

### 4.4 Where Cowen stands as of 30 Oct 2026 [S/V]
- His latest videos (RSS [V]): "Bitcoin Q4 Dump (Live Show!)" (30 Oct); "All of BTC's Prior Major Drops That Marked Market Cycle Bottoms Have Always Occurred.." (29 Oct); "Bitcoin: Post-FOMC" (29 Oct); "Bitcoin: Bears Regaining Control" (25 Oct); "Bitcoin: A Precarious Position" (24 Oct); "Bitcoin Bull Market Support Band" (22 Oct); "Oil Prices Keep Rising, Is a Market Correction Coming" (19 Oct); "What will the Federal Reserve Do Next?" (19 Oct); "Gold: Dubious Speculation" (27 Oct).
- **Stance:** following a bearish Q4 roadmap "until proven wrong (back above $83k)". His support band for BTC is ~$72–76k, and the realized price (~$53k) is the level to watch if a lower low comes. Past midterm BTC lows came with a 10–20% equity drawdown, so he wants to see stocks crack. If no lower low comes by end-Oct or end-year, the bearish case weakens and he "expects to be a bull again going into 2027".

---

## 5. Vocabulary (his recurring phrases and jargon)

| Term | One-line meaning (as he uses it) |
|---|---|
| Risk metric | His 0–1 normalized, de-trended price oscillator for an asset (per denomination: USD, BTC, ETH). 0 = historically cheap, 1 = historically stretched. Not a probability. |
| Risk bands / "time in risk bands" | 0.1-wide buckets of the risk metric, used for DCA in and out. Shows how long price historically stayed in each band. |
| Dynamic DCA | Buying more the lower the risk band (and selling slices as risk rises), instead of a fixed DCA. |
| Total / composite indicator risk | Average of price, on-chain and social risk (each 0–1). |
| On-chain risk | Composite 0–1 of on-chain valuation metrics (MVRV, supply in profit, etc.). |
| Social risk | Composite 0–1 of retail-attention data: YouTube subscribers and views, X followers of analysts, exchanges and L1s, plus (2026) Google Trends and the Coinbase app rank. |
| Macro recession risk | ITC 0–1 score of how "recession-like" US data look (employment, income/product, production, rates). |
| Liquidity risk | ITC 0–1 percentile of how tight US dollar liquidity is (FFR, 2Y, DXY, Δ Fed assets, ΔM2). |
| Logarithmic regression (bands) | A best-fit line of log price vs log time, with bands around it. Upper bands = historical bubble zones. |
| Fair value logarithmic regression | A log regression fitted only to "non-bubble" data, i.e. long-term fair value. |
| "The Beauty of Mathematics" | His monthly series on log-regression / fair-value charts, mostly for total crypto market cap. |
| Asymmetric quantile regression (fan) | 2026 model: separate curvature for upper and lower price quantiles. The upper tail flattens; lower support stays near a power law. |
| Diminishing returns | Each cycle's peak multiple is smaller than the last. |
| Lengthening cycles (LCT) | His 2019–21 theory that cycles get longer. Abandoned after 2021. |
| Four-year cycle | Halving-linked cycle: pre-halving, halving, post-halving (top in Q4), midterm (bear) year. |
| Post-halving year / pre-halving year / halving year / midterm year | Years 1 / 3 / 4 / 2 of the cycle as he labels them (e.g. 2025 / 2023 / 2024 / 2026). |
| Midterm year | The US midterm-election year. Historically BTC's (and the S&P's) weakest year, with the cycle low around Q4. |
| Window of weakness | Seasonal windows in which midterm-year lows tended to occur (Feb, late Mar/Apr, Jun, Sep–Oct). |
| "We live in a simulation" / "Simulation confirmed" | Ironic shorthand for price tracking the historical midterm-year average path. |
| Left-/right-translated cycle | A top that comes early (left) or late (right) relative to the cycle midpoint. |
| Counter-trend rally | A bear-market rally that fails at resistance (BMSB, 200D, 50W). |
| Macro lower high / lower low | Bear-market structure on weekly or monthly charts. |
| Bull Market Support Band (BMSB) | 20-week SMA + 21-week EMA. Above = bull, below = bear. |
| Bear Market Resistance Band | The same band acting as resistance from below during a bear. |
| "A date with destiny" | Price meeting the 200-week SMA (for BTC or the S&P). |
| 20W / 21W / 50W / 100W / 200W / 300W | Weekly moving averages he tracks. In bears the 50W, 100W and 200W are lost in that order. |
| 200D (200-day SMA) | Daily trend line. In bears often rejection resistance. |
| Golden cross / death cross | 50D crossing above / below the 200D. Often a short-term contrarian signal for him ("golden cross dump", "death cross rally"). |
| Pi Cycle top | 111D SMA crossing 2×350D SMA; a historical top marker. |
| Short-term bubble risk | Extension of price above the 20W SMA. |
| Weekly / monthly / 3-day close | Candle close used to confirm breaks. "Closes matter more than wicks." |
| Fakeout | A break above or below a level that quickly reverses (e.g., "fakeout confirmed, Oct 25"). |
| Hold the line | Holding a support level, usually the 20W, in a bull market. |
| Dubious Speculation | His explicitly speculative scenario-video series. |
| "Not financial advice" / "NFA Live" | Disclaimer, and the name of his live shows with Guy (Coin Bureau) and Rob (Digital Asset News). |
| Running ROI / ROI after bottom/halving/peak | Return comparisons between cycles from fixed anchor points. |
| Drawdown from ATH | Percentage below the all-time high. Bears historically bottom at 70–85% for BTC (less each cycle). |
| Realized price / "cost basis of the network" | Realized cap ÷ supply. Every prior bear bottomed below it. |
| Balanced price / terminal price | On-chain price bands: deep-value floor / historical top ceiling. |
| MVRV Z-score | Market vs realized value, standardized. Below 0 = bottoming zone. |
| Supply in profit / loss (crossing) | Share of coins in profit vs loss. A crossing has preceded cycle lows by about 1–4 months. |
| Bitcoin dominance (BTC.D) | BTC market cap ÷ total crypto market cap. He shows it with and without stablecoins. |
| USDT.D / stablecoin dominance | Stablecoins' share of total crypto market cap. Rising = risk-off within crypto. |
| ETH/BTC | Ether priced in bitcoin. His "altcoin index". |
| TOTAL / TOTAL2 / TOTAL3 / OTHERS(.D) | Total crypto cap / ex-BTC / ex-BTC-and-ETH / outside the top 10 (TradingView tickers). ITC has a synthetic "Total Market Cap excl. BTC, ETH, stables". |
| "All bitcoin pairs to range lows" / "alts to 0.25" | Alts must capitulate against BTC (aggregate alt cap ≈ 25% of BTC cap) before an alt season. |
| Alt season | BTC dominance falling while alts rise in USD. Needs looser policy, retail and a euphoric top. |
| Final rotation | Late-cycle return of capital from alts back into BTC (dominance spike). |
| "Oscillators at best, bleeders at worst" | His description of altcoins vs BTC over cycles. |
| "Going home" (ETH) | ETH returning to a prior base ($1,500–1,600 in 2025). |
| Satoshi value | Value measured in BTC rather than USD. |
| Apathy vs euphoria top | Whether the cycle peak came with retail mania (2017, 2021) or without it (2019, 2025). |
| Crypto ghost town | 2026 description of collapsed retail participation. |
| The pivot | The Fed's switch from hiking or holding to cutting, or from QT to QE. |
| QT / QE / QT taper / end of QT | Balance-sheet shrinkage / expansion / slowing the runoff / stopping it (1 Dec 2025). |
| Terminal rate | The peak policy rate of a hiking cycle. BTC has historically bottomed near it. |
| Neutral (rate) | His shorthand for FFR ≈ 2Y yield. Above = restrictive. |
| Liquidity / net liquidity | Central-bank balance sheets minus TGA and RRP (2023 model). More generally, the ease of dollar funding. |
| Accounting for the money supply | Dividing an asset by M2 (or M1) to strip out monetary inflation. |
| Soft / hard / no landing | Slowdown without recession / with recession / no slowdown. |
| Late business cycle | Tight labor turning, high valuations, rising uncertainty. Risk cascades down the curve. |
| ITC business cycle (metric) | S&P 500 adjusted by unemployment², inflation, rates and M2 (his 2026 visualization of cycle extension). |
| Risk cascade / risk curve | Risk leaves in the order alts → BTC → stocks → gold (energy last), and returns in reverse. |
| Checkmate (for the Fed) | Supply-driven inflation plus a weakening labor market: it can't cut and can't hike. |
| Sahm rule | Recession signal: 3-month average unemployment ≥ 0.5 pp above its prior-12-month low. |
| Uninversion / bull steepener / bear steepener | Curve moving back above zero / steepening because short yields fall / steepening because long yields rise. |
| "Good news is bad news" | Strong data raise yields and delay cuts, which hurts risk assets. |
| Main Street vs Wall Street | ISM / real economy vs asset prices. Retail crypto needs Main Street. |
| Rotation trap | Selling outperformers (gold) to buy laggards (stocks or crypto) on a rotation narrative. |
| Bear goggles / realist vs doomer | His terms for bearish bias and for balanced vs catastrophist views. |
| Summer lull / "Wake me up when September ends" | Seasonal weakness of summer and September. |
| Yearly open | The 1 January price, used to compare midterm-year paths (e.g., −15% by early March). |
| Bottom-watch mode | 2026 memo phrase: the framework shifts from confirming the decline to watching for the low. |
| Time-based capitulation | A bear that resets through months of sideways drift rather than a single crash. |
| Roadmap (void above X) | An ordered checklist of expected events with an explicit invalidation level. |

---

## 6. Notes for course designers (coverage check against this inventory) [I]

1. **Must-cover, high weight** (he uses them constantly):
   - Fed funds / FOMC / cuts and pivot, and QT/QE.
   - Unemployment rate (+ Sahm, claims, JOLTS, payrolls and revisions).
   - CPI/PCE/PPI, 10Y and the yield curve (inversion, un-inversion, bull vs bear steepener), the DXY.
   - S&P 500 (+ S&P/M2, S&P/gold), gold and silver, oil.
   - The four-year cycle and midterm seasonality, monthly seasonality.
   - Log regression / fair value, risk-metric concept, BMSB / 50W / 200W / 200D.
   - BTC dominance (with and without stables), ETH/BTC, alt/BTC pairs, stablecoin dominance.
   - Social risk / apathy, realized price, MVRV-Z, supply in profit/loss.
   - The late-business-cycle / risk-cascade framework.
2. **Medium:** M2 and net liquidity, TGA/RRP, real rates, 30Y and term premium, ISM ("Main Street" — explain both his use *and* the competing "ISM → alt season" thesis, which is other analysts'), GDP/GDI, smoothed recession probabilities, CAPE, breadth, correlations, political regimes, Pi Cycle, golden/death crosses, RSI, Fibonacci, terminal and balanced price, Puell/hash ribbons/thermocap, SSR, ETF flows, Fear & Greed.
3. **On his platform but rarely in videos:** credit spreads, NFCI and financial-stress indices, consumer sentiment, housing details, bank lending standards, fiscal deficit. Cover them briefly as "context indicators".
4. **Attribution traps:**
   - "1995 soft landing" is not his. His 1990s analogs are 1996–2000 (S&P/M2), 1997 (one hike, long hold) and 1998 (20% drop then new highs).
   - "ISM above 50 = alt season" is not his.
   - "Lengthening cycles" was his until 2021, but he dropped it.
   - "Rate cuts not bullish at first" is his (2023–24). "Rate hikes not immediately bearish" is also his (Feb 2022 and Sep 2026).
5. **Proprietary content:** describe the risk metric, social risk and ITC business-cycle metric conceptually. Platform help texts are public, but do not copy formulas or paid charts.
6. **Date sensitivity:** his views changed fast in 2026 (bearish Jan–Jun; conceded in Sep; bearish roadmap again in late Oct). Any "Cowen thinks X" sentence in the course must carry a date.

---

## Sources

**Primary (Cowen's own properties)**
- ITC app (public JS bundle; chart catalogue and dashboard help texts), fetched 2026-10-30: https://app.intothecryptoverse.com/ (the extracted list is not published here).
- ITC home page: https://intothecryptoverse.com
- Benjamin Cowen personal site and reports index: https://benjamincowen.com/ ; https://benjamincowen.com/reports
- The Triple Squeeze (30 Sep 2026): https://benjamincowen.com/reports/the-triple-squeeze-september-2026
- The Balance of Risks (15 Aug 2026): https://benjamincowen.com/reports/the-balance-of-risks-august-2026
- Bitcoin Cycle Memo – July 2026: https://benjamincowen.com/reports/bitcoin-cycle-memo-july-2026
- Asymmetric Tail Curvature in Bitcoin Price Quantiles (29 May 2026): https://benjamincowen.com/reports/asymmetric-tail-curvature-in-bitcoin-price-quantiles
- Macro Risk Memo (May 2026): https://benjamincowen.com/reports/macro-risk-memo-may-2026
- Crypto Risk Memo (Q2 2026): https://benjamincowen.com/reports/crypto-risk-memo-q2-2026
- How Risk Cascades Through Markets (Mar 2026): https://benjamincowen.com/reports/how-risk-cascades-through-markets-march-2026
- Macro Risk Memo Feb 2026: https://benjamincowen.com/reports/macro-risk-memo-feb-2026
- Crypto Macro Risk Memo – Q1 2026: https://benjamincowen.com/reports/crypto-macro-risk-memo-q1-2026
- YouTube channel RSS (last 15 uploads to 30 Oct 2026): https://www.youtube.com/feeds/videos.xml?channel_id=UCRvqjQPSeaWn-uEx-w0XOIg
- X posts (text from search snippets; IDs decoded to dates): https://x.com/benjamincowen/status/2019835733503255006 (6 Feb 2026) ; https://x.com/benjamincowen/status/2114535552523612377 (26 Oct 2026)

**Video index with AI summaries (2,385 videos, 2019 → 11 Jun 2026)**
- https://rosetta.to/u/intothecryptoverse (year pages /2019 … /2026) (the extracted dataset is not published here).

**Interviews / media about Cowen**
- Bankless, "Where is Crypto Going in 2026? | Ben Cowen" (23 Dec 2025): https://www.bankless.com/podcast/where-is-crypto-going-in-2026-ben-cowen
- Cointelegraph Magazine, Hall of Flame (19 Nov 2024): https://cointelegraph.com/magazine/bitcoin-dominance-crypto-predictions-bull-run-benjamin-cowen-hall-of-flame/
- Cointelegraph Magazine, "The debate over Bitcoin's four-year cycle is over" (2026): https://cointelegraph.com/magazine/bitcoin-four-year-cycle-dead-debate-bear-market-2026-benjamin-cowen
- Cointelegraph, "Why bitcoin setup looks more like 2019": https://cointelegraph.com/magazine/why-bitcoin-setup-looks-more-like-2019-benjamin-cowen
- CoinMarketCap Academy, "Bitcoin 4-Year Cycle Points to October 2026 Bottom": https://coinmarketcap.com/academy/article/%20bitcoin-4-year-cycle-october-2026
- CoinMarketCap Academy, "Benjamin Cowen Puts 65% Odds on Lower Bitcoin Price Still Ahead": https://coinmarketcap.com/academy/article/benjamin-cowen-puts-65percent-odds-on-lower-bitcoin-price-still-ahead
- 24/7 Wall St., "Did Benjamin Cowen Predict the Bitcoin Bottom Correctly?" (6 Oct 2026): https://247wallst.com/investing/cryptocurrency/2026/10/06/benjamin-cowen-said-the-cycle-would-bottom-bitcoin-near-60000-in-october-did-benjamin-cowen-predict-the-bitcoin-bottom-correctly/
- Benzinga via TradingView, "Bitcoin Analyst Admits His Rate-Hike Thesis 'Was Not Rooted in the Data'" (Sep 2026): https://www.tradingview.com/news/benzinga:45b48150d094b:0-bitcoin-analyst-admits-his-rate-hike-thesis-was-not-rooted-in-the-data/
- Benzinga, "Bitcoin Falls as Analyst Says the Fed 'Really Should' Raise Rates": https://www.benzinga.com/crypto/cryptocurrency/26/09/61640748/bitcoin-falls-as-analyst-says-the-fed-really-should-raise-rates-this-month
- Benzinga, "Bitcoin Drops to $80,000 After Fed Meeting: Is the Bear Thesis Playing Out?": https://www.benzinga.com/crypto/cryptocurrency/26/10/62696461/bitcoin-drops-to-80000-after-fed-meeting-is-the-bear-thesis-playing-out
- BeInCrypto via Yahoo Finance, "Bitcoin Falls Below $80,000: Is Benjamin Cowen's Bearish Q4 Roadmap Playing Out?" (26 Oct 2026): https://finance.yahoo.com/markets/crypto/articles/bitcoin-falls-below-80-000-032051576.html
- BeInCrypto, "Benjamin Cowen's Midterm Cycle Thesis…": https://beincrypto.com/cowen-bitcoin-cycle-accumulation-stage/ ; "New Memo Points to Q4 Bitcoin Bottom Near $44,000": https://beincrypto.com/benjamin-cowen-memo-q4-bitcoin-bottom/ (snippets only; site returned 403)
- Benzinga, "Bitcoin Market Dominance … Will Peak At 60% Until December" (Aug 2024): https://benzinga.com/markets/cryptocurrency/24/08/40402971/bitcoin-market-dominance-in-final-stretch-will-peak-at-60-until-december-analyst-says
- Benzinga, "Federal Reserve Cuts Interest Rates—Bitcoin Dominance May Rise" (Nov 2024): https://www.benzinga.com/markets/cryptocurrency/24/11/41850110/federal-reserve-cuts-interest-ratesbitcoin-dominance-may-rise-as-a-result
- Benzinga, "Could Inflation, Unemployment Derail The Bitcoin Bull Run?" (Feb 2025): https://benzinga.com/markets/cryptocurrency/25/02/43706856/could-inflation-unemployment-derail-the-bitcoin-bull-run
- Benzinga, "Here's Why 'Altcoin Season' … Has Not Happened Yet" (Jul 2025): https://www.benzinga.com/crypto/cryptocurrency/25/07/46217148/heres-why-altcoin-season-for-xrp-eth-sol-has-not-happened-yet
- Daily Hodl, "Interest Rate Hike Not Necessarily Doom and Gloom…" (28 Feb 2022): https://dailyhodl.com/2022/02/28/interest-rate-hike-not-necessarily-doom-and-gloom-for-bitcoin-btc-says-analyst-benjamin-cowen-heres-why/
- Coin Edition, "Yield Curve Inversion Raises Serious Recession Fears": https://coinedition.com/yield-curve-inversion-raises-serious-recession-fears-analyst/
- The Informer Post (aggregates Cowen video quotes): https://theinformerpost.beehiiv.com/p/fed-rate-cuts-may-not-be-bullish-for-bitcoin-says-crypto-analyst-benjamin-cowen-heres-why ; https://theinformerpost.beehiiv.com/p/crypto-analyst-benjamin-cowen-says-fed-pivot-and-altcoin-rallies-wont-happen-until-this-occurs
- Cointelegraph, ISM PMI and the bitcoin cycle (Feb 2026): https://cointelegraph.com/news/ism-manufacturing-pmi-bitcoin-cycle-extended
- TradingView community "Cowen Corridor" re-creation: https://www.tradingview.com/scripts/cowen/

**Market and macro data**
- Federal Reserve FOMC statement, 16 Sep 2026: https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf
- CNBC, Fed rate decision Sep 2026: https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html ; Oct 2026 recap: https://www.cnbc.com/2026/10/28/fed-meeting-today-live-updates.html ; June 2026: https://www.cnbc.com/2026/06/17/fed-interest-rate-decision-june-2026.html
- Chase, Warsh's first meeting (Jun 2026): https://www.chase.com/personal/investments/learning-and-insights/article/kevin-warsh-june-2026-federal-reserve-meeting-key-takeaways ; July 2026: https://www.chase.com/personal/investments/learning-and-insights/article/kevin-warsh-july-2026-federal-reserve-will-deliver-price-stability
- E*Trade, "Fed closes 2025 with cut": https://us.etrade.com/knowledge/library/perspectives/market-happenings/fomc-dec2025-25bps ; ACBS Dec 2025 note: https://acbs.com.vn/en/report/macro-flash-note-december-11-2025-the-fed-cut-rate-by-25bps-while-internal-decision-differed-markets-price-in-02-additional-cuts-totaling-50bps-in-2026
- BLS, unemployment 4.2% in Sep 2026: https://www.bls.gov/opub/ted/2026/unemployment-rate-little-changed-at-4-2-percent-in-september-2026.htm ; Nov 2025 4.6%: https://www.bls.gov/opub/ted/2025/unemployment-rate-4-6-percent-in-november-2025.htm
- St. Louis Fed flash report (Oct 2026): https://www.stlouisfed.org/on-the-economy/2026/oct/flash-report-unemployment-rises-slightly-job-growth-slows-september
- CNN, September 2026 jobs: https://www.cnn.com/2026/10/02/economy/us-jobs-report-september-final
- CoinDesk, a year after the record high (6 Oct 2026): https://www.coindesk.com/markets/2026/10/06/from-retail-leverage-to-etf-flows-a-year-after-its-record-high-bitcoin-is-down-just-32
- CoinDesk, BTC slides under $64k on Iran strikes (28 Feb 2026): https://www.coindesk.com/markets/2026/02/28/bitcoin-slides-under-usd64-000-as-u-s-and-israel-launch-strikes-on-iran
- Boston Globe (28 Feb 2026): https://www.bostonglobe.com/2026/02/28/business/bitcoin-slides-below-64000-after-us-and-israel-strikes-on-iran/
- Backpack, "Bitcoin Crash 2026": https://learn.backpack.exchange/articles/bitcoin-crash
- CNBC, oil timeline (21 Apr 2026): https://www.cnbc.com/2026/04/21/oil-price-iran-war-middle-east.html ; EIA Q3 2026: https://www.eia.gov/todayinenergy/detail.php?id=68245 ; Wikipedia oil chronology: https://en.wikipedia.org/wiki/2026%E2%80%932028_world_oil_market_chronology ; Admiral Markets Brent: https://admiralmarkets.com/analytics/traders-blog/brent-crude-oil-price-iran-war ; Al Jazeera (28 Sep 2026): https://www.aljazeera.com/economy/2026/9/28/oil-prices-surge-after-trump-rejects-irans-plan-to-reopen-strait-of-hormuz
- CNBC, ETH record near $5,000 (24 Aug 2025): https://www.cnbc.com/2025/08/24/crypto-market-today.html ; Coinbase ETH: https://www.coinbase.com/price/ethereum
- Fortune BTC price, 28–29 Oct 2026: https://fortune.com/article/price-of-bitcoin-10-28-2026/ ; https://fortune.com/article/price-of-bitcoin-10-29-2026/
- Coingabbar, 30 Oct 2026 market: https://www.coingabbar.com/en/crypto-news-today-bitcoin-ethereum-price-falls-binance-hacked
- Cryptonomist, BTC dominance 60% (24 Oct 2026): https://en.cryptonomist.ch/2026/10/24/bitcoin-dominance-crypto-market-2/
