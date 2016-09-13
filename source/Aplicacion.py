import Bar
import Usuario
import Calificaciones
import Registrador

class Aplicacion:

    def __init__(self):
        registroBares = []
        #registroBaresPendientes = []
        registroUsuarios = []
        #registroAdmins = []
        registroDeCategorias = []

        registroDeCalificaciones = []

        registrador = Registrador()
        filtro = Filtro()

    def registrarUsuario(self, nombreUsuario):
        self.registrador.registrar(nombreUsuario, registroUsuarios)
    #def registrarAdmin(self, nombreUsuario):
        #self.registrador.registrar(nombreUsuario, registroAdmins)

    def agregarBar(self, usuario, nombreBar, ubicacion, tieneWiFi, puntajeWiFi, puntajeEnchufes):
        nuevoBar = Bar(nombreBar, ubicacion, tieneWiFi)
        self.registrador.registrar(nuevoBar, registroBares)

        if tieneWiFi:
            categoriaWiFi = ([unaCategoria for unaCategoria in registroDeCategorias if unaCategoria.darNombre() == "WiFi"])[0]
            calificacion = Calificacion(puntajeWiFi, usuario, categoriaWiFi, nuevoBar)
            registrador.registrar(calificacion, registroDeCalificaciones)

        categoriaEnchufes = ([unaCategoria for unaCategoria in registroDeCategorias if unaCategoria.darNombre() == "Enchufes"])[0]
        calificacion = Calificacion(puntajeEnchufes, usuario, categoriaEnchufes, nuevoBar)
        registrador.registrar(calificacion, registroDeCalificaciones)

    def agregarCategoria(self, nombreDeLaCategoria):
        self.registrador.registrar(Categoria(nombreDeLaCategoria))

    def calificarBar(self, usuario, bar, categoria, puntaje):
        # chequear si bar está bares
        # chequear si categoria está en categorias
        calificacion = Calificacion(puntaje, usuario, categoria, bar)
        if (registrador.buscar(calificacion)):
        	# MAGIA NEGRA: Las calificaciones son iguales, aún con puntajes distintos. Entonces, modifico mi "misma" calificación
        	registrador.modificar(calificacion, calificacion, registroDeCalificaciones)
        else: 
        	registrador.registrar(calificacion, registroDeCalificaciones)

    # fijarse si es necesario chequear si bar y categoria son correctos
    # def chequearBar(nombreBar)
    #    return Bar
