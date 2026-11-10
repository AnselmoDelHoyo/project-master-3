# Kata 28: Busca el primer elemento que aparece repetido.
def primer_duplicado(elementos):
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


if __name__ == "__main__":
    print(primer_duplicado([1, 2, 3, 2, 4]))
