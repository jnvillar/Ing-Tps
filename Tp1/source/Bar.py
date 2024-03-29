from Ubicacion import *

class Bar(object):

	def __init__(self, nombreBar, ubicacionBar, wiFi):
		assert(type(ubicacionBar) == Ubicacion and type(wiFi) == bool and type(nombreBar) ==  str)
		self.nombre = nombreBar
		self.ubicacion = ubicacionBar
		self.hayWiFi = wiFi

	def __eq__ (self, otro):
		return self.nombre == otro.nombre and self.ubicacion == otro.ubicacion

	def __ne__(self, otro):
    		#""" Devuelve si dos puntos son distintos. """
    		return not self == otro

	def darNombre(self):
		return self.nombre

	def darUbicacion(self):
		return self.ubicacion

	def tieneWifi(self):
		return self.hayWiFi
