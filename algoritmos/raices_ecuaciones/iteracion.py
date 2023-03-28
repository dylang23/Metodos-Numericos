class Iteracion:

    def __init__(self, raiz_aprox, error_calculado, funcion_valuada=None, lim_inf=None, lim_sup=None):
        self._raiz_aprox = raiz_aprox
        self._error_calculado = error_calculado
        self._lim_inf = lim_inf
        self._lim_sup = lim_sup
        self._funcion_valuada = funcion_valuada

    @property
    def raiz_aprox(self):
        return self._raiz_aprox

    @property
    def error_calculado(self):
        return self._error_calculado

    @property
    def lim_inf(self):
        return self._lim_inf

    @property
    def lim_sup(self):
        return self._lim_sup

    @property
    def funcion_valuada(self):
        return self._funcion_valuada


class IteracionBiseccion(Iteracion):
    def __init__(self, raiz_aprox, error_calculado, funcion_valuada=None, lim_inf=None, lim_sup=None):
        super().__init__(raiz_aprox, error_calculado, funcion_valuada, lim_inf, lim_sup)


class IteracionRegulaFalsi(Iteracion):
    def __init__(self, raiz_aprox, error_calculado, funcion_valuada=None, lim_inf=None, lim_sup=None):
        super().__init__(raiz_aprox, error_calculado, funcion_valuada, lim_inf, lim_sup)


class IteracionPuntoFijo:
    def __init__(self, raiz_aprox_prev, raiz_aprox, funcion_valuada, error_calculado):
        self._raiz_aprox = raiz_aprox
        self._raiz_aprox_prev = raiz_aprox_prev
        self._funcion_valuada = funcion_valuada
        self._error_calculado = error_calculado

    @property
    def raiz_aprox(self):
        return self._raiz_aprox

    @property
    def raiz_aprox_prev(self):
        return self._raiz_aprox_prev

    @property
    def funcion_valuada(self):
        return self._funcion_valuada

    @property
    def error_calculado(self):
        return self._error_calculado


class IteracionSecante:
    def __init__(self, valor_ini, valor_sig, raiz_aprox, error_calculado, funcion_valuada):
        self._valor_ini = valor_ini
        self._valor_sig = valor_sig
        self._raiz_aprox = raiz_aprox
        self._error_calculado = error_calculado
        self._funcion_valuada = funcion_valuada

    @property
    def valor_ini(self):
        return self._valor_ini

    @property
    def valor_sig(self):
        return self._valor_sig

    @property
    def raiz_aprox(self):
        return self._raiz_aprox

    @property
    def error_calculado(self):
        return self._error_calculado

    @property
    def funcion_valuada(self):
        return self._funcion_valuada


class IteracionNewton:
    def __init__(self, raiz_aprox, raiz_aprox_prev, funcion_valuada, derivada_valuada, error_calculado):
        self._raiz_aprox = raiz_aprox
        self._raiz_aprox_prev = raiz_aprox_prev
        self._funcion_valuada = funcion_valuada
        self._derivada_valuda = derivada_valuada
        self._error_calculado = error_calculado

    @property
    def raiz_aprox(self):
        return self._raiz_aprox

    @property
    def raiz_aprox_prev(self):
        return self._raiz_aprox_prev

    @property
    def funcion_valuada(self):
        return self._funcion_valuada

    @property
    def derivada_valuada(self):
        return self._derivada_valuda

    @property
    def error_calculado(self):
        return self._error_calculado
