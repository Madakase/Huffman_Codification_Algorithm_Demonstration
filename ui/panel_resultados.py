import tkinter as tk

class PanelResultados(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # Título
        self.label_titulo = tk.Label(
            self,
            text="Resultados de la codificación",
            font=("Arial", 13, "bold")
        )
        self.label_titulo.pack(pady=5)

        # Texto original
        self.label_original = tk.Label(self, text="Mensaje original:")
        self.label_original.pack(anchor="w", padx=5)

        self.texto_original = tk.Text(self, height=4)
        self.texto_original.pack(fill=tk.X, padx=5, pady=2)

        # Texto codificado
        self.label_codificado = tk.Label(self, text="Mensaje codificado (binario):")
        self.label_codificado.pack(anchor="w", padx=5)

        self.texto_codificado = tk.Text(self, height=4)
        self.texto_codificado.pack(fill=tk.X, padx=5, pady=2)

        # Métricas
        self.label_metricas = tk.Label(self, text="Métricas:")
        self.label_metricas.pack(anchor="w", padx=5, pady=5)

        self.label_tamano_original = tk.Label(self, text="Tamaño original: 0 bits")
        self.label_tamano_original.pack(anchor="w", padx=10)

        self.label_tamano_codificado = tk.Label(self, text="Tamaño codificado: 0 bits")
        self.label_tamano_codificado.pack(anchor="w", padx=10)

        self.label_reduccion = tk.Label(self, text="Reducción: 0 %")
        self.label_reduccion.pack(anchor="w", padx=10)

    def actualizar_resultados(self, texto, binario):
        self.texto_original.delete("1.0", tk.END)
        self.texto_original.insert(tk.END, texto)

        self.texto_codificado.delete("1.0", tk.END)
        self.texto_codificado.insert(tk.END, binario)

        # Cálculo de tamaños
        tam_original = len(texto) * 8  # 8 bits por carácter (ASCII)
        tam_codificado = len(binario)

        if tam_original > 0:
            reduccion = ((tam_original - tam_codificado) / tam_original) * 100
        else:
            reduccion = 0

        self.label_tamano_original.config(text=f"Tamaño original: {tam_original} bits")
        self.label_tamano_codificado.config(text=f"Tamaño codificado: {tam_codificado} bits")
        self.label_reduccion.config(text=f"Reducción: {round(reduccion, 2)} %")
