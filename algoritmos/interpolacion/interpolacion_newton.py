
class PolinomioNewton():
    def __init__(self, puntos): 
        self._orden = len(puntos) - 1
        self._x_valores = [punto[0] for punto in puntos]
        self._coeficientes = self._calculo_coeficientes(puntos)

    def _calculo_coeficientes(self, puntos):
        orden = len(puntos) 
        x_valores = [punto[0] for punto in puntos]
        y_valores = [punto[1] for punto in puntos]
        dif_divididas = [[y_valores[i]] + [0]
                         * (orden - 1) for i in range(orden)]
        
        for i in range(1, orden):
            for j in range(i, orden):
                dif_divididas[j][i] = (
                    dif_divididas[j][i - 1] - dif_divididas[j - 1][i - 1]) / (x_valores[j] - x_valores[j - i])

        coeficientes_polinomio = [dif_divididas[i][i] for i in range(orden)]

        return coeficientes_polinomio

    def eval(self, valor):
        prod = 1
        resultado = self._coeficientes[0]
        for i in range(self._orden):
            prod *= valor - self._x_valores[i]
            resultado += prod * self._coeficientes[i + 1]
        
        return resultado

puntos = [(1, 0), (4, 1.386294), (6, 1.791759), (5, 1.609438)]

polinomio_newton = PolinomioNewton(puntos)
print(polinomio_newton.eval(2))






