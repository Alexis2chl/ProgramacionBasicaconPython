# Crear una cuadrícula de 5x5 inicializada con espacios en blanco.
grid = [[" " for _ in range(5)] for _ in range(5)]

def mostrar_cuadricula():
    for fila in grid:
        print(" | ".join(fila))
        print("-" * 9)  # Línea separadora entre filas.

# Función principal del programa
def colorear_celdas():
    while True:
        mostrar_cuadricula()  # Mostrar la cuadrícula actual.
        
        # Solicitar al usuario las coordenadas para colorear.
        try:
            fila = int(input("Ingrese el número de la fila (0-4): "))
            columna = int(input("Ingrese el número de la columna (0-4): "))
            
            # Verificar que las coordenadas estén dentro del rango válido.
            if 0 <= fila < 5 and 0 <= columna < 5:
                # Colorear la celda con el símbolo "#"
                grid[fila][columna] = "#"
            else:
                print("¡Coordenadas fuera de rango! Las filas y columnas deben ser entre 0 y 4.")
            
        except ValueError:
            print("Por favor ingrese valores válidos (números enteros).")
        
        # Preguntar si el usuario quiere continuar o salir.
        continuar = input("¿Quieres colorear otra celda? (s/n): ").lower()
        if continuar != 's':
            break

# Ejecutar el programa
colorear_celdas()
