#!/usr/bin/env python3
"""Stock-price reaction to cybersecurity 8-K filings.

Scrapes board-cybersecurity.com's incident tracker for the N most recent
SEC 8-K cybersecurity disclosures, pulls each company's ticker, fetches
daily closes from Yahoo Finance (Stooq fallback), and computes the price
change from the last close before the filing to ~1 week and ~1 month after.

Outputs a self-contained HTML report (chart + table) and prints a summary.

Note: Yahoo occasionally returns empty history for delisted or
recently-reorganized tickers; affected rows show "no data" in the report
and usually resolve on a later rerun.

Usage:
    python3 cyber8k_report.py [--count 51] [--output akira/8k-market-reaction.html]

Stdlib only — no dependencies.
"""

import argparse
import csv
import datetime as dt
import io
import json
import re
import statistics
import sys
import time
import urllib.request
from pathlib import Path

BASE = "https://www.board-cybersecurity.com"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "akira" / "8k-market-reaction.html"


def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")


# ---------------------------------------------------------------- scraping

def scrape_8k_entries(count):
    """Walk tracker pages; return the first `count` rows sourced from SEC 8-K."""
    found = []
    for page in range(1, 100):
        html = get(f"{BASE}/incidents/tracker?page={page}")
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)[1:]  # skip header
        if not rows:
            break
        for row in rows:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
            if len(cells) < 3:
                continue
            clean = [re.sub(r"<[^>]+>", " ", c).strip() for c in cells]
            if "SEC 8-K" not in clean[2]:
                continue
            link = re.search(r'href="(/incidents/tracker/[^"]+)"', row)
            found.append({
                "date": clean[0],
                "company": re.sub(r"\s+", " ", clean[1]),
                "link": link.group(1) if link else None,
            })
        print(f"  tracker page {page}: {len(found)} 8-K entries", file=sys.stderr)
        if len(found) >= count:
            return found[:count]
        time.sleep(0.3)
    return found


def fetch_ticker(entry):
    """Read the incident detail page for the ticker symbol."""
    if not entry["link"]:
        return None
    text = re.sub(r"<[^>]+>", "\n", get(BASE + entry["link"]))
    m = re.search(r"Ticker\s*\n\s*([A-Z][A-Z0-9.\-]{0,9})\s*\n", text)
    return m.group(1) if m else None


# ------------------------------------------------------------------ prices

def prices_yahoo(sym, d1, d2):
    p1 = int(dt.datetime(d1.year, d1.month, d1.day).timestamp())
    p2 = int(dt.datetime(d2.year, d2.month, d2.day).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?period1={p1}&period2={p2}&interval=1d")
    try:
        data = json.loads(get(url))
        res = data["chart"]["result"][0]
        out = {}
        for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]):
            if c is not None:
                out[dt.datetime.fromtimestamp(t, dt.timezone.utc).date()] = round(c, 4)
        return out
    except Exception:
        return {}


def prices_stooq(sym, d1, d2):
    url = (f"https://stooq.com/q/d/l/?s={sym.lower()}.us"
           f"&d1={d1:%Y%m%d}&d2={d2:%Y%m%d}&i=d")
    try:
        body = get(url)
        if not body.startswith("Date"):
            return {}
        return {dt.date.fromisoformat(r["Date"]): float(r["Close"])
                for r in csv.DictReader(io.StringIO(body))
                if r.get("Close") not in (None, "", "N/D")}
    except Exception:
        return {}


def last_before(prices, target):
    ds = sorted(d for d in prices if d < target)
    return prices[ds[-1]] if ds else None


def first_on_after(prices, target):
    ds = sorted(d for d in prices if d >= target)
    return prices[ds[0]] if ds else None


