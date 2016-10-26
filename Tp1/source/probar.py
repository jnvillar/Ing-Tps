import sys
import os

from Bar import *
from RegistrarBar import *
from Usuario import *
from RegistrarUsuario import *
from Filtrar import *
from Calificaciones import *

if __name__ == "__main__":

	##### crear usuarios

	print '\nCreando usuarios\n'

	user1 = Usuario("Leandro")
	user2 = Usuario("Juani")
	user3 = Usuario("Axel")
	user4 = Usuario("Andy")
	user5 = Usuario("Petr")
	user6 = Usuario("Axel")

	print '\nCreando bares\n'

	#### crear bares
	bar1 = Bar("Super Bar", (1000,1000), True)
	bar2 = Bar("Nuevo Bar", (3,1), True)
	bar3 = Bar("Bar Cool", (1,3), False)
	bar4 = Bar("Nuevo Bar", (-1000,-999), True)
	bar5 = Bar("Nuevo Bar 3", (10,10), True)

	print '\nProbando registros bares y usuarios\n'

	#### probando registros
	regBar = RegistrarBar()
	regUser = RegistrarUsuario()

	RegistroBares = []
	RegistroUsuarios = []

	regBar.agregarBar(bar1, RegistroBares)
	regBar.agregarBar(bar2, RegistroBares)
	regBar.agregarBar(bar4, RegistroBares)
	regBar.agregarBar(bar3, RegistroBares)
	regBar.agregarBar(bar5, RegistroBares)

	regUser.agregarUsuario(user3, RegistroUsuarios)
	regUser.agregarUsuario(user1, RegistroUsuarios)
	regUser.agregarUsuario(user2, RegistroUsuarios)
	regUser.agregarUsuario(user6, RegistroUsuarios)
	regUser.agregarUsuario(user4, RegistroUsuarios)

	print "RegBar[0]:", RegistroBares[0].darNombre()
	print "RegBar[1]:", RegistroBares[1].darNombre()
	print "RegBar[2]:", RegistroBares[2].darNombre()
	print "RegUser[0]:", RegistroUsuarios[0].darNombre()
	print "RegUser[1]:", RegistroUsuarios[1].darNombre()
	print "RegUser[3]:", RegistroUsuarios[3].darNombre()
	print RegistroBares[2].darNombre()

	print '\nTesteando modificar ubicacion\n'

	#testear modificar ubicacion
	print "El usuario", user1.darNombre(), "tiene la siguiente ubicacion:", user1.darUbicacion()
	user1.actualizarUbicacion((3,3))
	print "El usuario", user1.darNombre(), "tiene la siguiente ubicacion:", user1.darUbicacion()

	print '\nProbando filtros\n'

	#### probando filtros
	print "bares a menos de 400m del usuario", user1.darNombre(), "y sin wifi"
	filtrar = Filtrar()
	RegistroBares2 = filtrar.porDistancia(user1.darUbicacion(), RegistroBares, 400)
	RegistroBares2 = filtrar.porWifi(RegistroBares2)
	for unBar in RegistroBares2:
		print unBar.darNombre()

	print '\nProbando calificaciones\n'

	#### probando calificaciones

	contenedor = ContenedorCategorias()
	categoria1 = Categoria("Enchufes")
	categoria2 = Categoria("WiFi")
	contenedor.agregarCategoria(categoria1)
	contenedor.agregarCategoria(categoria2)
	calificacion1 = Calificacion(3, user1)
	calificacion2 = Calificacion(4, user1)
	categoria1.agregarCalificacion(bar1,calificacion1)
	categoria2.agregarCalificacion(bar1,calificacion2)

	for unContenedor in contenedor.verContenedor():
		print unContenedor.darNombre()


	sys.exit(1)