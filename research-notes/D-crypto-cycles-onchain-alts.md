# Cluster D: crypto cycles, valuation models, on-chain, sentiment, dominance & altcoins, chart technicals (as used by Benjamin Cowen)

Research file for the "practical-macro-economy" course. Compiled on 2026-10-30. Educational only, not financial advice.

**Claim markers**
- **[V]** verified from a primary or reputable source (URL in Sources).
- **[V-calc]** computed by this researcher from primary data downloaded on 2026-10-30: Coin Metrics Community API daily BTC/ETH `PriceUSD`, `CapMVRVCur`, `SplyCur`, `HashRate`; DefiLlama stablecoin totals; alternative.me Fear & Greed history; CoinGecko `/global`; FRED `DFEDTARU`. Method notes are in §11. Coin Metrics prices are daily reference closes (UTC), so they differ slightly from exchange intraday highs and lows. Both are given where it matters.
- **[S]** secondary source or snippet (news article, aggregator, transcript summary).
- **[I]** my inference or interpretation.

---

## 0. Executive summary (the 12 things a reader must know)

1. **The 4-year rhythm held on timing. Amplitude did not hold.** In each of the last three cycles, BTC topped about 1,060 days after the previous cycle low: 1,067, 1,059 and 1,062 days on daily closes [V-calc]. The 2025 top (6 Oct 2025, ~$126.1k intraday) landed exactly on schedule, which supports Cowen's "topped within one week of when it historically tops" claim [S][V-calc]. The bear market that followed was the shallowest on record: -53% on closes and -54% intraday to the 30 Jun / 1 Jul 2026 low, against -84%, -84% and -77% before [V-calc][S].
2. **Diminishing returns are measurable.** Cycle-low-to-top multiples were 539x, 112x, 21x and 7.9x. Tops measured against a log-log "fair value" fit shrank from 11x to 6.6x, 3.0x and 1.23x. Bottoms sit at a nearly constant ~0.42–0.59x of fair value [V-calc]. Fixed thresholds such as "Mayer > 2.4", "MVRV Z > 7" or "Pi Cycle cross" therefore stopped firing at tops, while bottom zones stayed comparatively stable.
3. **The 2025 top was apathetic.** Crypto Fear & Greed peaked at only 74 around the October 2025 top, against 84 at the November 2021 top and 95 in February 2021 [V-calc]. Coinbase was ranked ~260th in the US App Store in September 2025 [S]. ETH/BTC was ~0.03–0.04 instead of 0.08–0.15, and there was no broad altseason. Cowen compares the 2025 top to the 2019 "apathy top" [S].
4. **Cowen's base case for 2026 was a midterm-year bear market with a Q4 low, "probably October."** His cycle-day count from the 21 Nov 2022 intraday low puts prior lows at days 1,432–1,436, which maps to 23–27 Oct 2026 [S][V-calc]. As of 30 Oct 2026 the price (~$78–80k) sits ~35% above the June low and no lower low has printed. Whether June was the low remains unresolved [V-calc].
5. **The 200-week SMA held again, approximately.** BTC printed one weekly close below it ($59,517 vs ~$62.4k, week ending 28 Jun 2026) plus two marginal closes in August, then reclaimed it [V-calc][S]. Unlike every prior bear, price never closed below the realized price (~$53–54k) [V-calc].
6. **Current state (late October 2026).** BTC ≈ $78–80k. 200W SMA ≈ $67.1k (price ~1.17x). BMSB = 20W SMA $72.4k / 21W EMA $76.5k, and price is above it, having regained it 23 Aug 2026. 50W SMA ≈ $76.0k. 200D ≈ $73.1k (golden cross 8 Sep 2026). Realized price ≈ $54k, MVRV ≈ 1.45, MVRV-Z ≈ 0.8. BTC dominance ≈ 59.4% (CoinGecko). ETH/BTC ≈ 0.029. Fear & Greed = 30 ("Fear") on 30 Oct after ~50 the prior week [V-calc][V].
7. **BTC dominance tracks liquidity regimes.** It fell in QE/ZIRP (2017 with global QE; 2020–21 QE: ~70% → ~39–40%). It rose through hikes and QT (2018–19: ~33% → ~70%+; 2022–25: ~40% → ~65% in May 2025). The 2024–26 ETF and institutional bid is concentrated in BTC, which adds a structural floor under dominance [S][I].
8. **ETH/BTC bottomed near QT end in both 2019 and 2025.** In 2019 the low was 6 Sep (0.0164), five weeks after the first cut (31 Jul) and as QT ended (1 Aug). In 2025 the low was 21 Apr (0.0181), three weeks after QT was slowed to a trickle (1 Apr). Both times, though, the ratio's bounce faded once the BTC bear market began [V-calc][V][S].
9. **Macro tightened again in 2026.** The Fed hiked 25 bp on 16 Sep 2026 to 3.75–4.00%, its first hike since 2023 [V]. The 10y was >5.2% and Brent >$100 (September 2026) [S]. That backdrop is consistent with BTC dominance staying ~58–61% and with no altseason [I].
10. **On-chain bottom signals fired early or only partially.** STH-MVRV < 1, supply-in-profit/loss cross, NUPL ~0.09 (vs negative before), Puell ~0.6–0.7 and a hash-ribbon capitulation (8 Jun → 26 Aug 2026) all occurred. Deeper classic capitulation readings (MVRV < 1, NUPL < 0) did not [V-calc][S].
11. **Sentiment hit record lows in 2026.** Fear & Greed printed an all-time low of 5 in February 2026 and stayed ≤20 on 98 days of 2026 [V-calc]. Cowen's social-interest gauge sat at ~0.2–0.25 (2018-like) in July–August 2026 [S].
12. **Practical meta-lesson [I].** Timing regularities (Q4 tops of the post-halving year, ~1,060 days low→top, ~1 year top→bottom, a midterm-year low) have been more robust than price-level regularities. Bands should be time-adjusted. Every indicator needs a "this time the amplitude is smaller" correction.

---

## 1. Snapshot as of 29–30 Oct 2026

| Metric | Value | Reading | Source |
|---|---|---|---|
| BTC price | $78,193 (CM close 29 Oct); ~$80.0k (Fortune, 29 Oct 08:45 ET) | ~-37% from ATH; +34% from June low | [V-calc], [S] Fortune |
| ATH | $126,198 intraday on 6 Oct 2025 (CMC); $124,824 daily close | Cycle top (Cowen and most analysts) | [S] Pintu/CMC, [V-calc] |
| Cycle low so far | $57,748 intraday on 1 Jul 2026; $58,525 daily close on 30 Jun 2026 | -54.2% / -53.1% | [S], [V-calc] |
| 200W SMA | ≈ $67.1k (Pintu: $67.49k) | Price ≈ 1.17x | [V-calc], [S] |
| 200W EMA | ≈ $69.6k | | [V-calc] |
| 50W SMA | ≈ $76.0k (Pintu: $75.8k) | Price above; reclaimed in week of ~20 Sep 2026 | [V-calc], [S] |
| BMSB (20W SMA / 21W EMA) | $72.4k / $76.5k | Last weekly close $80.0k is above the band (regained 23 Aug 2026) | [V-calc] |
| 200D SMA / 50D SMA | $73.1k / $81.9k | Golden cross 8 Sep 2026; Mayer Multiple 1.07 | [V-calc] |
| Pi Cycle (111D vs 2×350D) | $74.9k vs $152.2k | Far from a cross; no cross at all in the 2024–25 cycle | [V-calc] |
| Realized price | ≈ $54.1k (CM); $52.5k (crypto.news, 24 Oct) | MVRV 1.45, MVRV-Z ≈ 0.8 | [V-calc], [S] |
| STH realized price | ~$69k (crypto.news, 24 Oct) to ~$73.5–74.6k (21Shares, late Sep; NewHedge, 20 Oct) | Price is near the STH cost basis, so the cohort is at break-even | [S] |
| Log-log fair value (my fit) | ≈ $144k (±1σ band $72k–$288k) | Price ≈ 0.54x fair, -0.88σ | [V-calc] |
| BTC dominance | 59.37% (CoinGecko, 30 Oct 07:21 UTC); 59.5–60.1% (CMC-based reports) | 2026 range ~58–61% | [V], [S] |
| ETH dominance | 10.34% (CoinGecko) | | [V] |
| ETH/BTC | 0.0289 (CM, 29 Oct) | 2026 range 0.0257 (6 Jun) to 0.0352 (6 Jan) | [V-calc] |
| ETH price | ≈ $2,256 | ATH ~$4,950 on 24 Aug 2025 (intraday) | [V-calc], [S] |
| Stablecoin supply | ≈ $301–308B (DefiLlama) | Flat since the Oct 2025 top (+0.6% over 90 days) | [V-calc] |
| USDT.D | 6.79% (USDC 2.68%) | | [V] |
| Crypto Fear & Greed (alternative.me) | 30 "Fear" (30 Oct); 51 (29 Oct) | 2026 low 5 (Feb); 2026 high 78 (22 Sep) | [V-calc] |
| Altcoin Season Index | ~45–53 (late Oct 2026) | "Mixed" (75+ = altseason) | [S] |
| Hash rate (30d avg, CM est.) | ≈ 1,022 EH/s | -8% from Nov 2025 peak (~1,111); trough ~896 on 28 Jul 2026 (-19%) | [V-calc] |
| Fed funds | 3.75–4.00% (hiked 16 Sep 2026; held 28 Oct, 10–2 with two dissents for a hike) | Chair: Kevin Warsh | [V] FRED, [V] Fed |
| US spot BTC ETF holdings | ~1.29M BTC (late Sep 2026); trough 1.22M on 13 Jul 2026 | | [S] 21Shares, Pintu |

---

## 2. Cycles

