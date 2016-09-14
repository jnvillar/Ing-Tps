from Calificaciones import *

class Directorio(object):
	def __init__(self):
		self.registroBares = []
		self.registroUsuarios = []
		self.registroAdmins = []

		catWiFi = Categoria("WiFi")
		catEnchufes = Categoria("Enchufes")
		self.registroDeCategorias = [catWiFi, catEnchufes]
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
