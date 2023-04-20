from numpy import copy, array, float64

# Para la manipulación de matrices se utliza la libreria numpy
# Se utiliza una precisión de float64, esto quiere decir 64 bits, 15-17 cifras significativas


def gauss_simple(matriz):

    matriz = matriz_to_numpyarray(matriz)
    matriz_triangular_superior = eliminacion_hacia_adelante(matriz)
    solucion = sustitucion_atras(matriz_triangular_superior)

    return solucion


def eliminacion_hacia_adelante(matriz):

    matriz = copy(matriz)
    filas = matriz.shape[0]
    columnas = matriz.shape[1]

    for i in range(filas - 1):
        pivote_gauss_simple(matriz, i)
        for j in range(i + 1, filas):
            factor = matriz[j][i] / matriz[i][i]
            for k in range(i + 1, columnas):
                matriz[j][k] = matriz[j][k] - factor * matriz[i][k]

    return matriz

def sustitucion_atras(matriz):

    filas = matriz.shape[0]
    columns = matriz.shape[1]

    solucion = [None] * filas
    solucion[filas - 1] = matriz[filas - 1][columns - 1] / \
        matriz[filas - 1][filas - 1]

    for i in range(filas - 2, -1, -1):
        solucion_parcial = matriz[i][columns - 1]
        for j in range(i + 1, filas):
            solucion_parcial = solucion_parcial - \
                matriz[i][j] * solucion[j]
        solucion[i] = solucion_parcial / matriz[i][i]

    return solucion



def gauss_jordan(matriz):
    matriz = matriz_to_numpyarray(matriz)
    solucion = eliminar_gauss_jordan(matriz)
    return solucion

def eliminar_gauss_jordan(matriz):

    filas = matriz.shape[0]
    columnas = matriz.shape[1]

    for i in range(filas):
        pivoteo_gauss_jordan(matriz, i)
        pivot = matriz[i][i]
        matriz[i] = [matriz[i][j] / pivot for j in range(columnas)]

        for j in range(filas):
            factor = matriz[j][i]
            if i != j:
                for k in range(columnas):
                    matriz[j][k] = matriz[j, k] - factor * matriz[i, k]

    solucion = [matriz[i][columnas - 1] for i in range(filas)]

    return solucion


# Funciones utiles

def matriz_to_numpyarray(matriz):

    matriz = array(matriz, dtype=float64)

    return matriz


def pivote_gauss_simple(matriz, index):

    coeficientes_mayores = mayores_coeficiente(matriz)
    mayor_pivot = abs(matriz[index][index] / coeficientes_mayores[index])
    mayor_fila_pivot = index

    for i in range(index + 1, len(matriz)):
        posible_mayor_pivot = abs(matriz[i, index] / coeficientes_mayores[i])
        if posible_mayor_pivot > mayor_pivot:
            mayor_pivot = posible_mayor_pivot
            mayor_fila_pivot = i

    if mayor_fila_pivot != index:
        matriz[[index, mayor_fila_pivot],
               :] = matriz[[mayor_fila_pivot, index], :]


# Devuelve un array de los coeficientes mayores en valor absoluto de cada fila


def mayores_coeficiente(matriz):

    mayores_coeficientes = []
    filas = len(matriz)

    for i in range(filas):
        mayor_coeficiente = abs(matriz[i][0])

        for j in range(1, filas):
            if abs(matriz[i][j]) > mayor_coeficiente:
                mayor_coeficiente = abs(matriz[i][j])

        mayores_coeficientes.append(mayor_coeficiente)

    return mayores_coeficientes


def pivoteo_gauss_jordan(matriz, index):

    if index >= len(matriz):
        return 

    mayor_pivot = abs(matriz[index][index])
    mayor_fila_pivot = index

    for i in range(index + 1, len(matriz)):
        posible_mayor_pivot = abs(matriz[i, index])
        if posible_mayor_pivot > mayor_pivot:
            mayor_pivot = posible_mayor_pivot
            mayor_fila_pivot = i

    if mayor_fila_pivot != index:
        matriz[[index, mayor_fila_pivot],
               :] = matriz[[mayor_fila_pivot, index], :]
