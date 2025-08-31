
from producto import Producto
from inventario import Inventario

# Esta función gestiona el flujo del programa y el menú de usuario.
def menu_principal():
    # Crea una instancia de la clase 'Inventario', lo que carga el inventario inicial.
    inventario = Inventario()

    # Inicia un bucle infinito para mostrar el menú hasta que el usuario decida salir.
    while True:
        # Imprime las opciones disponibles para el usuario.
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        # Pide al usuario que ingrese una opción.
        opcion = input("Seleccione una opción: ")

        # Se usa una estructura 'if-elif-else' para manejar la lógica de cada opción.
        if opcion == '1':
            try:
                # Solicita los datos del nuevo producto.
                id_prod = input("Ingrese el ID del producto: ")
                nombre_prod = input("Ingrese el nombre: ")
                cantidad_prod = int(input("Ingrese la cantidad: "))
                precio_prod = float(input("Ingrese el precio: "))
                # Crea un nuevo objeto 'Producto'.
                nuevo_producto = Producto(id_prod, nombre_prod, cantidad_prod, precio_prod)
                # Llama al método para añadir el producto al inventario.
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                # Maneja el error si el usuario ingresa un valor no numérico.
                print("Error: La cantidad y el precio deben ser números.")

        elif opcion == '2':
            # Solicita el ID del producto a eliminar.
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            # Llama al método para eliminar el producto.
            inventario.eliminar_producto_por_id(id_prod)

        elif opcion == '3':
            # Solicita el ID del producto a actualizar.
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            # Variable para rastrear si se realizó alguna actualización.
            actualizacion_hecha = False
            # Pide la nueva cantidad.
            nueva_cant = input("Nueva cantidad (deje en blanco para no actualizar): ")
            if nueva_cant:
                try:
                    nueva_cant = int(nueva_cant)
                    actualizacion_hecha = True
                except ValueError:
                    print("Error: La cantidad debe ser un número.")
                    nueva_cant = None
            
            # Pide el nuevo precio.
            nuevo_precio = input("Nuevo precio (deje en blanco para no actualizar): ")
            if nuevo_precio:
                try:
                    nuevo_precio = float(nuevo_precio)
                    actualizacion_hecha = True
                except ValueError:
                    print("Error: El precio debe ser un número.")
                    nuevo_precio = None

            # Llama al método de actualización si se proporcionó al menos un nuevo valor.
            if actualizacion_hecha:
                inventario.actualizar_producto(id_prod, nueva_cantidad=nueva_cant, nuevo_precio=nuevo_precio)
            else:
                print("No se realizaron cambios.")
        
        elif opcion == '4':
            # Solicita el nombre del producto para buscar.
            nombre_prod = input("Ingrese el nombre del producto a buscar: ")
            # Llama al método de búsqueda.
            inventario.buscar_producto_por_nombre(nombre_prod)

        elif opcion == '5':
            # Llama al método para mostrar todos los productos.
            inventario.mostrar_todos_los_productos()
        
        elif opcion == '6':
            # Si la opción es "Salir", se guarda el inventario.
            inventario.guardar_inventario()
            print("Saliendo del programa.")
            # Rompe el bucle 'while' para terminar el programa.
            break

        else:
            # Si el usuario ingresa una opción no válida.
            print("Opción no válida. Por favor, intente de nuevo.")


# Esta es la línea que inicia el programa.
# El bloque 'if __name__ == "__main__"' asegura que el código se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    menu_principal()