import sys

def agregarUsuario(Usuario, RegistroUsuarios):
	repetido = buscarUsuario(Usuario, RegistroUsuarios)
	if not repetido: 
		RegistroUsuarios.append(Usuario)
	else: sys.stderr.write('Fallo agregarUsuario: El Usuario ya se encuentra registrado en el Sistema \n')

def buscarUsuario(Usuario, RegistroUsuario):
	encontrado = False
	for unUsuario in RegistroUsuario:
		if unUsuario.nombre == Usuario.nombre : 
			encontrado = True
	return encontrado
