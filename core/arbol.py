class Nodo:
    """
    Representa un nodo del árbol de Huffman.
    Puede ser hoja (símbolo) o nodo interno.
    """

    def __init__(self, simbolo=None, frecuencia=0):
        self.simbolo = simbolo      # carácter (hoja)
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def es_hoja(self):
        return self.izquierda is None and self.derecha is None

    def __lt__(self, other):
        """
        Permite ordenar nodos por frecuencia.
        """
        return self.frecuencia < other.frecuencia

    def __repr__(self):
        if self.simbolo is not None:
            return f"Nodo('{self.simbolo}', {self.frecuencia})"
        return f"Nodo(INTERNO, {self.frecuencia})"


def crear_nodos_desde_frecuencias(frecuencias):
    """
    Convierte el diccionario de frecuencias en nodos.
    """
    nodos = []
    for simbolo, freq in frecuencias.items():
        nodos.append(Nodo(simbolo, freq))
    return nodos


def unir_nodos(nodo1, nodo2):
    """
    Une dos nodos en un nuevo nodo padre.
    """
    nuevo = Nodo(
        simbolo=None,
        frecuencia=nodo1.frecuencia + nodo2.frecuencia
    )
    nuevo.izquierda = nodo1
    nuevo.derecha = nodo2
    return nuevo
