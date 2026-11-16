# Philip Muchemi — research & data science portfolio

Live: https://muchem1.github.io/PhilipWaweru/

A responsive, dependency-free portfolio served by GitHub Pages from the repository root. The design presents project questions, individual contributions, methods, deliverables and interpretation limits.

## Structure

- `index.html`: accessible page content, SEO and structured profile metadata.
- `assets/css/portfolio.css`: visual system, responsive layouts, reduced-motion and print support.
- `assets/css/fonts.css`: locally hosted font declarations (DM Sans, Space Grotesk and Instrument Serif).
- `assets/js/portfolio.js`: six case studies, filters, accessible dialogs, CT scenario comparison and county-map interactions.
- `assets/portfolio/`: compressed project visuals, simplified county geometry, professional CV and downloadable chart data.
- `scripts/build_site.py`: local reference checks and a disposable `dist/` preview.
- `scripts/build_resume.py`: rebuild the two-page résumé (Python + ReportLab + DejaVu Sans).

## Run & verify

```sh
python scripts/build_site.py
node --check assets/js/portfolio.js
python -m http.server 8000
```

Then visit `http://localhost:8000/`. No API keys, analytics trackers, external JavaScript libraries, package installation or build step are required for GitHub Pages. Fonts are served locally. Native `<dialog>` provides keyboard focus containment and Escape-to-close behavior. County navigation uses a single tab stop and arrow keys. Motion respects the system reduced-motion preference.

Project deep links use `#case/ct`, `#case/yellowfever`, `#case/livestock`, `#case/rabies`, `#case/kdhs` and `#case/fires`.

## Evidence and visual provenance

The biography, employment dates, methods and contribution descriptions were checked against Philip's latest November 2026 CVs. Six dashboards and seven manuscripts mean **analytical contributions**, not six sole-authored products or seven published papers. The CT scenario is a modelled analysis, not implementation evidence.

- **CT comparison:** 155 existing sites; a scenario adding 98 sites increases estimated 30-minute coverage from 78.77% to 90.98%. The plotted difference is 12.21 percentage points. `ct-scenario-summary.csv` contains exactly these chart inputs. This is not a new model run.
- **County map:** derived from the supplied `Kenya_counties.gpkg` (47 features, EPSG:4326), simplified for presentation. Colours distinguish county shapes and do not encode disease risk, access or facility counts. The source GeoPackage remains outside the repository.
- **Forest fire / temperature / Westlands maps:** original outputs already present in the portfolio repository, converted to WebP. The original versions remain in `images/`.
- **Livestock dashboard:** earlier working screenshot supplied during the livestock dashboard project. It illustrates the application; it is not a live embed or a claim that every displayed number is the latest result.
- **KDHS:** project description checked against the scholarship CV: R workflows for multi-header survey tables, harmonised Chapters 2/4/5 datasets, CSV/Parquet outputs and Shiny views. The schematic contains no generated survey values.
- **Livestock screenshot gallery:** original October 2026 interface captures for the facility explorer and county overview. The overview is cropped to its introductory/summary panel to avoid blank lower panels; the facility view is resized only. Figures belong to the earlier interface state and are not asserted as current findings.
- **Bayesian and vaccination illustrations:** custom HTML/CSS method diagrams. They contain no invented county risks, facility locations or model evaluation metrics.
- **Power BI image:** the original portfolio professional-survey exercise, labelled as a portfolio exercise in the enlarged view.

The case studies do not expose unpublished source datasets, claim publication status or invent model-performance scores. Public source links point to Philip's existing GitHub and Tableau profiles/projects. The contact address was already public on the previous site.

## Updating content

Edit case-study copy in `assets/js/portfolio.js` and visible summaries in `index.html` together. Replace WebP assets with the same filenames to preserve links. Re-run the validation script after changes. To rebuild the résumé, run `python scripts/build_resume.py` and visually inspect both PDF pages.

Legacy template files remain for history and existing links, but the new homepage loads only the new portfolio stylesheet and script. The original template's license remains in `LICENSE.txt`.


## Editorial revision, November 2026

The second design review replaced the slogan-led dark homepage with an identity-led editorial layout, larger reading sizes, a light paper/green/terracotta palette and a locally hosted serif/sans type system. Two visible flagship projects lead the work, while four complementary projects complete the six-project selection. The facility-list comparison was replaced by the substantive KDHS data-and-dashboard project, including in the professional résumé.

The review prioritised recruiting clarity, visible evidence, distinct analytical capabilities, faithful attribution, responsive reading and restrained movement. The Livestock Master Plan now has two switchable original captures and image enlargement, in addition to the detailed project notes. Native dialogs, keyboard county navigation, reduced-motion support and direct project links remain.
