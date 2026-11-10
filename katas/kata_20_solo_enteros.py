# Kata 20: Conserva solo los valores de tipo int usando filter().
def solo_enteros(valores):
    return list(filter(lambda valor: isinstance(valor, int) and not isinstance(valor, bool), valores))


if __name__ == "__main__":
    print(solo_enteros([1, "dos", 3, "cuatro"]))
