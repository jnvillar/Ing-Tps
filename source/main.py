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

	tieneWifi = cambiarSNPorTrueFalse(raw_input("Tiene WiFi? (s/n) "))

	ubicacion = insertarUbicacionBar()

	if tieneWifi:
		puntajeWiFi = insertarPuntuacion("Calificacion del WiFi (1 a 5): ")
		puntajes.append(puntajeWiFi)

	puntajeEnchufes = insertarPuntuacion("Calificación de los enchufes (1 a 5): ")
	puntajes.append(puntajeEnchufes)

	nuevoBar = Bar(nombreBar, ubicacion, tieneWifi)
	app.agregarBar(user,nuevoBar, puntajes)
	print "Bar agregado \n"

def accionCalificarBar(app,user):

	nombreBar = raw_input("Nombre del bar: ")
	baresMismoNombre = app.obtenerBaresMismoNombre(nombreBar)
	
	if len(baresMismoNombre) == 0:
		print "No existe el bar \n"
		return
	visualizarBares(baresMismoNombre)
	eleccion = esValorValido(0,len(baresMismoNombre)-1,"Ingrese indice de bar deseado: ")

	barCalificar = baresMismoNombre[eleccion]
	tieneInternet = barCalificar.tieneWifi()
	quieroCalificarCategoria = True
	categorias = app.obtenerCategorias()
	if not tieneInternet:
		del categorias[0]

	while quieroCalificarCategoria:
		print "Elegir Categoria"
		visualizarCategorias(categorias)
	
		eleccion = esValorValido(0,len(categorias)-1,"Ingrese Categoria deseada:")
		categoriaCalificar = categorias[eleccion]

		puntajeBar = insertarPuntuacion("Puntaje (1-5): ")

		# creo aca el objeto calificacion o se hacer despues?
		app.calificarBar(user,barCalificar,categoriaCalificar,puntajeBar)

		quieroCalificarCategoria = cambiarSNPorTrueFalse(raw_input("Queres calificar otra categoria de este bar? (s/n): "))

	print "Calificacion realizada \n"

def accionBuscarBarCercano400(app):
	puntoDado = insertarUbicacionUsuario()
	baresCercanos = app.buscarBaresCercanos(puntoDado,400)
	if len(baresCercanos) == 0:
		print "No hay bares Cercanos \n"
		return
	visualizarBares(baresCercanos)

def accionBuscarBarCercano(app):
	puntoDado = insertarUbicacionUsuario()
	distancia = int(raw_input("Dame Distancia: "))

	baresCercanos = app.buscarBaresCercanos(puntoDado,distancia)
	if len(baresCercanos) == 0:
		print "No hay bares Cercanos \n"
		return
	visualizarBares(baresCercanos)

def accionFiltrarBaresVariosCriterios(app):
	ListaCategorias = app.obtenerCategorias()
	print "Criterios Disponibles \n"
	visualizarCriterios(ListaCategorias)

	masCriterios = True
	filtros = []
	cantidadDeCriterios = len(ListaCategorias) + 2
	while (masCriterios):
		criterio = esValorValido(0,cantidadDeCriterios-1,"Ingrese Criterio:")
		if criterio == 0:
			distancia = int(raw_input("Ingrese Distancia:"))
			puntoDado = insertarUbicacionUsuario()
			filtros = filtros + [FiltroPorDistancia(distancia,puntoDado)]
		elif criterio == 1:
			filtros = filtros + [FiltroPorWiFi()]
		else:
			rango = int(raw_input("Ingrese calificacion Minima:")) #hay que chequear que el rango sea valido
			filtros = filtros + [FiltroPorCategoria(ListaCategorias[criterio-2],rango)]
		masCriterios = cambiarSNPorTrueFalse(raw_input("Desea agregar otro criterio? s/n: "))
	
	baresFiltrados = app.filtrarBaresVariosCriterios(filtros)

	if len(baresFiltrados) == 0:
		print "No hay bares con los filtros establecidos \n"
		return
	visualizarBares(baresFiltrados)

		
def cambiarSNPorTrueFalse(entrada):
	if entrada == "s":
		return True
	elif entrada == "n":
		return False
	else: 
		return cambiarSNPorTrueFalse(raw_input("Valor incorrecto, reintente con s/n: "))

def insertarUbicacionBar():
	X = int(raw_input("Dónde queda? (X): "))
	Y = int(raw_input("Dónde queda? (Y): "))
	ubicacion = Ubicacion(X, Y)
	return ubicacion

def insertarUbicacionUsuario():
	X = int(raw_input("Dame tu posición (X): "))
	Y = int(raw_input("Dame tu posición (Y): "))
	ubicacion = Ubicacion(X, Y)
	return ubicacion

def insertarPuntuacion(string):
	puntaje = 0
	while (puntaje < 1 or puntaje > 5):
		puntaje = int(input(string))
		if puntaje < 1 or puntaje > 5:
			print "La calificaciòn debe estar entre 1 y 5"
	return puntaje

def visualizarBares(listaBares):
	i = 0
	for unBar in listaBares:
		print i,". ","Bar: ", unBar.darNombre(), "Ubicacion: ", unBar.darUbicacion(), "Tiene WiFi: ", unBar.tieneWifi()
		i=i+1
	print "\n"

def visualizarCategorias(categorias):
	indice = 0
	for cat in categorias:
		print indice, ". ", cat.darNombre()
		indice = indice+1
	print "\n"

def visualizarCriterios(categorias):
	print "0 .  Distancia"
	print "1 .  Disponibilidad de WiFi"
	i = 2
	for categoria in categorias:		
		print i,". ","Categoria:  ",categoria.darNombre() 
		i += 1
	print "\n"


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
