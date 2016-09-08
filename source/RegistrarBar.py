import sys

class RegistrarBar:

	def agregarBar(self, Bar, RegistroBares):
		repetido = self.buscarBar(Bar, RegistroBares)
		if not repetido : 
			RegistroBares.append(Bar)
		else: sys.stderr.write('Fallo agregarBar: El Bar ya se encuentra en el Sistema \n')

	def buscarBar(self, Bar, RegistroBares):
		encontrado = False
		for unBar in RegistroBares:
			if unBar.darNombre() == Bar.darNombre(): 
				encontrado = True
		return encontrado


	
