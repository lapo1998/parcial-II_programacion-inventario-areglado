import pickle  
import os      
# Se importa la clase Producto desde el archivo producto.py para poder trabajar con sus objetos.
from producto import Producto

# Esta clase gestiona la colección de todos los objetos 'Producto'.
class Inventario:
    """Clase que gestiona la colección de productos, permitiendo operaciones CRUD."""
    
    # El constructor inicializa el Inventario y carga los datos desde el archivo.
    def __init__(self, nombre_archivo="inventario.dat"):
        # Almacena el nombre del archivo de datos.
        self.nombre_archivo = nombre_archivo
        # Utiliza un diccionario para almacenar los productos, con el ID como clave.
        self.productos = self.cargar_inventario()

    # Este método carga los datos del inventario desde un archivo, asegurando la persistencia.
    def cargar_inventario(self):
        # Comprueba si el archivo de inventario existe.
        if os.path.exists(self.nombre_archivo):
            try:
                # Abre el archivo en modo de lectura binaria ('rb').
                with open(self.nombre_archivo, 'rb') as f:
                    print("Inventario cargado con éxito.")
                    # Deserializa los datos y los retorna como un diccionario.
                    return pickle.load(f)
            except Exception as e:
                # Maneja posibles errores durante la carga.
                print(f"Error al cargar el inventario: {e}")
                return {}
        else:
            # Si el archivo no existe, inicia un nuevo inventario vacío.
            print("No se encontró el archivo de inventario. Iniciando con un inventario vacío.")
            return {}

    # Este método guarda los datos del inventario en un archivo.
    def guardar_inventario(self):
        try:
            # Abre el archivo en modo de escritura binaria ('wb').
            with open(self.nombre_archivo, 'wb') as f:
                # Serializa el diccionario de productos y lo guarda.
                pickle.dump(self.productos, f)
            print("Inventario guardado con éxito.")
        except Exception as e:
            # Maneja errores durante el guardado.
            print(f"Error al guardar el inventario: {e}")

    # Este método añade un nuevo producto al diccionario.
    def añadir_producto(self, producto):
        # Verifica si el ID del producto ya existe para evitar duplicados.
        if producto.get_id() in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            # Si el ID es único, añade el producto.
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido.")

    # Este método elimina un producto por su ID.
    def eliminar_producto_por_id(self, id_producto):
        # Verifica si el producto existe antes de intentar eliminarlo.
        if id_producto in self.productos:
            producto_eliminado = self.productos.pop(id_producto)
            print(f"Producto '{producto_eliminado.get_nombre()}' eliminado.")
        else:
            # Informa al usuario si el producto no se encontró.
            print(f"Error: No se encontró un producto con el ID {id_producto}.")

    # Este método actualiza la cantidad o el precio de un producto existente.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Verifica si el producto existe.
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            # Si se proporciona una nueva cantidad, la actualiza.
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
                print(f"Cantidad de '{producto.get_nombre()}' actualizada a {nueva_cantidad}.")
            # Si se proporciona un nuevo precio, lo actualiza.
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
                print(f"Precio de '{producto.get_nombre()}' actualizado a ${nuevo_precio:.2f}.")
        else:
            # Informa si el producto no existe.
            print(f"Error: No se encontró un producto con el ID {id_producto}.")

    # Este método busca productos por nombre de forma insensible a mayúsculas/minúsculas.
    def buscar_producto_por_nombre(self, nombre_producto):
        # Crea una lista de productos que coinciden con el nombre de búsqueda.
        encontrados = [p for p in self.productos.values() if p.get_nombre().lower() == nombre_producto.lower()]
        if encontrados:
            print("\n--- Productos Encontrados ---")
            # Muestra los productos que se encontraron.
            for p in encontrados:
                print(p)
            print("-----------------------------")
        else:
            # Si no hay coincidencias, informa al usuario.
            print(f"No se encontraron productos con el nombre '{nombre_producto}'.")

    # Este método muestra todos los productos que están en el inventario.
    def mostrar_todos_los_productos(self):
        # Comprueba si el inventario está vacío.
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            for producto in self.productos.values():
                print(producto)
            print("---------------------------")
