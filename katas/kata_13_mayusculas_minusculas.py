# Kata 13: Devuelve cada letra sin repetir en mayúscula y minúscula.
def letras_mayusculas_minusculas(caracteres):
    return list(map(lambda letra: (letra.upper(), letra.lower()), set(caracteres)))


if __name__ == "__main__":
    print(letras_mayusculas_minusculas("aabbc"))
