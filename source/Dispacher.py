# -*- coding: latin-1 -*-

from Bar import *
from Usuario import *
from Calificaciones import *
from Directorio import *
from Registrador import *
from Filtrador import *
from Ubicacion import *
from Mapa import *

class Dispacher(object):

    def __init__(self):

       #Estas cosas deberian crearse en el main, no en el dispacher
        self.directorio = Directorio()
        self.registrador = Registrador()
        self.filtrador = Filtrador()

    def registrarUsuario(self, nombreUsuario):
        self.registrador.registrar(Usuario(nombreUsuario), self.directorio.darRegistroUsuarios())
    #def registrarAdmin(self, nombreUsuario):
        #self.registrador.registrar(nombreUsuario, registroAdmins)

    def obtenerCategorias(self):
        return self.directorio.darRegistroDeCategorias()

    def buscarUsuario(self, nombreUsuario):
        return self.registrador.pertenece(Usuario(nombreUsuario), self.directorio.darRegistroUsuarios())

    def obtenerBaresMismoNombre(self, nombreBar):
        filtros = [FiltroNombreBares(nombreBar)]
        return self.filtrador.filtrarBares(self.directorio,filtros)

    def obtenerUsuario(self, nombreUsuario):
        filtro = FiltroNombreUsuario(nombreUsuario)
        return self.filtrador.buscar(self.directorio.darRegistroUsuarios(),filtro)

    def agregarBar(self, usuario, bar , puntajes):

        self.registrador.registrar(bar, self.directorio.darRegistroBares())

        categoriaWiFi = self.filtrador.buscar(self.directorio.darRegistroDeCategorias(), FiltroNombreCategoria("WiFi"))
        categoriaEnchufes = self.filtrador.buscar(self.directorio.darRegistroDeCategorias(), FiltroNombreCategoria("Enchufes"))

        if bar.tieneWifi():
            self.calificarBar(usuario, bar, categoriaWiFi, puntajes[0])
            self.calificarBar(usuario, bar, categoriaEnchufes, puntajes[1])
        else:
            self.calificarBar(usuario, bar, categoriaEnchufes, puntajes[0])

        # if tieneWiFi:
        #     categoriaWiFi = ([unaCategoria for unaCategoria in self.directorio.darRegistroDeCategorias() if unaCategoria.darNombre() == "WiFi"])[0]
        #     calificacion = Calificacion(puntajeWiFi, usuario, categoriaWiFi, nuevoBar)
        #     self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

        # categoriaEnchufes = ([unaCategoria for unaCategoria in self.directorio.darRegistroDeCategorias() if unaCategoria.darNombre() == "Enchufes"])[0]
        # calificacion = Calificacion(puntajeEnchufes, usuario, categoriaEnchufes, nuevoBar)
        # self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

    def agregarCategoria(self, nombreDeLaCategoria):
        self.registrador.registrar(Categoria(nombreDeLaCategoria), self.directorio.darRegistroDeCategorias())

    def calificarBar(self, usuario, bar, categoria, puntaje):
        # chequear si bar está bares
        # chequear si categoria está en categorias
        if not (categoria.darNombre() == "WiFi" and not(bar.tieneWifi())): # este if chequea errores, esta bien dejarlo asi??
            calificacion = Calificacion(puntaje, usuario, categoria, bar)
            if (self.registrador.pertenece(calificacion,self.directorio.darRegistroDeCalificaciones())):
        	   # MAGIA NEGRA: Las calificaciones son iguales, aún con puntajes distintos. Entonces, modifico mi "misma" calificación
        	   self.registrador.modificar(calificacion, calificacion, self.directorio.darRegistroDeCalificaciones())
            else:
        	   self.registrador.registrar(calificacion, self.directorio.darRegistroDeCalificaciones())

    # fijarse si es necesario chequear si bar y categoria son correctos
    # def chequearBar(nombreBar)
    #    return Bar

    def buscarBaresCercanos(self, puntoDado, distancia):
        filtro = [FiltroPorDistancia(distancia,puntoDado)]
        baresCercanos = self.filtrador.filtrarBares(self.directorio,filtro)
        return baresCercanos

    def filtrarBaresVariosCriterios(self,listaFiltros):
        return self.filtrador.filtrarBares(self.directorio,listaFiltros)

    def obtenerCalificaciones(self, bar):
        return self.filtrador.buscar(self.directorio.darRegistroDeCalificaciones(), FiltroCalificacionesDeUnBar(bar))

    def mostrarRuta(self, origen, destino):
        m = Mapa(origen, destino)
        m.mostrarRuta()

    def mostrarUbicacion(self, ubicacion):
        m = Mapa(ubicacion, ubicacion)
        m.mostrarUbicacion()
        return
