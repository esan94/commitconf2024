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
st.markdown(body="## :one: Los puentes de Köninsberg")
body_a = (
    "La **ciencia de las redes o grafos** es un campo fascinante y fundamental en las matemáticas y la informática. Este, tiene un punto inicial peculiar, dado que se originó a partir de un problema real y "
    "aparentemente simple: **el Problema de los Puentes de Königsberg**. \n\n"
    "Este problema, planteado en el siglo XVIII, se centraba en que la ciudad de Königsberg estaba"
    "dividida por el río Pregel y conectada por siete puentes. De ahí que naciera la pregunta ¿una persona puede cruzar cada puente exactamente una vez "
    "y volver al punto de partida?. No fue hasta 1736 cuando Leonhard Euler, probó que era imposible, sentando las bases de la teoría de grafos."
)
st.markdown(body=body_a)
st.image(image="static/koninsber.png", 
         caption="Fig 1: Imagen pictórica de la ciudad de Königsberg. Donde se puede apreciar los trozos de tierra A, B, C, D y los 7 puentes que los unen.", 
         use_column_width="always")
body_b = (
    "La solución de Euler se basaba en que para que tal camino existiera, cada porción de tierra de la ciudad debía tener un número par de puentes "
    "(excepto posiblemente el punto de inicio y final). En el caso de Königsberg, cada una de las cuatro áreas de tierra tenía un número impar de puentes, "
    "por lo que encontrar un trayecto que satisfaga la pregunta era imposible."
)
st.markdown(body=body_b)
st.image(image="static/koninsber2.png", 
         caption="Fig 2: Problema de la ciudad de Königsberg representado como un grafo.", 
         use_column_width="always"
         )
body_c = (
    "Gracias a esto, ahora sabemos que:\n"
    "- Los problemas son más sencillos si se representan como grafos.\n"
    "- Los caminos son una propiedad del grafo, y estos tienen propiedades en su estructura que limitan o mejoran ciertos comportamientos."
)
st.markdown(body=body_c)
body_d = (
    "La solución de Euler no solo resolvió el problema sino que también introdujo el concepto de grafos, estructuras compuestas por nodos y aristas que los conectan. "
    "Este concepto es versátil, sencillo y se ha convertido en una herramienta indispensable en varias áreas: \n"
    "- **Modelado de Redes**: En informática y telecomunicaciones, los grafos se utilizan para modelar redes de comunicación, "
    "donde los nodos representan terminales y las aristas representan conexiones. Este modelado es fundamental para el diseño y análisis de redes, "
    "como internet y redes sociales"
    "- **Optimización de Rutas**: En logística y transporte, la teoría de grafos se aplica para optimizar rutas. Algoritmos como el de *Dijkstra* permiten "
    "encontrar el camino más corto entre dos puntos, una herramienta esencial para sistemas de GPS y la planificación de rutas de entrega."
    "- Biotecnología y Farmacología: Los grafos también juegan un papel clave en la representación de interacciones moleculares y redes metabólicas, "
    "facilitando el descubrimiento de nuevos medicamentos y la comprensión de enfermedades complejas."
    "\n\n"
    "Euler, al resolver el problema de los puentes de Königsberg, no solo abrió la puerta a una nueva rama de las matemáticas sino que también proporcionó "
    "una herramienta poderosa para abordar problemas en el mundo real. Hoy en día, la teoría de grafos continúa evolucionando, encontrando nuevas "
    "aplicaciones en campos tan diversos como la inteligencia artificial, la ecología, la teoría de juegos o las redes epidemiológicas. "
    "Su origen, arraigado en un problema práctico y tangible, sirve como un recordatorio inspirador de cómo las preguntas simples pueden llevar a descubrimientos "
    "profundos y de amplio alcance."
)
st.markdown(body=body_d)