from algoritmos.edo.euler import euler_sedo
from algoritmos.edo.runge_kutta import rk_cuarto_orden_sedo
from parsers.parsear_expression import str_to_function

ec_diff1 = str_to_function("4x - y", ['t', 'x', 'y'])
ec_diff2 = str_to_function("3x - 2y", ['t', 'x', 'y'])
condiciones_iniciales = [1, 3]
intervalo = [0, 2.5]
pasos = 250
tam_paso = 0.01

resultados = euler_sedo([ec_diff1, ec_diff2], intervalo, condiciones_iniciales, tam_paso, pasos)
print("Euler")
print(resultados)


print("Rk order 4")
resultados = rk_cuarto_orden_sedo([ec_diff1, ec_diff2], intervalo, condiciones_iniciales, tam_paso, pasos)
print(resultados)