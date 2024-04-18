from loguru import logger
from shutil import copy2

import streamlit as st
hide_img_fs = """
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
"""
st.markdown(hide_img_fs, unsafe_allow_html=True)

st.sidebar.image(image="static/emt-logo.png", use_column_width="always")
st.sidebar.page_link(page="commit_conf.py", label=" Commit Conf 2024", icon="🎤")
st.sidebar.markdown(body="# :spider_web: ¿Qué son los grafos?")
st.sidebar.page_link(page="pages/konigsberg.py", label=" Los puentes de Königsberg", icon="1️⃣")
st.sidebar.page_link(page="pages/networks.py", label=" Redes y grafos", icon="2️⃣")
st.sidebar.page_link(page="pages/properties.py", label=" Propiedades", icon="3️⃣")
st.sidebar.page_link(page="pages/wantmore.py", label=" ¿Quieres saber más?", icon="4️⃣")
st.sidebar.markdown(body="# :bar_chart: ¿Cómo son los datos?")
st.sidebar.page_link(page="pages/eda.py", label=" Análisis exploratorio", icon="1️⃣")
st.sidebar.markdown(body="# :busstop: La red de la EMT de Madrid")
st.sidebar.page_link(page="pages/tools.py", label=" Herramientas", icon="1️⃣")
st.sidebar.page_link(page="pages/net_analysis.py", label=" Análisis de la red", icon="2️⃣")
st.sidebar.markdown(body="# :construction: ¿Qué pasaría si...?")
st.sidebar.page_link(page="pages/collapse.py", label=" Colapsando la red", icon="1️⃣")
st.sidebar.divider()
st.sidebar.page_link(page="pages/bia.py", label=" bIA", icon="🤖")

row = st.columns(spec=2, gap="small")
images = ["./static/wlogo.png", "./static/bravent-blanco.png"]
for col, image in zip(row, images):
    col.image(image=image, use_column_width="auto")
st.title(body="Colapso programado: Simulando desastres en la red de autobuses de Madrid.")
st.caption(body="Commit Conf 2024, 19 de abril 15:45 - 16:30")

row = st.columns(spec=3, gap="small")

row[0].image(image="static/ub.png", use_column_width=True)
row[0].markdown("<p style='text-align: center;'><a href=https://www.linkedin.com/in/david-lopez-martin/ target='_blank'><img src='https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg' width='24' height='24' /></a> David López Martín</p>", 
                unsafe_allow_html=True)
row[0].markdown("<p style='text-align: center;'><small><strong>Junior AI Data Scientist</strong></small></p>", 
                unsafe_allow_html=True)
row[0].markdown("<p style='text-align: center;'><small><i>david.lopezmartin@bravent.net</i></small></p>", 
                unsafe_allow_html=True)
row[-1].image(image="static/ua.png", use_column_width=True)
row[-1].markdown("<p style='text-align: center;'><a href=https://www.linkedin.com/in/estebanmsg/ target='_blank'><img src='https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg' width='24' height='24' /></a> Esteban Sánchez</p>", 
                unsafe_allow_html=True)
row[-1].markdown("<p style='text-align: center;'><small><strong>Lead Data Scientist</strong></small></p>", 
                unsafe_allow_html=True)
row[-1].markdown("<p style='text-align: center;'><small><i>esteban.sanchez@bravent.net</i></small></p>", 
                unsafe_allow_html=True)