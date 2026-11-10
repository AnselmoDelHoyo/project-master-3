from functools import reduce


# Kata 22: Multiplica todos los valores de una lista usando reduce().
def producto_total(numeros):
    return reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)


if __name__ == "__main__":
    print(producto_total([2, 3, 4]))
