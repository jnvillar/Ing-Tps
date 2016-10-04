import math
from GPS import *

class Filtrador:

	def filtrarBares(self, directorio,listaDeFiltros):		
		baresFiltrados =  directorio.darRegistroBares()
		for filtro in listaDeFiltros:			
			baresFiltrados = filtro.aplicarFiltro(baresFiltrados,directorio)
		return baresFiltrados 

	def buscar(self, registro,filtro):		
		elementoBuscado = filtro.aplicarFiltro(registro)
		return elementoBuscado

class Filtro:
	def aplicarFiltro(self,lista,directorio):  
		raise NotImplementedError("es una clase abstracta")

class FiltroBares(Filtro):
	def aplicarFiltro(self,lista,directorio):  
		raise NotImplementedError("es una clase abstracta")

class FiltroPorDistancia(FiltroBares):
	def __init__(self,distancia,ubicacionDadaPorElUsuario):
		self.distanciaMaxima = distancia
		self.punto = ubicacionDadaPorElUsuario

	def aplicarFiltro(self, listaBares,directorio):
		gps = GPS()
		BaresCercanos = [unBar for unBar in listaBares if gps.distanciaEntre(self.punto, unBar.darUbicacion()) < self.distanciaMaxima]
		return BaresCercanos
	
class FiltroPorWiFi(FiltroBares):
	def aplicarFiltro(self, listaBares,directorio):
		BaresConWiFi = [unBar for unBar in listaBares if unBar.tieneWifi()]
		return BaresConWiFi

class FiltroNombreBares(FiltroBares):
	def __init__(self,nombreDelBar):
		self.nombreBar = nombreDelBar

	def aplicarFiltro(self, listaBares, directorio):	
		baresMismoNombre = [unBar for unBar in listaBares if unBar.darNombre() == self.nombreBar]
		return baresMismoNombre

class FiltroPorCategoria(FiltroBares):
	def __init__(self,cat,rang):
		self.categoria = cat
		self.rango = rang
	
	def aplicarFiltro(self, listaBares,directorio):
		BaresAceptados = [unBar for unBar in listaBares if self.promedio(self.categoria, unBar, directorio.darRegistroDeCalificaciones()) >= self.rango]
		return BaresAceptados

	def promedio(self, categoria, bar, registroCalificaciones):
		sumaParcial = 0
		cantidadCalificaciones = 0
		for calificacion in registroCalificaciones:
			if calificacion.darBar() == bar and calificacion.darCategoria() == categoria:
				sumaParcial = sumaParcial+calificacion.darValor()
				cantidadCalificaciones = cantidadCalificaciones + 1

		return sumaParcial / max(1,cantidadCalificaciones)

class FiltroNombreCategoria(Filtro):
	def __init__(self,nombreDeLaCategoria):
		self.nombreCategoria = nombreDeLaCategoria

	def aplicarFiltro(self, registroCategorias):
		categoria = [unaCategoria for unaCategoria in registroCategorias if unaCategoria.darNombre() == self.nombreCategoria][0]
		return categoria	

class FiltroNombreUsuario(Filtro):
	def __init__(self,nombreDelUsuario):
		self.nombreUsuario = nombreDelUsuario

	def aplicarFiltro(self, registroUsuarios):
		usuario = [unUsuario for unUsuario in registroUsuarios if unUsuario.darNombre() == self.nombreUsuario][0]
		return usuario

