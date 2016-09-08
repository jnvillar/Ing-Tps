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
		return self.valor

class Categoria:

	def __init__(self,nombre):
		self.nombreDeLaCategoria = nombre
		self.contenedorDeCalifiaciones = {}

	def agregarCalificacion(bar,calificacion):
		self.contenedorDeCalifiaciones.setdefault(bar.darNombre(),[]).append(calificacion)

	def quitarCalificacion(bar,calificacion):
		self.contenedorDeCalifiaciones[bar.darNombre()].remove(calificacion)

	def darNombre(self):
		return nombreDeLaCategoria

class ContenedorCategorias:
	def __init__(self):
		self.categorias = []
	
	def agregarCategoria(self, categoria)
		self.categorias.append(categorias)

	def agregarCalificacion(self,categoria,calificacion)
		assert(categoria in categorias)
		categorias[categorias.index(categoria)].agregarCalificacion(calificacion)

	def eliminarCalificacion(self,categoria,calificacion)
		assert(categoria in categorias)
		categorias[categorias.index(categoria)].quitarCalificacion(calificacion)
