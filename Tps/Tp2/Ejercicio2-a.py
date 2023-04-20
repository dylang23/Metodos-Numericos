from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan

'''
Ejercicio 2-a)
Ingresando los datos del problema con un redondeo de tres cifras significativas.
'''


def main():
    print("Ejercicio 2-a con rendondeo")
    matriz = [[1, 0.5, 0.333, 0.25, 2.083], [0.5, 0.333, 0.25, 0.2, 1.283],
              [0.333, 0.25, 0.2, 0.167, 0.95], [0.25, 0.2, 0.167, 0.143, 0.760]]

    solucion_gauss_simple = gauss_simple(matriz)
    solucion_gauss_jordan = gauss_jordan(matriz)

    print("Solución con Gauss simple: ", solucion_gauss_simple)
    print("Solución con Gauss-Jordan: ", solucion_gauss_jordan)


if __name__ == "__main__":
    main()