### 2.1 Halvings (supply-side clock)
- **Definition.** Every 210,000 blocks (~4 years) the block subsidy halves. Halvings so far [V]:
  - block 210,000 on 28 Nov 2012 (50 → 25 BTC)
  - block 420,000 on 9 Jul 2016 (25 → 12.5)
  - block 630,000 on 11 May 2020 (12.5 → 6.25)
  - block 840,000 on 20 Apr 2024, 00:09 UTC (19 Apr in the Americas; 6.25 → 3.125)
  - next: block 1,050,000, estimated ~April 2028 [I]
- **Free data.** mempool.space and blockchain.com (block height). FRED `CBBTCUSD` gives Coinbase BTC price. TradingView `INDEX:BTCUSD` or `BITSTAMP:BTCUSD` give long history.
- **How Cowen uses it.** He anchors the "4-year cycle" to halvings and to cycle lows, and has said halvings matter less over time while the cycle may be driven as much by the liquidity and business cycle (midterm years, QT timing) [S]. In March 2026 he said: "Bitcoin tops when it always tops, like every cycle, it tops in the fourth quarter" [S Cointelegraph, 6 Mar 2026].
- **Reality check [I].** The halving's direct supply effect has shrunk geometrically. In 2024 the issuance cut was ~450 BTC/day (~$30M/day at the time), small next to ETF flows that sometimes exceeded $1B/day. The persistence of the cycle in 2025 therefore argues it is partly self-fulfilling (reflexive positioning) and partly coincident with US policy and election cycles: 2013/2017/2021/2025 are post-election years, and 2014/2018/2022/2026 are midterm years.

### 2.2 Cycle tops and bottoms (dates, prices, durations)

Intraday levels are approximate exchange or CMC prints [S]. Daily closes and durations are Coin Metrics [V-calc].

| Cycle | Low (prior) | Top | Low (after) | Low→top | Top→low | Low→low | Drawdown | Low→top multiple |
|---|---|---|---|---|---|---|---|---|
| 2011–15 | 18 Nov 2011, ~$2 | 4 Dec 2013, close $1,135 (intraday ~$1,150–1,160 Bitstamp; ~$1,240 Mt Gox late Nov) | 14 Jan 2015, close $176 (intraday ~$152–170) | 747 d | 406 d | 1,153 d | -84.5% close (≈-86/-87% intraday) | 539x |
| 2015–18 | 14 Jan 2015 | 16–17 Dec 2017, close $19,641 (intraday ~$19.8k; CMC ~$20.1k) | 15 Dec 2018, close $3,185 (intraday ~$3,122) | 1,067 d | 364 d | 1,431 d | -83.8% | 112x |
| 2018–22 | 15 Dec 2018 | 8–10 Nov 2021, close $67,542 (intraday ~$69.0k on 10 Nov) | 9 Nov 2022 close $15,758; intraday low 21 Nov 2022 ~$15.5k | 1,059 d | 366 d | 1,425 d (1,437 to 21 Nov) | -76.7% close (-77.5% intraday) | 21x |
| 2022–26 | 9/21 Nov 2022 | 6 Oct 2025, close $124,824 (intraday $126.1–126.3k) | 30 Jun 2026 close $58,525; 1 Jul 2026 intraday $57,748 (low so far) | 1,062 d (1,050 from 21 Nov) | 267 d (so far) | 1,329 d (so far) | -53.1% close / -54.2% intraday | 7.9x |

Halving → top: 371 d (2013), 525 d (2017), 546 d (2021), 534 d (2025) [V-calc]. The "~12–18 months after the halving" rule held, with the last three in a tight 525–546-day band.

Cycle low → next halving: 542, 513 and 528 days. If June 2026 is the final low, the gap to the ~April 2028 halving would be ~655 days, out of pattern. A Q4-2026 low would be back in pattern (~540) [V-calc][I]. This is one quantitative reason Cowen kept looking for a Q4 low.

Mid-cycle and double tops:
- **2013:** April 2013 (~$230 close, ~$266 intraday on 10 Apr) and December 2013.
- **2021:** 13–14 Apr 2021 (~$63.4k close / $64.8k intraday) and 10 Nov 2021.
- **2024:** a March 2024 pre-halving high of $73.1k close, followed by a 7-month range. This was the "mid-cycle" pattern of the 2024–25 cycle.

**Cowen's day-count framing [S][V-calc].**
- On 15 Aug 2026 Cowen posted "#BTC is now on day 1363 of the cycle". That count runs from the 21 Nov 2022 intraday low and puts prior bottoms at days ~1,432/1,436.
- 2022-11-21 + 1,432 days = **23 Oct 2026**. 30 Oct 2026 is day 1,439, so the "window" has just been reached.
- The June 30 low fell on day 1,317, ~115 days "early".
- Cowen also uses a calendar framing. In his 6 Jun 2026 video he gave this sequence: Feb low → spring lower-high → June sweep of the Feb low → counter-trend rally → "October low likely lower than June unless June brings a massive capitulation" [S transcript].
- His "three stages of a bear market" (video of 7 Jun 2026) [S]:
  - Stage 1: few accept it's a bear (Oct 2025 → Feb 2026).
  - Stage 2: about half accept it (Feb → Jun 2026).
  - Stage 3: the majority accept it (Jun → Oct 2026).
  - Reversals tend to come when ~75–80% are bearish.

**Independent test [I].** Low→top timing is extremely regular (σ ≈ 4 days across three cycles on closes). Top→low (406/364/366) is fairly regular. Low→low (1,153/1,431/1,425) is regular for only two observations. That is a tiny sample (n = 3–4) with heavy look-ahead in choosing the "low". Treat it as a prior, not a law.

### 2.3 Drawdowns and diminishing returns
- **Drawdowns:** -84.5% (2013–15), -83.8% (2017–18), -76.7% (2021–22), -53.1% so far (2025–26) [V-calc]. Even before 2026 the series was shrinking. The 2026 step change matches the much smaller 2025 blow-off: price was only 1.23x log-fair-value at the top versus 3.0x in 2021.
- **Top ROI from cycle low:** 539x → 112x → 21x → 7.9x. Each cycle's multiple is ~1/2.7–1/5 of the previous one [V-calc].
- **Cowen's "diminishing returns" vs "lengthening cycles" [S].** Diminishing returns means each top and each bottom is a smaller multiple of the last. It is well supported by the data. Lengthening cycles (popular in 2021) means each cycle stretches longer in time. It was not borne out: the 2021 and 2025 tops came on schedule. Cowen has said the two "are not mutually exclusive", and that a $64k top in 2021 would have been "diminishing returns without lengthening cycles" [S].
- **Running ROI from cycle low at the same day count** [V-calc]:
  - Day 1,000: 27.0x / 14.1x / 7.5x (2015, 2018, 2022 lows).
  - Day 1,400: 31.7x / 6.0x / 5.5x.
  - Day 1,432: 18.2x / 5.2x / 5.1x.
  - In "running ROI" space the 2022–26 cycle has tracked the 2018–22 cycle closely since day ~1,300. Cowen's "ROI from cycle bottom" charts show exactly this overlay.

### 2.4 Seasonality and the monthly-returns heatmap (2013–2025, close-to-close) [V-calc]

| Month | Median | Mean | Positive years |
|---|---|---|---|
| Jan | +0.9% | +4.4% | 7/13 |
| Feb | +12.3% | +13.2% | 10/13 |
| Mar | -2.1% | +12.9% | 6/13 |
| Apr | +8.2% | +12.2% | 8/13 |
| May | +9.0% | +10.0% | 7/13 |
| Jun | +1.8% | -0.7% | 7/13 |
| Jul | +8.1% | +7.9% | 9/13 |
| **Aug** | **-8.4%** | +1.0% | **4/13** |
| **Sep** | **-2.9%** | -3.2% | **5/13** |
| **Oct** | **+14.8%** | +19.9% | **10/13** |
| Nov | +8.9% | +41.4% (skewed by 2013) | 8/13 |
| Dec | -3.4% | +4.0% | 5/13 |

- **Calendar-year returns** (close to close): 2013 +5,286%, 2014 -56%, 2015 +34%, 2016 +126%, 2017 +1,337%, 2018 -74%, 2019 +94%, 2020 +305%, 2021 +60%, 2022 -64%, 2023 +156%, 2024 +121%, 2025 -6.3%, 2026 YTD -10.7% [V-calc]. 2025 was the **first post-halving "top year" to finish negative**.
- **2026 monthly** [V-calc]: Jan -10.1, Feb -14.9, Mar +1.9, Apr +11.9, May -3.5, Jun -20.5, Jul +7.4, Aug +24.9, Sep +6.4, Oct (to 29th) -6.4.
  - August 2026 (+25%) and September broke the "weak Aug/Sep" seasonality, which Cowen had flagged ("August and September are historically weak"; average midterm-August ≈ -10%) [S altcoinbuzz].
- **Q4 of the post-halving year:** 2013 +479%, 2017 +221%, 2021 +6%, 2025 -23% [V-calc]. The peak date crept earlier within Q4 (4 Dec → 17 Dec → 10 Nov → 6 Oct). In 2025 the "Q4 top" was the **first day** of Q4 strength, not a Q4 rally.
- **Midterm-year (US) Q4:** 2014 -17.6%, 2018 -44.2%, 2022 -15.0% [V-calc]. All three midterm years ended near the cycle low (Jan 2015 / Dec 2018 / Nov 2022). This is the empirical basis of Cowen's "the winning strategy has typically been to just DCA in the second half of the midterm year rather than try and time the exact bottom" [S].
- **Data/tools.** Heatmaps on CoinGlass, Bitcoin Magazine Pro, Into The Cryptoverse (paid), and TradingView "Seasonality".
- **Caveat [I].** n = 13 per month and n = 3 per regime: the noise is huge. October's strength is partly the 2013/2021/2023 bulls. A t-test on any single month is not significant at conventional levels.

---

## 3. Valuation and trend models

