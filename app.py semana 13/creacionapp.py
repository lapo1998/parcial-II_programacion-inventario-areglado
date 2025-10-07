import tkinter as tk
from tkinter import ttk, messagebox

def agregar_tarea():
    # Función para agregar una nueva tarea a la lista.
    tarea = entrada_tarea.get()  
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        # Muestra una advertencia si no hay texto.
        messagebox.showwarning("Advertencia", "escribe una tarea.")

def eliminar_tarea():
    # Función para eliminar la tarea seleccionada.
    try:
        indice_seleccionado = lista_tareas.curselection()[0]
        # Borra la tarea en ese índice.
        lista_tareas.delete(indice_seleccionado)
    except IndexError:
        # Muestra una advertencia si no se seleccionó una tarea.
        messagebox.showwarning("Advertencia", "selecciona una tarea para eliminar.")

def limpiar_lista():
    # Borra todos los elementos desde el inicio hasta el final.
    lista_tareas.delete(0, tk.END)

# aqui creamos la ventana principal de la aplicación.
ventana = tk.Tk()
# Establece el título de la ventana.
ventana.title("Gestor de Tareas GUI")
# tamaño inicial de la ventana.
ventana.geometry("460x500")

# Crea un marco para organizar los widgets.
frame_principal = ttk.Frame(ventana, padding="10")
frame_principal.pack(fill=tk.BOTH, expand=True)

# aca crea y configura los componentes (widgets).
etiqueta_titulo = ttk.Label(frame_principal, text="Mi Lista de Tareas", font=("Helvetica", 16, "bold"))
etiqueta_titulo.pack(pady=10)

# Campo de entrada de texto.
entrada_tarea = ttk.Entry(frame_principal, width=40)
entrada_tarea.pack(pady=5)

# Botón para agregar.
boton_agregar = ttk.Button(frame_principal, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Botón para eliminar.
boton_eliminar = ttk.Button(frame_principal, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Botón para limpiar.
boton_limpiar = ttk.Button(frame_principal, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Lista para mostrar las tareas.
lista_tareas = tk.Listbox(frame_principal, width=50, height=10, borderwidth=2, relief="groove")
lista_tareas.pack(pady=10)

# Inicia el bucle principal que mantiene la ventana abierta.

ventana.mainloop()
