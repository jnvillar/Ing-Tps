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

        calificador = Calificador()
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
            categoriaWIFI = ([unaCategoria for unaCategoria in registroDeCategorias if unaCategoria.darNombre() == "WiFi"])[0]
            calificador.Calificar(nuevoBar, usuario, puntajeWiFi, categoriaWIFI)

        categoriaEnchufes = ([unaCategoria for unaCategoria in registroDeCategorias if unaCategoria.darNombre() == "Enchufes"])[0]
        calificador.Calificar(nuevoBar, usuario, puntajeEnchufes, categoriaEnchufes)

    def agregarCategoria(self, nombreDeLaCategoria):
        self.registrador.registrar(Categoria(nombreDeLaCategoria))

    def calificarBar(self, usuario, bar, categoria, puntaje):
        # chequear si bar está bares
        # chequear si categoria está en categorias
        calificador.Calificar(bar, usuario, puntaje, categoria)

    # fijarse si es necesario chequear si bar y categoria son correctos
    # def chequearBar(nombreBar)
    #    return Bar
