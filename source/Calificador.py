class Calificador():
	def __init__(self, regCalificaciones):
		self.RegistroDeCalificaciones = regCalificaciones


	def Calificar(self,bar,usuario,val):
		calificacionUsuario = Calificacion(usuario,val)
		yaCalifico = RegistroDeCalificaciones.existeCalificacionDeUnUsuario(bar,usuario)
		if yaCalifico:
			RegistroDeCalificaciones.modificarCalificacion(bar,calificacionUsuario)
		else:
			RegistroDeCalificaciones.agregarCalificacion(bar,calificacionUsuario)

		