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
st.sidebar.page_link(page="pages/konigsberg.py", label=" Los puentes de Köninsberg", icon="1️⃣")
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

st.title(body=":spider_web: ¿Qué son los grafos?")
st.markdown(body="## :four: ¿Quieres saber más?")
body_a = (
    "Si te ha llamado la atención el mundo de los grafos y su utilidad, puedes conocer más" 
    " en profundidad la teoría que hay detrás de ellos y su aplicación a través de las "
    "siguientes herramientas."
)
st.markdown(body=body_a)


body_0 = (
    "<h3><a href='https://networkx.org/nx-guides/' style='text-decoration:none; color:inherit;'>NetworkX</a></h3>"
    "Se trata de un sitio web que ofrece materiales educativos desarrollados y seleccionados oficialmente por la "
    "comunidad de NetworkX. El objetivo del repositorio es proporcionar recursos educativos de alta "
    "calidad para aprender sobre el análisis de redes y la teoría de grafos con NetworkX."
)
st.markdown(body_0, unsafe_allow_html=True)
st.write("") 
body_1 = (
"""
Este repositorio incluye:

- Documentación narrativa extensa, como tutoriales.
- Exámenes detallados de algoritmos comunes de grafos y redes, y sus implementaciones en NetworkX.
- Demostraciones o aplicaciones específicas de dominio de NetworkX que resalten las mejores prácticas para el análisis de redes.
"""
)
st.markdown(body=body_1)

body_2 = (
    "https://networkx.org/nx-guides/"
)
st.markdown(body=body_2)
body_3 = (
    "<h3><a href='http://networksciencebook.com/' style='text-decoration:none; color:inherit;'>NetworkScienceBook</a></h3>"
    "Este libro escrito por Albert-László Barabási y trasladado a sitio web explora los principios teóricos y las aplicaciones "
    "prácticas de la ciencia de redes. Se aborda cómo las redes complejas se encuentran en una amplia gama de sistemas naturales y artificiales," 
    "incluyendo redes sociales, sistemas biológicos, infraestructuras de transporte etc."
    )
st.markdown(body_3, unsafe_allow_html=True)
st.write("") 

body_4 = (
    "La obra proporciona una introducción detallada a los conceptos clave de la teoría de grafos y la dinámica de redes, incluyendo medidas de centralidad,"
    " teoría de percolación, y modelos de crecimiento de redes. Además, explora fenómenos emergentes en redes, como la formación de comunidades y la propagación de información."
)
st.markdown(body_4)

st.write("[Network Science - Albert-László Barabási](http://networksciencebook.com/)")
