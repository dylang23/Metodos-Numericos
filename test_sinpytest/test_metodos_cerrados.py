from parsers.parsear_expression import str_to_function
from algoritmos.raices_ecuaciones.metodos_cerrados import biseccion, regula_falsi


expression = "cos(4x-2) + exp(1-x)"
funcion = str_to_function(expression)

iteraciones_biseccion = biseccion(funcion, 0.8, 1.2, error_aceptado=1e-4)
iteraciones_regula_falsi = regula_falsi(funcion, 0.8, 1.2, error_aceptado=1e-4)


print("Iteraciones para biseccion: ")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
    "i","a[i]", "b[i]", "xp[i]", "f([xp[i])", "DXp[i]"))

for i, iteracion in enumerate(iteraciones_biseccion):
    lim_inf = round(iteracion.lim_inf, 6) 
    lim_sup = round(iteracion.lim_sup, 6)
    raiz_aprox = round(iteracion.raiz_aprox, 6)
    funcion_valuada = round(iteracion.funcion_valuada, 6)
    error = round(iteracion.error_calculado, 6)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(i + 1, lim_inf, lim_sup, raiz_aprox, funcion_valuada, error))

print("")

print("Iteraciones para regula falsi")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
    "i","a[i]", "b[i]", "xp[i]", "f([xp[i])", "DXp[i]"))
for i, iteracion in enumerate(iteraciones_regula_falsi):
    lim_inf = round(iteracion.lim_inf, 6) 
    lim_sup = round(iteracion.lim_sup, 6)
    raiz_aprox = round(iteracion.raiz_aprox, 6)
    funcion_valuada = round(iteracion.funcion_valuada, 6)
    error = round(iteracion.error_calculado, 6)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(i + 1, lim_inf, lim_sup, raiz_aprox, funcion_valuada, error))

