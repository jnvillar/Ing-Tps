#!/usr/bin/env python
# -*- coding: latin-1 -*-

import cv2
import numpy as np
import urllib
from motionless import *
from Ubicacion import *
import googlemaps
import webbrowser

class Mapa(object):
    #habria que hacer que reciba un origen y destino, no con coordenadas
    def __init__(self, origen, destino):
        self.gmaps = googlemaps.Client(key='AIzaSyCYMZgZTgYwc2CeJy37REmBjTevjDPBKHA')
        self.origen = origen
        self.destino = destino
        # MacOS
        # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Windows
        # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

        # Linux
        self.chrome_path = '/usr/bin/google-chrome %s'

    def distance(self):
        # expressed in metric system
        directions_result = self.gmaps.directions(self.origen,
                                     self.destino,
                                     mode="walking",
                                     alternatives= False)

        return directions_result[0]['legs'][0]['distance']['value']

    def address2coord(self, address):
        return self.gmaps.geocode(address)[0]['geometry']['location']

    def mostrar(self):
        coords_origin = self.address2coord(self.origen)
        coords_dest = self.address2coord(self.destino)
        url = "https://www.google.com.ar/maps/dir/{},{}/{},{}".format(
            coords_origin['lat'],
            coords_origin['lng'], 
            coords_dest['lat'], 
            coords_dest['lng'])

        webbrowser.get(self.chrome_path).open(url)