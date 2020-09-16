#!/usr/bin/env python
# coding: utf-8

# In[38]:


import fiona
import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from shapely.geometry import Point, Polygon
from shapely.geometry import shape, mapping
import numpy as np
import geoplot as gplt
import seaborn as sns
import folium 
get_ipython().system('pip install -U folium')
get_ipython().system('pip install Pillow')
from PIL import Image
from PIL import Image
import requests
from folium.plugins import MarkerCluster
import geopandas
import os
import shapefile
from json import dumps


# In[164]:


df = pd.read_csv('neighborhoods.csv')
df = df[df['State'] =="NJ"]
df = df[df["City"] == "Paterson"]
df2 = pd.read_csv('zipcodes.csv')
df2 = df2[df2['State'] =="NJ"]
df2


# In[62]:


## load shapefile
shp_sd = gpd.read_file('NJ_County_Centroids_3424.shp')
shp_sd2 = gpd.read_file('NJ_Municipal_Boundaries_3424.shp')
# #coords = df16[['lat', 'lon']].values
# #geom = gpd.points_from_xy(df16['lat'], df16['lon'])
# crs = {'init': 'epsg:4326'}
df3= pd.read_json('nj_new_jersey_zip_codes_geo.min.json')
cali_map = folium.Map(location=[40.914745, -74.162827], zoom_start=12)
folium.Choropleth(geo_data=df3['features'][512], 
                     fill_color='OrRd',
                     fill_opacity=0.2,
                     line_opacity=0.5,
                     key_on='feature.properties.ZCTA5CE10').add_to(cali_map)
folium.LayerControl().add_to(cali_map)
df3
# shp_sd2= shp_sd2[shp_sd2["COUNTY"]== 'PASSAIC']
# shp_sd2 = shp_sd2[shp_sd2["NAME"]== 'Paterson']
# shp_sd2 
#shp_sd2.head()
#gdf = gpd.GeoDataFrame(coords, crs=crs, geometry=geom)


# In[46]:


map3 = folium.Map(location=(40.914745, -74.162827), zoom_start=12)
folium.TileLayer('openstreetmap').add_to(map3)
folium.TileLayer('Stamen Terrain').add_to(map3)
folium.TileLayer('Stamen Toner').add_to(map3)
folium.LayerControl().add_to(map3)

map3


# In[47]:


map= folium.Map(location=(40.914745, -74.162827), zoom_start=12)
folium.TileLayer('openstreetmap').add_to(map)
folium.TileLayer('Stamen Terrain').add_to(map)
folium.TileLayer('Stamen Toner').add_to(map)
#folium.LayerControl().add_to(map)

_geojson=geopandas.read_file('NJ_Municipal_Boundaries_3424.geojson')
_geojson.head()


# In[48]:


fig, ax = plt.subplots(figsize=(30,15))
shp_sd.plot(ax=ax, color="lightgray", edgecolor="black");


# In[51]:


fig, ax = plt.subplots(figsize=(30,15))
shp_sd2.plot(ax=ax, color="lightgray", edgecolor="black");
shp_sd2


# In[110]:


gdff= shp_sd2.to_crs("EPSG:4326") 
print(gdff.crs)
EPSG:4326
mappy = folium.Map(location=[43.062776, -75.420884],tiles="cartodbpositron", zoom_start=14)
folium.GeoJson(data=gdff["geometry"]).add_to(mappy) 
mappy


# In[169]:



import geopandas
gdf = geopandas.read_file('nj_new_jersey_zip_codes_geo.min.json')

mo = folium.Map([40.914745, -74.162827], zoom_start=9)

folium.GeoJson(
    gdf,
).add_to(mo)

folium.Choropleth(
    geo_data=gdf,
    data=df2,
    columns=['RegionID', '2020-07-31'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=.5,
    line_opacity=0.2,
    legend_name='Market Value (%)',
    highlight=True
).add_to(mo)


mo


# In[167]:


# gdff= shp_sd2.to_crs("EPSG:4326") 
# print(gdff.crs)
# EPSG:4326
# mapp = folium.Map(location=[43.062776, -75.420884],tiles="cartodbpositron", zoom_start=7)
# folium.GeoJson(data=gdff["geometry"]).add_to(mapp) 
# mapp
# from branca.colormap import linear

# colormap = linear.YlGn_09.scale(
#     df2['2020-07-31'].min(),
#     df2['2020-07-31'].max())


# unemployment_dict = df2.set_index('RegionName')['2020-07-31']
# folium.GeoJson(
#     gdff,
#     name='unemployment',
#     style_function=lambda feature: {
#         'fillColor': colormap(unemployment_dict[feature['id']]),
#         'color': 'black',
#         'weight': 1,
#         'dashArray': '5, 5',
#         'fillOpacity': 0.9,
#     }
# ).add_to(mapp)
# mapp


# In[ ]:




