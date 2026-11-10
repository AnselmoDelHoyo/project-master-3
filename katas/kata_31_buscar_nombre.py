# Kata 31: Busca un nombre introducido por el usuario dentro de una lista.
def buscar_nombre():
    nombres = [nombre.strip() for nombre in input("Nombres separados por comas: ").split(",")]
    nombre_buscado = input("Nombre que quieres buscar: ").strip()
    if nombre_buscado not in nombres:
        raise ValueError("El nombre no está en la lista.")
    print(f"{nombre_buscado} ha sido encontrado.")


if __name__ == "__main__":
    try:
        buscar_nombre()
    except ValueError as error:
        print(error)
