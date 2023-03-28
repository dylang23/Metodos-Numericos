from parsers.parsear_expression import str_to_function


def punto_fijo(funcion_f, funcion_g, valor_inicial, cant_iter=100, error_aceptado=1e-5):

    raiz_aprox = valor_inicial
    
    for _ in range(cant_iter):

        raiz_aprox_prev = raiz_aprox
        raiz_aprox = funcion_g(raiz_aprox_prev)
        error_calculado = abs((raiz_aprox - raiz_aprox_prev) / raiz_aprox)
        
        if error_calculado < error_aceptado:
            break 
    
    return raiz_aprox


funcion_f = str_to_function("exp(-x)-x")
funcion_g = str_to_function("exp(-x)")
print(punto_fijo(funcion_f, funcion_g, 0))

