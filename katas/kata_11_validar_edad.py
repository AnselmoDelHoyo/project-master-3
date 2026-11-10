# Kata 11: Pide una edad y comprueba que esté entre 0 y 120.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if not 0 <= edad <= 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        return edad
    except ValueError as error:
        print(f"Edad no válida: {error}")
        return None


if __name__ == "__main__":
    print(pedir_edad())
