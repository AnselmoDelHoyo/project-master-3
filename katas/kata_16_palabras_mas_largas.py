# Kata 16: Devuelve las palabras de un texto que tienen más de n caracteres.
def palabras_mas_largas(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


if __name__ == "__main__":
    print(palabras_mas_largas("Python permite crear programas", 5))
