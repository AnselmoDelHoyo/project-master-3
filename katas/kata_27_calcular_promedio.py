# Kata 27: Calcula el promedio de una lista de números.
def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    print(calcular_promedio([4, 6, 8]))
