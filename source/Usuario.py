class Usuario:

	def __init__(self, nombreUsuario):
		self.nombre = nombreUsuario
		self.ubicacion = 0
	
	def darNombre(self):
		return self.nombre

	def darUbicacion(self):
	#	# Actualizar ubicacion
		return self.ubicacion

	def actualizarUbicacion(self, nuevaUbicacion):
		self.ubicacion = nuevaUbicacion