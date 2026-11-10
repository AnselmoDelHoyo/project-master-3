# Kata 19: Filtra los números impares con una lambda.
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


if __name__ == "__main__":
    print(filtrar_impares([1, 2, 3, 4, 5]))
