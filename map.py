# Import folium : https://github.com/python-visualization/folium
import folium
# Import pandas : https://pandas.pydata.org/pandas-docs/stable/index.html
import pandas as pd

print(dir(folium))

data = pd.read_csv('Dataset.csv').fillna(value = 0)
# [819 rows x 36 columns]

location = data['Latitude'].mean(), data['Longitude'].mean()
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


for name, lat, long, elev, vei in zip(data['Name'], data['Latitude'], data['Longitude'], data['Elevation'], data['VEI']):
    popup = folium.Popup("This is the " + name + " volcano", parse_html=True)
    folium.Marker(location=[lat, long], popup=popup, icon=folium.Icon(color=col(elev))).add_to(m)

#    if vei != 0:
#        vei_str = "VEI = " + str(vei)


# folium.CircleMarker(location=[lat, long], popup=vei_str, color=col(elev), radius=(int(vei)*10)).add_to(m)


# for lat, long in zip(data['Latitude'], data['Longitude']):
   # folium.Marker(location=[lat, long]).add_to(m)

print()
print(m.save('map.html'))
