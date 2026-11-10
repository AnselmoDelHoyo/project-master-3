from functools import reduce


# Kata 17: Convierte una lista de dígitos en el número que representan.
def digitos_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)


if __name__ == "__main__":
    print(digitos_a_numero([5, 7, 2]))
