# Import folium : https://github.com/python-visualization/folium
import folium
# Import pandas : https://pandas.pydata.org/pandas-docs/stable/index.html
import pandas as pd
# from ipywidgets import interact


# print(dir(folium))

data = pd.read_csv('Dataset.csv').fillna(value = 0)
print(data.head())

location = data['Latitude'].mean(), data['Longitude'].mean()

# Cloudmade Mapbox needs an API key, Mapbox Control Room is limited to a few levels
# tiles = [name.strip() for name in """
#     OpenStreetMap
#     Mapbox Bright
#     Mapbox Control Room
#     Stamen Terrain
#     Stamen Toner
#     Stamen Watercolor
#     CartoDB positron
#     CartoDB dark_matter""".strip().split('\n')]

# @interact(lat=(-90., 90.), lon=(-180., 180.), tiles=tiles, zoom=(1, 18))
# def create_map(lat=52.518611, lon=13.408333, tiles="Stamen Toner", zoom=10):
#     return folium.Map(location=(lat, lon), tiles=tiles, zoom_start=zoom)

m = folium.Map(location=location, zoom_start=3, tiles='Stamen Terrain')
# m.add_child(folium.LatLngPopup())


# Get Marker color based on elevation
def col(ele):
    if 0 < ele < 1500:
        color = 'green'
    elif 1501 < ele < 3000:
        color = 'yellow'
    elif 3001 < ele < 5000:
        color = 'orange'
    else:
        color = 'red'
    return color

def Vei(num):
    if num == 0:
        vei = 'Not available'
    else:
        vei = str(num)
    return vei

for year, name, latitude, longitude, elev, vei, vol_type, status in zip(data['Year'], data['Name'], data['Latitude'], data['Longitude'], data['Elevation'], data['VEI'], data['Type'], data['Status']):
    popup = folium.Popup("This is the " + name + " volcano which erupted in " + str(year) + ". It is a " + vol_type + " with " + status + " status and an elevation of " + str(elev) + 
                            "m. The Volcano Explosivity Index of the eruption was " + Vei(vei) + ".", parse_html=True)
    folium.Marker(location=[latitude, longitude], popup=popup, icon=folium.Icon(color=col(elev))).add_to(m)

#    if vei != 0:
#        vei_str = "VEI = " + str(vei)


# folium.CircleMarker(location=[lat, long], popup=vei_str, color=col(elev), radius=(int(vei)*10)).add_to(m)


# for lat, long in zip(data['Latitude'], data['Longitude']):
   # folium.Marker(location=[lat, long]).add_to(m)

print(m.save('map.html'))