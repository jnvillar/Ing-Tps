# -*- coding: latin-1 -*-
from Dispacher import *

def accionRegistrarUsuario(app):
	while True:
		nombre = raw_input("Nombre de usuario: ")
		existe = app.buscarUsuario(nombre)
		if existe:
			print "Ya existe el nombre"
		else:
			app.registrarUsuario(nombre)
			return

def accionAgregarBar(app,user):
	puntajes = []
	nombreBar = raw_input("Nombre del bar: ")
	tieneWifi = cambiarSNPorTrueFalse(raw_input("Tiene WiFi? (s/n) "))
	ubicacion = insertarUbicacion("Ingrese Dirección del Bar: ")

	if tieneWifi:
		puntajeWiFi = insertarPuntuacion("Calificación del WiFi (1 a 5): ")
		puntajes.append(puntajeWiFi)

	puntajeEnchufes = insertarPuntuacion("Calificación de los enchufes (1 a 5): ")
	puntajes.append(puntajeEnchufes)
	nuevoBar = Bar(nombreBar, ubicacion, tieneWifi)
	app.agregarBar(user,nuevoBar, puntajes)
	print "Bar agregado \n"

def accionCalificarBar(app,user):
	nombreBar = raw_input("Ingrese Nombre del Bar: ")
	if esListaVacia(app.obtenerBaresMismoNombre(nombreBar),"No existe el bar \n"):
		return
	barCalificar = obtenerBar(nombreBar)
	tieneInternet = barCalificar.tieneWifi()
	categorias = app.obtenerCategorias()
	if not tieneInternet:
		del categorias[0]

	quieroCalificarCategoria = True
	while quieroCalificarCategoria:
		print "Elegir Categoría"
		visualizarCategorias(categorias)
		eleccion = esValorValido(0, len(categorias)-1, "Ingrese Categoría deseada: ")
		categoriaCalificar = categorias[eleccion]
		puntajeBar = insertarPuntuacion("Puntaje (1-5): ")
		app.calificarBar(user, barCalificar, categoriaCalificar, puntajeBar)
		quieroCalificarCategoria = cambiarSNPorTrueFalse(raw_input("Querés calificar otra categoría de este bar? (s/n): "))

	print "Calificación realizada \n"

def accionBuscarBarCercano400(app,user):
	direccionDadaPorElUsuario = queUbicacionUsar(user)
	baresCercanos = app.buscarBaresCercanos(direccionDadaPorElUsuario,400)
	if esListaVacia(baresCercanos,"No hay bares a menos de esa distancia \n"):
		return
	visualizarBares(baresCercanos)

def accionBuscarBarCercano(app):
	direccionDadaPorElUsuario = queUbicacionUsar(user)
	distancia = int(raw_input("Dame Distancia: "))
	baresCercanos = app.buscarBaresCercanos(direccionDadaPorElUsuario,distancia)
	if esListaVacia(baresCercanos,"No hay bares a menos de esa distancia \n"):
		return
	visualizarBares(baresCercanos)

def accionFiltrarBaresVariosCriterios(app):
	ListaCategorias = app.obtenerCategorias()
	print "Criterios Disponibles \n"
	visualizarCriterios(ListaCategorias)
	cantidadDeCriterios = len(ListaCategorias) + 2
	filtros = []
	masCriterios = True
	while (masCriterios):
		criterio = esValorValido(0,cantidadDeCriterios-1,"Ingrese Criterio: ")
		if criterio == 0:
			distancia = int(raw_input("Ingrese Distancia: "))
			puntoDado = insertarUbicacion("Ingrese la dirección deseada: ")
			filtros = filtros + [FiltroPorDistancia(distancia,puntoDado)]
		elif criterio == 1:
			filtros = filtros + [FiltroPorWiFi()]
		else:
			rango = int(raw_input("Ingrese calificación mínima: ")) #hay que chequear que el rango sea valido
			filtros = filtros + [FiltroPorCategoria(ListaCategorias[criterio-2],rango)]
		masCriterios = cambiarSNPorTrueFalse(raw_input("Desea agregar otro criterio? s/n:  "))

	baresFiltrados = app.filtrarBaresVariosCriterios(filtros)
	if esListaVacia(baresFiltrados,"No hay bares que cumplan con los criterios ingresados \n"):
		return
	visualizarBares(baresFiltrados)

def queUbicacionUsar(user):
	utilizarUbicacionUsuario = cambiarSNPorTrueFalse(raw_input("Desea usar su ubicación o utilizar otra?: (s/n) "))
	if utilizarUbicacionUsuario:
		return user.darUbicacion()
	direccion = insertarUbicacion("Ingrese su Dirección: ")
	return direccion

def cambiarSNPorTrueFalse(entrada):
	if entrada == "s":
		return True
	elif entrada == "n":
		return False
	else:
		return cambiarSNPorTrueFalse(raw_input("Valor incorrecto, reintente con s/n: "))

def insertarUbicacion(texto):
	direccion = raw_input(texto)
	ubicacion = Ubicacion(direccion)
	return ubicacion