def measure(entry, today):
    fdate = dt.date.fromisoformat(entry["date"])
    d1 = fdate - dt.timedelta(days=14)
    d2 = min(fdate + dt.timedelta(days=100), today)
    sym = entry["ticker"]
    prices = {}
    if sym:
        for attempt in range(3):
            prices = prices_yahoo(sym, d1, d2)
            if prices:
                break
            time.sleep(1.5 * (attempt + 1))
        if not prices:
            prices = prices_stooq(sym, d1, d2)
        if not prices:
            print(f"  warning: no price history for {sym} "
                  f"(delisted, OTC, or source temporarily missing data)", file=sys.stderr)
    prev = last_before(prices, fdate)
    wk = mo = qt = None
    if fdate + dt.timedelta(days=7) <= today:
        wk = first_on_after(prices, fdate + dt.timedelta(days=7))
    if fdate + dt.timedelta(days=30) <= today:
        mo = first_on_after(prices, fdate + dt.timedelta(days=30))
    if fdate + dt.timedelta(days=90) <= today:
        qt = first_on_after(prices, fdate + dt.timedelta(days=90))
    pct = lambda v: round((v / prev - 1) * 100, 2) if v and prev else None
    return {
        "company": entry["company"], "ticker": sym, "date": entry["date"],
        "prev_close": prev, "week_close": wk, "month_close": mo, "quarter_close": qt,
        "week_pct": pct(wk), "month_pct": pct(mo), "quarter_pct": pct(qt),
    }


# ------------------------------------------------------------------ report

HTML_TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stock reaction to cybersecurity 8-Ks</title>
<style>
  :root {
    --surface: #fcfcfb; --page: #f9f9f7;
    --ink: #0b0b0b; --ink-2: #52514e; --muted: #898781;
    --grid: #e1e0d9; --baseline: #c3c2b7;
    --border: rgba(11,11,11,0.10);
    --wk: #2a78d6; --mo: #1baf7a;
    --neg: #a33b3b; --pos: #006300;
    --tip-bg: #0b0b0b; --tip-ink: #fcfcfb;
    --rowhover: rgba(42,120,214,0.07);
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --surface: #1a1a19; --page: #0d0d0d;
      --ink: #ffffff; --ink-2: #c3c2b7; --muted: #898781;
      --grid: #2c2c2a; --baseline: #383835;
      --border: rgba(255,255,255,0.10);
      --wk: #3987e5; --mo: #199e70;
      --neg: #e66767; --pos: #0ca30c;
      --tip-bg: #f4f4f0; --tip-ink: #111110;
      --rowhover: rgba(57,135,229,0.10);
    }
  }
  html, body { margin: 0; background: var(--page); color: var(--ink);
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif; line-height: 1.5; }
  .wrap { max-width: 920px; margin: 0 auto; padding: 40px 20px 72px; }
  .eyebrow { font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--muted); font-weight: 600; margin-bottom: 10px; }
  h1 { font-size: clamp(24px, 4vw, 34px); line-height: 1.15; font-weight: 700;
    letter-spacing: -0.015em; margin: 0 0 12px; text-wrap: balance; }
  .lede { color: var(--ink-2); font-size: 15px; max-width: 66ch; margin: 0 0 8px; }
  .method { color: var(--muted); font-size: 13px; max-width: 72ch; margin: 0; }
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px; margin: 32px 0; }
  .kpi { background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 14px 16px; }
  .kpi .lbl { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;
    color: var(--muted); font-weight: 600; }
  .kpi .val { font-size: 30px; font-weight: 700; letter-spacing: -0.02em; margin: 4px 0 2px; }
  .kpi .val.up { color: var(--pos); } .kpi .val.dn { color: var(--neg); }
  .kpi .sub { font-size: 12px; color: var(--muted); }
  .panel { background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; padding: 20px 20px 12px; margin: 28px 0; }
  .panel h2 { font-size: 16px; font-weight: 700; margin: 0 0 2px; }
  .panel .note { font-size: 12.5px; color: var(--muted); margin: 0 0 14px; }
  .legend { display: flex; gap: 18px; align-items: center; font-size: 12.5px;
    color: var(--ink-2); margin-bottom: 10px; flex-wrap: wrap; }
  .legend .sw { display: inline-block; width: 12px; height: 12px; border-radius: 3px;
    vertical-align: -1px; margin-right: 6px; }
  .chart-scroll { overflow-x: auto; }
  #chart { display: block; width: 100%; height: auto; min-width: 620px; }
  .tip { position: fixed; pointer-events: none; z-index: 10; background: var(--tip-bg);
    color: var(--tip-ink); border-radius: 6px; padding: 8px 10px; font-size: 12px;
    line-height: 1.45; max-width: 260px; opacity: 0; transition: opacity 80ms;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25); }
  @media (prefers-reduced-motion: reduce) { .tip { transition: none; } }
  .tip b { font-size: 12.5px; }
  .tip .trow { display: flex; justify-content: space-between; gap: 14px;
    font-variant-numeric: tabular-nums; }
  .tablewrap { overflow-x: auto; margin-top: 14px; border: 1px solid var(--border);
    border-radius: 10px; background: var(--surface); }
  table { border-collapse: collapse; width: 100%; font-size: 12.8px; min-width: 760px; }
  th { text-align: right; font-size: 10.5px; letter-spacing: 0.09em;
    text-transform: uppercase; color: var(--muted); font-weight: 600;
    padding: 10px 10px 8px; border-bottom: 1px solid var(--grid); white-space: nowrap; }
  th:first-child, td:first-child { text-align: left; padding-left: 16px; }
  th:nth-child(2), td:nth-child(2) { text-align: left; }
  td { padding: 7px 10px; border-bottom: 1px solid var(--grid); text-align: right;
    font-variant-numeric: tabular-nums; white-space: nowrap; color: var(--ink-2); }
  tr:last-child td { border-bottom: none; }
  tbody tr:hover { background: var(--rowhover); }
  td.co { color: var(--ink); font-weight: 600; max-width: 230px; overflow: hidden;
    text-overflow: ellipsis; }
  td .tick { color: var(--muted); font-weight: 400; }
  td.up { color: var(--pos); font-weight: 600; } td.dn { color: var(--neg); font-weight: 600; }
  td.na { color: var(--muted); }
  .foot { font-size: 12px; color: var(--muted); max-width: 78ch; margin-top: 28px; }
