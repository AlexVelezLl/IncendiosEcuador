import folium
map1 =folium.Map(location=[-2.1961601,-79.8862076], zoom_start=7)
file = open("fire_nasa_global.csv")
file.readline()

fgv =folium.FeatureGroup(name="Incendios")
i=1
for line in file:
        line = line.strip().split(",")
        lat= float(line[0])
        lon = float(line[1])
        DN = line[-1]
        if lat>-5.5 and lon>-82 and lat<1 and lon<-75:
            i += 1
            fgv.add_child(folium.Marker(location=[lat, lon],
                                    popup="fire!!",
                                    icon=folium.Icon(icon='fire', color="red")))
map1.add_child(fgv)
map1.save("Incendios.html")
