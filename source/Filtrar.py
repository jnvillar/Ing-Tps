import math

class Filtrar:

	def filtrarPorDistancia(self, distanciaUsuario, RegistroBares, cantDistanciaFiltrar):
		RegistroBares2 = []
		for unBar in RegistroBares:
			dist = math.hypot(unBar.darUbicacion()[0] - distanciaUsuario[0], unBar.darUbicacion()[1] - distanciaUsuario[1])
			if dist < cantDistanciaFiltrar:
				RegistroBares2.append(unBar)

		return RegistroBares2

