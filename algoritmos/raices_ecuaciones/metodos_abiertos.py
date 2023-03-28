from .iteracion import IteracionNewton, IteracionPuntoFijo, IteracionSecante
from typing import List


def punto_fijo(funcion_f, funcion_g, valor_inicial, cant_iter=100, error_aceptado=1e-5) -> List[IteracionPuntoFijo]:

    raiz_aprox = valor_inicial
    iteraciones = []

    for _ in range(cant_iter):

        raiz_aprox_prev = raiz_aprox
        raiz_aprox = funcion_g(raiz_aprox_prev)
        error_calculado = abs((raiz_aprox - raiz_aprox_prev) / raiz_aprox)

        iteraciones.append(IteracionPuntoFijo(
            raiz_aprox_prev, raiz_aprox, funcion_f(raiz_aprox_prev), error_calculado))

        if error_calculado < error_aceptado:
            break

    return iteraciones


def newton(funcion_f, derivada_f, valor_inicial, cant_iter=100, error_aceptado=1e-5) -> List[IteracionNewton]:

    raiz_aprox = valor_inicial
    iteraciones = []

    for _ in range(cant_iter):

        raiz_aprox_prev = raiz_aprox
        if derivada_f(raiz_aprox_prev) == 0:
            break

        raiz_aprox = raiz_aprox_prev - \
            funcion_f(raiz_aprox_prev) / derivada_f(raiz_aprox_prev)
        error_calculado = abs(raiz_aprox - raiz_aprox_prev)

        iteraciones.append(IteracionNewton(raiz_aprox, raiz_aprox_prev, funcion_f(
            raiz_aprox_prev), derivada_f(raiz_aprox), error_calculado))

        # if funcion_f(raiz_aprox) < error_aceptado: break
        if error_calculado < error_aceptado:
            break

    return iteraciones


def secante(funcion_f, valor_inicial, valor_sig, cant_iter=100, error_aceptado=1e-5) -> List[IteracionSecante]:

    iteraciones = []
    for _ in range(cant_iter):

        if funcion_f(valor_inicial) == funcion_f(valor_sig):
            break

        raiz_aprox = valor_inicial - \
            funcion_f(valor_inicial)*(valor_inicial - valor_sig) / \
            (funcion_f(valor_inicial) - funcion_f(valor_sig))

        error_calculado = abs(raiz_aprox - valor_sig)

        iteraciones.append(IteracionSecante(
            valor_inicial, valor_sig, raiz_aprox, error_calculado, funcion_f(raiz_aprox)))

        if error_calculado < error_aceptado:
            break

        valor_inicial = valor_sig
        valor_sig = raiz_aprox

    return iteraciones
