import tkinter as tk
from tkinter import ttk

class PanelTablas(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # Título
        self.label_titulo = tk.Label(
            self,
            text="Tablas de análisis",
            font=("Arial", 13, "bold")
        )
        self.label_titulo.pack(pady=5)

        # Tabla
        columnas = ("Simbolo", "Frecuencia", "Probabilidad", "Codigo")

        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=20)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        self.tabla.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def limpiar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

    def actualizar_tablas(self, frecuencias, probabilidades, codigos):
        self.limpiar_tabla()

        simbolos = set(frecuencias.keys()) | set(codigos.keys())

        for s in simbolos:
            freq = frecuencias.get(s, 0)
            prob = probabilidades.get(s, 0)
            cod = codigos.get(s, "")

            self.tabla.insert("", tk.END, values=(s, freq, round(prob, 5), cod))
