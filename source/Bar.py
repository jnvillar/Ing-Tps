class Bar:

	def __init__(self, nombreBar, ubicacionBar, wiFi):
		self.nombre = nombreBar
		self.ubicacion = ubicacionBar
		self.hayWiFi = wiFi
	
	def darNombre(self):
		return self.nombre

	def darUbicacion(self):
		return self.ubicacion

	def tieneWifi(self):
		return self.hayWiFi