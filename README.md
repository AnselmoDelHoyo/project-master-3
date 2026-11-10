# Proyecto 3 - Katas Python

En este repositorio voy reuniendo las soluciones de las katas del Proyecto 3 de Python.

La idea es practicar funciones, listas, diccionarios, condicionales, bucles,
excepciones, clases y el uso de `map`, `filter` y `reduce`.

## Organización

Cada ejercicio tiene su propio archivo dentro de la carpeta `katas`. Así puedo abrir
y ejecutar una kata sin tener que buscarla entre cientos de líneas de código.

```text
Proyecto 3 - Katas - Python/
├── katas/
│   ├── kata_01_frecuencia_letras.py
│   ├── kata_02_doblar_numeros.py
│   └── ...
├── main.py
├── README.md
└── requirements.txt
```

Cada archivo contiene el enunciado como comentario, una función con la solución y
un ejemplo sencillo al final.

## Ejecución

Puedes ejecutar una kata concreta desde la terminal integrada de Visual Studio Code:

```powershell
python katas/kata_01_frecuencia_letras.py
```

También puedes ejecutar el punto de entrada del proyecto:

```powershell
python main.py
```

No se han usado librerías externas, así que no hay nada que instalar.
