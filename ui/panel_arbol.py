import tkinter as tk
from utils.visualizacion import preparar_datos_visualizacion

class PanelArbol(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # Título
        self.label_titulo = tk.Label(
            self,
            text="Árbol de Huffman",
            font=("Arial", 13, "bold")
        )
        self.label_titulo.pack(pady=5)

        # Canvas
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def limpiar(self):
        self.canvas.delete("all")

    def dibujar_arbol(self, raiz):
        """
        Dibuja el árbol de Huffman en el Canvas.
        """
        self.limpiar()

        if raiz is None:
            return

        datos = preparar_datos_visualizacion(raiz)
        posiciones = datos["posiciones"]
        conexiones = datos["conexiones"]

        # Dibujar conexiones
        for padre, hijo, bit in conexiones:
            x1, y1 = posiciones[padre]
            x2, y2 = posiciones[hijo]

            self.canvas.create_line(x1, y1, x2, y2, width=2)

            # Etiqueta del bit (0 o 1)
            xm = (x1 + x2) // 2
            ym = (y1 + y2) // 2
            self.canvas.create_text(xm, ym - 5, text=bit, font=("Arial", 9))

        # Dibujar nodos
        for nodo, (x, y) in posiciones.items():
            r = 18

            # Círculo del nodo
            self.canvas.create_oval(
                x - r, y - r, x + r, y + r,
                fill="#dff0ff",
                outline="black"
            )

            # Texto del nodo
            if nodo.simbolo is not None:
                texto = f"{nodo.simbolo}\n{nodo.frecuencia}"
            else:
                texto = f"{nodo.frecuencia}"

            self.canvas.create_text(x, y, text=texto, font=("Arial", 9, "bold"))
