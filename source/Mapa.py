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
        self.coord_origen = gmaps.geocode(origen)[0]['geometry']['location']
        self.coord_dest = gmaps.geocode(destino)[0]['geometry']['location']
        # MacOS
        # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Windows
        # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

        # Linux
        self.chrome_path = '/usr/bin/google-chrome %s'

    def mostrar(self):
        url = "https://www.google.com.ar/maps/dir/{},{}/{},{}".format(
            self.coords_origin['lat'],
            self.coords_origin['lng'], 
            self.coords_destination['lat'], 
            self.coords_destination['lng'])

        webbrowser.get(chrome_path).open(url)