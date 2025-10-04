#aplicacion GUI con atajos con clik y botones de teclado como atajos
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk 

class TaskManagerApp:
    def __init__(self, master):
        # Configuración Inicial de la Interfaz Gráfica (Tkinter)
        self.master = master
        master.title("Gestión de Tareas con Atajos - Versión Estable Final")
        master.geometry("580x500")

        # Almacén de datos: lista de tuplas (tarea, completada_booleana)
        self.tasks = []
        
        # Marco principal
        main_frame = tk.Frame(master, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campo de Entrada (Entry)
        self.task_entry = tk.Entry(main_frame, width=40, font=('Arial', 12))
        self.task_entry.pack(pady=10, fill=tk.X)
        self.task_entry.focus_set()

        # Botón Añadir (Manejo de Eventos de Clic)
        add_button = tk.Button(main_frame, text="Añadir Tarea (Enter)", command=self.add_task)
        add_button.pack(pady=5, fill=tk.X)

        # Listado de Tareas (ttk.Treeview)
        self.task_listbox = ttk.Treeview(main_frame, height=10, selectmode='browse', show='tree')
    
        # 1. Tarea Completada subrayada y de color verde 
        self.task_listbox.tag_configure('completed', font=('Arial', 12, 'underline'), foreground='green')
        # 2. Tarea Pendiente color negro
        self.task_listbox.tag_configure('pending', font=('Arial', 12, ''), foreground='black')
        
        self.task_listbox.column('#0', width=550, anchor='w')
        self.task_listbox.heading('#0', text='Tareas')
        
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Marco para los botones de acción
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)

        # Botón 'Fin' marca como completado el evento
        complete_button = tk.Button(button_frame, text="Marcar Completada ( Fin )", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, expand=True, padx=5)

        # Botón Eliminar
        delete_button = tk.Button(button_frame, text="Eliminar (Supr)", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, expand=True, padx=5)

        # 3. Atajos de Teclado (Bindings)
        
        # Atajo: Añadir con "Enter"
        master.bind('<Return>', lambda event: self.add_task())
        master.bind('<End>', lambda event: self.mark_completed())
        
        # Atajo: Eliminar tarea con "Delete" / "Supr"
        master.bind('<Delete>', lambda event: self.delete_task())
        
        # Atajo: Cerrar la aplicación con "Escape"
        master.bind('<Escape>', lambda event: self.master.quit())


    def update_listbox(self):
        """Función central para proporcionar feedback visual y refrescar la vista del Treeview."""
        
        # Borrar todos los items del Treeview
        for item in self.task_listbox.get_children():
            self.task_listbox.delete(item)
            
        for task_text, is_completed in self.tasks:
            # Feedback Visual: Asignar el estilo (tag)
            tag = 'completed' if is_completed else 'pending'
            
            # Insertar en Treeview y aplicar el tag
            self.task_listbox.insert('', 'end', text=task_text, tags=(tag,))


    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append((task_text, False)) 
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Atención", "Debes ingresar una descripción para la tarea.")
        self.task_entry.focus_set()

    def get_selected_index(self):
        """Obtiene el índice de la tarea seleccionada en la lista interna (self.tasks)."""
        selected_item_id = self.task_listbox.focus()
        if not selected_item_id:
            return None
        
        children = self.task_listbox.get_children()
        try:
            return list(children).index(selected_item_id)
        except ValueError:
            return None

    def mark_completed(self):
        """Marca la tarea seleccionada como completada (o pendiente si ya estaba completa)."""
        selected_index = self.get_selected_index()
        
        if selected_index is not None:
            # Invierte el estado de la tarea (Completa -> Pendiente, o viceversa)
            task_text, is_completed = self.tasks[selected_index]
            self.tasks[selected_index] = (task_text, not is_completed) 
            
            self.update_listbox()
        else:
            messagebox.showwarning("Atención", "Debes seleccionar una tarea para marcarla.")


    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_index = self.get_selected_index()
        
        if selected_index is not None:
            self.tasks.pop(selected_index)
            self.update_listbox()
        else:
            messagebox.showwarning("Atención", "Debes seleccionar una tarea para eliminarla.")

# Iniciar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()