import streamlit as st
import networkx as nx
from pandas import concat, DataFrame, read_csv, merge
from matplotlib import pyplot as plt
from toolbox.net_utils import generate_graph, get_k_connected_components, get_basic_statistics
from toolbox.genai import OpenAIManager
from toolbox.utils import add_data_to_complete_chat
from loguru import logger
from json import loads

hide_img_fs = """
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
"""

oai = OpenAIManager()

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

st.title(body=":construction: ¿Qué pasaría si...?")
st.markdown(body="## :one: Colapsando la red")

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

text = st.text_area(
    label="¿Quieres conectar una línea nueva? (GPT Powered)",
    placeholder=f"Escribe el nombre de la nueva línea y las/los '{selectbox_dict.get(option)}' que conectar."
    )
if text:
    with open("toolbox/context.txt", "r") as file:
        context = file.read()
    conversation = add_data_to_complete_chat(complete_chat=[], role="system", content=context)
    conversation = add_data_to_complete_chat(complete_chat=conversation, role="user", content=text)
    oai_response = oai.get_response_openai(complete_chat=conversation, temperature=0)
    response_dict = loads(oai_response)
    if response_dict.get("respuesta", 1) is None:
        logger.info("La respuesta fue None")
    else:
        try:
            new_df = DataFrame(response_dict)
            new_df = new_df.unstack().reset_index(drop=False).drop(columns="level_1").rename(columns={"level_0": "edge", 0: "from_node"})
            ll_01 = data[["from_node", "from_lat", "from_lon", "n_buses", "weight"]].drop_duplicates(keep="first").reset_index(drop=True)
            ll_02 = data[["to_node", "to_lat", "to_lon", "n_buses", "weight"]].drop_duplicates(keep="first").reset_index(drop=True).rename(columns={"to_lat": "from_lat", "to_lon": "from_lon", "to_node": "from_node"})
            ll = concat([ll_01, ll_02], ignore_index=True)
            new_df_aux = DataFrame(columns=["from_node", "to_node", "edge"])
            for index, row in new_df.iterrows():
                if index == new_df.shape[0] - 1:
                    break
                new_df_aux_temp = DataFrame({
                    "from_node": [row["from_node"]],
                    "to_node": [new_df.at[index + 1, "from_node"]],
                    "edge": [row["edge"]],
                })
                new_df_aux = concat([new_df_aux, new_df_aux_temp], ignore_index=True).drop_duplicates(keep="first")
            new_df_aux = merge(new_df_aux, ll, on="from_node", how="inner").drop_duplicates(keep="first")
            new_df_aux = merge(new_df_aux, ll.drop(columns=["n_buses", "weight"]).rename(columns={"from_lat": "to_lat", "from_lon": "to_lon", "from_node": "to_node"}), on="to_node", how="inner")
            new_df_aux = new_df_aux[data.columns].drop_duplicates(keep="first", subset=["from_node", "to_node", "edge"])
            data = concat([data, new_df_aux], axis=0, ignore_index=True)
        except Exception as err:
            logger.error(err)

edge_options = sorted(data["edge"].str.zfill(5).unique())
node_options = sorted(list(set(
    data["from_node"].unique().tolist() + data["to_node"].unique().tolist()
    )))
edges = cols[0].multiselect(
    "¿Quieres eliminar alguna línea?",
    edge_options,
    placeholder="Elige una o varias líneas a eliminar"
    )
nodos = cols[1].multiselect(
    "¿Quieres eliminar algun nodo?",
    node_options,
    placeholder="Elige uno o varios nodos a eliminar"
    )

cols = st.columns(spec=2, gap="small")
cols[1].markdown("### Grafo.")
if edges:
    logger.info("Filtrando edges")
    data = data[~data["edge"].str.zfill(5).isin(edges)]
if nodos:
    logger.info("Filtrando nodos")
    data = data[~data["from_node"].isin(nodos)]
    data = data[~data["to_node"].isin(nodos)]
graph = generate_graph(dataframe=data)
is_connected = nx.is_connected(G=graph)
if not is_connected:
    connected_nodes = get_k_connected_components(network=graph, k=100000)
    graph = graph.subgraph(nodes=connected_nodes[0])
pos = nx.get_node_attributes(graph, "pos")
ww = [graph[u][v]["weight"] * 2 for u,v in graph.edges()]
fig, ax = plt.subplots(figsize=(4,4))
nx.draw(
    graph, pos, width=ww, ax=ax,
    with_labels=False, node_color="#2c7abf", font_size=8, 
    node_size=1, edge_color="#686c6f", font_color="#fff", 
    font_weight="bold"
    )
cols[1].pyplot(fig=fig, clear_figure=True, use_container_width=True)
cols[0].markdown("### Métricas.")
statistics = get_basic_statistics(network=graph)
statistics_body = (
    f"- Número de nodos del grafo: {statistics.get('num_nodes')}\n"
    f"- Número de conexiones del grafo: {statistics.get('num_edges')}\n"
    f"- Densidad del grafo: {round(statistics.get('density'), 3)}\n"
    f"- Diámetro del grafo: {round(statistics.get('diameter'), 3)}\n"
    f"- Grado medio del grafo: {round(statistics.get('mean_ncn'), 3)}\n"
    f"- Media de caminos más cortos del grafo: {round(statistics.get('mean_net_sp'), 3)}\n"
)
cols[0].markdown(body=statistics_body)
ns = [100 * statistics["centrality"].get(node) for node in graph.nodes]
df = DataFrame({selectbox_dict[option]: graph.nodes, "% conectados": ns})
df = df.sort_values(by="% conectados", ascending=False).head(5).reset_index(drop=True)
cols = st.columns(spec=2, gap="small")
cols[0].table(df)
ns = [100 * statistics["closeness_centrality"].get(node) for node in graph.nodes]
df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de centralidad de cercanía": [_/100 for _ in ns]})
df = df.sort_values(by="Grado de centralidad de cercanía", ascending=False).head(5).reset_index(drop=True)
cols[1].table(df)
cols = st.columns(spec=2, gap="small")

ns = [100 * statistics["eig_centrality"].get(node) for node in graph.nodes]
df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de centralidad propia": [_/100 for _ in ns]})
df = df.sort_values(by="Grado de centralidad propia", ascending=False).head(5).reset_index(drop=True)
cols[0].table(df)

ns = [100 * statistics["betweeness_centrality"].get(node) for node in graph.nodes]
df = DataFrame({selectbox_dict[option]: graph.nodes, "Grado de intermediación": ns})
df = df.sort_values(by="Grado de intermediación", ascending=False).head(5).reset_index(drop=True)
cols[1].table(df)

if not is_connected:
    warning_body = f"> :warning: <small style='font-size: 10px;'>Con las elecciones tomadas el grafo inicial se ha desconectado en {len(connected_nodes)} subgrafos.</small>"
    st.markdown(body=warning_body, unsafe_allow_html=True)