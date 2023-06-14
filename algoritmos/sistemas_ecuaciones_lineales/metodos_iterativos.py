from numpy import array, float64
from numpy.linalg import norm



def verificar_criterio(solucion_previa, solucion_actual, error_aceptado):

    for sol_anterior, sol_actual in zip(solucion_previa, solucion_actual):
        error_calculado = abs((sol_actual - sol_anterior) / sol_actual)
        if error_calculado > error_aceptado:
            return False
    return True


def gauss_seidel(matriz, solucion_inicial, iter_max=50, error_aceptado=1e-5):

    matriz = array(matriz, dtype=float64)
    normalizar(matriz)
    filas = matriz.shape[0]
    solucion_actual = list(solucion_inicial)

    for iter in range(iter_max):
        solucion_previa = list(solucion_actual)

        for i in range(filas):
            suma_parcial = matriz[i][filas]
            for j in range(filas):
                if i != j:
                    suma_parcial -= matriz[i][j] * solucion_actual[j]

            solucion_actual[i] = suma_parcial / matriz[i][i]

        if (verificar_criterio(solucion_previa, solucion_actual, error_aceptado)):
            break

    return solucion_actual, iter


def jacobi(matriz, solucion_inicial, iter_max=50, error_aceptado=1e-5):

    matriz = array(matriz, dtype=float64)
    #normalizar(matriz)
    filas = matriz.shape[0]
    solucion_actual = list(solucion_inicial)

    for iter in range(iter_max):
        solucion_previa = list(solucion_actual)

        for i in range(filas):
            suma_parcial = matriz[i][filas]
            for j in range(filas):
                if i != j:
                    suma_parcial -= matriz[i][j] * solucion_previa[j]

            solucion_actual[i] = suma_parcial / matriz[i][i]

        # diferencia_solucion = array([sol_act - sol_ant for sol_ant,
        #                       sol_act in zip(solucion_previa, solucion_actual)])
        # norma = norm(diferencia_solucion)

        if (verificar_criterio(solucion_previa, solucion_actual, error_aceptado)):
            break

    return solucion_actual, iter


def normalizar(matriz):
    mayores_coeficientes = []
    filas = len(matriz)

    for i in range(filas):
        mayor_coeficiente = abs(matriz[i][0])

        for j in range(1, filas + 1):
            if abs(matriz[i][j]) > mayor_coeficiente:
                mayor_coeficiente = abs(matriz[i][j])

        mayores_coeficientes.append(mayor_coeficiente)

    for i in range(filas):
        for j in range(filas + 1):
          ##  print(i, j)
            matriz[i][j] /= mayores_coeficientes[i]
