from turtle import pd
import csv
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import folium
from folium import IFrame
from folium.plugins import MarkerCluster
from folium.plugins import FloatImage

img_url = 'images/logo.png'

data =  pd.read_csv('Final Data/Offshore_Projects.CSV', sep=';', encoding='UTF-8')
print(data['Longitude'])

def plot3():
    df1 = pd.read_csv('Final Data/Offshore_Projects.CSV', encoding='UTF-8', sep = ';')
    df2 = pd.read_csv('Final Data/Offshore_Testfelder.CSV', encoding='UTF-8', sep=';')
    types = ['OpenStreetMap', 'cartodbpositron', 'Stamen Toner', 'CartoDB dark_matter', 'stamenwatercolor']
    icon_url = 'images/wind-farm.png'
    icon = folium.features.CustomIcon(icon_url, icon_size=(14, 14))

    m = folium.Map(location=[54.127,1.382], zoom_start=5, tiles = types[3])
    #german_geojson = '2_hoch.geo.json'
    #folium.GeoJson(german_geojson, name="Germany").add_to(m)
    for i in range(len(types)):
        folium.TileLayer(types[i]).add_to(m)

    #folium.TileLayer(types[0]).add_to(m)
    folium.LayerControl().add_to(m)
    FloatImage(img_url, bottom=0, left=0).add_to(m)

    for i in range(len(df1['Name'])):  
        print(str(df1['Baujahr'][0]).replace('.0',''))
        marker = folium.Marker(
            location = [df1['Latitude'][i], df1['Longitude'][i]],
            #icon = icon,
            #content = , width=632+20, height=420+20),
            popup = folium.Popup(
                '<h5>'+str(df1['Name'][i])+'</h5><b>Baujahr: </b>'+str(df1['Baujahr'][i]).replace('.0','')+'<br><b>Leistung: </b>'+str(df1['Leistung'][i])+' MW<br><b>Turbine Zahl: </b>'+str(df1['Turbine Zahl'][i])+'<br> --- <br><b>Kustenentfernung: </b>'+str(df1['Kustenentfernung'][i])+' km<br><b>Wassteriefe: </b>'+str(df1['Wassertiefe'][i])+' m', 
                min_width = 160, 
                max_width=160),
            #tooltip=tooltip
            )
        marker.add_to(m)

    for j in range(len(df2['Name'])):
        print(df2['Name'][j])
        marker = folium.CircleMarker(
            
            location = [df2['lon'][j], df2['lat'][j]],
            popup = folium.Popup(
                '<h5>'+str(df2['Name'][j])+'</h5><br><b>Info: </b>'+str(df2['Connection'][j])+'<br><b>Projects: </b>'+str(df2['Projects'][j])+'<br><b>Area: </b>'+str(df2['Area'][j])+' km2',
                min_width = 100,
                max_width= 100

            ),

            color = 'red'
        )

        marker.add_to(m)
    m.save('/Users/sid/Documents/Work/EnBW/Windkraft/Map Code/map.html')
    
plot3()