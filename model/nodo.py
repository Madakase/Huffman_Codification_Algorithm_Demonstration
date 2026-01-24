class Nodo:
    """
    Modelo conceptual de un nodo del árbol binario de Huffman.

    Representa un vértice en una estructura discreta tipo árbol.
    """

    def __init__(self, simbolo=None, frecuencia=0):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
        self.codigo = ""   # código binario asignado (opcional, didáctico)

    def es_hoja(self):
        """
        Determina si el nodo es hoja.
        """
        return self.izquierda is None and self.derecha is None

    def tiene_hijos(self):
        """
        Verifica si el nodo tiene descendientes.
        """
        return self.izquierda is not None or self.derecha is not None

    def set_hijos(self, izquierdo, derecho):
        """
        Asigna hijos al nodo.
        """
        self.izquierda = izquierdo
        self.derecha = derecho

    def set_codigo(self, codigo):
        """
        Asigna el código binario al nodo.
        """
        self.codigo = codigo

    def obtener_info(self):
        """
        Retorna información estructurada del nodo.
        """
        return {
            "simbolo": self.simbolo,
            "frecuencia": self.frecuencia,
            "codigo": self.codigo,
            "es_hoja": self.es_hoja()
        }

    def __repr__(self):
        if self.simbolo is not None:
            return f"Nodo(simbolo='{self.simbolo}', frecuencia={self.frecuencia})"
        return f"Nodo(INTERNO, frecuencia={self.frecuencia})"
