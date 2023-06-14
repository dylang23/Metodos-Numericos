from parsers.parsear_expression import str_to_function

def multiple_trapecio(funcion, intervalo):
    lim_inf = intervalo[0]
    lim_sup = intervalo[1]
    x = lim_inf
    paso = (lim_sup - lim_inf) / 2
    nro_pasos = int((lim_sup - lim_inf) / paso)
    sum = funcion(x)

    for i in range(nro_pasos - 1):
        x += paso
        sum = sum + 2 * funcion(x)
    
    sum += funcion(lim_sup)

    resultado = (lim_sup - lim_inf) * sum / (2 * nro_pasos)

    return resultado

function_str = '0.2 + 25x - 200x**2 + 675x**3 - 900x**4 + 400x**5'

funcion = str_to_function(function_str)

# print(multiple_trapecio(funcion, [0, 0.8]))