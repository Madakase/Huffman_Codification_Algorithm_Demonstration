import tkinter as tk
from ui.panel_entrada import PanelEntrada
from ui.panel_tablas import PanelTablas
from ui.panel_arbol import PanelArbol
from ui.panel_resultados import PanelResultados

class VentanaPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador Didáctico del Algoritmo de Huffman")
        self.root.geometry("1400x800")

        # Frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Sub-frames
        self.frame_superior = tk.Frame(self.frame_principal, height=150)
        self.frame_superior.pack(fill=tk.X)

        self.frame_central = tk.Frame(self.frame_principal)
        self.frame_central.pack(fill=tk.BOTH, expand=True)

        self.frame_izquierdo = tk.Frame(self.frame_central, width=400)
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_centro = tk.Frame(self.frame_central)
        self.frame_centro.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame_derecho = tk.Frame(self.frame_central, width=400)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.Y)

        # Paneles
        self.panel_entrada = PanelEntrada(self.frame_superior, self)
        self.panel_entrada.pack(fill=tk.BOTH, expand=True)

        self.panel_tablas = PanelTablas(self.frame_izquierdo)
        self.panel_tablas.pack(fill=tk.BOTH, expand=True)

        self.panel_arbol = PanelArbol(self.frame_centro)
        self.panel_arbol.pack(fill=tk.BOTH, expand=True)

        self.panel_resultados = PanelResultados(self.frame_derecho)
        self.panel_resultados.pack(fill=tk.BOTH, expand=True)

    # ==============================
    # Integración del sistema
    # ==============================

    def actualizar_datos(self, texto, frecuencias, probabilidades, arbol, codigos, mensaje_codificado):
        # Tablas
        self.panel_tablas.actualizar_tablas(frecuencias, probabilidades, codigos)

        # Árbol
        self.panel_arbol.dibujar_arbol(arbol)

        # Resultados
        self.panel_resultados.actualizar_resultados(texto, mensaje_codificado)
