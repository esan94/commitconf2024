import networkx as nx
import streamlit as st
from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv

from toolbox.net_utils import generate_graph, get_basic_statistics, get_k_connected_components

from loguru import logger

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

st.title(body=":busstop: La red de la EMT de Madrid.")
st.markdown(body="## :two: Análisis de la red")
selectbox_dict = {
    "cp": "Código Postal",
    "distrito": "Distrito",
    "busstop": "Parada de autobús"
}
option = st.selectbox(
   "¿Qué tipo de nodo quieres ver?",
   ("cp", "distrito", "busstop"),
   index=0, format_func=lambda c: selectbox_dict[c]
)
cols = st.columns(spec=2, gap="small")
data = read_csv(f"data/net_{option}.csv")
if option == "busstop":
    data = data[data["n_buses"] > 1]
graph = generate_graph(dataframe=data)
is_connected = nx.is_connected(G=graph)
if not is_connected:
    connected_nodes = get_k_connected_components(network=graph, k=1)
    graph = graph.subgraph(nodes=connected_nodes[0])

statistics = get_basic_statistics(network=graph)
pos = nx.get_node_attributes(graph, "pos")
ww = [graph[u][v]["weight"] * 2 for u,v in graph.edges()]
fig, ax = plt.subplots(figsize=(4,4))
nx.draw(
    graph, pos, width=ww, ax=ax,
    with_labels=False, node_color="#2c7abf", font_size=8, 
    node_size=1, edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )
cols[0].pyplot(fig=fig, clear_figure=True, use_container_width=True)
if option == "busstop":
    warning_body = "> :warning: <small style='font-size: 10px;'>Para el grafo basado en paradas de autobús se han filtrado aquellas paradas que están conectadas solo por 1 autobús por motivos de cómputo.</small>"
    cols[1].markdown(body=warning_body, unsafe_allow_html=True)
if not is_connected:
    warning_body = "> :warning: <small style='font-size: 10px;'>El grafo inicial no está completamente conectado. La visualización y cálculos se realiza sobre el conjunto de nodos que más conexiones tiene.</small>"
    cols[1].markdown(body=warning_body, unsafe_allow_html=True)
statistics_body = (
    f"- Número de nodos del grafo: {statistics.get('num_nodes')}\n"
    f"- Número de conexiones del grafo: {statistics.get('num_edges')}\n"
    f"- Densidad del grafo: {round(statistics.get('density'), 3)}\n"
    f"- Diámetro del grafo: {round(statistics.get('diameter'), 3)}\n"
    f"- Grado medio del grafo: {round(statistics.get('mean_ncn'), 3)}\n"
    f"- Media de caminos más cortos del grafo: {round(statistics.get('mean_net_sp'), 3)}\n"
)
cols[1].markdown(body=statistics_body)
st.markdown("### Distribución de grado.")
fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["ncn"], bins=20, color="#2c7abf")
ax.set_xlabel("Conexiones")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()

st.markdown("### Distribución de caminos más cortos.")
fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["mean_sp"], bins=20, color="#2c7abf")
ax.set_xlabel("Media de caminos más cortos")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()

st.markdown("### Centralidad de grado.")
fig, ax = plt.subplots(figsize=(4,4))
ns = [100 * statistics["centrality"].get(node) for node in graph.nodes]
nx.draw(
    graph, pos, ax=ax, node_size=ns, width=[_*.5 for _ in ww],
    with_labels=False, node_color="#2c7abf", font_size=8, 
    edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )
df = DataFrame({selectbox_dict[option]: graph.nodes, "% conectados": ns})
df = df.sort_values(by="% conectados", ascending=False).head(5).reset_index(drop=True)
cols = st.columns(spec=2, gap="small")
cols[0].markdown("Grafo")
cols[0].pyplot(fig=fig, clear_figure=True, use_container_width=True)
cols[1].markdown("Top 5 nodos más conectados")
cols[1].table(df)
fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["centrality"].values(), bins=20, color="#2c7abf")
ax.set_xlabel("Grado de centralidad")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.markdown(" ")
st.markdown("Distribución de la centralidad de grado")
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()

