#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df_incidents = pd.read_csv('D:\Certificates\SQL Jupyter Notebook\Generating Maps with Python\Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')


# In[2]:


df_incidents.head()


# In[3]:


df_incidents.shape


# In[4]:


# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]


# In[5]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[7]:


import folium 


# In[9]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[10]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)


# In[12]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)


# In[13]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.features.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map
sanfran_map


# In[14]:


from folium import plugins

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map


# In[15]:


# lists each neighborhood in San Francisco

neighborhood_counts = df_incidents['PdDistrict'].value_counts()
df_incidents_counts = pd.DataFrame(data=neighborhood_counts.values, index=neighborhood_counts.index, columns=['Count'])
df_incidents_counts = df_incidents_counts.reset_index()
df_incidents_counts.rename({'PdDistrict': 'Neighborhood'}, axis='columns', inplace=True)
df_incidents_counts.head(10)


# In[16]:


# Load the San Francisco GeoJSON file
geojson = r'https://cocl.us/sanfran_geojson'

# Create the map centered around San Francisco with a zoom level of 12
sanfran_map = folium.Map(location=[37.77, -122.42], zoom_start=12)

# Generate the choropleth map
sanfran_map.choropleth(
    geo_data=geojson,
    data=df_incidents_counts,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
)

# Display the map
sanfran_map


# In[ ]:




