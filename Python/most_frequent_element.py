# English: Function to find the most frequent element in a list
# Español: Función para encontrar el elemento más frecuente en una lista
def encontrar_elemento_mas_frecuente(lista):
    # English: Create an empty dictionary to store the frequency of each element
    # Español: Crear un diccionario vacío para almacenar la frecuencia de cada elemento
    frecuencias = {}

    # English: Loop through each element in the list
    # Español: Recorrer cada elemento en la lista
    for elemento in lista:
        # English: Update the frequency of the element in the dictionary
        # Español: Actualizar la frecuencia del elemento en el diccionario
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    # English: Find the element with the highest frequency
    # Español: Encontrar el elemento con la mayor frecuencia
    elemento_mas_frecuente = max(frecuencias, key=frecuencias.get)

    return elemento_mas_frecuente


# English: Tests
# Español: Pruebas
print(encontrar_elemento_mas_frecuente([1, 3, 1, 3, 2, 1]))  # English: Should print 1 / Español: Debería imprimir 1
print(encontrar_elemento_mas_frecuente([3, 3, 1, 3, 2, 1]))  # English: Should print 3 / Español: Debería imprimir 3
