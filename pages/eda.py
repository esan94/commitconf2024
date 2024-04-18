import streamlit as st
import folium
from folium.plugins import MarkerCluster
import pandas as pd
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


st.title(body=":bar_chart: ¿Cómo son los datos?")
st.markdown(body="## :one: Exploratory Data Analysis")

texto = """
El Análisis Exploratorio de Datos (EDA) es una técnica fundamental en el proceso de comprensión de conjuntos de datos complejos. En el contexto 
de la red de autobuses de Madrid, esta metodología adquiere una relevancia significativa al ofrecer una visión detallada de la infraestructura y 
el funcionamiento del sistema de transporte público en la capital española. 
"""
st.write(texto)

df_combinado_nonull = pd.read_csv('data/df_combinado_latlon.csv')
# Crear un mapa centrado en Madrid
madrid_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12)
# Crear un cluster de marcadores
marker_cluster = MarkerCluster().add_to(madrid_map)
# Añadir marcadores para cada parada
for index, row in df_combinado_nonull.iterrows():
    folium.Marker(location=[row['latitud'], row['longitud']], popup=row['codigo_parada']).add_to(marker_cluster)
# Guardar el mapa como un archivo HTML
mapa_html = madrid_map._repr_html_()
# Mostrar el mapa en la aplicación de Streamlit
st.components.v1.html(mapa_html, width=800, height=500)

texto = """
En esta parte de la presentación, nos adentramos en el análisis de datos de la EMT, comenzando con una exploración visual a través de un 
mapa interactivo que muestra todas las paradas de autobús en la ciudad. Este mapa proporciona una representación inicial de la distribución geográfica 
de las paradas y su densidad en diferentes áreas urbanas. Nos da un primer contexto del volumen de paradas al que nos encontramos y vemos de un primer vistazo 
áreas bastante más masificadas que otras.
"""
st.write(texto)

texto = """
Este análisis no solo proporcionará una descripción detallada de cómo son los datos de la red, sino que también servirá como base para la toma de 
decisiones informadas en la planificación y optimización de rutas, la asignación de recursos y la mejora del servicio de transporte público en la ciudad en 
el posterior análisis mediante grafos.
"""
st.write(texto)


texto = """
Se analizará la red de autobuses de Madrid a través de cuatro bloques temáticos principales: Afluencia, Líneas, Distritos y Distancias. Cada bloque se centra en 
aspectos específicos del sistema de transporte, desde la distribución geográfica de las paradas hasta la conectividad entre ellas. Además, se incluye un análisis adicional 
sobre Contaminación, que examina el impacto ambiental del transporte público en la ciudad. Estos bloques ofrecen una visión completa del funcionamiento y la eficiencia del 
sistema de autobuses en Madrid.
"""
st.write(texto)

# 1st block. PARADAS
st.markdown(body="### 1- Afluencia. Paradas con mayor y menor afluencia")

texto = """
Entendiendo como "afluencia" en este análisis como la cantidad de autobuses de diferentes líneas que pasan por una misma estación física o parada en un 
período de tiempo determinado. Este indicador es importante para comprender la demanda de pasajeros en cada punto de la red y para evaluar la eficiencia y 
la capacidad del sistema para satisfacer dicha demanda.
"""
st.write(texto)

st.markdown(body="##### Paradas con mayor afluencia")
emt_csv = pd.read_csv('data/df_combinado_latlon.csv')
df_distritos = pd.read_csv('data/df_distritos.csv')
df_distritos.rename(columns={'numero_distrito':'distrito_parada'}, inplace=True)
important_stops = emt_csv[['codigo_parada','direccion_parada','distrito_parada','latitud','longitud']].value_counts().reset_index().head(9)
df_merged = pd.merge(important_stops, df_distritos[['distrito_parada', 'nombre_distrito']], on='distrito_parada', how='left')
df_merged= df_merged[['direccion_parada','nombre_distrito','count']]
st.write(df_merged)

