def dibujar_circulos_concentricos(tamano):
    # Crear una cuadrícula de tamaño (2*tamano+1) x (2*tamano+1) centrada en (tamano, tamano)
    for i in range(2 * tamano + 1):
        for j in range(2 * tamano + 1):
            # Calcular la distancia al centro
            distancia = max(abs(i - tamano), abs(j - tamano))
            
            # Si la distancia es igual al radio del círculo actual, dibujar el borde
            if distancia <= tamano:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Solicitar al usuario el tamaño de los círculos concéntricos
tamano = int(input("Ingrese el tamaño de los círculos concéntricos (radio máximo): "))
dibujar_circulos_concentricos(tamano)
