# Philip Muchemi — data science & research

Live: https://muchem1.github.io/PhilipWaweru/

A responsive, dependency-free portfolio with eleven case studies. The dark navy/blue visual system combines readable project summaries, original research figures, aggregate charts and accessible project dialogs.

## Development

```sh
python scripts/build_site.py
node --check assets/js/portfolio.js
python -m http.server 8000
```

GitHub Pages serves `index.html` and `assets/` directly. The build command validates references, image descriptions, SVG syntax, unique IDs and county geometry, then prepares an ignored `dist/` directory for preview. No credentials, external JavaScript dependencies or build step are required for production.

- `assets/js/portfolio.js`: case studies, native dialogs, filters, CT scenario comparison, screenshot gallery and county navigation.
- `assets/css/portfolio.css`: locally hosted typography, responsive layout, reduced motion and print styles.
- `scripts/build_actual_visuals.py`: build result figures from the four supplied project archives after extraction. Pass the directory containing `Brazil/`, `manuscript_occurence/`, `outputs/` and `outputs_00/`.
- `scripts/build_project_visuals.py`: context charts from earlier verified project sources; requires those local source files. Does not overwrite fitted yellow fever or rabies results.
- `assets/portfolio/actual-output-provenance.json`: aggregate inputs and source labels for the new result charts.

## Projects and evidence

1. **Brazil paediatric care access:** Hospital Pequeno Príncipe, Curitiba. Postal-code geocoding and walking/motorised friction-surface modelling. The public comparison is redrawn from the supplied aggregate plots (20 records); both original distributions are included. This small sample does not represent Brazil or Paraná. Patient points and postal-code records are excluded.
2. **CT placement:** 155 existing sites; the scenario adding 98 sites increases modelled 30-minute population coverage from 78.77% to 90.98%. This is a project scenario, not measured implementation impact.
3. **Kenya Livestock Master Plan:** original working interface captures, live dashboard link and water-point inventory record counts. Earlier screenshot values are not asserted to be current national estimates.
4. **Healthcare accessibility and readiness:** original paired oncology maps and national CSV results. Population within less than 120 minutes is 91.1989% for available services (290 facilities) and 85.0148% for availability plus a 100% readiness score (50 facilities). Source denominators are retained; unclassified population is not reassigned.
5. **Yellow fever:** actual fitted `manuscript_occurence` BYM2 posterior output for 47 counties, original probability and uncertainty maps, and covariate effect intervals. The coloured county map is redrawn from fitted probabilities. Occurrence is not individual infection risk or a forecast.
6. **KDHS:** Chapters 2/4/5 data preparation, harmonised datasets and Shiny exploration; the card is a workflow illustration.
7. **Rabies:** actual county-level estimated dog-population catchment outputs. National potential coverage is population-weighted, approximately 72.8% for 1 km and 95.9% for 3 km school buffers. Original county map and comparison chart included. Potential geographical coverage is not vaccination uptake.
8. **Aberdare fires:** original undergraduate fire-severity map and multi-sensor analysis description.
9. **HBPTAP:** appraisal and budget-impact work covering 125 proposed interventions. Scope dots and budget formula are explicitly illustrative; no financial results are invented.
10. **Facility performance:** CEMA team application, 18 indicators and January 2022–December 2025. Overview counts are a reviewed application snapshot: 17,572 listed, 12,570 with any reporting. Any reporting is not complete reporting or a quality score.
11. **Afya Mazingira:** team platform with a chart reconstructed from archived JKUAT station temperature samples. Historical station observations are distinguished from regional forecasts. Daily means can reflect uneven sampling.

The public repository includes selected figures and aggregate summaries, not the uploaded archives, patient records or full analytical datasets. Project descriptions distinguish individual contributions, team products, modelled outputs and observed results. No publication status, evaluation metric or implementation impact is invented.

## Interaction and accessibility

Project filters announce counts. Native dialogs support focus containment and Escape to close; figures open at full size. Case studies have direct `#case/brazil`, `#case/accessibility`, `#case/yellowfever` and equivalent links. County navigation uses one tab stop and arrow keys. Motion respects reduced-motion preferences. Fonts are served locally and there are no analytics trackers.

Legacy template files and their license remain for existing links and history.
