#include <iostream>
#include <string>

using namespace std;

class Usuario{
public:
	Usuario(string nombreDelUsuario);
	string darNombre();
	int darUbicacion();
private:
	string nombre;
	int ubicacion;
};