def esListaVacia(lista,texto):
	if len(lista) == 0:
		print texto
		return True
	return False

def insertarPuntuacion(string):
	puntaje = 0
	while (puntaje < 1 or puntaje > 5):
		puntaje = int(input(string))
		if puntaje < 1 or puntaje > 5:
			print "La calificación debe estar entre 1 y 5"
	return puntaje

def visualizarCategorias(categorias):
	indice = 0
	for cat in categorias:
		print indice, ". ", cat.darNombre()
		indice = indice+1

def esValorValido(menorA,mayorA,string):
	Valido = True
	while(Valido):
		eleccion = int(raw_input(string))
		if eleccion>=menorA and eleccion<=mayorA:
			Valido = False
		else:
			print "Valor no válido, por favor intente de nuevo: "
	return eleccion

def visualizarCriterios(categorias):
	print "0 .  Distancia"
	print "1 .  Disponibilidad de WiFi"
	i = 2
	for categoria in categorias:
		print i,". ","Categoría:  ",categoria.darNombre()
		i += 1
	print "\n"

def obtenerBar(nombreBar):
	baresMismoNombre = app.obtenerBaresMismoNombre(nombreBar)
	if(esListaVacia(baresMismoNombre,"No existe el bar \n")):
		return -1
	visualizarBares(baresMismoNombre)
	eleccion = esValorValido(0,len(baresMismoNombre)-1,"Ingrese índice de bar deseado: ")
	bar = baresMismoNombre[eleccion]
	return bar

def accionActualizarUbicacionUsuario(app,user):
	direccion = insertarUbicacion("Ingrese su Ubicación: ")
	user.actualizarUbicacion(direccion)

def accionBuscarBar(app, user):
    nombreBar = raw_input("Ingrese Nombre del Bar: ")
    if esListaVacia(app.obtenerBaresMismoNombre(nombreBar), "No existe el bar \n"):
        return
    bar = obtenerBar(nombreBar)
    visualizarBares([bar])
    visualizarCalificacionesDeUnBar(app, bar)

def visualizarBares(listaBares):
    i = 0
    for unBar in listaBares:
        print i,". ","Bar: ", unBar.darNombre(), "Ubicación: ", unBar.darUbicacion(), "Tiene WiFi: ", unBar.tieneWifi()
        i = i+1
    print "\n"

def visualizarCalificacionesDeUnBar(app, bar):
	listaCalificaciones = app.obtenerCalificaciones(bar)
	i=0
	for unaCalificacion in listaCalificaciones:
		if unaCalificacion.darBar() == bar:
			print i,". ",  "Valor: ", unaCalificacion.darValor(),"Cat: ", unaCalificacion.darCategoria().darNombre(), "Usuario: " , unaCalificacion.darUsuario().darNombre()
			i+=1
	print "\n"

def seleccionarBar(app,user,bar):
	visualizarBares[bar]
	verInfoLocalizacion = True
	while verInfoLocalizacion:
		print "1. Ver Ubicacion del Bar en el mapa. \n 2. Ver ruta hacia el bar. \n 3. Salir"
		eleccion = esValorValido(1, 3, "Ingrese su eleccion: ")
		if eleccion==1:
			app.mostrarUbicacion(bar.darUbicacion())
		elif eleccion == 2:
			direccion = queUbicacionUsar(user)
			app.mostrarRuta(direccion, bar.darUbicacion())
		elif eleccion == 3:
			return
		
		verInfoLocalizacion = cambiarSNPorTrueFalse(raw_input("Desea volver a seleccionar el bar?: (s/n)"))

def cicloPrograma(app,user):
	seguir = True
	while seguir:
		print "Elegí acción: \n 1. Agregar Bar \n 2. Calificar Bar \n 3. Buscar Bares a menos de 400m \n 4. Buscar Bares a menos de una distancia dada \n 5. Filtrar Bares por varios criterios \n 6. Ingresar su Ubicacion \n 7. Buscar Bar \n d. Desloguearse\n q. Salir del Programa\n"
		accion = raw_input()
		if accion == "1":
			accionAgregarBar(app,user)
		if accion == "2":
			accionCalificarBar(app,user)
		if accion == "3":
			accionBuscarBarCercano400(app,user)
		if accion == "4":
			accionBuscarBarCercano(app)
		if accion == "5":
			accionFiltrarBaresVariosCriterios(app)
		if accion == "6":
			accionActualizarUbicacionUsuario(app,user)
		if accion == "7":
			accionBuscarBar(app,user)
		if accion == "d":
			seguir = False
		if accion == "q":
			exit(0)

if __name__ == "__main__":
	app = Dispacher()
	app.agregarCategoria("WiFi")
	app.agregarCategoria("Enchufes")
	app.agregarCategoria("Baños")
	app.agregarCategoria("Comida")
	app.agregarCategoria("Atencion")
	app.agregarCategoria("Precios")
	app.agregarCategoria("Cerveza")
	while True:
		accion = raw_input("Desea ingresar o registrarse? i/r, q para salir ")
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
			print "Accion inválida"
