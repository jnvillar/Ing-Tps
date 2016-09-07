#include "Usuario.h"

Usuario::Usuario(string nombreDelUsuario){
	nombre = nombreDelUsuario;
	ubicacion = 0;
}

string Usuario::darNombre(){
	return nombre;
}

int Usuario::darUbicacion(){
	// ubicacion = posicionActual();                      API GOOGLE MAPS
	return ubicacion;
}
