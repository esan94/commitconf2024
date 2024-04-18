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

st.title(body=":busstop: La red de la EMT de Madrid")
st.markdown(body="## :one: Herramientas")
st.markdown("### Python")
body_a = (
    "Es un lenguaje de programación de alto nivel, interpretado y con un enfoque en la legibilidad del código. Se utiliza en múltiples áreas, incluyendo desarrollo web, ciencia de datos, inteligencia artificial, y automatización. Su diseño y filosofía enfatizan la simplicidad y la flexibilidad.\n\n"
    "[Documentación](https://docs.python.org/3/)"
)
st.markdown(body=body_a)
st.markdown("### Pandas")
body_a = (
    "Es una biblioteca de Python que proporciona estructuras de datos y herramientas de análisis de datos. Es ampliamente utilizada en tareas de manipulación y análisis de datos debido a su eficiencia y facilidad de uso, especialmente con grandes conjuntos de datos.\n\n"
    "[Documentación](https://pandas.pydata.org/docs/)"
)
st.markdown(body=body_a)
st.markdown("### NetworkX")
body_a = (
    "Es un paquete de Python para la creación, manipulación, y estudio de la estructura, dinámica y funciones de redes complejas. Se utiliza en ciencias de datos para el análisis de redes sociales, redes de comunicación, y mucho más.\n\n"
    "[Documentación](https://networkx.org/)"
)
st.markdown(body=body_a)
st.markdown("### Streamlit")
body_a = (
    "Es un marco (framework) de trabajo para Python que permite a los usuarios crear aplicaciones web para análisis de datos de manera rápida y sencilla. Está diseñado para que los científicos de datos y los ingenieros puedan convertir scripts de análisis de datos en aplicaciones web interactivas sin la necesidad de tener experiencia en desarrollo web.\n\n"
    "[Documentación](https://streamlit.io/)"
)
st.markdown(body=body_a)

st.markdown("### OpenAI")
body_a = (
    "Es una organización de investigación en inteligencia artificial que busca promover y desarrollar IA amigable para beneficio de la humanidad en su conjunto. Proporciona varias APIs para interactuar con modelos de inteligencia artificial avanzados, como GPT-3 y DALL-E.\n\n"
    "[Documentación](https://platform.openai.com/docs/introduction)"
)
st.markdown(body=body_a)