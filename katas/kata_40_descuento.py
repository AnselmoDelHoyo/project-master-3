# Kata 40: Calcula el precio final con un cupón válido.
def calcular_precio_final(precio, tiene_cupon, cupon=0):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if tiene_cupon and cupon > 0:
        return max(0, precio - cupon)
    return precio


if __name__ == "__main__":
    try:
        precio = float(input("Precio original: "))
        respuesta = input("¿Tienes cupón? (si/no): ").strip().lower()
        cupon = float(input("Valor del cupón: ")) if respuesta == "si" else 0
        print(f"Precio final: {calcular_precio_final(precio, respuesta == 'si', cupon):.2f} €")
    except ValueError:
        print("Debes introducir un precio y un cupón válidos.")
