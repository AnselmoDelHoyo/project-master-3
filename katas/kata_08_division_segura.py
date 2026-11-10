# Kata 8: Divide dos números y controla errores de entrada.
def division_segura():
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        print(f"El resultado es: {dividendo / divisor}")
    except ValueError:
        print("Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")


if __name__ == "__main__":
    division_segura()
