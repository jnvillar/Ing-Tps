class RegistrarUsuario:

	def __init__(self):


	def agregarUsuario(self, Usuario, RegistroUsuarios):
		repetido = buscarUsuario(Usuario, RegistroUsuarios)
		if(!repetido) 
			RegistroUsuarios.push(Usuario)
		else sys.stderr.write('Fallo agregarUsuario: El Usuario ya se encuentra registrado en el Sistema')

	def buscarUsuario(Usuario, RegistroUsuario):
		encontrado = False
		for unUsuario in RegistroUsuario:
			if(unUsuario == Usuario) 
				encontrado = true
		return encontrado
