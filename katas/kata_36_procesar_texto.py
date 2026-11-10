# Kata 36: Cuenta, reemplaza o elimina palabras de un texto.
def contar_palabras(texto):
    resultado = {}
    for palabra in texto.lower().split():
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    return " ".join(item for item in texto.split() if item != palabra)


def procesar_texto(texto, opcion, *argumentos):
    if opcion == "contar":
        return contar_palabras(texto)
    if opcion == "reemplazar" and len(argumentos) == 2:
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    if opcion == "eliminar" and len(argumentos) == 1:
        return eliminar_palabra(texto, argumentos[0])
    raise ValueError("Opción o argumentos no válidos.")


if __name__ == "__main__":
    print(procesar_texto("hola hola mundo", "contar"))
