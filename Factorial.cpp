/** Nombre del programa: factorial
    autor:Evelyn Bravo
    version 1.0
    Este programa obtiene el factorial de un numero ingresado por el usuario
**/
#include <iostream>

using namespace std;

int factorial(int num) {
    /** Esta funcion utiliza un ciclo for para ir acumulando la multiplicacion del numero menos i y se va guardando en la variable facto**/
    int facto = 1;
    if (num == 1) {
        facto = 1;
    }
    else {
        for (int i = 1; i < num + 1;i++) {
            facto = facto * i;
        }
        return facto;

    }
}

int main() {
    int opcion, opcion2;
    int saldo = 20000;


    do {
        /**Menu para el usuario**/
        cout << "--MENU--" << endl;
        cout << "1. Factorial" << endl;
        cout << "2. Cajero" << endl;
        cout << "3. Salir" << endl;
        cout << "ingrese una opcion: ";
        cin >> opcion;

        switch (opcion) {

        case 1:
            /**Se pide al usuario que ingrese un numero**/
            int num;
            cout << "ingrese un numero para obtener su factorial" << endl;
            cin >> num;
            /** se muestra el resultado en pantalla**/
            cout << "el factorial del numero es: " << factorial(num);

            break;

        case 2:
            int retiro;
            /**Menu Banco**/
            cout << "--MENU--" << endl;
            cout << "1. Consultar saldo" << endl;
            cout << "2. Retirar dinero" << endl;
            cout << "ingrese una opcion: ";
            cin >> opcion2;

            if (opcion2 == 1) {
                cout << "Su saldo es de: " << saldo << endl;
            }
            else if (opcion2 == 2) {
                cout << "Ingrese la cantidad a retirar: " << endl;
                cin >> retiro;
                saldo = saldo - retiro;
                cout << "Su saldo es de: " << saldo << endl;
                retiro = 0;
            }
            break;


        }
    } while (opcion != 3);




}