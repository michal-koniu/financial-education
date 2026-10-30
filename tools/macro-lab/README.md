# macro lab

One Python script that downloads free data from [FRED](https://fred.stlouisfed.org/) and recomputes every
statistical table the course quotes: yield-curve inversions vs recessions, Sahm-rule triggers, unemployment lows,
what happened after each first Fed cut, the presidential cycle, bitcoin's moving averages and log-regression fair
value, rolling correlations, and the "does liquidity lead bitcoin?" tests.

- Standard library only (Python 3.9+): no pandas, no API key, no account.
- First run downloads ~25 CSV files (a few MB) into `.fred-cache/`; later runs within 24 hours reuse them.
- Output: a single Markdown file you can open on GitHub or in any editor.

```bash
python3 macro_lab.py                     # writes REPORT.md
python3 macro_lab.py --out my-report.md  # choose the output file
python3 macro_lab.py --offline           # recompute from the cache only
```

[`REPORT-2026-10-30.md`](REPORT-2026-10-30.md) is the snapshot the course text was written from (data through
29 October 2026). Run the script again to see how the numbers have moved since.

## What each section computes

| Section | Data (FRED ids) | Method |
|---|---|---|
| Dashboard | DFEDTARU, DGS2, DGS10, T10Y2Y, T10Y3M, DFII10, T10YIE, BAMLH0A0HYM2, UNRATE, SAHMREALTIME, ICSA, CPIAUCSL, PCEPILFE, M2SL, WALCL, RRPONTSYD, DTWEXBGS, VIXCLS, CBBTCUSD | latest value, 3 months and 1 year earlier; CPI, core PCE and M2 as year-on-year % |
| Recessions | USREC | NBER recession months turned into start/end dates |
| Yield curve | T10Y3M, T10Y2Y | monthly averages; inversion episodes of >= 2 months; months from first inversion and from un-inversion to the next recession |
| Sahm rule | SAHMREALTIME | first month >= 0.50 (re-armed below 0.30), compared with recession start |
| Unemployment | UNRATE | cycle low before each recession and the rise by the time it started |
| Fed cycles | DFEDTAR + DFEDTARU, NASDAQCOM, UNRATE, CBBTCUSD | last hike → first cut (moves >= 0.25 pp), Nasdaq +3/+6/+12 months, worst close within 18 months, unemployment peak |
| Presidential cycle | NASDAQCOM | calendar-year returns by year of the four-year cycle; midterm-year drawdowns and the rebound from the low |
| Bitcoin | CBBTCUSD, CBETHUSD, NASDAQCOM, DTWEXBGS, DFII10, WALCL, WTREGEN, RRPONTSYD, M2SL | 200-week SMA, 20W SMA / 21W EMA, log-log regression fair value; weekly return correlations by year; lagged correlations with net liquidity and M2 |

## Limits you should know

- FRED's bitcoin series (Coinbase) starts in December 2014, so the regression misses the 2010–2014 history and the
  2013 cycle. Its fair value differs from fits on the full history; it is here to show the method.
- The Nasdaq Composite stands in for "stocks" because FRED's S&P 500 series covers only the last ten years.
- Eight recessions and three bitcoin cycles are tiny samples. A pattern that held every time can still fail next time.
- Correlations on overlapping year-on-year windows look stronger than they are. Weekly-return correlations are the
  honest version.

Educational tool, not financial advice.

---

**PL:** Skrypt pobiera bezpłatne dane z FRED i przelicza wszystkie tabele statystyczne cytowane w kursie
(krzywa rentowności a recesje, reguła Sahm, cykle Fed, cykl prezydencki, średnie i regresja bitcoina, korelacje).
Uruchomienie: `python3 macro_lab.py` (tylko biblioteka standardowa, bez klucza API). Migawka użyta do napisania
kursu: [`REPORT-2026-10-30.md`](REPORT-2026-10-30.md). Materiał edukacyjny, nie doradztwo finansowe.
