# Kata 4: Resta los valores de dos listas con map().
def diferencia_listas(lista_1, lista_2):
    if len(lista_1) != len(lista_2):
        raise ValueError("Las dos listas deben tener la misma longitud.")
    return list(map(lambda valor_1, valor_2: valor_1 - valor_2, lista_1, lista_2))


if __name__ == "__main__":
    print(diferencia_listas([10, 20, 30], [1, 2, 3]))
