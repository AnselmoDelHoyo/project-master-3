# Kata 30: Comprueba si dos palabras son anagramas.
def son_anagramas(palabra_1, palabra_2):
    palabra_1 = palabra_1.replace(" ", "").lower()
    palabra_2 = palabra_2.replace(" ", "").lower()
    return sorted(palabra_1) == sorted(palabra_2)


if __name__ == "__main__":
    print(son_anagramas("Roma", "amor"))
