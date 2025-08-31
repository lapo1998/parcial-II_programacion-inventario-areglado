from inventario import Inventario
from producto import Producto

def mostrar_menu():
    """
    Función que muestra el menú de opciones al usuario para interactuar con el sistema.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    """
    Función principal para la ejecución del programa.
    Contiene el bucle principal que maneja la interacción con el usuario.
    """
    inventario = Inventario()
    
    # Añadimos algunos productos iniciales para pruebas, para que el inventario no esté vacío al empezar.
    inventario.anadir_producto(Producto(101, "Laptop Gamer", 10, 1200.00))
    inventario.anadir_producto(Producto(102, "celulares", 50, 25.50))
    inventario.anadir_producto(Producto(103, "mauses,teclado", 30, 75.00))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                # Se pide al usuario que ingrese los datos del nuevo producto.
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id, nombre, cantidad, precio)
                inventario.anadir_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para ID, cantidad y precio.")
        
        elif opcion == '2':
            try:
                # Se pide al usuario el ID del producto a eliminar.
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto_por_id(id)
            except ValueError:
                print("Entrada inválida. El ID debe ser un número.")
        
        elif opcion == '3':
            try:
                # Se pide al usuario el ID del producto a actualizar.
                id = int(input("Ingrese el ID del producto a actualizar: "))
                # Se manejan entradas opcionales para cantidad y precio.
                nueva_cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
                nuevo_precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")
                
                nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
                nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None
                
                inventario.actualizar_cantidad_o_precio(id, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Entrada inválida. La cantidad y el precio deben ser números.")
        
        elif opcion == '4':
            # Se pide el nombre para buscar productos.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for p in resultados:
                    print(p)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        elif opcion == '5':
            # Muestra todos los productos del inventario.
            inventario.mostrar_todos_los_productos()
        
        elif opcion == '6':
            print("Saliendo del sistema. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()