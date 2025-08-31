#semana 10 mejoramiento de codigo
from inventario import Inventario
# Importamos la clase Producto.
from producto import Producto

# Función que muestra el menú de opciones.
def mostrar_menu():
    """
    Función que muestra el menú de opciones al usuario.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

# Función principal del programa.
def main():
    """
    Función principal que ejecuta el programa.
    """
    # Creamos una instancia de la clase Inventario.
    # Esto automáticamente carga los datos desde el archivo.
    inventario = Inventario()
    
    # Bucle principal que mantiene el menú activo hasta que el usuario decida salir.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Lógica para la opción 1: Añadir producto.
        if opcion == '1':
            # Usamos try-except para validar que las entradas sean del tipo correcto.
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.anadir_producto(nuevo_producto)
            # Manejamos el error si el usuario no ingresa un número.
            except ValueError:
                print("❌ Entrada inválida. Asegúrese de ingresar números para ID, cantidad y precio.")
        
        # Lógica para la opción 2: Eliminar producto.
        elif opcion == '2':
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                # Llamamos al método de Inventario para eliminar.
                inventario.eliminar_producto_por_id(id_prod)
            except ValueError:
                print("❌ Entrada inválida. El ID debe ser un número.")
        
        # Lógica para la opción 3: Actualizar producto.
        elif opcion == '3':
            try:
                id_prod = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
                nuevo_precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")
                
                # Convertimos las entradas a números si no están vacías, si no, se deja como None.
                nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
                nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None
                
                # Llamamos al método de Inventario para actualizar.
                inventario.actualizar_cantidad_o_precio(id_prod, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("❌ Entrada inválida. La cantidad y el precio deben ser números.")
        
        # Lógica para la opción 4: Buscar producto.
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            # Llamamos al método de Inventario para buscar.
            resultados = inventario.buscar_productos_por_nombre(nombre)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for p in resultados:
                    print(p)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        # Lógica para la opción 5: Mostrar todos los productos.
        elif opcion == '5':
            # Llamamos al método de Inventario para mostrar todos los productos.
            inventario.mostrar_todos_los_productos()
        
        # Lógica para la opción 6: Salir del programa.
        elif opcion == '6':
            print("Saliendo del sistema. ¡Adiós!")
            break
    
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa.
if __name__ == "__main__":
    main()