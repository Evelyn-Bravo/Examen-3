/** Nombre del programa: factorial
	autor:Evelyn Bravo
	version 1.0
	Este programa obtiene el factorial de un numero ingresado por el usuario
**/
#include <iostream>

using namespace std;

int factorial(int num) {
	/** Esta funcion utiliza un ciclo for para ir acumulando la multiplicacion del numero menos i y se va guardando en la variable facto**/
	int facto;
	for (int i = 1; i < num;i++) {
		facto += num * (num - i);
	}
	return facto;
}

int main() {
	/**Se pide al usuario que ingrese un numero**/
	int num;
	cout << "ingrese un numero para obtener su factorial" << endl;
	cin >> num;
	cout << "el factorial del numero es: " << factorial(num);

}