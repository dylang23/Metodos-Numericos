class Iteracion:

    def __init__(self, raiz_aprox, error_calculado, funcion_valuada=None, lim_inf=None, lim_sup=None):
        self._raiz_aprox = raiz_aprox
        self._error_calculado = error_calculado
        self._lim_inf = lim_inf
        self._lim_sup = lim_sup
        self._funcion_valuada = funcion_valuada

    @property
    def raiz_aprox(self, cifras_decimal=6):
        return round(self._raiz_aprox, cifras_decimal)

    @property
    def error_calculado(self, cifras_decimal=6):
        return round(self._error_calculado, cifras_decimal)

    @property
    def lim_inf(self, cifras_decimal=6):
        return round(self._lim_inf, cifras_decimal)

    @property
    def lim_sup(self, cifras_decimal=6):
        return round(self._lim_sup, cifras_decimal)

    @property
    def funcion_valuada(self, cifras_decimal=6):
        return round(self._funcion_valuada, cifras_decimal)

    def __str__(self) -> str:
        return "{}   ,{}   ,{}    ,{}   ,{}".format(self.raiz_aprox, self.error_calculado, self.funcion_valuada, self.lim_inf, self.lim_sup)