</style></head><body>
<div class="wrap">
  <div class="eyebrow">Market reaction study &middot; data as of __ASOF__</div>
  <h1>Does the market punish a cybersecurity 8-K?</h1>
  <p class="lede">The __N__ most recent SEC 8-K cybersecurity disclosures from the
    Board-Cybersecurity incident tracker, with each company's share price the day
    before the filing and roughly one week and one month after.</p>
  <p class="method">Returns are measured from the last close <em>before</em> the 8-K
    date to the first close on/after +7 and +30 calendar days. Recent filings
    without a one-week or one-month price yet are shown as pending.</p>
  <div class="kpis">
    <div class="kpi"><div class="lbl">Median, 1 week later</div>
      <div class="val __WK_CLS__">__WK_MED__</div><div class="sub">__WK_N__ of __N__ measurable</div></div>
    <div class="kpi"><div class="lbl">Median, 1 month later</div>
      <div class="val __MO_CLS__">__MO_MED__</div><div class="sub">__MO_N__ of __N__ measurable</div></div>
    <div class="kpi"><div class="lbl">Up after 1 week</div>
      <div class="val">__WK_UP__ / __WK_N__</div><div class="sub">of measurable companies</div></div>
    <div class="kpi"><div class="lbl">Up after 1 month</div>
      <div class="val">__MO_UP__ / __MO_N__</div><div class="sub">of measurable companies</div></div>
  </div>
  <div class="panel">
    <h2>Backtest: short every filer, three holding periods</h2>
    <p class="note">Hypothetical: short $1,000 of each company right after its cyber
      8-K, cover at +1 week, +1 month, or +3 months. Flat $1,000 notional per name,
      no leverage, no borrow fees or commissions modeled. Column N shrinks with
      horizon &mdash; only filings old enough to reach that date are included.</p>
    <div class="tablewrap">
      <table>
        <thead><tr>
          <th style="text-align:left;padding-left:16px">Holding period</th>
          <th>Total P&amp;L</th><th>Return on capital</th><th>Win rate</th><th>Worst single loss</th>
        </tr></thead>
        <tbody>
          <tr>
            <td class="co" style="text-align:left">1 week</td>
            <td class="__SHORT_CLS__">__SHORT_PNL__</td>
            <td class="__SHORT_CLS__">__SHORT_ROC__</td>
            <td>__SHORT_WINS__ / __SHORT_N__</td>
            <td class="dn">__SHORT_WORST__ (__SHORT_WORST_TICKER__)</td>
          </tr>
          <tr>
            <td class="co" style="text-align:left">1 month</td>
            <td class="__SHORT30_CLS__">__SHORT30_PNL__</td>
            <td class="__SHORT30_CLS__">__SHORT30_ROC__</td>
            <td>__SHORT30_WINS__ / __SHORT30_N__</td>
            <td class="dn">__SHORT30_WORST__ (__SHORT30_WORST_TICKER__)</td>
          </tr>
          <tr>
            <td class="co" style="text-align:left">3 months</td>
            <td class="__SHORT90_CLS__">__SHORT90_PNL__</td>
            <td class="__SHORT90_CLS__">__SHORT90_ROC__</td>
            <td>__SHORT90_WINS__ / __SHORT90_N__</td>
            <td class="dn">__SHORT90_WORST__ (__SHORT90_WORST_TICKER__)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="note" style="margin-top:10px">Short-selling has uncapped downside &mdash;
      each row's worst loss shows a single name that can wipe out many winners.</p>
  </div>
  <div class="panel">
    <h2>Price change after the 8-K, by company</h2>
    <p class="note">Percent change vs. the close on the trading day before the filing.
      Newest filings at top. Bars are clipped at &plusmn;50% &mdash; clipped values are labeled.
      Hover any bar for exact prices.</p>
    <div class="legend">
      <span><span class="sw" style="background:var(--wk)"></span>1 week later</span>
      <span><span class="sw" style="background:var(--mo)"></span>1 month later</span>
      <span style="color:var(--muted)">&mdash; not yet available</span>
    </div>
    <div class="chart-scroll"><svg id="chart" xmlns="http://www.w3.org/2000/svg"></svg></div>
  </div>
  <h2 style="font-size:16px">Full data</h2>
  <div class="tablewrap"><table id="tbl">
    <thead><tr>
      <th>Company</th><th>8-K date</th><th>Prev close</th>
      <th>+1 wk close</th><th>+1 wk %</th><th>+1 mo close</th><th>+1 mo %</th>
    </tr></thead><tbody></tbody>
  </table></div>
  <div class="foot">
    <p><strong>Sources &amp; caveats.</strong> Companies and 8-K dates from
      board-cybersecurity.com's incident tracker (source column "SEC 8-K"); daily
      closes from Yahoo Finance. Dates are the tracker's latest 8-K activity date,
      which for some names is an amendment to an earlier disclosure. A small,
      recent sample &mdash; treat any pattern as suggestive, not statistical proof.</p>
  </div>
