#!/usr/bin/env python
# -*- coding: latin-1 -*-

import urllib
import googlemaps
import webbrowser
from Ubicacion import *

class GPS(object):
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyCYMZgZTgYwc2CeJy37REmBjTevjDPBKHA')

    def distanciaEntre(self, origen, destino):
        # Expresada en metros
        directions_result = self.gmaps.directions(origen.darDireccion(),
                                     destino.darDireccion(),
                                     mode="walking",
                                     alternatives= False)

        return directions_result[0]['legs'][0]['distance']['value']

    def ubicacionACoordenadas(self, ubicacion):
        return self.gmaps.geocode(ubicacion.darDireccion())[0]['geometry']['location']

    def mostrarRutaEnMapa(self, origen, destino):

        coords_origin = self.ubicacionACoordenadas(origen)
        coords_dest = self.ubicacionACoordenadas(destino)

        url = "https://www.google.com.ar/maps/dir/{},{}/{},{}".format(
            coords_origin['lat'],
            coords_origin['lng'],
            coords_dest['lat'],
            coords_dest['lng'])

        webbrowser.open(url)

    def mostrarUbicacionEnMapa(self, ubicacion):
        coords = self.ubicacionACoordenadas(ubicacion)
        url = "https://www.google.com.ar/maps/dir/{},{}".format(
            coords['lat'],
            coords['lng'])

        webbrowser.open(url)