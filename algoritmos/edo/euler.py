from parsers.parsear_expression import str_to_function

def euler(funcion, intervalo, condicion_inicial=(0, 0), tam_paso=0.5):

    valor_xinicial = intervalo[0]
    valor_xfinal = intervalo[1]
    valor_yinicial = condicion_inicial[1]
    valor_ysiguiente = valor_yinicial
    euler_pasos = [(valor_xinicial, valor_yinicial)]

    while valor_xinicial < valor_xfinal:
        valor_ysiguiente =  valor_yinicial + tam_paso * funcion(valor_xinicial, valor_yinicial)
        valor_yinicial = valor_ysiguiente
        valor_xinicial += tam_paso
        euler_pasos.append((valor_xinicial, valor_ysiguiente))
    
    return euler_pasos


#funcion = str_to_function("-2*x^3 + 12*x^2 -20*x + 8.5", variables=['x', 'y'])
#print(euler(funcion, intervalo=[0, 4], condicion_inicial=(0, 1), tam_paso=0.5))

# Euler para Sistemas de Ecuaciones Diferenciales Ordinarias
def euler_sedo(ecuaciones, intervalo, condiciones_iniciales, tam_paso, pasos):

    valor_xinicial = intervalo[0]
    euler_pasos = [[valor_xinicial] + condiciones_iniciales]
    cant_ecuaciones = len(ecuaciones)
    euler_parcial = [0] * cant_ecuaciones
    
    for i in range(pasos):
        for j in range(cant_ecuaciones):
            euler_parcial[j] = euler_pasos[i][j + 1] + tam_paso * ecuaciones[j](*euler_pasos[i])    
        valor_xinicial += tam_paso
        euler_pasos.append([valor_xinicial] + euler_parcial)
    
    return euler_pasos



#ec_dif1 = str_to_function("-0.5y1", variables=['x', 'y1', 'y2'])
#ec_dif2 = str_to_function("4 -0.3y2 -0.1y1", variables=['x', 'y1', 'y2'])
#condiciones_iniciales = [4, 6]
#tam_paso = 0.5
#pasos = 4

'''
ec_dif1 = str_to_function("2*exp(t) - 2*y - z", variables=['t', 'y', 'z'])
ec_dif2 = str_to_function("y", variables=['t', 'y', 'z'])
condiciones_iniciales = [0, 1]
tam_paso = 0.1
pasos = 20

print(euler_sedo([ec_dif1, ec_dif2], [0, 2], condiciones_iniciales, tam_paso, pasos))
'''