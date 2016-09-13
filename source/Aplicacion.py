import Bar
import Usuario
import RegistrarBar
import RegistrarUsuario

class Aplicacion:

    def __init__(self):
        registroBares = []
        registroUsuarios = []
        registroAdmins = []

        registradorBares = RegistrarBar()
        registradorUsuarios = RegistrarUsuario()

        filtro = Filtro()

    def registrarUsuario(self, nombreUsuario):
        self.registradorUsuarios.registrarUsuario(nombreUsuario, registroUsuarios)
    def registrarAdmin(self, nombreUsuario):
        self.registradorAdmins.registrarUsuario(nombreUsuario, registroAdmins)
    def agregarBar(self, nombreBar, Ubicacion, tieneWiFi, puntajeWiFi, puntajeEnchufes):
        self.registradorBares.agregarBar(Bar(nombreBar))

    def calificarBar(self, Usuario, Bar, Categoria, Puntaje):
