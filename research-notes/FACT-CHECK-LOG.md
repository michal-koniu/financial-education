# Fact-check log

Corrections made to the English chapters after independent fact-checking against FRED, the macro lab and primary sources (30 October 2026). Where these notes and the research notes disagree, the corrected chapter text is the reference.

## Fact-check: chapters 01–04 (EN)

Checked against CANONICAL-FACTS.md, the regenerated lab report, research A/B/C/D/E, the Cowen video index JSON (all 40 cited video titles and dates matched), and fresh FRED CSV downloads on 2026-10-30 (UNRATE, CPIAUCSL/NS, CPILFESL, PCEPI/PCEPILFE, PPIFIS, MICH, shelter, DGS2/10/30/3MO, DFII10, THREEFYTP10, T10Y2Y, T10Y3M, T5YIFR, HY/IG OAS, WALCL, Brent/WTI, DFF). About 160 claims checked (ch01 ~40, ch02 ~50, ch03 ~40, ch04 ~30); 41 fixes made.

| chapter | location | was | now | source |
|---|---|---|---|---|
| 01 | "You will learn", heading, checklist | "about eight recessions" | "nine US recessions since 1960" (heading "Small samples: nine recessions since 1960"; checklist "three or four crypto cycles") | lab NBER table (9 since 1960) |
| 01 | Unfinished windows | lab shows "none within 36 m" for the 2025-03 inversion | lab says "none yet (window open to 2028-03)"; kept as a lesson about careless labels | regenerated lab report |
| 01 | Check yourself Q7 + answer | quoted the old lab label | quotes the new label; the answer says the window can't be judged before March 2028 | lab report |
| 01 | Recession shading | NBER lag "about 6–12 months" | 4 months (Feb 2020 peak), 8 months (Mar 2001), 12 months (Dec 2007) | NBER announcement dates (Jun 2020, Nov 2001, Dec 2008) |
| 01 | Survivorship and curve-fitting | S2F "average out-of-sample error +295% vs +32% for a simple power law" | overpredicted on ~95% of days in 2019–26, geometric-mean error +295%, against +32% for a power law calibrated to 2018 | research E §2.6 |
| 02 | Fed funds, "Connections" | unemployment led the first cut by "~6 m in 2007, ~3 in 2019" | 4–6 m in 2007; "barely at all in 2019" (3.6% to 3.7%); 17 m in 2024 | FRED UNRATE |
| 02 | Terminal-rate check | last hikes "20 Dec 2018" and "27 Jul 2023"; "five days apart" | announced 19 Dec 2018 (effective 20 Dec), four days after BTC's low; 26 Jul 2023 (effective 27 Jul) | FOMC dates; lab uses effective dates |
| 02 | FOMC statement | the July memo "read the July 9–3 vote" (the memo is dated 15 Jul, before the vote) | July memo: 130 words and easing bias removed; the August memo cites the 9–3 vote | research E §2.7, §2.8 |
| 02 | Dot plot / BTC low | "$58.6k on a daily close" (3 places) | "about $57.7–58.6k, depending on source" | CANONICAL-FACTS; matches ch05/06 |
| 02 | Taylor rule | headline-PCE variant "about 5.6%" | "about 5.7% (1.2 + 3.65 + 0.825)" | arithmetic |
| 02 | Real rates, Connections | TIPS "2.93% in September 2026, highest since Nov 2008" | 2.93% at end-Sep and 2.95% on 5 Oct, highest since Nov 2008 | FRED DFII10 |
| 02 | Recession cuts | "500 bp or more … 2020" | "usually 500 bp or more"; notes 2020 was 150 bp (rates hit zero) | FOMC history |
| 02 | 2024–26 table | Jan–Jul 2025 dissents: only July listed | adds Waller's March dissent on QT | research B §7.1 |
| 02 | Oil shock / inflation | "lab's FRED calculation gives 4.0%; the research computes 3.7%" | 3.7% for Sep 2026 (lab 3.72%); May peak 4.2% SA / 4.25% BLS headline | regenerated lab; CANONICAL |
| 02 | Markets | 2-year "September high of 4.88%" | "2026 high of 4.92% (28 Sep, FRED daily close)" | FRED DGS2 |
| 02 | Markets | Cowen's "5.29%, highest since 2007"; "sources differ" | the 2007 high on FRED was 5.26%, so 5.29% was already the highest since 2002 | FRED DGS10 |
| 02 | 2024–26 summary | "last hike 27 Jul 2023" | "last hike effective 27 Jul 2023" | lab method |
| 03 | Mermaid node D | "lag 6–23 m" | "recession 9–23 m after first inversion" | lab tables (9–17 / 11–23) |
| 03 | Yields table + "When the 2-year stops rising" | 2Y Sep high 4.88 | 4.92 (28 Sep) | FRED DGS2 |
| 03 | 10-year, How to read | "sources differ on the comparison" | same FRED 2007-high note as ch02 | FRED DGS10 |
| 03 | Lab 10y–3m table | 2025-03 row "none within 36 m" | "none yet (window open to 2028-03)" | regenerated lab |
| 03 | "Unfinished window" bullet, Q4 + answer | old label | new label; Q4 reworded | lab |
| 03 | The facts (2022–24) | "2s10s first inverted on 6 Jul 2022"; "10y–3m inverted on 25 Oct 2022" | brief dip on 1 and 4 Apr 2022, inverted for good from 6 Jul 2022; 10y–3m first closed negative on 18 Oct, stayed negative from 25 Oct 2022 | FRED T10Y2Y, T10Y3M |
| 03 | Putting it together #1 | same inversion dates | same correction | FRED |
| 03 | Two cautions | NBER "typically 6–12 months" | 4 / 8 / 12-month examples | NBER |
| 03 | Term premium | "+0.17 Jan 2024; peaked 1.08 in Sep 2026" | ~+0.2 (Jan 2024 average); 1.08 at end-Sep and ~1.10 on 5 Oct (highest since Apr 2010) | FRED THREEFYTP10 |
| 03 | TIPS card | "September high of 2.93%" | 2.93% end-Sep, 2.95% on 5 Oct | FRED DFII10 |
| 03 | Putting it together #5 | 0.17 → 1.08 pp; real yields 2.93% | ~0.2 → ~1.1 pp; 2.95% | FRED |
| 03 | Breakevens | "CPI went from 2.4% to over 4% during 2026" | 2.4% (Jan) to above 4% (May) | CANONICAL |
| 03 | MOVE | "about 260 in 2008, March 2020, and about 199" (implied 260 in 2020) | ~260 in late 2008, in the 160s in March 2020, ~199 in Mar 2023 | ICE (Bassman interview), American Century |
| 03 | Putting it together #2 | "3.4% → 4.3%, April 2023 → August 2024" | 3.4% → 4.2% (July–Aug 2024 revised; July first printed 4.3%) | FRED UNRATE (current vintage) |
| 03 | Steepening worked example | "+0.51 (December 2025) → +1.09 (September 2026)" | dated 31 Dec 2025 / 30 Sep 2026, daily closes (monthly averages are 0.46 / 0.90) | FRED T10Y3M |
| 04 | Title | "# 04 · Inflation" | "# 04. Inflation" (matches other chapters) | spec/style |
| 04 | CPI table | Jun 2022 9.0%, May 2026 4.2% with no basis note | adds BLS NSA headline 9.1% and 4.25% | FRED CPIAUCNS; CANONICAL |
| 04 | Base effects, "data trap" paragraph | described the lab as printing 4.02% (a current lab error) | a generic missing-month trap (~4.0% vs the correct 3.7%); the lab now matches dates and shows 3.72% | regenerated lab; FACTCHECK-BRIEF |
| 04 | Check yourself Q4 + answer | "Why does the lab show 4.02%…" | generic 12-rows-vs-12-months question; answer 3.7% (lab 3.72%) | lab |
| 04 | Checkmate quotes | attributed to "Inflation Soars to 3.3%" (10 Apr) and the May memo | attributed to the 7 Apr and 12 May 2026 videos (Rosetta), matching ch02 and research B | research B §1.9 |
| 04 | May memo | "(research E, section 5)" | reference removed (internal file) | — |
| 04 | Transmission step 3 | TIPS 2.93% in Sep | 2.93% end-Sep, 2.95% on 5 Oct | FRED |
| 04 | Putting it together #1 | chain starts "Oil spikes", illustrated by tariffs; "core CPI at 3.0%" at the Sep 2025 cut | "supply or price-level shock (oil, tariffs)"; core about 3% (3.1% in August, the latest print before the cut) | FRED CPILFESL |
| 04 | Several places | opaque internal refs ("inventory call #10", "inventory section 1b/1c", "inventory 1.6") | plain-words provenance (date of call; "keyword count over his video index") | style |
| 04 | Dollar → crypto step | quoted "Altcoin season is unlikely…" as a quotation from an inventory row | stated as his framing, per secondary summaries | research A row 1.6 [S] |

