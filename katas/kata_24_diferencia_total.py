from functools import reduce


# Kata 24: Resta de forma acumulada los números de una lista.
def diferencia_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda acumulado, numero: acumulado - numero, numeros)


if __name__ == "__main__":
    print(diferencia_total([20, 5, 3]))
