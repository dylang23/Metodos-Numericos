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
    

puntos = [(1, 0), (4, 1.386294), (6, 1.791759), (5, 1.609438)]

polinomio_newton = PolinomioLagrange(puntos)
print(polinomio_newton.eval(2))

