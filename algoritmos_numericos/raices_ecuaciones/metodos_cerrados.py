
'''

Paramétros: 

funcion_f: funcion definida en [lim_inf, lim_sup]

lim_inf: limite inferior del intervalo
lim_sup: limite superior del intervalo

error_aceptado: el valor por defecto es 1e-5

'''


def biseccion(funcion_f, lim_inf, lim_sup, error_aceptado=1e-5)  -> float:
    
    raiz_aprox =  (lim_sup - lim_inf) / 2
    error =  (lim_sup - lim_inf)

    while error < error_aceptado:

        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0

        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox

        error = abs(lim_sup - lim_inf)
        raiz_aprox = (lim_sup - lim_inf) / 2
    
    return raiz_aprox

