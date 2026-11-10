# Kata 6: Calcula el factorial de un número de forma recursiva.
def factorial(numero):
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if numero in (0, 1):
        return 1
    return numero * factorial(numero - 1)


if __name__ == "__main__":
    print(factorial(5))
