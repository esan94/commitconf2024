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
st.markdown(body="## :two: Redes y grafos")

body_a = (
    "Imagina un mapa del metro con sus estaciones y las líneas que las conectan. Ahora, piensa en este mapa como una red, una estructura que nos ayuda a "
    "visualizar y entender cómo diferentes cosas están conectadas entre sí. En matemáticas y ciencia de la computación, esta red se llama un \"grafo\"."
)
st.markdown(body=body_a)
st.image(image="static/metro.png", caption="Fig 1: Mapa del metro de Madrid.", use_column_width="auto")
rows = st.columns(spec=2, gap="small")
rows[0].image("static/mermaid.png", use_column_width="auto", caption="Fig 2: Representación básica de un grafo.")
body_b = (
    "La figura 2, es una representación mucho más sencilla de un grafo. De donde se pueden ver sus dos propiedades más interesantes:\n\n"
    "- **Nodos**: Los rectángulos A, B, C y D. Pueden representar cualquier cosa, pueden ser personas, ordenadores, páginas web, torres eléctricas o estaciones de metro, entre otras cosas."
)
rows[1].markdown(body=body_b)
body_c = (
    "- **Aristas**: Son las conexiones entre los nodos del grafo. En grafo de personas pueden ser que \"tiene amistad con\", en un grafo de "
    "páginas web pueden ser links a otras webs, o en un grafo de actrices y actores de cine pueden ser las películas en las que han trabajado "
    "juntos. En definitiva cualquier conexión que se pueda establecer entre los nodos del grafo."
)
st.markdown(body=body_c)
st.markdown(body="### Tipos de grafos")
body_d = (
    "- **Unidireccional**: Imagina una calle de un solo sentido. La conexión solo va en una dirección. En un grafo unidireccional, una arista va de un nodo a otro, pero no al revés.\n"
    "- **Bidireccional**: Como una calle de doble sentido. Aquí, las aristas permiten el movimiento en ambas direcciones entre dos nodos.\n"
    "- **Con peso** o ***Weighted***: Aquí, las aristas tienen un \"peso\" o valor. Esto es útil, por ejemplo, en mapas donde las "
    "aristas podrían representar la distancia o el tiempo entre dos puntos. O en un grafo sobre la red eléctrica, el peso puede ser el cantidad de energía "
    "entre nodo y nodo."
)
st.markdown(body=body_d)
st.markdown(body="### Estructuras de red")
body_e = (
    "- **Red aleatoria (*Random Network*)**: Como su nombre indica, en estas redes los nodos se conectan al azar. Es como si hicieras amigos de manera completamente aleatoria.\n"
    "- **Red Libre de Escala (*Scale-Free Network*)**: Algunos nodos, que se agrupan en los llamados \"hubs\" tienen muchas más conexiones que otros. Piensa en una red social donde algunas celebridades tienen millones de seguidores.\n\n"
    "Esto son dos tipos de estructura que son importantes, sin embargo hay más, que no son el objetivo de esta charla."
)
st.markdown(body=body_e)
st.markdown(body="### Resumen")
body_f = (
    "Los grafos son herramientas poderosas que nos ayudan a visualizar y entender las complejas redes que forman parte de nuestra vida "
    "cotidiana. Desde la forma en que navegamos en internet hasta cómo interactuamos en nuestras comunidades, los grafos ofrecen una forma de "
    "mapear y analizar estas conexiones intrincadas."
)
st.markdown(body=body_f)
