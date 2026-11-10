# Kata 33: Suma los elementos de dos listas que están en la misma posición.
sumar_listas = lambda lista_1, lista_2: [valor_1 + valor_2 for valor_1, valor_2 in zip(lista_1, lista_2)]


if __name__ == "__main__":
    print(sumar_listas([1, 2, 3], [4, 5, 6]))
