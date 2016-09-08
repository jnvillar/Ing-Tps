import sys
import os

from Bar import *
from RegistrarBar import *
from Usuario import *
from RegistrarUsuario import *

if __name__ == "__main__":

	user1 = Usuario("Leandro")
	user2 = Usuario("Juani")
	user3 = Usuario("Axel")
	user4 = Usuario("Andy")
	user5 = Usuario("Petr")
	user6 = Usuario("Axel")

	bar1 = Bar("Super Bar", 3, True)
	bar2 = Bar("Nuevo Bar", 2, True)
	bar3 = Bar("Bar Cool", 1, False)
	bar4 = Bar("Nuevo Bar", 55, True)

	regBar = RegistrarBar()
	regUser = RegistrarUsuario()

	RegistroBares = []
	RegistroUsuarios = []

	regBar.agregarBar(bar1, RegistroBares)
	regBar.agregarBar(bar2, RegistroBares)
	regBar.agregarBar(bar4, RegistroBares)
	regBar.agregarBar(bar3, RegistroBares)

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
	#print RegistroBares[2].darNombre()

	#testear modificar ubicacion
	print "El usuario", user1.darNombre(), "tiene la siguiente ubicacion:", user1.darUbicacion()
	user1.actualizarUbicacion(3)
	print "El usuario", user1.darNombre(), "tiene la siguiente ubicacion:", user1.darUbicacion()

	print bar1.darNombre()
	print bar1.darUbicacion()
	print bar1.tieneWifi()

	sys.exit(1)