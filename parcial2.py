from algoritmos.interpolacion.interpolacion_lagrange import PolinomioLagrange
from algoritmos.integracion.regla_simpson import simpson_tercio, simpson_octavo
from algoritmos.integracion.regla_trapecio import multiple_trapecio


puntos = [(0, -1), (1, 1), (4, 1)]
polinomio_lagrange = PolinomioLagrange(puntos)

print(polinomio_lagrange.polinomio())