</div>
<div class="tip" id="tip"></div>
<script>
const DATA = __DATA__;
const esc = v => String(v == null ? '' : v).replace(/[&<>'"]/g, ch => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'}[ch]));
const fmt$ = v => v == null ? '—' : (v < 1 ? '$' + v.toFixed(4) : '$' + v.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}));
const fmtP = v => v == null ? '—' : (v > 0 ? '+' : '') + v.toFixed(Math.abs(v) >= 100 ? 0 : 1) + '%';

const rows = DATA.filter(d => d.prev_close != null);
const CLAMP = 50, ROWH = 30, BARH = 9, GAP = 2;
const ML = 60, MR = 24, MT = 22, MB = 8, PW = 660;
const H = MT + rows.length * ROWH + MB;
const svg = document.getElementById('chart');
svg.setAttribute('viewBox', `0 0 ${ML + PW + MR} ${H}`);
const x = v => ML + (Math.max(-CLAMP, Math.min(CLAMP, v)) + CLAMP) / (2 * CLAMP) * PW;
const NS = 'http://www.w3.org/2000/svg';
const el = (tag, attrs, parent) => {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  (parent || svg).appendChild(e); return e;
};

[-50, -25, 0, 25, 50].forEach(v => {
  el('line', {x1: x(v), x2: x(v), y1: MT - 4, y2: H - MB,
    stroke: v === 0 ? 'var(--baseline)' : 'var(--grid)',
    'stroke-width': v === 0 ? 1.5 : 1});
  const t = el('text', {x: x(v), y: MT - 9, 'text-anchor': 'middle',
    'font-size': 10.5, fill: 'var(--muted)'});
  t.textContent = (v > 0 ? '+' : '') + v + '%';
});

const tip = document.getElementById('tip');
function showTip(evt, d) {
  tip.innerHTML = `<b>${esc(d.company)} (${esc(d.ticker)})</b><br>8-K filed ${esc(d.date)}
    <div class="trow"><span>Close before</span><span>${fmt$(d.prev_close)}</span></div>
    <div class="trow"><span>+1 week</span><span>${d.week_close == null ? 'pending' : fmt$(d.week_close) + '  ' + fmtP(d.week_pct)}</span></div>
    <div class="trow"><span>+1 month</span><span>${d.month_close == null ? 'pending' : fmt$(d.month_close) + '  ' + fmtP(d.month_pct)}</span></div>`;
  tip.style.opacity = 1;
  moveTip(evt);
}
function moveTip(evt) {
  const w = tip.offsetWidth, vw = window.innerWidth;
  let lx = evt.clientX + 14; if (lx + w > vw - 8) lx = evt.clientX - w - 14;
  tip.style.left = lx + 'px';
  tip.style.top = Math.max(8, evt.clientY - 20) + 'px';
}
const hideTip = () => tip.style.opacity = 0;

