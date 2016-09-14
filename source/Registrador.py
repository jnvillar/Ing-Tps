import sys

#TODO: Asserts

class Registrador(object):

	#### Duda: Iniciar Registro de Bares aca, dentro de esta clase
	def registrar(self, dato, registro):
		assert(type(registro) == list)
		repetido = self.buscar(dato, registro)
		#repetido = Bar.darNombre() in [ unBar.darNombre() for unBar in RegistroBares]
		if not repetido :
			registro.append(dato)
		else: sys.stderr.write('Fallo registrar: El Dato ya se encuentra cargado en el Sistema \n')

	def buscar(self, dato, registro):
		for unDato in registro:
			if unDato == dato:
				return True
		return False

	def eliminar(self, dato, registro):
		existe = self.buscar(datoViejo, registro)
		if existe:
			registro.remove(dato)
		else: sys.stderr.write('Fallo eliminar: El Dato no se encuentra cargado en el Sistema \n')

	def modificar(self, datoViejo, datoNuevo, registro):
		existe = self.buscar(datoViejo, registro)
		if existe:
			self.eliminar(datoViejo, registro)
			self.registrar(datoNuevo, registro)
		else: sys.stderr.write('Fallo modificar: El Dato que se intenta modificar no se encuentra cargado en el Sistema \n')

	#def darDato(self, dato, registro):
	#	existe = self.buscar(dato, registro)
	#	if existe:
	#		for unDato in registro:
	#			if unDato == dato:
	#				return unDato
	#	else: sys.stderr.write('Fallo eliminar: El Dato no se encuentra cargado en el Sistema \n')