# mapa1.1
attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
      )
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"
# Crear un mapa centrado en Madrid
important_stops_map = folium.Map(location=[40.4168, -3.7038], zoom_start=15, tiles=tiles, attr=attr)

# Añadir marcadores para cada parada
for index, row in important_stops.iterrows():
    folium.Marker(location=[row['latitud'], row['longitud']], icon=folium.Icon(color='red')).add_to(important_stops_map)

mapa1_1 = important_stops_map._repr_html_()
st.components.v1.html(mapa1_1, width=800, height=500)

texto = """
* Las paradas con mayor número de líneas se concentran entre el distrito 1 (Centro) y 3 (Retiro)
* Se observan dos paradas con 19 líneas y cuatro paradas con 18 líneas
* Se observan que las 10 paradas con mayor afluencia de líneas se concentran en la zona central de Madrid
"""
st.write(texto)

st.markdown(body="##### Paradas con menor afluencia")
# paradas con 1 stop
insignificant_stops = emt_csv[['codigo_parada','direccion_parada','distrito_parada','latitud','longitud']].value_counts().reset_index()
insignificant_stops = insignificant_stops[insignificant_stops['count']==1]
df_merged_2 = pd.merge(insignificant_stops, df_distritos[['distrito_parada', 'nombre_distrito']], on='distrito_parada', how='left')
df_merged_2= df_merged_2[['direccion_parada','nombre_distrito','count']]
st.write(df_merged_2)

#mapa 1.2
# Crear un cluster de marcadores
marker_cluster_ins = MarkerCluster(color='green').add_to(important_stops_map)

# Añadir marcadores para cada parada
for index, row in insignificant_stops.iterrows():
    folium.Marker(location=[row['latitud'], row['longitud']], icon=folium.Icon(color='green')).add_to(marker_cluster_ins)

mapa1_2 = important_stops_map._repr_html_()
st.components.v1.html(mapa1_2, width=800, height=500)

texto = """
* Al añadir las paradas con una sola línea al mapa se observa que, aunque hay algunas en los 
distritos centrales, la mayoría se localizan en la periferia, fuera de la m-30
"""
st.write(texto)

texto = """
**Conclusión:** Tras analizar la afluencia de autobuses, observamos que las paradas con mayor afluencia se encuentran 
principalmente en las zonas centrales de la ciudad, donde convergen múltiples líneas de autobús. Una posible acción a estudiar, y que se verá más adelante,
es qué ocurriría con la red si se eliminan ciertos tramos que comparten muchas líneas de autobús.
"""
st.write(texto)

# 2nd block. LINEAS
st.markdown(body="### 2- Líneas. Mayor y menor numero de paradas")

texto = """
Este bloque se centra en analizar la distribución del número de paradas en cada línea de autobús dentro de la red. Este análisis permitirá 
comprender la extensión y la cobertura de cada línea a lo largo de la ciudad, así como identificar diferencias significativas entre ellas en términos de longitud y densidad de paradas.
"""
st.write(texto)

recorrido_toA = pd.read_csv('data/stops_toA.csv')

import matplotlib.pyplot as plt

# Calcular el número de paradas por línea
conteo_paradas_por_linea = recorrido_toA['linea'].value_counts()
moda = conteo_paradas_por_linea.mode()[0]

# Graficar el número de paradas por línea como un histograma
plt.figure(figsize=(12, 6))
plt.hist(conteo_paradas_por_linea, bins=43, color='#2c7abf')  # Puedes ajustar el número de bins según tus datos
plt.xlabel('Número de paradas')
plt.ylabel('Frecuencia')
plt.title('Distribución del número de paradas por línea de autobús')
plt.axvline(x=moda, color='red', linestyle='-', label=f'Moda: {moda}', lw = 3)
plt.grid(axis='y')


# plt.tight_layout()
plt.show()
st.pyplot(plt)

