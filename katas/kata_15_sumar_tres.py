# Kata 15: Suma tres a cada número de una lista con una función lambda.
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


if __name__ == "__main__":
    print(sumar_tres([1, 2, 3]))
