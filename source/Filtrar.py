import math

class Filtrar:

	def porDistancia(self, puntoDado, RegistroBares, rango):
		BaresCercanos = [unBar for unBar in RegistroBares if self.distancia(puntoDado, unBar.darUbicacion()) < rango]
		return BaresCercanos

	def distancia(self, puntoDado, ubicacionBar):
		return math.hypot(ubicacionBar[0] - puntoDado[0], ubicacionBar[1] - puntoDado[1])

	def porWifi(self, RegistroBares):
		BaresConWiFi = [unBar for unBar in RegistroBares if unBar.tieneWifi()]
		return BaresConWiFi

	def porCategoria(self, Categoria, RegistroBares, rango):
		BaresAceptados = [unBar for unBar in RegistroBares if self.promedio(Categoria, unBar) >= rango]
		return BaresAceptados

	##### Falta hacer dicha funcion, que no se donde deberia ir. ######
	def promedio(self, Categoria, Bar):
		return 0 

