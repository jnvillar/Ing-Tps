class Ubicacion(object):

	def __init__(self, posicionX, posicionY):
		assert(type(posicionY)==int and type(posicionY)==int)
		self.coordenadaX = posicionX
		self.coordenadaY = posicionY

	def __eq__ (self, otro):
		return self.coordenadaY == otro.coordenadaY and self.coordenadaX == otro.coordenadaX

	def darCoordenadaX(self):
		return self.coordenadaX

	def  darCoordenadaY(self):
		return self.coordenadaY
