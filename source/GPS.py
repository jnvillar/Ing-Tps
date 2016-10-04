#!/usr/bin/env python
# -*- coding: latin-1 -*-

import urllib
import googlemaps
import webbrowser
from Ubicacion import *

class GPS(object):
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyCYMZgZTgYwc2CeJy37REmBjTevjDPBKHA')

    def distanciaEntre(origen, destino):
        # Expresada en metros
        directions_result = self.gmaps.directions(origen.darDireccion(),
                                     destino.darDireccion(),
                                     mode="walking",
                                     alternatives= False)

        return directions_result[0]['legs'][0]['distance']['value']

    #def address2coord(self, direccion):
        #return self.gmaps.geocode(direccion)[0]['geometry']['location']

    def mostrarRutaEnMapa(origen, destino):

        coords_origin = self.address2coord(origen.darDireccion())
        coords_dest = self.address2coord(destino.darDireccion())

        url = "https://www.google.com.ar/maps/dir/{},{}/{},{}".format(
            coords_origin['lat'],
            coords_origin['lng'],
            coords_dest['lat'],
            coords_dest['lng'])

        webbrowser.open(url)
