# Kata 29: Oculta todos los caracteres salvo los últimos cuatro.
def enmascarar_variable(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


if __name__ == "__main__":
    print(enmascarar_variable("12345678"))
