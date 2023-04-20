from algoritmos.sistemas_ecuaciones_lineales.metodos_directos import gauss_simple, gauss_jordan, mayores_coeficiente
from pytest import approx, mark


@mark.parametrize(
        
    "matriz, solucion_esperada, error_aceptado",    
    [
        ([[2, 3, 4, 2], [1, 2, 7, 1], [4, 13, 2, 1]],
         [1.51315789, -0.39473684, 0.03947368], 1e-5),

        ([[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]], [3, -2.5, 7], 1e-5)
    ]

)
def test_gauss_simple(matriz, solucion_esperada, error_aceptado):

    solucion = gauss_simple(matriz)
    assert solucion_esperada == approx(solucion, abs=error_aceptado)


@mark.parametrize(
        
    "matriz, solucion_esperada, error_aceptado",    
    [
        ([[2, 3, 4, 2], [1, 2, 7, 1], [4, 13, 2, 1]],
         [1.51315789, -0.39473684, 0.03947368], 1e-5),

        ([[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]], [3, -2.5, 7], 1e-5)
    ]

)
def test_gauss_jordan(matriz, solucion_esperada, error_aceptado):
    
    solucion = gauss_jordan(matriz)
    assert solucion_esperada == approx(solucion, abs=error_aceptado)



def test_mayor_coeficientes():
    matriz = [[9, 2, 3], [2, 5, 3], [4, 3, 10]]
    coeficientes_mayores_esperados = [9, 5, 10]
    coeficientes_mayores_resultado = mayores_coeficiente(matriz)

    assert coeficientes_mayores_esperados == coeficientes_mayores_resultado