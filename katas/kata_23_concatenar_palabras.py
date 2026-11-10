from functools import reduce


# Kata 23: Concatena una lista de palabras usando reduce().
def concatenar_palabras(palabras):
    return reduce(lambda acumulado, palabra: acumulado + palabra, palabras, "")


if __name__ == "__main__":
    print(concatenar_palabras(["Hola", " ", "mundo"]))