texto = """
    * La mayoría de líneas tienen alrededor de 30 paradas
    * Por otro lado, se observa un número considerable de líneas con 15 paradas o menos y alguna línea con más de 40 paradas 
"""
st.write(texto)

st.markdown(body="#### Líneas con más paradas")
conteo_paradas_por_linea = recorrido_toA['linea'].value_counts()
lineas_masparadas = conteo_paradas_por_linea.head(9).reset_index()
lineas_masparadas = lineas_masparadas['linea'].tolist()
df_lineas_masparadas = recorrido_toA[recorrido_toA['linea'].isin(lineas_masparadas)]

# st.write(df_lineas_masparadas)

# Opcion 1
colores_linea = {
    116: 'blue',
    150: 'red',
    34: 'green',
    174: 'orange',
    506: 'purple',
    505: 'pink',
    138: 'yellow',
    137: 'black',
    132: 'lightblue'
}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Añadir marcadores para cada parada
for index, row in df_lineas_masparadas.iterrows():
    # Obtener el color correspondiente a la línea actual
    color = colores_linea.get(row['linea'], 'gray')  # Usar gris como color predeterminado si la línea no está en el diccionario
    folium.Marker(location=[row['longitude'], row['latitude']], icon=folium.Icon(color=color)).add_to(lineas_masparadas_map)

# Mostrar el mapa en el notebook
mapa2_1 = lineas_masparadas_map._repr_html_()
st.components.v1.html(mapa2_1, width=800, height=500)

# Opcion 2
# attr = (
#     'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
# )
# tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# # Crear un mapa centrado en Madrid
# lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# # Crear un diccionario para almacenar las coordenadas de las líneas
# lineas = {}

# # Iterar sobre el DataFrame para agrupar las coordenadas por línea
# for index, row in df_lineas_masparadas.iterrows():
#     if row['linea'] not in lineas:
#         lineas[row['linea']] = []
#     # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
#     lineas[row['linea']].append([row['longitude'], row['latitude']])

# # Agregar las líneas al mapa
# for linea, coordenadas in lineas.items():
#     color = colores_linea.get(linea, 'gray')
#     folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    

# # Mostrar el mapa en el notebook
# mapa2_2 = lineas_masparadas_map._repr_html_()
# st.components.v1.html(mapa2_2, width=800, height=500)

texto = """
* Todas las líneas con mayor número de paradas tienen estaciones dentro de la m-30
* Estas líneas van de distritos centrales a distritos de la periferia
"""
st.write(texto)

st.markdown(body="#### Líneas con menos paradas")

lineas_menosparadas = conteo_paradas_por_linea.tail(7).reset_index()
lineas_menosparadas = lineas_menosparadas['linea'].tolist()
lineas_menosparadas = recorrido_toA[recorrido_toA['linea'].isin(lineas_menosparadas)]
# st.write(lineas_menosparadas)

# Definir el diccionario de colores
colores_linea = {
    180: 'blue',
    709: 'red',
    702: 'green',
    718: 'orange',
    721: 'purple',
    527: 'pink',
    481: 'yellow',
}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Crear un diccionario para almacenar las coordenadas de las líneas
lineas = {}

# Iterar sobre el DataFrame para agrupar las coordenadas por línea
for index, row in lineas_menosparadas.iterrows():
    if row['linea'] not in lineas:
        lineas[row['linea']] = []
    # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
    lineas[row['linea']].append([row['longitude'], row['latitude']])

# Agregar las líneas al mapa
for linea, coordenadas in lineas.items():
    color = colores_linea.get(linea, 'gray')
    folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    

# Mostrar el mapa en el notebook
mapa2_3 = lineas_masparadas_map._repr_html_()
st.components.v1.html(mapa2_3, width=800, height=500)

