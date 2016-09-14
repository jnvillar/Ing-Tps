# -*- coding: latin-1 -*-
from Dispacher import *

def accionAgregarBar(app,user):
	nombreBar = raw_input("Nombre del bar: ")
	hayWifi = ""

	tieneWiFi = False
	while not (hayWifi == "Si" or hayWifi == "No"):
		hayWifi = raw_input("Tiene WiFi? (Si/No) ")
		if hayWifi != "Si" and hayWifi != "No":
			print "Elija Si o No."
	puntajeWiFi = 0

	X = int(raw_input("Dònde queda? (X): "))
	Y = int(raw_input("Dònde queda? (Y): "))
	ubicacion = Ubicacion(X, Y)	

	if hayWifi == "Si":
		while (puntajeWiFi < 1 or puntajeWiFi > 5):
			puntajeWiFi = int(input("Calificacion del WiFi (1 a 5): "))
			if puntajeWiFi < 1 or puntajeWiFi > 5:
				print "La calificaciòn debe estar entre 1 y 5"
		tieneWiFi = True

	puntajeEnchufes = 0
	while (puntajeEnchufes < 1 or puntajeEnchufes > 5):
		puntajeEnchufes = int(input("Calificacion de los enchufes (1 a 5): "))
		if puntajeEnchufes < 1 or puntajeEnchufes > 5:
			print "La calificaciòn debe estar entre 1 y 5"


	app.agregarBar(user, nombreBar, ubicacion, tieneWiFi, puntajeWiFi, puntajeEnchufes)

def accionCalificarBar(app,user):
	nombreBar = raw_input("Nombre del bar: ")
	existe = app.buscarBar(nombreBar)
	if not existe:
		print "No existe el bar"
	barCalificar = app.obtenerBar(nombreBar)

	categorias = app.obtenerCategorias()
	print "Elegir Categoria"
	indice = 1
	for cat in categorias:
		print indice, ". ", cat
		indice = indice+1
	categoria = raw_input()
	if app.existeCategoria(categoria):
		categoriaCalificar = app.obtenerCategoria(categoria)
	else:
		print "No existe categoria"
		return

	puntajeBar = input("Calificacion del bar: ")
	# creo aca el objeto calificacion o se hacer despues?
	app.calificarBar(user,barCalificar,categoriaCalificar,puntajeBar)



def accionBuscarBarCercano(app,user):
	app.buscarBaresCercanos(user)



def cicloPrograma(app,user):
	while True:
		print "Elegi accion: \n 1. Agregar Bar \n 2. Calificar Bar \n 3. Buscar Bares a menos de 400m"
		accion = raw_input()
		if accion == "1":
			accionAgregarBar(app,user)
		if accion == "2":
			accionCalificarBar(app,user)
		if accion == "3":
			accionBuscarBarCercano(app,user)



def accionRegistrarUsuario(app):
	while True:
		nombre = raw_input("Nombre de usuario: ")
		existe = app.buscarUsuario(nombre)
		if existe:
			print "Ya existe el nombre"
		else:
			app.registrarUsuario(nombre)
			return




if __name__ == "__main__":
	app = Dispacher()
	while True:
		accion = raw_input("Desea ingresar o registrarse? ")
		if accion == "ingresar":
			nombre = raw_input("Nombre de usuario: ")
			existe = app.buscarUsuario(nombre)
			if existe:
				#contrasena = raw_input("Contrasena: ")
				user = app.obtenerUsuario(nombre)
				cicloPrograma(app,user)
			else:
				print "El usuario ingresado no existe"
		elif accion == "registrar":
			accionRegistrarUsuario(app)
		else:
			print "Accion invalida"
