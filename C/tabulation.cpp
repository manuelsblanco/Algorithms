#include <stdio.h>

int main() {
    int c;  // Variable para almacenar el carácter leído

    // Leer cada carácter desde la entrada estándar
    while ((c = getchar()) != EOF) {
        switch (c) {
            case '\t':  // Tabulación
                printf("\\t");
            break;
            case '\b':  // Retroceso
                printf("\\b");
            break;
            case '\\':  // Diagonal invertida
                printf("\\\\");
            break;
            default:
                putchar(c);
            break;
        }
    }

    return 0;
}