texto = """
* Al contrario, las líneas con menos paradas se encuentran en los distritos periféricos
* Hacen recorridos muy particulares y específicos (Aeropuerto, Ifema ...)
"""
st.write(texto)

texto = """
**Conclusión:** La distribución del número de paradas en las líneas de autobús de Madrid refleja una combinación de factores geográficos, demográficos y de demanda, que influyen en la planificación y la 
eficiencia del servicio de transporte público en la ciudad. Sin embargo, este análisis hace recapacitar acerca de si son necesarios algunos trayectos o si es necesario crear una línea para casos tan específicos.
"""
st.write(texto)

# 3rd block. LINEAS
st.markdown(body="### 3- Distritos. Distritos más o menos relevantes")

texto = """
En este bloque, se analizarán los distritos más relevantes dentro de la red de autobuses de Madrid, considerando el número de paradas de autobús ubicadas en cada uno. 
Este análisis nos permitirá identificar los distritos que tienen una mayor densidad de paradas y, por lo tanto, una mayor conectividad y accesibilidad en términos de transporte público.
"""
st.write(texto)

st.markdown(body="#### Distritos con más paradas")

diccionario_distritos = {
    1: "Centro",
    2: "Arganzuela",
    3: "Retiro",
    4: "Salamanca",
    5: "Chamartín",
    6: "Tetuán",
    7: "Chamberí",
    8: "Fuencarral-El Pardo",
    9: "Moncloa-Aravaca",
    10: "Latina",
    11: "Carabanchel",
    12: "Usera",
    13: "Puente de Vallecas",
    14: "Moratalaz",
    15: "Ciudad Lineal",
    16: "Hortaleza",
    17: "Villaverde",
    18: "Villa de Vallecas",
    19: "Vicálvaro",
    20: "San Blas-Canillejas",
    21: "Barajas"
}

# Crear DataFrame
df_distritos = pd.DataFrame(list(diccionario_distritos.items()), columns=['numero_distrito', 'nombre_distrito'])
emt_csv = emt_csv[['codigo_estacion','codigo_parada','nombre_parada','linea','direccion_parada'	,'cp_parada','distrito_parada','longitud','latitud']]
distrito_paradas_lineas = emt_csv['distrito_parada'].value_counts()
df_paradas_distritos = df_distritos.merge(distrito_paradas_lineas, left_on='numero_distrito', right_index=True)
df_paradas_distritos.rename(columns={'count': 'paradas_totales'}, inplace=True)
df_paradas_distritos = df_paradas_distritos.sort_values(by='paradas_totales', ascending=False)
# st.write(df_paradas_distritos)


emt_csv_paradas_unicas = emt_csv.drop_duplicates(subset = 'codigo_parada')
emt_csv_paradas_unicas = emt_csv_paradas_unicas['distrito_parada'].value_counts()
df_paradas_distritos_final = df_paradas_distritos.merge(emt_csv_paradas_unicas, left_on='numero_distrito', right_index=True)
df_paradas_distritos_final.rename(columns={'count':'paradas_unicas'}, inplace=True)

#Distritos con mayor número de paradas
df_sorted_total = df_paradas_distritos_final.sort_values(by='paradas_totales', ascending=False)
plt.figure(figsize=(10, 6))
colors = ['red' if x == 'Centro' else '#2c7abf' for x in df_sorted_total['nombre_distrito']]
plt.bar(df_sorted_total['nombre_distrito'], df_sorted_total['paradas_totales'], color=colors)
plt.xlabel('Distrito')
plt.ylabel('Número de Paradas Totales')
plt.title('Distritos con Mayor Número de Paradas Totales')
plt.tick_params(axis='x', rotation=90)
st.pyplot(plt)

st.markdown(body="#### Distritos con más paradas únicas")
df_paradas_distritos_final.drop(columns=['paradas_totales'], inplace=True)
df_paradas_distritos_final = df_paradas_distritos_final.sort_values(by='paradas_unicas', ascending=False)
# st.write(df_paradas_distritos_final)

