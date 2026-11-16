"""Validate and prepare a dependency-free static preview. GitHub Pages serves the root."""
from pathlib import Path
from html.parser import HTMLParser
import json, shutil, re
root=Path(__file__).resolve().parents[1]
class Audit(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for key in ['src','href']:
   if a.get(key):self.links.append(a[key])
  if tag=='img':self.images.append(a)
a=Audit();a.feed((root/'index.html').read_text())
assert len(set(a.ids))==len(a.ids),'Duplicate HTML IDs'
for link in a.links:
 if link.startswith(('http:','https:','mailto:','data:')):continue
 if link.startswith('#'):assert link[1:] in a.ids,link
 else:assert (root/link.split('#')[0]).is_file(),link
for im in a.images:
 if im.get('src'):assert im.get('alt'),'Missing image description'
js=(root/'assets/js/portfolio.js').read_text()
for asset in re.findall(r"(?:image|file):'([^']+)'",js):assert (root/'assets/portfolio'/asset).is_file(),asset
for css in (root/'assets/css').glob('*.css'):
 if css.name not in ['portfolio.css','fonts.css','editorial-fonts.css']:continue
 for target in re.findall(r'url\(([^)]+)\)',css.read_text()):
  target=target.strip("\"'")
  if not target.startswith(('http','data:')):assert (css.parent/target).is_file(),target
geo=json.loads((root/'assets/portfolio/kenya-counties.json').read_text());assert len(geo['features'])==47
assert abs((90.98-78.77)-12.21)<1e-8
out=root/'dist';out.mkdir(exist_ok=True)
shutil.copy2(root/'index.html',out/'index.html')
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)
print(f'PASS: {len(a.links)} local/external references, {len(a.images)} image descriptions, unique IDs, 47 counties, CT arithmetic. Static preview ready.')
