#!/usr/bin/env python3
"""macro_lab.py - recompute the course's lead/lag statistics from free FRED data.

Usage:
    python3 macro_lab.py [--out REPORT.md] [--cache .fred-cache] [--offline]

Standard library only (Python 3.9+). Downloads public CSVs from
https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES> (no API key) and
caches them for 24 h. Writes one Markdown report with every table the course
quotes, so you can refresh the numbers whenever you like.

Educational tool, not financial advice. Correlation is not causation, and
small samples (8 recessions, 3 bitcoin cycles) cannot prove a rule.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import math
import os
import statistics
import sys
import time
import urllib.request

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
Series = list  # list[tuple[dt.date, float]]


# ---------------------------------------------------------------- data access

def fetch(sid: str, cache: str, offline: bool = False) -> Series:
    """Return [(date, value)] for a FRED series, skipping missing values ('.')."""
    os.makedirs(cache, exist_ok=True)
    path = os.path.join(cache, sid + ".csv")
    fresh = os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400
    if not fresh and not offline:
        for attempt in range(4):
            try:
                data = urllib.request.urlopen(FRED.format(sid), timeout=120).read().decode()
                with open(path, "w", encoding="utf-8") as f:
                    f.write(data)
                break
            except Exception as exc:  # network hiccup: retry, then fall back to cache
                if attempt == 3:
                    if not os.path.exists(path):
                        raise SystemExit(f"cannot download {sid}: {exc}")
                    print(f"warning: {sid} download failed ({exc}); using cached copy", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
    out = []
    with open(path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) < 2 or row[0].startswith("observation") or row[0] == "DATE":
                continue
            try:
                out.append((dt.date.fromisoformat(row[0]), float(row[1])))
            except ValueError:
                pass
    return out


# ------------------------------------------------------------------- helpers

def month_key(d: dt.date) -> dt.date:
    return dt.date(d.year, d.month, 1)


def monthly(s: Series, how: str = "last") -> Series:
    """Resample to calendar months (last observation or mean)."""
    buckets: dict = {}
    for d, v in s:
        buckets.setdefault(month_key(d), []).append(v)
    return [(k, (v[-1] if how == "last" else statistics.fmean(v))) for k, v in sorted(buckets.items())]


def weekly(s: Series) -> Series:
    """Resample to weeks ending Sunday (last observation in the week)."""
    buckets: dict = {}
    for d, v in s:
        end = d + dt.timedelta(days=6 - d.weekday())
        buckets[end] = v
    return sorted(buckets.items())


def add_months(d: dt.date, n: int) -> dt.date:
    y, m = divmod(d.month - 1 + n, 12)
    return dt.date(d.year + y, m + 1, 1)


def months_between(a: dt.date, b: dt.date) -> int:
    return (b.year - a.year) * 12 + b.month - a.month


def value_on(s: Series, d: dt.date):
    """Last value on or before d (None if d precedes the series)."""
    lo, hi, best = 0, len(s) - 1, None
    while lo <= hi:
        mid = (lo + hi) // 2
        if s[mid][0] <= d:
            best, lo = s[mid][1], mid + 1
        else:
            hi = mid - 1
    return best


def pct(a, b):
    return None if a in (None, 0) or b is None else (b / a - 1) * 100


def yoy(s: Series, periods: int) -> Series:
    """Percent change versus the same date `periods` months earlier, matched by date, not by row.

    Matching by date matters: FRED leaves gaps (e.g. no October 2025 CPI after the government shutdown),
    and stepping back a fixed number of rows would then silently compare 13 months.
    """
    by_date = dict(s)
    out = []
    for d, v in s:
        prev = by_date.get(add_months(dt.date(d.year, d.month, 1), -periods))
        if prev and d.day == 1:
            out.append((d, (v / prev - 1) * 100))
    return out


def log_returns(s: Series) -> Series:
    return [(s[i][0], math.log(s[i][1] / s[i - 1][1])) for i in range(1, len(s)) if s[i][1] > 0 and s[i - 1][1] > 0]


def diffs(s: Series) -> Series:
    return [(s[i][0], s[i][1] - s[i - 1][1]) for i in range(1, len(s))]


def align(a: Series, b: Series):
    db = dict(b)
    pairs = [(d, v, db[d]) for d, v in a if d in db]
    return [p[0] for p in pairs], [p[1] for p in pairs], [p[2] for p in pairs]


def pearson(x, y):
    if len(x) < 8:
        return None
    mx, my = statistics.fmean(x), statistics.fmean(y)
    sx = math.sqrt(sum((v - mx) ** 2 for v in x))
    sy = math.sqrt(sum((v - my) ** 2 for v in y))
    return None if sx == 0 or sy == 0 else sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def lagged_corr(lead: Series, follow: Series, lag: int):
    """corr(lead[t], follow[t+lag]) on aligned, equally spaced series."""
    _, x, y = align(lead, follow)
    if lag > 0:
        x, y = x[:-lag], y[lag:]
    return pearson(x, y)


def sma(vals, n):
    return [None if i + 1 < n else statistics.fmean(vals[i + 1 - n:i + 1]) for i in range(len(vals))]


def ema(vals, n):
    k, out, e = 2 / (n + 1), [], None
    for v in vals:
        e = v if e is None else v * k + e * (1 - k)
        out.append(e)
    return out


def fmt(v, nd=1, suffix=""):
    return "n/a" if v is None else f"{v:,.{nd}f}{suffix}"


def table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


# ----------------------------------------------------------------- analyses

def recessions(usrec: Series):
    """NBER recessions as (start_month, end_month) from the monthly USREC dummy."""
    out, start = [], None
    for d, v in usrec:
        if v == 1 and start is None:
            start = d
        if v == 0 and start is not None:
            out.append((start, add_months(d, -1)))
            start = None
    if start is not None:
        out.append((start, None))
    return out


def inversion_episodes(spread_m: Series, min_months: int = 2):
    """Episodes where the monthly-average spread is < 0 for >= min_months.

    Returns (first_inverted_month, last_inverted_month, uninversion_month, min_value).
    Short gaps (one positive month) inside an episode are merged.
    """
    eps, cur = [], None
    for i, (d, v) in enumerate(spread_m):
        if v < 0:
            if cur and months_between(cur[1], d) <= 2:
                cur = [cur[0], d, min(cur[2], v)]
            else:
                if cur:
                    eps.append(cur)
                cur = [d, d, v]
    if cur:
        eps.append(cur)
    out = []
    for first, last, low in eps:
        if months_between(first, last) + 1 < min_months:
            continue
        un = add_months(last, 1)
        out.append((first, last, un if un <= spread_m[-1][0] else None, low))
    return out


def curve_section(spread_id, spread_m, recs):
    rows = []
    eps = inversion_episodes(spread_m)
    for first, last, un, low in eps:
        nxt = next((r for r in recs if r[0] >= first), None)
        if nxt and months_between(first, nxt[0]) > 36:
            nxt = None
        rows.append([
            first.strftime("%Y-%m"), un.strftime("%Y-%m") if un else "still inverted", fmt(low, 2),
            nxt[0].strftime("%Y-%m") if nxt else (
                "none within 36 m" if add_months(first, 36) <= spread_m[-1][0]
                else f"none yet (window open to {add_months(first, 36):%Y-%m})"),
            months_between(first, nxt[0]) if nxt else "-",
            months_between(un, nxt[0]) if (nxt and un) else "-",
        ])
    return (f"### Yield curve {spread_id}: inversion episodes vs NBER recessions\n\n"
            "Monthly averages; an episode is >= 2 inverted months (one-month gaps merged). "
            "'Un-inverted' = first month back above zero. Negative lag = recession began before the curve un-inverted.\n\n"
            + table(["first inverted", "un-inverted", "low (pp)", "next recession start",
                     "months inversion -> recession", "months un-inversion -> recession"], rows))


def sahm_section(sahm: Series, recs):
    rows, armed = [], True
    for d, v in sahm[12:]:  # the first year of the series has too little history behind it
        if v >= 0.5 and armed:
            nxt = next((r for r in recs if r[1] is None or r[1] >= add_months(d, -12)), None)
            nxt = nxt if nxt and months_between(nxt[0], d) <= 12 and months_between(d, nxt[0]) <= 12 else None
            rows.append([d.strftime("%Y-%m"), fmt(v, 2),
                         nxt[0].strftime("%Y-%m") if nxt else "no recession within 12 m",
                         months_between(nxt[0], d) if nxt else "-"])
            armed = False
        if v < 0.3:
            armed = True
    return ("### Sahm rule (real-time) triggers\n\n"
            "Trigger = first month the real-time Sahm indicator reaches 0.50; re-armed after it falls below 0.30. "
            "'Months after start' > 0 means the trigger came after the recession had already begun.\n\n"
            + table(["trigger month", "value", "recession start (+/-12 m)", "months after start"], rows))


def unemployment_section(un_m: Series, recs):
    rows, prev_end = [], None
    for start, end in recs:
        lo = max(add_months(start, -36), add_months(prev_end, 1) if prev_end else add_months(start, -36))
        prev_end = end
        window = [(d, v) for d, v in un_m if lo <= d <= start]
        trough = min(window, key=lambda p: (p[1], -p[0].toordinal()))
        at_start = value_on(un_m, start)
        after = [(d, v) for d, v in un_m if start <= d <= add_months(start, 36)]
        peak = max(after, key=lambda p: p[1]) if after else None
        rows.append([start.strftime("%Y-%m"), f"{trough[0]:%Y-%m} ({trough[1]:.1f}%)",
                     months_between(trough[0], start), fmt(at_start - trough[1], 1, " pp"),
                     f"{peak[0]:%Y-%m} ({peak[1]:.1f}%)" if peak else "n/a"])
    return ("### Unemployment rate: cycle low vs recession start\n\n"
            "Trough = lowest monthly U-3 rate in the 36 months before the recession began, but after the previous "
            "recession ended (latest month on ties).\n\n"
            + table(["recession start", "unemployment low", "months low -> recession",
                     "rise by recession start", "peak within 36 m"], rows))


def target_rate(cache, offline) -> Series:
    """Fed funds target: DFEDTAR (1982-2008) spliced with the range upper bound DFEDTARU (2008-)."""
    old = fetch("DFEDTAR", cache, offline)
    new = fetch("DFEDTARU", cache, offline)
    cut = new[0][0]
    return [p for p in old if p[0] < cut] + new


def fed_cycles(target: Series, min_step: float = 0.25):
    """(last_hike_date, first_cut_date, peak_rate) for every turn from hiking to cutting.

    Only moves of at least `min_step` percentage points count as policy moves, which filters out
    the 1980s fine-tuning adjustments of 1/16 to 3/16 of a point.
    """
    changes = [(target[i][0], target[i][1] - target[i - 1][1]) for i in range(1, len(target))
               if abs(target[i][1] - target[i - 1][1]) >= min_step - 1e-9]
    out, last_hike, hiked = [], None, 0.0
    for d, ch in changes:
        if ch > 0:
            last_hike, hiked = d, hiked + ch
        elif ch < 0:
            if last_hike is not None:
                out.append((last_hike, d, value_on(target, last_hike)))
            last_hike, hiked = None, 0.0
    return out


def fed_section(cycles, nasdaq, un_m, recs, btc):
    rows = []
    for hike, cut, peak in cycles:
        base = value_on(nasdaq, cut)
        fwd = [pct(base, value_on(nasdaq, cut + dt.timedelta(days=n))) for n in (91, 182, 365)]
        window = [v for d, v in nasdaq if cut <= d <= cut + dt.timedelta(days=548)]
        trough = (min(window) / base - 1) * 100 if window else None
        un0 = value_on(un_m, month_key(cut))
        later = [(d, v) for d, v in un_m if month_key(cut) <= d <= add_months(cut, 36)]
        unpk = max(later, key=lambda p: p[1]) if later else None
        rec = next((r for r in recs if month_key(cut) <= r[0] <= add_months(cut, 24)
                    or (r[0] <= month_key(cut) and (r[1] is None or r[1] >= month_key(cut)))), None)
        b = value_on(btc, cut) if btc and cut >= btc[0][0] else None
        b12 = pct(b, value_on(btc, cut + dt.timedelta(days=365))) if b else None
        rows.append([f"{hike:%Y-%m-%d}", f"{cut:%Y-%m-%d}", (cut - hike).days // 30, fmt(peak, 2, "%"),
                     fmt(fwd[0], 1, "%"), fmt(fwd[1], 1, "%"), fmt(fwd[2], 1, "%"), fmt(trough, 1, "%"),
                     f"{un0:.1f}% -> {unpk[1]:.1f}% ({months_between(month_key(cut), unpk[0])} m)" if unpk else "n/a",
                     rec[0].strftime("%Y-%m") if rec else "no", fmt(b12, 0, "%") if b12 is not None else "-"])
    return ("### Fed: from the last hike to the first cut, and what followed\n\n"
            "Target rate = DFEDTAR (1982-2008) + upper bound DFEDTARU; only moves >= 0.25 pp count. "
            "Dates are FRED effective dates (a cut announced in the evening shows the next day). Equity proxy = Nasdaq Composite (NASDAQCOM, the "
            "longest free daily index on FRED). 'Worst' = lowest close within 18 months after the first cut vs the "
            "close on the cut day. Unemployment peak searched within 36 months.\n\n"
            + table(["last hike", "first cut", "months paused", "peak target", "Nasdaq +3 m", "+6 m", "+12 m",
                     "worst within 18 m", "unemployment at cut -> peak (lag)", "recession within 24 m",
                     "BTC +12 m"], rows))


def presidential_section(nasdaq: Series):
    yearly = {}
    for d, v in nasdaq:
        yearly.setdefault(d.year, []).append((d, v))
    names = {0: "election year", 1: "post-election", 2: "midterm", 3: "pre-election"}
    stats = {k: [] for k in names}
    mid_rows = []
    years = sorted(yearly)
    for y in years[1:]:
        if y == dt.date.today().year:
            continue
        prev_close = yearly[y - 1][-1][1]
        ret = (yearly[y][-1][1] / prev_close - 1) * 100
        stats[y % 4].append(ret)
        if y % 4 == 2:
            closes = yearly[y]
            hi_run, dd, low_d, low_v = prev_close, 0.0, None, None
            for d, v in closes:
                hi_run = max(hi_run, v)
                dd = min(dd, (v / hi_run - 1) * 100)
                if low_v is None or v < low_v:
                    low_d, low_v = d, v
            after = pct(low_v, value_on(nasdaq, low_d + dt.timedelta(days=365)))
            mid_rows.append([y, fmt(ret, 1, "%"), fmt(dd, 1, "%"), f"{low_d:%Y-%m-%d}", fmt(after, 1, "%")])
    rows = [[names[k], len(v), fmt(statistics.fmean(v), 1, "%"), fmt(statistics.median(v), 1, "%"),
             f"{sum(1 for r in v if r > 0)}/{len(v)}"] for k, v in stats.items() if v]
    return ("### Presidential cycle (Nasdaq Composite, calendar-year returns since 1972)\n\n"
            + table(["year of the cycle", "years", "mean", "median", "up years"], rows)
            + "\n\n#### Midterm years in detail\n\n"
            + table(["year", "calendar return", "max drawdown in year", "date of year low", "low -> +12 m"], mid_rows))


def btc_section(btc_d: Series, nasdaq: Series, dollar: Series, real10: Series, walcl, tga, rrp, m2, eth_d, target):
    w = weekly(btc_d)
    dates, closes = [d for d, _ in w], [v for _, v in w]
    s200, s20, e21 = sma(closes, 200), sma(closes, 20), ema(closes, 21)
    last = len(closes) - 1
    genesis = dt.date(2009, 1, 3)
    xs = [math.log10((d - genesis).days) for d in dates]
    ys = [math.log10(v) for v in closes]
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    resid = [y - (a + b * x) for x, y in zip(xs, ys)]
    sd = statistics.pstdev(resid)
    fair = 10 ** (a + b * xs[last])
    ath_i = max(range(len(closes)), key=closes.__getitem__)
    status = table(["metric", "value"], [
        ["latest close (week ending)", f"{dates[last]:%Y-%m-%d}: ${closes[last]:,.0f}"],
        ["all-time high (weekly close)", f"{dates[ath_i]:%Y-%m-%d}: ${closes[ath_i]:,.0f}"],
        ["drawdown from ATH", fmt((closes[last] / closes[ath_i] - 1) * 100, 1, "%")],
        ["200-week SMA", f"${s200[last]:,.0f} (price is {abs(pct(s200[last], closes[last])):.0f}% "
                         f"{'above' if closes[last] >= s200[last] else 'below'} it)"],
        ["bull market support band (20W SMA / 21W EMA)", f"${s20[last]:,.0f} / ${e21[last]:,.0f}"],
        ["log-regression fair value (fit since 2014-12)", f"${fair:,.0f}; price/fair = {closes[last] / fair:.2f}"],
        ["regression residual in std devs (z)", fmt(resid[last] / sd, 2)],
        ["fitted slope b in log10(price) = a + b*log10(days since 2009-01-03)", fmt(b, 2)],
    ])

    def corr_row(name, other, transform):
        ow = weekly(other)
        x = log_returns(w)
        y = transform(ow)
        _, xa, ya = align(x, y)
        full = pearson(xa, ya)
        last52 = pearson(xa[-52:], ya[-52:])
        yearly = []
        for yr in range(2016, dt.date.today().year + 1):
            _, xx, yy = align([p for p in x if p[0].year == yr], [p for p in y if p[0].year == yr])
            yearly.append(fmt(pearson(xx, yy), 2))
        return [name, fmt(full, 2), fmt(last52, 2)] + yearly

    years = list(range(2016, dt.date.today().year + 1))
    corr = table(["BTC weekly log-return vs", "all weeks", "last 52 w"] + [str(y) for y in years], [
        corr_row("Nasdaq weekly log-return", nasdaq, log_returns),
        corr_row("broad dollar (DTWEXBGS) log-return", dollar, log_returns),
        corr_row("10y real yield (DFII10) weekly change", real10, diffs),
    ])

    # Liquidity lead/lag: net liquidity = Fed balance sheet - TGA - reverse repo (all in $bn).
    wal = {d: v / 1000 for d, v in weekly(walcl)}
    tg = {d: v / 1000 for d, v in weekly(tga)}
    rr = dict(weekly(rrp))
    net = sorted((d, wal[d] - tg[d] - rr.get(d, 0.0)) for d in wal if d in tg)
    net = [p for p in net if p[0] >= dt.date(2015, 1, 1)]
    btc13 = [(w[i][0], math.log(w[i][1] / w[i - 13][1])) for i in range(13, len(w))]
    net13 = [(net[i][0], net[i][1] - net[i - 13][1]) for i in range(13, len(net))]
    liq_rows = [[f"{lag} w", fmt(lagged_corr(net13, btc13, lag), 2)] for lag in (0, 4, 8, 12, 16, 26)]

    m2m = monthly(m2)
    btcm = monthly(btc_d)
    m2y, btcy = yoy(m2m, 12), yoy(btcm, 12)
    m2_rows = [[f"{lag} m", fmt(lagged_corr(m2y, btcy, lag), 2)] for lag in (0, 2, 3, 6, 9, 12)]

    ethbtc = []
    ed = dict(eth_d)
    for d, v in btc_d:
        if d in ed and v:
            ethbtc.append((d, ed[d] / v))
    ew = weekly(ethbtc)
    eth_rows = []
    for yr in range(2017, dt.date.today().year + 1):
        pts = [p for p in ew if p[0].year == yr]
        if len(pts) > 4:
            t0, t1 = value_on(target, dt.date(yr, 1, 1)), value_on(target, dt.date(yr, 12, 31))
            eth_rows.append([yr, f"{pts[0][1]:.4f}", f"{pts[-1][1]:.4f}", fmt(pct(pts[0][1], pts[-1][1]), 0, "%"),
                             fmt(t1 - t0, 2, " pp") if t0 is not None and t1 is not None else "n/a"])

    return ("### Bitcoin status (Coinbase BTC-USD, FRED CBBTCUSD)\n\n" + status
            + "\n\nThe regression here is fitted only on data since Dec 2014 (FRED's coverage), so its slope and fair value "
              "differ from fits that include 2010-2014; use it to learn the method, not as the canonical fair value.\n\n"
            + "### Rolling correlations (weekly)\n\n" + corr
            + "\n\n### Does net liquidity lead bitcoin? (13-week change in WALCL - TGA - RRP vs 13-week BTC log-return)\n\n"
            + table(["net liquidity leads by", "correlation"], liq_rows)
            + "\n\n### Does M2 lead bitcoin? (US M2 YoY vs BTC YoY, monthly)\n\n"
            + table(["M2 leads by", "correlation"], m2_rows)
            + "\n\nOverlapping YoY windows inflate correlations; treat these as descriptive.\n\n"
            + "### ETH/BTC by calendar year vs the change in the Fed target rate\n\n"
            + table(["year", "ETH/BTC first week", "last week", "change", "Fed target change in year"], eth_rows))


def dashboard(cache, offline):
    spec = [
        ("Fed funds target, upper bound (%)", "DFEDTARU", None),
        ("2-year Treasury yield (%)", "DGS2", None),
        ("10-year Treasury yield (%)", "DGS10", None),
        ("10y-2y spread (pp)", "T10Y2Y", None),
        ("10y-3m spread (pp)", "T10Y3M", None),
        ("10y real yield, TIPS (%)", "DFII10", None),
        ("10y breakeven inflation (%)", "T10YIE", None),
        ("High-yield credit spread (pp)", "BAMLH0A0HYM2", None),
        ("Unemployment rate (%)", "UNRATE", None),
        ("Sahm rule real-time (pp)", "SAHMREALTIME", None),
        ("Initial jobless claims", "ICSA", None),
        ("CPI, YoY (%)", "CPIAUCSL", 12),
        ("Core PCE, YoY (%)", "PCEPILFE", 12),
        ("M2, YoY (%)", "M2SL", 12),
        ("Fed balance sheet ($bn)", "WALCL", None),
        ("Reverse repo ($bn)", "RRPONTSYD", None),
        ("Broad dollar index", "DTWEXBGS", None),
        ("VIX", "VIXCLS", None),
        ("Bitcoin (USD)", "CBBTCUSD", None),
    ]
    rows = []
    for name, sid, yo in spec:
        s = fetch(sid, cache, offline)
        if yo:
            s = yoy(s, yo)
        if sid == "WALCL":
            s = [(d, v / 1000) for d, v in s]
        d, v = s[-1]
        m3 = value_on(s, d - dt.timedelta(days=91))
        y1 = value_on(s, d - dt.timedelta(days=365))
        rows.append([name, sid, f"{d:%Y-%m-%d}", fmt(v, 2), fmt(m3, 2), fmt(y1, 2)])
    return "### Dashboard: latest values\n\n" + table(["indicator", "FRED id", "as of", "latest", "3 m ago", "1 y ago"], rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="REPORT.md")
    ap.add_argument("--cache", default=".fred-cache")
    ap.add_argument("--offline", action="store_true", help="use cached CSVs only")
    a = ap.parse_args()
    f = lambda sid: fetch(sid, a.cache, a.offline)  # noqa: E731

    recs = recessions(f("USREC"))
    recs = [r for r in recs if r[0].year >= 1960]
    un_m = f("UNRATE")
    nasdaq = f("NASDAQCOM")
    target = target_rate(a.cache, a.offline)
    btc = f("CBBTCUSD")
    parts = [
        f"# macro_lab report\n\nGenerated {dt.datetime.now():%Y-%m-%d %H:%M} from FRED. "
        "Educational, not financial advice.\n",
        dashboard(a.cache, a.offline),
        "### NBER recessions since 1960\n\n" + table(
            ["start", "end"], [[s.strftime("%Y-%m"), e.strftime("%Y-%m") if e else "ongoing"] for s, e in recs]),
        curve_section("10y-3m (T10Y3M)", monthly(f("T10Y3M"), "mean"), recs),
        curve_section("10y-2y (T10Y2Y)", monthly(f("T10Y2Y"), "mean"), recs),
        sahm_section(f("SAHMREALTIME"), recs),
        unemployment_section(un_m, recs),
        fed_section(fed_cycles(target), nasdaq, un_m, recs, btc),
        presidential_section(nasdaq),
        btc_section(btc, nasdaq, f("DTWEXBGS"), f("DFII10"), f("WALCL"), f("WTREGEN"), f("RRPONTSYD"),
                    f("M2SL"), f("CBETHUSD"), target),
    ]
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(parts) + "\n")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    sys.exit(main())