# Gráfico de barras para los distritos con mayor número de paradas únicas
df_sorted_unique = df_paradas_distritos_final.sort_values(by='paradas_unicas', ascending=False)
plt.figure(figsize=(10, 6))
colors = ['red' if x == 'Centro' else '#2c7abf' for x in df_sorted_unique['nombre_distrito']]
plt.bar(df_sorted_unique['nombre_distrito'], df_sorted_unique['paradas_unicas'], color=colors)
plt.xlabel('Distrito')
plt.ylabel('Número de Paradas Únicas')
plt.tick_params(axis='x', rotation=90)
plt.title('Distritos con Mayor Número de Paradas Únicas')
st.pyplot(plt)

# 4th block. LINEAS
st.markdown(body="### 4- Distancias")

texto = """
En este bloque se analizan las distancias entre paradas en la red de autobuses, con el objetivo de identificar 
las líneas más largas y más cortas, así como las distancias entre paradas más largas y más cortas.

Este análisis nos permitirá comprender mejor la distribución de las paradas a lo largo de las rutas de autobús y su impacto en la accesibilidad 
y la eficiencia del servicio. Además, se podrá identificar posibles áreas de mejora en términos de conectividad y accesibilidad en la red de autobuses de Madrid. 
"""
st.write(texto)

df_distancias = pd.read_csv('data/stops_toA.csv')

st.markdown(body="#### Líneas con la distancia más larga y más corta")

distancias_maximas = df_distancias.groupby('linea')['distance'].max()
distancias_minimas = df_distancias.groupby('linea')['distance'].max()
distancias_maximas = distancias_maximas.sort_values(ascending=False).head(5)
distancias_minimas = distancias_minimas.sort_values(ascending=False).tail(5)

col1, col2 = st.columns(2)  # Divide el espacio en dos columnas

with col1:
    st.write('Distancias máximas')
    st.write(distancias_maximas)

with col2:
    st.write('Distancias mínimas')
    st.write(distancias_minimas)

df_distancias_maximas = df_distancias[df_distancias['linea'].isin(distancias_maximas.index)]
df_distancias_minimas = df_distancias[df_distancias['linea'].isin(distancias_minimas.index)]

# Lineas con la distancia más larga
colores_linea = {
    203: 'blue',
    527: 'red', 
    506: 'green',  
    509: 'yellow',    
    200: 'black'    

}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Crear un diccionario para almacenar las coordenadas de las líneas
lineas = {}

# Iterar sobre el DataFrame para agrupar las coordenadas por línea
for index, row in df_distancias_maximas.iterrows():
    if row['linea'] not in lineas:
        lineas[row['linea']] = []
    # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
    lineas[row['linea']].append([row['longitude'], row['latitude']])

# Agregar las líneas al mapa
for linea, coordenadas in lineas.items():
    color = colores_linea.get(linea, 'gray')
    folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    
# Mostrar el mapa en el notebook
mapa4_1 = lineas_masparadas_map._repr_html_()


# Lineas con la distancia más corta
colores_linea = {
    177: 'blue',
    601: 'red', 
    92: 'green',  
    452: 'yellow',    
    481: 'black' 

}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Crear un diccionario para almacenar las coordenadas de las líneas
lineas = {}

# Iterar sobre el DataFrame para agrupar las coordenadas por línea
for index, row in df_distancias_minimas.iterrows():
    if row['linea'] not in lineas:
        lineas[row['linea']] = []
    # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
    lineas[row['linea']].append([row['longitude'], row['latitude']])

# Agregar las líneas al mapa
for linea, coordenadas in lineas.items():
    color = colores_linea.get(linea, 'gray')
    folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    
# Mostrar el mapa en el notebook
mapa4_2 = lineas_masparadas_map._repr_html_()

st.components.v1.html(mapa4_1, width=800, height=500)
st.components.v1.html(mapa4_2, width=800, height=500)

