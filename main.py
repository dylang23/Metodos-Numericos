from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan
from algoritmos.sistemas_ecuaciones_lineales.metodos_iterativos import gauss_seidel, jacobi
from algoritmos.sistemas_ecuaciones_lineales.utiles import determinante

def main():
    matriz = [[1, 0.5, 0.333, 0.25, 2.08], [0.5, 0.333, 0.25, 0.2, 1.28], [
        0.333, 0.25, 0.2, 0.167, 0.95], [0.25, 0.2, 0.167, 0.143, 0.760]]

    matriz_coeficientes =  [[1, 0.5, 0.333, 0.25], [0.5, 0.333, 0.25, 0.2], [
        0.333, 0.25, 0.2, 0.167], [0.25, 0.2, 0.167, 0.143]]

    print(determinante(matriz_coeficientes))
    solucion_gauss_simple = gauss_simple(matriz)
    solucion_gauss_jordan = gauss_jordan(matriz)
    

    print("Solución con Gauss simple: ", solucion_gauss_simple)
    print("Solución con Gauss-Jordan: ", solucion_gauss_jordan)


if __name__ == "__main__":
    main()
