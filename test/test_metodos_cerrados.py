from parsers.parsear_expression import str_to_function
from algoritmos_numericos.raices_ecuaciones.metodos_cerrados import biseccion

expression = "cos(4x-2) + exp(1-x)"
funcion = str_to_function(expression)

raiz = biseccion(funcion, 0.8, 1.2, error_aceptado=0.00001)