texto = """
En primer lugar, es importante destacar que las líneas con la distancia más larga suelen corresponder a aquellas que tienen como destino el aeropuerto. 
Esto sugiere que estas líneas operan como rutas de larga distancia, conectando puntos clave de la ciudad con el aeropuerto, un nodo importante en términos 
de movilidad regional y turismo. Sin embargo, se observa que dos líneas son exactamente iguales a execpción de una parada, por lo que se podría investigar 
en la herramienta de análisis como influye quitar una de las 2 líneas en la conectividad total del grafo.

Por otro lado, las líneas con la distancia más corta entre paradas pueden presentar desafíos en términos de eficiencia y utilidad del servicio. 
En algunos casos, estas líneas pueden ser demasiado cortas para proporcionar una conectividad significativa entre diferentes áreas urbanas, lo que puede 
resultar en una baja demanda de transporte público en estas rutas. Una posible solución podría ser considerar la eliminación de estas líneas o la 
reestructuración de sus rutas para mejorar su utilidad y eficiencia.
"""
st.write(texto)

st.markdown(body="#### Mayor y menor distancia entre paradas ")
# Calcular la distancia entre paradas
df_distancias['distancia_entre_paradas'] = df_distancias.groupby('linea')['distance'].diff().fillna(0)
# Resetear la distancia cuando cambia la línea
linea_cambia = df_distancias['linea'] != df_distancias['linea'].shift(1)
df_distancias['distancia_entre_paradas'] = df_distancias['distancia_entre_paradas'].where(~linea_cambia, 0).astype(int)
distancias_parada_maximas = df_distancias.groupby('linea')['distancia_entre_paradas'].max()
distancias_parada_minimas = df_distancias.groupby('linea')['distancia_entre_paradas'].nsmallest(2).groupby(level=0).nth(1)
distancias_parada_maximas = distancias_parada_maximas.sort_values(ascending=False).head(5)
distancias_parada_minimas = distancias_parada_minimas.sort_values(ascending=False).tail(6)
df_distancias_parada_max = df_distancias[df_distancias['linea'].isin(distancias_parada_maximas.index)]
df_distancias_parada_max = df_distancias_parada_max[df_distancias_parada_max['distancia_entre_paradas'].isin(distancias_parada_maximas) | df_distancias_parada_max['distancia_entre_paradas'].isin(distancias_parada_maximas).shift(-1)]
distancias_parada_minimas = distancias_parada_minimas.loc[distancias_parada_minimas != 0]
distancias_parada_minimas_reset = distancias_parada_minimas.reset_index()
distancias_parada_minimas_reset.drop('level_1', axis=1, inplace=True)
distancias_parada_minimas_reset_final = df_distancias[df_distancias['linea'].isin(distancias_parada_minimas_reset['linea'])]
distancias_parada_minimas_reset_final = distancias_parada_minimas_reset_final[distancias_parada_minimas_reset_final['distancia_entre_paradas'].isin(distancias_parada_minimas_reset['distancia_entre_paradas']) | distancias_parada_minimas_reset_final['distancia_entre_paradas'].isin(distancias_parada_minimas_reset['distancia_entre_paradas']).shift(-1) ]

# st.write(df_distancias_parada_max)
# st.write(distancias_parada_minimas_reset_final)

# Lineas con la distancia más corta
colores_linea = {
    165: 'blue',
    166: 'red', 
    200: 'green',  
    203: 'yellow',    
    527: 'black' 

}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Crear un diccionario para almacenar las coordenadas de las líneas
lineas = {}

# Iterar sobre el DataFrame para agrupar las coordenadas por línea
for index, row in df_distancias_parada_max.iterrows():
    if row['linea'] not in lineas:
        lineas[row['linea']] = []
    # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
    lineas[row['linea']].append([row['longitude'], row['latitude']])

