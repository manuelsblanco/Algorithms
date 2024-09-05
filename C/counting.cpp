#include <stdio.h>

int main() {
    int c;                  // Variable para almacenar cada carácter leído
    int spaces = 0;         // Contador de espacios en blanco
    int tabs = 0;           // Contador de tabuladores
    int newlines = 0;       // Contador de nuevas líneas

    // Leer cada carácter hasta el final del archivo (EOF)
    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            spaces++;
        } else if (c == '\t') {
            tabs++;
        } else if (c == '\n') {
            newlines++;
        }
    }

    // Imprimir los resultados
    printf("Espacios en blanco: %d\n", spaces);
    printf("Tabuladores: %d\n", tabs);
    printf("Nuevas líneas: %d\n", newlines);

    return 0;
}