import random

# Lista de símbolos que se utilizarán para el collage
symbols = ["#", "*", "@", "&", "%", "$", "+", "!", "?", "~"]

# Función para generar y mostrar el collage
def generar_collage(tamano):
    for y in range(tamano):
        line = ""
        for x in range(tamano):
            line += random.choice(symbols) + " "  # Seleccionar un símbolo aleatorio y añadirlo a la línea
        print(line)  # Imprimir la línea con los símbolos

# Tamaño de la cuadrícula (10x10)
tamano = 10
generar_collage(tamano)
