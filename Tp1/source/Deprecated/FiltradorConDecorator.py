import abc

class Filtrador:
	self.filtro = None
	self.nombre = None
	def filtrar(self):
		raise NotImplementedError("es una clase abstracta")
	

class FiltroBase(Filtrador):
	def __init__(self,name):
	 	self.nombre = name
	 	self.filtro
	def filtrar(self):
		filtro.filtrar()


class FiltroCompuesto(Filtrador):
	 def __init__(self,name,filtro):
	 	self.nombre = name
	 	self.miFiltro

	 def filtrar(self):
		filtro.filtrar(miFiltro.filtrar())

	