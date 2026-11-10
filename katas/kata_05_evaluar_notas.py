# Kata 5: Calcula la media y decide si está aprobado o suspenso.
def evaluar_notas(notas, nota_aprobado=5):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


if __name__ == "__main__":
    print(evaluar_notas([4, 5, 8]))
