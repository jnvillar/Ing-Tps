class Calificacion:
	def __init__(self, val, user):
		assert(val<6 and 0<val)
		self.estrellas = val
		self.usuario = user

	def darUsuario(self):
		return self.usuario

	def modificarValor(self,val,user):
		assert(val<6 and 0<val)
		assert(self.usuario == user) 
		self.estrellas = val

	def darValor(self):
		return self.estrellas

class Calificaciones:

	def __init__(self,nombre):
		self.nombreDeLaCategoria = nombre
		self.contenedorDeCalifiaciones = {}

	def agregarCalificacion(self,bar,calificacion):
		self.contenedorDeCalifiaciones.setdefault(bar.darNombre(),[]).append(calificacion)

		# que solo tome al usuario
	def quitarCalificacion(self,bar,calificacion):
		assert(bar in self.contenedorDeCalifiaciones)
		self.contenedorDeCalifiaciones[bar.darNombre()].remove(calificacion)

		# que solo tome la calificacion nueva
	def modificarCalificacion(self,bar,calificacionVieja,calificacionNueva) 
		assert(bar in self.contenedorDeCalifiaciones)
		self.quitarCalificacion(bar,calificacionVieja)
		self.agregarCalificacion(bar,calificacionNueva)

	def buscarCalificacionDeUnUsuario(self,bar,usuario):
		assert(bar in self.contenedorDeCalifiaciones)
		listaDeCalificaciones = self.contenedorDeCalifiaciones.get(bar)
		for calificacion in listaDeCalificaciones:
			if calificacion.darUsuario == usuario:
				return calificacion

	def existeCalificacionDeUnUsuario(self,bar,usuario):
		assert(bar in self.contenedorDeCalifiaciones)
		listaDeCalificaciones = self.contenedorDeCalifiaciones.get(bar)
		for calificacion in listaDeCalificaciones:
			if calificacion.darUsuario == usuario:
				return True
		return False


	def darNombre(self):
		return self.nombreDeLaCategoria

class ContenedorDeCalificaciones:
	def __init__(self):
		self.categorias = []
	
	def agregarCategoria(self, categoria):
		self.categorias.append(categoria)

	def verCalificacionesDeUnaCategoria(self,categoria):
		assert(categoria in categorias)
		return categorias[categorias.index(categoria)]

	def agregarCalificacion(self,categoria,bar,calificacion):
		assert(categoria in categorias)
		categorias[categorias.index(categoria)].agregarCalificacion(bar,calificacion)

	def eliminarCalificacion(self,categoria,bar,calificacion):
		assert(categoria in categorias)
		categorias[categorias.index(categoria)].quitarCalificacion(bar,calificacion)

	def existeCalificacionDeUnUsuario(self,categoria,bar,usuario):
		assert(categoria in categorias)
		categorias[categorias.index(categoria)].existeCalificacionDeUnUsuario(bar,usuario)

	def modificarCalificacion(self,categoria,bar,calificacion):
		self.eliminarCalificacion(categoria,bar,calificacion)
		self.agregarCalificacion(categoria,bar,calificacion)
