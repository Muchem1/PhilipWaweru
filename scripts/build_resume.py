from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parents[1]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Body',font));pdfmetrics.registerFont(TTFont('Bold',bold))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
styles={
 'name':ParagraphStyle('name',fontName='Bold',fontSize=25,leading=31,textColor=HexColor('#172b1d'),spaceAfter=7),
 'role':ParagraphStyle('role',fontName='Body',fontSize=11,leading=16,textColor=HexColor('#42603b'),spaceAfter=11),
 'contact':ParagraphStyle('contact',fontName='Body',fontSize=8,leading=12,textColor=HexColor('#45534a'),spaceAfter=16),
 'heading':ParagraphStyle('heading',fontName='Bold',fontSize=10,leading=14,textColor=HexColor('#42603b'),spaceBefore=15,spaceAfter=9),
 'sub':ParagraphStyle('sub',fontName='Bold',fontSize=9.5,leading=14,textColor=HexColor('#172b1d'),spaceBefore=8,spaceAfter=5),
 'body':ParagraphStyle('body',fontName='Body',fontSize=9,leading=14,spaceAfter=7,textColor=HexColor('#29372e')),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8,leading=12,textColor=HexColor('#566157'),spaceAfter=7)
}
story=[]
def p(text,style='body'):story.append(Paragraph(text,styles[style]))
def title():
 p('PHILIP MUCHEMI','name');p('Data Science Researcher | Geospatial Analytics | Decision Support','role')
 p('Nairobi, Kenya | +254 798 031 620 | <link href="mailto:muchemiwaweruu@gmail.com">muchemiwaweruu@gmail.com</link><br/><link href="https://muchem1.github.io/PhilipWaweru/">muchem1.github.io/PhilipWaweru/</link> | <link href="https://github.com/Muchem1">github.com/Muchem1</link>','contact')
title()
p('PROFILE','heading')
p('Data Science Research Assistant with a geospatial background, working across public health and development. Combines Bayesian spatial modelling, location optimisation, remote sensing and interactive software to turn complex datasets into evidence for planning. Experience in reproducible data preparation, research communication and multidisciplinary collaboration.')
p('TECHNICAL CAPABILITIES','heading')
for a,b in [
 ('Programming and data','R, Python, SQL, JavaScript; record linkage, deduplication, coordinate checks, administrative harmonisation, CSV and Parquet outputs.'),
 ('Statistical and decision modelling','Bayesian spatial logistic regression; R-INLA and BYM2; facility location analysis using p-median, maximal covering and set covering; random forest modelling in undergraduate research.'),
 ('Geospatial and earth observation','sf, terra, gdistance; QGIS, ArcGIS, Google Earth Engine; raster/vector processing, travel-time and coverage analysis, satellite-derived vegetation and burn indices.'),
 ('Communication and applications','Shiny dashboards, cartography, Power BI, Tableau, downloadable planning bulletins and documented research workflows.')]: p('<b>'+a+':</b> '+b)
p('PROFESSIONAL EXPERIENCE','heading')
p('Centre for Epidemiological Modelling and Analysis (CEMA)','sub')
p('Data Science Research Assistant | November 2024 - present','small')
p('Contributed maps and analytical outputs to six dashboards and seven manuscripts. Prepared reproducible workflows, documented analytical methods and supported interpretation of spatial and statistical evidence.')
p('<b>Diagnostic equipment placement:</b> compared CT-placement scenarios using 5,428 demand locations and a network of 919 facilities, including 155 existing sites in the covering analysis. In one modelled scenario, 98 additional sites raised estimated population coverage within 30 minutes from 78.77% to 90.98%. Produced maps and scenario comparisons; examined equipment payback assumptions.')
p('<b>Kenya Livestock Master Plan:</b> built a Shiny dashboard covering 14 infrastructure types, national and county views, 60-minute accessibility indicators, seasonal water dependence and downloadable Word/PDF bulletins. Prepared reusable CSV and Parquet outputs.')
p('<b>Yellow fever research:</b> prepared county covariates and adjacency data, applied Bayesian spatial logistic modelling in R-INLA with BYM2 effects, and produced posterior occurrence estimates and credible intervals.')
story.append(PageBreak())
p('PHILIP MUCHEMI','name');p('Selected research, experience & education','role')
p('SELECTED ANALYTICAL WORK','heading')
p('Rabies vaccination planning | CEMA','sub')
p('Combined school locations, county boundaries and gridded population data with 1 km and 3 km buffers. Produced maps and county summaries of potential geographical coverage gaps, with walking and motorised access scenarios.')
p('Health facility list comparison | KMHFR and KHFA','sub')
p('Developed R workflows for cleaned-name matching, spatial comparison, deduplication and data-quality checks. Produced matched/unmatched records, review files and a map-based comparison dashboard with transparent matching rules.')
p('Evaluation of Air Pollution from Forest Fires in Aberdare National Park','sub')
p('Undergraduate research | 2023','small')
p('Integrated Sentinel-5P air-pollution observations with Sentinel-2, Landsat and MODIS imagery for the 2019 and 2023 fire episodes. Used NDVI, NBR and dNBR to assess vegetation change and burn severity; applied random forest modelling and produced maps of fire impacts and air-pollution patterns.')
p('OTHER PROFESSIONAL EXPERIENCE','heading')
for name,role,dates,desc in [
 ('Nairobi City County','GIS and Data Intern','January - April 2024','Maintained geodatabases covering infrastructure, land use and demographics. Integrated survey, satellite and administrative records and checked spatial data quality.'),
 ('Kenya Red Cross Society','GIS and Data Analyst - Volunteer','August 2022 - March 2024','Digitised approximately 1,400 buildings in Wajir, Narok and Turkana using OpenStreetMap and JOSM to support disaster preparedness and response.'),
 ('Kenya Agricultural and Livestock Research Organization','GIS Attachee','January - April 2023','Processed satellite imagery and spatial datasets for land suitability, crop monitoring and resource mapping. Prepared thematic maps and documented methods.')]:
 p(name,'sub');p(role+' | '+dates,'small');p(desc)
p('EDUCATION & DEVELOPMENT','heading')
p('<b>BSc Geospatial Information Science</b><br/>Jomo Kenyatta University of Agriculture and Technology | September 2019 - December 2023')
p('Data Analytics Bootcamp | September 2023 - March 2024<br/>Additional professional development: Spatial Data Science, Esri')
p('LANGUAGES','heading');p('English and Swahili')
def footer(canvas,doc):
 canvas.setStrokeColor(HexColor('#bec9b8'));canvas.line(45,38,550,38)
 canvas.setFont('Body',7);canvas.setFillColor(HexColor('#566157'));canvas.drawString(45,25,'PHILIP MUCHEMI | DATA SCIENCE & GEOSPATIAL RESEARCH');canvas.drawRightString(550,25,str(doc.page))
path=ROOT/'assets/portfolio/Philip_Muchemi_CV.pdf'
SimpleDocTemplate(str(path),pagesize=(595.28,841.89),rightMargin=45,leftMargin=45,topMargin=42,bottomMargin=50,title='Philip Muchemi - Data Science and Geospatial Research CV',author='Philip Muchemi').build(story,onFirstPage=footer,onLaterPages=footer)
print(path)
