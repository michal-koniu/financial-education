# Cluster B: the Fed, interest rates, the bond market, inflation and labor

Research file for the course "practical-macro-economy". Compiled 2026-10-30.

**Claim markers.** [V] means verified from a primary or reputable source, with the URL in Sources. [S] means secondary, a snippet, or a well-known figure I did not re-fetch. [I] means my own inference or calculation.

**Data provenance.** Every US number for 2024-2026 below was downloaded on 2026-10-30 from FRED's CSV endpoint (`fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`). Unless noted, I computed year-over-year (YoY) and month-over-month (MoM) changes from seasonally adjusted (SA) index levels [V/I]. SA YoY can differ from the headline non-seasonally-adjusted (NSA) number BLS prints by about 0.1 pp. The historical cycle tables use FRED monthly averages and Shiller's monthly S&P 500 averages (datasets/s-and-p-500 on GitHub). Monthly averages blunt crashes such as March 2020, so treat those returns as approximate. Where a daily close is quoted, it comes from FRED `SP500` (2016 onwards) or is marked [S].

---

## 0. Snapshot: where things stand, late October 2026

| Indicator | Latest | Date | One year earlier (approx.) | Series / ticker |
|---|---|---|---|---|
| Fed funds target range | **3.75-4.00%** | hiked Sep 16, 2026; held Oct 28, 2026 (10-2, two dissents for a hike) | 3.75-4.00% (after Oct 29, 2025 cut) | DFEDTARL / DFEDTARU |
| Effective fed funds (EFFR) | 3.88% | Oct 28, 2026 | 3.86-3.89% | DFF / EFFR |
| Interest on reserve balances (IORB) | 3.90% | from Sep 17, 2026 | — | IORB |
| 3-month T-bill (constant maturity) | 4.18% | Oct 28 | 3.89% | DGS3MO |
| 2-year Treasury | 4.67% (Sep 2026 high 4.88%, Feb 27 low 3.38%) | Oct 28 | 3.60% | DGS2 / TVC:US02Y |
| 10-year Treasury | 5.05% (Oct 5 close 5.31% = highest close since May 2002) | Oct 28 | 4.11% | DGS10 / TVC:US10Y |
| 30-year Treasury | 5.37% (Oct 7 high 5.67%, highest since Jul 2002) | Oct 28 | 4.67% | DGS30 |
| 10Y-2Y spread | +0.37 pp | Oct 29 | +0.51 | T10Y2Y |
| 10Y-3M spread | +0.80 pp | Oct 29 | +0.22 | T10Y3M |
| 10Y real yield (TIPS) | 2.67% (Sep high 2.93% = highest since Nov 2008) | Oct 28 | 1.81% | DFII10 |
| 10Y breakeven inflation | 2.35% | Oct 29 | 2.30% | T10YIE |
| 5y5y forward inflation | 2.23% | Oct 29 | 2.20% | T5YIFR |
| 10Y term premium (Kim-Wright) | 0.94 pp (Sep 1.08 = highest since Apr 2010) | Oct 23 | 0.50 | THREEFYTP10 |
| High-yield OAS | 3.14 pp | Oct 28 | 2.94 | BAMLH0A0HYM2 |
| Investment-grade OAS | 0.86 pp | Oct 28 | 0.80 | BAMLC0A0CM |
| CPI, headline YoY | 3.7% (May 2026 peak 4.2%) | Sep 2026 | 3.0% | CPIAUCSL |
| CPI, core YoY | 2.6% | Sep 2026 | 3.0% | CPILFESL |
| PCE, headline YoY | 3.65% | Sep 2026 | 2.8% | PCEPI |
| PCE, core YoY (the Fed's gauge) | 3.12% | Sep 2026 | 2.8% | PCEPILFE |
| PPI, final demand YoY | 6.3% | Sep 2026 | 3.0% | PPIFIS |
| Michigan 1-year inflation expectations | 4.6% | Sep 2026 | 4.7% | MICH |
| Unemployment rate (U-3) | 4.2% (cycle high 4.5%, Nov 2025) | Sep 2026 | 4.4% | UNRATE |
| U-6 | 7.6% (high 8.7%, Nov 2025) | Sep 2026 | 8.1% | U6RATE |
| Sahm rule, real time | 0.00 | Sep 2026 | 0.23 | SAHMREALTIME |
| Nonfarm payrolls, monthly change | +29k; 2026 year to date ~+612k, about 68k/month | Sep 2026 | — | PAYEMS |
| Initial jobless claims | 194k | week of Oct 24 | ~220-230k [S] | ICSA |
| Continuing claims | 1.70M | week of Oct 17 | ~1.9M [S] | CCSA |
| JOLTS job openings | 7.08M | Aug 2026 | 7.2M | JTSJOL |
| Quits rate | 1.9% | Aug 2026 | 1.9-2.0% | JTSQUR |
| Participation rate | 61.8% | Sep 2026 | 62.5% | CIVPART |
| Fed balance sheet | $6.75T (QT ended Dec 1, 2025; low $6.57T in Nov 2025) | Oct 28 | $6.57T | WALCL |
| Brent crude | ~$123/bbl (Oct average $125; Apr 2026 high $138) | late Oct | ~$62-65 | DCOILBRENTEU |
| S&P 500 | 7,744 (all-time high 7,819 on Oct 6, 2026) | Oct 28 | 6,891 | SP500 |

**State of play in one paragraph [V data, I interpretation].** The Fed cut 175 bp between September 2024 and December 2025, to 3.50-3.75%. It then paused through mid-2026. On September 16, 2026, under new Chair **Kevin Warsh**, it **hiked** 25 bp to 3.75-4.00%, the first hike since July 2023. The cause was an **energy supply shock**: the 2026 Iran war closed the Strait of Hormuz from about late February/March 2026, and Brent went from about $71 in February to $117 average in April and about $125 in October. That shock pushed headline CPI from 2.4% (Jan-Feb 2026) to 4.2% (May) and 3.7% (Sep), and core PCE above 3%. The labor market looks *stable-to-firm by the cycle's own standards*. Unemployment peaked at 4.5% in November 2025 and is now 4.2%. Claims are near multi-decade lows, and the Sahm rule reads 0.00. Hiring is slow, though: payrolls average about 68k/month in 2026, quits sit at 1.9%, and participation is falling.

The curve tells a 2026-specific story. The 2Y rose about 130 bp from its February low, more than the 10Y (+108 bp), so 10Y-2Y has **bear-flattened** from +0.74 (Jan 30) to +0.37. Measured against 3-month bills, which are pinned by policy, the curve is +0.80 and positive. The 2Y now trades about 80 bp **above** effective fed funds, which is the market pricing more hikes. CME FedWatch put the odds of a December 2026 hike at about 83% after the October 28 meeting [S].

There is no recession as of October 2026. That makes the 2022-24 inversion, which began in July 2022 (2s10s) and October 2022 (3m10y), the longest-dated "unfulfilled" inversion signal on record.

---

## 1. How Benjamin Cowen frames this cluster

Recurring claims, with evidence where I could find it. Cowen publishes almost daily, so these are recurring themes, not a full catalogue.

1. **"The Fed chases the 2-year."** The 2-year yield is the market's forecast of the policy path. When the 2Y drops below fed funds the Fed eventually cuts, and when it rises above, hikes come into play. He also uses the fed-funds-minus-2Y gap as a rough proxy for "how restrictive vs. neutral" policy is. In the December 2025 Bankless episode, with fed funds about 3.75% and the 2Y about 3.5%, he said the Fed "need[s] one more rate cut just to get to the point where you could argue we're at neutral" [S, Bankless page summary]. In April 2026 ("FOMC: The End of an Era") his base case was "the Fed ends up cutting rates to chase the 2-year yield" [S, Rosetta transcript summary].
2. **The late-cycle sequence.** Hiring and openings fall first, then layoffs and claims rise, then unemployment rises. The Fed cuts "for the wrong reasons" and stocks fall. He also argues that a falling stock market is itself what tips the labor market: "It's the stock market going down that leads to the recession" (Mar 27, 2026, "Bitcoin in a Late Business Cycle Environment") and "You have to have lower asset prices" (May 8, 2026, "Labor Market Holds Steady") [S, Rosetta].
3. **Initial claims of about 300k as the recession line.** "I do not think the United States is in a recession until we are looking at initial claims printing 300K" (Apr 2026). The same threshold reappears in May 2026 [S, Rosetta]. He also notes the seasonal summer rise in claims seen in 2023-2025.
4. **The unemployment rate versus its moving average.** In a March 3, 2024 thread he said the inverted curve still warranted caution, but unemployment was "still near historic lows" and the 24-month moving-average signal "takes a long time to play out" [S, ThreadReader]. He also described the Sahm rule triggering in a rising number of states, while caveating that the rule was not designed for state-level use [S].
5. **The first cut is not bullish by itself.** Markets topped around the start of cutting cycles in 2000/01 and 2007, and they tend to bottom near the **last** cut, not the first [S, secondary crypto-news coverage, 2024]. He contrasts recessionary cycles (2001, 2007) with soft-landing "insurance" cycles (1995, 1998, 2019).
6. **The yield curve and "recession" Google searches.** "The first peak on google searches for 'recession' tends to occur around the time of yield curve inversion because people think that inversion means 'recession now'. The second peak is when the actual recession arrives" (X post, 2023) [S]. October 2023: "there may be a recession around the corner based on the yield curve" (3m10y inverted since Oct 2022) [S, Coin Edition].
7. **After cuts, the long end can go *up*.** June 2025 X post: "Trump wants Powell to cut rates. But when they cut rates last year, the long end of the yield curve went up" [S, X snippet]. The FRED data back this: the 10Y went from 3.63% (Sep 16, 2024) to 4.58% at end-2024 [V].
8. **The 2019 analog for crypto and QT.** Bitcoin topped on apathy shortly before QT ended, in 2019 and in 2025 (QT ended Dec 1, 2025). A base-building period followed. Crypto is "more sensitive to rate cuts and liquidity than the stock market is" (May 12, 2026, "Inflation Rises to 3.8%") [S, Rosetta]. "Bitcoin ... thrives under looser monetary policy conditions" (Apr 2026) [S].
9. **The 1970s "second wave" risk and the "checkmate" scenario.** A supply-driven energy shock lifts inflation while labor softens, so the Fed cannot defend both mandates: "They can defend one weakness, but if you have two weaknesses, the defense breaks down" and "that's how the Federal Reserve ultimately gets checkmated" (Apr 7 and May 12, 2026). "If inflation were to start another major inflationary wave, that would have negative consequences for the stock market" [S, Rosetta]. Energy "topped after the stock market in a late business cycle environment" [S].
10. **Midterm-year seasonality, applied to yields.** In October 2026 he expected the 10Y to peak before mid-November, citing the 2018 and 2022 midterms, when the 10Y topped between early October and mid-November. He had called 5% a soft target and allowed for 5.4-5.6% (BeInCrypto/Yahoo, Oct 6, 2026) [S]. His August 15, 2026 "Balance of Risks" memo reportedly gave 65% to a midterm correction then recovery, 20% to a policy-error correction, and 15% to a recessionary transition [S, Datawallet profile, low-confidence source].

**Charts he typically shows** [S/I]: fed funds rate with the 2Y overlaid; unemployment rate with recession shading and a 12- or 24-month moving average; 10Y-2Y and 10Y-3M spreads with recession bars; CPI YoY with a 1970s overlay (Burns-era second wave); initial claims; JOLTS components (openings, quits, hires, layoffs); a state-level unemployment "heatmap"; the S&P 500 around rate-cut dates; and the S&P 500 divided by gold and by M2.

**Independent assessment [I].** Points 1, 3 and 7 are well supported by data. Point 2 describes the 1990/2001/2007 template well, but it failed twice in 2024-26: unemployment rose, the Fed cut, and no recession followed. Point 5 is true on average but has a 50/50 split across cycles, and the deciding variable is whether a recession arrives. That is unknowable at the first cut. Point 10 rests on two prior observations (2018, 2022), which is too small a sample to carry weight. Point 9 is the most relevant framework for 2026.

---

## 2. Fed indicators

### 2.1 Federal funds rate: target range, EFFR, IORB
1. **Definition and sources.** The FOMC sets a *target range* 25 bp wide, for example 3.75-4.00%. The **EFFR** is the volume-weighted median rate on overnight unsecured interbank (fed funds) loans. The New York Fed publishes it daily at about 9:00 ET for the prior day. FRED series: `DFEDTARL` / `DFEDTARU` (range), `DFF` (daily EFFR), `FEDFUNDS` (monthly average), `EFFR`. Before December 2008 there was a single target (`DFEDTAR`), and before about 1982 the Fed targeted reserves and money, so "the funds rate" then means the effective rate [V/S]. The rate is administered through **IORB**, currently 3.90%, the **ON RRP** (overnight reverse repo) floor at 3.75%, and the **standing repo facility** ceiling at 4.00% (Sep 16, 2026 implementation note) [V]. TradingView: `FRED:FEDFUNDS`, `ECONOMICS:USINTR`.
2. **How to read it.** The level alone says little. What matters is the level *relative to inflation* (real rate, §2.6), *relative to neutral* (§2.4), and *relative to the 2Y* (market expectations, §3.1). The direction of change, and above all **turning points** (last hike, first cut), drive markets. A common misreading is "rate cuts are bullish." Cuts made because growth is collapsing are not (see §6.1).
3. **Cowen's use.** Fed funds overlaid with the 2Y, which he treats as the lead. Policy is "restrictive" when fed funds sits above the 2Y [S].
4. **Relationships.** The 2Y leads by roughly 0-6 months [I, consistent with 2019, 2024 and 2026]. Unemployment rising off its low tends to lead the first cut by several months: about 6 months in 2007, about 3 in 2019, and about 17 in 2024, counting from the April 2023 low of 3.4% [V/I]. Inflation surprises lead hikes, as in 2022 and Sep 2026.
5. **Assets [I].** Higher real policy rates raise the discount rate and the opportunity cost of holding zero-yield assets (BTC, gold). The usual sign is negative for crypto and long-duration equities and positive for the dollar. The effect is strongest when a move is *unexpected*. Priced-in moves (90% priced before Sep 16, 2026 [S]) have muted announcement-day effects.
6. **Takeaway.** Watch the *direction* of policy and why it is moving, not the level.

### 2.2 FOMC meetings, the statement and the press conference
1. **Schedule and mechanics.** Eight scheduled meetings a year, at roughly six-week intervals. The statement comes out at 2:00 pm ET and the Chair's press conference starts at 2:30 pm ET. **Minutes** follow three weeks later. Voters are the 7 Governors, the New York Fed President, and 4 rotating Reserve Bank presidents (12 in total) [V]. 2026 meetings were Jan 27-28, Mar 17-18, Apr 28-29, Jun 16-17, Jul 28-29, Sep 15-16 and Oct 27-28, with Dec 8-9 still to come [V/S].
2. **Statement style changed under Warsh.** Statements under Chair Warsh, from June 2026, are much shorter ("The Committee will deliver price stability"), drop the familiar risk-balance paragraph, and give no explicit forward guidance [V, statements]. On Oct 28, 2026 Warsh announced that **in 2027 one of the eight meetings will be a "strategy" meeting with no rate vote or statement**, and that in 2028 there will be two strategy meetings and six policy meetings [V, press conference transcript]. He calls his approach "interrogating reality" and says he is "not a data-point-dependent" chair [V].
3. **How to read it.** Read the statement as *changes in wording* relative to the previous one, and pay attention to the **dissents**, which signal where the next move is headed. In 2026 the dissent sequence was Miran wanting cuts (Jan-Apr), then three regional presidents (Hammack, Kashkari, Logan) objecting to an "easing bias" in April, then the same three dissenting **for a hike** in July. The hike came in September. In October, Cook and Hammack dissented for another hike [V]. The trail of hawkish dissents preceded the hike by about two meetings.
4. **Cowen's use.** He often makes FOMC-day videos ("FOMC: The End of an Era", Apr 29, 2026; "Jerome Powell: 'I Won't See You Next Time'", May 1, 2026; "Powell Steps Down as Chair of the Federal Reserve", May 15, 2026) [S, Rosetta titles].
5. **Assets.** Intraday volatility in rates, the dollar and crypto peaks at 2:00-3:30 pm ET. The direction is set by the surprise versus pricing.
6. **Takeaway.** Dissents and wording changes carry more information than the decision itself, which is usually fully priced.

### 2.3 Summary of Economic Projections (SEP) and the dot plot
1. **Definition.** Published quarterly (Mar, Jun, Sep, Dec) with the statement. Each of the 19 participants submits projections for GDP, unemployment, PCE and core PCE, plus the *appropriate* end-year fed funds rate, which is the "dot." The table reports medians, central tendencies and ranges. Source: federalreserve.gov `fomcprojtablYYYYMMDD.htm` [V]. **Under Warsh the Chair does not submit a dot or a projection**, so the 2026 SEPs reflect 18 participants. Warsh: "I don't submit a dot. I don't plan on submitting a dot" [V, Oct 28 transcript; the Sep 16 transcript says the same].
2. **How the median moved, 2024-26 [V]:**

| SEP | Fed funds median: current year / next / year after | Longer-run rate (nominal neutral, r*+2) | Current-year PCE / core PCE | Current-year unemployment |
|---|---|---|---|---|
| Sep 2024 | 4.4 / 3.4 / 2.9 | 2.9 | 2.3 / 2.6 | 4.4 |
| Dec 2025 | 3.6 / 3.4 (2026) / 3.1 | 3.0 | 2.9 / 3.0 | 4.5 |
| Mar 2026 | 3.4 (2026) / 3.1 / 3.1 | 3.1 | 2.7 / 2.7 | 4.4 |
| Jun 2026 | **3.8** (2026, i.e. a hike) / 3.6 / 3.4 | 3.1 | 3.6 / 3.3 | 4.3 |
| Sep 2026 | **4.1** (2026, one more hike) / 4.1 / 3.9 | **3.2** | 3.7 / 3.4 | 4.1 |

3. **How to read it.** The dots are *conditional forecasts, not promises*. In Sep 2024 they implied 2.9% by 2026. The actual rate is 3.875%, because the energy shock intervened. The **longer-run dot** is the Committee's estimate of the nominal neutral rate. It has drifted up from 2.5% (2019-2023) to 3.2% [S for the earlier level, V for 3.2]. A common misreading is to treat the median as a consensus forecast of the actual path. Markets (FedWatch) and dots often diverge, and markets have been right more often at turning points [S].
4. **Cowen's use.** He contrasts the dot-implied path with market pricing and with the 2Y [S/I].
5. **Assets [I].** An upward shift in the dots (Jun and Sep 2026) is hawkish: a stronger dollar and higher real yields, which weigh on long-duration assets and crypto.
6. **Takeaway.** Read the dots as the Committee's *reaction function* ("if inflation does X, we do Y"), not as a forecast.

### 2.4 Neutral rate (r*)
1. **Definition.** The real short rate consistent with full employment and stable inflation; it is unobservable. Estimates come from the NY Fed's Laubach-Williams and Holston-Laubach-Williams models (newyorkfed.org, quarterly) and from the SEP longer-run dot. Nominal neutral is r* plus 2% inflation.
2. **How to read it.** Policy is "restrictive" if real fed funds is above r*. The SEP longer-run median of 3.2% implies r* of about 1.2% [V/I]. Warsh on neutral: "In a word, no ... I've always been interested in a neutral rate as an academic matter" — he does not steer by it [V, Sep 16 transcript].
3. **Cowen's use.** He uses the fed funds versus 2Y gap as a market proxy for neutral (Bankless, Dec 2025) [S].
4. **Relationships [I].** Rising r* estimates, driven by fiscal deficits, AI capex and higher term premium, mean the same nominal rate is *less* restrictive than it looks. That is one candidate explanation for why 2022-24 tightening did not cause a recession.
5. **Assets.** Indirect: it shapes how high "terminal" rates and long yields can stay.
6. **Takeaway.** "Restrictive" is relative to a moving, uncertain target, and the error bands are about ±1 pp.

### 2.5 Taylor rule
1. **Definition.** A benchmark rate: i = r* + π + 0.5(π − 2) + 0.5 × (output gap). An Okun-law variant uses 2 × (u* − u). The Atlanta Fed publishes a "Taylor Rule Utility" (atlantafed.org). FRED has no official series [S].
2. **Now [I].** With r* = 1.2, core PCE π = 3.1, and unemployment gap ≈ 0 (u = 4.2 versus SEP longer-run 4.2): i ≈ 1.2 + 3.1 + 0.55 ≈ **4.85%**. That is about 1 pp above the current 3.875%. With r* = 0.5, the rule gives about 4.15%, close to the SEP's 4.1%. With headline PCE (3.65) instead of core, it gives about 5.6%. Conclusion: by simple-rule standards policy is **not tight**, which fits the hawkish dissents.
3. **Common misreading.** Treating the rule as a forecast. The Fed deviated massively in 2021-22: the rule implied rates above 7% while the funds rate was near 0 [S].
4. **Cowen's use.** I could not verify that he uses the Taylor rule; it is not a staple of his content [I].
5. **Assets.** None directly. It is a framing tool for "behind the curve" arguments.
6. **Takeaway.** A useful sanity check on whether the Fed is ahead of or behind inflation.

### 2.6 Real fed funds rate
1. **Definition.** Nominal fed funds minus an inflation measure: trailing core PCE, headline CPI, or expected inflation (Michigan, or the Cleveland Fed's model). FRED has no single series; compute DFF − PCEPILFE YoY [I]. TradingView: `FRED:DFF-...`, custom.
2. **Now [I].** 3.88 − 3.12 (core PCE) = **+0.76**. Against headline PCE (3.65) it is +0.2. Against Michigan 1-year expectations (4.6) it is −0.7. In mid-2024 it was about +2.6 (5.33 − 2.7), the most restrictive since 2007.
3. **How to read it.** Positive and above r* is restrictive. Volcker took it to about +5 to +8 in 1980-82. Burns let it go negative in 1974-77, the "second wave" setup [S]. The 2026 risk [I] is that if inflation broadens, the real rate is barely positive. That is the hawks' argument.
4. **Assets [I].** Rising real rates are the single most consistent macro headwind for gold, BTC and growth stocks. Gold's 2022-24 resilience was an exception driven by central-bank buying.
5. **Takeaway.** Always subtract inflation before judging whether rates are high.

### 2.7 CME FedWatch probabilities
1. **Definition.** Probabilities of FOMC outcomes derived from 30-day fed funds futures prices. Free at cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html. SOFR futures and OIS give similar information.
2. **How to read it.** It shows market pricing, not truth. It is reliable within about 2 weeks of a meeting, because the Fed rarely surprises against more than 70% odds, and unreliable 6 or more months out. Before Sep 16, 2026 the market priced about 90% for a hike [S, press-conference question]. After Oct 28 it put about 83% on a December hike [S].
3. **Cowen's use.** He cites FedWatch odds frequently. In October 2026 he noted the odds of an October hike fell from 64% to 17.7% within a week [S, BeInCrypto].
4. **Assets.** Large changes in probabilities often drive more market movement than the decision itself.
5. **Takeaway.** Watch *changes* in pricing.

### 2.8 The "pivot" and hiking, pause and cutting cycles
1. **Definition.** A "pivot" is the shift from tightening (or pause) to easing, or the reverse. A cycle runs from the first hike to the last hike, then a pause, then the first cut. Typical modern pause between last hike and first cut: **about 4-18 months, mean about 10** (§6.1).
2. **Two kinds of easing cycle [I].** **Insurance or "mid-cycle" cuts** (1995, 1998, 2019, and 2024-25 in hindsight) are 75-175 bp, made with no recession, and stocks rise. **Recession cuts** (1974, 1980, 1989-92, 2001, 2007-08, 2020) total 500 bp or more, unemployment rises 2-5 pp, and stocks fall 20-55% from the first cut.
3. **2024-26 [V].** The cycle was hikes Mar 2022 → Jul 2023 (5.25-5.50%), a 14-month pause, cuts Sep 2024 → Dec 2025 (−175 bp in 6 moves), a 9-month pause, then a hike in Sep 2026. Structurally this resembles **1998 → 1999** (75 bp of insurance cuts, then 175 bp of hikes in 1999-2000) more than 2007 [I].
4. **Cowen's use.** "The pivot" is a recurring word. In March 2024 he framed the pivot as the trigger for broader market breadth and for altcoins [S].
5. **Assets.** See §6.1.
6. **Takeaway.** Asking "why is the Fed cutting?" is more useful than asking "is the Fed cutting?".

### 2.9 QE/QT and the balance sheet (brief; liquidity is cluster C)
`WALCL` (weekly, Wednesday level, released Thursday at 4:30 pm ET). QT2 ran Jun 2022 → Dec 1, 2025 and took the balance sheet from about $8.97T to $6.57T [V/S]. The Oct 29, 2025 statement: "The Committee decided to conclude the reduction of its aggregate securities holdings on December 1" [V]. From December 2025 the Fed has bought T-bills for "reserve management" (the directive allows purchases "to maintain an ample level of reserves"), and agency (MBS) principal is reinvested into bills. WALCL is back to $6.75T [V]. Warsh has floated a smaller balance sheet over time via a "Balance Sheet Task Force", but there is no decision yet (Oct 28 presser) [V]. Cowen ties the end of QT to the 2019 crypto analog ("Bitcoin topped two months before quantitative tightening ended") [S].

### 2.10 Forward guidance
Explicit guidance ("extended period", calendar-based, dots) peaked in 2012-2021. Warsh explicitly rejects it: "This won't surprise you: I'm not in the forward guidance business" (Sep 16, 2026 press conference) [V]. He says he took office about "110 or 20 days" earlier, which points to roughly late May 2026 [V/I]. The practical implication [I] is more weight on market pricing (2Y, FedWatch) and more meeting-day surprise risk. Higher rate volatility follows: the MOVE index was above 100 in late September 2026 [S].

---

## 3. Bonds

### 3.1 Treasury yields: 3-month, 2-year, 10-year, 30-year
1. **Definition and source.** Constant-maturity yields from the US Treasury's daily par yield curve (treasury.gov, published at about 3:30 pm ET). FRED `DGS3MO`, `DGS2`, `DGS10`, `DGS30`, plus monthly `GS10`, `GS2` and `TB3MS` (secondary-market 3M bill, back to 1934). TradingView `TVC:US03MO`, `US02Y`, `US10Y`, `US30Y`.
2. **What each tells you [I].** The **3M** is almost pure current policy. The **2Y** is the expected policy path over 2 years and is the most Fed-sensitive. The **10Y** is expected average short rates plus the term premium, and is the global discount rate (mortgages, equity valuation). The **30Y** carries fiscal, term-premium and inflation-risk signal.
3. **2026 path [V].** 2Y: 3.52 (Jan) → 3.38 (Feb 27 low) → 4.88 (Sep) → 4.67. 10Y: 4.26 → 3.97 (Feb) → 5.31 (Oct 5) → 5.05. 30Y: 4.87 → 5.67 (Oct 7) → 5.37. On Oct 5, 2026 the 10Y set its highest daily close since May 2002 [V/I].
4. **Common misreading.** "Fed cuts mean lower mortgage rates." After the first cut in Sep 2024 the 10Y *rose* about 100 bp in 3 months (3.63 → 4.58) because growth held up and the term premium rose [V]. Cowen made exactly this point in 2025 [S].
5. **Assets [I].** A 10Y above 5% has coincided with equity stress before: Oct 2023 (S&P −10%) and 2007. In 2026 the S&P made all-time highs with the 10Y at 5.0-5.3%, so this time the earnings and AI-capex boom dominated. Cowen noted in Apr 2026 that "the 10-year yield spiked pretty high" in 2023 and contributed to that drawdown [S].
6. **Takeaway.** The 2Y tells you about the Fed. The 10Y tells you about everything else (growth, term premium, fiscal).

### 3.2 Yield-curve spreads: 10Y-2Y (T10Y2Y) and 10Y-3M (T10Y3M)
1. **Definition.** Daily FRED `T10Y2Y` (from 1976) and `T10Y3M` (from 1982). For longer history use GS10 − TB3MS (monthly, from the 1950s). TradingView: `FRED:T10Y2Y` or the expression `TVC:US10Y-TVC:US02Y`.
2. **Which spread [S/I].** The Fed's own research (Estrella-Mishkin, and the NY Fed probit model) prefers **10Y-3M**. It has the better record and is the input to the NY Fed's monthly recession probability (newyorkfed.org/research/capital_markets/ycfaq). Markets and media watch 2s10s. The near-term forward spread (Engstrom-Sharpe, Fed Board, 2018) argues that only the front end matters.
3. **How to read it.** Inversion (below 0) reflects expected future cuts, meaning the market thinks policy is too tight. It is a *conditional* signal with **long and variable lags** (§6.2). Un-inversion usually happens because the Fed starts cutting (bull steepening). Historically **recessions began 0-8 months after un-inversion** in 1990, 2001, 2008 and 2020. That is the basis of Cowen's "the danger is the un-inversion" framing [S/I].
4. **Now [V].** 10Y-2Y +0.37, 10Y-3M +0.80. 10Y-2Y peaked at +0.74 on Jan 30, 2026 and has bear-flattened since.
5. **Takeaway.** Inversion says "policy is tight relative to the future". It does not give a date.

### 3.3 Steepening and flattening: bull versus bear
Definitions:
- **Bull steepening**: short yields fall faster than long yields, typically when the Fed cuts into weakness. Examples: 2001, 2007-08, Aug-Sep 2024, the classic pre-recession pattern.
- **Bear steepening**: long yields rise faster, driven by term premium, inflation or fiscal worries. Examples: Oct 2024 → Jan 2025, and 2026 measured against 3M bills.
- **Bear flattening**: short yields rise faster, typically during hikes. Examples: 2022, 2026 for 2s10s.
- **Bull flattening**: long yields fall faster, a flight to duration or growth scare. Example: 2019.

**Cycle template [S/I]:** bear flattening (hiking) → inversion → bull steepening (cuts begin) → recession. **2024-26 broke the template.** A bull steepening in Aug-Sep 2024 was followed by a *bear* steepening (no recession, sticky inflation, rising term premium), and then by 2026 bear flattening (re-hiking). That sequence looks like **1998-2000**, where a 1998 bull steepening was followed by a 1999-2000 bear flattening and inversion, then the 2001 recession [I]. In crypto, bear steepening driven by term premium and real yields has been hostile to BTC [I].

### 3.4 Term premium
1. **Definition.** The extra yield for holding a long bond instead of rolling bills. Estimated with models, not observed. NY Fed **ACM** (daily/monthly, newyorkfed.org) and Fed Board **Kim-Wright** (FRED `THREEFYTP10`).
2. **History and now.** It was negative for much of 2016-2021 (QE). It was about +0.17 in Jan 2024 and is now **0.94**, with a September 2026 peak of 1.08, the highest since 2010 [V].
3. **Why it matters [I].** Rising term premium explains why long yields rose after 2024 cuts and why mortgage rates did not fall. It also explains why the 2022-24 inversion overstated how restrictive policy was: the curve was mechanically flatter because QE had compressed the term premium. That is a plausible reason the curve "failed".
4. **Assets.** A higher term premium means higher discount rates for long-duration equities and crypto, and favours bills over long bonds.

### 3.5 Real yields: TIPS and DFII10
1. **Definition.** Yield on Treasury Inflation-Protected Securities. FRED `DFII10` (10Y, from 2003), `DFII5`.
2. **Now.** 2.67%, with a September high of 2.93%, the highest since November 2008. Above 2% marks the tightest real financial conditions in roughly 15 years [V/I].
3. **Relationship.** Gold and BTC are classically inverse to real yields. The gold-to-real-yield link broke in 2022-24 [S]. Cowen published "Gold Drops Nearly 30%" on Mar 23, 2026 [S, title], consistent with a real-yield and dollar squeeze [I].
4. **Takeaway.** The real yield is the cleanest "cost of money" for non-yielding assets.

### 3.6 Breakeven inflation (T10YIE) and 5y5y forward (T5YIFR)
1. **Definition.** Nominal minus TIPS yield gives the market-implied average CPI inflation. The 5y5y is expected inflation 5-10 years ahead, the Fed's favourite "anchoring" gauge [S]. Both are on FRED daily.
2. **Now.** 10Y breakeven 2.35%, 5y5y 2.23%, essentially unchanged despite CPI going from 2.4% to 4.2% [V]. **Long-run expectations are anchored**, which is the key difference from the 1970s [I]. Warsh explicitly targets "inflation compensation in market prices stays low" [V]. The caveat is that breakevens embed liquidity and risk premia, and Michigan 1-year expectations (4.6%) are far less anchored.
3. **Takeaway.** If the 5y5y breaks above about 2.6-2.7%, the "second wave" narrative gains real support [I]. That has not happened.

### 3.7 MOVE index
ICE BofA MOVE: implied volatility of 1-month Treasury options across the 2/5/10/30Y tenors. TradingView `TVC:MOVE`; not on FRED. Peaks: 2008 (about 260), March 2020, March 2023 (SVB, about 199) [S]. It was above 100 on Sep 25, 2026, around the hike [S, Saxo]. Rate volatility is a risk-off input for all leveraged assets, since VaR (value-at-risk) shocks force collateral and margin cuts [I].

### 3.8 Credit spreads
1. **Definition.** ICE BofA US High Yield Option-Adjusted Spread (FRED `BAMLH0A0HYM2`) and US Corporate (IG) OAS (`BAMLC0A0CM`), daily. **Note: FRED now shows only about 3 years of ICE history** because of licensing. The full history is in ICE or Bloomberg [V].
2. **Benchmarks.** HY OAS at about 2.4-2.6 marks extreme complacency (2007, Jan 2025's 2.59). About 5 is the long-run average zone. About 8 or more is recession. Peaks: about 20+ in Dec 2008, about 10.9 in Mar 2020, about 5.8 in mid-2022 [S]. In April 2025 the tariff shock took it to 4.61 [V].
3. **Now.** HY 3.14, IG 0.86: tight. No credit stress is confirming the recession narrative [V/I].
4. **Relationships.** Credit spreads typically widen *before and during* recessions and lead unemployment by 1-6 months [S]. They correlate positively with VIX and negatively with BTC and equities.
5. **Takeaway.** No recession call is credible without widening credit spreads.

### 3.9 Treasury auctions and the supply narrative
Treasury's quarterly refunding statement (Feb/May/Aug/Nov, early month) sets coupon sizes. Auction metrics are tail versus when-issued yield, bid-to-cover, and indirect (foreign or real-money) versus dealer takedown. The narrative: large deficits (about 6% of GDP [S]) and a high bill share keep the term premium elevated. A BeInCrypto piece in Aug 2026 credits a "doubled Treasury bond buyback" with helping risk assets [S, low confidence]. Weak 10/30Y auctions often coincide with spikes in long yields [I].

---

## 4. Inflation

### 4.1 CPI and core CPI
1. **Definition.** BLS Consumer Price Index for All Urban Consumers (CPI-U), released monthly about 10-15 days after month-end at 8:30 am ET. Core excludes food and energy. FRED `CPIAUCSL` (SA), `CPIAUCNS` (NSA, the "headline" YoY BLS quotes), `CPILFESL`. TradingView `ECONOMICS:USIRYY` (YoY), `USCIR` (core). CPI is not revised, except that seasonal factors are revised for 5 years each February [S].
2. **Path [V/I, SA YoY]:**

| Date | Headline | Core | Note |
|---|---|---|---|
| Jun 2022 | 9.0 | 5.9 (core peak 6.6 in Sep 2022) | 40-year high |
| Jan 2025 | 3.0 | 3.3 | |
| Apr 2025 | 2.3 | 2.8 | Tariff announcements |
| Sep 2025 | 3.0 | 3.0 | |
| Oct 2025 | — | — | Not published (federal shutdown Oct 1 – Nov 12, 2025) |
| Jan-Feb 2026 | 2.4 | 2.5 | The low |
| Mar 2026 | 3.3 | 2.6 | Energy shock; MoM +0.87% |
| Apr 2026 | 3.8 | 2.7 | Cowen video "Inflation Rises to 3.8%" |
| May 2026 | **4.2** | 2.8 | Peak |
| Jun 2026 | 3.5 | 2.6 | MoM −0.42% as oil fell |
| Sep 2026 | 3.7 | 2.6 | MoM +0.65% headline, +0.33% core |

3. **How to read it.** Headline is noisy (energy). Core shows *persistence*. In 2026 the gap between headline and core is the story: a **supply shock** that has *not yet* broadened. The 3-month annualised core is about 3.4% [I], higher than the YoY figure, which is an early warning that core is turning up.
4. **Cowen's use.** Monthly CPI-day videos ("Inflation Soars to 3.3%", Apr 10, 2026; "Inflation Rises to 3.8%", May 12, 2026). He breaks down CPI categories (housing, food, apparel, transportation about 7% YoY) and calls the 2026 spike "mostly a supply driven issue" [S, Rosetta].
5. **Assets [I].** A hot CPI surprise lifts yields and the dollar and hits crypto and growth equities on the day; the 2022 playbook is the extreme case. Energy and commodities benefit.
6. **Takeaway.** Compare 3- and 6-month annualised core with YoY to see the direction early.

### 4.2 "Supercore", shelter and OER
- **Supercore** means core services excluding shelter (housing). Powell's favourite wage-driven gauge in 2022-23. It is not a single FRED series; compute it from CPI "services less energy services" (`CUSR0000SASLE`) minus shelter weights, or use BLS "services less rent of shelter" (`CUSR0000SASL2RS`) [S].
- **Shelter** (`CUSR0000SAH1`) is about 35% of CPI and about 44% of core CPI. It includes **Owners' Equivalent Rent (OER)** (`CUSR0000SEHC`), an imputed rent. It **lags market rents by about 12 months** (Zillow and Apartment List rents lead) [S]. Shelter YoY peaked at about 8% in 2023 [S] and is 3.2% in Sep 2026 [V]. Shelter disinflation was the main driver of falling core in 2024-25 [I].
- **Misreading.** Shelter is backward-looking. A housing slowdown shows up in CPI with about a 1-year lag.

### 4.3 PCE and core PCE, the Fed's target
1. **Definition.** BEA Personal Consumption Expenditures price index, released with Personal Income and Outlays about 4 weeks after month-end. FRED `PCEPI`, `PCEPILFE`. The 2% target is defined on **headline PCE**, but core PCE is the operational guide [V/S]. PCE has broader coverage, chain weights, a smaller shelter weight (about 15%), and includes employer- and government-paid healthcare. It is **revised**.
2. **Now.** Headline 3.65%, core **3.12%** (Sep 2026). Core PCE has been above 3% for most of 2026 [V]. Unusually, core PCE (3.1) is *above* core CPI (2.6). The likely causes are PCE's lower shelter weight (shelter is disinflating) and higher weights on energy-sensitive services (airfares, transport) and on portfolio-management fees, which rise with stock prices [I/S].
3. **Peak.** Core PCE 5.6% in Sep 2022 [V].
4. **Takeaway.** When CPI and PCE diverge, the Fed follows PCE. Warsh cited core PCE at "about 3.2" on Sep 16 [V].

### 4.4 PPI
BLS Producer Price Index for final demand (`PPIFIS`), released about mid-month, usually after CPI. PPI components that feed PCE (airfares, medical, portfolio management) move core PCE nowcasts. YoY is **6.3%** (Sep 2026), up from about 3% in 2025, and is mostly energy [V/I]. PPI leads goods CPI by about 0-3 months [S]. It is a pipeline signal, not a target.

### 4.5 Michigan inflation expectations
University of Michigan Surveys of Consumers: 1-year (`MICH`) and 5-10-year expectations. Preliminary mid-month, final end-month. Peaks: **6.6% (May 2025, tariff fear)** and 4.6% (Sep 2026) [V]. Michigan expectations are noisy and partisan-sensitive since 2024, so compare them with the NY Fed Survey of Consumer Expectations and with market 5y5y [S/I].

### 4.6 YoY versus MoM annualised, and base effects
- YoY = this month ÷ same month last year. MoM annualised = (1+m)^12 − 1. A 0.3% core MoM is about 3.7% annualised, and 0.2% is about 2.4% [I].
- **Base effects.** YoY drops mechanically when a big month from a year ago "rolls off". Example: the Mar-May 2026 energy surge (+0.87%, +0.64%, +0.47% MoM) will roll off in Mar-May 2027, mechanically pulling headline YoY down even if prices stay high [I]. The June 2026 −0.42% month will roll off in June 2027 and push YoY *up*.
- **Misreading.** "Inflation is falling" when only YoY is falling because of base effects while the monthly run rate stays hot.

### 4.7 Disinflation versus deflation
Disinflation means inflation is falling but still positive (2023-24). Deflation means prices are falling, which is rare in the US: 2009 (−2% YoY headline from oil), and briefly 2015 and 2020 [V/I]. Cowen's pre-2026 thesis was disinflation toward 2% (2023-25). He warned that only a policy mistake or a shock would re-accelerate inflation [S].

### 4.8 The 1970s "second wave" analogy (Arthur Burns)
**Facts [V, FRED].** CPI peaked at 6.4% (Feb 1970). Fed funds was cut from 9% to about 3.5% by 1972. CPI then rose to **12.2% (Nov 1974)**. The Fed under **Arthur Burns** eased again from 12.9% (Jul 1974) to about 4.7% (Dec 1976) while inflation was still about 5% at the 1976 trough. CPI then hit **14.6% (Mar 1980)**. Volcker took fed funds to about 19% (Jun 1981). A Hoover/Fed paper (Nelson, 2024) attributes much of the 1976-80 wave to Burns-era policy [S].

**2022-26 overlay [I].** CPI peaked at 9.0% (Jun 2022), troughed at 2.3-2.4% (Apr 2025, Jan 2026), and is back at 3.7-4.2% in 2026. The shape rhymes with the 1970s. The magnitude so far is much smaller (the 1976 trough was 5%, against 2.4% now). The 2026 trigger is an oil shock, which is also 1973-74-like. The key differences: long-run expectations are anchored (5y5y at 2.2%), the Fed **hiked** into the shock instead of easing, unions and wage indexation are weaker, and the economy is less energy-intensive.

**Cowen** references the 1970s as a risk scenario and links a renewed major wave to stock-market damage (May 2026) [S]. The narrative is supported in direction and so far weak in magnitude.

### 4.9 Tariffs and inflation, 2025-26
Tariff announcements in April 2025 ("Liberation Day", Apr 2) produced an expectations spike (Michigan 6.5-6.6%), a credit spread spike (HY 4.61 on Apr 7) and an S&P drawdown of about −19% from the February 2025 peak to April 8 [V for HY and S&P, S for the peak date]. Realised CPI pass-through was modest and gradual: core goods firmed, and core CPI went from 2.8% (Apr) to 3.1% (Aug 2025) [V/I]. The Fed treated tariffs as a one-time price-level shift and cut anyway from Sep 2025 [V, statements: "in light of the shift in the balance of risks"]. A 2026 Supreme Court ruling against IEEPA tariffs is referenced in secondary sources (title only, not verified) [S].

---

## 5. Labor

### 5.1 Unemployment rate: U-3 and U-6
1. **Definition.** BLS Employment Situation report, from the household survey (CPS, about 60k households). Released the first Friday of the month at 8:30 am ET for the prior month. **U-3** (`UNRATE`) counts jobless people actively searching. **U-6** (`U6RATE`) adds marginally attached and involuntary part-time workers. Seasonal factors are revised each January. TradingView `ECONOMICS:USUR`.
2. **Path [V].** 3.4% (Apr 2023, cycle low) → 4.2-4.3% (Jul-Aug 2024, Sahm trigger) → 4.0% (Jan 2025) → **4.5% (Nov 2025, peak)** → 4.3-4.4% (H1 2026) → 4.1% (Jul-Aug 2026) → 4.2% (Sep 2026). U-6 peaked at 8.7% (Nov 2025) and is now 7.6%. The October 2025 household survey was never collected because of the shutdown [V, FRED gap].
3. **How to read it.** Watch the *change* from the cycle low, not the level. Since 1955 every recession started after unemployment had risen 0.3-1.0 pp from its trough, with a median lead of about 8 months from trough to recession start (§6.5) [V/I]. Labor supply matters: in 2023-24 immigration expanded the labor force, so unemployment rose without layoffs. In 2025-26 net immigration fell sharply and participation dropped from 62.5% to 61.8%, so the *break-even* payroll pace collapsed, possibly to 0-50k/month [S/I]. Low payroll growth no longer implies rising unemployment.
4. **Cowen's use.** Unemployment with recession bars and a moving average is a core chart. "Labor Market Holds Steady" (May 8, 2026) [S]. He expected unemployment to rise into late 2024 and 2025 [S].
5. **Assets.** See §6.1 and §6.5. Rising unemployment means bull steepening, falling yields, Fed cuts, and equity drawdowns *if* it accelerates.
6. **Takeaway.** Use the trend and change in unemployment alongside claims. The 2025-26 labor-supply shock makes the level less informative.

### 5.2 Sahm rule (SAHMREALTIME)
1. **Definition.** Claudia Sahm (2019). The rule fires when the 3-month average of U-3 is at least **0.50 pp** above its minimum over the prior 12 months. FRED `SAHMREALTIME` uses the *real-time* (as-first-published) unemployment vintages; `SAHMCURRENT` uses current revised data.
2. **Track record [V/I, SAHMREALTIME from Dec 1959].** First crossings of 0.50:

| Trigger month | Recession (NBER start) | Comment |
|---|---|---|
| Dec 1959 (0.77) | May 1960 | Fired before the start |
| Oct 1969 (0.50) | Jan 1970 | About 3 months before |
| Mar 1974 (0.50) | Dec 1973 | About 3 months after the start |
| Nov 1976 (0.50) | none | **False positive** (borderline 0.50) |
| Apr 1980 (0.67) | Feb 1980 | 2 months after |
| Nov 1981 (0.80) | Jul/Aug 1981 | About 3 months after |
| Nov 1990 (0.50) | Jul/Aug 1990 | About 3 months after |
| Jun 2001 (0.53) | Mar/Apr 2001 | About 2-3 months after |
| Apr 2008 (0.50) | Dec 2007/Jan 2008 | About 4 months after |
| Apr 2020 (4.0) | Feb/Mar 2020 | Coincident |
| **Jul 2024 (0.53; 0.57 in Aug)** | **none as of Oct 2026** | **False positive** |

3. **How to read it.** It is a *coincident-to-lagging* recession *dating* rule, not a forecaster. It typically fires 0-4 months **after** the recession starts [V/I]. Sahm herself said in 2024 it was likely a false signal because the rise came from labor-supply growth (immigrants and re-entrants) rather than layoffs. Her view was that "the Sahm rule is likely overstating" the weakness [S].
4. **2025-26.** It reached 0.43 in Nov 2025 (unemployment 4.5-4.6%) without triggering. It is 0.00 now [V].
5. **Cowen's use.** He discussed it in 2024 as a signal of "looser monetary policy regardless of whether a recession is imminent" and connected it to a peak in BTC dominance [S, secondary]. He also discussed state-level Sahm triggers (Mar 2024) [S].
6. **Takeaway.** Treat the Sahm rule as confirmation, not a forecast. 2024 showed that a labor-*supply* shock can trigger it falsely.

### 5.3 Initial and continuing jobless claims
1. **Definition.** Department of Labor weekly UI claims, released Thursday at 8:30 am ET. FRED `ICSA` (initial, SA), `CCSA` (continuing, one week further lagged), `IC4WSA` (4-week average). TradingView `ECONOMICS:USIJC`.
2. **How to read it.** Claims are the most *timely* hard labor indicator. As a share of the labor force they are at historic lows. Cowen's threshold: "It's not a recession until this is at 300K" [S]. Historically, initial claims rising about 20-30% off their cycle low has preceded recessions by about 0-6 months [S]. Watch for seasonal-adjustment quirks: summer auto retooling and January.
3. **Now.** Initial claims 194k (Oct 24, 2026), with the 4-week average "at the lowest level in generations" according to Warsh (Oct 28) [V]. Continuing claims 1.70M, down from about 1.9-1.97M in 2025 [V/S]. The 2025 pattern was low firing and low hiring. Rising continuing claims meant re-employment was slow, which was the warning sign in 2025 [I].
4. **Takeaway.** Claims are the first hard data to break in a real downturn, and in October 2026 they are not breaking.

### 5.4 Nonfarm payrolls and revisions
1. **Definition.** BLS establishment survey (CES, about 120k businesses). Released the same day as unemployment. `PAYEMS` is the level; take differences for monthly change. The two prior months are revised each release. There is an annual **benchmark revision** to March QCEW tax-record counts: preliminary in Aug/Sep, final with the January report in February.
2. **Benchmarks [V/S].** Year to Mar 2024: preliminary −818k (Aug 2024), final −598k [S]. **Year to Mar 2025: preliminary −911k (Sep 9, 2025), the largest on record; final −898k (Feb 11, 2026)** [S]. Year to Mar 2026: preliminary only **−79k** (Aug 28, 2026), the smallest since 2021 [S/V].
3. **2025 politics.** After the Aug 1, 2025 report revised May-June down by about 258k, the President fired the BLS commissioner [S]. That fuelled a data-credibility debate. The revisions were within normal statistical behaviour in direction, though large [I].
4. **Now [V].** 2026 monthly changes: +160, −156, +214, +148, +63, +31, −10, +133, +29 (k). About 68k/month. Several negative months, yet unemployment *fell*, which fits a labor-supply shock [I].
5. **Takeaway.** Payrolls are heavily revised, so one month means little. Use 3-month averages and check against claims and the household survey.

### 5.5 JOLTS: openings and quits
BLS Job Openings and Labor Turnover Survey, monthly with a ~5-week lag (Aug 2026 data released Oct 2026). FRED `JTSJOL`, `JTSQUR`, `JTSHIR`, `JTSLDR`. Openings peaked at about 12M (Mar 2022) [S] and are 7.08M now [V]. The quits rate of **1.9%** is below pre-pandemic (about 2.3%) and signals workers are afraid to switch jobs: a "low-hire, low-fire" market [I]. Cowen tracks openings, quits, hires and layoffs as the "first domino" in his labor sequence [S]. The Beveridge curve (openings vs unemployment) shows that the 2022-24 normalisation came through openings, not unemployment, which was Waller's soft-landing argument [S].

### 5.6 Participation rate
`CIVPART`, monthly from the household survey. 62.5-62.7% in 2024 → 61.8% (Sep 2026, low 61.4% in Jul 2026) [V]. Drivers: ageing and immigration. A falling participation rate holds down measured unemployment, so it flatters U-3 [I].

### 5.7 The "unemployment bottoms, then rises into recession" pattern
See §6.5. Unemployment has a strong *momentum* property: once it rises about 0.5 pp it has historically tended to keep rising, because of the layoff → spending → layoff feedback loop. The Sahm rule is built on that. **2024-26 is the main counter-example in the post-war record:** a +0.9 pp rise from 3.4% to 4.3% (and 4.5% on a single print) that reversed without a recession. There is a 1960s precedent: in 1962-63 and 1967 unemployment crossed above its moving average without a recession (§6.5) [V/I].

---

## 6. Relationship analysis with historical episodes

### 6.1 Every Fed easing cycle since 1970: S&P 500 from the first cut, timing, and unemployment

S&P 500 returns use **monthly average** prices (Shiller dataset) from the month of the first cut; daily-close figures are added where known. "UN peak" is the maximum unemployment rate within 48 months of the first cut. Gap from last hike to first cut comes from FOMC history [S] where marked.

| First cut (month) | Recession? | Last hike → first cut | S&P +6m | +12m | +24m | Max drawdown within 24m (monthly avg) | UN at cut → UN peak (date) | Months from first cut to UN peak |
|---|---|---|---|---|---|---|---|---|
| Jan 1970* | Yes (Dec 1969 – Nov 1970) | short | −16% | +4% | +14% | −16% | 3.9 → 6.1 (Dec 1970) | 11 |
| Aug 1974 | Yes (Nov 1973 – Mar 1975) | ~1-2 m [S] | +5% | +13% | +36% | −12% (bottom Dec 1974) | 5.5 → 9.0 (May 1975) | 9 |
| May 1980 | Yes (Jan – Jul 1980) | ~1 m [S] | +26% | +22% | +8% | 0% | 7.5 → 10.8 (Nov 1982) | 30 |
| Jul 1981 | Yes (Jul 1981 – Nov 1982) | ~1-2 m [S] | −9% | −15% | +29% | −15% | 7.2 → 10.8 (Nov 1982) | 16 |
| Sep/Oct 1984 | **No** | ~1-2 m [S] | +8% | +11% | +44% | −1% | 7.3 → 7.4 | ~1 |
| Jun 1989 | Yes (Jul 1990 – Mar 1991) | ~4 m (Feb/May 1989 → Jun 1989) [S] | +8% | +11% | +17% | −5% avg (daily: about −20% Jul-Oct 1990 [S]) | 5.3 → 7.8 (Jun 1992) | 36 |
| **Jul 6, 1995** | **No (soft landing)** | 5 m (Feb 1, 1995) [S] | +10% | +16% | +66% | 0% | 5.7 → 5.7 (already peaked) | 0 |
| **Sep 29, 1998** | **No (LTCM insurance)** | 18 m (Mar 25, 1997) [S] | +26% | +29% | +44% | 0% | 4.6 → 4.6; later 6.3 in 2003 (next cycle) | n/a |
| **Jan 3, 2001** | Yes (Mar – Nov 2001) | 7.5 m (May 16, 2000) [S] | −10% | −15% | −33% | −36% avg; daily 1,347.6 → 776.8 (Oct 9, 2002) = **−42%** [S] | 4.2 → 6.3 (Jun 2003) | 29 |
| **Sep 18, 2007** | Yes (Dec 2007 – Jun 2009) | 14.5 m (Jun 29, 2006) [S] | −12% | −19% | −30% | −49% avg; daily 1,519.8 → 676.5 (Mar 9, 2009) = **−55%**; S&P made its ATH 3 weeks *after* the cut (1,565, Oct 9, 2007) [S] | 4.7 → 10.0 (Oct 2009) | 25 |
| **Jul 31, 2019** | Yes, exogenous (Feb – Apr 2020) | 7.5 m (Dec 19, 2018) [S] | +9% | +7% | +46% | daily 2,980 → 3,386 peak (Feb 19, 2020) → 2,237 (Mar 23, 2020) = **−25%** from cut [V] | 3.7 → 14.8 (Apr 2020) | 9 |
| Mar 3, 2020 | (same) | — | +27% | +47% | +66% | — | 4.4 → 14.8 | 1 |
| **Sep 18, 2024** | **No (as of Oct 2026)** | 14 m (Jul 26, 2023) | +1% (avg) | +17% | +36% | daily 5,618 → 4,983 (Apr 8, 2025) = **−11%** [V] | 4.1 → **4.5 (Nov 2025)** | 14 |

*1970: pre-1980 policy was not set as a formal target; the dates mark when the funds rate peaked and fell [I].

**Patterns [I]:**
- **Recession cycles** (1970, 1974, 1980-82, 1989-90, 2001, 2007): unemployment peaked **9-36 months after the first cut**, median about 20 months, and 2-5 pp higher. Stocks either kept falling well after the first cut (2001, 2007: −42%/−55% daily) or had already bottomed *before* the cut because the Fed cut late into an existing crash (1974, 1980).
- **Non-recession cycles** (1984, 1995, 1998, 2024): unemployment peaked within 0-14 months and rose 0-0.4 pp. S&P was +11% to +29% at 12 months.
- **Median 12-month S&P return from the first cut:** about +11% across all 13 cycles. Recession cycles average about +3% with a −15% to +22% spread. Non-recession cycles average about +18% [I, from table]. The "cuts are bearish" claim is **true only conditional on recession**.
- **Gap from last hike to first cut:** about 4-18 months in the modern era (1989-2024), mean about 10. No reliable difference between soft-landing and recession cycles: 1995 had 5 m (soft landing), 1998 had 18 m (soft landing), 2001 had 7.5 m (recession), 2007 had 14.5 m (recession). Treat claims of "the longer the pause, the worse the outcome" as unproven [I].
- **2024-26 classification:** behaves like 1995/1998. Unemployment peaked 14 months after the first cut at +0.4 pp above its level at the cut; S&P is +38% from the first cut (5,618 → 7,744). The 1998 analogy has a sting in its tail: the Fed re-hiked in 1999-2000 and the recession came in 2001.
- **Cowen's "markets bottom near the last cut"** [S]: true for 2001-03 (last cut Jun 2003; bottom Oct 2002/Mar 2003) and 2008-09 (last cut Dec 2008; bottom Mar 2009). Not true for 2019-20 (bottom Mar 23, 2020 came about a week after the last cut on Mar 15). Rough rule only.

### 6.2 Yield-curve inversion → un-inversion → recession, for every recession since 1970

The table uses monthly averages; daily dates are given where computed. "Inversion start" is the first month of the episode. "Un-inversion" is the first positive month after the last negative one.

| Recession (NBER, USREC first month) | Spread | Inversion start | Deepest | Un-inversion | Inversion → recession | Un-inversion → recession |
|---|---|---|---|---|---|---|
| Dec 1969 / Jan 1970 | 10Y-3M (GS10−TB3MS) | Jan 1969 | −0.29 (Aug 1969) | Feb 1970 | ~12 m | un-inverted ~1 m *after* start |
| Nov/Dec 1973 | 10Y-3M | Jun 1973 | −1.27 | Oct 1974 | ~6 m | ~10 m *after* start |
| Jan/Feb 1980 | 10Y-3M / 2s10s | Dec 1978 (2s10s Sep 1978) | −2.45 (Mar 1980) | May 1980 | ~14 m (2s10s ~17) | ~3 m after start |
| Jul/Aug 1981 | 10Y-3M | Nov 1980 | −2.65 | Sep 1981 | ~9 m | ~1 m after start |
| Jul/Aug 1990 | 2s10s | Jan 1989 | −0.32 | Apr 1990 | **19 m** | **4 m before** |
| | 10Y-3M | Jun 1989 | −0.16 | Jan 1990 | 14 m | 7 m before |
| Mar/Apr 2001 | 2s10s | Feb 2000 (brief Jun 1998 dip) | −0.41 | Jan 2001 | 14 m (34 m from 1998) | **3 m before** |
| | 10Y-3M | Jul 2000 | −0.70 | Feb 2001 | 9 m | 2 m before |
| Dec 2007 / Jan 2008 | 2s10s | Feb 2006 (merged episode; first touches late 2005) | −0.15 avg | Jun 2007 | ~23 m | **7 m before** |
| | 10Y-3M | Aug 2006 | −0.52 | Jun 2007 | 17 m | 7 m before |
| Feb/Mar 2020 | 2s10s | Aug 2019 (brief) | ~−0.05 | Sep 2019 | ~7 m | ~6 m before |
| | 10Y-3M | May 2019 | −0.36 | Mar 2020 | 10 m | **0 m** |
| **None yet** | 2s10s | **Jul 6, 2022 (daily)** | **−1.08 (Jul 3, 2023)**, deepest since 1981 | **Sep 6, 2024** (first durable positive close; touched 0 on Aug 27) | **52+ m and counting** | **25+ m, no recession** |
| | 10Y-3M | **Oct 25, 2022 (daily)** | **−1.89 (May 4, 2023)** | Dec 2024 (brief), re-inverted Feb-Aug 2025, **durably positive from Oct 17, 2025** | **48+ m** | **12+ m** |

False signals: 10Y-3M inverted in 1966-67 with no recession until 1970, 40 months later (a "growth recession" / 1966 credit crunch). 2s10s inverted briefly in Jun 1998, 34 months before 2001 [V/I].

**Interpretation [I]:**
- Historical lead from inversion start to recession: **6-23 months** (10Y-3M 6-17 months).
- From un-inversion to recession: **0-7 months before** in the modern era (1990-2020). In the 1970s-80s the curve un-inverted *after* the recession started, because the Fed eased into it.
- **2022-26 is the outlier.** Inverted longer and deeper than any episode since 1980-81, un-inverted (both spreads) through the Fed's 2024-25 cuts, and no NBER recession 48+ months after inversion. That is beyond every historical lag. Candidate explanations: (a) the term premium was depressed by QE, so the inversion overstated tightness; (b) households and corporates had locked in low fixed rates in 2020-21, which weakened transmission; (c) large fiscal deficits; (d) the AI capex boom (Warsh, Oct 28: capex at "a historically high share of GDP"); (e) the immigration labor-supply surge let unemployment rise without layoffs.
- **Where we are (Oct 2026).** Positive curve, bear-flattening in 2s10s because of re-hiking, with 10Y-3M about +0.8. In the 1998 → 2000 template, the curve re-inverted in 2000 after renewed hikes and the recession followed in 2001. **Watch whether renewed hikes re-invert 2s10s** [I]. Cowen's "un-inversion means danger" framing was not borne out in 2024-26 [I].

### 6.3 Sahm rule track record
See the table in §5.2. Of 13 first crossings since 1959, 11 coincided with recessions and 2 were false (1976, 2024). It never fired more than about 5 months before a recession start, and typically fired 2-4 months *after*. The real-time version had **no** false positives between 1977 and 2023. The 2024 false positive is linked to labor-supply growth [V/S/I].

### 6.4 Inflation peaks and the Fed's response

| CPI YoY peak | Peak | Core at peak | Fed funds at peak | Fed response | Outcome |
|---|---|---|---|---|---|
| Feb 1970 | 6.4% | 5.9% | 9.0% | Eased hard (to ~3.5% by 1972) | Recession 1970; inflation re-accelerated (wave 2) |
| Nov 1974 | 12.2% | 11.0% | 9.5% (12.9% Jul 1974) | Eased to ~4.7% by 1976 (Burns) | Trough 5.0% (Dec 1976), then wave 3 |
| Mar 1980 | 14.6% | 12.6% | 17.2% | Volcker: credit controls, cut, then re-hike to ~19% | Double-dip 1980 / 1981-82; inflation broken |
| Oct 1990 | 6.4% | 5.4% | 8.1% | Eased through the oil-shock recession | Recession 1990-91; inflation fell to ~3% |
| Sep 2005 / Jul 2008 | 4.7% / 5.5% | 1.9-2.5% | 3.6% / 2.0% | Looked through oil (2008: cutting) | 2008 oil spike → GFC; deflation 2009 |
| Jun 2022 | 9.0% | 5.9% (core peak 6.6% Sep 2022) | 1.2% | +525 bp in 16 months | Disinflation to 2.3% by Apr 2025, no recession |
| May 2026 | 4.2% | 2.8% | 3.6% | Paused; hiked Sep 2026 (+25 bp); more hikes priced | Ongoing |

**Lessons [I]:**
1. Oil-shock inflation episodes (1973-74, 1979-80, 1990, 2008) all ended in recession. That is the strongest historical warning for 2026, and it matches Cowen's "energy tops last before the cycle ends" [S].
2. The Fed has historically reacted to oil shocks by *easing* once growth broke (1974, 1990, 2008). The 2026 Fed is *hiking* into one, which is Volcker-like rather than Burns-like. That lowers second-wave risk and raises policy-error / recession risk.
3. The 1970s waves happened with inflation expectations unanchored. 2026 long-run breakevens are at about 2.2-2.4%.

### 6.5 Canonical sequence, lead/lag map, and where it fails

**Textbook late-cycle sequence** (approximate lags; [S] historical regularities, [I] synthesis):

1. Fed hikes → 2Y rises above 10Y (**bear flattening → inversion**). Lead to recession: 6-23 months.
2. Openings and quits roll over (JOLTS). Lead to unemployment: about 6-12 months.
3. Credit spreads stop tightening; the HY OAS low comes 6-18 months before recession (Jun 2007, Jan 2025?).
4. Unemployment troughs. Median about 8 months before recession start; range 1-33, since 1957 [V/I: 1957 6 m, 1960 33 m, 1970 8 m, 1973 2 m, 1980 9 m, 1990 17 m, 2001 12 m, 2008 8 m, 2020 1 m].
5. The 2Y falls below fed funds and the market prices cuts → last hike → pause (about 4-18 months).
6. Initial claims rise more than 20% off the low; unemployment rises about 0.5 pp (Sahm). Coincident with recession start.
7. Fed's first cut → **bull steepening → un-inversion**. 0-7 months before recession.
8. Stocks peak. Usually *before or around* the first cut (2000, 2007, 2020), within about 0-12 months.
9. Recession begins (NBER, dated with a lag of 6-12 months).
10. Unemployment peaks 9-36 months after the first cut. Stocks bottom near the last cut or mid-recession.
11. Crypto: since 2019, BTC has tended to *lead* equities at tops (2021: Nov BTC vs Jan 2022 S&P; 2025: Oct 6 BTC peak vs S&P still rising in 2026) [S/I], and it suffers most in liquidity contractions (2022).

**Unemployment crossing above its 12-month moving average** (first cross after 12+ months below; my test, [V data, I method]): 1962 (no recession), 1967 (no), 1969 (yes, 7 m later), 1973 (yes, coincident), 1979 (yes, 6 m), 1985 (no), 1989 (yes, 11 m), 1995 (no), 1998 (no), 2000 (yes, 8 m), 2007 (yes, 7 m), 2016 (no), 2019 (yes, exogenous), 2023 (**no**). About 8 of 15 hits. It is a useful *alert* but has many false positives, especially in mid-cycle slowdowns (1995, 1998, 2016, 2023). Cowen's 24-month version is slower and has fewer false signals [S], but I did not test it.

**Where 2024-26 broke the sequence [V/I]:** steps 1, 2, 4, 5, 6 (Sahm), 7 and 8 (partial: −11% in Apr 2025, not a bear market) all occurred, and step 9 did not. The labor market re-tightened (unemployment 4.5 → 4.2) and the Fed re-hiked. Any course teaching the sequence should present it as **probabilistic**: the 2024-26 cycle, 1998 and 1966-67 are documented failures.

---

## 7. 2025-2026 chronology (with levels)

### 7.1 FOMC decisions [V, federalreserve.gov statements]

| Meeting (decision date) | Decision | Range after | Dissents |
|---|---|---|---|
| Sep 18, 2024 | −50 bp | 4.75-5.00 | Bowman (−25) [S] |
| Nov 7, 2024 | −25 | 4.50-4.75 | — |
| Dec 18, 2024 | −25 | 4.25-4.50 | Hammack (hold) [S] |
| Jan 29, 2025 | hold | 4.25-4.50 | — |
| Mar 19, 2025 | hold; QT slowed | 4.25-4.50 | Waller (wanted QT pace kept) |
| May 7, 2025 | hold | 4.25-4.50 | — |
| Jun 18, 2025 | hold | 4.25-4.50 | — |
| Jul 30, 2025 | hold | 4.25-4.50 | Bowman, Waller (−25) |
| **Sep 17, 2025** | **−25** ("shift in the balance of risks") | 4.00-4.25 | Miran (−50) |
| Oct 29, 2025 | −25; QT ends Dec 1 | 3.75-4.00 | Miran (−50); Schmid (hold) |
| Dec 10, 2025 | −25 | 3.50-3.75 | Miran (−50); Goolsbee, Schmid (hold) |
| Jan 28, 2026 | hold | 3.50-3.75 | Miran, Waller (−25) |
| Mar 18, 2026 | hold | 3.50-3.75 | Miran (−25) |
| Apr 29, 2026 (Powell's last as Chair) | hold, easing bias in statement | 3.50-3.75 | Miran (−25); Hammack, Kashkari, Logan (against the easing bias) |
| Jun 17, 2026 (Warsh's first) | hold, 12-0 | 3.50-3.75 | — |
| Jul 29, 2026 | hold, 9-3 | 3.50-3.75 | Hammack, Kashkari, Logan (**+25**) |
| **Sep 16, 2026** | **+25**, 12-0 | **3.75-4.00** | — |
| **Oct 28, 2026** | hold, 10-2 | 3.75-4.00 | Cook, Hammack (**+25**) |
| Dec 8-9, 2026 | — | — | FedWatch ~83% hike [S] |

Leadership: Powell's term as Chair ended in May 2026 (Cowen video "Powell Steps Down as Chair of the Federal Reserve", May 15, 2026 [S]). Kevin Warsh has been Chair since about late May 2026 ("Since becoming Chairman just five months ago", Oct 28 [V]). Stephen Miran joined as Governor in Sep 2025 and stopped appearing as a voter from June 2026 (12-0 vote) [V/I]. Lisa Cook remained a voting Governor despite the 2025 attempt to remove her [V/S].

### 7.2 Unemployment path (U-3, %) [V]
2024: 3.7 (Jan) → 4.2 (Jul-Aug) → 4.1 (Dec). 2025: 4.0 (Jan) → 4.2 (Feb-Apr) → 4.3 (May) → 4.1 (Jun) → 4.3 (Jul-Aug) → 4.4 (Sep) → [Oct missing] → **4.5 (Nov)** → 4.4 (Dec). 2026: 4.3 (Jan) → 4.4 (Feb) → 4.3 (Mar-May) → 4.2 (Jun) → 4.1 (Jul-Aug) → **4.2 (Sep)**.

### 7.3 CPI path (headline/core YoY, SA) [V/I]
2025: 3.0/3.3 (Jan) → 2.3/2.8 (Apr) → 2.7/2.9 (Jun) → 3.0/3.0 (Sep) → 2.7/2.6 (Nov) → 2.65/2.65 (Dec). 2026: 2.4/2.5 (Jan) → 2.4/2.5 (Feb) → 3.3/2.6 (Mar) → 3.8/2.7 (Apr) → **4.2/2.8 (May)** → 3.5/2.6 (Jun) → 3.3/2.5 (Jul) → 3.35/2.45 (Aug) → 3.7/2.6 (Sep). Core PCE: 2.8 (2025 average) → 3.1-3.2 (2026). Oil (Brent monthly average): $71 (Feb 2026) → $103 (Mar) → **$117 (Apr)** → $85 (Jun, after a June reopening memorandum [S]) → $114 (Sep) → $125 (Oct) [V/S].

### 7.4 Curve path [V]
- 2s10s: −0.47 (May 24, 2024, the 2024 daily low) → 0 (Aug 27, 2024) → +0.33 (Dec 2024) → +0.57 (Apr 2025) → +0.71 (Dec 2025) → **+0.74 (Jan 30, 2026 peak)** → +0.30 (Jun 2026) → +0.37 (Oct 29, 2026).
- 3m10y: −1.43 (Jan 2024) → +0.21 (Dec 2024) → −0.17 (Jun 2025) → +0.22 (Oct 2025) → +0.51 (Dec 2025) → +1.09 (Sep 2026) → +0.80 (Oct 29, 2026).
- 2025: a bull steepening (front end down with cuts) plus a stable term premium. 2026: the front end re-priced from cuts to hikes, giving bear flattening in 2s10s and steepening against bills.

### 7.5 Reading of the current state [I]
- **Policy**: mildly restrictive in nominal terms, near-neutral in real terms (+0.8 versus core PCE), below Taylor-rule prescriptions. Hawkish bias, data-light communication.
- **Inflation**: headline driven by an energy supply shock. Core CPI is contained (2.6) but core PCE is 3.1 and 3-month core momentum is about 3.4% annualised. Long-run expectations are anchored.
- **Labor**: tight-ish by unemployment and claims, but low-hire/low-quit, with falling participation and very slow payroll growth. The Sahm rule reads 0.
- **Curve**: positive, re-flattening. A 2s10s re-inversion would be the classic next step if hikes continue (the 1999-2000 template).
- **Credit**: tight spreads, so no stress signal.
- **Scenario framing, not a forecast.** (a) The 1990 template: an oil shock plus a hiking Fed tips a slowing economy into a short recession, with equities −20%. This is Cowen's late-cycle thesis. (b) The 1999-2000 template: hikes plus a capex boom extend the cycle; the curve re-inverts and the recession comes later (2027-28). (c) A soft re-landing: oil reverses (Hormuz reopening), headline inflation falls on base effects in spring 2027, and the Fed stops at one or two hikes. Base effects alone will pull headline YoY down sharply in Mar-May 2027 if oil merely stays flat.

---

## 8. Transmission to asset classes (summary)

| Driver | BTC / ETH / alts | S&P 500 / Nasdaq | Treasuries | US dollar (DXY / broad) | Gold | Reliability [I] |
|---|---|---|---|---|---|---|
| Hawkish surprise (hike or dots up) | − (alts most) | − (growth most) | front end −, curve flatter | + | − (via real yields) | High on the day; medium over months |
| Insurance cuts, no recession | + with lag (2019: BTC topped *before* the cuts; 1995/98 stocks +) | + (+11-29% in 12 m) | bull steepening | − | + | Medium |
| Recession cuts | − then + after the last cut | −35 to −55% (2001, 2008) | long bonds rally strongly | mixed (+ in crisis, − later) | + | High (conditional on recession) |
| Inversion | little direct effect | none reliable (stocks rose in 2006, 2019, 2023) | — | — | — | Low as a timing tool |
| Un-inversion via bull steepening | − historically (2001, 2008, 2020) | − within 0-7 m historically, but not 2024-26 | + | − | + | Medium; failed 2024-26 |
| Bear steepening / term-premium rise | − | − valuation pressure (Oct 2023) | long end − | ± | ± | Medium |
| Rising real yields | − | − long duration | — | + | − (broke 2022-24) | Medium-high |
| CPI upside surprise | − on the day | − | yields + | + | ± | High intraday |
| Energy supply shock | − (crypto fell H1 2026 [S]) | energy sector +, index ± | breakevens +, then real yields + | + | + early, − if real yields spike | Medium |
| Claims above ~300k / Sahm trigger | − | − | + (bull steepening) | − | + | Medium-high when confirmed by credit spreads |
| HY spread widening | − (high beta) | − | + | + | + | High as confirmation |

Crypto-specific context, kept brief because it belongs to other clusters. Several sources say BTC topped around **Oct 6, 2025** and fell to about $60k by Jul 1, 2026, with a 2026 base-building phase [S, low-confidence secondary]. Cowen: "Crypto is more sensitive to rate cuts and liquidity than the stock market is" [S]. The 2026 re-tightening fits with BTC lagging equities: the S&P made new highs in Oct 2026 while BTC was well below its 2025 peak [I].

---

## 9. Practical takeaways (educational, not advice)

1. **Ask *why* the Fed is moving.** Cuts into rising unemployment and widening credit spreads have historically been bearish for risk assets. Cuts with stable claims have been bullish. In 2026 the Fed is hiking into a supply shock, which history (1974, 1990, 2008) treats as a late-cycle risk, not a sign of strength.
2. **Use a dashboard, not a single signal.** Curve (timing unreliable), claims (timely), Sahm (confirms, does not forecast), credit spreads (the confirmation), the 2Y versus fed funds (direction of policy), core PCE momentum (3-month annualised), and 5y5y (anchoring). In 2024-26 every single-indicator recession call failed.
3. **Mind the data quirks.** Base effects (spring 2027), benchmark revisions, the Oct 2025 data gap, labor-supply shocks that distort unemployment and Sahm, and FRED's truncated HY OAS history.

---

## Sources

Primary (Fed, FRED, BLS):
- FRED CSV endpoint used for every series named above: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFEDTARU (and likewise for DFEDTARL, DFF, FEDFUNDS, DFEDTAR, UNRATE, U6RATE, SAHMREALTIME, CPIAUCSL, CPILFESL, PCEPI, PCEPILFE, PPIFIS, MICH, CUSR0000SAH1, CUSR0000SEHC, PAYEMS, ICSA, CCSA, JTSJOL, JTSQUR, CIVPART, DGS3MO, DGS2, DGS10, DGS30, GS10, GS2, TB3MS, T10Y2Y, T10Y3M, DFII10, T10YIE, T5YIFR, THREEFYTP10, BAMLH0A0HYM2, BAMLC0A0CM, WALCL, SP500, USREC, DCOILBRENTEU, DTWEXBGS)
- FOMC statement, Sep 16, 2026: https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf
- FOMC statement, Oct 28, 2026: https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- FOMC statements, 2025-26: https://www.federalreserve.gov/newsevents/pressreleases/monetary20250129a.htm, …20250319a, …20250507a, …20250618a, …20250730a, …20250917a, …20251029a, …20251210a, …20260128a, …20260318a, …20260429a, …20260617a, …20260729a, …20260916a (same URL pattern)
- Chair Warsh press conference, Sep 16, 2026: https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf
- Chair Warsh press conference, Oct 28, 2026: https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20261028.pdf
- SEP tables: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20240918.htm, …20251210.htm, …20260318.htm, …20260617.htm, …20260916.htm
- BLS preliminary benchmark, Aug 28, 2026: https://www.bls.gov/news.release/archives/prebmk_08282026.htm ; CES benchmark page: https://www.bls.gov/web/empsit/cesbmk.htm
- NY Fed yield-curve recession model FAQ: https://www.newyorkfed.org/research/capital_markets/ycfaq.html

Historical S&P 500 data:
- Shiller monthly S&P 500 (datasets/s-and-p-500): https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv

Benjamin Cowen material (transcript summaries, posts, secondary coverage):
- Rosetta channel index (video titles and dates): https://rosetta.to/u/intothecryptoverse/
- "Labor Market Holds Steady" (May 8, 2026): https://rosetta.to/u/intothecryptoverse/labor-market-holds-steady
- "Inflation Rises to 3.8%" (May 12, 2026): https://rosetta.to/u/intothecryptoverse/inflation-rises-to-3-8
- "FOMC: The End of an Era" (Apr 29, 2026): https://rosetta.to/u/intothecryptoverse/fomc-the-end-of-an-era
- "Bitcoin in a Late Business Cycle Environment" (Mar 27, 2026): https://rosetta.to/u/intothecryptoverse/bitcoin-in-a-late-business-cycle-environment
- "Stocks and Geopolitical Conflict" (Apr 7, 2026): https://rosetta.to/u/intothecryptoverse/stocks-and-geopolitical-conflict
- @intocryptoverse thread, Mar 3, 2024: https://threadreaderapp.com/thread/1764301220942868800.html
- X post on "recession" Google searches: https://x.com/benjamincowen/status/1720960708630688249
- X post on long-end yields after cuts (Jun 2025): https://x.com/benjamincowen/status/1939783091037356302
- Bankless, "Where is Crypto Going in 2026?" (Dec 2025): https://www.bankless.com/podcast/where-is-crypto-going-in-2026-ben-cowen
- BeInCrypto via Yahoo, "Benjamin Cowen Says Yields Could Fall After Midterms" (Oct 6, 2026): https://finance.yahoo.com/markets/crypto/articles/benjamin-cowen-says-yields-could-050200041.html
- Coin Edition, 3m10y recession comment (Oct 6, 2023): https://coinedition.com/yield-curve-inversion-raises-serious-recession-fears-analyst/
- Datawallet profile (low-confidence secondary; Aug 2026 memo): https://www.datawallet.com/crypto/who-is-ben-cowen
- Benzinga (Feb 2025; content not retrievable, 403): https://benzinga.com/markets/cryptocurrency/25/02/43706856/could-inflation-unemployment-derail-the-bitcoin-bull-run

Other secondary sources:
- Fed rate decision coverage, Oct 2026 (FedWatch December odds): https://www.cnbc.com/2026/10/28/fed-rate-decision-warsh-takeaways.html ; https://finance.yahoo.com/economy/policy/live/fed-meeting-live-updates-federal-reserve-october-meeting-kevin-warsh-161129201.html
- Raisin, Sep 2026 decision summary: https://www.raisin.com/en-us/news/fed-rate-decision-policy-breakdown-september-2026/
- 2026 Iran war fuel crisis: https://en.wikipedia.org/wiki/2026_Iran_war_fuel_crisis ; World Bank blog: https://blogs.worldbank.org/en/opendata/strait-of-hormuz-disruption-sends-oil-prices-surging
- First Trust on the final benchmark (Feb 12, 2026): https://www.ftportfolios.com/Commentary/EconomicResearch/2026/2/12/another-massive-payroll-revision ; on the 2026 preliminary benchmark: https://www.ftportfolios.com/Commentary/EconomicResearch/2026/9/10/bls-payroll-revisions-fall-back-in-line-down-just-79,000
- Wolf Street on the Sep 2025 preliminary benchmark (−911k): https://wolfstreet.com/2025/09/09/annual-benchmark-payroll-revisions-nonfarm-job-creation-for-12-months-to-march-chopped-by-911000-to-1-45-million-jobs-created/
- Saxo options brief (MOVE above 100, Sep 25, 2026): https://www.home.saxo/content/articles/options/bond-vol-overtakes-equity-vol---options-brief---25-september-2026-25092026
- Nelson (Hoover), "Milton Friedman and the second wave of the Great Inflation": https://www.hoover.org/sites/default/files/2024-04/Nelson%20-%20MiltonFriedmanSecondWaveGreatInflation.pdf