### Verified unchanged (selected)
- Lab tables are copied exactly: correlations, lead/lag, the Fed cycle table and the inversion tables (apart from the 2025-03 label).
- FOMC 2026 calendar, every 2024–26 decision and dissent, SEP medians, IORB 3.90%, EFFR 3.88%, 3m bill 4.18%.
- 10Y 5.31% (5 Oct), the highest close since May 2002; 30Y 5.67% (7 Oct), the highest since Jul 2002.
- Daily lows: 2s10s −1.08 (3 Jul 2023), 10y–3m −1.89 (4 May 2023).
- HY OAS 2.59 (22 Jan 2025) and 4.61 (7 Apr 2025).
- WALCL low $6.536T (3 Dec 2025), peak $8.965T (13 Apr 2022).
- Brent and WTI monthly averages for 2026; Brent $138.21 (7 Apr) and $123.10 (27 Oct); Brent $133.18 (8 Mar 2022).
- CPI MoM: +0.87 / +0.64 / +0.47 / −0.42 / +0.65.
- SA CPI path 2020–26.
- Core PCE peak 5.6% (Sep 2022), Sep 2026 PCE 3.65 / core 3.12, PPI 6.3%, shelter 3.2% (peak 8.2%, Mar 2023), Michigan 6.6% (May 2025) and 4.6% (Sep 2026), 5y5y 2.23%.
- 1970s CPI and fed funds peaks; Hamilton's 10 of 11; research C's oil-rise percentages.
- Log-regression arithmetic: −1σ ≈ $85.6k, −2σ ≈ $49.7k, +1σ ≈ $254k.
- Bond price table and every annualisation and EMA/SMA/RSI example.
- Cowen memo figures (Triple Squeeze tables 1–3, curve snapshot, FedWatch path, first-hike lens, 1999 not 1997, 130-word statement, 9/8/1 June SEP split, global policy rate 3.42%, recession composite 0.024).
- No "buy/sell when" language found. Structure in all four chapters passes: disclaimer, nav, `<details>`, mermaid (labels quoted), tables, no [V]/[S]/[I] tags. validate.py reports only missing-file errors (PL, 00, 16, SOURCES).

