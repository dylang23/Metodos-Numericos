from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan
from algoritmos.sistemas_ecuaciones_lineales.metodos_iterativos import gauss_seidel, jacobi
from algoritmos.sistemas_ecuaciones_lineales.utiles import determinante


def prueba_solucion(matriz, solucion):
    for i in range(len(matriz)):
        prueba = 0
        for j in range(len(matriz)):
            prueba += matriz[i][j] * solucion[j]
        print(prueba)

matriz = [[0.2, 1.3, -4, 1.25, 5, 8], 
          [-0.06, -0.39, 1.2, -0.38, -1.5, -2.4],
          [0.03, 0.2, -0.6, 0.19, 0.75, 1.2],
          [0.19, 1.24, -3.82, 1.19, 4.77, 7.63],
          [0.29, 1.88, -5.78, 1.81, 7.23, 11.56]]

solucion_seidel = gauss_seidel(matriz, [0, 0, 0, 0, 0], iter_max=10, error_aceptado=1e-5)

print(solucion_seidel)
print(prueba_solucion(matriz, solucion_seidel[0]))
    