# Agregar las líneas al mapa
for linea, coordenadas in lineas.items():
    color = colores_linea.get(linea, 'gray')
    folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    
# Mostrar el mapa en el notebook
mapa4_3 = lineas_masparadas_map._repr_html_()
st.components.v1.html(mapa4_3, width=800, height=500)

# Lineas con la distancia más corta
colores_linea = {
    132: 'blue',
    127: 'red', 
    402: 'green',  
    403: 'yellow',    
    603: 'black' 

}

attr = (
    'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
)
tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"

# Crear un mapa centrado en Madrid
lineas_masparadas_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12, tiles=tiles, attr=attr)

# Crear un diccionario para almacenar las coordenadas de las líneas
lineas = {}

# Iterar sobre el DataFrame para agrupar las coordenadas por línea
for index, row in distancias_parada_minimas_reset_final.iterrows():
    if row['linea'] not in lineas:
        lineas[row['linea']] = []
    # Asegurarse de que las coordenadas estén en el orden correcto (latitud, longitud)
    lineas[row['linea']].append([row['longitude'], row['latitude']])

# Agregar las líneas al mapa
for linea, coordenadas in lineas.items():
    color = colores_linea.get(linea, 'gray')
    folium.PolyLine(locations=coordenadas, color=color,weight=5).add_to(lineas_masparadas_map)
    
# Mostrar el mapa en el notebook
mapa4_4 = lineas_masparadas_map._repr_html_()
st.components.v1.html(mapa4_4, width=800, height=500)


texto = """
En el análisis de las paradas más largas y más cortas en una línea de autobús específica, es importante tener en cuenta que las paradas 
más largas, en muchos casos, están relacionadas con tramos que conectan con el aeropuerto. Esto refuerza la idea de que el servicio de 
transporte público hacia el aeropuerto desempeña un papel crucial en la movilidad regional y turística, ya que las paradas más largas 
reflejan la necesidad de cubrir distancias significativas entre el aeropuerto y otros puntos de la ciudad.

Por otro lado, algunas paradas más cortas pueden carecer de sentido en términos de eficiencia del servicio. Es posible que estas paradas 
se encuentren muy cerca entre sí, lo que podría indicar una redundancia en la ruta o paradas que no están justificadas por la demanda de 
pasajeros o la necesidad de conectividad. En estos casos, una posible solución sería reconsiderar la ubicación de estas paradas o 
eliminar aquellas que no contribuyan significativamente a la accesibilidad y eficiencia del servicio.
"""
st.write(texto)

st.markdown(body="### 5- Contaminación")

texto = """
A partir de este análisis previo, surge la necesidad de examinar el impacto ambiental del sistema de transporte público en Madrid. 
En este bloque de contaminación, se explora cómo la operación de la red de autobuses contribuye a los niveles de contaminación (emisiones de CO2) en la 
ciudad y cómo estos niveles pueden variar en función de los kilómetros recorrido.

Para este análisis se ha recurrido a la información de Observatorio de Servicios Urbanos: https://www.osur.es/2017/03/27/contaminacion-y-transporte-publico/ ,
que indica que un autobús de media emite 750 gramos de CO2 por kilómetro recorrido.
"""
st.write(texto)

st.markdown(body="#### Distritos más contaminantes")

df_info = pd.read_csv('data/emt-data-clean.csv')
df_paradas = pd.read_csv('data/stops_toA.csv')

df2_unique = df_info.drop_duplicates(subset='codigo_parada')
distritos_df = pd.merge(df_paradas, df2_unique[['codigo_parada', 'distrito_parada']], left_on='stopNum', right_on='codigo_parada', how='left')
distritos_df.drop(columns=['codigo_parada'], inplace=True)
distritos_df.rename(columns={'distrito_parada': 'distrito'}, inplace=True)
distritos_df.dropna(inplace=True)
distritos_df['distrito'] = distritos_df['distrito'].astype(int)
distritos_df['distancia_entre_paradas'] = distritos_df.groupby('linea')['distance'].diff().fillna(0)
linea_cambia = distritos_df['linea'] != distritos_df['linea'].shift(1)
distritos_df['distancia_entre_paradas'] = distritos_df['distancia_entre_paradas'].where(~linea_cambia, 0).astype(int)