### Unresolved / for other chapters
1. **ch13 line 204**: "NBER dates it 6–12 months later". The actual lags were 4 months (2020), 8 (2001) and 12 (2008). Suggest the same wording as ch01/03.
2. **ch13 line 451**: TIPS "2.93% in September, highest since Nov 2008". The 2026 high is 2.95% on 5 Oct.
3. **ch15 lines 185 and 197** still describe the lab's 2025-03 10y–3m row as "none within 36 m" / "failed signal so far". The lab now says "none yet (window open to 2028-03)". Lines 185 and 197 need updating.
4. Any chapter quoting the 2Y "Sep high 4.88%" (research B) should use 4.92% (28 Sep, FRED). None found outside 02/03.
5. **Research B** carries values that FRED no longer matches. Writers of later chapters should know:
   - 2Y high 4.88: FRED shows 4.92.
   - Term-premium peak 1.08 "in Sep": FRED shows 1.10 on 5 Oct.
   - TIPS 2.93: FRED shows 2.95 on 5 Oct.
   - 2s10s "first inverted 6 Jul 2022": FRED shows a brief dip on 1 and 4 Apr 2022 first.
6. **ch04** cites a [Benzinga Feb 2025](https://benzinga.com/markets/cryptocurrency/25/02/43706856/could-inflation-unemployment-derail-the-bitcoin-bull-run) link marked "content not retrievable". It is kept as is and is worth replacing if a readable source exists.
7. **ch01–04** still refer to "the course's Fed research" / "research B" in running text. Those files are not published, so a SOURCES.md entry or rewording may be wanted. Left as is, apart from the opaque section numbers.

## Fact-check, chapters 05–08

Scope: EN chapters 05 (labor), 06 (growth), 07 (liquidity and dollar), 08 (stocks, gold, cross-asset).
Ground truth: CANONICAL-FACTS.md, the regenerated lab report, research A/B/C/E, the FRED CSVs in `research/C_data` (I recomputed values from them), the Cowen video index (`A-cowen-videos-2019-2026.json`) for every video title and date, and the web (one search on 2008–09 S&P EPS).

About 190 claims checked: roughly 45 in ch05, 55 in ch06, 50 in ch07 and 40 in ch08. That covers more than 15 historical facts per chapter and every dated Cowen video or memo attribution. All Cowen video titles and dates matched the index.

The lab CPI check came back clean. None of the four chapters quotes the 4.0%/4.02% September 2026 CPI figure or describes the lab's CPI as buggy. Ch07's "flatter" refers to the lab's note on overlapping YoY windows, not to the regression note, so it stays.

### Fixes made

| chapter | location | was | now | source |
|---|---|---|---|---|
| 05 | sequence paragraph under the mermaid diagram | "The Sahm rule usually fires 2–4 months *after* a recession starts" | "has typically fired 1–3 months after" (lab table) | Lab Sahm table: 1, 3, 2, 3, 3, 2, 3, 1 months; this also matches ch05's own notes and Answer 3 |
| 05 | claims history table, 2006–08 row | High "536k (Nov 2008)"; outcome "Recession from Dec 2007 / Jan 2008" | "2006–09 \| 282k (Jan 2006) \| 665k (Mar 2009) \| Recession Dec 2007 peak to Jun 2009" | FRED ICSA (C_data): 2008 max 587k, cycle peak 665k on 28 Mar 2009 |
| 05 | Putting it together #1 | "claims 282k → 536k" | "282k → 665k" | same |
| 05 | "What it does not show" | "15 signals since 1962, of which about 8 were followed by recessions" | "14 signals since 1962, of which 7 were followed by recessions (one of them, 2019–20, caused by the pandemic)" | Research B §6.5 lists 14 dated crosses with 7 hits. Its own "8 of 15" summary does not match that list |
| 05 | Cowen framework table | The 15 Jan and 15 Feb 2026 rows came after Apr 2026 | Rows put back in date order | — |
| 05 | "Unemployment peaks after the market bottom" intro | The 1980 recession was silently missing from "every recession since 1969" | Added a note: S&P low 27 Mar 1980, unemployment 7.8% in Jul 1980 | Research C §4.9 table; FRED UNRATE |
| 06 | late-cycle mermaid diagram | "Stocks bottom 3–6 months before it ends" | "Stocks usually bottom 1–6 months before it ends" | Research C: 1–6 months in 7 of 8 recessions; this also matches the chapter text |
| 06 | Corporate earnings card | "EPS falls about 15–30% in recessions (2001 about −30% operating; 2008–09 about −50% GAAP)" | 15–30% typical; 2008–09 operating EPS roughly halved, as-reported (GAAP) EPS fell more than 80% (Cambridge Associates link added) | Web: Cambridge Associates (Jun 2009) gives operating EPS −~50% from the Q2 2007 peak and as-reported EPS −83% |
| 06 | ISM Services card | "Services dipped briefly below 50 in April–May 2025" (this contradicted "27th straight month of expansion") | Says the index printed just below 50 in May 2025 (first release) and explains that seasonal revisions can change consecutive-month counts | April 2025 was 51.6; only May (49.9) was below 50, on the first print |
| 07 | key-readings table, TGA row | "Highest since 2021" | "Near its highest since 2021 ($1.006 T on 22 Apr 2026)" | FRED WTREGEN: 22 Apr 2026 $1,005,968m > 28 Oct 2026 $999,727m |
| 07 | TGA card "Now" | "the highest since 2021" | "close to the April 2026 level of $1.006 T, the highest since 2021" | same |
| 07 | key-readings table, reserves row | "Below the $3.0–3.3 T range of 2024–mid 2026" | "Near the bottom of the 2024–26 range ($2.85 T on 29 Oct 2025 to $3.63 T in Mar 2024)" | FRED WRESBAL |
| 07 | reserves card "Now" | "$3.0–3.3 T in 2024–mid 2026 and $3.98 T at the 2021 peak" | "$2.85 T (29 Oct 2025) to $3.63 T (Mar 2024) … $4.28 T at the December 2021 peak" | FRED WRESBAL max 4,275,806 on 8 Dec 2021. Research C's 3.98/3.0–3.3 is wrong |
| 07 | reserves takeaway | "less slack than at any time since 2019" | "about as little slack as during the autumn-2025 funding squeeze, and less than at almost any time since 2020" | Reserves were $2.62 T in Jul 2020 and $2.85 T in Oct 2025 |
| 07 | M2 card | the 1930s money stock "fell by almost 30%" | "fell by about a third" | Friedman–Schwartz: M2 fell about 33–35% from 1929 to 1933 |
| 07 | QE/QT table | "Nov 2008–Oct 2014 … ~$0.9 T → ~$4.5 T" | "~$0.9 T (pre-crisis, mid-2008) → ~$4.5 T" | WALCL was already $2.07 T on 5 Nov 2008 |
| 08 | gold "Recent path" | "About −30% by late March ("Gold Drops Nearly 30%", 23 Mar 2026)" | Hedged as a sharp spring decline; the video title is quoted; the late-March level is marked unverified, because his own 15 Mar memo had gold near $5,018 (about −10%) | Research E memo header (15 Mar: gold $5,018) conflicts with the video title |
| 08 | S&P ÷ gold "How it played out" | "Gold then fell about 30% by late March" | Same hedge | same |
| 08 | Putting it together #5 | "fell about 30% by late March" | "fell sharply into the spring and was about 28% below the peak by late October" | Peak ~$5,560 vs $4,024 (29–30 Oct) = −28% |
| 08 | risk-cascade table, stage 5 | "down from 4.6% in Nov 2025" | "down from 4.5% in Nov 2025 (first printed as 4.6%)" | CANONICAL-FACTS (current vintage 4.5%); consistent with ch05 |
| 08 | correlation card | "underperformed the S&P by roughly 25–35 percentage points a year" | "roughly 23–24 percentage points in each year (2025: −7% vs +16.4%; 2026 YTD: −11% vs +13.1%)" | The chapter's own returns table |
| 08 | S&P card and Putting it together #3 | "Equity bears with a recession: −30% to −57%"; "deepens to −30% to −57%" | "−17% to −57%, about −36% on average"; "about −36% on average, up to −57%" | The chapter's own table (1980 −17%, 1990 −20%, 1981–82 −27%) |
| 08 | S&P card and Putting it together #3 | "bitcoin +305% in 2020" | "about +306%" | Matches the chapter's table (+306%) |
| 08 | gold card, Cowen use | "31 of 116 videos in the first half of 2026" | "31 of the 116 videos he published between 1 January and 11 June 2026 … the video index ends on 11 June" | Research A §1c: the 2026 column covers 1 Jan–11 Jun (editor item; matches ch09) |

### Verified and left unchanged (sample)

- **Ch05.** The lab tables (Sahm, unemployment lows, Fed cycles) match the regenerated report exactly. The unemployment path matches research B §7.2 and FRED. The benchmark revisions (−818k/−598k, −911k/−898k, −79k) are correct. 2026 payrolls average 68k. JOLTS 7.08M and quits 1.9% are correct. The S&P lows and unemployment peaks (1970–2020) are correct. The 175 bp of cuts, the hike on 16 Sep 2026, and BTC's top (6 Oct 2025), drawdown (−52%) and low ($57.7–58.6k) are correct.
- **Ch06.** Checked against FRED: GDP path (Q1 2022 −1.0, Q2 2022 +0.6, 2025–26 quarters), mortgage rates (2.65%, 7.79%, 6.26%, 7.24%), Michigan sentiment (50.0, 56.6, 44.8, 48.1), housing starts and permits, INDPRO +2.2%, TOTALSL +2.7%, RSAFS +6.3%, Case-Shiller (+2.1%, −27%) and DRCCLACBS (2.85, 6.77, 1.53, 3.22). Brent monthly averages ($71 → $103 → $117) and the S&P −9.1% are correct. Every Cowen video date is correct. The ISM history levels, the Pal attribution and the "1995 is not his" trap are handled correctly.
- **Ch07.** Checked against FRED: M2 (+26.8% in Feb 2021, the 21.77/20.71 T peak and trough, −4.66%, the negative stretch from Dec 2022 to Feb 2024, the regained peak in May 2025, 23.41 T), WALCL (8.965 T peak; 6.536 T low on 3 Dec 2025), the RRP record (2.554 T), the TGA in 2025 (296/958 bn), SOFR 5.25% (Sep 2019), the broad-dollar peaks and lows, every net-liquidity table value (13 dates), and USDJPY (161.73, 143.95, 163.86, 156.87). VIX 38.57 is correct. The lab correlation tables match. Every Cowen video date is correct.
- **Ch08.** The lab correlation table matches. The S&P recession table matches research C. The VIX records, CAPE history and Buffett quote are correct. Oil is correct: Hamilton's 10 of 11, the five-of-eight count, and the Brent monthly averages. The spot ETF launch date (11 Jan 2024) is correct. Every Cowen video date is correct.
- **Structure (all four chapters).** Each has a disclaimer footer, a nav footer with the correct relative links, a "Check yourself" section with `<details>`, at least one mermaid diagram with quoted labels, tables and no [V]/[S]/[I] tags. `validate.py` reports no problems in 05–08; the only errors are the expected missing PL, 00/16/SOURCES and README items.

### Unresolved, or for other chapters (not edited, outside my range)

1. **Ch13 line 89** says the Sahm rule "fired 2–4 months after the recession start in most cases, per the lab". The lab shows 1–3, and ch13's own table at line 201 already says 1–3. Ch13 needs the same fix I made in ch05.
2. **Ch14 line 111 (T21)** says "Gold … fell about 30% by late March". This conflicts with Cowen's 15 Mar memo (gold ≈ $5,018). Use the same hedge as ch08.
3. **The late-March 2026 gold level.** The video title "Gold Drops Nearly 30%" (23 Mar 2026) and the 15 Mar memo price (gold ≈ $5,018) cannot both describe spot gold from the peak unless gold fell about 20% in one week. The `stq_xauusd.csv` data file is an HTML bot-check page, not data, so I could not verify it. Ch08 is now hedged.
4. **Research C errors upstream.** Reserves "$3.98T 2021 peak" and "$3.0–3.3T range" are wrong (FRED: $4.28 T; $2.85–3.63 T). The "2008–09 ≈ −50% GAAP" EPS figure is wrong (that is roughly the operating figure; GAAP fell more than 80%). Research B §6.5 says "about 8 of 15" signals but lists 14 with 7 hits. Any other chapter that drew on these lines should be rechecked. A grep of 01–15 found no other occurrences.
5. **The ISM "47.5 overall-economy threshold"** (ch06) rests on research C's citation of ISM's September 2026 report. I could not check it independently; older ISM reports used figures around 42.

## Fact-check: chapters 09–12 (EN)

Scope: 09-SEASONALITY-AND-POLITICAL-CYCLES, 10-BITCOIN-CYCLES-AND-VALUATION-MODELS, 11-ON-CHAIN-AND-SENTIMENT, 12-DOMINANCE-ALTCOINS-AND-ROTATION.
Claims checked: about 190 (ch09 ~55, ch10 ~60, ch11 ~40, ch12 ~35). They were checked against CANONICAL-FACTS, the lab report (REPORT-2026-10-30), research A/C/D/E, and the web for a few attributed or historical items: Bouman–Jacobsen in the AER 2002, Pi Cycle (Philip Swift, Apr 2019) and the ETH/BTC peak (~0.148–0.15, 12–13 Jun 2017).
None of the four chapters quotes the lab's CPI or the old 4.0%/4.02% Sep-2026 figure, and none has [V]/[S]/[I] tags. Structure is intact in all four: disclaimer, navigation, `<details>`, mermaid with quoted labels, tables.
`validate.py` reports no errors for chapters 09–12. The only errors left are missing PL, 00/16/SOURCES and README files. The cross-chapter anchors used in 10↔11↔12 match the target headings.

| chapter | location | was | now | source |
|---|---|---|---|---|
| 09 | intro paragraph | "about 30% of his videos in the first half of 2026 (35 of 116)" | "…between 1 January and 11 June 2026 (35 of 116)" | A §1c: the 2026 column covers only 1 Jan–11 Jun |
| 09 | Year-to-date / midterm template, "Where it comes from" | "35 of 116 videos in the first half of 2026" | "…published between 1 January and 11 June 2026" | A §1c |
| 09 | Midterm-year detail, bullet 2 | "But four lows came in January or February" | "But four lows came in the first half, three of them in January or February" | Lab midterm table: 1978-01, 1986-01, 2014-02 and 1994-06 |
| 09 | "How 2026 tracked the template", paragraph after the table | "burden of proof has shifted to the bears" (secondary report) | Quote now cited to the Triple Squeeze memo (30 Sep 2026); the 50%-vs-40% comparison stays labelled as secondary | E §2.9 [V]; A T-section [S] |
| 09 | Putting it together #4 | "bitcoin rose 24.9% after the US Treasury expanded its bond buybacks (about $64k → about $80k)" | "rose 24.9% (about $63k → about $78k month-end to month-end), in a month when the Treasury expanded buybacks (reported by CoinDesk; causal link not established)" | A §4.1 [S]; B marks the buyback link as low-confidence; month-end levels are our arithmetic from the D monthly returns |
| 10 | Lengthening-cycles card | "114 video titles…, almost all from 2019–22" | "114…, 98 of them from 2019–22" | A §1c (2+32+49+15 = 98) |
| 10 | Section 7, "What happened" bullet | "came slightly below the $60–70k range he had named, and on the earlier date" | "came slightly below the $60–70k range he had named for May/June; the timing matched that earlier expectation, not the October base case" | A §3 row 17 (the old wording was unclear) |
| 11 | Realized price, Connections | "price stopped at the 200W" | "price stopped near the 200W (about 0.94× it at the June low), above realized price" | D §3.4: the low was 0.94× the 200W, and the 28 Jun weekly close was below it |
| 11 | MVRV, "What it has meant for assets" | "Readings above about 3.5 coincided with tops through 2021" | MVRV >3.5 at the 2013 and 2017 tops and 3.43 at the April 2021 mid-top; the Nov 2021 top reached only 2.85 | D §4.2 table |
| 11 | MVRV takeaway | "In 2026 it reached 1.10" | "In 2026 it bottomed at 1.10" | D §4.2 (the old wording implied a peak) |
| 11 | Apathy vs euphoria | "no one left to sell the altcoins to" quote cited to the Q1 2026 memo | Cited as a spoken quote reported by Cointelegraph Magazine (search snippet); the apathy-top thesis itself is cited to the memo | E §2.1 does not contain the quote; D §6.2 marks it [S] |
| 11 | ETF holdings, "How Cowen uses it" | "6.77% of total supply in April 2026" (no caveat) | Note added: 6.77% of ~20M BTC ≈ 1.35M BTC, above the 1.22–1.29M US spot-ETF figures, so fund coverage likely differs | E §2.4 vs D §5.6 |
| 11 | Composite on-chain risk | Listed RHODL as a component with no caveat (while §4 calls RHODL "weightless" on the dashboard) | Clarifying sentence added: the dashboard lists RHODL and supply P/L as unweighted, so the memo composite and the dashboard weighting may differ | A §1b [V]; E §2.8 [V] |
| 12 | Intro paragraph | "ETH 'going home' against BTC" | "ETH 'going home' to its $1,500–1,600 base in April 2025 (the ETH/BTC low came the same month)" | A T5: "going home" was an ETH/USD call |
| 12 | Section 4, risk cascade | The whole asset ordering attributed to the March 2026 memo | Staged framework cited to the March memo; the explicit alts → BTC → equities (energy last) ordering cited to the 25 Feb 2026 video (summary) | E §2.3; A §1.7 and T-section |
| 12 | Section 5, "What holds up", bullet 3 | "Bitcoin often leads liquidity cycles" cited to a video and CryptoAdventure | Primary source added: Crypto Macro Risk Memo Q1 2026 (15 Jan 2026) | E §2.1 [V] |

### Spot-checked and confirmed, no change (selection)
- **Halvings, tops and lows.** Halving dates; halving→top 371/525/546/534 d; low→top 1,067/1,059/1,062 d; low→next halving 542/513/528 d; drawdowns −84.5/−83.8/−76.7/−53.1%; multiples 539×/112×/21×/7.9×.
- **Day counts.** Cowen's July-memo days 1,332/1,424/1,432/1,050/1,061/1,068 (= 15–23 Oct 2026); day 1,363 on 15 Aug; June low on day 1,317; 30 Oct = day 1,439.
- **Lab report values.** Nasdaq presidential-cycle and midterm tables; BTC 200W $67,497; BMSB $72,965/$76,677; fair value $147,386, 0.53, z −1.17, slope 5.84; ETH/BTC-by-year table; −37.5% from the $124,720 weekly-close ATH. Our arithmetic on the lab tables (median midterm drawdown ~20%, median rally ~+38%, 9/13 lows in H2) checks out.
- **Recession starts by presidential year.** The 3/2/0/4 split matches the lab's NBER list.
- **S&P calendar returns.** 2010 +12.8%, 2014 +11.4%, 2018 −6.2%, 2022 −19.4%. The 2022 S&P low was on 12 Oct. The 2026 S&P drawdown was −9.1% (6,978.6 → 6,343.72), with a record of 7,818.93 on 6 Oct.
- **Cowen's memos.** Triple Squeeze figures: ~day 50, $64k/$38k, first-hike lens −20%/+70% and +12%/−60%, 10Y YTD ~1.27. Balance of Risks figures: ~7/20/25% midterm drawdowns, S&P YTD 1.137, BTC 0.714, gold 1.010, DXY rebased ~91.5. July memo figures: 0.49 → ~$43,800, quantile fan $65.5k/$116k/$202k, MVRV-Z 0.395, 56.83/43.15% supply in profit/loss, the Risk Scorecard rows, 389k YouTube views.
- **On-chain history.** MVRV/MVRV-Z, NUPL, Puell, Mayer, Pi Cycle and golden/death cross tables; hash-ribbon episodes; days below realized price 304/134/179.
- **Fear & Greed.** The episode table; record low of 5 in Feb 2026; 98 days at or below 20; 2026 high of 78; 30 on 30 Oct.
- **Dominance and ETH/BTC.** BTC.D history (32.4% Jan 2018, 60% 30 Oct 2024, 65% 6 May 2025, ex-stables ~67%). ETH/BTC 0.146 / 0.0164 / 0.0877 / 0.0181 / 0.0422 / 0.0257 / 0.0289. The balance-sheet-regime table matches D §7.2.
- **Web checks.** Bouman–Jacobsen, AER 92(5) 2002: 36 of 37 markets per the paper's abstract. The search confirmed the citation but not the count, so the count comes from the abstract as I recall it. Pi Cycle: Philip Swift, April 2019. ETH/BTC peak ~0.148–0.15 on 12–13 Jun 2017 (the course's 0.146 is the Coin Metrics close).

