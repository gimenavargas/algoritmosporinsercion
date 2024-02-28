def insertion_sort(arr):  #Esta línea define una función llamada `insertion_sort` que toma una lista `arr` como argumento. 
                           #Esta función realizará el ordenamiento por inserción en la lista que se le pase.

    for i in range(1, len(arr)): #Este bucle for itera sobre los índices de la lista arr, empezando desde el segundo elemento (índice 1) hasta el último elemento.
                                 # Se salta el primer elemento porque, en el ordenamiento por inserción, se asume que la parte izquierda de la lista está ordenada inicialmente.

        key = arr[i] #Esta línea guarda el valor del elemento actual (`arr[i]`) en la variable `key`. Este es el elemento que se insertará en la parte ordenada de la lista.

        j = i - 1 #Se inicializa j con el índice anterior al índice actual "i".

        while j >= 0 and key < arr[j]: #Este bucle `while` busca la posición correcta para insertar el elemento `key` en la parte ordenada de la lista.
                                     # Continúa mientras `j` es mayor o igual a cero (asegurando que no nos salgamos de los límites de la lista)
                                     # y mientras el elemento `key` sea menor que el elemento en la posición `j`.

            arr[j + 1] = arr[j]#Se desplaza cada elemento mayor que key una posición hacia la derecha para dejar espacio para insertar "key".

            j -= 1#Se decrementa `j` para seguir comparando hacia atrás en la lista ordenada.

        arr[j + 1] = key#Una vez que se encuentra la posición correcta para key, se inserta en la lista ordenada moviendo los elementos mayores una posición hacia la derecha.

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6]#Se define un ejemplo de lista `arr` que se pasa a la función `insertion_sort` para ser ordenada.
insertion_sort(arr)
print("Arreglo ordenado por inserción:")
for i in range(len(arr)):
    print("%d" % arr[i])


#Finalmente, se imprime la lista ordenada después de haber aplicado el algoritmo de ordenamiento por inserción.
