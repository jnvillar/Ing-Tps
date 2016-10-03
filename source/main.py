# -*- coding: latin-1 -*-
from Dispacher import *

def esValorValido(menorA,mayorA,string):
	Valido = True
	while(Valido):
		eleccion = int(raw_input(string))
		if eleccion>=menorA and eleccion<=mayorA:
			Valido = False
		else:
			print "Valor no Valido, por favor intente de nuevo\n"
	return eleccion

def accionAgregarBar(app,user):
	puntajes = []
	nombreBar = raw_input("Nombre del bar: ")
	hayWifi = ""

	tieneWiFi = False
	while not (hayWifi == "s" or hayWifi == "n"):
		hayWifi = raw_input("Tiene WiFi? (s/n) ")
		if hayWifi != "s" and hayWifi != "n":
			print "Elija s o n."
	puntajeWiFi = 0

	X = int(raw_input("Dònde queda? (X): "))
	Y = int(raw_input("Dònde queda? (Y): "))
	ubicacion = Ubicacion(X, Y)

	if hayWifi == "s":
		while (puntajeWiFi < 1 or puntajeWiFi > 5):
			puntajeWiFi = int(input("Calificacion del WiFi (1 a 5): "))
			if puntajeWiFi < 1 or puntajeWiFi > 5:
				print "La calificaciòn debe estar entre 1 y 5"
		tieneWiFi = True
		puntajes.append(puntajeWiFi)

	puntajeEnchufes = 0
	while (puntajeEnchufes < 1 or puntajeEnchufes > 5):
		puntajeEnchufes = int(input("Calificación de los enchufes (1 a 5): "))
		if puntajeEnchufes < 1 or puntajeEnchufes > 5:
			print "La calificación debe estar entre 1 y 5"

	puntajes.append(puntajeEnchufes)

	nuevoBar = Bar(nombreBar, ubicacion, tieneWiFi)
	app.agregarBar(user,nuevoBar, puntajes)
	print "Bar agregado \n"

def accionCalificarBar(app,user):

	nombreBar = raw_input("Nombre del bar: ")
	baresMismoNombre = app.obtenerBaresMismoNombre(nombreBar)
	existe = len(baresMismoNombre) > 0
	if not existe:
		print "No existe el bar \n"
		return
	i = 0
	for unBar in baresMismoNombre:
		print i,". ","Bar: ", unBar.darNombre(), " -- Ubicacion: ", unBar.darUbicacion(), " -- Tiene WiFi: ", unBar.tieneWifi()
		i=i+1

	valorValido = True
	while(valorValido):
		eleccion = int(raw_input("Ingrese indice de bar deseado: "))
		if eleccion>=len(baresMismoNombre) or eleccion<0:
			print "Valor no Valido, por favor intente de nuevo\n"
		else:
			valorValido = False

	barCalificar = baresMismoNombre[eleccion]
	tieneInternet = barCalificar.tieneWifi()
	quieroCalificarCategoria = True
	categorias = app.obtenerCategorias()
	if not tieneInternet:
		del categorias[0]

	while quieroCalificarCategoria:

		
		print "Elegir Categoria"
		indice = 0

		for cat in categorias:
			print indice, ". ", cat.darNombre()
			indice = indice+1
	
		esValorValido(0,len(categorias)-1,"Ingrese Categoria deseada:")
		categoriaCalificar = categorias[eleccion]

		puntajeBar = input("Puntaje (1-5): ")
		
		# creo aca el objeto calificacion o se hacer despues?
		app.calificarBar(user,barCalificar,categoriaCalificar,puntajeBar)

		decision = ""

		while not (decision == "s" or decision == "n"):
			decision = raw_input("Queres calificar otra categoria de este bar? (s/n): ")
			if decision != "s" and decision != "n":
				print "Elija s o n."

		if decision == "n" : quieroCalificarCategoria = False



	#if app.existeCategoria(categoria):
	#	categoriaCalificar = app.obtenerCategoria(categoria)
	#else:
	#	print "No existe categoria"
	#	return





