
# Se importan las clases necesarias del proyecto para poder utilizarlas.
# La clase Biblioteca contiene la lógica principal.
# La clase Libro se usa para crear nuevos objetos de libro.
from biblioteca import Biblioteca
from libro import Libro

def mostrar_menu():
    """
    Función que imprime el menú de opciones en la consola para guiar al usuario.
    Se utiliza para mantener el código principal más limpio y organizado.
    """
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*40)
    print("1. Añadir un libro")
    print("2. Quitar un libro")
    print("3. Registrar un nuevo usuario")
    print("4. Dar de baja un usuario")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados a un usuario")
    print("9. Salir del programa")
    print("="*40)

def main():
    """
    Función principal del programa. Aquí se crea el objeto de la biblioteca
    y se ejecuta el bucle que gestiona el menú interactivo.
    """
    # Se crea una instancia de la clase Biblioteca.
    biblioteca = Biblioteca()
    
    # Se añaden algunos libros y usuarios de prueba para que el sistema tenga datos al iniciar.
    # Esto facilita la prueba de las demás funcionalidades sin tener que añadir datos manualmente cada vez.
    biblioteca.anadir_libro(Libro("Inteligencia artificial", "Álvaro Montes", "Tecnología", "ISBN_IA"))
    biblioteca.anadir_libro(Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "978-0618053267"))
    biblioteca.anadir_libro(Libro("Huasipungo", "Jorge Icaza", "Novela", "ISBN_H"))
    biblioteca.anadir_libro(Libro("Siete tratados", "Juan Montalvo", "Ensayo", "ISBN_ST"))
    biblioteca.anadir_libro(Libro("El árbol del bien y del mal", "Medardo Angel Silva", "Poesía", "ISBN_ABM"))
    
    # Se añaden algunos usuarios de prueba para las funcionalidades de préstamos.
    manuel = biblioteca.registrar_usuario("Manuel Lapo")
    maribel = biblioteca.registrar_usuario("Maribel Salinas")
    
    # Bucle principal del programa. Se ejecuta indefinidamente hasta que el usuario decida salir (opción 9).
    while True:
        # Se muestra el menú en cada iteración del bucle.
        mostrar_menu()
        # Se solicita al usuario que ingrese una opción.
        opcion = input("➡️  Seleccione una opción: ")

        # Se utiliza una estructura if-elif-else para manejar cada opción del menú.
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            # Se llama al método anadir_libro de la clase Biblioteca para añadir el libro.
            biblioteca.anadir_libro(nuevo_libro)
            
        elif opcion == '2':
            # Se solicita el ISBN del libro a quitar.
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            # Se llama al método quitar_libro.
            biblioteca.quitar_libro(isbn)
            
        elif opcion == '3':
            # Se solicita el nombre del nuevo usuario.
            nombre = input("Ingrese el nombre del usuario a registrar: ")
            # Se llama al método registrar_usuario.
            biblioteca.registrar_usuario(nombre)

        elif opcion == '4':
            # Se usa un bloque try-except para manejar errores si el usuario ingresa un valor no numérico.
            try:
                id_usuario = int(input("Ingrese el ID del usuario a dar de baja: "))
                biblioteca.dar_de_baja_usuario(id_usuario)
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número para el ID.")

        elif opcion == '5':
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                isbn = input("Ingrese el ISBN del libro a prestar: ")
                biblioteca.prestar_libro(id_usuario, isbn)
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número para el ID.")

        elif opcion == '6':
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                isbn = input("Ingrese el ISBN del libro a devolver: ")
                biblioteca.devolver_libro(id_usuario, isbn)
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número para el ID.")

        elif opcion == '7':
            query = input("Ingrese el término de búsqueda: ")
            tipo = input("Buscar por (titulo, autor, categoria): ")
            resultados = biblioteca.buscar_libros(query, tipo)
            print("Resultados de la búsqueda:")
            if resultados:
                for libro in resultados:
                    print(f" - {libro}")
            else:
                print("No se encontraron resultados.")

        elif opcion == '8':
            try:
                id_usuario = int(input("Ingrese el ID del usuario para listar préstamos: "))
                biblioteca.listar_libros_prestados(id_usuario)
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número para el ID.")

        elif opcion == '9':
            # Si el usuario elige la opción 9, se rompe el bucle y el programa termina.
            print("👋 Saliendo del sistema...")
            break

        else:
            # Si la opción ingresada no es válida, se muestra un mensaje de error.
            print("❌ Opción no válida. Por favor, intente de nuevo.")

# Este es el punto de entrada del programa. El código dentro de este bloque
# solo se ejecuta cuando el archivo main.py se corre directamente.
if __name__ == "__main__":
    main()