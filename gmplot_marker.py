import geocoder
import gmplot

city = input('Enter city: ')
b = geocoder.osm(city)
gmap1 = gmplot.GoogleMapPlotter((b.latlng)[0], (b.latlng)[1], 13)

f = open("places.txt", "r")
for line in f.readlines():
    line = line.strip()
    g = geocoder.osm(str(line))
    try:
        gmap1.marker(float(g.latlng[0]), float(g.latlng[1]), title = str(line))
    except:
        print(line)
        continue

gmap1.draw("places.html")