### Unresolved / for other reviewers
1. **Ch08, line ~268** says "31 of 116 videos in the first half of 2026". The keyword sample actually covers 1 Jan–11 Jun 2026, which is the same approximation I corrected in ch09. This needs fixing by the 05–08 reviewer.
2. **ETF holdings conflict (ch11).** Cowen's July memo has a ">1.25M BTC peak in late 2025, now below". The 21Shares/Pintu figure is ~1.29M BTC in late Sep 2026. Both are presented as sourced. I added the coverage caveat, but the numbers are not reconciled.
3. **Inferred month-end prices (ch09 #4).** The ~$63k → ~$78k end-July → end-August levels are inferred from Coin Metrics monthly returns, not read from a source. They are labelled as month-end arithmetic.
4. **Bouman–Jacobsen count.** The "36 of 37" count was not confirmed by the web search. It matches the paper's abstract as I recall it, so I left it unchanged.
5. **Ch12 wording.** The quote "all BTC pairs to 0.25" (25 Oct 2024) is reproduced from A [S]. What the 0.25 refers to is ambiguous; it is probably the alt-cap/BTC-cap ratio, not a pair price. It was left verbatim and should be checked against the original source if one can be found.

## Fact-check: chapters 13, 14, 15

About 125 claims checked against CANONICAL-FACTS, the regenerated lab report, research A–E, and the FRED CSVs in `research/C_data` (CBBTCUSD, CPIAUCSL, DGS10, T10Y2Y, DTWEXBGS, RRPONTSYD, BAMLH0A0HYM2, MORTGAGE30US, WALCL/WTREGEN, UNRATE, A191RL1Q225SBEA, USREC, DCOILBRENTEU). 50 fixes, all made in place. Validator: the only errors in my range are the expected missing-file ones (16-GLOSSARY.md). Table column counts and code fences in 13–15 are OK.

### Fixes

| chapter | location | was | now | source |
|---|---|---|---|---|
| 13 | §11 table, Inflation | CPI YoY 4.02% "per the lab" (research files 3.7%; "sources differ by method") | 3.72% (lab, SA, date-matched; BLS headline 3.7%), down from May peak ~4.25% | lab report (fixed); CANONICAL-FACTS |
| 15 | §5 worked example | CPI 4.02% YoY | CPI 3.72% YoY (Sep) | lab report |
| 15 | §5 "Limits you should know" | lab CPI 4.02% vs research 3.7%, "sources compute differently" | generic trap: the missing Oct-2025 print turns a 12-row step into a 13-month change; the lab matches by date, so 3.72% agrees with BLS 3.7% | FACTCHECK-BRIEF; lab code line 115 |
| 15 | §5 table, Bitcoin status | regression "flatter than full-history fits" | "slope and fair value differ from fits that include 2010–14" | lab report and README (regenerated) |
| 14 | §7 log regression limits | lab fit "gives a lower fair value than full-history fits" | "gives a different slope and fair value than fits that include 2010–14" | lab README |
| 13 | §1 short version | recession: stocks fall 30–55%; bottom 3–6 months before recession ends | ~36% average (17–57% since 1969); bottom 1–6 months before the end (2001–02 exception) | research C §4.9 table; ch06 and ch08 line 492 |
| 13 | §2 master mermaid | "Stocks ↓ 30-55% if recession" | "Stocks ↓ about 36% on average if recession" | research C |
| 13 | §3.1 counter-example; §9 Sep-2026 row | BTC rose "$63k → $83k after the 16 Sep hike" | ~$76k on hike day → ~$86k on 21 Sep; the move from ~$63k was the mid-August level | FRED CBBTCUSD: 15 Sep 75,656; 16 Sep 76,209; 21 Sep 86,397; 30 Sep 83,483; mid-Aug ~62.9–63.9k |
| 13 | §3.2 | Sahm fired "2–4 months after" the start, "per the lab" | 1–3 months after in most cases since 1970 (lab) | lab Sahm table; editor, aligned with ch05 |
| 13 | §3.6 | records are "in his words … the top of the ladder rather than proof of health" | quotes "what the late stage of the ladder looks like" and "not the edge of a cliff" | research E §2.8 and §3.2 (Aug memo) |
| 13 | §4.1 step 7 | 0–7 months before recession, cited to the lab | 2–11 months (lab), 0–7 by research B's daily dating; 11 and 7 are two 1989–90 episodes | lab 10Y–3M table; research B §6.2 |
| 13 | §4.1 step 8 | "range −1 to +12" (ambiguous sign) | "from 12 months before to 1 month after" | research C §4.9 |
| 13 | §4.1 step 9 | NBER dates recessions "6–12 months later" | "about 4–12 months later" | editor (01–04 checker) |
| 13 | §4.4, 15 May row | "Powell steps down; Warsh succeeds" | Powell's chair term ends (last meeting 29 Apr); Warsh chairs from the June meeting | research B §7.1 |
| 13 | §5.2 S&P, Recession column | −30% to −57% | about −36% average (−17% to −57%); bottoms 1–6 months before the recession ends | research C; ch06 |
| 13 | §5.2 Gold, Tightening column | "2022 was an exception (central-bank buying)" | "2022–24 broke the pattern" (gold fell about 20% from Mar to Nov 2022) | research B §2.6 and §3.5; research C |
| 13 | §6 matrix: inflation → 2-year | dissents for a hike "two meetings before" the Sep hike | dissents against easing bias in April, and for a hike in July, the meeting before | research B §7.1 |
| 13 | §6 matrix: un-inversion | "0–7 months (lab: 2–11)" (lab contradicts typical lag) | 2–11 months in the lab (0–7 by research B's dating) | lab; research B |
| 13 | §6 matrix: Sahm | coincident to 4 months after | usually 1–3 months after (lab range −3 to +7) | lab |
| 13 | §6 matrix: rising unemployment → first cut | 2019 cut ~3 months after the unemployment low | 2019 (like 1998) cut with unemployment still at or near its low; lag 4–17 months (2007, 2024) | FRED UNRATE 2019: 3.6% May–Jun, 3.7% Jul, 3.5% Sep |
| 13 | §6 matrix: S&P drawdown → BTC | "weekly correlation 0.21…" (implied S&P) | "lab weekly correlation with the Nasdaq" | lab report |
| 13 | §8.1 Sep memo | 10Y 5.29% "(highest since 2007)" stated as fact | marked as his wording; on FRED closes, 5.31% on 5 Oct was the highest since May 2002 | research E §2.9; research B §0 |
| 13 | §8.1 Aug scenario table | NFCI "toward or above zero" listed inside the recession cluster | cluster = payrolls YoY <0, claims, unemployment, composite; NFCI above zero named separately as the early warning | research E §2.8 |
| 13 | §8.2 | the policy-error state's conditions "largely occurred" | the energy and Fed conditions occurred, but labor was not stalling | research E §5; B §0 |
| 13 | §8.2 | Brent $123.10 "near its 2026 highs" | not far below the April high of ~$138; energy-stock records in Oct | research B §0; FRED |
| 13 | §9, 2018–19 row | BTC "rose about ×4 in 2019" | ×4 to its June 2019 high (calendar 2019 was +94%) | research D |
| 13 | §10, ISM new orders, 2024–25 column | "below 50 for 26 months" | the headline ISM was below 50 for 26 months (Nov 2022–Dec 2024) | research C §1 |
| 13 | §11 Real yield | 2.93% in September, highest since Nov 2008 | 2.95% on 5 Oct (FRED DFII10) | editor (01–04 checker) |
| 13 | §11 Crypto internals | BTC.D 59.4% (CoinGecko) | about 58.5–60%, providers differ (A gives CoinGecko 58.5%, D gives 59.4%) | research A §4.3, D §6 |
| 13 | §7 lab table | 2022–24 *and 2025* 10Y–3M episodes "no recession within 36 months" | 2025 window still open (to Mar 2028) | lab report (regenerated) |
| 13 | §12 chain 1 | recession "within 0–7 months, stocks −30% to −55%" | "within months; stocks fell 34–57% peak to trough in these episodes" | research C table (2001 −49%, 2008 −57%, 2020 −34%) |
| 13 | Answer 3 | "lab: 11, 7, 2, 7, 5" for 1990–2020 | explains that 11 and 7 are two 1989–90 episodes | lab |
| 14 | intro | "about 2,400 videos since 2019" | "well over 2,000 (2,385 indexed 2019 – 11 Jun 2026)" | research A §0, §1c |
| 14 | T23 status; track row 27; answer 6 | BTC "$63k → $83k after the hike" | ~$76k on hike day → ~$86k on 21 Sep; $63k → $83k ran from mid-Aug to end-Sep | FRED CBBTCUSD |
| 14 | Putting it together #4 | BTC rose "about 30% after the hike" | ~13% in the week after (~30% from mid-August) | FRED CBBTCUSD |
| 14 | Putting it together #3 | unemployment "4.2% and falling" | 4.2% (Sep), below the 4.5% Nov-2025 peak (it rose from 4.1% in Aug) | CANONICAL-FACTS |
| 14 | T15 status | one weekly close below the 200W | adds the two marginal August closes | research D key finding 5 |
| 14 | track row 6 | BTC +155% in 2023 | +156% (FRED: 16,531 → 42,301), consistent with ch08/13/15 | research D; FRED |
| 14 | T21 status; track row 23 | gold "fell about 30% by late March" | hedged: video title "Gold Drops Nearly 30%"; late-March level unverified; ~$3,970 June low (~−29%), ~−28% on 30 Oct | editor; ch08 hedge; research A, C |
| 14 | §5 track record | no per-row sourcing | added a Source column for all 29 rows (rosetta video titles and dates, Benzinga, Cointelegraph, Bankless, CMC, BeInCrypto, memos); intro says which sources are primary and which secondary | research A §2–3 and Sources; E §5 |
| 15 | §5 table, yield-curve row | "none within 36 m" = failed so far | distinguishes "none within 36 m" (failed) from "none yet" (window open) | lab report |
| 15 | §5 worked example, yield curve | 2025 10Y–3M episode "none within 36 m", signal "failed" | 2025 episode "none yet (window open to 2028-03)"; only the 2022–24 signal failed | lab report; editor |
| 15 | §8 chain 3 | July hike dissents "two meetings before" the Sep hike | April dissents against easing bias and July hike dissents (the meeting before) | research B §7.1 |
| 15 | Exercise 4 | "From 30 Jan … 2-year +130 bp (from Feb low), 10-year +108 bp" (mixed bases) | from the 27 Feb lows (3.38% and 3.97%) to 28 Oct; spread +0.74 (30 Jan) → +0.37 (29 Oct) | FRED DGS10 (27 Feb 3.97; 28 Oct 5.05); research B |

Checks that passed (sample): the lab rows in 13 §7 and 15 §5; Fed dates and ranges (Dec 2025, 16 Sep, 28 Oct 10–2, 29 Jul 9–3); +525 bp in 16 months; RRP record $2.554T on 30 Dec 2022; HY 2.59 (Jan 2025) and 4.61 (7 Apr 2025); CPI MoM +0.87/+0.64/+0.47 (Mar–May 2026); mortgage 7.24%; TGA ~$1.0T and net liquidity ~$5.75T; Q3 GDP +3.4%; USREC 0; 10Y 5.31% on 5 Oct; 10Y 3.63 → 4.58% after the Sep 2024 cut; ETH/BTC 0.0164 (6 Sep 2019) and 0.0181 (21 Apr 2025); BTC top 26 Jun 2019 and 6 Oct 2025, 5 and 8 weeks before QT ended; Fear & Greed low of 5; ISM 52.6 (first expansion in 12 months), 54.5, new orders 55.3, prices 77.9; S&P values 6,343.72, 7,818.93 and 7,744; VIX 80.86 and 82.69; DXY 114.78; M2 +26.8% and −4.86%; BTC.D 60% on 30 Oct 2024; diminishing returns ×539/×112/×21/×7.9; memo dates, reference prices, 65/20/15 weights, sequence-risk lags; release calendar times; the 2026 FOMC schedule and the Warsh "strategy meeting"; shutdown dates; the lab CLI flags.

Structure: all three chapters have a disclaimer footer, a nav footer, mermaid diagrams with quoted labels, tables, and "Check yourself" in `<details>`. No [V]/[S]/[I] tags and no buy/sell rules. The attribution traps are respected: ISM→alt season is Pal's, "1995" is not Cowen's, and he dropped "lengthening cycles".

### Issues outside my range (not edited)
- **ch02 (lines 265, 425), ch04 (line 319), ch10 (line 187):** each says BTC rallied "from about $63k to about $83k" after the 16 Sep 2026 hike. FRED CBBTCUSD shows ~$76.2k on hike day, ~$86.4k on 21 Sep and ~$83.5k on 30 Sep. ~$63k was the mid-August level. Use the same correction as ch13 and ch14.
- **ch02 (lines 270, 427):** says hawkish dissents preceded the hike "by about two meetings (July's three hike dissents)". July was the meeting just before September. The trail started in April with dissents against the easing bias.
- **ch04 (lines ~170 and 365):** still describes the lab's 4.02% CPI as a lab error ("Why does the lab dashboard show 4.02%…"). The lab is fixed (3.72%). Rewrite as a generic data trap.
- **ch08 (lines 96, 471):** gives recession equity bears as "−30% to −57%". Ch08 line 492, ch06 and research C give ~−36% average (−17% to −57%). Ch13 now uses the latter.
- **ch02 (line 321):** gives the 2-year 2026 high as 4.92% (28 Sep). Research B §0 says 4.88%. Check against FRED DGS2 (not in C_data).

### Unresolved / judgement calls
- The checkmate quote is dated 10 Apr 2026 ("Inflation Soars to 3.3%", research A). Research B dates it 7 Apr and 12 May. I kept 10 Apr plus May, as A gives it.
- 2018 BTC calendar return: ch13 uses −73% (as ch08 does). Research D says −74% and ch09 says "−73% to −74%". Left as is.
- The DFII10 peak of 2.95% on 5 Oct comes from the editor. DFII10 is not in the local C_data, so I could not re-verify it here.
