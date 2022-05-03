#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################


def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="Bulk Leads")

# st.image("https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/balloon_1f388.png", width=100)
st.image(
    "logo.png",
    width=100,
)

st.title("Bulk Lead Finder")

job_title = ''
industry = ''
job_company_name =''
location_country =''

c29, c30, c31 = st.columns([1, 5, 2])

with c30:

    job_title = st.text_input('Job title', '')
    industry = st.selectbox(
     'Industry',
     ('',
 'media production',
 'higher education',
 'financial services',
 'hospitality',
 'real estate',
 'fine art',
 'marketing and advertising',
 'government relations',
 'banking',
 'medical devices',
 'construction',
 'computer software',
 'insurance',
 'staffing and recruiting',
 'information technology and services',
 'motion pictures and film',
 'pharmaceuticals',
 'chemicals',
 'investment management',
 'health, wellness and fitness',
 'food production',
 'aviation & aerospace',
 'restaurants',
 'law practice',
 'facilities services',
 'education management',
 'market research',
 'apparel & fashion',
 'logistics and supply chain',
 'international trade and development',
 'environmental services',
 'farming',
 'accounting',
 'internet',
 'military',
 'consumer goods',
 'government administration',
 'automotive',
 'entertainment',
 'machinery',
 'biotechnology',
 'telecommunications',
 'legal services',
 'primary/secondary education',
 'industrial automation',
 'defense & space',
 'human resources',
 'mining & metals',
 'paper & forest products',
 'architecture & planning',
 'computer games',
 'research',
 'design',
 'warehousing',
 'medical practice',
 'music',
 'consumer electronics',
 'oil & energy',
 'airlines/aviation',
 'non-profit organization management',
 'retail',
 'hospital & health care',
 'mechanical or industrial engineering',
 'public safety',
 'mental health care',
 'religious institutions',
 'wholesale',
 'veterinary',
 'cosmetics',
 'consumer services',
 'writing and editing',
 'public relations and communications',
 'management consulting',
 'public policy',
 'recreational facilities and services',
 'wine and spirits',
 'leisure, travel, & tourism',
 'law enforcement',
 'online media',
 'civil engineering',
 'package/freight delivery',
 'broadcast media',
 'electrical/electronic manufacturing',
 'plastics',
 'commercial real estate',
 'building materials',
 'graphic design',
 'packaging and containers',
 'utilities',
 'information services',
 'semiconductors',
 'wireless',
 'civic & social organization',
 'arts and crafts',
 'security and investigations',
 'photography',
 'e-learning',
 'furniture',
 'transportation/trucking/railroad',
 'computer hardware',
 'import and export',
 'sports',
 'outsourcing/offshoring',
 'supermarkets',
 'publishing',
 'newspapers',
 'fund-raising',
 'professional training & coaching',
 'think tanks',
 'libraries',
 'individual & family services',
 'fishery',
 'renewables & environment',
 'computer & network security',
 'sporting goods',
 'international affairs',
 'events services',
 'translation and localization',
 'museums and institutions',
 'animation',
 'venture capital & private equity',
 'investment banking',
 'program development',
 'computer networking',
 'executive office',
 'dairy',
 'glass, ceramics, & concrete',
 'gambling & casinos',
 'textiles',
 'printing',
 'performing arts',
 'alternative medicine',
 'capital markets',
 'shipbuilding',
 'railroad manufacture',
 'maritime',
 'business supplies and equipment',
 'judiciary',
 'political organization',
 'luxury goods & jewelry',
 'ranching',
 'philanthropy',
 'nanotechnology',
 'tobacco',
 'legislative office',
 'alternative dispute resolution',
 'food & beverages'))
    job_company_name = st.text_input('Company name', '')
    location_country = st.selectbox(
     'Location Country',
     ('',
 'cambodia',
 'canada',
 'united states',
 'bulgaria',
 'turkey',
 'united kingdom',
 'malaysia',
 'india',
 'tunisia',
 'pakistan',
 'niger',
 'denmark',
 'germany',
 'france',
 'new zealand',
 'brazil',
 'egypt',
 'hong kong',
 'chile',
 'australia',
 'colombia',
 'spain',
 'china',
 'venezuela',
 'netherlands',
 'south africa',
 'belgium',
 'italy',
 'norway',
 'japan',
 'bangladesh',
 'argentina',
 'sweden',
 'mexico',
 'romania',
 'taiwan',
 'united arab emirates',
 'philippines',
 'ireland',
 'puerto rico',
 'peru',
 'lithuania',
 'morocco',
 'indonesia',
 'poland',
 'luxembourg',
 'trinidad and tobago',
 'thailand',
 'israel',
 'czechia',
 'libya',
 'ecuador',
 'iraq',
 'singapore',
 'kenya',
 'saudi arabia',
 'greece',
 'tanzania',
 'russia',
 'finland',
 'liechtenstein',
 'switzerland',
 'vietnam',
 'qatar',
 'kazakhstan',
 'panama',
 'slovakia',
 'iran',
 'ukraine',
 'bolivia',
 'jordan',
 'zimbabwe',
 'macedonia',
 'portugal',
 'croatia',
 'mali',
 'mozambique',
 'costa rica',
 'kuwait',
 'sri lanka',
 'burkina faso',
 'mauritius',
 'saint kitts and nevis',
 'south korea',
 'ethiopia',
 'slovenia',
 'haiti',
 'albania',
 'bahamas',
 'latvia',
 'austria',
 'dominican republic',
 'algeria',
 'serbia',
 'malta',
 'ghana',
 'angola',
 'lebanon',
 'nepal',
 'uganda',
 'guatemala',
 'uruguay',
 'nigeria',
 'oman',
 'democratic republic of the congo',
 'jamaica',
 'azerbaijan',
 'cook islands',
 'swaziland',
 'belarus',
 'hungary',
 'cameroon',
 'isle of man',
 'aruba',
 'paraguay',
 'sudan',
 'macau',
 'bahrain',
 'cyprus',
 'senegal',
 'fiji',
 'estonia',
 'nicaragua',
 'seychelles',
 'moldova',
 'uzbekistan',
 'iceland',
 'cayman islands',
 'benin',
 'el salvador',
 'sierra leone',
 'zambia',
 'bosnia and herzegovina',
 'yemen',
 'antigua and barbuda',
 'côte d’ivoire',
 'french polynesia',
 'myanmar',
 'honduras',
 'mongolia',
 'barbados',
 'laos',
 'gabon',
 'montenegro',
 'rwanda',
 'gambia',
 'namibia',
 'armenia',
 'kosovo',
 'afghanistan',
 'bermuda',
 'kiribati',
 'burundi',
 'guam',
 'togo',
 'botswana',
 'martinique',
 'papua new guinea',
 'solomon islands',
 'palau',
 'madagascar',
 'marshall islands',
 'syria',
 'netherlands antilles',
 'saint lucia',
 'guadeloupe',
 'guinea',
 'Åland islands',
 'maldives',
 'somalia',
 'malawi',
 'vanuatu',
 'grenada',
 'monaco',
 'gibraltar',
 'brunei',
 'jersey',
 'liberia',
 'christmas island',
 'kyrgyzstan',
 'tuvalu',
 'cuba',
 'guinea-bissau',
 'republic of the congo',
 'turks and caicos islands',
 'bhutan',
 'lesotho',
 'belize',
 'mauritania',
 'andorra',
 'palestine',
 'timor-leste',
 'new caledonia',
 'djibouti',
 'suriname',
 'cape verde',
 'guyana',
 'eritrea',
 'san marino',
 'anguilla',
 'georgia',
 'british virgin islands',
 'turkmenistan',
 'são tomé and príncipe',
 'chad',
 'comoros',
 'french guiana',
 'micronesia',
 'tajikistan',
 'réunion',
 'greenland',
 'samoa',
 'faroe islands',
 'u.s. virgin islands',
 'svalbard and jan mayen',
 'northern mariana islands',
 'guernsey',
 'equatorial guinea',
 'dominica',
 'saint vincent and the grenadines',
 'norfolk island',
 'tokelau',
 'montserrat',
 'wallis and futuna',
 'curaçao',
 'central african republic',
 'saint helena',
 'pitcairn',
 'american samoa',
 'vatican city',
 'south sudan',
 'tonga',
 'antarctica',
 'mayotte',
 'british indian ocean territory',
 'bouvet island',
 'french southern territories',
 'western sahara',
 'niue',
 'cocos (keeling) islands',
 'falkland islands',
 'nauru',
 'north korea',
 'saint pierre and miquelon',
 'saint barthélemy',
 'caribbean netherlands',
 'heard island and mcdonald islands',
 'saint martin',
 'sint maarten',
 'south georgia and the south sandwich islands'))

