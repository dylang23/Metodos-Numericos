from .iteracion import IteracionBiseccion, IteracionRegulaFalsi
from typing import List


def biseccion(funcion_f, lim_inf, lim_sup, cant_iter=100, error_aceptado=1e-5) -> List[IteracionBiseccion]:

    raiz_aprox = lim_inf
    i = 0
    iteraciones = []
    
    while i < cant_iter:

        raiz_aprox_prev = raiz_aprox
        raiz_aprox = (lim_inf + lim_sup) / 2
        error_calculado = abs(raiz_aprox - raiz_aprox_prev)
        
        iteraciones.append(IteracionBiseccion(raiz_aprox, error_calculado,
                          funcion_f(raiz_aprox), lim_inf, lim_sup))

        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0

        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox
    
        if error_calculado < error_aceptado: 
            break

        i += 1

    return iteraciones


def regula_falsi(funcion_f, lim_inf, lim_sup, cant_iter=100, error_aceptado=1e-5) -> List[IteracionRegulaFalsi]:

    def nueva_aprox():
        return lim_sup - (funcion_f(lim_sup) * (lim_inf - lim_sup)
                            ) / (funcion_f(lim_inf) - funcion_f(lim_sup))    
    
    raiz_aprox = lim_inf
    iteraciones = []
    iter = 0

    while iter < cant_iter:
        
        raiz_aprox_previa = raiz_aprox
        raiz_aprox = nueva_aprox()
        error_calculado = abs(raiz_aprox - raiz_aprox_previa)

        iteraciones.append(IteracionRegulaFalsi(raiz_aprox, error_calculado,
                          funcion_f(raiz_aprox), lim_inf, lim_sup))
        
        condicion_bolzano = funcion_f(lim_inf) * funcion_f(raiz_aprox) < 0
        
        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox

        if error_calculado < error_aceptado: 
            break
        
        iter += 1

    return iteraciones