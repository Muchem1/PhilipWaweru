"""Create web-ready figures from supplied analytical outputs.
Usage: python scripts/build_actual_visuals.py /path/to/extracted/project_sources
Only aggregate figures and county summaries are published.
"""
from pathlib import Path
import sys,csv,json,re,html
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]; O=ROOT/'assets/portfolio'
S=Path(sys.argv[1])
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def svg(name,title,subtitle,body,foot):
 (O/f'{name}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" role="img"><title>{html.escape(title)}</title><desc>{html.escape(subtitle+' '+foot)}</desc><rect width="900" height="520" fill="#1d242c"/><style>text{{font-family:Arial,sans-serif;fill:#ecf0f5}}.muted{{fill:#b4bac2;font-size:14px}}.label{{font-size:17px}}.value{{fill:#9ac7ff;font-size:25px}}.small{{fill:#b4bac2;font-size:12px}}</style><text x="42" y="48" font-size="25">{html.escape(title)}</text><text x="42" y="78" class="muted">{html.escape(subtitle)}</text>{body}<path d="M42 470H858" stroke="#454d5a"/><text x="42" y="495" class="small">{html.escape(foot)}</text></svg>''')
def webp(src,name):
 im=Image.open(S/src).convert('RGB');im.thumbnail((1800,1800));im.save(O/name,'WEBP',quality=90,method=6)
# Preserve original figures with their legends. No patient location graphics.
for src,name in [
 ('Brazil/outputs/travel_time_distribution_walking.png','brazil-walking.webp'),
 ('Brazil/outputs/travel_time_distribution_motorized.png','brazil-motorized.webp'),
 ('manuscript_occurence/risk_map_manuscript_occurence.png','yellow-fever-risk.webp'),
 ('manuscript_occurence/credible_interval_width_map_manuscript_occurence.png','yellow-fever-uncertainty.webp'),
 ('manuscript_occurence/posterior_covariate_effects_manuscript_occurence.png','yellow-fever-effects.webp'),
 ('outputs_00/paper 3 outputs/bar_chart_county_coverage_1km_vs_3km.png','rabies-county-comparison.webp'),
 ('outputs_00/paper 3 outputs/map_county_coverage_class_3km.png','rabies-coverage.webp'),
 ('outputs/all services/oncology_services/accessibility_maps_facet.png','oncology-access-maps.webp')]:webp(src,name)
# Brazil: values transcribed from the two supplied aggregate plots.
b=''
for i,label in enumerate(['0–29','30–59','60–119','120–179','180+']):
 x=98+i*155
 for j,(val,col) in enumerate(zip(([5,5,35,10,45][i],[85,5,5,0,5][i]),['#8896aa','#9ac7ff'])):
  h=val*3.0;bx=x+j*43;b+=f'<rect x="{bx}" y="{380-h}" width="34" height="{h}" fill="{col}"/><text x="{bx+17}" y="{369-h}" text-anchor="middle" class="small">{val}%</text>'
 b+=f'<text x="{x+38}" y="410" text-anchor="middle" class="label">{label}</text>'
b+='<rect x="535" y="95" width="12" height="12" fill="#8896aa"/><text x="556" y="106" class="small">Walking</text><rect x="655" y="95" width="12" height="12" fill="#9ac7ff"/><text x="676" y="106" class="small">Motorised</text><text x="450" y="445" text-anchor="middle" class="muted">Modelled journey time (minutes) · share of analysed records</text>'
svg('output-brazil','The same hospital. Very different journeys.','Hospital Pequeno Príncipe, Curitiba · 20-record study',b,'Source: supplied walking / motorised output plots. Postal-code-based estimates; not observed journeys.')
# Fitted county posterior probabilities, joined to portfolio county boundaries.
yf=rows(S/'manuscript_occurence/posterior_predictions_manuscript_occurence.csv');norm=lambda s:re.sub('[^a-z]','',s.lower());look={norm(r['county']):r for r in yf}
g=json.loads((O/'kenya-counties.json').read_text());pts=[p for f in g['features'] for poly in f['geometry']['coordinates'] for ring in poly for p in ring];xmin=min(p[0] for p in pts);xmax=max(p[0] for p in pts);ymin=min(p[1] for p in pts);ymax=max(p[1] for p in pts);scale=min(360/(xmax-xmin),340/(ymax-ymin));b=''
colors=['#40536d','#8090a6','#b0c4df','#f0cf78']
for f in g['features']:
 r=look[norm(f['properties']['name'])];v=float(r['posterior_probability']);d=' '.join(' '.join(('M' if j==0 else 'L')+f'{100+(p[0]-xmin)*scale:.2f},{110+(ymax-p[1])*scale:.2f}' for j,p in enumerate(ring))+'Z' for poly in f['geometry']['coordinates'] for ring in poly);b+=f'<path d="{d}" fill="{colors[min(int(v*4),3)]}" stroke="#1d242c" stroke-width=".7"><title>{html.escape(r["county"])}: {v:.3f}</title></path>'
