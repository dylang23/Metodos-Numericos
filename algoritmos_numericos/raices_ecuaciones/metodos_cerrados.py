from parsers.parsear_expression import str_to_function

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
        print(round(lim_inf,6), round(lim_sup,6), round(raiz_aprox,6), round(funcion(raiz_aprox),6), round(error_calculado,6))
        
        if condicion_bolzano:
            lim_sup = raiz_aprox
        else:
            lim_inf = raiz_aprox
    
        raiz_aprox_previa = raiz_aprox
        raiz_aprox = (lim_inf + lim_sup) / 2
        error_calculado = abs(raiz_aprox - raiz_aprox_previa)
    
    print(round(lim_inf,6), round(lim_sup,6), round(raiz_aprox,6), round(funcion(raiz_aprox),6), round(error_calculado,6))
    return raiz_aprox



expression = "cos(4x-2) + exp(1-x)"
funcion = str_to_function(expression)

raiz = biseccion(funcion, 0.8, 1.2, error_aceptado=0.0001)