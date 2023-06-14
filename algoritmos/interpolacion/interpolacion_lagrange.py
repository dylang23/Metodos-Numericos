from parsers.parsear_expression import str_to_exprsympy, simply_exprstr
import sympy as sp

# Para verificar
# https://es.planetcalc.com/9023/#:~:text=Esta%20calculadora%20en%20l%C3%ADnea%20construye%20la%20interpolaci%C3%B3n%20polin%C3%B3mica,adicionales%2C%20si%20se%20introducen%2C%20y%20traza%20un%20gr%C3%A1fico

class PolinomioLagrange:
    def __init__(self, puntos):
        self._x_valores = [punto[0] for punto in puntos]
        self._y_valores = [punto[1] for punto in puntos]

    def eval(self, valor):
        cant_puntos = len(self._x_valores)
        resultado = 0
        for i in range(cant_puntos):
            prod = 1
            for j in range(cant_puntos):
                if i != j:
                    prod *= (valor - self._x_valores[j]) / \
                        (self._x_valores[i] - self._x_valores[j])

            resultado += prod * self._y_valores[i]

        return resultado

    def polinomio(self):
        polinomio = ''
        cant_puntos = len(self._x_valores)

        for i in range(cant_puntos):
            if i != 0:
                polinomio += ' + '
            for j in range(cant_puntos):
                if i != j:
                    polinomio += '(x' + ' - ' + str(self._x_valores[j]) + ')' + '/' + '(' + str(
                        self._x_valores[i]) + ' - ' + str(self._x_valores[j]) + ')'
            polinomio += ' * ' + str(self._y_valores[i])

        return 'p(x) = ' + simply_exprstr(polinomio)


# Ejercicio 2
# puntos = [(-1, 1), (0, -1), (2, 2), (3, 2)]
# polinomio_lagrange = PolinomioLagrange(puntos)
# print(polinomio_lagrange.polinomio())
# print(polinomio_lagrange.eval(2))


# Ejercicio 3
# Con dos puntos. El punto de ebullición de la acetona es de 78.6 a atm
# puntos2 = [(1, 56.5), (5, 113.0)]
# polinomio_lagrange2 = PolinomioLagrange(puntos2)
# punto_ebullicion2 = polinomio_lagrange2.eval(2)
# print("Punto de ebullición con dos puntos: ", punto_ebullicion2)

# #Con tres puntos
# puntos3 = [(1, 56.5), (5, 113.0), (20, 181.0)]
# polinomio_lagrange3 = PolinomioLagrange(puntos3)
# punto_ebullicion3 = polinomio_lagrange3.eval(2)
# print("Punto de ebullición con tres puntos: ", punto_ebullicion3)

# #Con cuatro puntos

# puntos4 = [(1, 56.5), (5, 113.0), (20, 181.0), (40, 214.5)]
# polinomio_lagrange4 = PolinomioLagrange(puntos4)
# punto_ebullicion4 = polinomio_lagrange4.eval(2)
# print("Punto de ebullición con cuatro puntos: ", punto_ebullicion4)


# Ejercicio 4

# puntos = [(0, 1.787),  (5, 1.519), (10, 1.307),
#           (20, 1.002), (30, 0.796), (40, 0.653)]
# polinomio_lagrange = PolinomioLagrange(puntos)
# punto_viscosidad = polinomio_lagrange.eval(7.5)
# print(punto_viscosidad)
