from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan

matriz = [[0.2, 1.3, -4, 1.25, 5, 8], 
          [-0.06, -0.39, 1.2, -0.38, -1.5, -2.4],
          [0.03, 0.2, -0.6, 0.19, 0.75, 1.2],
          [0.19, 1.24, -3.82, 1.19, 4.77, 7.63],
          [0.29, 1.88, -5.78, 1.81, 7.23, 11.56]]
print(gauss_simple(matriz))