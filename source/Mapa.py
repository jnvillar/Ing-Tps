#!/usr/bin/env python
# -*- coding: latin-1 -*-

from Ubicacion import *
from GPS import *

class Mapa(object):

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.gps = GPS()

    def mostrar(self):
        self.gps.mostrarRutaEnMapa(self.origen, self.destino)
