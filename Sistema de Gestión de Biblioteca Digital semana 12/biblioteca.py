sfrom libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()
        self.coleccion_usuarios = {}
        self.contador_usuarios = 0

    # Funcionalidad: Añadir/quitar libros
    def anadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"❌ El libro con ISBN {libro.isbn} ya existe.")
            return
        self.libros_disponibles[libro.isbn] = libro
        print(f"✅ Libro '{libro.datos[0]}' añadido.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"🗑️ Libro con ISBN {isbn} quitado.")
        else:
            print(f"❌ No se encontró un libro con ISBN {isbn}.")

    # Funcionalidad: Registrar/dar de baja usuarios
    def registrar_usuario(self, nombre):
        id_usuario = self.contador_usuarios
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios_registrados.add(id_usuario)
        self.coleccion_usuarios[id_usuario] = nuevo_usuario
        self.contador_usuarios += 1
        print(f"👤 Usuario '{nombre}' registrado con éxito. ID: {id_usuario}")
        return nuevo_usuario

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"❌ El usuario con ID {id_usuario} no está registrado.")
            return False
        
        usuario = self.coleccion_usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"⚠️ El usuario '{usuario.nombre}' tiene libros prestados. No se puede dar de baja.")
            return False
        
        self.usuarios_registrados.remove(id_usuario)
        del self.coleccion_usuarios[id_usuario]
        print(f"✅ Usuario con ID {id_usuario} dado de baja.")
        return True

    # Funcionalidad: Prestar/devolver libros
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("❌ Usuario no registrado.")
            return False
        
        if isbn not in self.libros_disponibles:
            print("❌ Libro no disponible en la biblioteca.")
            return False

        usuario = self.coleccion_usuarios[id_usuario]
        if isbn in usuario.libros_prestados:
            print(f"⚠️ El libro con ISBN {isbn} ya está prestado.")
            return False
        
        usuario.libros_prestados.append(isbn)
        print(f"➡️ Libro con ISBN {isbn} prestado a '{usuario.nombre}'.")
        return True

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("❌ Usuario no registrado.")
            return False

        usuario = self.coleccion_usuarios[id_usuario]
        if isbn in usuario.libros_prestados:
            usuario.libros_prestados.remove(isbn)
            print(f"↩️ Libro con ISBN {isbn} devuelto por '{usuario.nombre}'.")
            return True
        else:
            print(f"❌ El usuario '{usuario.nombre}' no tiene este libro prestado.")
            return False

    # Funcionalidad: Buscar libros
    def buscar_libros(self, query, tipo='titulo'):
        resultados = []
        for libro in self.libros_disponibles.values():
            if tipo == 'titulo' and query.lower() in libro.datos[0].lower():
                resultados.append(libro)
            elif tipo == 'autor' and query.lower() in libro.datos[1].lower():
                resultados.append(libro)
            elif tipo == 'categoria' and query.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Funcionalidad: Listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print("❌ Usuario no registrado.")
            return
        
        usuario = self.coleccion_usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"El usuario '{usuario.nombre}' no tiene libros prestados.")
            return

        print(f"📚 Libros prestados a '{usuario.nombre}':")
        for isbn in usuario.libros_prestados:
            libro = self.libros_disponibles.get(isbn)
            if libro:
                print(f"   - {libro.datos[0]} de {libro.datos[1]} (ISBN: {isbn})")