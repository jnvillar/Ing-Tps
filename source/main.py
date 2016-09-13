from Aplicacion.py import *


def accionAgregarBar(app,user):
	nombreBar = raw_input("Nombre del bar: ")
	existe = app.buscarBar(nombreBar)
	if existe:
		print "Ya existe el bar"
		return
	hayWifi = raw_input("Tiene WiFi? ")
	puntajeWiFi = 0
	if hayWifi == "Si":
		puntajeWiFi = input("Calificacion del WiFi: ")

	puntajeEnchufes = input("Calificacion de los enchufes: ")

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



def accionBuscarBar(app,user):
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
			accionBuscarBar(app,user)

if __name__ == "__main__":
	app = Aplicacion()
	while True:
		nombre = raw_input("Nombre de usuario: ")
		existe = app.buscarUsuario(nombre)
		if existe:
			#contrasena = raw_input("Contrasena: ")
			user = obtenerUsuario(nombre)
			cicloPrograma(app,user)
		


