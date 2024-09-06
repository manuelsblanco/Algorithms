#include <stdio.h>

unsigned setbits(unsigned x, int p, int n, unsigned y) {
    // Crear una máscara para los n bits menos significativos de y
    unsigned mask = (1U << n) - 1; // Genera una máscara con n bits en 1
    unsigned y_bits = y & mask;    // Extrae los n bits menos significativos de y

    // Desplazar los bits de y a la posición correcta
    y_bits <<= (p - n + 1);

    // Crear una máscara para los n bits a reemplazar en x
    mask <<= (p - n + 1);

    // Limpiar los n bits en x y luego poner los bits de y
    return (x & ~mask) | y_bits;
}

int main() {
    unsigned x = 0xFFFF; // Ejemplo de número para x
    unsigned y = 0x0F;   // Ejemplo de número para y
    int p = 8;           // Posición de los bits a reemplazar
    int n = 4;           // Número de bits a reemplazar

    unsigned result = setbits(x, p, n, y);
    printf("Resultado: 0x%X\n", result); // Imprime el resultado en formato hexadecimal

    return 0;
}