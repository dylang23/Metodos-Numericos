from algoritmos.edo.euler import euler_sedo
from algoritmos.edo.runge_kutta import rk_cuarto_orden_sedo
from parsers.parsear_expression import str_to_function



ec_diff1 = str_to_function("y", variables=['t', 'z', 'y'])
ec_diff2 = str_to_function("2*exp(t) - 2y - z", variables=['t', 'z', 'y'])
condiciones_iniciales = [0, 1]
intervalo = [0, 2]
tam_paso = 0.1
pasos = 20

print("Resolución con método de euler para sistemas")
euler_pasos = euler_sedo([ec_diff1, ec_diff2], intervalo, condiciones_iniciales, tam_paso, pasos)

for euler_paso in euler_pasos:
    print(round(euler_paso[0], 2), round(euler_paso[1], 2), round(euler_paso[2], 2))


print("Resolución con método de rk order 4 para sistemas")
rk_pasos = rk_cuarto_orden_sedo([ec_diff1, ec_diff2], intervalo, condiciones_iniciales, tam_paso, pasos)
for rk_paso in rk_pasos:
    print(round(rk_paso[0], 2), round(rk_paso[1], 2), round(rk_paso[2], 2))