st.markdown("### Centralidad de intermediación.")
fig, ax = plt.subplots(figsize=(4,4))
ns = [100 * statistics["betweeness_centrality"].get(node) for node in graph.nodes]
nx.draw(
    graph, pos, ax=ax, node_size=ns, width=[_*.5 for _ in ww],
    with_labels=False, node_color="#2c7abf", font_size=8, 
    edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )
df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de intermediación": ns})
df = df.sort_values(by="Grado de intermediación", ascending=False).head(5).reset_index(drop=True)
cols = st.columns(spec=2, gap="small")
cols[0].markdown("Grafo")
cols[0].pyplot(fig=fig, clear_figure=True, use_container_width=True)
cols[1].markdown("Top 5 nodos")
cols[1].table(df)
cols[1].markdown("> :bulb: El grado de intermediación es el porcentaje de veces que un nodo aparece en el camino más corto entre otros dos nodos.")
fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["betweeness_centrality"].values(), bins=20, color="#2c7abf")
ax.set_xlabel("Grado de intermediación")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.markdown(" ")
st.markdown("Distribución de la centralidad de intermediación")
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()

st.markdown("### Centralidad de cercanía.")
fig, ax = plt.subplots(figsize=(4,4))
ns = [100 * statistics["closeness_centrality"].get(node) for node in graph.nodes]
nx.draw(
    graph, pos, ax=ax, node_size=ns, width=[_*.5 for _ in ww],
    with_labels=False, node_color="#2c7abf", font_size=8, 
    edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )
df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de centralidad de cercanía": [_/100 for _ in ns]})
df = df.sort_values(by="Grado de centralidad de cercanía", ascending=False).head(5).reset_index(drop=True)
cols = st.columns(spec=2, gap="small")
cols[0].markdown("Grafo")
cols[0].pyplot(fig=fig, clear_figure=True, use_container_width=True)
cols[1].markdown("Top 5 nodos")
cols[1].table(df)
cols[1].markdown("> :bulb: El grado de cercanía indica como de cerca está un nodo del resto. Da una medida de nodos con gran impacto en la propagación.")

fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["closeness_centrality"].values(), bins=20, color="#2c7abf")
ax.set_xlabel("Grado de centralidad de cercanía")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.markdown(" ")
st.markdown("Distribución de la centralidad de cercanía")
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()

st.markdown("### Centralidad propia.")
fig, ax = plt.subplots(figsize=(4,4))
ns = [100 * statistics["eig_centrality"].get(node) for node in graph.nodes]
nx.draw(
    graph, pos, ax=ax, node_size=ns, width=[_*.5 for _ in ww],
    with_labels=False, node_color="#2c7abf", font_size=8, 
    edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )

df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de centralidad propia": [_/100 for _ in ns]})
df = df.sort_values(by="Grado de centralidad propia", ascending=False).head(5).reset_index(drop=True)
cols = st.columns(spec=2, gap="small")
cols[0].markdown("Grafo")
cols[0].pyplot(fig=fig, clear_figure=True, use_container_width=True)
cols[1].markdown("Top 5 nodos")
cols[1].table(df)
cols[1].markdown("> :bulb: El grado de centralidad propia indica como de importante es un nodo con respecto a otros nodos importantes. Mide la influencia de un nodo.")

fig, ax = plt.subplots(figsize=(12,4))
ax.hist(statistics["eig_centrality"].values(), bins=20, color="#2c7abf")
ax.set_xlabel("Grado de centralidad propia")
ax.set_ylabel("Num. Nodos")
ax.spines[["right", "top"]].set_visible(False)
st.markdown(" ")
st.markdown("Distribución de la centralidad propia")
st.pyplot(fig=fig, clear_figure=True, use_container_width=True)
st.divider()
