# Kata 18: Filtra estudiantes con calificación mayor o igual a 90.
def estudiantes_destacados(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


if __name__ == "__main__":
    estudiantes = [{"nombre": "Ana", "edad": 20, "calificacion": 95}]
    print(estudiantes_destacados(estudiantes))
