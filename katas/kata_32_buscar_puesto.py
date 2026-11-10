# Kata 32: Devuelve el puesto de una persona si aparece en la lista de empleados.
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."


if __name__ == "__main__":
    empleados = [{"nombre": "Ana Ruiz", "puesto": "Desarrolladora"}]
    print(buscar_puesto("Ana Ruiz", empleados))
