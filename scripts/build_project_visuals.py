"""Build portfolio SVGs from verified summaries and local aggregate data. No raw records published."""
from pathlib import Path
import csv,json,math,statistics,html
O=Path('assets/portfolio'); summaries={}
def svg(name,title,subtitle,body,foot):
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" role="img"><title>{html.escape(title)}</title><rect width="900" height="520" fill="#1d242c"/><style>text{{font-family:Arial,sans-serif;fill:#ecf0f5}}.muted{{fill:#b4bac2;font-size:14px}}.label{{font-size:17px}}.value{{fill:#9ac7ff;font-size:22px}}.small{{fill:#b4bac2;font-size:12px}}</style><text x="42" y="48" font-size="25">{html.escape(title)}</text><text x="42" y="78" class="muted">{html.escape(subtitle)}</text>{body}<path d="M42 470H858" stroke="#454d5a"/><text x="42" y="495" class="small">{html.escape(foot)}</text></svg>'''
 (O/(name+'.svg')).write_text(s)
# Exact scenario summary, not a new model run.
b=''
for i,(name,v) in enumerate([('Existing CT network',78.77),('With 98 additional sites',90.98)]):
 y=155+i*110;b+=f'<text x="42" y="{y}" class="label">{name}</text><rect x="42" y="{y+20}" width="700" height="28" fill="#384352"/><rect x="42" y="{y+20}" width="{7*v}" height="28" fill="{["#8495ac","#9ac7ff"][i]}"/><text x="770" y="{y+43}" class="value">{v}%</text>'
b+='<text x="42" y="405" font-size="29" fill="#9ac7ff">+12.21 percentage points within 30 minutes</text>'
svg('output-accessibility','Improving geographical access to CT','Estimated population coverage within 30 minutes',b,'Modelled scenario: 155 existing sites; 98 additional sites. Not measured implementation impact.')
# Real local inventory water status; aggregate records only.
source=Path('/workspace/scratch/013b4a835268/cleaned/Water_Point.csv');counts={}
with source.open(encoding='utf-8-sig') as f:
 for r in csv.DictReader(f):
  k=(r.get('Status') or 'Not recorded').strip().title();counts[k]=counts.get(k,0)+1
summaries['livestock_water_status_records']=counts
items=sorted(counts.items(),key=lambda x:-x[1]);maximum=max(counts.values());b=''
for i,(k,n) in enumerate(items[:5]):
 y=130+i*58;b+=f'<text x="42" y="{y}" class="label">{html.escape(k)}</text><rect x="220" y="{y-18}" width="{500*n/maximum}" height="23" fill="#9ac7ff"/><text x="{235+500*n/maximum}" y="{y}" class="label">{n:,}</text>'
svg('output-livestock','Water infrastructure: permanence matters','Status of water-point inventory records in the supplied project dataset',b,'Source: cleaned Water_Point.csv. Record counts, not an estimate of national access or unique facilities.')
# Fitted yellow fever / rabies results are built by build_actual_visuals.py.
b=''
for i in range(125):b+=f'<circle cx="{58+(i%25)*17}" cy="{132+(i//25)*23}" r="4" fill="#9ac7ff"/>'
b+='<text x="55" y="295" font-size="47">125</text><text x="160" y="290" class="label">proposed interventions</text><text x="55" y="330" class="muted">Budget-impact work within a multidisciplinary appraisal process</text><text x="560" y="145" class="label">Population needing care</text><text x="560" y="195" class="label">× expected service use</text><text x="560" y="245" class="label">× cost per service</text><path d="M555 275H830" stroke="#7d8ea6"/><text x="560" y="315" class="value">Budget implications</text><text x="55" y="410" class="muted">Evidence synthesis • burden • equity • costing considerations</text>'
svg('output-hbptap','HBPTAP: evidence behind resource choices','Project scope + illustrative budget-impact logic',b,'125 denotes proposed interventions assessed, not interventions funded. No confidential cost estimates shown.')
# Verified page snapshot retrieved previously; render reporting coverage, not service-quality score.
n=17572;r=12570;no=n-r;summaries['facility_snapshot']={'listed':n,'reporting_at_least_one_indicator':r,'period':'2022-2025'}
b=f'<text x="55" y="163" font-size="55">{r:,}</text><text x="55" y="198" class="label">reported at least one indicator</text><text x="510" y="163" font-size="55">{n:,}</text><text x="510" y="198" class="label">facilities listed in the application</text><rect x="55" y="250" width="780" height="50" fill="#404955"/><rect x="55" y="250" width="{780*r/n}" height="50" fill="#9ac7ff"/><text x="55" y="338" class="label">{r/n*100:.1f}% reporting at least one indicator</text><text x="55" y="392" class="muted">18 KHIS indicators • January 2022–December 2025 • 48 months</text>'
svg('output-facility','Facility performance starts with reporting','Application overview snapshot — counts shown at the time of review',b,'Source: CEMA Facility Performance tool. Any reporting does not imply complete reporting or good performance.')
# Real archived observations: daily mean SHT temperature; sampled days do not imply complete coverage.
by={}
with open('/workspace/scratch/68fc9dbc2c55/afya-review/data/conduit_master_2025_2026.csv') as f:
 for r in csv.DictReader(f):
  try:v=float(r['temp_sht'])
  except (ValueError,TypeError):continue
  if math.isfinite(v):by.setdefault(r['ts'][:10],[]).append(v)
vals=[(d,statistics.mean(v)) for d,v in sorted(by.items())];summaries['afya_daily_mean_temperature']=[{'date':d,'temperature_c':round(v,3)} for d,v in vals]
lo=min(v for _,v in vals)-1;hi=max(v for _,v in vals)+1
points=' '.join(f'{80+i*740/(len(vals)-1):.1f},{395-(v-lo)*260/(hi-lo):.1f}' for i,(_,v) in enumerate(vals))
b=''
for i in range(5):
 v=lo+(hi-lo)*i/4;y=395-i*65;b+=f'<path d="M80 {y}H830" stroke="#384352"/><text x="35" y="{y+5}" class="small">{v:.0f}°C</text>'
b+=f'<polyline points="{points}" fill="none" stroke="#9ac7ff" stroke-width="2"/><text x="80" y="434" class="small">{vals[0][0]}</text><text x="730" y="434" class="small">{vals[-1][0]}</text>'
svg('output-afya','Afya Mazingira: the station behind the decisions','Daily mean SHT air temperature • JKUAT station archive',b,'Historical observations on sampled days, not a live forecast. Station data are not county-wide observations.')
(O/'output-data.json').write_text(json.dumps(summaries,separators=(',',':')))
print('Built five context visuals and source aggregates. Use build_actual_visuals.py for supplied model results.')
