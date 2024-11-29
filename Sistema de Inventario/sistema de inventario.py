from tabulate import tabulate   # type: ignore

# Inicialización del inventario
inventario = {
    "Nike": [10, 100.0, "NIK123", 80.0],
    "Sketchers": [5, 120.0, "SKE456", 90.0],
    "Puma": [8, 110.0, "PUM789", 85.0],
    "Adidas": [7, 130.0, "ADI321", 100.0],
    "Converse": [6, 150.0, "CON654", 120.0]
}

# Función para mostrar el inventario en formato de tabla
def mostrar_inventario(inventario):
    headers = ["Producto", "Stock", "Precio", "Código", "Costo Unitario"]
    table = [[prod] + datos for prod, datos in inventario.items()]
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Menú interactivo
opc = ""
while opc != "s":
    print("\nMenú de Inventario")
    print("1- Agregar producto")
    print("2- Eliminar producto")
    print("3- Buscar producto")
    print("4- Mostrar inventario")
    print("s- Salir")
    opc = input("Ingrese una opción: ").lower()

    if opc == "1":  # Agregar producto
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            print("El producto ya existe en el inventario.")
        else:
            stock = int(input(f"Ingrese la cantidad inicial de stock para {producto}: "))
            precio = float(input(f"Ingrese el precio del producto {producto}: "))
            codigo = input(f"Ingrese el código del producto {producto}: ")
            costo_unitario = float(input(f"Ingrese el costo unitario del producto {producto}: "))

            # Agregar producto al inventario
            inventario[producto] = [stock, precio, codigo, costo_unitario]
            print(f"Producto {producto} agregado con éxito.")

    elif opc == "2":  # Eliminar producto
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in inventario:
            del inventario[producto]
            print(f"Producto {producto} eliminado con éxito.")
        else:
            print("El producto no existe en el inventario.")

    elif opc == "3":  # Buscar producto
        producto = input("Ingrese el nombre del producto a buscar: ")
        if producto in inventario:
            headers = ["Producto", "Stock", "Precio", "Código", "Costo Unitario"]
            table = [[producto] + inventario[producto]]
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("El producto no existe en el inventario.")

    elif opc == "4":  # Mostrar inventario
        print("\nInventario Actual:")
        mostrar_inventario(inventario)

    elif opc == "s":  # Salir
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
