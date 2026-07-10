#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, html, json, os, re, sqlite3, subprocess, urllib.request
from pathlib import Path
from urllib.parse import quote_plus

from maintenance_reliability import enrich_listing


ROOT=Path(__file__).resolve().parents[1]
TODAY=dt.date.today().isoformat()
CL_URL='https://norfolk.craigslist.org/search/cta?max_price=10000&postal=23462&search_distance=50'
AT_URL='https://www.autotempest.com/results?zip=23462&radius=50&maxprice=10000&maxmiles=150000'
HEADERS={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.9'}
PICKUPS=[('Toyota','Tacoma'),('Ford','Ranger'),('Chevrolet','Colorado'),('Chevy','Colorado'),('GMC','Canyon'),('Nissan','Frontier'),('Mazda','B')]
EMAIL_TO=os.getenv('AKIRA_CAR_SEARCH_EMAIL_TO','roger.gregory@xerox.com')
EMAIL_FROM=os.getenv('AKIRA_CAR_SEARCH_EMAIL_FROM','rtgregory@gmail.com')
EMAIL_DISABLED=os.getenv('AKIRA_CAR_SEARCH_EMAIL_DISABLED','').lower() in {'1','true','yes'}

def fetch(url):
    req=urllib.request.Request(url,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=40) as r:
        return r.read().decode('utf-8','replace')

def clean(s):
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s or ''))).strip()

def as_int(s):
    if s is None: return None
    m=re.search(r'\d[\d,]*',str(s))
    return int(m.group(0).replace(',','')) if m else None

def parse_year_make_model(title):
    year=as_int(re.search(r'\b(19\d{2}|20\d{2})\b',title).group(1)) if re.search(r'\b(19\d{2}|20\d{2})\b',title) else None
    makes=['Toyota','Honda','Ford','Chevrolet','Chevy','GMC','Nissan','Mazda','Scion','Hyundai','Kia','Subaru','Dodge','Jeep','Buick','Lincoln','Mercury','Cadillac','Mitsubishi','Ram']
    make=None
    for mk in makes:
        if re.search(r'\b'+re.escape(mk)+r'\b',title,re.I): make=mk; break
    model=None
    if make:
        rest=re.split(re.escape(make),title,flags=re.I,maxsplit=1)[-1].strip(' -')
        if rest: model=rest.split()[0].strip(' ,-/')
    return year,make,model

def mileage_from_text(text):
    pats=[r'\b(\d{2,3},\d{3})\s*(?:mi|miles|mile|k miles)', r'\b(\d{2,3})k\s*(?:mi|miles)?\b', r'\bmileage\D{0,20}(\d{2,3},?\d{3})\b', r'\bodometer\D{0,20}(\d{2,3},?\d{3})\b']
    for pat in pats:
        m=re.search(pat,text,re.I)
        if m:
            val=m.group(1)
            if val.isdigit() and len(val)<=3 and 'k' in m.group(0).lower(): return int(val)*1000
            n=as_int(val)
            if n and n>1000: return n
    return None

def parse_cl_static(page):
    rows=[]
    pat=re.compile(r'<li class="cl-static-search-result" title="(.*?)">\s*<a href="(.*?)">(.*?)</a>\s*</li>',re.S)
    for m in pat.finditer(page):
        title=html.unescape(m.group(1)); url=html.unescape(m.group(2)); body=m.group(3)
        pm=re.search(r'<div class="price">\$([\d,]+)</div>',body)
        lm=re.search(r'<div class="location">\s*(.*?)\s*</div>',body,re.S)
        price=as_int(pm.group(1)) if pm else None
        loc=clean(lm.group(1)) if lm else None
        rows.append({'title':title,'url':url,'price':price,'location':loc})
    return rows

def wanted(row):
    t=row['title'].lower(); p=row.get('price') or 999999
    if any(x in t for x in ['toyota','honda','tacoma','ranger','colorado','canyon','frontier']): return True
    if 'mazda b' in t or 'b-series' in t: return True
    if p<=3500: return True
    return False

