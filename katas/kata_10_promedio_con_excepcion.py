# Kata 10: Lanza una excepción propia si no hay números para calcular la media.
class ListaVaciaError(Exception):
    pass


def promedio_con_error(numeros):
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    try:
        print(promedio_con_error([]))
    except ListaVaciaError as error:
        print(error)
