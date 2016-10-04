import googlemaps
import webbrowser

gmaps = googlemaps.Client(key='AIzaSyCYMZgZTgYwc2CeJy37REmBjTevjDPBKHA')

origin="Costa Rica 4677, Ciudad Autonoma de Buenos Aires"
destination="Gorriti 5037"

geocode_origin = gmaps.geocode(origin)
geocode_destination = gmaps.geocode(destination)

coords_origin = geocode_origin[0]['geometry']['location']
coords_destination = geocode_destination[0]['geometry']['location']

url = "https://www.google.com.ar/maps/dir/{},{}/{},{}".format(coords_origin['lat'], coords_origin['lng'], coords_destination['lat'], coords_destination['lng'])

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

#obtener la distancia entre origen y destino
directions_result = gmaps.directions(origin="Costa Rica 4677, Ciudad Autonoma de Buenos Aires",
                                     destination="Gorriti 5037",
                                     mode="walking",
                                     alternatives= False)

print directions_result[0]['legs'][0]['distance']['value']