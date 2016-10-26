import math

class Filtrar(object):

	def porDistancia(self, puntoDado, RegistroBares, rango):
		BaresCercanos = [unBar for unBar in RegistroBares if self.distancia(puntoDado, unBar.darUbicacion()) < rango]
		return BaresCercanos

	def distancia(self, puntoDado, ubicacionBar):

		return math.hypot(ubicacionBar.darCoordenadaX() - puntoDado.darCoordenadaX(), ubicacionBar.darCoordenadaY() - puntoDado.darCoordenadaY())

	def porWifi(self, RegistroBares):
		BaresConWiFi = [unBar for unBar in RegistroBares if unBar.tieneWifi()]
		return BaresConWiFi

	def porCategoria(self, Categoria, RegistroBares, rango):
		

	##### Falta hacer dicha funcion, que no se donde deberia ir. ######
	def promedio(self, Categoria, Bar):
		return 0

	def darUsuario(self, nombreUsuario, registroUsuarios):
		usuario = [unUsuario for unUsuario in registroUsuarios if unUsuario.darNombre() == nombreUsuario][0]
		return usuario

	def darBaresConMismoNombre(self, nombreBar, registroBares):
		baresMismoNombre = [unBar for unBar in registroBares if unBar.darNombre() == nombreBar]
		return baresMismoNombre

	def darCategoria(self, nombreCategoria, registroCategorias):
		categoria = [unaCategoria for unaCategoria in registroCategorias if unaCategoria.darNombre() == nombreCategoria][0]
		return categoria	
