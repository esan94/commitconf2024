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
st.markdown(body="## :three: Propiedades")
body_a = (
    "Los grafos tienen una serie de propiedades esenciales para analizar y comprender "
    "la estructura y dinámica de las redes. En esta sección veremos alguna de las propiedades de estos que podremos medir en la red de "
    "la EMT."
)
st.markdown(body=body_a)
st.markdown(body="### Nodos y Links")
body_0 = (
    "El número total de nodos o el tamaño de la red se representa como $N$. Mientras que el número total de links, o conexiones se representa como $L$."
)
st.markdown(body=body_0)

st.markdown(body="### Grado")
body_b = (
    "Indica el número de conexiones que tiene un nodo. Es decir, el número de aristas o de interacciones que tiene un nodo. Estas pueden ser salientes o entrantes, lo que "
    "divide la propiedad en grado de entrada y grado de salida. El grado de un nodo se define como $k_i$ donde $i$ representa el nodo en cuestión.\n\n"
    "Si dividimos entre grado de entrada y de salida, tendríamos respectivamente $k_i^{in}$ y $k_i^{out}$ donde se satisface "
    "que $k_i = k_i^{in} + k_i^{out}$.\n\n"
    "Otra propiedad importante es la media de grados, es decir la media de conexiones que tiene la red "
    "que nos da información sobre como de conectados estan los nodos de la red de media, y se calcula "
    "$\langle k\\rangle = \\frac{1}{N} \sum_{i=1}^N k_i = \\frac{2L}{N}$. El término $2L$ viene porque la misma conexión de un nodo la tiene el nodo que conecta. \n\n"
    "La distribución de los grados es una propiedad muy interesante dado que nos indica la cantidad de nodos que tienen una determinada cantidad de conexiones."
)
st.markdown(body=body_b)
st.markdown(body="### Diámetro")
body_c = (
    "El diámetro de un grafo es el camino más largo del grafo, si nos quedamos solo con los caminos más cortos entre dos nodos. A partir "
    "de dicho valor podemos conocer que todos los nodos están conectados por un número igual o menor al diámetro."
)
st.markdown(body=body_c)
st.markdown(body="### Caminos más cortos")
body_d = (
    "Los caminos más cortos son aquellos caminos que unen cada nodo con el menor número de pasos entre ellos. Conocer la distribución de estos y la media, ayuda a saber "
    "cuantos movimientos hay que hacer de media para llegar a otro nodo.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_d)
st.markdown(body="### Centralidad de grado")
body_e = (
    "Mide la importancia de un nodo basándose en cuántas conexiones tiene. Un nodo con alta centralidad de grado es como una persona muy popular en una red social.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_e)
st.markdown(body="### Centralidad de intermediación")
body_f = (
    "Esta métrica identifica los nodos que actúan como puentes en la red. Un nodo con alta centralidad de intermediación tiene un rol crucial en conectar diferentes partes de la red.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_f)
st.markdown(body="### Centralidad de cercanía")
body_g = (
    "Indica qué tan rápido se puede llegar a todos los demás nodos desde un nodo dado. Un nodo con alta centralidad de cercanía está bien posicionado para difundir información rápidamente a través de la red.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_g)
st.markdown(body="### Centralidad propia")
body_g2 = (
    "Indica como de conectado está un nodo a otros nodos importantes de la red. Mide la influencia del nodo en función de qué tan buena situación tiene en la red "
    "y las conexiones que tienen sus conexiones. Una centralidad propia alta indica que dicho nodo está conectado a otros nodo de centralidad propia alta también.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_g2)
st.markdown(body="### Densidad")
body_h = (
    "Indica cómo de conectado está un grafo con respecto al total de conexiones que podría tener por el número de nodos que tiene. A través de la teoría de la combinatoria, sabemos que la elección de dos nodos dentro de un conjunto de $N$ "
    "nodos viene dada por $\\frac{N(N-1)}{2}$. Como tenemos una cantidad de $L$ conexiones reales, la densidad queda como $D=\\frac{2L}{N(N-1)}$. "
    "Para los grafos directos el término $2$ no aparece."
)
st.markdown(body=body_h)
st.markdown(body="### Coeficiente de clustering")
body_i = (
    "El coeficiente de clustering se define como la probabilidad de que dos nodos dados de un nodo $i$ esten conectados tambien. El coeficiente es "
    "la media de todos los coeficientes de los nodos.\n\n"
    "Esta propiedad, al ser por nodo, puede ser representada en un histograma, para conocer la distribución."
)
st.markdown(body=body_i)




