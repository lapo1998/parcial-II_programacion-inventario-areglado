#semana 10 mejoramiento de codigo
from producto import Producto
# Importamos el módulo 'os' para interactuar con el sistema operativo,
# en este caso, para verificar si un archivo existe.
import os

# Definición de la clase Inventario.
# Esta clase gestiona toda la lógica del inventario, incluyendo la persistencia.
class Inventario:
    """
    Clase que gestiona la lista de productos y las operaciones del inventario.
    Ahora incluye la funcionalidad de guardar y cargar datos desde archivos.
    """
    # El constructor de la clase. Se ejecuta al crear una instancia de Inventario.
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para los productos.
        Llama al método para cargar el inventario al iniciar.
        """
        # Inicializamos una lista vacía para almacenar los objetos Producto.
        self.productos = []
        self.cargar_inventario()

    # Método para guardar los datos del inventario en un archivo.
    def guardar_inventario(self, nombre_archivo="Inventario.txt"):
        """
        Guarda el inventario actual en un archivo de texto.
        Maneja errores de permisos.
        """
        # Usamos un bloque try-except para manejar posibles errores.
        try:
            # Abrimos el archivo en modo de escritura ('w'). 'with' asegura que el archivo se cierre automáticamente.
            with open(nombre_archivo, 'w') as f:
                for p in self.productos:
                    # Escribimos los atributos del producto en el archivo, separados por comas.
                    # El formato es: id,nombre,cantidad,precio
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            # Mensaje de éxito para el usuario.
            print("✅ Inventario guardado con éxito en el archivo.")
            return True
        except PermissionError:
            print(f"❌ Error de permisos: No se puede escribir en el archivo {nombre_archivo}.")
            return False
        # Manejo de cualquier otro error inesperado.
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al guardar: {e}")
            return False

    # Método para cargar los datos del inventario desde un archivo.
    def cargar_inventario(self, nombre_archivo="Inventario.txt"):
        """
        Carga los productos desde un archivo de texto.
        Maneja `FileNotFoundError` y errores de formato.
        """
        # Verificamos si el archivo existe antes de intentar abrirlo.
        if not os.path.exists(nombre_archivo):
            print(f"ℹ️ El archivo '{nombre_archivo}' no existe. Se creará uno nuevo al guardar.")
            return

        # Usamos un bloque try-except para manejar errores durante la lectura.
        try:
            # Abrimos el archivo en modo de lectura ('r').
            with open(nombre_archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    # Verificamos que la línea tenga 4 partes (id, nombre, cantidad, precio).
                    if len(partes) == 4:
                        # Usamos otro try-except para manejar errores de conversión de tipos.
                        try:
                            # Convertimos cada parte al tipo de dato correcto.
                            id_producto = int(partes[0])
                            nombre = partes[1]
                            cantidad = int(partes[2])
                            precio = float(partes[3])
                            # Creamos un nuevo objeto Producto con los datos.
                            producto = Producto(id_producto, nombre, cantidad, precio)
                            # Añadimos el nuevo producto a la lista del inventario.
                            self.productos.append(producto)
                        # Capturamos errores si las partes no se pueden convertir a int o float.
                        except (ValueError, IndexError):
                            print(f"⚠️ Advertencia: Línea con formato incorrecto. Se saltó: {linea.strip()}")
                print(f"📦 Inventario cargado con éxito desde '{nombre_archivo}'.")
        # Manejo de la excepción si el archivo no se encuentra.
        except FileNotFoundError:
            print(f"❌ Error: El archivo '{nombre_archivo}' no fue encontrado.")
        except PermissionError:
            print(f"❌ Error de permisos: No se puede leer el archivo {nombre_archivo}.")
        # Manejo de cualquier otro error inesperado.
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al cargar: {e}")

    # Método para añadir un producto.
    def anadir_producto(self, producto: Producto):
        # Iteramos sobre la lista para verificar si el ID ya existe.
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(f"❌ Error: El producto con ID {producto.get_id()} ya existe.")
                return False
        # Si no existe, añadimos el producto a la lista.
        self.productos.append(producto)
        print(f"✅ Producto '{producto.get_nombre()}' añadido con éxito.")
        # Llamamos al método para guardar el inventario después de la adición.
        self.guardar_inventario()
        return True

    # Método para eliminar un producto.
    def eliminar_producto_por_id(self, id: int):
        # Iteramos sobre la lista para encontrar el producto por su ID.
        for p in self.productos:
            if p.get_id() == id:
                # Si lo encontramos, lo eliminamos de la lista.
                self.productos.remove(p)
                print(f"✅ Producto con ID {id} eliminado.")
                # Guardamos el inventario después de la eliminación.
                self.guardar_inventario()
                return True
        print(f"❌ Error: No se encontró ningún producto con el ID {id}.")
        return False

    # Método para actualizar un producto. Modificado para guardar el inventario.
    def actualizar_cantidad_o_precio(self, id: int, nueva_cantidad=None, nuevo_precio=None):
        # Iteramos sobre la lista para encontrar el producto por su ID.
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(f"✅ Producto con ID {id} actualizado.")
                # Guardamos el inventario después de la actualización.
                self.guardar_inventario()
                return True
        print(f"❌ Error: No se encontró ningún producto con el ID {id}.")
        return False

    # Método para buscar productos por nombre. No necesita cambios.
    def buscar_productos_por_nombre(self, nombre: str):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    # Método para mostrar todos los productos. No necesita cambios.
    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            # Iteramos y mostramos cada producto.
            for p in self.productos:
                print(p)
            print("-------------------------")