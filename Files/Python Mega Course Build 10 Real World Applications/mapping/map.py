import folium

map= folium.Map(location=[17.807548, 73.985829])
fg=folium.FeatureGroup(name="My MAp ")

for coordinates in [[17.807518, 73.985817],[17.677374, 74.004230]]:
    fg.add_child(folium.Marker(location=coordinates,popup="hi my name is ",icon=folium.Icon(color="green")))
map.add_child(fg )
map.save("Map1.html")
