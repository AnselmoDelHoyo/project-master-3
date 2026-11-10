"""Punto de entrada del proyecto.

Ejecuta cada archivo de la carpeta katas para probar un ejercicio concreto.
Por ejemplo: python katas/kata_01_frecuencia_letras.py
"""

from katas.kata_01_frecuencia_letras import frecuencia_letras


if __name__ == "__main__":
    print("Proyecto 3 - Katas Python")
    print("Cada ejercicio se ejecuta desde su propio archivo dentro de katas.")
    print(f"Ejemplo de la kata 1: {frecuencia_letras('hola mundo')}")
