class RegistrarBar:

	def __init__(self):


	def agregarBar(self, Bar, RegistroBares):
		repetido = buscarBar(Bar, RegistroBares)
		if(!repetido) 
			RegistroBares.push(Bar)
		else sys.stderr.write('Fallo agregarBar: El Bar ya se encuentra en el Sistema')

	def buscarBar(Bar, RegistroBar):
		encontrado = False
		for unBar in RegistroBar:
			if(unBar == Bar) 
				encontrado = true
		return encontrado


	
