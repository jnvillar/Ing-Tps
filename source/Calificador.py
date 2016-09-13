from Calificaciones import *

class Calificador():
	def __init__(self, regCalificaciones):
		self.RegistroDeCalificaciones = regCalificaciones

	def calificar(self, bar, usuario, val, categoria):
		calificacionUsuario = Calificacion(usuario,val)

		registroCategoria = Filtrar().
		yaCalifico = RegistroDeCalificaciones.existeCalificacionDeUnUsuario(bar,usuario)
		if yaCalifico:
			RegistroDeCalificaciones.modificarCalificacion(bar,calificacionUsuario)
		else:
			RegistroDeCalificaciones.agregarCalificacion(bar,calificacionUsuario)
