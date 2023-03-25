
'''

Paramétros: 

funcion_f: funcion definida en [lim_inf, lim_sup]

lim_inf: limite inferior del intervalo
lim_sup: limite superior del intervalo

error_aceptado: el valor por defecto es 1e-5

'''


def biseccion(funcion_f, lim_inf, lim_sup, error_aceptado=1e-5):
    
    
    raiz_aprox = (lim_inf + lim_sup) / 2
    error_calculado =  raiz_aprox - lim_inf

    while error_aceptado < error_calculado:

        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0

        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox

        raiz_aprox_previa = raiz_aprox
        raiz_aprox = (lim_inf + lim_sup) / 2
        
        error_calculado = (raiz_aprox - raiz_aprox_previa)
    
    return raiz_aprox

