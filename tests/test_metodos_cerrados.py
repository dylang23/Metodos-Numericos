from parsers.parsear_expression import str_to_function
from algoritmos.raices_ecuaciones.metodos_cerrados import biseccion, regula_falsi


expression = "cos(4x-2) + exp(1-x)"
funcion = str_to_function(expression)

iteraciones_biseccion = biseccion(funcion, 0.8, 1.2, error_aceptado=1e-4)
iteraciones_regula_falsi = regula_falsi(funcion, 0.8, 1.2, error_aceptado=1e-4)

print("Iteraciones para biseccion: ")
for solucion in iteraciones_biseccion:
    print(round(solucion.raiz_aprox,6), solucion.error_calculado)

print("Iteracion para regula falsi")
for solucion in iteraciones_regula_falsi:
    print(solucion.raiz_aprox)
