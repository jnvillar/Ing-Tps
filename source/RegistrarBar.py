class RegistrarBar:

	def __init__(self):


	def agregarBar(self, Bar, RegistroBares):
		repetido = buscarBar(Bar, RegistroBares)
		if(!repetido) RegistroBares.push(Bar)

	
