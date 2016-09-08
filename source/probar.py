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

	RegistroBares = []
	RegistroUsuarios = []

	agregarBar(bar1, RegistroBares)
	agregarBar(bar2, RegistroBares)
	agregarBar(bar4, RegistroBares)
	agregarBar(bar3, RegistroBares)

	agregarUsuario(user3, RegistroUsuarios)
	agregarUsuario(user1, RegistroUsuarios)
	agregarUsuario(user2, RegistroUsuarios)
	agregarUsuario(user6, RegistroUsuarios)
	agregarUsuario(user4, RegistroUsuarios)

	print "RegBar[0]:", RegistroBares[0].nombre
	print "RegBar[1]:", RegistroBares[1].nombre
	print "RegBar[2]:", RegistroBares[2].nombre
	print "RegUser[0]:", RegistroUsuarios[0].nombre
	print "RegUser[1]:", RegistroUsuarios[1].nombre
	print "RegUser[3]:", RegistroUsuarios[3].nombre
	#print RegistroBares[3].nombre

	#testear modificar ubicacion
	print "El usuario", user1.nombre, "tiene la siguiente ubicacion:", user1.ubicacion
	user1.ubicacion = 3
	print "El usuario", user1.nombre, "tiene la siguiente ubicacion:", user1.ubicacion

	sys.exit(1)