rows.forEach((d, i) => {
  const y0 = MT + i * ROWH;
  const g = el('g', {});
  const hit = el('rect', {x: 0, y: y0, width: ML + PW + MR, height: ROWH, fill: 'transparent'}, g);
  const lab = el('text', {x: ML - 8, y: y0 + ROWH / 2 + 4, 'text-anchor': 'end',
    'font-size': 11.5, 'font-weight': 600, fill: 'var(--ink-2)'}, g);
  lab.textContent = d.ticker;

  const bar = (val, cy, color) => {
    if (val == null) {
      const t = el('text', {x: x(0) + 6, y: cy + BARH / 2 + 3.5, 'font-size': 10,
        fill: 'var(--muted)'}, g);
      t.textContent = '—';
      return;
    }
    const clipped = Math.abs(val) > CLAMP;
    const xa = x(0), xb = x(val);
    el('rect', {x: Math.min(xa, xb), y: cy, width: Math.max(1, Math.abs(xb - xa)),
      height: BARH, rx: 2.5, fill: color}, g);
    if (clipped) {
      const dir = val > 0 ? 1 : -1;
      el('path', {d: `M ${xb + dir * 1} ${cy} l ${dir * 4} ${BARH / 2} l ${-dir * 4} ${BARH / 2} Z`,
        fill: color}, g);
      const t = el('text', {x: xb - dir * 8, y: cy + BARH / 2 + 3.5,
        'text-anchor': val > 0 ? 'end' : 'start', 'font-size': 10,
        'font-weight': 700, fill: 'var(--ink)',
        stroke: 'var(--surface)', 'stroke-width': 3, 'paint-order': 'stroke'}, g);
      t.textContent = fmtP(val);
    }
  };
  const mid = y0 + (ROWH - (BARH * 2 + GAP)) / 2;
  bar(d.week_pct, mid, 'var(--wk)');
  bar(d.month_pct, mid + BARH + GAP, 'var(--mo)');

  hit.addEventListener('mousemove', e => showTip(e, d));
  hit.addEventListener('mouseleave', hideTip);
});

