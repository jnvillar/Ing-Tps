class Ubicacion(object):

	def __init__(self, calle):
		assert(type(calle)==str)
		self.direccion = calle		

	def __eq__ (self, otro):
		return self.direccion == otro.darDireccion()

	def darDireccion(self):
		return self.direccion	

	def __str__(self):
		return 	"(%s)" % (self.direccion)


