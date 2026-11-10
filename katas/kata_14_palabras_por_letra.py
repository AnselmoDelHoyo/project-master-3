# Kata 14: Filtra palabras que comienzan con una letra usando filter().
def palabras_por_letra(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))


if __name__ == "__main__":
    print(palabras_por_letra(["Ana", "Alba", "Luis"], "a"))
