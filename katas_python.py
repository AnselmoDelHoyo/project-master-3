"""Soluciones del Proyecto 3: Katas Python."""

from functools import reduce


# ---------------------------------------------------------------------------
# 1. FUNCIONES, TIPOS DE DATOS Y COLECCIONES
# ---------------------------------------------------------------------------

# Kata 1: Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra. Los espacios no se
# deben considerar.
def frecuencia_letras(texto):
    """Cuenta cuántas veces aparece cada carácter, sin contar espacios."""
    frecuencias = {}

    for letra in texto:
        if letra != " ":
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


# Kata 2: Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map().
def doblar_numeros(numeros):
    """Devuelve una lista con el doble de cada número."""
    return list(map(lambda numero: numero * 2, numeros))


# Kata 3: Escribe una función que tome una lista de palabras y una palabra
# objetivo. La función debe devolver las palabras que contengan ese objetivo.
def palabras_con_objetivo(palabras, objetivo):
    """Busca las palabras que contienen el texto objetivo."""
    return [palabra for palabra in palabras if objetivo in palabra]


# Kata 4: Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map().
def diferencia_listas(lista_1, lista_2):
    """Resta los elementos de dos listas que están en la misma posición."""
    if len(lista_1) != len(lista_2):
        raise ValueError("Las dos listas deben tener la misma longitud.")

    return list(map(lambda valor_1, valor_2: valor_1 - valor_2, lista_1, lista_2))


# Kata 5: Escribe una función que calcule la media de una lista y devuelva una
# tupla con la media y el estado aprobado o suspenso.
def evaluar_notas(notas, nota_aprobado=5):
    """Calcula la media de las notas y comprueba si se ha aprobado."""
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")

    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# Kata 6: Escribe una función que calcule el factorial de un número de manera
# recursiva.
def factorial(numero):
    """Calcula el factorial de un entero no negativo de forma recursiva."""
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if numero in (0, 1):
        return 1

    return numero * factorial(numero - 1)


# Kata 7: Genera una función que convierta una lista de tuplas a una lista de
# strings. Usa la función map().
def tuplas_a_strings(tuplas):
    """Convierte cada tupla en un texto, separando sus valores con espacios."""
    return list(map(lambda tupla: " ".join(map(str, tupla)), tuplas))


# ---------------------------------------------------------------------------
# 2. MAP, FILTER, REDUCE Y FUNCIONES LAMBDA
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 3. EXCEPCIONES Y VALIDACIONES
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 4. PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 5. CONDICIONALES
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    # Las llamadas de ejemplo se irán añadiendo al completar cada bloque.
    pass

# ---------------------------------------------------------------------------
# 2. MAP, FILTER, REDUCE Y FUNCIONES LAMBDA
# ---------------------------------------------------------------------------

# Kata 9: Excluye mascotas prohibidas usando filter().
def filtrar_mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


# Kata 12: Devuelve la longitud de cada palabra de una frase usando map().
def longitud_palabras(frase):
    return list(map(len, frase.split()))


# Kata 13: Devuelve cada letra sin repetir en mayúscula y minúscula.
def letras_mayusculas_minusculas(caracteres):
    letras_sin_repetir = set(caracteres)
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_sin_repetir))


# Kata 14: Devuelve las palabras que comienzan con una letra concreta.
def palabras_por_letra(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))


# Kata 15: Suma tres a cada número de una lista con una lambda.
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# Kata 16: Devuelve las palabras de un texto con más de n caracteres.
def palabras_mas_largas(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# Kata 17: Convierte una lista de dígitos en el número que representan.
def digitos_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)


# Kata 18: Filtra estudiantes con una calificación de 90 o superior.
def estudiantes_destacados(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


# Kata 19: Filtra los números impares de una lista con una lambda.
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# Kata 20: Devuelve únicamente los valores enteros de una lista.
def solo_enteros(valores):
    return list(filter(lambda valor: isinstance(valor, int) and not isinstance(valor, bool), valores))


# Kata 21: Calcula el cubo de un número mediante una lambda.
cubo = lambda numero: numero ** 3


# Kata 22: Obtiene el producto total de una lista usando reduce().
def producto_total(numeros):
    return reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)


# Kata 23: Concatena una lista de palabras usando reduce().
def concatenar_palabras(palabras):
    return reduce(lambda acumulado, palabra: acumulado + palabra, palabras, "")


