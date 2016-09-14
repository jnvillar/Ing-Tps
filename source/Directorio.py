class Directorio:
	def __init__(self):
		self.registroBares = []
		self.registroUsuarios = []
		self.registroAdmins = []
		self.registroDeCategorias = []
		self.registroDeCalificaciones = []

	def darRegistroBares(self):
		return self.registroBares

	def darRegistroUsuarios(self):
		return self.registroUsuarios

	def darRegistroAdmins(self):
		return self.registroAdmins

	def darRegistroDeCategorias(self):
		return self.registroDeCategorias

	def darRegistroDeCalificaciones(self):
		return self.registroDeCalificaciones
