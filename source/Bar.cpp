#include "Bar.h"

Bar::Bar(string nombreDelBar, int ubicacionDelBar){
	nombre = nombreDelBar;
	ubicacion = ubicacionDelBar;
}

string Bar::darNombre(){
	return nombre;
}

int Bar::darUbicacion(){
	return ubicacion;
}