b+='<text x="500" y="155" font-size="45">47 counties</text><text x="500" y="188" class="muted">Fitted posterior occurrence probability</text>'
for i,(col,label) in enumerate(zip(colors,['Below 0.25','0.25 to below 0.50','0.50 to below 0.75','0.75 and above'])):
 y=240+i*43;b+=f'<rect x="500" y="{y-16}" width="25" height="20" fill="{col}"/><text x="542" y="{y}" class="label">{label}</text>'
svg('output-yellowfever','Yellow fever: the geography of occurrence','Kenya · Bayesian spatial logistic model · BYM2 / R-INLA',b,'Source: manuscript_occurence posterior output. Recorded occurrence, not individual infection risk.')
# Rabies: population-weighted national potential coverage from 47 county rows.
vals=[]
for km in [1,3]:
 rr=rows(S/f'outputs_00/paper 3 outputs/{km}km_county_population_coverage.csv');v=100*sum(float(x['covered_dog_population']) for x in rr)/sum(float(x['total_dog_population']) for x in rr);vals.append(v)
b=''
for i,v in enumerate(vals):
 y=165+i*115;b+=f'<text x="42" y="{y}" class="label">{[1,3][i]} km school catchments</text><rect x="42" y="{y+20}" width="700" height="30" fill="#384352"/><rect x="42" y="{y+20}" width="{7*v}" height="30" fill="{["#8896aa","#9ac7ff"][i]}"/><text x="765" y="{y+44}" class="value">{v:.1f}%</text>'
b+='<text x="42" y="410" class="label">Wider catchments change who could be reached.</text>'
svg('output-rabies','Planning dog-vaccination catchments','Estimated dog population inside school buffers · national aggregation',b,'Source: 47 county coverage outputs. Potential geographical coverage, not vaccination uptake.')
# HTA: retain the exact source denominator and <120-minute threshold.
rr=[rows(S/f'outputs/all services/oncology_services/{f}_national.csv')[0] for f in ['available','available_and_100pct_ready']];b=''
for i,r in enumerate(rr):
 v=float(r['pct_of_national_population']);y=160+i*110;b+=f'<text x="42" y="{y}" class="label">{["Service available","Available + 100% readiness score"][i]} · {r["facility_count"]} facilities</text><rect x="42" y="{y+20}" width="700" height="30" fill="#384352"/><rect x="42" y="{y+20}" width="{7*v}" height="30" fill="{["#8896aa","#9ac7ff"][i]}"/><text x="765" y="{y+44}" class="value">{v:.1f}%</text>'
b+='<text x="42" y="405" class="label">Service availability and measured readiness tell different stories.</text>'
svg('output-hta-access','Cancer care: proximity is only part of access','Oncology services · population modelled within less than 120 minutes',b,'Source: oncology national outputs. Readiness uses the project score; not a clinical quality assessment.')
# Public aggregate provenance, no individual or facility records.
manifest={'brazil':{'sample_records':20,'walking_pct':[5,5,35,10,45],'motorised_pct':[85,5,5,0,5],'source':'Supplied travel_time_distribution figures; transcribed percentages'},'rabies':{'buffer_km':[1,3],'national_potential_dog_population_coverage_pct':vals,'source':'paper 3 outputs county population coverage CSVs'},'oncology':rr,'yellow_fever':{'counties':len(yf),'source':'posterior_predictions_manuscript_occurence.csv','scenario':'manuscript_occurence'}}
(O/'actual-output-provenance.json').write_text(json.dumps(manifest,indent=2))
print('Built four aggregate result visuals and eight original figures.')
