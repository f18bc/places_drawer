import geocoder
import gmplot

city = input('Enter city: ')
b = geocoder.osm(city)
gmap1 = gmplot.GoogleMapPlotter((b.latlng)[0], (b.latlng)[1], 13)

c = 0
cc = 0

f = open("places.txt", "r")
for line in f.readlines():
    line = line.strip()
    g = geocoder.osm(str(line))
    try:
        gmap1.marker(float(g.latlng[0]), float(g.latlng[1]), title = str(line))
        c += 1
    except:
        print("Unable to search:", line)
        cc += 1
        continue
    cc += 1
ccc = cc - c
print("Failed to read ", ccc, "Places" )
gmap1.draw("where.html")
