# Se define la clase Usuario para representar a los usuarios de la biblioteca.
class Usuario:
    # El constructor de la clase, que se inicializa con el nombre y un ID único para cada usuario.
    def __init__(self, nombre, id_usuario):
        # Se asignan el nombre y el ID de usuario al objeto.
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Se inicializa una lista vacía. Esta lista se usará para guardar los ISBN de los libros que el usuario tiene prestados.
        self.libros_prestados = []

    # El método __repr__ para una representación del objeto Usuario.
    def __repr__(self):
        # Devuelve una cadena legible que incluye el nombre y el ID del usuario.
        return f"Usuario(nombre='{self.nombre}', ID='{self.id_usuario}')"