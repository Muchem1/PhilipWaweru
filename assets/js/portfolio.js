'use strict';
const cases = {
  ct: {
    category:'HEALTH SYSTEMS / LOCATION OPTIMISATION', title:'Where should the next CT scanner go?',
    lead:'A national diagnostic-equipment analysis comparing geographical access under alternative facility-placement scenarios. The aim was to make the trade-offs between population coverage, remote communities and investment needs visible.',
    tags:['R','Facility location','Travel-time analysis','Scenario comparison'],
    question:'How could additional CT sites improve access, given the existing network and the distribution of population?',
    role:'At CEMA, I prepared and analysed population, facility and travel-time data, compared placement scenarios, and produced maps and summaries for team discussion. I also examined equipment payback assumptions alongside geographical access.',
    methods:['Combined 5,428 demand locations with a facility network of 919 sites, including 155 existing CT sites in the covering analysis.','Compared covering and location-allocation approaches, including maximal covering, set covering and p-median formulations across project scenarios.','Summarised population coverage in travel-time bands and examined where additional sites changed access.'],
    result:'In one modelled scenario, adding 98 sites increased estimated population coverage within 30 minutes from 78.77% to 90.98%: a gain of 12.21 percentage points.',
    outputs:'Travel-time maps, facility-placement scenarios, population coverage comparisons and payback scenario analysis.',
    caveat:'The figures describe a modelled scenario, not confirmed deployment or measured improvements in healthcare use. Access estimates depend on population, facility and travel-time inputs; payback depends on patient-volume and financial assumptions.'
  },
  yellowfever:{
    category:'EPIDEMIOLOGY / BAYESIAN SPATIAL RESEARCH',title:'Understanding yellow fever risk',
    lead:'County-level yellow fever occurrence modelling in Kenya, combining environmental and demographic evidence with spatial relationships between neighbouring counties.',
    tags:['R-INLA','BYM2','Bayesian logistic regression','Uncertainty'],
    question:'How does the probability of recorded yellow fever occurrence vary geographically, after accounting for covariates and spatial dependence?',
    role:'I harmonised county data, prepared environmental and demographic predictors, constructed adjacency relationships, fitted Bayesian spatial models in R-INLA, and summarised posterior estimates for the research workflow.',
    methods:['Standardised county names and prepared transformed and scaled covariates.','Screened predictors for collinearity and compared model specifications.','Used a binomial likelihood with a logit link and BYM2 spatial effects to represent structured and unstructured county variation.','Summarised posterior occurrence probabilities, covariate effects and 95% credible intervals.'],
    result:'The output is a county-level view of estimated occurrence probability, accompanied by uncertainty rather than a single unqualified risk ranking.',
    outputs:'Posterior probability maps, credible intervals, covariate summaries, adjacency inputs and documented modelling scripts.',
    caveat:'Recorded occurrence is influenced by surveillance and reporting. County-level associations do not establish causation or individual infection risk. The portfolio diagram shows model structure, not fitted county risk values.'
  },
  livestock:{
    category:'DEVELOPMENT / INTERACTIVE RESEARCH SOFTWARE',title:'Infrastructure evidence, made usable',
    lead:'An interactive Shiny dashboard for the Kenya Livestock Master Plan, bringing scattered infrastructure evidence into national and county planning views.',
    tags:['R','Shiny','sf / terra','Accessibility','Downloadable reports'],
    question:'How can planners explore infrastructure distribution, service access and water dependence without navigating separate datasets and analytical scripts?',
    role:'I built the dashboard and reproducible spatial processing workflow, integrated infrastructure and administrative data, developed accessibility summaries, and created downloadable planning bulletins.',
    methods:['Prepared datasets covering 14 infrastructure types, including markets, veterinary services, processing facilities and water points.','Combined facility locations, boundaries, population demand and motorised travel-time analysis.','Built national and county filters, infrastructure attribute summaries, seasonal/permanent water comparisons and 60-minute access indicators.','Prepared CSV and Parquet outputs and Word/PDF reporting workflows.'],
    result:'A single application connects location, attributes, accessibility and reporting so that infrastructure questions can be explored at national and county scales.',
    outputs:'Interactive Shiny dashboard, maps, comparative charts, reusable datasets and downloadable bulletins.',
    image:'livestock-dashboard.webp', imageAlt:'Earlier working screenshot of the livestock infrastructure dashboard',imageCaption:'An earlier working view of the application; the final workflow includes national and county reporting.',
    caveat:'Accessibility and infrastructure indicators depend on inventory completeness, input dates and travel assumptions. The screenshot is a project artifact, not a live application embedded in this portfolio.'
  },
  rabies:{
    category:'ONE HEALTH / GEOSPATIAL COVERAGE',title:'Finding the gaps in vaccination access',
    lead:'Spatial analysis of school-based dog-vaccination planning, examining the relationship between possible vaccination locations, population distribution and areas outside potential catchments.',
    tags:['R','Population grids','1 km / 3 km buffers','Coverage analysis'],
    question:'Which areas and populations could fall outside the potential catchments of school-based dog-vaccination locations?',
    role:'I combined school points, administrative boundaries and gridded population data, constructed catchments, and produced maps and county summaries of potential coverage gaps.',
    methods:['Prepared and checked school locations and county boundaries.','Constructed 1 km and 3 km buffers and accounted for overlapping catchments when estimating covered areas.','Summarised population inside and outside catchments to compare potential geographical coverage.','Extended access analysis to walking and motorised travel-time scenarios.'],
    result:'Coverage-gap maps and county summaries provide a geographical basis for discussing where additional outreach or alternative delivery arrangements may be needed.',
    outputs:'Catchment maps, potential population coverage summaries and travel-time access layers.',
    caveat:'Geographical catchments represent potential access, not actual vaccination uptake or protection. The buffer illustration is a method diagram, not a mapped vaccination site. Human population inputs alone do not directly measure the number of dogs vaccinated.'
  },
  matching:{
    category:'DATA ENGINEERING / RESEARCH DATA QUALITY',title:'Two facility lists. A clearer picture.',
    lead:'Comparing the Kenya Master Health Facility Registry (KMHFR) and Kenya Health Facility Assessment (KHFA) lists to examine overlap and make data-quality decisions transparent.',
    tags:['R','Record linkage','Deduplication','Audit outputs'],
    question:'Which facilities appear in both lists, and how do name, coordinate and administrative inconsistencies affect the comparison?',
    role:'I developed and revised the matching workflow, cleaned facility identifiers and administrative attributes, generated audit outputs, and produced a presentation-ready comparison dashboard.',
    methods:['Normalised names by removing differences in case, punctuation, accents and spacing.','Compared coordinate-based matching with exact cleaned-name matching as separate analytical approaches.','Checked duplicates, missing attributes, ambiguous candidates and administrative consistency.','Produced matched and unmatched outputs with summaries of how the matching rules affected inclusion.'],
    result:'A reproducible comparison workflow with explicit matching rules and review files, rather than an unexplained overlap total.',
    outputs:'Matched/unmatched CSVs, data-quality tables, candidate audits and a map-based comparison dashboard.',
    image:'facility-matching.webp',imageAlt:'KMHFR and KHFA facility comparison dashboard',imageCaption:'An exact cleaned-name matching run. Totals are specific to the input versions and matching rules shown in this artifact.',
    caveat:'An exact name match is a rule-based candidate match, not conclusive proof of facility identity. Identical names and inconsistent administrative fields require review; totals can change between dataset versions and matching methods.'
  },
  fires:{
    category:'EARTH OBSERVATION / UNDERGRADUATE RESEARCH',title:'Reading a landscape after fire',
    lead:'Evaluation of air pollution from forest fires in Aberdare National Park, integrating multiple satellite sensors to investigate the 2019 and 2023 fire episodes.',
    tags:['Remote sensing','Random forest','Sentinel / Landsat / MODIS','NDVI / NBR / dNBR'],
    question:'What can satellite observations reveal about vegetation change, burn severity and air-pollution patterns associated with forest-fire episodes?',
    role:'For my undergraduate research in 2023, I integrated imagery, prepared vegetation and burn indices, applied random forest modelling, and produced maps of fire impacts and air-pollution patterns.',
    methods:['Combined Sentinel-5P air-pollution observations with Sentinel-2, Landsat and MODIS imagery.','Used NDVI, NBR and dNBR to examine vegetation change and burn severity.','Applied random forest modelling as part of the analysis and interpreted the outputs alongside thematic maps.'],
    result:'A multi-sensor research workflow connecting land-surface change with atmospheric observations, supported by cartographic outputs such as the 2023 fire-severity map.',
    outputs:'Fire-severity and vegetation maps, air-pollution pattern analysis and undergraduate research reporting.',
    image:'aberdare-fire.webp',imageAlt:'Original 2023 Aberdare fire severity map',imageCaption:'Original fire-severity output from the 2023 undergraduate research project.',
    caveat:'Satellite observations have different resolutions, acquisition times and retrieval limitations. The portfolio does not claim a model accuracy score or causal pollution effect without the supporting evaluation results.'
  }
};
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
// Progressive enhancement: content stays visible if the observer is unsupported.
if ('IntersectionObserver' in window) {
  document.documentElement.classList.add('js-ready');
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target);}}),{threshold:.07});
  $$('.reveal').forEach(el=>observer.observe(el));
}
$('#year').textContent=new Date().getFullYear();
const menu=$('.menu-toggle');
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');$('#navigation').classList.toggle('open',open);});
$$('#navigation a').forEach(a=>a.addEventListener('click',()=>{menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');$('#navigation').classList.remove('open');}));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){menu.click();menu.focus();}});
let ticking=false;
addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{const total=document.documentElement.scrollHeight-innerHeight;$('.scroll-progress').style.width=`${total>0?scrollY/total*100:0}%`;ticking=false;});ticking=true;}},{passive:true});
let animation;
$$('[data-scenario]').forEach(button=>button.addEventListener('click',()=>{
  const expanded=button.dataset.scenario==='expanded';
  $$('[data-scenario]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  const target=expanded?90.98:78.77, start=parseFloat($('#coverage-number').textContent);
  $('#coverage-fill').style.width=target+'%';
  $('#scenario-detail').innerHTML=`<span class="status-dot"></span>${expanded?'Expanded · 90.98% within 30 minutes · +12.21 pp':'Baseline · 155 existing sites · 78.77% within 30 minutes'}`;
  cancelAnimationFrame(animation);
  if(reduced.matches){$('#coverage-number').textContent=target.toFixed(2);return;}
  const t=performance.now();
  const frame=now=>{const p=Math.min((now-t)/650,1), eased=1-Math.pow(1-p,3);$('#coverage-number').textContent=(start+(target-start)*eased).toFixed(2);if(p<1)animation=requestAnimationFrame(frame);};
  animation=requestAnimationFrame(frame);
}));
$$('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
  $$('[data-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});
  const filter=button.dataset.filter;
  const featureShown=filter==='all'||filter==='modelling'||filter==='geospatial';
  $('#ct-project').hidden=!featureShown;
  let count=featureShown?1:0;
  $$('.project-card').forEach(card=>{const show=filter==='all'||card.dataset.categories.split(' ').includes(filter);card.hidden=!show;if(show){count++;card.classList.add('is-visible');}});
  $('#filter-status').textContent=`${count} projects shown`;
}));
const dialog=$('#case-dialog');
function renderCase(id){
  const c=cases[id];if(!c)return;
  $('#case-body').innerHTML=`<p class="case-eyebrow">${c.category}</p><h2 id="case-title" tabindex="-1">${c.title}</h2><p class="case-lead">${c.lead}</p><div class="tags">${c.tags.map(t=>`<span>${t}</span>`).join('')}</div><div class="case-detail-grid"><div class="case-detail"><h3>THE QUESTION</h3><p>${c.question}</p></div><div class="case-detail"><h3>MY CONTRIBUTION</h3><p>${c.role}</p></div></div><div class="case-detail"><h3>THE APPROACH</h3><ul>${c.methods.map(m=>`<li>${m}</li>`).join('')}</ul></div><div class="case-result">${c.result}</div><div class="case-detail"><h3>DELIVERABLES</h3><p>${c.outputs}</p></div>${c.image?`<button class="case-asset" data-image="assets/portfolio/${c.image}" data-caption="${c.imageCaption}"><img src="assets/portfolio/${c.image}" alt="${c.imageAlt}"><span>${c.imageCaption} Open full image ↗</span></button>`:''}<p class="case-caveat"><strong>Interpretation:</strong> ${c.caveat}</p><div class="case-links">${id==='ct'?'<a class="text-link" href="assets/portfolio/ct-scenario-summary.csv" download>Download scenario data ↓</a>':''}<a class="text-link" href="mailto:muchemiwaweruu@gmail.com?subject=${encodeURIComponent('Portfolio enquiry: '+c.title)}">Discuss this project ↗</a><a class="text-link" href="assets/portfolio/Philip_Muchemi_CV.pdf" target="_blank" rel="noopener">View résumé ↗</a></div>`;
  if(!dialog.open)dialog.showModal();
  dialog.scrollTop=0;
  $('#case-title').focus({preventScroll:true});
}
function openCase(id){if(!cases[id])return;history.pushState(null,'',`#case/${id}`);renderCase(id);}
document.addEventListener('click',event=>{
  const button=event.target.closest('[data-case],[data-open-case]');
  if(button){event.preventDefault();openCase(button.dataset.case||button.dataset.openCase);}
  const image=event.target.closest('[data-image]');
  if(image){$('#lightbox-image').src=image.dataset.image;$('#lightbox-image').alt=image.dataset.caption;$('#image-caption').textContent=image.dataset.caption;$('#image-dialog').showModal();}
});
$$('dialog').forEach(d=>{
  d.querySelector('.dialog-close').addEventListener('click',()=>d.close());
  d.addEventListener('click',event=>{if(event.target===d){const r=d.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)d.close();}});
});
dialog.addEventListener('close',()=>{if(location.hash.startsWith('#case/'))history.replaceState(null,'','#work');});
function syncCase(){const id=location.hash.match(/^#case\/(\w+)$/)?.[1];if(id&&cases[id])renderCase(id);else if(dialog.open)dialog.close();}
addEventListener('hashchange',syncCase);addEventListener('popstate',syncCase);syncCase();
async function loadMap(){
  const svg=$('#kenya-map'), readout=$('#county-readout');
  try{
    const response=await fetch('assets/portfolio/kenya-counties.json');if(!response.ok)throw new Error('Map unavailable');
    const data=await response.json();
    const pts=data.features.flatMap(f=>f.geometry.coordinates.flatMap(p=>p.flat()));
    const xs=pts.map(p=>p[0]),ys=pts.map(p=>p[1]);const x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
    const scale=Math.min(450/(x1-x0),510/(y1-y0));const ox=(560-(x1-x0)*scale)/2,oy=45;
    svg.setAttribute('role','group');svg.setAttribute('aria-label','Kenya county boundaries. Use arrow keys to explore county names. Colours distinguish boundaries, not risk levels.');
    data.features.forEach((f,i)=>{
      const path=document.createElementNS('http://www.w3.org/2000/svg','path');
      const d=f.geometry.coordinates.map(p=>p.map(ring=>ring.map((p,j)=>`${j?'L':'M'}${((p[0]-x0)*scale+ox).toFixed(1)},${((y1-p[1])*scale+oy).toFixed(1)}`).join('')+'Z').join('')).join('');
      path.setAttribute('d',d);path.setAttribute('class','county');path.setAttribute('tabindex',i===0?'0':'-1');path.setAttribute('role','button');path.setAttribute('aria-label',`${f.properties.name} County`);
      const title=document.createElementNS('http://www.w3.org/2000/svg','title');title.textContent=f.properties.name+' County';path.append(title);
      const highlight=()=>{readout.textContent=f.properties.name+' County · Kenya';};
      path.addEventListener('mouseenter',highlight);path.addEventListener('focus',highlight);path.addEventListener('click',()=>{svg.querySelectorAll('.county').forEach(p=>p.setAttribute('tabindex','-1'));path.setAttribute('tabindex','0');highlight();path.focus({preventScroll:true});});
      path.addEventListener('keydown',event=>{if(['ArrowRight','ArrowDown','ArrowLeft','ArrowUp','Home','End'].includes(event.key)){event.preventDefault();const delta=event.key==='ArrowRight'||event.key==='ArrowDown'?1:-1;const next=event.key==='Home'?0:event.key==='End'?data.features.length-1:(i+delta+data.features.length)%data.features.length;const paths=svg.querySelectorAll('.county');paths.forEach(p=>p.setAttribute('tabindex','-1'));paths[next].setAttribute('tabindex','0');paths[next].focus({preventScroll:true});}else if(event.key==='Enter'||event.key===' '){event.preventDefault();highlight();}});
      svg.append(path);
    });
    svg.addEventListener('mouseleave',()=>{if(!svg.contains(document.activeElement))readout.textContent='47 counties. One connected picture.';});
  }catch(error){readout.textContent='Research focus: Kenya · 47 counties';svg.setAttribute('aria-label','Map could not load. Research focus: Kenya.');}
}
loadMap();
