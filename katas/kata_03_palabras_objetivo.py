# Kata 3: Devuelve las palabras que contienen un texto objetivo.
def palabras_con_objetivo(palabras, objetivo):
    return [palabra for palabra in palabras if objetivo in palabra]


if __name__ == "__main__":
    print(palabras_con_objetivo(["casa", "caseta", "perro"], "casa"))
