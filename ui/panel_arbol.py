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

        # Frame contenedor
        contenedor = tk.Frame(self)
        contenedor.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        self.scroll_x = tk.Scrollbar(contenedor, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(contenedor, orient=tk.VERTICAL)

        # Canvas
        self.canvas = tk.Canvas(
            contenedor,
            bg="white",
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set
        )

        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)

        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Área virtual grande
        self.canvas.config(scrollregion=(0, 0, 3000, 3000))

        # Soporte para arrastre 
        self.canvas.bind("<ButtonPress-1>", self.iniciar_arrastre)
        self.canvas.bind("<B1-Motion>", self.arrastrar)

        self._drag_data = {"x": 0, "y": 0}

    def iniciar_arrastre(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def arrastrar(self, event):
        dx = self._drag_data["x"] - event.x
        dy = self._drag_data["y"] - event.y
        self.canvas.xview_scroll(int(dx / 2), "units")
        self.canvas.yview_scroll(int(dy / 2), "units")
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def limpiar(self):
        self.canvas.delete("all")

    def dibujar_arbol(self, raiz):
        """
        Dibuja el árbol de Huffman en el Canvas con escalado y scroll.
        """
        self.limpiar()

        if raiz is None:
            return

        datos = preparar_datos_visualizacion(raiz)
        posiciones_logicas = datos["posiciones"]
        conexiones = datos["conexiones"]

 

        escala_x = 180   # separación horizontal entre niveles
        escala_y = 90    # separación vertical entre nodos
        margen = 80

        posiciones = {}

        for nodo, (nivel, pos) in posiciones_logicas.items():
            x = nivel * escala_x + margen
            y = pos * escala_y + margen
            posiciones[nodo] = (x, y)

    

        for padre, hijo, bit in conexiones:
            x1, y1 = posiciones[padre]
            x2, y2 = posiciones[hijo]

            self.canvas.create_line(x1, y1, x2, y2, width=2)

            # Etiqueta del bit
            xm = (x1 + x2) // 2
            ym = (y1 + y2) // 2
            self.canvas.create_text(xm, ym - 5, text=bit, font=("Arial", 9))

      

        for nodo, (x, y) in posiciones.items():
            r = 18

            self.canvas.create_oval(
                x - r, y - r, x + r, y + r,
                fill="#dff0ff",
                outline="black"
            )

            if nodo.simbolo is not None:
                texto = f"{nodo.simbolo}\n{nodo.frecuencia}"
            else:
                texto = f"{nodo.frecuencia}"

            self.canvas.create_text(x, y, text=texto, font=("Arial", 9, "bold"))

    

        self.canvas.update_idletasks()
        bbox = self.canvas.bbox("all")
        if bbox:
            self.canvas.config(scrollregion=bbox)
