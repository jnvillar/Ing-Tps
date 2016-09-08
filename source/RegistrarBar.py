import sys

def agregarBar(Bar, RegistroBares):
	repetido = buscarBar(Bar, RegistroBares)
	if not repetido : 
		RegistroBares.append(Bar)
	else: sys.stderr.write('Fallo agregarBar: El Bar ya se encuentra en el Sistema \n')

def buscarBar(Bar, RegistroBares):
	encontrado = False
	for unBar in RegistroBares:
		if unBar.nombre == Bar.nombre: 
			encontrado = True
	return encontrado


	
