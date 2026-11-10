# Kata 7: Convierte una lista de tuplas en una lista de textos usando map().
def tuplas_a_strings(tuplas):
    return list(map(lambda tupla: " ".join(map(str, tupla)), tuplas))


if __name__ == "__main__":
    print(tuplas_a_strings([("Ana", 20), ("Luis", 22)]))
