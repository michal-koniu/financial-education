# financial-education

**Free, bilingual (English + Polish) courses for investors: how the economy moves markets, explained with real data.**

> Polish version of this page: [README_PL.md](README_PL.md).

![Language: English and Polish](https://img.shields.io/badge/language-English%20%2B%20Polish-red)
![Course: 16 chapters](https://img.shields.io/badge/course-16%20chapters%20%2B%20glossary-blue)
![Guide: GTA 6 income options](https://img.shields.io/badge/guide-GTA%206%20income%20options-orange)
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

## Guide — [making money around GTA 6: what is realistic](en/gta6-income-options/README.md) (`en/gta6-income-options/`, Polish: [`pl/gta6-mozliwosci-zarobku/`](pl/gta6-mozliwosci-zarobku/README.md))

An educational guide for a technically strong reader with a local AI rig who wants to know which money options around a huge
game launch are real, which are hype, and where agents actually help. 25 options rated on income, probability, automation,
speed and risk with the arithmetic shown, the six places where "agents do everything" fails, an agent pipeline with human
gates, a 90-day launch plan with kill criteria, and a list of what is excluded and why. Desk research with evidence tags,
as of 30 October 2026; facts and platform rules change fast, so re-check them before acting. Not legal, tax or investment advice.

| File | What is in it |
|---|---|
| [README](en/gta6-income-options/README.md) | the summary in ten points, the rating table, recommendations, hype to discount, glossary, known gaps |
| [01-STATUS-AND-RULES](en/gta6-income-options/01-STATUS-AND-RULES.md) | game status, launch analogues, Rockstar/Take-Two/Cfx/Tebex rules, platform and search rules |
| [02-OPTIONS-RATED](en/gta6-income-options/02-OPTIONS-RATED.md) | every option: how it pays, evidence, agents vs human, risks, low/base/high income, the selection rule |
| [03-AGENT-PIPELINES](en/gta6-income-options/03-AGENT-PIPELINES.md) | where agents fail, the recommended combination, the pipeline with human gates and guard rails |
| [04-LAUNCH-PLAN-90-DAYS](en/gta6-income-options/04-LAUNCH-PLAN-90-DAYS.md) | phases, key dates, kill criteria, time and money budget |
| [05-EXCLUDED](en/gta6-income-options/05-EXCLUDED.md) | what is excluded and why, and what is legal but not recommended |
| [SOURCES](en/gta6-income-options/SOURCES.md) | all sources with quality notes |

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
