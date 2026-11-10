# Kata 12: Devuelve la longitud de cada palabra usando map().
def longitud_palabras(frase):
    return list(map(len, frase.split()))


if __name__ == "__main__":
    print(longitud_palabras("Python es muy útil"))
