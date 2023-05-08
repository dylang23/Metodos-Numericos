from parsers.parsear_expression import str_to_function


def rk_cuarto_orden(funcion, intervalo, condicion_inicial, tam_paso):

    valor_xinicial = intervalo[0]
    valor_xfinal = intervalo[1]
    valor_yinicial = condicion_inicial[1]
    print(valor_xinicial, valor_yinicial)
    while valor_xinicial < valor_xfinal:
        k1 = funcion(valor_xinicial, valor_yinicial)
        k2 = funcion(valor_xinicial + tam_paso / 2,
                     valor_yinicial + (k1 * tam_paso) / 2)
        k3 = funcion(valor_xinicial + tam_paso / 2,
                     valor_yinicial + (k2 * tam_paso) / 2)
        k4 = funcion(valor_xinicial + tam_paso, valor_yinicial + k3 * tam_paso)
        #print(k1, k2, k3, k4)
        pendiente = (k1 + 2*(k2 + k3) + k4) / 6
        valor_ysiguiente = valor_yinicial + pendiente * tam_paso
        valor_yinicial = valor_ysiguiente
        valor_xinicial += tam_paso
        print(valor_xinicial, valor_ysiguiente)


def rk_cuarto_orden_sedo(funciones, intervalo, condiciones_iniciales, tam_paso, pasos):
    
    def kvalor(k, nro_funcion):
        if k == 1:
            pass
    
    valor_xinicial = intervalo[0]
    rk_pasos = [[valor_xinicial] + condiciones_iniciales]
    cant_funciones = len(funciones)
    rk_parcial = [0] * cant_funciones
    rk_kvalores = [[0] * cant_funciones for _ in range(4)]

    for i in range(pasos):
        # Calculo de los k-valores
       # print("Paso", i + 1)
        for k in range(4):
            for j in range(cant_funciones):
                if k == 0:
                    rk_kvalores[k][j] = funciones[j](*rk_pasos[i])
                if k == 1:                                     
                    valores = [ valor_xinicial + tam_paso/2 ] + [rk_pasos[i][j + 1] + (rk_kvalores[k-1][j] * tam_paso) / 2 for j in range(cant_funciones)]
                    rk_kvalores[k][j] = funciones[j](*valores)
                if k == 2:
                    valores = [ valor_xinicial + tam_paso/2 ] + [rk_pasos[i][j + 1] + (rk_kvalores[k-1][j] * tam_paso) / 2 for j in range(cant_funciones)]
                    rk_kvalores[k][j] = funciones[j](*valores)
                if k == 3:
                    valores = [ valor_xinicial + tam_paso ] + [rk_pasos[i][j + 1] + (rk_kvalores[k-1][j] * tam_paso) for j in range(cant_funciones)]
                    rk_kvalores[k][j] = funciones[j](*valores)
        #        print("k", k + 1, j+1, " ", rk_kvalores[k][j])

        for j in range(cant_funciones):
            pendiente = (rk_kvalores[0][j] + 2 * (rk_kvalores[1][j] + rk_kvalores[2][j]) + rk_kvalores[3][j]) / 6
            rk_parcial[j] = rk_pasos[i][j + 1] + tam_paso * pendiente
        
        valor_xinicial += tam_paso
        rk_pasos.append([valor_xinicial] + rk_parcial)

    return rk_pasos
#funcion = str_to_function("-2*x^3 + 12*x^2 - 20*x + 8.5", variables=['x', 'y'])
#print(rk_cuarto_orden(funcion, [0, 4], (0, 1), 0.5))

#funcion = str_to_function("3*exp(-t) + 0.4*y", variables=['t', 'y'])
#rk_cuarto_orden(funcion, [0,3], (0, 5), 0.1)

#ec_dif1 = str_to_function("-0.5y1", variables=['x', 'y1', 'y2'])
#ec_dif2 = str_to_function("4 -0.3y2 -0.1y1", variables=['x', 'y1', 'y2'])
#condiciones_iniciales = [4, 6]
#tam_paso = 0.5
#pasos = 4

#print(rk_cuarto_orden_sedo([ec_dif1, ec_dif2], [0, 2], condiciones_iniciales, tam_paso, pasos))


'''
ec_dif1 = str_to_function("y", variables=['t', 'z', 'y'])
ec_dif2 = str_to_function("2*exp(t) - 2*y - z", variables=['t', 'z', 'y'])

condiciones_iniciales = [0, 1]
tam_paso = 0.1
pasos = 20

print(rk_cuarto_orden_sedo([ec_dif1, ec_dif2], [0, 2], condiciones_iniciales, tam_paso, pasos))
'''