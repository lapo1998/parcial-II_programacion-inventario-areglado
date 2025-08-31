#semana 10 mejoramiento de codigo

class Producto:
    """
    Clase que representa un producto en el sistema de inventario.
    Contiene los atributos básicos y los métodos para gestionarlos.
    """
    # Método constructor que se ejecuta al crear un nuevo objeto Producto.
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos del producto.
        """
        # Atributos de la instancia de la clase. Usamos un guion bajo para indicar que son "privados".
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos Getter (para obtener los valores de los atributos)
    def get_id(self):
        # Retorna el ID del producto.
        return self._id

    def get_nombre(self):
        # Retorna el nombre del producto.
        return self._nombre

    def get_cantidad(self):
        # Retorna la cantidad del producto.
        return self._cantidad

    def get_precio(self):
        # Retorna el precio del producto.
        return self._precio

    # Métodos Setter (para modificar los valores de los atributos)
    def set_cantidad(self, nueva_cantidad):
        # Permite actualizar la cantidad del producto, validando que no sea negativa.
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        # Permite actualizar el precio del producto, validando que no sea negativo.
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

    # Método especial que define cómo se imprime el objeto como una cadena de texto.
    def __str__(self):
        """
        Método especial para una representación en cadena (string) del objeto.
        Útil para imprimir la información del producto de forma legible.
        """
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"