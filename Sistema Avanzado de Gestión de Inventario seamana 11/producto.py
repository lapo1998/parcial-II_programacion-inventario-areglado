
class Producto:
    """Clase que representa un producto individual en el inventario."""
    
    # El método constructor '__init__' se ejecuta cuando se crea un nuevo objeto 'Producto'.
    # Recibe el ID, nombre, cantidad y precio para inicializar el objeto.
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos 'getter' para acceder de forma segura a los atributos.
    def get_id(self):
        # Retorna el ID del producto.
        return self.id_producto

    def get_nombre(self):
        # Retorna el nombre del producto.
        return self.nombre

    def get_cantidad(self):
        # Retorna la cantidad en stock.
        return self.cantidad

    # Métodos 'setter' para modificar los atributos.
    def set_cantidad(self, nueva_cantidad):
        # Actualiza la cantidad en stock.
        self.cantidad = nueva_cantidad

    def get_precio(self):
        # Retorna el precio del producto.
        return self.precio

    def set_precio(self, nuevo_precio):
        # Actualiza el precio del producto.
        self.precio = nuevo_precio

    # El método especial '__str__' retorna una cadena que representa al objeto.
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