# Kata 24: Calcula la resta acumulada de los elementos de una lista.
def diferencia_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda acumulado, numero: acumulado - numero, numeros)


# Kata 26: Calcula el resto de una división mediante una lambda.
resto_division = lambda dividendo, divisor: dividendo % divisor


# Kata 33: Suma los elementos correspondientes de dos listas.
sumar_listas = lambda lista_1, lista_2: list(map(lambda valores: valores[0] + valores[1], zip(lista_1, lista_2)))


# ---------------------------------------------------------------------------
# 3. EXCEPCIONES Y VALIDACIONES
# ---------------------------------------------------------------------------

# Kata 8: Divide dos números introducidos por el usuario y controla errores.
def division_segura():
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        print(f"El resultado es: {dividendo / divisor}")
    except ValueError:
        print("Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")


# Kata 10: Excepción personalizada para una lista vacía.
class ListaVaciaError(Exception):
    """Se usa cuando no se puede calcular un promedio sin números."""


def promedio_con_error(numeros):
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


# Kata 11: Pide una edad y valida que esté dentro de un rango razonable.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if not 0 <= edad <= 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        return edad
    except ValueError as error:
        print(f"Edad no válida: {error}")
        return None


# Kata 25: Cuenta los caracteres de un texto.
def contar_caracteres(texto):
    return len(texto)


# Kata 27: Calcula el promedio de una lista de números.
def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)


# Kata 28: Busca el primer elemento duplicado de una lista.
def primer_duplicado(elementos):
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# Kata 29: Enmascara todo el texto salvo sus últimos cuatro caracteres.
def enmascarar_variable(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


# Kata 30: Comprueba si dos palabras son anagramas.
def son_anagramas(palabra_1, palabra_2):
    normalizada_1 = palabra_1.replace(" ", "").lower()
    normalizada_2 = palabra_2.replace(" ", "").lower()
    return sorted(normalizada_1) == sorted(normalizada_2)


# Kata 31: Busca un nombre introducido por el usuario dentro de una lista.
def buscar_nombre():
    nombres = input("Introduce nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_buscado = input("Nombre que quieres buscar: ").strip()
    if nombre_buscado not in nombres:
        raise ValueError("El nombre no está en la lista.")
    print(f"{nombre_buscado} ha sido encontrado.")


# Kata 32: Busca el puesto de una persona dentro de una lista de empleados.
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."

# ---------------------------------------------------------------------------
# 4. PROGRAMACIÓN ORIENTADA A OBJETOS
# ---------------------------------------------------------------------------

# Kata 34: Clase Arbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if not 0 <= posicion < len(self.ramas):
            raise IndexError("La posición de la rama no existe.")
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas,
        }


# Kata 35: Clase UsuarioBanco.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0 or cantidad > self.saldo:
            raise ValueError("No es posible retirar esa cantidad.")
        self.saldo -= cantidad

    def transferir_dinero(self, destinatario, cantidad):
        self.retirar_dinero(cantidad)
        destinatario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.saldo += cantidad


# Kata 36: Procesa texto según una opción.
def contar_palabras(texto):
    contador = {}
    for palabra in texto.lower().split():
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    return " ".join(item for item in texto.split() if item != palabra)


def procesar_texto(texto, opcion, *argumentos):
    if opcion == "contar":
        return contar_palabras(texto)
    if opcion == "reemplazar":
        if len(argumentos) != 2:
            raise ValueError("Debes indicar la palabra original y la nueva.")
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    if opcion == "eliminar":
        if len(argumentos) != 1:
            raise ValueError("Debes indicar la palabra que quieres eliminar.")
        return eliminar_palabra(texto, argumentos[0])
    raise ValueError("La opción debe ser contar, reemplazar o eliminar.")


# ---------------------------------------------------------------------------
# 5. CONDICIONALES
# ---------------------------------------------------------------------------

# Kata 37: Indica si es de mañana, tarde o noche según la hora.
def momento_del_dia(hora):
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 12:
        return "día"
    if 12 <= hora < 20:
        return "tarde"
    return "noche"


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


# Kata 40: Calcula el precio final aplicando un cupón válido.
def calcular_precio_final(precio, tiene_cupon, cupon=0):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if tiene_cupon and cupon > 0:
        return max(0, precio - cupon)
    return precio
