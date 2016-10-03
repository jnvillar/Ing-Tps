#!/usr/bin/env python
# -*- coding: latin-1 -*-

import cv2
import numpy as np
import urllib
from motionless import *

# Api key de Andy para static maps
# AIzaSyCIbENEL7DDZRXa0HgCENU5sXhcXHvWS2s

# Usar motionless para generar la url
# https://github.com/ryancox/motionless

# Style
road_styles = [{
    'feature': 'road.highway',
    'element': 'geomoetry',
    'rules': {
        'visibility': 'simplified',
        'color': '#c280e9'
    }
}, {
    'feature': 'transit.line',
    'rules': {
        'visibility': 'simplified',
        'color': '#bababa'
    }
}]

dmap = DecoratedMap(style=road_styles)
dmap.add_marker(LatLonMarker(lat=48.858278, lon=2.294489, label='A'))
#dmap.add_marker(AddressMarker('Obelisco, Buenos Aires, Argentina',label='A'))
#dmap.add_marker(AddressMarker('1600 Amphitheatre Parkway Mountain View, CA',label='G'))
url = dmap.generate_url()

# Luego abrirla y pasarla a OpenCV
req = urllib.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'load it as it is'

while not cv2.waitKey() & 0xff == 27:
    cv2.imshow('Ubicacion en mapa',img)
