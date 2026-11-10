# Kata 37: Indica si es día, tarde o noche según la hora.
def momento_del_dia(hora):
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 12:
        return "día"
    if 12 <= hora < 20:
        return "tarde"
    return "noche"


if __name__ == "__main__":
    print(momento_del_dia(16))