def detail(row):
    text=fetch(row['url'])
    title=clean(re.search(r'<span id="titletextonly">(.*?)</span>',text,re.S).group(1)) if re.search(r'<span id="titletextonly">(.*?)</span>',text,re.S) else row['title']
    price=as_int(re.search(r'<span class="price">\$([\d,]+)</span>',text).group(1)) if re.search(r'<span class="price">\$([\d,]+)</span>',text) else row['price']
    body=clean(re.search(r'<section id="postingbody">(.*?)</section>',text,re.S).group(1)) if re.search(r'<section id="postingbody">(.*?)</section>',text,re.S) else ''
    attrs=' '.join(clean(x) for x in re.findall(r'<p class="attrgroup">(.*?)</p>',text,re.S))
    loc=row.get('location')
    # map blurb often has title location
    if not loc:
        lm=re.search(r'<small>(.*?)</small>',text,re.S)
        if lm: loc=clean(lm.group(1))
    mileage=mileage_from_text(' '.join([title,attrs,body]))
    year,make,model=parse_year_make_model(title)
    is_pick= any(mk.lower() in title.lower() and md.lower() in title.lower() for mk,md in PICKUPS)
    title_status='clean' if re.search(r'clean title',body+' '+attrs,re.I) else 'unknown'
    return {**row,'title':title,'price':price,'location':loc,'body':body,'attrs':attrs,'mileage':mileage,'year':year,'make':make,'model':model,'is_small_pickup':is_pick,'title_status':title_status}

def make_listing(r):
    notes=[]
    if r.get('mileage') is None: notes.append('Mileage not visible in observed Craigslist title/body; odometer not shown in captured listing text.')
    else: notes.append(f"Visible mileage parsed as {r['mileage']:,} miles.")
    body=(r.get('body') or '')[:500]
    if body: notes.append('Observed body snippet: '+body)
    reason=[]
    mk=(r.get('make') or '').lower(); price=r.get('price'); mil=r.get('mileage')
    if mk=='toyota': reason.append('Toyota preference')
    elif mk=='honda': reason.append('Honda preference')
    if r.get('is_small_pickup'): reason.append('small/midsize pickup preference')
    if price is not None: reason.append('under $10,000')
    if mil is not None: reason.append('under 150,000 visible miles')
    else: reason.append('mileage not visible')
    return {'source':'Craigslist Hampton Roads','url':r['url'],'vehicle':r['title'],'year':r.get('year'),'make':r.get('make'),'model':r.get('model'),'trim':None,'price':r.get('price'),'mileage':r.get('mileage'),'location':r.get('location'),'distance_miles':None,'dealer':'unknown Craigslist seller','vin':None,'title_status':r.get('title_status'),'notes':' '.join(notes),'is_small_pickup':bool(r.get('is_small_pickup')),'match_reason':'; '.join(reason)}

def score(item):
    mk=(item.get('make') or '').lower(); sc={'toyota':100,'honda':86}.get(mk,72 if item.get('is_small_pickup') else 20)
    if item.get('price') and item['price']<=7000: sc+=10
    if item.get('mileage') and item['mileage']<=90000: sc+=15
    elif item.get('mileage') and item['mileage']<=120000: sc+=8
    if item.get('year') and item['year']>=2010: sc+=5
    return -sc

def render_dashboard(listings, source_notes, counts, report_path, json_path):
    vault_root=ROOT.parents[1]
    dash_dir=vault_root/'daily'; dash_dir.mkdir(exist_ok=True)
    dash_path=dash_dir/'car_search.html'
    def esc(x): return html.escape('' if x is None else str(x), quote=True)
    def money(x): return '—' if x is None else f"${int(x):,}"
    def miles(x): return '<span class="reliability reliability-bad">unknown</span>' if x is None else f"{int(x):,}"
    def reliability(l):
        status=(l.get('maintenance_reliability') or 'neutral').lower()
        label=status if status in {'bad','neutral','good'} else 'neutral'
        if label == 'good':
            return f'<span class="reliability reliability-{esc(label)}">{esc(label)}</span>'
        if label == 'neutral':
            return f'<span class="reliability reliability-{esc(label)}">{esc(label)}</span>'
        reason=l.get('maintenance_reliability_reason') or 'No clear reliability trend observed.'
        return f'<span class="reliability reliability-{esc(label)}">{esc(label)}</span><div class="why">{esc(reason)}</div>'
    total=len(listings); toyotas=sum(1 for x in listings if (x.get('make') or '').lower()=='toyota'); hondas=sum(1 for x in listings if (x.get('make') or '').lower()=='honda'); pickups=sum(1 for x in listings if x.get('is_small_pickup'))
    rows=[]
    for i,l in enumerate(listings[:30],1):
        make=(l.get('make') or '').lower(); is_pickup='true' if l.get('is_small_pickup') else 'false'
        rows.append(f"""<tr data-make=\"{esc(make)}\" data-pickup=\"{is_pickup}\"><td>{i}</td><td><a href=\"{esc(l.get('url'))}\">{esc(l.get('vehicle'))}</a><div class=\"why\">{esc(l.get('match_reason'))}</div></td><td>{esc(l.get('year'))}</td><td>{money(l.get('price'))}</td><td>{miles(l.get('mileage'))}</td><td>{reliability(l)}</td></tr>""")
    html_doc=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Car Search Dashboard</title>
