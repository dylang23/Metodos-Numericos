from parsers.parsear_expression import str_to_function
from algoritmos_numericos.raices_ecuaciones.iteracion import Iteracion
'''

Paramétros: 

funcion_f: funcion definida en [lim_inf, lim_sup]

lim_inf: limite inferior del intervalo
lim_sup: limite superior del intervalo

error_aceptado: el valor por defecto es 1e-5

'''


def biseccion(funcion_f, lim_inf, lim_sup, cant_iter=100, error_aceptado=1e-5):

    raiz_aprox = (lim_inf + lim_sup) / 2
    error_calculado = raiz_aprox - lim_inf
    i = 0
    iteraciones = []
    iteraciones.append(Iteracion(raiz_aprox, error_calculado,
                      funcion_f(raiz_aprox), lim_inf, lim_sup))

    while i < cant_iter and error_aceptado < error_calculado:

        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0

        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox

        raiz_aprox_previa = raiz_aprox
        raiz_aprox = (lim_inf + lim_sup) / 2
        error_calculado = abs(raiz_aprox - raiz_aprox_previa)

        iteraciones.append(Iteracion(raiz_aprox, error_calculado,
                          funcion_f(raiz_aprox), lim_inf, lim_sup))
        i += 1

    return iteraciones


def regula_falsi(funcion_f, lim_inf, lim_sup, cant_iter=100, error_aceptado=1e-5):

    def nueva_aprox():
        return lim_sup - (funcion_f(lim_sup) * (lim_inf - lim_sup)
                            ) / (funcion_f(lim_inf) - funcion_f(lim_sup))    
    
    raiz_aprox = nueva_aprox()
    error_calculado = abs(raiz_aprox - lim_inf)
    iteraciones = []
    iteraciones.append(Iteracion(raiz_aprox, error_calculado,
                      funcion_f(raiz_aprox), lim_inf, lim_sup))
    iter = 0

    while iter < cant_iter and error_aceptado < error_calculado:
        
        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0
        
        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox

        raiz_aprox_previa = raiz_aprox
        raiz_aprox = nueva_aprox()
        error_calculado = abs(raiz_aprox - raiz_aprox_previa)

        iteraciones.append(Iteracion(raiz_aprox, error_calculado,
                          funcion_f(raiz_aprox), lim_inf, lim_sup))
        iter += 1

    return iteraciones



expression = "cos(4x-2) + exp(1-x)"
funcion = str_to_function(expression)

soluciones_biseccion = biseccion(funcion, 0.8, 1.2, error_aceptado=0.0001)
soluciones_regulafalsi = regula_falsi(funcion, 0.8, 1.2, error_aceptado=0.0001)

print("Biseccion: ")
for solucion in soluciones_biseccion:
    print(solucion)

print("Regula falsi: ")
for solucion in soluciones_regulafalsi:
    print(solucion)
