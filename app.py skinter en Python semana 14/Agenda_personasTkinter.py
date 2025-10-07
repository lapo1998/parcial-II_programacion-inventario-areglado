# Agenda personas en tikinter
import tkinter as tk
# Importa los widgets con estilo moderno Treeview, Button, Label, Frame
from tkinter import ttk, messagebox
# Importa el widget de calendario para la selección de fechas.
from tkcalendar import Calendar

# Define la función que se ejecuta al presionar "Agregar Evento
def agregar_evento():
    # Obtiene el texto de los campos de entrada de la interfaz
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Verifica que los campos no estén vacíos antes de agregar el evento.
    if fecha and hora and descripcion:
        # Inserta los valores como una nueva fila en el Treeview la tabla
        tabla_eventos.insert('', tk.END, values=(fecha, hora, descripcion))
        
        # Limpia los campos de entrada para el próximo evento.
        entrada_fecha.delete(0, tk.END)
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        # Muestra una ventana de advertencia si los campos están incompletos.
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Define la función para eliminar un evento seleccionado.
def eliminar_evento():
    # Obtiene el identificador del evento que el usuario ha seleccionado.
    seleccionado = tabla_eventos.selection()
    
    # Comprueba si realmente hay un evento seleccionado.
    if seleccionado:
        # Abre un cuadro de diálogo para pedir confirmación al usuario.
        confirmacion = messagebox.askyesno("Confirmar Eliminación", 
                                           "¿Está seguro de que desea eliminar este evento?")
        
        # Si el usuario hace clic en Sí procede con la eliminación.
        if confirmacion:
            tabla_eventos.delete(seleccionado)
    else:
        # Muestra un mensaje si no se ha seleccionado ninguna fila.
        messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

def salir_aplicacion():
    ventana.destroy()

# Define la función que muestra el calendario.
def mostrar_calendario():
    # Crea una ventana secundaria para el calendario.
    top = tk.Toplevel(ventana)
    
    # Crea el widget de calendario.
    cal = Calendar(top, selectmode='day', date_pattern='dd/mm/yyyy')
    cal.pack(pady=20)
    
    # Define una función interna para seleccionar la fecha.
    def seleccionar_fecha():
        # Obtiene la fecha seleccionada por el usuario.
        fecha_seleccionada = cal.get_date()
        entrada_fecha.delete(0, tk.END)
        entrada_fecha.insert(0, fecha_seleccionada)
        top.destroy()
    
    # Crea el botón para confirmar la selección de la fecha.
    boton_seleccionar = ttk.Button(top, text="Seleccionar", command=seleccionar_fecha)
    boton_seleccionar.pack(pady=5)

# Crea la ventana principal de la aplicación.
ventana = tk.Tk()
# Establece el título de la ventana.
ventana.title("Agenda Personal autor Elvio")
# Define el tamaño inicial de la ventana.
ventana.geometry("600x600")
# Establece el color de fondo.
ventana.configure(bg="#f0f0f0")

# Crea un Frame principal para organizar los demás componentes.
marco_principal = ttk.Frame(ventana, padding="10 10 10 10")
marco_principal.pack(expand=True, fill=tk.BOTH)

# Crea un Frame para agrupar las etiquetas, campos de entrada y el botón de agregar.
marco_entrada = ttk.Frame(marco_principal)
marco_entrada.pack(pady=10, fill=tk.X)

# Crea la etiqueta para el campo de fecha.
ttk.Label(marco_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada_fecha = ttk.Entry(marco_entrada)
entrada_fecha.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Crea el botón para abrir el calendario.
boton_calendario = ttk.Button(marco_entrada, text="...", command=mostrar_calendario)
boton_calendario.grid(row=0, column=2, padx=5, pady=5)

# Crea la etiqueta para el campo de hora.
ttk.Label(marco_entrada, text="Hora (hh:mm):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entrada_hora = ttk.Entry(marco_entrada)
entrada_hora.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Crea la etiqueta para el campo de descripción.
ttk.Label(marco_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
# Crea el campo de entrada para la descripción.
entrada_descripcion = ttk.Entry(marco_entrada)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Crea el botón para agregar el evento, vinculado a la función agregar_evento
boton_agregar = ttk.Button(marco_entrada, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, column=1, pady=10, sticky="w")

# Crea el widget de tabla TreeView para mostrar los eventos.
tabla_eventos = ttk.Treeview(marco_principal, columns=("Fecha", "Hora", "Descripción"), show="headings")
# Define los encabezados de las columnas.
tabla_eventos.heading("Fecha", text="Fecha")
tabla_eventos.heading("Hora", text="Hora")
tabla_eventos.heading("Descripción", text="Descripción")
# Posiciona la tabla en la ventana.
tabla_eventos.pack(expand=True, fill=tk.BOTH, pady=10)

# Establece el ancho de las columnas para un mejor diseño visual.
tabla_eventos.column("Fecha", width=100)
tabla_eventos.column("Hora", width=80)
tabla_eventos.column("Descripción", width=350)
# Crea un Frame para agrupar los botones de "Eliminar" y "Salir".
marco_botones = ttk.Frame(marco_principal)
marco_botones.pack(pady=10)

# Crea el botón de "Eliminar"
boton_eliminar = ttk.Button(marco_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Crea el botón de "Salir", vinculado a la función `salir_aplicacion`.
boton_salir = ttk.Button(marco_botones, text="Salir", command=salir_aplicacion)
boton_salir.pack(side=tk.LEFT, padx=5)

ventana.mainloop()
