class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Utiliza una tupla para el título y el autor para hacerlos inmutables.
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        # Representación del objeto, útil para la depuración y visualización.
        return f"Libro(título='{self.datos[0]}', autor='{self.datos[1]}', categoría='{self.categoria}', ISBN='{self.isbn}')"