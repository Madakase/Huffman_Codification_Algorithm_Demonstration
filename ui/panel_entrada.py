import tkinter as tk
from core.frecuencia import generar_tabla_frecuencias
from core.huffman import construir_arbol_huffman
from core.codificacion import generar_codigos, codificar_mensaje
from utils.validaciones import normalizar_entrada

class PanelEntrada(tk.Frame):

    def __init__(self, parent, controlador):
        super().__init__(parent)

        self.controlador = controlador

        # Título
        self.label_titulo = tk.Label(
            self,
            text="Entrada del mensaje",
            font=("Arial", 14, "bold")
        )
        self.label_titulo.pack(pady=5)

        # Campo de texto
        self.texto_input = tk.Text(self, height=5)
        self.texto_input.pack(fill=tk.X, padx=10, pady=5)

        # Botones
        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(pady=5)

        self.btn_analizar = tk.Button(
            self.frame_botones,
            text="Analizar mensaje",
            command=self.analizar_mensaje
        )
        self.btn_analizar.pack(side=tk.LEFT, padx=5)

        self.btn_construir = tk.Button(
            self.frame_botones,
            text="Construir árbol Huffman",
            command=self.construir_arbol
        )
        self.btn_construir.pack(side=tk.LEFT, padx=5)

        # Estado
        self.label_estado = tk.Label(self, text="Estado: esperando entrada...")
        self.label_estado.pack(pady=5)

        # Variables internas
        self.frecuencias = {}
        self.probabilidades = {}
        self.arbol = None
        self.codigos = {}
        self.mensaje_codificado = ""

    # ==============================
    # Lógica de eventos
    # ==============================

    def analizar_mensaje(self):
        texto = self.texto_input.get("1.0", tk.END)
        texto = normalizar_entrada(texto)

        if not texto:
            self.label_estado.config(text="Estado: texto inválido")
            return

        tabla = generar_tabla_frecuencias(texto)

        self.frecuencias = {}
        self.probabilidades = {}

        for simbolo, datos in tabla.items():
            self.frecuencias[simbolo] = datos["frecuencia"]
            self.probabilidades[simbolo] = datos["probabilidad"]

        self.label_estado.config(text="Estado: frecuencias y probabilidades calculadas")

    def construir_arbol(self):
        if not self.frecuencias:
            self.label_estado.config(text="Estado: primero analiza el mensaje")
            return

        self.arbol = construir_arbol_huffman(self.frecuencias)
        self.codigos = generar_codigos(self.arbol)

        texto = self.texto_input.get("1.0", tk.END)
        texto = normalizar_entrada(texto)

        self.mensaje_codificado = codificar_mensaje(texto, self.codigos)

        self.controlador.actualizar_datos(
            texto,
            self.frecuencias,
            self.probabilidades,
            self.arbol,
            self.codigos,
            self.mensaje_codificado
        )

        self.label_estado.config(text="Estado: árbol y codificación generados")
