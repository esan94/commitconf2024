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


st.image(image="./static/neglogo.png")
st.markdown("")
st.markdown("")
row = st.columns(spec=3, gap="large")
row[0].markdown("## Misión :dart:")
row[0].markdown("""
<div style="text-align: justify">
<small>En Bravent, nuestra misión es la de proporcionar soluciones tecnológicas innovadoras y personalizadas que impulsen el éxito
de nuestros clientes. Aprovechamos la experiencia de nuestro equipo y la vanguardia de la tecnología para resolver los desafíos
empresariales más complejos.</small>
</div>
""", unsafe_allow_html=True)
row[1].markdown("## Visión :telescope:")
row[1].markdown("""
                <div style="text-align: justify">
                <small> Aspiramos a ser un motor de cambio referente en la industria, anticipando y adoptando las últimas
                tendencias tecnológicas para superar las expectativas de nuestros clientes. </small>
                </div>
                """, unsafe_allow_html=True)
row[2].markdown("## Valores :heart:")
row[2].markdown("\n - Innovación \n - Trabajo en equipo \n - Aprendizaje continuo \n - Excelencia \n - Cultura de bienestar", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown(body="## 🤖 BraventIA")
body_a = (
    "En BraventIA, somos un equipo apasionado de expertos en inteligencia artificial que está "
    "en constante búsqueda de la innovación y el desarrollo tecnológico. Nuestro enfoque se centra en aprovechar"
    " el poder de la IA para transformar y potenciar el panorama empresarial."
)
st.markdown(body=body_a)

body_0 = (
    "Nos destacamos por nuestra dedicación a la excelencia y nuestra capacidad para enfrentar desafíos complejos "
    "con soluciones creativas. Nos esforzamos por entender las necesidades únicas de cada cliente y ofrecer soluciones"
    "personalizadas que impulsen su éxito en un mundo cada vez más digitalizado."
)
st.markdown(body=body_0)


image_urls = [
    "./static/adri.png",
    "./static/carlos.png",
    "./static/david.png",
    "./static/esteban.png",
    "./static/ferjo.png",
    "./static/jose.png",
    "./static/marialu.png",
    "./static/mario.png",
    "./static/salva.png",
    "./static/sergio.png",
    "./static/subu.png",
    "./static/jopa.png"
]

num_columns = 4
num_rows = 3


# Título del grid
st.markdown(body="## 👫 Equipo")
st.markdown("---")

# Tamaño reducido de las imágenes
image_width = 130

# Crear el grid
for i in range(num_rows):
    row = st.columns(num_columns)
    for j in range(num_columns):
        index = i * num_columns + j
        if index < len(image_urls):
            with row[j]:
                st.image(image_urls[index], width=image_width, use_column_width=False)


st.markdown(body="## :telephone_receiver: Contacto")
st.markdown('#### Únete a nosotros: ')
st.write('talentmanagement@bravent.net')
st.markdown('#### ¿Algún proyecto en mente? Innova con nosotros')
st.write('eduardo.garcia@bravent.net')