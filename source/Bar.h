#include <iostream>
#include <string>

using namespace std;

class Bar{
public:
	Bar(string nombreDelBar, int ubicacionDelBar);
	int darUbicacion();
	string darNombre();	

private: 
	int ubicacion;
	string nombre;	
};