def accionBuscarBarCercano400(app):
	X = int(raw_input("Dame tu posición (X): "))
	Y = int(raw_input("Dame tu posición (Y): "))
	puntoDado = Ubicacion(X, Y)
	baresCercanos = app.buscarBaresCercanos(puntoDado,400)
	if len(baresCercanos) == 0:
		print "No hay bares Cercanos \n"
		return
	i = 0
	for unBar in baresCercanos:
		print i,". ","Bar: ", unBar.darNombre(), "Ubicacion: ", unBar.darUbicacion(), "Tiene WiFi: ", unBar.tieneWifi()
		i=i+1

def accionBuscarBarCercano(app):
	X = int(raw_input("Dame tu posición (X): "))
	Y = int(raw_input("Dame tu posición (Y): "))
	distancia = int(raw_input("Dame Distancia: "))
	puntoDado = Ubicacion(X, Y)

	baresCercanos = app.buscarBaresCercanos(puntoDado,distancia)
	if len(baresCercanos) == 0:
		print "No hay bares Cercanos \n"
		return
	i = 0
	for unBar in baresCercanos:
		print i,". ","Bar: ", unBar.darNombre(), "Ubicacion: ", unBar.darUbicacion(), "Tiene WiFi: ", unBar.tieneWifi()
		i=i+1

def accionFiltrarBaresVariosCriterios(app):
	print "Criterios Disponibles \n"
	print "0. Distancia \n"
	print "1. Disponibilidad de WiFi \n"
	i = 2
	ListaCategorias = app.obtenerCategorias()
	for categoria in ListaCategorias:		
		print i,". ","Categoria:  ",categoria.darNombre(),"\n" 
		i += 1

	masCriterios = True
	filtros = []
	while (masCriterios):
		criterio = int(raw_input("Ingrese Criterio:"))
		if criterio == 0:
			distancia = int(raw_input("Ingrese Distancia:"))
			X = int(raw_input("Dame tu posición (X): "))
			Y = int(raw_input("Dame tu posición (Y): "))
			puntoDado = Ubicacion(X, Y)
			filtros = filtros + [FiltroPorDistancia(distancia,puntoDado)]
		elif criterio == 1:
			filtros = filtros + [FiltroPorWiFi()]
		else:
			rango = int(raw_input("Ingrese calificacion Minima:"))
			filtros = filtros + [FiltroPorCategoria(ListaCategorias[criterio-2],rango)]
		masCriterios = cambiarSNPorTrueFalse(raw_input("Desea agregar otro criterio? s/n: "))
	
	baresFiltrados = app.filtrarBaresVariosCriterios(filtros)

	if len(baresFiltrados) == 0:
		print "No hay bares con los filtros establecidos \n"
		return
	i = 0
	for unBar in baresFiltrados:
		print i,". ","Bar: ", unBar.darNombre(), "Ubicacion: ", unBar.darUbicacion(), "Tiene WiFi: ", unBar.tieneWifi()
		i=i+1
		
def cambiarSNPorTrueFalse(entrada):
	if entrada == "s":
		return True
	elif entrada == "n":
		return False
	else: cambiarSNPorTrueFalse(raw_input("Valor incorrecto, reintente con s/n: "))
		



def cicloPrograma(app,user):
	seguir = True
	while seguir:
		print "Elegi accion: \n 1. Agregar Bar \n 2. Calificar Bar \n 3. Buscar Bares a menos de 400m \n 4. Buscar Bares a menos de una distancia dada \n 5. Filtrar Bares por varios criterios \n d. Desloguearse\n q. Salir del Programa\n"
		accion = raw_input()
		if accion == "1":
			accionAgregarBar(app,user)
		if accion == "2":
			accionCalificarBar(app,user)
		if accion == "3":
			accionBuscarBarCercano400(app)
		if accion == "4":
			accionBuscarBarCercano(app)
		if accion == "5":
			accionFiltrarBaresVariosCriterios(app)
		if accion == "d":
			seguir = False
		if accion == "q":
			exit(0)





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
		accion = raw_input("Desea ingresar o registrarse?  Presione q para salir ")
		if accion == "i":
			nombre = raw_input("Nombre de usuario: ")
			existe = app.buscarUsuario(nombre)
			if existe:
				#contrasena = raw_input("Contrasena: ")
				user = app.obtenerUsuario(nombre)
				cicloPrograma(app,user)
			else:
				print "El usuario ingresado no existe"
		elif accion == "r":
			accionRegistrarUsuario(app)

		elif accion == "q":
			print "Gracias por usar la App"
			exit(0)

		else:
			print "Accion invalida"