dic_distr = pd.read_csv('data/df_distritos.csv')
dic_distr.drop(columns=['Unnamed: 0'], inplace=True)
distrito_distancia = distritos_df.groupby('distrito')['distancia_entre_paradas'].sum()
distrito_distancia_sorted = distrito_distancia.sort_values(ascending=False)
merged_df = pd.merge(distrito_distancia_sorted, dic_distr, left_on='distrito', right_on='numero_distrito')

datos_areas = {
    'numero_distrito': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    'area_distrito_ha': [522.82, 646.22, 546.62, 539.24, 917.55, 537.47, 467.92, 23783.84, 4653.11, 2542.72, 
                          1404.83, 777.77, 1496.86, 610.32, 1142.57, 2741.98, 2018.76, 5146.72, 3526.67, 2229.24, 4192.28]}

# Crear DataFrame de áreas de distritos
areas_df = pd.DataFrame(datos_areas)

merged_df_2 = pd.merge(merged_df, areas_df, left_on='numero_distrito', right_on='numero_distrito')
merged_df_2['area_km2']=merged_df_2['area_distrito_ha']/100
merged_df_2['CO2_total (kg)']=(round(merged_df_2['distancia_entre_paradas']*0.75,0).astype(int))/1000
merged_df_2['CO2_superficie (Kg/Km2)']=(merged_df_2['CO2_total (kg)'])/(merged_df_2['area_km2'])


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
colors = ['red' if x == 'Centro' else '#2c7abf' for x in merged_df_2['nombre_distrito']]
plt.bar(merged_df_2['nombre_distrito'], merged_df_2['CO2_total (kg)'], color=colors)
plt.xlabel('Distrito')
plt.ylabel('CO2 Kg')
plt.title('Distritos con Mayor emisión de CO2 (kg/linea recorrida)')
plt.tick_params(axis='x', rotation=90)
plt.show()
st.pyplot(plt)

merged_df_2.sort_values(by='CO2_superficie (Kg/Km2)',ascending=False, inplace=True)
plt.figure(figsize=(10, 6))
colors = ['red' if x == 'Centro' else '#2c7abf' for x in merged_df_2['nombre_distrito']]
plt.bar(merged_df_2['nombre_distrito'], merged_df_2['CO2_superficie (Kg/Km2)'], color=colors)
plt.xlabel('Distrito')
plt.ylabel('CO2 Kg/Km2')
plt.title('Distritos con Mayor emisión de CO2 (kg/linea recorrida)')
plt.tick_params(axis='x', rotation=90)
plt.show()
st.pyplot(plt)

texto = """
Al analizar los resultados, encontramos que el distrito Centro a pesar de ser uno 
de los distritos más pequeños en términos de área geográfica, registra algunas de las emisiones de CO2 absolutas más 
altas dentro de la red de autobuses de la ciudad. Esto sucede prácticamente con todos los distritos centrales de Madrid (Salamanca, Arganzuela, etc.)

El distrito Centro de Madrid enfrenta, por tanto, desafíos significativos en términos de emisiones de CO2 relacionadas 
con el transporte público. Estos resultados resaltan la importancia de implementar medidas para reducir las emisiones 
de CO2 en esta área, como la optimización de rutas, la promoción de formas alternativas de movilidad y la mejora de la 
infraestructura de transporte público para garantizar un servicio eficiente y sostenible en el corazón de la ciudad. Para ello proponemos 
ayudarnos del análisis mediante grafos que permitan entender lo que supondrían estos cambios en las distintas líneas de la red.
"""
st.write(texto)