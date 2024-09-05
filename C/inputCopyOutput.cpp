#include <stdio.h>

int main() {
    int c;          // Variable para almacenar el carácter leído
    int in_space = 0; // Bandera para indicar si estamos dentro de una secuencia de espacios

    // Leer cada carácter desde la entrada estándar
    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            // Si encontramos un espacio y no estamos en una secuencia de espacios, imprimimos un solo espacio
            if (!in_space) {
                putchar(c);
                in_space = 1; // Marcar que estamos en una secuencia de espacios
            }
        } else {
            // Si el carácter no es un espacio, imprimimos el carácter y restablecemos la bandera
            putchar(c);
            in_space = 0; // Restablecer la bandera
        }
    }

    return 0;
}