const tb = document.querySelector('#tbl tbody');
DATA.forEach(d => {
  const tr = document.createElement('tr');
  const pctCell = v => v == null ? `<td class="na">—</td>`
    : `<td class="${v >= 0 ? 'up' : 'dn'}">${fmtP(v)}</td>`;
  tr.innerHTML =
    `<td class="co">${esc(d.company)} <span class="tick">${esc(d.ticker)}</span></td>` +
    `<td style="text-align:left">${esc(d.date)}</td>` +
    `<td>${d.prev_close == null ? '<span class="na">no data</span>' : fmt$(d.prev_close)}</td>` +
    `<td class="${d.week_close == null ? 'na' : ''}">${fmt$(d.week_close)}</td>` + pctCell(d.week_pct) +
    `<td class="${d.month_close == null ? 'na' : ''}">${fmt$(d.month_close)}</td>` + pctCell(d.month_pct);
  tb.appendChild(tr);
});
</script>
</body></html>
"""


def build_report(results, today):
    wk = [r["week_pct"] for r in results if r["week_pct"] is not None]
    mo = [r["month_pct"] for r in results if r["month_pct"] is not None]
    fmt_med = lambda v: ("+" if v > 0 else "") + f"{v:.1f}%"
    cls = lambda v: "up" if v > 0 else ("dn" if v < 0 else "")
    wk_med = statistics.median(wk) if wk else 0
    mo_med = statistics.median(mo) if mo else 0

    shorts = [(r["ticker"], -r["week_pct"]) for r in results if r["week_pct"] is not None]
    short_n = len(shorts)
    short_pnl = sum(1000 * (ret / 100) for _, ret in shorts)
    short_wins = sum(1 for _, ret in shorts if ret > 0)
    worst_ticker, worst_ret = min(shorts, key=lambda s: s[1], default=(None, 0))
    worst_pnl = 1000 * (worst_ret / 100)
    fmt_money = lambda v: ("+" if v > 0 else ("-" if v < 0 else "")) + "$" + f"{abs(v):,.2f}"

    shorts30 = [(r["ticker"], -r["month_pct"]) for r in results if r["month_pct"] is not None]
    short30_n = len(shorts30)
    short30_pnl = sum(1000 * (ret / 100) for _, ret in shorts30)
    short30_wins = sum(1 for _, ret in shorts30 if ret > 0)
    worst30_ticker, worst30_ret = min(shorts30, key=lambda s: s[1], default=(None, 0))
    worst30_pnl = 1000 * (worst30_ret / 100)

    shorts90 = [(r["ticker"], -r["quarter_pct"]) for r in results if r.get("quarter_pct") is not None]
    short90_n = len(shorts90)
    short90_pnl = sum(1000 * (ret / 100) for _, ret in shorts90)
    short90_wins = sum(1 for _, ret in shorts90 if ret > 0)
    worst90_ticker, worst90_ret = min(shorts90, key=lambda s: s[1], default=(None, 0))
    worst90_pnl = 1000 * (worst90_ret / 100)

    subs = {
        "__ASOF__": today.strftime("%b %-d, %Y"),
        "__N__": str(len(results)),
        "__WK_MED__": fmt_med(wk_med) if wk else "—",
        "__MO_MED__": fmt_med(mo_med) if mo else "—",
        "__WK_CLS__": cls(wk_med), "__MO_CLS__": cls(mo_med),
        "__WK_N__": str(len(wk)), "__MO_N__": str(len(mo)),
        "__WK_UP__": str(sum(1 for v in wk if v > 0)),
        "__MO_UP__": str(sum(1 for v in mo if v > 0)),
        "__DATA__": json.dumps(results),
        "__SHORT_CLS__": cls(short_pnl),
        "__SHORT_PNL__": fmt_money(short_pnl) if short_n else "—",
        "__SHORT_DEPLOYED__": f"{short_n * 1000:,}",
        "__SHORT_ROC__": fmt_med(short_pnl / (short_n * 1000) * 100) if short_n else "—",
        "__SHORT_WINS__": str(short_wins),
        "__SHORT_N__": str(short_n),
        "__SHORT_WORST__": fmt_money(worst_pnl) if short_n else "—",
        "__SHORT_WORST_TICKER__": worst_ticker or "—",
        "__SHORT30_CLS__": cls(short30_pnl),
        "__SHORT30_PNL__": fmt_money(short30_pnl) if short30_n else "—",
        "__SHORT30_DEPLOYED__": f"{short30_n * 1000:,}",
        "__SHORT30_ROC__": fmt_med(short30_pnl / (short30_n * 1000) * 100) if short30_n else "—",
        "__SHORT30_WINS__": str(short30_wins),
        "__SHORT30_N__": str(short30_n),
        "__SHORT30_WORST__": fmt_money(worst30_pnl) if short30_n else "—",
        "__SHORT30_WORST_TICKER__": worst30_ticker or "—",
        "__SHORT90_CLS__": cls(short90_pnl),
        "__SHORT90_PNL__": fmt_money(short90_pnl) if short90_n else "—",
        "__SHORT90_DEPLOYED__": f"{short90_n * 1000:,}",
        "__SHORT90_ROC__": fmt_med(short90_pnl / (short90_n * 1000) * 100) if short90_n else "—",
        "__SHORT90_WINS__": str(short90_wins),
        "__SHORT90_N__": str(short90_n),
        "__SHORT90_WORST__": fmt_money(worst90_pnl) if short90_n else "—",
        "__SHORT90_WORST_TICKER__": worst90_ticker or "—",
    }
    html = HTML_TEMPLATE
    for k, v in subs.items():
        html = html.replace(k, v)
    return html


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--count", type=int, default=51, help="number of 8-K filers (default 51)")
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT), help="output HTML file")
    args = ap.parse_args()
    today = dt.date.today()

    print(f"Scraping tracker for first {args.count} SEC 8-K entries...", file=sys.stderr)
    entries = scrape_8k_entries(args.count)

    results = []
    for e in entries:
        e["ticker"] = fetch_ticker(e)
        r = measure(e, today)
        results.append(r)
        print(f"  {r['ticker'] or '????':6} {r['date']}  prev={r['prev_close']}"
              f"  1wk={r['week_pct']}%  1mo={r['month_pct']}%", file=sys.stderr)
        time.sleep(0.3)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        f.write(build_report(results, today))
    print(f"\nWrote {output} ({len(results)} companies). Open it in a browser.")


if __name__ == "__main__":
    main()
