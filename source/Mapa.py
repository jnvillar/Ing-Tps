#!/usr/bin/env python
# -*- coding: latin-1 -*-

import cv2
import numpy as np
import urllib
from motionless import *
from Ubicacion import *
import webbrowser

class Mapa(object):
    def __init__(self, ubi):
        self.dmap = DecoratedMap()
        self.dmap.add_marker(LatLonMarker(lat=ubi.darCoordenadaX(), lon=ubi.darCoordenadaY(), label='B'))

    def mostrar(self):
        url = self.dmap.generate_url()
        # Si se quisiera abrir con el navegador
        # webbrowser.open(url)

        # Abrir con OpenCV.
        # Experimental. Mejor sería usar el browser
        req = urllib.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)

        while True:
            cv2.imshow('Ubicacion en mapa', img)
            if cv2.waitKey(100) == 27:
                break
