import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
pop = list(data["NAME"])
ele = list(data["ELEV"])

map = folium.Map(location=[40.249999, -111.6499974], zoom_start=5, tiles = "Stamen Terrain")


def colorDef(x):
    if x < 1500:
        return "green"
    elif x < 3000:
        return "orange"
    else:
        return "red"

fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln , nm, el  in zip(lat,lon,pop,ele):
    fgv.add_child(folium.CircleMarker(location = [lt, ln] , fill_color = colorDef(el), popup = nm + " " + str(el) + "m",
    fill_opacity = .6, color = colorDef(el)))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("index.html")
