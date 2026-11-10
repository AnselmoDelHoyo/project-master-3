# Kata 38: Convierte una calificación numérica en texto.
def calificacion_en_texto(calificacion):
    if not 0 <= calificacion <= 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")
    if calificacion < 70:
        return "insuficiente"
    if calificacion < 80:
        return "bien"
    if calificacion < 90:
        return "muy bien"
    return "excelente"


if __name__ == "__main__":
    print(calificacion_en_texto(86))
