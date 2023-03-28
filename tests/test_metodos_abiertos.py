from algoritmos.raices_ecuaciones.metodos_abiertos import newton, punto_fijo, secante
from parsers.parsear_expression import str_to_function

funcion_f = str_to_function("x^2 + 10cosx")
derivada_f = str_to_function("2x - 10sen(x)")

funcion_g = str_to_function("x + 0.152334*(x**2 + 10cos(x))")


## Llamando a cada metodo
iteraciones_newton = newton(funcion_f, derivada_f, 1, error_aceptado=1e-5)

iteraciones_punto_fijo = punto_fijo(
    funcion_f, funcion_g, 1.5, error_aceptado=1e-7)

iteraciones_secante = secante(funcion_f, 1.2, 1.5, error_aceptado=1e-7)



print("Iteraciones del metodo de newton")
for iteracion in iteraciones_newton:
    print(iteracion.raiz_aprox_prev, iteracion.funcion_valuada,
          iteracion.error_calculado, iteracion.raiz_aprox)


print("Iteraciones del metodo de la secante")
for iteracion in iteraciones_secante:
    print(iteracion.raiz_aprox, iteracion.error_calculado)


print("Iteraciones del metodo de punto fijo")
print("{:<20} {:<20} {:<20} {:<20}".format(
    "x[i]", "f(x[i])", "error", "x[i+1]"))
for iteracion in iteraciones_punto_fijo:
    raiz_aprox_prev = round(iteracion.raiz_aprox_prev, 8)
    funcion_valuada = round(iteracion.funcion_valuada, 8)
    error_calculado = round(iteracion.error_calculado, 8)
    raiz_aprox = round(iteracion.raiz_aprox, 8)
    
    print("{:<20} {:<20} {:<20} {:<20}".format(
        raiz_aprox_prev, funcion_valuada, error_calculado, raiz_aprox))
