# Kata 9: Quita de la lista las mascotas prohibidas usando filter().
def filtrar_mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


if __name__ == "__main__":
    print(filtrar_mascotas_permitidas(["Perro", "Mapache", "Gato"]))
