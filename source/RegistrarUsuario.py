import sys

class RegistrarUsuario:

	def agregarUsuario(self, Usuario, RegistroUsuarios):
		repetido = self.buscarUsuario(Usuario, RegistroUsuarios)
		if not repetido: 
			RegistroUsuarios.append(Usuario)
		else: sys.stderr.write('Fallo agregarUsuario: El Usuario ya se encuentra registrado en el Sistema \n')

	def buscarUsuario(self, Usuario, RegistroUsuario):
		encontrado = False
		for unUsuario in RegistroUsuario:
			if unUsuario.darNombre() == Usuario.darNombre() : 
				encontrado = True
		return encontrado