### 3.1 Logarithmic regression ("log regression bands", "rainbow")
1. **Definition.** Fit log(price) against log(time since genesis) (log-log, i.e., power law), or against log(time) with log price (Cowen's "logarithmic regression" curves). The fit gives a "fair value" curve, with upper and lower bands at fixed residual multiples or Fibonacci deviations.
   - The "Bitcoin Rainbow Chart" (Blockchaincenter / Über Holger, based on a 2014 bitcointalk log-regression) is a coloured version.
   - Cowen shows "logarithmic regression bands" and "fair value log regression" charts on intothecryptoverse.com (paid) and in his "The Beauty of Mathematics" video series (part 71 published 9 Jun 2026) [S rosetta].
   - Free versions: Bitcoin Magazine Pro "Rainbow Price Chart", blockchaincenter.net rainbow, TradingView community scripts such as "Logarithmic Regression Fib Deviation Bands" and the "Bitcoin Power Law Bands".
2. **My fit** (daily closes from Aug 2010; days since 3 Jan 2009) [V-calc]:
   - log10(P) = -16.305 + 5.628·log10(days), residual σ = 0.301 (factor ~2.0).
   - Fair value today ≈ **$144k**; ±1σ ≈ $72k–$288k.
   - Projected fair value: end-2026 ≈ $152k, end-2027 ≈ $206k, end-2028 ≈ $275k. These are curve values, not forecasts.
   - Residuals at tops: +3.47σ (2013), +2.72σ (2017), +1.57σ (2021), **+0.29σ (2025)**.
   - Residuals at bottoms: -0.88σ (2015), -0.76σ (2018), -1.14σ (2022), **-1.15σ (June 2026)**.
   - So tops are converging toward the curve, while bottoms hold a stable ~-0.8 to -1.15σ zone. Today price sits at -0.88σ.
3. **Common misreadings.** Treating fair value as a target. Assuming symmetric bands: a symmetric-σ model will never fire at a top again. The fit itself shifts as data arrive, and a constant residual σ is wrong because volatility decays. Linear-time log charts (log price vs linear time) imply exponential growth and overstate future fair value.
4. **Cowen.** He says fair value is "where price tends to return". When price is under fair value in a bear year it is "time-based capitulation" more than price capitulation [S]. Diminishing-returns bands (upper band decaying faster than lower band) are his core long-term framework.
5. **Takeaway.** Log regression is a decent map of where cycle lows have been and a poor guide to how high a top will go. Use asymmetric, time-decaying bands.

### 3.2 Cowen's risk metric (concept; proprietary)
- **What is public [S].** A 0–1 colour-coded "risk" (0 = historically low risk to accumulate, 1 = historically high risk) for BTC and many alts, on intothecryptoverse.com behind a paywall. Cowen has described it as based on price's extension from a long-term moving average or fair value, adjusted for diminishing returns. The exact formula is **not public**, and community TradingView "Benjamin Cowen's Simplified Risk Metric" scripts state they are approximations. He has added a separate "social risk" (§5.3) and in 2026 cited "MVRV Z-score bouncing rather than resetting below zero" under the risk heading [S Cowen memo].
- **How such a metric is built, generically [I]:**
  1. Choose a anchor: a 350D/400D/50W/200W SMA or a log-regression fair value.
  2. Compute the extension x(t) = ln(P/anchor).
  3. Correct for diminishing returns by multiplying x(t) by a time factor (e.g., t^k or e^{kt}, with k fitted so past tops share a similar height) or by dividing by a rolling or decaying envelope.
  4. Normalize to 0–1 with an all-time min–max (or percentile rank) of the adjusted series.
  5. Optionally smooth it, or average several sub-metrics (price-based, on-chain, social).
- **Strengths and pitfalls [I].** It converts a noisy chart into a single regime number, and the time adjustment fixes the "tops keep getting lower" problem. On the other hand, min–max normalisation is **re-fitted with hindsight**, so past readings change when new data arrive (repainting). The time-decay parameter is effectively chosen to make old tops line up. The 2025 top did not reach very high risk on simple versions; a 2025 top at 1.23x fair value is ~0.6–0.7 on a naive scale [I].

### 3.3 Bull Market Support Band (BMSB)
1. **Definition.** The zone between the **20-week SMA** and the **21-week EMA** of weekly closes. TradingView: add SMA(20) and EMA(21) on a 1W `BTCUSD` chart. Cowen coined and popularised the name. In bear phases he calls the same band the "bear market resistance band" (video "Bitcoin Closes Below the Bear Market Resistance Band", 1 Jun 2026) [S].
2. **Reading.** In bull markets, weekly closes above the band with pullbacks to it act as support. Losing it on weekly closes and failing the retest has marked the start of bears (Dec 2021, Nov 2025). In bears, the band is resistance until price reclaims it convincingly. Cowen has said "BTC tends to break below it on the first retest" [S].
3. **History of state changes on weekly closes** [V-calc]:
   - 2021: lost May 2021, regained Aug 2021, lost 5 Dec 2021.
   - 2022–23: regained 15 Jan 2023.
   - 2024: lost/regained repeatedly July–September 2024 (a chop that preceded the Q4 2024 breakout).
   - 2025: lost 9 Mar 2025, regained 27 Apr 2025, lost 19 Oct and then **2 Nov 2025** (the top confirmation).
   - 2026: brief regain 26 Apr, lost again 31 May, **regained 23 Aug 2026**. It has stayed above since; band now $72.4–76.5k.
4. **This cycle's twist.** Cowen argued in late 2025 that the 50W SMA acted as the "real" bull market support this cycle [S]. The 50W (~$76k now) is currently inside or just above the band.
5. **Takeaway.** The BMSB works as a regime filter, not a level. Multiple flips in sideways markets (2024) produce whipsaws.

### 3.4 200-week SMA and 200-week EMA
1. **Definition.** The mean of the last 200 weekly closes (~3.8 years, roughly one full cycle). The EMA weights recent data more and sits higher in uptrends. Bitcoin Magazine Pro has a "200 Week Moving Average Heatmap".
2. **Reading.** It has historically marked cycle lows. Price/200W at cycle lows [V-calc]: 0.92 (Jan 2015), 1.00 (Dec 2018), 0.66 (Nov 2022, the FTX capitulation and the deepest undercut), 0.94 (June 2026).
   - Weekly closes below the 200W [V-calc]: Aug–Sep 2015 (5 weeks), 15 Mar 2020 (1), Jun 2022–Mar 2023 (36), mid/late 2023 (11), **28 Jun 2026 ($59,517 vs $62,433)**, and marginal closes on 2 Aug and 16 Aug 2026.
   - At tops the multiple has collapsed: 16.9x (2017), 3.95x (2021), 2.33x (2025).
3. **Cowen.** In Nov 2025: "I think Bitcoin has a date with destiny (200 week moving average) in 2026, probably around $60k-$70k" [S X post, 17 Nov 2025]. On 29 Jun 2026: "The four year cycle strikes again. Bitcoin just had a weekly close below the 200W moving average. The first time it closed below the 200W moving average in 2022 was also in June" [S X]. He also argued that "the idea that the 4 year cycle 'failed' despite Bitcoin dropping below the 200W moving average in H2 of the midterm year seems wrong" [S X].
4. **Takeaway.** The 200W is a good "value zone" marker with surprisingly precise lows. It is not a floor: 2022 undercut it by 34%. It rises over time (now ~$67k), so time spent near it matters as much as the touch.

### 3.5 200-day SMA, 50-week SMA, golden/death cross, Mayer Multiple
- **200D SMA.** Now $73.1k. The standard bull/bear trend divider (TradingView SMA 200 on 1D).
- **Mayer Multiple** (Trace Mayer, ~2017) = price / 200D SMA. The classic thresholds (>2.4 "bubble", <1 "cheap") have decayed [V-calc]:
  - At tops: 5.71 (2013), 3.78 (2017), 1.48 (2021), **1.18 (2025)**. April 2013 was 8.26 and April 2021 1.97.
  - At bottoms: 0.40, 0.51, 0.67, **0.78**.
  - Now 1.07.
  - Bottom readings rising and top readings falling means the oscillator is **compressing**, like volatility.
- **Golden/death crosses (50D vs 200D)** since 2017 [V-calc]:
  - Death crosses: 30 Mar 2018, 26 Oct 2019, 26 Mar 2020, 19 Jun 2021, 15 Jan 2022, 11 Sep 2023, 10 Aug 2024, 7 Apr 2025, **16 Nov 2025**.
  - Golden crosses: 23 Apr 2019, 18 Feb 2020, 21 May 2020, 15 Sep 2021, 7 Feb 2023, 30 Oct 2023, 28 Oct 2024, 22 May 2025, **8 Sep 2026**.
  - These are lagging. Several crosses (2019, 2021, 2024, 2025) were near local extremes and reversed, which makes them contrarian as often as confirming. They are useful only as a description of regime.
- **50W SMA.** Now $76.0k. Cowen's July 2026 memo said a "sustained weekly reclaim" of the 50W (then ~$86.5k) would weaken the Q4-low thesis [S]. The 50W has since fallen to ~$76k as 2025's high prices rolled out, and price is above it.
  - This is a lesson in moving targets: a falling MA is easier to reclaim and does not mean the same thing as a rising one [I].

### 3.6 Pi Cycle Top indicator
1. **Definition.** The 111-day SMA crosses above 2× the 350-day SMA (Philip Swift, 2019; Bitcoin Magazine Pro chart).
2. **History of crosses** [V-calc]: 6 Apr 2013, 5 Dec 2013 (1 day after the top), 16 Dec 2017 (top day), **12 Apr 2021** (the April mid-cycle top, not November). **No cross in 2024–25**: the 111D peaked well below 2×350D.
   - Now: 111D $74.9k vs 2×350D $152.2k.
3. **Reading.** It worked 3–4 times when tops were parabolic. It fails structurally once blow-offs shrink, because the 2× multiplier is fixed while cycle amplitude decays. This is a textbook example of a fixed threshold meeting diminishing returns [I].
4. **Takeaway.** No signal is not evidence of no top (2021 November, 2025).

### 3.7 Stock-to-Flow (S2F) and why it failed
- **Definition.** PlanB (March 2019) regressed log market cap on log stock/flow ratio (stock = supply, flow = annual issuance). S2F doubles at each halving, so the model predicted a step-jump in "fair value" after each halving. The S2FX extension (April 2020) projected ~$288k average for 2020–24, and the model was widely read as ~$100k by end-2021.
- **Outcome [V-calc][I].** 2021 peaked at $69k. 2024–25 peaked at $126k versus S2F values that by 2024–25 implied several hundred thousand dollars. 2026 trades at ~$80k.
- **Why it failed [I]:**
  1. Spurious regression of two trending series: supply and price both trend up.
  2. It ignores demand and liquidity entirely.
  3. Out-of-sample n was tiny (two halvings).
  4. Issuance becomes irrelevant as flow → 0; after 2024 the daily issuance is dwarfed by ETF and treasury flows.
- **Cowen** was a long-time sceptic, arguing for diminishing returns over S2F's accelerating returns [S].
- **Takeaway.** A model with no demand variable and an exploding forecast should be treated as a narrative.

### 3.8 Power-law model
- **Definition.** Same idea as log-log regression. Giovanni Santostasi popularised it (with Harold Burger's "power law corridor"): price ∝ days^~5.7–5.8. My fit gives an exponent of 5.63 with a different start date and fit window [V-calc].
- **Status.** Bottoms have respected the lower corridor (June 2026 ≈ 0.45x fair, the same as Nov 2022). The 2025 top barely exceeded the mid-line.
- **Takeaway.** It is consistent with diminishing returns, but its proponents' "$1M by 2033"-type projections depend on the exponent staying fixed, which is untested [I].

### 3.9 RSI (weekly/monthly), bearish divergence; log vs linear scale; weekly/monthly closes
- **RSI(14) on 1W/1M.** Monthly RSI > ~90 marked 2013/2017 tops, ~80–85 in 2021, and lower in 2024–25 [S/I]. **Bearish divergence** (price higher high, RSI lower high) appeared on weekly and monthly charts into the 2021 and 2025 tops [S]. Bears end with weekly RSI ~25–30 (2015, 2018, 2022) and recover above 50 later.
- **Cowen** uses weekly RSI resets and divergences in "Bitcoin: Bearish Divergence" type videos [S]. Divergence can persist for months, so it is a warning and not a timer.
- **Log vs linear scale.** Log scale is mandatory for multi-year BTC charts: equal vertical distance means equal % change. Trendlines and regression only make sense in log space. Linear charts exaggerate recent moves.
- **Weekly and monthly closes.** Cowen emphasises closes (Sunday 00:00 UTC on most charts) over wicks. Example: the 200W "loss" was a weekly close (28 Jun 2026), not the intraday wick [S]. Exchanges differ in close times; CME futures add gap risk.

---

## 4. On-chain indicators

Free sources: Glassnode Studio (some free tiers), checkonchain.com, Bitcoin Magazine Pro, NewHedge, CryptoQuant, and the Coin Metrics Community API (used here).

### 4.1 Realized price and realized cap
1. **Definition.** Realized cap = Σ(each coin × price when it last moved), i.e., aggregate cost basis. Realized price = realized cap / supply. Cowen: "The realized price is essentially just equivalent to the realized cap of Bitcoin divided by the circulating supply" [S, video 11 Jun 2026].
2. **History** [V-calc]. Price traded below realized price for 304 days (Oct 2014–Oct 2015), 134 days (Nov 2018–Apr 2019) and 179 days (Jun 2022–Jan 2023). **In 2026: 0 days.** The low on 30 Jun 2026 ($58.5k) held ~10% above the realized price (~$53k).
3. **Cowen.** "Historically" dips below realized price near the end of bear markets, but "doesn't spend much time there". In June 2026 he flagged that not reaching it "would break some models" [S].
4. **Now.** ~$54k (CM). It rises slowly as coins change hands at higher prices.
5. **Takeaway.** Realized price is the network's aggregate cost basis. A bear market that never trades below it is evidence of either a shallower cycle (more stable holder base: ETFs and treasuries) or an incomplete capitulation. 2026 has not yet resolved which [I].

### 4.2 MVRV and MVRV Z-score
1. **Definition.** MVRV = market cap / realized cap (Murad Mahmudov & David Puell, 2018). MVRV-Z = (market cap − realized cap) / σ(market cap over all history) (Awe & Wonder, 2019).
2. **Thresholds and decay** [V-calc, CM data; Glassnode values differ slightly]:

| | MVRV | MVRV-Z |
|---|---|---|
| Top Apr 2013 | 5.64 | 10.7 |
| Top Dec 2013 | 4.72 | 7.7 |
| Top Dec 2017 | 4.43 | 9.4 |
| Top Apr 2021 | 3.43 | 5.4 |
| Top Nov 2021 | 2.85 | 3.5 |
| **Top Oct 2025** | **2.29** | **2.5** |
| Low Jan 2015 | 0.56 | -0.6 |
| Low Dec 2018 | 0.69 | -0.5 |
| Low Nov 2022 | 0.75 | -0.4 |
| **Low Jun 2026** | **1.10** | **+0.18** |
| **Now** | **1.45** | **~0.8** |

   The classic "Z > 7 = top zone, Z < 0 = bottom zone" rules failed at both ends this cycle.
3. **Cowen's July 2026 memo [S]:** the "MVRV Z-Score is bouncing rather than resetting below zero". He read it as a sign the full reset may not have happened. That is one argument for his Q4 lower-low scenario.
4. **Related:** "mean MVRV price" ~$97k (21Shares) [S]. STH-MVRV (short-term holders, <155 days) oscillates around 1. It was 1.15 in late September 2026 (highest since Nov 2025) and ~0.96 on 24 Oct 2026 [S]. The 1.0 level acts as support in uptrends and resistance in downtrends (Glassnode framing).

### 4.3 NUPL (Net Unrealized Profit/Loss)
- **Definition.** (market cap − realized cap) / market cap = 1 − 1/MVRV. Zones: <0 capitulation, 0–0.25 hope/fear, 0.25–0.5 optimism, 0.5–0.75 belief/greed, >0.75 euphoria.
- **Historical values.** Tops: >0.75 in 2013/2017; ~0.65–0.7 in 2021; ~0.56 in Oct 2025 (1 − 1/2.29) [V-calc]. Bottoms: -0.43 (2018), -0.31 (2022), **+0.09 (2026)** [S Pintu; consistent with CM MVRV 1.10 → 0.09].
- **Takeaway.** Same decay as MVRV. 2026 never went into "capitulation".

### 4.4 STH and LTH realized price and supply
- **Definition.** Glassnode splits coins into short-term holder (STH, <155 days) and long-term holder (LTH) cohorts.
- **Reading.** The STH cost basis is the line bulls must hold in bull markets and the ceiling in bears. LTH supply rises in bears (accumulation, "HODLing") and falls into tops (distribution).
- **2025 distribution.** LTH distribution was large in 2024–25, including old-whale sales (one ~80k BTC Satoshi-era sale through Galaxy in July 2025) [S]. ETFs absorbed it.
- **Now.** The STH cost basis is ~$69–75k depending on source and date, and price ~$78–80k is hovering on it [S].
- **Cowen** mostly refers to "cost basis of the network" (realized price) and the supply-in-profit/loss cross. STH metrics are more often from Glassnode or Checkmate [S].

### 4.5 Supply in profit / loss
- **Definition.** The % of supply whose last-move price is below the current price.
- **History.** Bottoms historically had ~40–50% in profit, with the % in profit dropping below the % in loss.
- **2026.** Cowen's July 2026 memo notes the "percentage crossed at the early-summer low, a condition the memo links to historical bottoming windows". Another video says the low historically comes ~1–4 months after that cross [S]. That puts the window at roughly July–October 2026 [I].

### 4.6 SOPR (Spent Output Profit Ratio)
- **Definition.** Realized value / value at creation of spent outputs (Renato Shirakashi, 2019). Above 1 means coins are moved at a profit. aSOPR excludes <1h outputs.
- **Reading.** In bears, SOPR < 1 means capitulation, and rallies to 1 meet resistance (break-even sellers). In bulls, 1 is support.
- **2026.** 90-day SOPR bottomed at 0.993 versus a prior cycle low of 0.987 [S Pintu]. That is a milder capitulation than 2022.

### 4.7 Puell Multiple
- **Definition.** Daily USD value of new issuance / its 365-day average (David Puell). Above ~4 has been historically "miner euphoria" and below ~0.5 "miner capitulation".
- **My computed values** (7-day average; issuance from supply change; approximate) [V-calc]:
  - Tops: 8.65 (2013), 5.84 (2017), 1.55 (2021), **1.17 (2025)**.
  - Bottoms: 0.44, 0.35, 0.59, **0.68 (June 2026)**.
  - Now ~1.1.
- **Caveat.** Halvings mechanically cut the numerator, so the 2024 halving depresses readings for a year. That is another reason fixed thresholds decay.

### 4.8 Hash rate, miner capitulation, hash ribbons
- **Hash Ribbons** (Charles Edwards, 2019): capitulation starts when the 30D SMA of hash rate falls below the 60D SMA. A "buy" signal comes after recovery (30D back above 60D, ideally with price momentum confirming).
- **History** [V-calc on CM estimates; daily estimates are noisy and create one-day flips]:
  - Major capitulations: Oct 2018 – Jan 2019; Mar – Apr 2020 (COVID); May/Jun – Aug 2021 (China ban); Jun – Aug 2022; Nov 2022 – Jan 2023; May – Jul 2024 (post-halving).
  - **2026:** Jan 6 – Feb 26, Mar 27 – May 10, and **8 Jun – 26 Aug 2026** (the longest).
- **Hash rate.** 30D average peaked ~1,111 EH/s (11 Nov 2025). Trough ~896 EH/s (28 Jul 2026, **-19%**, the largest drawdown since the 2021 China ban). Now ~1,022 EH/s [V-calc].
- **Reading.** Hash-ribbon recoveries came near the 2019, 2020, mid-2021, 2023 and Aug 2026 turning points. It is a lagging confirmation of miner stress ending, not a top signal.
- **Macro link [I].** Miner economics = hashprice (BTC price × subsidy / hash) − power cost. High energy prices (oil >$100 in Sept 2026) plus a post-halving subsidy squeeze both stress miners. AI-datacenter conversions also diverted miner capacity in 2025–26 [S].

### 4.9 Exchange balances
- **Definition.** BTC held on known exchange addresses (Glassnode, CryptoQuant).
- **Trend.** A multi-year decline since 2020 as ETFs, custodians and self-custody grew. "Exchange reserves down ~28,000 BTC in the final week of September 2026" [S 21Shares].
- **Caveat.** Address-labelling errors, and ETF custodian wallets (Coinbase Custody) blur the "exchange" meaning.
- **Takeaway.** It tells you more about market structure than about tops and bottoms.

### 4.10 CVDD, Terminal Price, Balanced Price
- **CVDD** (Willy Woo): cumulative value-days destroyed / (market age × 6 million). Historically it touched the absolute lows (2015, 2018, 2020 wick, 2022).
- **Balanced price** = realized price − transferred price (David Puell). Cowen notes it was ~$37.7k in 2026 and that prior cycle lows printed beneath it [S memo].
- **Terminal price** = transferred price × 21. It was cited as a model "arguing the low is not yet in" in June 2026 [S].
- **Takeaway [I].** These deep-value floors keep rising with the cost basis but have not been tested since 2022. In a shallower cycle they may never be tested again.

### 4.11 Coin Days Destroyed (CDD) and variants
- **Definition.** Coins × days since last moved, summed for spent outputs.
- **Reading.** CDD spikes mean old coins moving (LTH distribution) and tend to cluster near tops: 2017, 2021, and 2024–25 with large old-whale sales. Binary CDD, Supply-Adjusted CDD and dormancy are variants.
- **Takeaway.** It is a context indicator. With ETFs, much trading never touches the chain.

---

## 5. Sentiment and social indicators

### 5.1 Crypto Fear & Greed Index (alternative.me; API `api.alternative.me/fng/`)
- **Definition.** A daily 0–100 index from 2018: volatility 25%, momentum/volume 25%, social media 15%, surveys 15% (paused), BTC dominance 10%, Google Trends 10%. Other versions exist (CMC, CoinGlass, CFGI), so values differ by source.
- **Values at turning points** [V-calc]:

| Episode | F&G range |
|---|---|
| Dec 2018 low | 10–27 |
| Mar 2020 crash | 8–17 |
| Feb 2021 | all-time high 95 |
| Apr 2021 top | 70–79 |
| Nov 2021 top | 71–84 |
| Jun 2022 | 6–14 |
| Nov 2022 low | 20–40 |
| Mar 2024 | 75–90 |
| **Oct 2025 top** | **49–74** (no "extreme greed" at the top) |
| Feb 2026 | **5** (all-time low, 12 and 23 Feb) |
| Jun 2026 low | 11–23 |

  2026 had 98 days ≤20. The 2026 high was 78 (22 Sep). Now 30 (30 Oct).
- **Reading.** Contrarian at extremes, but extremes cluster and persist. Fear readings can last months (2022 and 2026) before a low. The index embeds price momentum, so it is partly circular.

### 5.2 Google Trends ("bitcoin", worldwide)
- **History.** The all-time high was December 2017. The May 2021 and November 2024 spikes were well below it. Search interest stayed muted at the 2025 ATHs ("retail is almost nowhere to be found", Bitwise's André Dragosch) [S].
- **Caveat.** Normalised 0–100 per query and window, and the methodology changed in 2022. Compare within one download only.

### 5.3 YouTube views and subscribers; Cowen's "social risk" / social interest
- **What it measures.** Cowen tracks a 30-day MA of views across major crypto YouTube channels, plus a composite "social interest/risk" from Google Trends, Coinbase app rank, YouTube views/subscribers and X followers [S].
- **Readings:**
  - Jan 2026: crypto-YouTube views at the lowest since January 2021 [S].
  - Jul 2026: social interest ~0.25, "the same level as 2018" and below ~0.5 in the 2022 bear. Major-channel YouTube views ~358k/day, ~91% below 2021. His quote: "Frankly, there are dozens of us left at this point" [S Sahm Capital/Webull, 23 Jul 2026].
  - Aug 2026 transcripts: ~0.2, matching August 2018 [S].
- **Cowen's interpretation.** Apathy, not euphoria, characterised the 2025 top, as in 2019. He expected social interest to keep falling for 6–12 months [S]. Separately, he argued a "structural reputation problem" (scams, memecoins) may depress retail interest independent of the cycle [S BeInCrypto].
- **Takeaway [I].** Social metrics now lag as top signals because retail never came. They may still mark bottoms, since apathy lows coincided with 2015/2018/2022 lows. Cowen's own channel is in the sample, which creates selection bias.

### 5.4 Coinbase App Store ranking
- **History.** #1 overall US iPhone app in Dec 2017 and in 2021 [S]. Jumped 55th → 3rd in Nov 2024. 137th in Jul 2025 and **~260th in Sep 2025**, during ATHs [S The Block/Cointelegraph].
- **Caveat.** ETFs moved retail exposure into brokerage apps, so app rank understates participation.

### 5.5 Funding rates and open interest (CoinGlass, Coinalyze, Velo; TradingView `BTCUSDT.P` funding)
- **Definitions.** Perpetual funding is paid long→short when positive. OI is total open derivative contracts.
- **Reading.** Persistent high positive funding plus rising OI means crowded leverage and liquidation risk. Negative funding in downtrends often marks local lows (short squeezes).
- **Key events:**
  - 10–11 Oct 2025: a record ~$19B of liquidations after a US–China tariff shock, four days after the ATH. Many analysts mark this as the market-structure break of the cycle [S].
  - 5 Feb 2026: ~$2.65B single-day liquidations [S].
  - 21 Sep 2026: a short squeeze (~$650M shorts liquidated); funding "briefly turned negative" afterwards [S 21Shares].
- **Cowen** rarely uses funding as a primary signal. He treats leverage flushes as noise inside the cycle framework [I].

### 5.6 ETF flows (Farside Investors, SoSoValue; issuer sites)
- **Background.** US spot BTC ETFs launched 11 Jan 2024. Cumulative net inflows since then exceed $55B (Glassnode via 21Shares) [S].
- **2026 flows:** -$5.6B YTD at end-July; August +$3.5B; September +$2.6B (including ~$1B days on 21–22 Sep). Holdings bottomed at 1.22M BTC on 13 Jul 2026 and were ~1.29M BTC (>6% of supply) by late September [S].
- **Reading [I].** Flows are pro-cyclical: they chase price and amplify trends. Since 2024 they dominate marginal demand, which helps explain both the higher bottoms (sticky holders) and the muted tops (less retail leverage).
- **Cowen:** "To pretend like it's different this time because of some narrative on Wall Street…" [S CMC Academy]. In other words, ETFs don't cancel the cycle.

### 5.7 Stablecoin supply growth (DefiLlama `stablecoins.llama.fi`; TradingView `CRYPTOCAP:USDT`, `USDT.D`, `USDC.D`)
- **History** [V-calc]:
  - 2021 boom: supply +125% over 90 days (Apr 2021).
  - Peak $188B (2 Apr 2022), then a contraction to a $123B trough (19 Aug 2023) during QT and hikes.
  - Re-expansion to $300.8B at the Oct 2025 top (+18.7% over 90 days).
  - **Flat at ~$300–310B for the whole 2026 bear** (90-day growth -1.6% at the June low, +0.6% now).
- **Reading.** Stablecoin growth is crypto's internal "M2". A stalled stablecoin supply has coincided with bear phases (2022–23, 2026). Re-acceleration preceded 2023–24 recoveries. The growth rate (90-day %) matters more than the level.

---

## 6. Dominance and altcoins

### 6.1 Definitions and tickers (TradingView)
- `CRYPTOCAP:BTC.D` is BTC market cap / total crypto market cap, including stablecoins. CoinMarketCap, CoinGecko and TradingView differ by ~1–2 points because of coin coverage.
- `CRYPTOCAP:ETH.D`
- `CRYPTOCAP:TOTAL` (all), `TOTAL2` (ex-BTC), `TOTAL3` (ex-BTC, ex-ETH)
- `CRYPTOCAP:OTHERS` (outside the top-10) and `OTHERS.D`
- `CRYPTOCAP:USDT.D`, `USDC.D`, `STABLE.C.D` (stablecoin dominance)
- `BINANCE:ETHBTC` and alt/BTC pairs (`SOLBTC`, etc.)
- **Altcoin Season Index** (blockchaincenter.net): the % of the top-50 coins (ex-stablecoins and wrapped tokens) that outperformed BTC over 90 days. ≥75 means "altseason" and ≤25 means "Bitcoin season". CMC's version uses the top 100 [S].

### 6.2 BTC dominance history [S unless noted; source spreads ±1–2 pts]

| Date | Level | Note |
|---|---|---|
| Pre-2017 | ~80–95% | |
| Jun 2017 | ~37–38% | ICO boom; ETH/BTC ATH |
| **Jan 2018** | **32.4%** (CMC daily, 14 Jan); CoinGecko 31.1% | All-time low; BTC topped a month earlier (Dec 2017) |
| Sep 2019 | ~70–73% | Peak around 10 Sep; QT ended 1 Aug 2019 |
| Jan 2021 | ~70% | |
| **May 2021** | **~39–40%** (39.3% on 19 May 2021) | |
| Late 2022 | ~38–40% | |
| **May 2025** | **~65%** (64.98–65.2% first week of May; 65% June 2025 per some sources) | Highest since early 2021 |
| Jul–Aug 2025 | slipped to ~57–61% | ETH run toward ATH |
| 2026 | ~58–61% | High ~60.6% on 5 May 2026; ~59.4% (CoinGecko) / ~59.5–60% (CMC) late Oct |

Ex-stablecoins, BTC's share is ~67% [S].

- **Cowen.** He spent 2023–24 arguing dominance would keep rising toward ~60% while QT continued, and was correct. In Nov 2024: "BTC dominance has retraced to the 0.618 Fib (60%), which marked the top for dominance last cycle" [S X].
- **2025 top [S].** He argued "no one left to sell the altcoins to" and that this cycle's top was "apathy rather than euphoria".

### 6.3 ETH dominance and ETH/BTC [V-calc unless noted]
- **ETH/BTC history:**
  - **ATH 0.146 on 12 Jun 2017** (intraday ~0.15).
  - Secondary Jan–Feb 2018 peak ~0.113.
  - QT bleed to **0.0164 (6 Sep 2019)**.
  - 0.0255 at end-2020, then **0.0877 (8 Dec 2021)**; Merge-era 0.0847 (7 Sep 2022).
  - Long bleed to **0.0181 (21 Apr 2025)**, the lowest since 2019. Some exchange prints are ~0.0177.
  - Bounce to **0.0422 (24 Aug 2025)**, when ETH made a nominal ATH (~$4,950 intraday; $4,831 close on 22 Aug) but the ratio stayed far below 2017/2021.
  - 0.0352 (6 Jan 2026) → **0.0257 (6 Jun 2026)** → 0.0327 (13 Sep, per [S]) → **0.0289 now**.
- **ETH dominance:** ~10.3% now (CoinGecko). It peaked ~20–22% in 2021 and ~30%+ briefly in 2018 [S].
- **Cowen on ETH/BTC [S X/Daily Hodl]:**
  - "ETH/BTC bottomed when QT ended" (2019).
  - "In 2019, ETH/BTC bottomed about 5 weeks after the 1st rate cut".
  - No clear reason to assume the bleed is over "until quantitative tightening ends".
  - Nov 2024: "For the 1st time in 3 years, there is an actual chance that ETH/BTC has bottomed… 0.03465". That was premature: the ratio fell another ~48%.
  - 2025: he accurately expected the bottom around QT slowing and ETH/USD support breaking (the "2019 wedge" analogy).

### 6.4 When alts outperformed and why they bleed in tightening
- **Outperformance windows [S/V-calc]:**
  - May–Jun 2017 and Dec 2017–Jan 2018: BTC.D 38% → 32% while BTC itself had already topped (17 Dec). The ETH/USD top came on 13 Jan 2018.
  - Q1–Q2 2021: index peak 98 on 16 Apr 2021; BTC.D ~70% → ~40%. This was during $120B/month QE and ZIRP.
  - Brief bursts: Feb 2024, Nov–Dec 2024 (post-election), Jul–Aug 2025 (ETH-treasury companies, BTC.D 65 → ~57–58%).
- **Why alts bleed in tightening [I, consistent with Cowen's framing]:**
  1. Alts are higher-beta, longer-duration risk assets with weaker cash-flow anchors, so a rising discount rate hurts them more.
  2. Liquidity contraction shrinks the speculative marginal buyer first.
  3. Alt supply keeps inflating (token unlocks, new listings), while BTC supply is nearly fixed.
  4. Institutional flows, ETF demand and corporate treasuries concentrated in BTC in 2024–26. Spot ETH ETFs (Jul 2024) drew far less, until the mid-2025 ETH-treasury-company fad.
  5. Index dilution: thousands of new tokens split the alt bid.
- **Counter-examples [I]:**
  - 2017's altseason occurred during Fed hikes (but with global QE and the ICO mania).
  - Sep 2024 rate cuts did not stop the ETH/BTC bleed, because QT continued until 2025.
  - The Apr 2025 ETH/BTC low and Aug 2025 bounce happened before the Fed's Sep 2025 cut.
  - The policy link is real but loose, and works through liquidity (QT/QE, dollar, stablecoin growth) more than through the policy rate alone.

### 6.5 USDT.D and stablecoin dominance
- **Definition.** Stablecoin market cap / total crypto market cap. It rises when risk assets fall (the denominator shrinks) and money parks in stables.
- **Reading.** It inversely mirrors TOTAL. Breaks of USDT.D support or resistance are used as risk-on/off confirmation.
- **2026.** USDT.D ~6.8% plus USDC.D ~2.7% now [V]. It rose through the 2026 drawdown as stable supply held flat while crypto market cap fell.

### 6.6 OTHERS.D and TOTAL3
- **What they show.** The "long-tail alt" gauges.
- **History.** OTHERS.D made lower highs in each cycle since 2021. TOTAL3 failed to exceed its 2021 high in real terms through most of 2024–26 [S/I]. The 2024–26 cycle is the first in which BTC made decisive new highs while the median alt never recovered its 2021 high: a "narrow" crypto bull, analogous to mega-cap concentration in equities [I].

---

## 7. Relationship analysis

### 7.1 What led tops and bottoms (sequence by episode)

| Episode | Earliest warnings (lead) | Coincident | Lagging confirmation |
|---|---|---|---|
| **Dec 2013 top** | MVRV ~4.7, Mayer 5.7; Pi Cycle crossed 5 Dec (+1 day); post-halving +371 d | Mt Gox / China PBoC ban news (5 Dec 2013) | Price < BMSB early 2014; Mt Gox collapse Feb 2014 |
| **Jan 2015 bottom** | MVRV < 1 from Oct 2014 (3 months earlier); price < realized price; Puell ~0.4 | Capitulation day 14 Jan | 200W reclaim; realized price reclaimed Oct 2015 (9 months later) |
| **Dec 2017 top** | Fed hiking + QT announced (Sep 2017; started Oct 2017); ETH/BTC peaked 6 months before (Jun 2017); Google Trends max; Coinbase #1 | Pi Cycle cross on the top day; MVRV-Z 9.4; F&G n/a | Death cross Mar 2018; BTC.D bottomed Jan 2018 (alts topped after BTC) |
| **Dec 2018 bottom** | Hash-ribbon capitulation from 30 Oct 2018; MVRV < 1 from 19 Nov | Fed hike 19 Dec 2018 then the "Powell pivot" (Jan 2019); F&G ~10 | QT ended Aug 2019; ETH/BTC bottomed Sep 2019 (alts lagged BTC by ~9 months) |
| **Apr 2021 mid-top / Nov 2021 top** | Apr: Pi Cycle, MVRV-Z 5.4, F&G 70–79, alt index 98. Nov: weekly RSI bearish divergence, lower MVRV high (2.85) | Fed taper announced 3 Nov 2021 (one week before the top); CPI at 6.2% | BMSB lost 5 Dec 2021; death cross Jan 2022; first hike 16 Mar 2022; QT Jun 2022 |
| **Nov 2022 bottom** | Hash-ribbon capitulation; price < realized price from Jun 2022; stablecoin supply contracting | FTX collapse (8–11 Nov); MVRV 0.75; F&G ~20 | CPI peak Jun 2022 → disinflation; BMSB regained 15 Jan 2023; golden cross Feb 2023; Fed's last hike Jul 2023 |
| **Oct 2025 top** | ~1,060 d from low (timing); weak breadth (ETH/BTC ~0.03–0.04, alt index never ≥75 in Q4); apathetic social; Coinbase ~260th; stablecoin growth slowing; lower MVRV high (2.29) | 10 Oct 2025 ~$19B liquidation cascade; Fed cutting (Sep/Oct 2025) and QT end announced 29 Oct | BMSB lost 2 Nov 2025; death cross 16 Nov 2025; F&G "extreme fear" mid-Nov; Feb 2026 crash |
| **Jun/Jul 2026 low (provisional)** | F&G record low 5 (Feb); social interest at 2018 levels; hash-ribbon capitulation from 8 Jun; supply-in-profit/loss cross | 200W SMA weekly close below (28 Jun); ETF holdings trough 13 Jul (1.22M BTC) | Hash-ribbon recovery 26 Aug; BMSB regained 23 Aug; golden cross 8 Sep; 50W reclaimed Sep. Missing: MVRV < 1, realized-price test, Fed easing (the Fed hiked in Sep 2026) |

**Patterns [I]:**
1. **Timing** indicators (days from low, Q4 of the post-halving year) were the best top-leads this cycle. **Valuation-extreme** indicators (MVRV-Z, Mayer, Pi, Puell) fired in parabolic cycles (2013/2017) but under-fired in 2021 and failed in 2025.
2. **Bottoms** are best flagged by combinations: realized price / MVRV ≈ 1, the 200W touch, hash-ribbon capitulation, F&G <15 for weeks, and social apathy. The combo is more robust than any single indicator.
3. **Alts lag BTC** at both turns. They top after BTC (Jan 2018) or in a blow-off before BTC (Apr/May 2021, Aug 2025 for ETH). They bottom later in BTC terms (ETH/BTC Sep 2019 vs BTC Dec 2018; ETH/BTC Apr 2025 vs BTC Nov 2022).
4. **Macro.** The Fed's turn toward tightening (taper Nov 2021; QT Sep/Oct 2017) coincided with or preceded tops. The end of QT or the first cuts have come *after* BTC lows but near ETH/BTC lows (2019, 2025).

### 7.2 BTC dominance and ETH/BTC vs Fed policy (FRED `DFEDTARU`, `WALCL`) [V FRED][V-calc][S]

| Fed regime (dates) | BTC.D | ETH/BTC | Fit with "tightening → BTC.D up, ETH/BTC down"? |
|---|---|---|---|
| Hikes 16 Dec 2015 → 20 Dec 2018 (0.25 → 2.50 upper); QT Oct 2017 → Jul 2019 | 2017: fell to 32% (global QE, ICO boom) despite hikes; 2018–19: rose to ~70% during QT | 0.146 Jun 2017 peak → 0.0164 Sep 2019 | 2017 contradicts; 2018–19 fits |
| Cuts 31 Jul, 18 Sep, 30 Oct 2019; QT end 1 Aug 2019 | Peaked ~Sep 2019 | **Bottom 6 Sep 2019** (5 weeks after the first cut) | Fits (Cowen's anchor case) |
| Emergency cuts 3 & 15 Mar 2020 to 0–0.25%; unlimited QE (WALCL ~$4.2T → ~$8.9T by 2022) | ~70% (Jan 2021) → ~39–40% (May 2021) | 0.023 (Mar 2020) → 0.0877 (Dec 2021) | Fits strongly (alts lagged QE by ~9–12 months) |
| Taper announced 3 Nov 2021; hikes 16 Mar 2022 → 26 Jul 2023 (0.50 → 5.50 upper); QT from 1 Jun 2022 | ~40% (late 2022) → 54% (2023) → ~57–60% (2024) | 0.085 (Sep 2022) → 0.038 (Sep 2024) | Fits |
| Cuts 18 Sep, 7 Nov, 18 Dec 2024 (5.50 → 4.50 upper); QT continuing (Treasury cap cut Jun 2024) | Kept rising to ~60–62% | Kept falling (0.0385 at the first cut) | Rate cuts alone **did not** reverse it; QT continued |
| QT slowed 1 Apr 2025 (Treasury runoff cap ~$5B/month) | Peaked ~65% (early May 2025) | **Bottom 21 Apr 2025 (0.0181)** → 0.0422 (24 Aug) | Fits the "balance sheet over rates" version |
| Cuts 17 Sep, 29 Oct, 10 Dec 2025 (→ 3.50–3.75%); **QT ended 1 Dec 2025** | ~57–61% | 0.032–0.036 (Dec 2025–Jan 2026) | BTC topped 6 Oct 2025, ~2 months before QT ended (the same as 2019: BTC top 26 Jun 2019, QT end 1 Aug) [S Cowen] |
| Hold Jan–Jul 2026; **hike 16 Sep 2026** (→ 3.75–4.00%); hold 28 Oct 2026 (two dissents for a hike); 10y >5.2%, Brent >$100 (Sep 2026) | ~58–61% | 0.0257 (Jun) → ~0.029 | Consistent with no altseason under renewed tightening |

**Interpretation [I]:**
- Dominance and ETH/BTC respond to *net liquidity* (balance sheet, reserve levels, dollar, stablecoin growth) more than to the policy-rate level.
- The cleanest signals were the QT end in 2019 and the QT slowdown in April 2025.
- ETH/BTC bottoms within ~0–6 weeks of a balance-sheet turn in two of two cases. That is n = 2, so it is suggestive and not reliable.
- The 2026 hike cycle is an out-of-sample test. A BTC.D that stays ~60% with ETH/BTC <0.035 would be consistent with the framework.

### 7.3 How on-chain and sentiment line up with macro [I, with dated evidence]
- **Rate shocks and real yields → leverage flush → sentiment extremes → on-chain capitulation**, in that order:
  - 2022: CPI peak and 75 bp hikes (Jun 2022) → F&G 6 (Jun 2022) → price < realized price (13 Jun 2022) → hash-ribbon capitulation (9 Jun) → final low after the FTX shock (Nov 2022).
  - 2026: tariff shock and liquidations (Oct 2025) → F&G 5 (Feb 2026) → hash-ribbon capitulation (Jun 2026) → 200W close below (28 Jun) → low (30 Jun / 1 Jul). The hawkish Fed (hike 16 Sep) did **not** produce a new low (Sep +6.4%), a notable divergence.
- **Stablecoin supply** turned flat with or slightly before the Oct 2025 top (+18.7% over 90 days at the top but decelerating) and stayed flat through 2026. That is consistent with crypto-native liquidity stalling while ETF flows set the marginal price.
- **Social apathy and dominance.** High BTC.D (alts not rotating) and low social interest go together (2019, 2025–26). Cowen ties the July 2026 apathy to "rising Bitcoin dominance and altcoins failing to rotate" [S].
- **The equities link** (detail in other clusters). BTC's 2022 low came one month after the S&P 500's Oct 2022 low. In 2025–26 BTC decoupled downward from strong equities for much of the year. That fits Cowen's "apathy top in a late-cycle economy" framing and his citing of 1962–82 S&P apathy tops [S].

---

## 8. Testing the narratives (including Cowen's)

| Claim | Evidence for | Evidence against / caveats | Verdict [I] |
|---|---|---|---|
| "4-year cycle is intact" | Top on schedule (1,062 d vs 1,059/1,067); Q4 post-halving top; 2026 bear; midterm-year weakness H1 2026 | Drawdown far smaller (-53%); low possibly ~115 d early (June); 2025 a negative "top year"; n = 3 | Timing intact, amplitude broken |
| "Bottom in October 2026" (Cowen base case) | Low-to-low ~1,425–1,437 d → late Oct 2026; midterm-year Q4 lows 2014/2018/2022; MVRV-Z and realized price not reset | As of 30 Oct, price +34% above the June low; golden cross, BMSB and 50W reclaimed; ETF holdings rising | Unresolved at time of writing. The window is now open; a lower low would vindicate the full-cycle model, and a higher low would mean "early bottom" (like 2018's early-ish low vs 2015) |
| "200W SMA is the bear-market floor" | June 2026 low ~0.94x 200W; 2015 0.92x; 2018 1.00x | 2022 0.66x; marginal closes below for weeks | A zone, not a line |
| "Alts need Fed easing" | 2019 and 2025 ETH/BTC lows near QT turns; 2021 altseason in QE | 2017 altseason in a hiking cycle; 2024 cuts didn't help; ETF concentration is structural | Liquidity matters, but structure (supply inflation, institutional BTC preference) now dominates |
| "S2F / Pi Cycle / MVRV-Z > 7 call tops" | Worked in 2013/2017 | Failed 2021 (Nov) and 2025 | Retire fixed thresholds; use time-decaying ones |
| "Sentiment extremes mark bottoms" | F&G <10 in Jun 2022, Feb 2026, Mar 2020 | Feb 2026 at 5 was not the low (June was lower) | Necessary-ish, not sufficient; extremes can repeat |

**Cowen's known misses [S].**
- He expected BTC to stall below ~$35k in Q4 2023, which did not happen.
- His Nov 2024 "ETH/BTC may have bottomed at 0.0347" call was premature by five months and ~48% in ratio.
- These are useful for teaching that his framework is probabilistic, as he himself says: "All models are wrong, some are useful."

---

## 9. Practical investor takeaways (educational)
1. **Cycle clock.** Know where you are in the cycle: days since the last low, the post-halving year, the midterm year. In BTC, timing patterns have been more reliable than price-level targets.
2. **Bands.** Read valuation bands as asymmetric and decaying. Expect smaller multiples at tops (MVRV ~2–3, Mayer ~1.2–1.5) and roughly stable bottom zones (realized price, 200W, ~0.45x log-fair-value).
3. **Bottoms.** Look for confluence: realized price or 200W, MVRV ≤ ~1.1, hash-ribbon capitulation, F&G <15 for weeks, and social apathy. No single indicator is enough.
4. **Alt regime.** Altcoin exposure is a bet on a liquidity regime change. Watch QT/QE, stablecoin growth, BTC.D losing ~58% and ETH/BTC trend before assuming altseason. Dominance has stayed ~58–65% since 2024.
5. **Composite scores.** Treat any composite risk or sentiment score as a summary of a few inputs: understand what's inside, and beware hindsight-fitted normalisation.

---

## 10. Quick reference: data sources and tickers

| Indicator | Free source / ticker |
|---|---|
| BTC/ETH price, long history | TradingView `INDEX:BTCUSD`, `BITSTAMP:BTCUSD`, `BINANCE:ETHBTC`; FRED `CBBTCUSD`, `CBETHUSD`; Coin Metrics Community API |
| MAs, BMSB, Mayer, Pi Cycle | TradingView (SMA/EMA on 1W/1D); Bitcoin Magazine Pro (Pi Cycle Top, Mayer, 200WMA heatmap) |
| Realized price, MVRV, MVRV-Z, NUPL, SOPR, STH/LTH, supply in profit | Glassnode Studio, checkonchain.com, NewHedge, CryptoQuant, Bitcoin Magazine Pro; Coin Metrics `CapMVRVCur` |
| Puell, hash rate, hash ribbons | Bitcoin Magazine Pro, Glassnode, mempool.space, Coin Metrics `HashRate` |
| CVDD, balanced price, terminal price | Bitcoin Magazine Pro, Glassnode, checkonchain |
| Fear & Greed | alternative.me (API), CMC, CoinGlass |
| Google Trends | trends.google.com ("bitcoin", worldwide, 5y/all) |
| Coinbase app rank | appfigures / Sensor Tower (paid); news trackers |
| Funding, OI, liquidations | CoinGlass, Coinalyze, Velo |
| ETF flows | farside.co.uk, SoSoValue |
| Stablecoins | DefiLlama stablecoins, TradingView `USDT.D`, `USDC.D` |
| Dominance and total caps | TradingView `CRYPTOCAP:BTC.D`, `ETH.D`, `TOTAL`, `TOTAL2`, `TOTAL3`, `OTHERS`, `OTHERS.D`; CoinGecko / CMC |
| Altseason | blockchaincenter.net/en/altcoin-season-index; CMC Altcoin Season Index |
| Fed policy | FRED `DFEDTARU`, `DFEDTARL`, `WALCL`, `RRPONTSYD`, `WRESBAL` |
| Cowen | YouTube @benjaminjcowen; intothecryptoverse.com (paid risk, charts); X @benjamincowen / @intocryptoverse; benjamincowen.com reports; rosetta.to/u/intothecryptoverse (transcripts) |

---

## 11. Method notes (for [V-calc])
- **Data:**
  - Coin Metrics Community API v4, `asset-metrics`, BTC 2010-07-18 → 2026-10-29 and ETH 2015-08-08 → 2026-10-29, daily.
  - Realized cap = market cap / `CapMVRVCur`.
  - MVRV-Z uses the expanding all-history σ of market cap.
  - Puell uses daily Δsupply × price / its 365-day mean, smoothed 7 days.
  - Weekly closes are Sunday daily closes.
  - EMA is seeded at the first observation.
  - Log-log fit: OLS of log10(price) on log10(days since 2009-01-03), from 2010-08-01.
- **Other sources:** Fear & Greed from api.alternative.me (2018-02-01 → 2026-10-30). Stablecoins from stablecoins.llama.fi/stablecoincharts/all. Dominance from api.coingecko.com/api/v3/global (snapshot 2026-10-30 07:21 UTC). Fed from FRED `DFEDTARU` (dates are effective dates, one day after the FOMC announcement).
- **Limitations:**
  - Reference-rate closes differ from intraday exchange extremes.
  - Coin Metrics MVRV differs from Glassnode by a few %.
  - Hash rate is estimated from block times and is noisy.
  - Dominance levels differ by provider.

---

## Sources

**Primary data / official**
- Coin Metrics Community API: https://community-api.coinmetrics.io/v4/timeseries/asset-metrics
- alternative.me Fear & Greed API: https://api.alternative.me/fng/ ; index page https://alternative.me/crypto/fear-and-greed-index/
- DefiLlama stablecoins: https://stablecoins.llama.fi/stablecoincharts/all ; https://defillama.com/stablecoins
- CoinGecko global: https://api.coingecko.com/api/v3/global ; BTC dominance chart https://www.coingecko.com/en/charts/bitcoin-dominance
- FRED DFEDTARU / WALCL: https://fred.stlouisfed.org/series/DFEDTARU , https://fred.stlouisfed.org/series/WALCL
- Federal Reserve, Oct 28 2026 press conference transcript (preliminary): https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20261028.pdf
- CNN, Fed holds Oct 2026 with two hike dissents: https://www.cnn.com/2026/10/28/business/live-news/federal-reserve-interest-rate-october
- Fox Business, Sep 16 2026 hike: https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-september-16-2026
- J.P. Morgan AM, FOMC statement Sep 2026: https://am.jpmorgan.com/us/en/asset-management/adv/insights/portfolio-insights/fixed-income/fixed-income-perspectives/fomc-statement-september-2026/
- Advisor Perspectives, Fed decision 16 Sep 2026: https://www.advisorperspectives.com/dshort/updates/2026/09/16/feds-interest-rate-decision-september-16-2026
- QT end Dec 1 2025 (Oct 29 2025 FOMC): https://benzinga.com/markets/macro-economic-events/25/10/48506713/federal-reserve-decision-october-30-25-basis-point-fed-funds-rate-balance-sheet-qt-quantitative-tightening ; https://www.lpl.com/research/blog/qt-is-ending-is-qe-next.html

**Cowen (primary or near-primary)**
- Cowen, "Bitcoin Cycle Memo – July 2026": https://benjamincowen.com/reports/bitcoin-cycle-memo-july-2026
- X posts: https://x.com/intocryptoverse/status/1990511167538954667 (200W "date with destiny", Nov 2025); https://x.com/benjamincowen/status/2071633906118402321 (weekly close below 200W, Jun 2026); https://x.com/benjamincowen/status/2101053560720863561 (cycle lows "not an exact science"); https://x.com/benjamincowen/status/1855065310186889454 (ETH/BTC 0.03465, Nov 2024); https://x.com/benjamincowen/status/1896942418886332511 (ETH 2019 wedge/QT)
- Video transcripts (rosetta.to): https://rosetta.to/u/intothecryptoverse ; https://rosetta.to/u/intothecryptoverse/bitcoin-sweeps-the-february-2026-low ; https://rosetta.to/u/intothecryptoverse/bitcoin-enters-the-3rd-stage-of-the-bear-market ; https://rosetta.to/u/intothecryptoverse/bitcoin-the-cost-basis-of-the-network ; https://rosetta.to/u/intothecryptoverse/bitcoin-bull-market-support-band-2025-10-23
- Into The Cryptoverse: https://intothecryptoverse.com/

**Secondary (news / research)**
- Cointelegraph Magazine, Cowen on the 4-year cycle (6 Mar 2026): https://cointelegraph.com/magazine/bitcoin-four-year-cycle-dead-debate-bear-market-2026-benjamin-cowen
- CoinMarketCap Academy, Cowen Oct 2026 bottom: https://coinmarketcap.com/academy/article/%20bitcoin-4-year-cycle-october-2026
- BeInCrypto, Cowen cycle not dead: https://beincrypto.com/bitcoin-four-year-cycle-not-dead-benjamin-cowen/ ; reputation/interest: https://beincrypto.com/cowen-crypto-scam-reputation-interest/
- AltcoinBuzz, "69–73 days" (18 Aug 2026): https://www.altcoinbuzz.io/benjamin-cowen-bitcoin-cycle-bottom-2026
- Sahm Capital, social interest at 2018 levels (23 Jul 2026): https://www.sahmcapital.com/news/content/there-are-dozens-of-us-left-analyst-says-as-bitcoin-social-interest-crashes-to-2018-levels-2026-07-23
- Pintu Academy, bear-market data (29 Oct 2026): https://pintu.co.id/en/academy/post/is-the-crypto-bear-market-over-2026
- 21Shares, Bitcoin outlook Oct 2026: https://www.21shares.com/en-eu/insights/bitcoin-outlook-october-2026
- Fortune BTC price 29 Oct 2026: https://fortune.com/article/price-of-bitcoin-10-29-2026/
- crypto.news price page (STH MVRV/realized price, 24 Oct 2026): https://crypto.news/price-prediction/bitcoin
- TokenPost STH-MVRV (Sep 2026): https://www.tokenpost.com/news/investing/24808
- NewHedge STH realized price: https://newhedge.io/bitcoin/short-term-holder-realized-price
- 24/7 Wall St., BTC dominance 59.5% (28 Oct 2026): https://247wallst.com/investing/cryptocurrency/2026/10/28/bitcoin-controls-59-5-of-the-crypto-market-is-altcoin-season-still-possible/
- U.Today, dominance >60% in 2026: https://u.today/bitcoin-dominance-surpasses-60-first-time-in-2026-as-btc-nears-80k
- CryptoTicker ETH/BTC Oct 2026: https://cryptoticker.io/en/ethereum-forecast-eth-btc-ratio-october-2026/
- ChainCatcher F&G (30 Oct 2026): https://www.chaincatcher.com/en/article/2300294
- CoinGecko research, dominance history: https://www.coingecko.com/research/publications/bitcoin-dominance-history
- Banxa, BTC dominance (39.3% on 19 May 2021): https://banxa.com/learn/markets-and-trading-basics/what-is-bitcoin-dominance
- Dominance ~65% May 2025: https://www.itiger.com/news/2533358087 ; https://bitcoinnews.com/markets/bitcoin-dominance-highest-in-4-years
- The Defiant, ETH/BTC 2025 lows: https://thedefiant.io/news/markets/eth-btc-ratio-hits-lowest-level-since-march-2020-0-02113-now-49-eth-1-bitcoin-e0d0397e
- Daily Hodl, Cowen on ETH/BTC & QT: https://dailyhodl.com/2025/02/06/benjamin-cowen-warns-ethereum-could-continue-bleeding-against-bitcoin-says-one-factor-to-determine-bottom/ ; https://dailyhodl.com/2025/03/13/welcome-to-pain-analyst-benjamin-cowen-says-ethereum-mirroring-2019-market-cycles-playbook/
- The Block, Coinbase App Store rank (Sep 2025): https://www.theblock.co/post/370698/coinbase-app-store-ranking-suggests-retail-still-on-sidelines-despite-crypto-rally ; Nov 2024: https://www.theblock.co/post/326545/coinbase-us-apple-app-store-top-10-number-1-finance
- Cointelegraph, retail/Google Trends debate: https://cointelegraph.com/markets/bitcoin-retail-investor-interest-debate-coinbase-app-store-surge-bull-run
- Forklog, crypto YouTube views lowest since 2021: https://forklog.com/en/youtube-cryptocurrency-content-views-plummet-to-lowest-since-2021/
- Feb 2026 crash coverage: https://cointelegraph.com/news/analysts-forecast-bitcoin-crash-60k-february-low ; https://www.mexc.com/ru-RU/crypto-pulse/article/cryptocurrency-crash-analysis-82798
- Stablecoin supply 2026: https://www.kucoin.com/blog/Stablecoin-Liquidity-Hits-$320B-Milestone-in-May-2026?lang=en_US
- Altcoin Season Index explainer: https://coingate.com/gift-cards/articles/article/altcoin-season-what-it-is-and-how-to-spot-one ; https://www.blockchaincenter.net/en/altcoin-season-index/ ; https://www.coinmarketcap.com/charts/altcoin-season-index
- TradingView Cowen-style reimplementations (risk metric is approximate, not official): https://www.tradingview.com/script/H4iCbDci-Benjamin-Cowen-s-Simplified-Risk-Metric ; https://www.tradingview.com/scripts/benjamin/
- Cowen on BMSB / lengthening cycles (secondary): https://benzinga.com/markets/cryptocurrency/25/03/44474962/bitcoin-tests-key-bull-market-support-at-88000-what-does-technical-analysis-say ; https://theinformerpost.beehiiv.com/p/bitcoins-bull-market-different-from-previous-cycles-says-analyst-benjamin-cowen-heres-why
- Bitcoin Magazine Pro (indicator definitions: Pi Cycle Top, Mayer, Puell, 200WMA heatmap, CVDD, MVRV-Z): https://www.bitcoinmagazinepro.com/charts/
- Glassnode Studio STH realized price/MVRV: https://studio.glassnode.com/charts/btc-sth-realized-price-mvrv?a=BTC

**Unverified or partly verified items (flagged)**
- The exact ATH print ($126,080 / $126,198 / $126,296 by venue).
- The October 2025 ~$19B liquidation total (widely reported; not checked against CoinGlass raw data).
- Coinbase #1 dates in 2017/2021.
- Google Trends relative peaks.
- The 2017 and 2019 dominance extremes, which vary by provider.
- Cowen's exact risk-metric construction (proprietary).
- The "day 1,162" top count quoted by CMC Academy, which does not reconcile with Coin Metrics dates (1,050–1,062 days); it may be a different anchor or a transcription error.
