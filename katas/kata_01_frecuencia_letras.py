# Kata 1: Frecuencia de letras sin contar espacios.
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


if __name__ == "__main__":
    print(frecuencia_letras("hola mundo"))
