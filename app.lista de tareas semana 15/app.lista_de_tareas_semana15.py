import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    # Definición de la clase principal de la aplicación GUI
    
    def __init__(self, master):
        # Constructor de la aplicación
        self.master = master
        master.title("📝 Gestor de Tareas") # Título de la ventana GUI
        master.geometry("500x600") # Define el tamaño inicial de la ventana
        master.resizable(False, False) # Deshabilita el redimensionamiento de la ventana

        # Variable vinculada al campo de entrada (Entry)
        self.task_entry = tk.StringVar()

        # Marco de Entrada y Botón Añadir
        self.frame_input = tk.Frame(master)
        self.frame_input.pack(pady=10)

        # Campo de Entrada (Entry) para escribir nuevas tareas
        self.entry_task = tk.Entry(
            self.frame_input,
            textvariable=self.task_entry,
            width=30,
            font=('Arial', 12)
        )
        self.entry_task.grid(row=0, column=0, padx=5)
        self.entry_task.focus() # Enfoca el cursor al iniciar

        # Botón para "Añadir Tarea" (usando el clic: self.add_task)
        self.add_button = tk.Button(
            self.frame_input,
            text="Añadir Tarea",
            command=self.add_task,
            bg='#4CAF50', 
            fg='white',
            font=('Arial', 10, 'bold')
        )
        self.add_button.grid(row=0, column=1, padx=5)

        # Lista de Tareas (Listbox) con Scrollbar
        self.task_list_frame = tk.Frame(master)
        self.task_list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Barra de desplazamiento vertical
        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Componente Listbox: Muestra las tareas actuales
        self.task_listbox = tk.Listbox( 
            self.task_list_frame,
            height=15,
            width=50,
            yscrollcommand=self.scrollbar.set, # Vincula el Listbox al scrollbar
            selectmode=tk.SINGLE,              # Permite seleccionar solo una tarea
            font=('Arial', 12)
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_listbox.yview) # Vincula el scrollbar al Listbox

        # Marco de Botones de Acción
        self.frame_actions = tk.Frame(master)
        self.frame_actions.pack(pady=10)

        # Botón para "Marcar como Completada" con (self.complete_task)
        self.complete_button = tk.Button(
            self.frame_actions,
            text="Completada ✔️",
            command=self.complete_task,
            bg='#2196F3', 
            fg='white',
            font=('Arial', 10, 'bold')
        )
        self.complete_button.grid(row=0, column=0, padx=10)

        # Botón para "Eliminar Tarea" (usando self.delete_task)
        self.delete_button = tk.Button(
            self.frame_actions,
            text="Eliminar 🗑️",
            command=self.delete_task,
            bg='#F44336', 
            fg='white',
            font=('Arial', 10, 'bold')
        )
        self.delete_button.grid(row=0, column=1, padx=10)

        # Evento de Teclado: Añadir tarea al presionar Enter
        self.entry_task.bind('<Return>', lambda event: self.add_task())
        
        # Evento de Teclado: Eliminar tarea al presionar Suprimir/Delete (<Delete>)
        self.task_listbox.bind('<Delete>', lambda event: self.delete_task())

        # Evento de Ratón: Marcar como completada con doble clic
        self.task_listbox.bind('<Double-1>', lambda event: self.complete_task())

    def add_task(self):
        # Método para añadir una nueva tarea
        new_task = self.task_entry.get().strip()
        if new_task:
            # Lógica: Inserta la tarea en el Listbox aparece en la lista
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.set("") 
            self.entry_task.focus() 
        else:
            messagebox.showwarning("Advertencia", "¡Debes introducir una tarea!")

    def complete_task(self):
        # uso esto para marcar la tarea seleccionada como completada
        try:
            selected_indices = self.task_listbox.curselection()
            if not selected_indices:
                raise IndexError 
                
            selected_index = selected_indices[0]
            current_text = self.task_listbox.get(selected_index)
            
            # Condición para actualizar el estado visual
            if not current_text.endswith(" [COMPLETADA]"):
                 # Actualiza el texto
                 self.task_listbox.delete(selected_index)
                 self.task_listbox.insert(selected_index, current_text + " [COMPLETADA]")
                 # Lógica: Cambia el color para reflejar el estado completado
                 self.task_listbox.itemconfig(
                     selected_index, 
                     {'bg': '#D9EAD3', 'fg': "#53C519"} 
                 )
            
        except IndexError:
            messagebox.showwarning("Advertencia", "¡Debes seleccionar una tarea!")

    def delete_task(self):
        # Método para eliminar la tarea seleccionada
        try:
            selected_index = self.task_listbox.curselection()[0]
            # Lógica: Remueve la tarea del Listbox (se elimina de la lista)
            self.task_listbox.delete(selected_index) 
        except IndexError:
            messagebox.showwarning("Advertencia", "¡Debes seleccionar una tarea para eliminarla!")

if __name__ == "__main__":
    root = tk.Tk() 
    app = ToDoApp(root) 
    # Inicia el bucle principal de Tkinter
    root.mainloop()