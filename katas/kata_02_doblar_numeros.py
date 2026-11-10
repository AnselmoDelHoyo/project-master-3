# Kata 2: Dobla cada número de una lista usando map().
def doblar_numeros(numeros):
    return list(map(lambda numero: numero * 2, numeros))


if __name__ == "__main__":
    print(doblar_numeros([1, 2, 3]))
