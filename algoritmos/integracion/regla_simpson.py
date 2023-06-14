from parsers.parsear_expression import str_to_function
import math


def simpson_tercio(funcion, intervalo, pasos=5):
    lim_inf = intervalo[0]
    lim_sup = intervalo[1]
    if pasos is None:
        paso = (lim_sup - lim_inf) / 2
        pasos = int((lim_sup - lim_inf) / paso)
    else:
        paso = (lim_sup - lim_inf) / pasos

    x = lim_inf
    sum = funcion(lim_inf) + funcion(lim_sup)

    for i in range(pasos - 2):
        x += paso
        if i % 2 == 0:
            sum += 4 * funcion(x)
        else:
            sum += 2 * funcion(x)
    x += paso
    sum += 4 * funcion(x)
    resultado = (lim_sup - lim_inf) * sum / (3 * pasos)

    return resultado


def simpson_octavo(funcion, intervalo, pasos=5):
    lim_inf = intervalo[0]
    lim_sup = intervalo[1]

    if pasos is None:
        paso = (lim_sup - lim_inf) / 2
        pasos = int((lim_sup - lim_inf) / paso)

    else:
        paso = (lim_sup - lim_inf) / pasos

    x = lim_inf
    sum = funcion(lim_inf) + funcion(lim_sup)

    for i in range(pasos - 1):
        x += paso
        if (i + 1) % 3 == 0:
            sum += 2 * funcion(x)
        else:
            sum += 3 * funcion(x)

    resultado = 3 * (lim_sup - lim_inf) * sum / (8 * pasos)

    return resultado


function_str = '1 / (1 + x^2)'
funcion = str_to_function(function_str)


# Punto 2


# resultado_punto2 = simpson_tercio(funcion, [-1, 1], pasos=2)
# print("Resultado apoximado con dos subdivisiones: ", resultado_punto2)


# # Punto 3

# resultado_punto3 = simpson_tercio(funcion, [-1, 1], pasos=4)
# print("Resultado aproximado con cuatro subdivisiones: ", resultado_punto3)


# # Punto 4
# print("Para n = 2: ", math.pi/2 - resultado_punto2, "una diferencia porcentual de ",
#       round((math.pi/2 - resultado_punto2) / (math.pi / 2), 2), '%')

# print("Para n = 4: ", math.pi/2 - resultado_punto3, "una diferencia porcentual de ",
#       round((math.pi/2 - resultado_punto3) / (math.pi / 2), 3), '%')


# Punto 5
# integral_parte1 = simpson_tercio(funcion, [-1, 1/3], pasos=6)
# integral_parte2 = simpson_octavo(funcion, [1/3, 1], pasos=3)
# print(integral_parte1 + integral_parte2)


#print("Con n= 100", round(simpson_tercio(funcion, [-1, 1], pasos=30), 8))
#print(simpson_octavo(funcion, [-1, 1], pasos=9))
