from producto import Producto

class Inventario:
    """
    Clase que gestiona la lista de productos y las operaciones del inventario.
    """
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los objetos de tipo Producto.
        """
        self.productos = []

    def anadir_producto(self, producto: Producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID del producto no exista para asegurar que sea único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(f"Error: El producto con ID {producto.get_id()} ya existe.")
                return False
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido con éxito.")
        return True

    def eliminar_producto_por_id(self, id: int):
        """
        Elimina un producto del inventario buscando su ID.
        """
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print(f"Producto con ID {id} eliminado.")
                return True
        print(f"Error: No se encontró ningún producto con el ID {id}.")
        return False

    def actualizar_cantidad_o_precio(self, id: int, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto existente por su ID.
        Los parámetros son opcionales, permitiendo actualizar uno o ambos.
        """
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(f"Producto con ID {id} actualizado.")
                return True
        print(f"Error: No se encontró ningún producto con el ID {id}.")
        return False

    def buscar_productos_por_nombre(self, nombre: str):
        """
        Busca productos en el inventario que contengan el nombre especificado.
        La búsqueda no distingue entre mayúsculas y minúsculas.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        """
        Muestra una lista completa de todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for p in self.productos:
                print(p)
            print("-------------------------")