with c31:
    env = st.radio(
     "Test environment has fewer records and faster queries",
     ('Test server', 'Production database'))

    if env == 'Test server':
        query = "SELECT * FROM `test` WHERE "
    else:
        query = "SELECT * FROM `linkedin` WHERE "

 
first_condition = True
if job_title:
    if not first_condition : 
        query = query+"AND "
    query = query+"`job_title` LIKE '%%"+job_title+"%%' "    
    first_condition = False
if industry:
    if not first_condition : 
        query = query+"AND "
    query = query+"`industry` = '"+industry+"' "   
    first_condition = False
if job_company_name:
    if not first_condition : 
        query = query+"AND "
    query = query+"`job_company_name` LIKE '%%"+job_company_name+"%%' "  
    first_condition = False
if location_country:
    if not first_condition : 
        query = query+"AND "
    query = query+"`location_country` = '"+location_country+"' " 
    first_condition = False
if first_condition :
    query = query+"0 ;"
else : 
    query = query+";"


#    st.code(query, language='sql')


if c30.button('Find Leads Now'):
    from sqlalchemy import create_engine
    engine = create_engine("mysql+pymysql://dbuser:password@194.163.187.134:3306/linkedindb")
    with st.spinner('Wait for it, this may take few minutes...'):
        df = pd.read_sql_query(query, engine)
    st.success('Done!')            
    del df["index"]
    st.write("Number of Leads found: "+str(len(df)))
#st.markdown("""---""")  
    st.subheader("Leads Search results 👇 ")
#    st.text("")
    st.write(df)
    c31.button = download_button(df, "leads.csv", "Download in CSV",  )
