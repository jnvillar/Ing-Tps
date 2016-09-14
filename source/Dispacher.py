# -*- coding: latin-1 -*-

from Bar import *
from Usuario import *
from Calificaciones import *
from Directorio import *
from Registrador import *
from Filtrar import *
from Ubicacion import *

class Dispacher(object):

    def __init__(self):

       #Estas cosas deberian crearse en el main, no en el dispacher
        self.directorio = Directorio()
        self.registrador = Registrador()
        self.filtro = Filtrar()

    def registrarUsuario(self, nombreUsuario):
        self.registrador.registrar(Usuario(nombreUsuario), self.directorio.darRegistroUsuarios())
    #def registrarAdmin(self, nombreUsuario):
        #self.registrador.registrar(nombreUsuario, registroAdmins)

    def buscarUsuario(self, nombreUsuario):
        return self.registrador.buscar(Usuario(nombreUsuario), self.directorio.darRegistroUsuarios())

    def obtenerBaresMismoNombre(self, nombreBar):
        return self.filtro.darBaresConMismoNombre(nombreBar, self.directorio.darRegistroBares())

    def obtenerUsuario(self, nombreUsuario):
        return self.filtro.darUsuario(nombreUsuario, self.directorio.darRegistroUsuarios())
        #self.directorio.darRegistroUsuarios()

    def agregarBar(self, usuario, nombreBar, ubicacion, tieneWiFi, puntajeWiFi, puntajeEnchufes):
        nuevoBar = Bar(nombreBar, ubicacion, tieneWiFi)
        self.registrador.registrar(nuevoBar, self.directorio.darRegistroBares())

        if tieneWiFi:
            categoriaWiFi = ([unaCategoria for unaCategoria in self.directorio.darRegistroDeCategorias() if unaCategoria.darNombre() == "WiFi"])[0]
            calificacion = Calificacion(puntajeWiFi, usuario, categoriaWiFi, nuevoBar)
            self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

        categoriaEnchufes = ([unaCategoria for unaCategoria in self.directorio.darRegistroDeCategorias() if unaCategoria.darNombre() == "Enchufes"])[0]
        calificacion = Calificacion(puntajeEnchufes, usuario, categoriaEnchufes, nuevoBar)
        self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

    def agregarCategoria(self, nombreDeLaCategoria):
        self.registrador.registrar(Categoria(nombreDeLaCategoria), self.directorio.darRegistroDeCategorias())

    def calificarBar(self, usuario, bar, categoria, puntaje):
        # chequear si bar está bares
        # chequear si categoria está en categorias
        calificacion = Calificacion(puntaje, usuario, categoria, bar)
        if (registrador.buscar(calificacion)):
        	# MAGIA NEGRA: Las calificaciones son iguales, aún con puntajes distintos. Entonces, modifico mi "misma" calificación
        	self.registrador.modificar(calificacion, calificacion, self.directorio.darRegistroDeCalificaciones())
        else:
        	self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

    # fijarse si es necesario chequear si bar y categoria son correctos
    # def chequearBar(nombreBar)
    #    return Bar
