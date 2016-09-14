class Usuario(object):

	def __init__(self, nombreUsuario):
		self.nombre = nombreUsuario
		self.ubicacion = (0,0)

	def __eq__(self, otro):
		#""" Devuelve si dos puntos son iguales. """
		return self.nombre == otro.nombre

	def __ne__(self, otro):
		#""" Devuelve si dos puntos son distintos. """
		return not self == otro

	def darNombre(self):
		return self.nombre

	def darUbicacion(self):
		#	# Actualizar ubicacion
		return self.ubicacion

	def actualizarUbicacion(self, nuevaUbicacion):
		self.ubicacion = nuevaUbicacion
