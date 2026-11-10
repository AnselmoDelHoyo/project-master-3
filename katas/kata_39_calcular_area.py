# Kata 39: Calcula el área de un rectángulo, círculo o triángulo.
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    if figura == "circulo":
        (radio,) = datos
        return 3.1416 * radio ** 2
    if figura == "triangulo":
        base, altura = datos
        return base * altura / 2
    raise ValueError("La figura debe ser rectangulo, circulo o triangulo.")


if __name__ == "__main__":
    print(calcular_area("triangulo", (4, 6)))
