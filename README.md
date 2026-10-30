# financial-education

**Free, bilingual (English + Polish) courses for investors: how the economy moves markets, explained with real data.**

> Polish version of this page: [README_PL.md](README_PL.md).

![Language: English and Polish](https://img.shields.io/badge/language-English%20%2B%20Polish-red)
![Course: 16 chapters](https://img.shields.io/badge/course-16%20chapters%20%2B%20glossary-blue)
![Data: FRED, reproducible](https://img.shields.io/badge/data-FRED%2C%20reproducible-green)
![License: CC BY 4.0 + MIT](https://img.shields.io/badge/license-CC%20BY%204.0%20%2B%20MIT-lightgrey)

Everything here is educational. Nothing is financial advice.

---

## Course — [practical macroeconomics for investors](en/practical-macro-economy/00-INDEX.md) (`en/practical-macro-economy/`, Polish: [`pl/praktyczna-makroekonomia/`](pl/praktyczna-makroekonomia/00-INDEKS.md))

After this course you can watch a macro-and-crypto market video, for example by
[Benjamin Cowen](https://www.youtube.com/@benjaminjcowen) (Into The Cryptoverse), whose indicator set the course
covers in full, and understand every indicator, metric and chart in it. You will know what each one measures, where
to get it for free, what it leads and what it follows, and what it has historically meant for bitcoin, altcoins,
stocks, bonds, the dollar and gold. The course is independent and not affiliated with him.

| Part | Chapters | Topics |
|---|---|---|
| Toolkit | [01](en/practical-macro-economy/01-HOW-TO-READ-MACRO-CHARTS.md) | log scales, moving averages, regression bands, risk scales, correlation and lead/lag, statistics traps |
| Macro | [02](en/practical-macro-economy/02-THE-FED-AND-INTEREST-RATES.md)–[09](en/practical-macro-economy/09-SEASONALITY-AND-POLITICAL-CYCLES.md) | the Fed, bonds and the yield curve, inflation, jobs, growth, liquidity and the dollar, stocks and gold, seasonality |
| Crypto | [10](en/practical-macro-economy/10-BITCOIN-CYCLES-AND-VALUATION-MODELS.md)–[12](en/practical-macro-economy/12-DOMINANCE-ALTCOINS-AND-ROTATION.md) | bitcoin cycles and valuation models, on-chain and sentiment, dominance and altcoins |
| Synthesis | [13](en/practical-macro-economy/13-HOW-IT-ALL-CONNECTS.md)–[16](en/practical-macro-economy/16-GLOSSARY.md) | **how it all connects**, a video decoder and track record, your dashboard and routine, glossary |

## Tool — [macro lab](tools/macro-lab/README.md) (`tools/macro-lab/`)

One Python script (standard library only, no API key) that downloads free FRED data and recomputes the course's
statistics: yield-curve inversions vs recessions, Sahm-rule triggers, what followed every first Fed cut, the
presidential cycle, bitcoin's moving averages, log-regression fair value and correlations.
[Snapshot of 30 October 2026](tools/macro-lab/REPORT-2026-10-30.md).

```bash
python3 tools/macro-lab/macro_lab.py --out REPORT.md
```

## Research notes — [`research-notes/`](research-notes/README.md)

The working notes behind the course (English), with evidence tags and sources, plus the
[fact-check log](research-notes/FACT-CHECK-LOG.md) of every correction made before publication.

---

## License

Course texts: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT. Details: [LICENSE.md](LICENSE.md).
