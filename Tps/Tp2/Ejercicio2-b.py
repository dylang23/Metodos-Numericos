from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan
from algoritmos.sistemas_ecuaciones_lineales.utiles import determinante

'''
    Ejercicio 2:
    b)Ingresando los datos del problema con un truncamiento en la tercer cifra decimal
'''


def main():
    print("Ejercicio 2-b con truncamiento")

    matriz = [[1, 0.5, 0.333, 0.25, 2.083], [0.5, 0.333, 0.25, 0.2, 1.283], [
        0.333, 0.25, 0.2, 0.166, 0.95], [0.25, 0.2, 0.166, 0.142, 0.759]]

    matriz_coeficiente = [[1, 0.5, 0.333, 0.25], [0.5, 0.333, 0.25, 0.2], [
        0.333, 0.25, 0.2, 0.166], [0.25, 0.2, 0.166, 0.142]]

    det_matriz = determinante(matriz_coeficiente)
    
    solucion_gauss_simple = gauss_simple(matriz)
    solucion_gauss_jordan = gauss_jordan(matriz)

    print("Solución con Gauss simple: ", solucion_gauss_simple)
    print("Solución con Gauss-Jordan: ", solucion_gauss_jordan)
    print("Determinante: ", det_matriz)
    
if __name__ == "__main__":
    main()