<style>
:root{{--bg:#f8fafc;--panel:#ffffff;--muted:#64748b;--text:#0f172a;--accent:#0284c7;--good:#16a34a;--warn:#d97706;--line:#cbd5e1}}*{{box-sizing:border-box}}body{{margin:0;background:linear-gradient(135deg,#f8fafc,#e0f2fe);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}}main{{max-width:1180px;margin:0 auto;padding:28px}}a{{color:#0369a1}}.top{{display:flex;justify-content:space-between;gap:16px;align-items:end;flex-wrap:wrap}}h1{{margin:.2rem 0;font-size:2rem}}.sub{{color:var(--muted)}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}}.card,.source{{background:rgba(255,255,255,.94);border:1px solid var(--line);border-radius:16px;padding:16px;box-shadow:0 10px 30px rgba(15,23,42,.08)}}.num{{font-size:2rem;font-weight:800;color:#0f172a}}.label,.source span{{display:block;color:var(--muted);font-size:.85rem}}.table-wrap{{overflow-x:auto;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.96);box-shadow:0 10px 30px rgba(15,23,42,.08)}}table{{width:100%;min-width:640px;border-collapse:collapse}}th,td{{padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left;font-size:.88rem}}th{{color:#075985;background:#f1f5f9;font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}}th[data-sort]::after{{content:' ' attr(data-sort);font-size:.7rem;color:var(--muted)}}tr:hover{{background:#f0f9ff}}.why{{color:var(--muted);font-size:.78rem;margin-top:2px}}.flag,.ok,.reliability{{display:inline-block;border-radius:999px;padding:3px 8px;margin:2px;font-size:.75rem}}.flag{{background:#fef3c7;color:#92400e;border:1px solid #fbbf24}}.ok,.reliability-good{{background:#dcfce7;color:#166534;border:1px solid #86efac}}.reliability-neutral{{background:#e0f2fe;color:#075985;border:1px solid #7dd3fc}}.reliability-bad{{background:#fee2e2;color:#991b1b;border:1px solid #fca5a5}}.sources{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-top:22px}}.source p{{color:var(--muted);font-size:.88rem}}footer{{margin-top:20px;color:var(--muted);font-size:.9rem}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}}.card{{background:rgba(255,255,255,.94);border:1px solid var(--line);border-radius:16px;padding:16px;box-shadow:0 10px 30px rgba(15,23,42,.08);cursor:pointer;text-align:left;font:inherit;color:inherit;transition:transform .12s ease,box-shadow .12s ease,border-color .12s ease}}.card:hover{{transform:translateY(-2px);box-shadow:0 14px 34px rgba(15,23,42,.12)}}.card.active{{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent)}}.num{{font-size:2rem;font-weight:800;color:#0f172a}}.label{{display:block;color:var(--muted);font-size:.85rem}}
</style></head><body><main><div class="top"><div><h1>Used-Car Search Dashboard</h1><div class="sub">Generated {TODAY} · ZIP 23462 · under $10k · under 150k visible miles · active sources only</div></div><div class="sub"><a href="../{esc(str(report_path.relative_to(vault_root)).replace(' ', '%20'))}">Markdown report</a> · <a href="../{esc(str(json_path.relative_to(vault_root)).replace(' ', '%20'))}">JSON data</a></div></div>
<section class="cards" id="car-search-filters"><button type="button" class="card active" data-filter="all"><div class="num">{total}</div><div class="label">verified leads</div></button><button type="button" class="card" data-filter="make:toyota"><div class="num">{toyotas}</div><div class="label">Toyotas</div></button><button type="button" class="card" data-filter="make:honda"><div class="num">{hondas}</div><div class="label">Hondas</div></button><button type="button" class="card" data-filter="pickup"><div class="num">{pickups}</div><div class="label">small/midsize pickups</div></button></section>
<div class="table-wrap"><table id="car-search-table"><thead><tr><th data-key="rank" data-type="num">#</th><th data-key="vehicle" data-type="text">Vehicle</th><th data-key="year" data-type="num">Year</th><th data-key="price" data-type="money">Price/Bid</th><th data-key="mileage" data-type="num">Mileage</th><th data-key="reliability" data-type="text">Reliability</th></tr></thead><tbody>{''.join(rows) if rows else '<tr><td colspan="6">No verified active-source leads today.</td></tr>'}</tbody></table></div>
<script>
(function(){{
  const table = document.getElementById('car-search-table');
  if (!table) return;
  const tbody = table.tBodies[0];
  const headers = Array.from(table.tHead.rows[0].cells);
  const parse = (cell, type) => {{
    const text = cell.textContent.trim();
    if (type === 'num') {{
      const n = text.replace(/[^0-9.-]/g, '');
      return n === '' ? Number.NEGATIVE_INFINITY : Number(n);
    }}
    if (type === 'money') {{
      const n = text.replace(/[^0-9.-]/g, '');
      return n === '' ? Number.POSITIVE_INFINITY : Number(n);
    }}
    return text.toLowerCase();
  }};
  headers.forEach((th, idx) => {{
    th.style.cursor = 'pointer';
    th.title = 'Sort';
    th.addEventListener('click', () => {{
      const type = th.dataset.type || 'text';
      const rows = Array.from(tbody.rows);
      const asc = th.dataset.sort !== 'asc';
      headers.forEach(h => delete h.dataset.sort);
      th.dataset.sort = asc ? 'asc' : 'desc';
      rows.sort((a, b) => {{
        const av = parse(a.cells[idx], type);
        const bv = parse(b.cells[idx], type);
        if (av < bv) return asc ? -1 : 1;
        if (av > bv) return asc ? 1 : -1;
        return 0;
      }});
      tbody.replaceChildren(...rows);
    }});
  }});
  const filterBar = document.getElementById('car-search-filters');
  if (filterBar) {{
    const cards = Array.from(filterBar.querySelectorAll('.card'));
    cards.forEach(card => {{
      card.addEventListener('click', () => {{
        cards.forEach(c => c.classList.remove('active'));
        card.classList.add('active');
        const filter = card.dataset.filter;
        Array.from(tbody.rows).forEach(row => {{
          let show = true;
          if (filter === 'pickup') show = row.dataset.pickup === 'true';
          else if (filter && filter.startsWith('make:')) show = row.dataset.make === filter.slice(5);
          row.style.display = show ? '' : 'none';
        }});
      }});
    }});
  }}
}})();
</script>
<footer>Canonical data remains Markdown/JSON/SQLite in the Akira vault; this dashboard is a convenience view generated at <code>daily/car_search.html</code>.</footer></main></body></html>"""
    dash_path.write_text(html_doc,encoding='utf-8')
    return dash_path

def send_dashboard_email(dash_path, report_path, listing_count, counts):
    if EMAIL_DISABLED:
        return {'status':'disabled','to':EMAIL_TO,'body_html':str(dash_path)}
    if not dash_path.exists():
        raise FileNotFoundError(f'car-search dashboard not found: {dash_path}')
    subject=f'Akira car search dashboard — {TODAY}'
    counts_text=', '.join(f'{source}: {count}' for source,count in sorted(counts.items())) or 'no verified leads'
    text_body=(
        f'This email contains the Akira used-car search dashboard generated for {TODAY}.\n\n'
        f'Verified listings/lots: {listing_count}\n'
        f'Counts by source: {counts_text}\n'
        f'Markdown report: {report_path}\n'
        f'HTML dashboard source file: {dash_path}\n'
    )
    html_body=dash_path.read_text(encoding='utf-8')
    message=(
        f'From: {EMAIL_FROM}\n'
        f'To: {EMAIL_TO}\n'
        f'Subject: {subject}\n\n'
        '<#multipart type=alternative>\n'
        f'{text_body}\n'
        '<#part type=text/html>\n'
        f'{html_body}\n'
        '<#/multipart>\n'
    )
    proc=subprocess.run(['himalaya','template','send'],input=message,text=True,capture_output=True,timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(f'himalaya send failed ({proc.returncode}): {(proc.stderr or proc.stdout).strip()}')
    return {'status':'sent','to':EMAIL_TO,'subject':subject,'body_html':str(dash_path)}

def main():
    data_dir=ROOT/'data'; rep_dir=ROOT/'daily-reports'; data_dir.mkdir(exist_ok=True); rep_dir.mkdir(exist_ok=True)
    source_notes={}
    # AutoTempest page check only: dynamic results not embedded in raw HTML in this stdlib runner.
    try:
        at=fetch(AT_URL); (data_dir/f'{TODAY}-at.html').write_text(at,encoding='utf-8')
        source_notes['AutoTempest']={'note':f'Accessible page shell fetched ({len(at)} chars), but no server-rendered listing titles were embedded for stdlib extraction in this run; no AutoTempest listings were inserted without verified listing rows. Manual fallback link retained.','attempted_url':AT_URL}
    except Exception as e:
        source_notes['AutoTempest']={'note':f'Fetch failed: {type(e).__name__}: {e}','attempted_url':AT_URL}
    listings=[]; excluded=[]
    try:
        cl=fetch(CL_URL); (data_dir/f'{TODAY}-cl.html').write_text(cl,encoding='utf-8')
        rows=parse_cl_static(cl)
        source_notes['Craigslist Hampton Roads']={'note':f'Accessible. Parsed {len(rows)} static search rows from Craigslist; detail pages fetched for Toyota/Honda/small-pickup/very-low-price candidates only.','attempted_url':CL_URL}
        for row in [x for x in rows if wanted(x)][:80]:
            try:
                r=detail(row)
                if r.get('price') is None or r['price']>=10000: continue
                if r.get('mileage') is not None and r['mileage']>=150000:
                    excluded.append(f"{r['title']} (${r.get('price'):,}) excluded: visible mileage {r['mileage']:,} >= 150,000")
                    continue
                listings.append(make_listing(r))
            except Exception as e:
                excluded.append(f"{row['title']} detail fetch/parse failed: {type(e).__name__}: {e}")
    except Exception as e:
        source_notes['Craigslist Hampton Roads']={'note':f'Fetch failed: {type(e).__name__}: {e}','attempted_url':CL_URL}
    # Auction raw files from dedicated scripts
    auc_path=data_dir/f'{TODAY}-auction757-raw.json'; egg_path=data_dir/f'{TODAY}-eggleston-raw.json'
    auc=json.loads(auc_path.read_text()) if auc_path.exists() else {}
    egg=json.loads(egg_path.read_text()) if egg_path.exists() else {}
    auc_lots=[]
    for ex in auc.get('bidwrangler_extractions',[]):
        for lot in ex.get('vehicle_lots') or []:
            amt=lot.get('current_or_sold_amount') or lot.get('start_amount')
            mil=lot.get('mileage')
            if (amt is None or int(amt)<10000) and (mil is None or mil<150000): auc_lots.append((ex,lot))
    source_notes['Auction757 / BidWrangler']={'note':f"Discovered {len(auc.get('auctions_discovered') or [])} Auction757 listing pages; BidWrangler vehicle API returned {sum(len(x.get('vehicle_lots') or []) for x in auc.get('bidwrangler_extractions',[]) if isinstance(x,dict))} vehicle lots, {len(auc_lots)} qualifying under filters.",'attempted_url':'https://auction757.com/upcoming-auctions/'}
    # Include active Auction757 lots if any
    for ex,lot in auc_lots:
        amt=lot.get('current_or_sold_amount') or lot.get('start_amount')
        listings.append({'source':'Auction757 / BidWrangler','url':lot.get('url'),'vehicle':lot.get('name'),'year':lot.get('year'),'make':lot.get('make'),'model':lot.get('model'),'trim':None,'price':amt,'mileage':lot.get('mileage'),'location':'Hampton Roads, VA','distance_miles':None,'dealer':'Auction757 / BidWrangler auction lot','vin':lot.get('vin'),'title_status':'auction paperwork/title risk','notes':f"Auction lot in {ex.get('auction_name')}; status {lot.get('status')}; AS IS/WHERE IS; key fees/title or DMV paperwork risks may apply. Description: {(lot.get('description') or '')[:400]}",'is_small_pickup':False,'match_reason':'Auction lot under numeric filters; verify before bidding'})
    current_egg=[]; stale_egg=[]
    today=dt.date.fromisoformat(TODAY)
    for pdf in egg.get('pdfs') or []:
        ad=pdf.get('auction_date')
        if not ad or dt.date.fromisoformat(ad) < today:
            if pdf.get('vehicle_count'): stale_egg.append(pdf)
            continue
        for v in pdf.get('vehicles') or []:
            mil=v.get('mileage')
            if mil is None or mil<150000: current_egg.append((pdf,v))
    source_notes['Eggleston Automotive']={'note':f"PDF discovery/extraction succeeded. Found {len(egg.get('pdfs') or [])} PDFs; {sum(p.get('vehicle_count') or 0 for p in egg.get('pdfs') or [])} vehicle rows total. No current/future qualifying rows were inserted; {len(stale_egg)} vehicle-list PDF(s) were stale/completed.",'attempted_url':'https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles'}
    for pdf,v in current_egg:
        listings.append({'source':'Eggleston Automotive','url':pdf.get('pdf_url'),'vehicle':v.get('vehicle'),'year':v.get('year'),'make':v.get('make'),'model':v.get('model'),'trim':None,'price':None,'mileage':v.get('mileage'),'location':'Hampton Roads, VA','distance_miles':None,'dealer':'Eggleston Automotive auction','vin':None,'title_status':'auction/disclaimer risk','notes':f"Eggleston auction PDF lot {v.get('lot')} case {v.get('case_number')}; auction date {pdf.get('auction_date')}; list subject to change/verify before bidding. Color {v.get('color')}; mileage text {v.get('mileage_text')}; notes {v.get('notes')}",'is_small_pickup':False,'match_reason':'Eggleston auction candidate under mileage filter; price unknown before auction'})
    # alert state: record none due; no external sending in cron final-response mode
    state_path=data_dir/'auction-alert-state.json'
    state=json.loads(state_path.read_text()) if state_path.exists() else {'alerts_sent':[]}
    due=[]
    for a in auc.get('auctions_discovered') or []:
        ad=a.get('date')
        if ad:
            days=(dt.date.fromisoformat(ad)-today).days
            if days==3: due.append({'source':'Auction757 / BidWrangler','key':f"auction757:{ad}:{a.get('listing_url')}",'date':ad,'title':a.get('title')})
    for pdf in egg.get('pdfs') or []:
        ad=pdf.get('auction_date')
        if ad and (dt.date.fromisoformat(ad)-today).days==3:
            due.append({'source':'Eggleston Automotive','key':f"eggleston:{ad}:{pdf.get('pdf_url')}",'date':ad,'title':pdf.get('label') or 'Eggleston vehicle auction PDF'})
    new_alerts=[]
    sent={x.get('key') for x in state.get('alerts_sent',[]) if isinstance(x,dict)}
    for d in due:
        if d['key'] not in sent:
            d['created_at']=dt.datetime.now().isoformat(timespec='seconds'); state.setdefault('alerts_sent',[]).append(d); new_alerts.append(d)
    if new_alerts: state_path.write_text(json.dumps(state,indent=2)+"\n")
    # De-dupe by url, add maintenance reliability signal, and sort
    uniq={};
    for x in listings: uniq[x['url']]=x
    listings=[enrich_listing(x) for x in uniq.values()]
    listings=sorted(listings,key=score)
    payload={'run_date':TODAY,'source_notes':source_notes,'listings':listings}
    json_path=data_dir/f'{TODAY}-listings.json'; json_path.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding='utf-8')
    # report
    counts={}
    for l in listings: counts[l['source']]=counts.get(l['source'],0)+1
    def money(x): return 'unknown' if x is None else f"${int(x):,}"
    def miles(x): return 'not visible' if x is None else f"{int(x):,}"
    def reliability_text(l):
        q=l.get('maintenance_reliability_query')
        suffix=f" Search: {q}" if q else ''
        return f"{l.get('maintenance_reliability') or 'neutral'} — {l.get('maintenance_reliability_reason') or 'No clear reliability trend observed.'}{suffix}"
    lines=[f'# Used-Car Daily Search — {TODAY}','', '## Date searched and criteria','',f'- Date searched: {TODAY}','- ZIP: 23462','- Radius: 50 miles','- Price/current bid/sold amount: under $10,000 when available','- Mileage: under 150,000 miles when visible','- Active automated sources only: AutoTempest, Craigslist Hampton Roads, Auction757 / BidWrangler, Eggleston Automotive PDFs','', '## Counts by active source','','| Source | Verified listings/lots captured |','|---|---:|']
    for src in ['AutoTempest','Craigslist Hampton Roads','Auction757 / BidWrangler','Eggleston Automotive']:
        lines.append(f'| {src} | {counts.get(src,0)} |')
    lines.append(f'| **Total in today\'s JSON** | **{len(listings)}** |')
    lines += ['', '## Active-source status','','| Source | Status / notes | URL |','|---|---|---|']
    for src,n in source_notes.items(): lines.append(f"| {src} | {n['note']} | <{n['attempted_url']}> |")
    lines += ['', '## Top ranked verified matches','','| Rank | Source | Vehicle | Year | Price/current bid | Mileage | Reliability | Location | Why it fits | Link |','|---:|---|---|---:|---:|---:|---|---|---|---|']
    for i,l in enumerate(listings[:15],1):
        lines.append(f"| {i} | {l['source']} | {l.get('vehicle') or ''} | {l.get('year') or ''} | {money(l.get('price'))} | {miles(l.get('mileage'))} | {reliability_text(l)} | {l.get('location') or ''} | {l.get('match_reason') or ''} | [link]({l.get('url')}) |")
    if not listings: lines.append('| — | — | No verified current listings/lots accessible from active sources today. | — | — | — | — | — | — | — |')
    lines += ['', '## Auction-lot section','']
    lines.append(f"- Auction757/BidWrangler: {len(auc_lots)} qualifying active vehicle lots found. Discovered auctions include: " + '; '.join(f"{a.get('title')} ({a.get('date') or 'date unknown'})" for a in (auc.get('auctions_discovered') or [])) + '.')
    if stale_egg:
        for p in stale_egg: lines.append(f"- Eggleston stale/completed vehicle PDF not inserted: {p.get('auction_date')} — {p.get('vehicle_count')} rows — <{p.get('pdf_url')}>. Eggleston lists are subject to change; check before bidding.")
    else: lines.append('- Eggleston: no current/future vehicle-list PDF rows found for insertion.')
    lines += ['', '## Auction alerts','']
    if new_alerts: lines += [f"- Created 3-days-before-auction alert state entry: {a['source']} {a['title']} on {a['date']}" for a in new_alerts]
    else: lines.append('- No 3-days-before-auction alerts were due today. Auction757 known dates were not exactly 3 days out; Eggleston vehicle-list PDF discovered was stale/completed or schedule-only.')
    lines += ['', '## Red flags and exclusions','']
    lines.append('- Mileage-missing Craigslist rows are included only when the listing was otherwise current; manually check odometer before pursuing.')
    lines.append('- Auction rows carry AS IS/WHERE IS, key-fee, title/DMV paperwork, and list-subject-to-change risks.')
    for e in excluded[:25]: lines.append(f'- {e}')
    lines += ['', '## Manual fallback links (active sources only)','',f'- Craigslist Hampton Roads cars+trucks: <{CL_URL}>',f'- AutoTempest: <{AT_URL}>','- Auction757 upcoming auctions: <https://auction757.com/upcoming-auctions/>','- Eggleston Automotive vehicles/PDFs: <https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles>','', '## SQLite / verification','',f'- Raw structured capture: `data/{TODAY}-listings.json`',f'- Daily Markdown report: `daily-reports/{TODAY}.md`','- SQLite ingest and verification commands are shown in the final cron summary.']
    rep_path=rep_dir/f'{TODAY}.md'; rep_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    dash_path=render_dashboard(listings, source_notes, counts, rep_path, json_path)
    email_result=send_dashboard_email(dash_path, rep_path, len(listings), counts)
    print(json.dumps({'json_path':str(json_path),'report_path':str(rep_path),'dashboard_path':str(dash_path),'listing_count':len(listings),'counts':counts,'new_alerts':new_alerts,'email':email_result},indent=2))

if __name__=='__main__':
    main()
