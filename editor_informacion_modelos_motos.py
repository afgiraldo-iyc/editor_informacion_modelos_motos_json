import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

class MotoJSONEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Modelos de Motocicleta JSON")
        self.root.geometry("1000x500")
        self.root.minsize(800, 400)

        self.data = {}
        self.file_path = ""

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Editor de Modelos de Motocicleta JSON", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        load_btn = tk.Button(btn_frame, text="Seleccionar Archivo JSON", command=self.load_json)
        load_btn.grid(row=0, column=0, padx=5)

        new_btn = tk.Button(btn_frame, text="Nuevo Registro", command=self.new_record)
        new_btn.grid(row=0, column=1, padx=5)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar:").grid(row=0, column=0)
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=40)
        search_entry.grid(row=0, column=1, padx=5)

        tk.Button(search_frame, text="Buscar", command=self.search).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Restablecer", command=self.populate_table).grid(row=0, column=3, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Modelo", "Año", "Categoría"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Modelo", text="Nombre o Modelo")
        self.tree.heading("Año", text="Año Modelo")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.bind("<Double-1>", self.edit_record)

        self.tree.pack(expand=True, fill="both")

        footer = tk.Label(self.root, text="Desarrollado por Nuevas Tecnologías División TI", font=("Arial", 10))
        footer.pack(pady=5)

    def load_json(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if self.file_path:
            try:
                # CORRECCIÓN: usar utf-8-sig para manejar archivos con BOM
                with open(self.file_path, "r", encoding="utf-8-sig") as f:
                    content = json.load(f)
                    if isinstance(content, dict):
                        self.data = content
                        self.populate_table()
                    else:
                        messagebox.showerror("Error", "La estructura del archivo JSON no es válida.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

    def save_json(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)

    def populate_table(self):
        self.tree.delete(*self.tree.get_children())
        for key, val in self.data.items():
            self.tree.insert("", "end", iid=key, values=(
                key,
                val.get("Nombre o modelo", ""),
                val.get("Año modelo", ""),
                val.get("Categoria", "")
            ))

    def search(self):
        term = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for key, val in self.data.items():
            if term in str(val).lower():
                self.tree.insert("", "end", iid=key, values=(
                    key,
                    val.get("Nombre o modelo", ""),
                    val.get("Año modelo", ""),
                    val.get("Categoria", "")
                ))

    def edit_record(self, event):
        selected_id = self.tree.focus()
        if selected_id:
            self.open_edit_window(selected_id, self.data[selected_id])

    def new_record(self):
        new_id = str(max([int(i) for i in self.data.keys()] + [0]) + 1)
        self.data[new_id] = {
            "Categoria": "",
            "Nombre o modelo": "",
            "Año modelo": "",
            "Precio": "",
            "Mensaje comercial": "",
            "Mensaje Tecnico": "",
            "Mensaje de disponibilidad ": ""
        }
        self.open_edit_window(new_id, self.data[new_id])

    def open_edit_window(self, record_id, data):
        edit_win = tk.Toplevel(self.root)
        edit_win.title(f"Editar registro {record_id}")

        labels = [
            "Categoria", "Nombre o modelo", "Año modelo",
            "Precio", "Mensaje comercial", "Mensaje Tecnico",
            "Mensaje de disponibilidad "
        ]
        entries = {}

        for i, field in enumerate(labels):
            tk.Label(edit_win, text=field + ":").grid(row=i, column=0, sticky="e", padx=5, pady=2)
            entry = tk.Entry(edit_win, width=80)
            entry.insert(0, data.get(field, ""))
            entry.grid(row=i, column=1, padx=5, pady=2)
            entries[field] = entry

        def save_changes():
            for field in labels:
                self.data[record_id][field] = entries[field].get()
            self.save_json()
            self.populate_table()
            edit_win.destroy()

        tk.Button(edit_win, text="Guardar Cambios", command=save_changes).grid(row=len(labels), column=0, pady=10)
        tk.Button(edit_win, text="Cancelar", command=edit_win.destroy).grid(row=len(labels), column=1)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MotoJSONEditor(root)
    root.mainloop()
