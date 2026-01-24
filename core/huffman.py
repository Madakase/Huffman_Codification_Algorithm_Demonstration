from core.arbol import crear_nodos_desde_frecuencias, unir_nodos, Nodo

def construir_arbol_huffman(frecuencias):
    """
    Implementa el algoritmo de Huffman.
    Retorna la raíz del árbol binario.
    """

    # Paso 1: crear nodos iniciales
    nodos = crear_nodos_desde_frecuencias(frecuencias)

    # Caso trivial
    if len(nodos) == 0:
        return None

    if len(nodos) == 1:
        # Solo un símbolo → árbol trivial
        return nodos[0]

    # Paso 2: aplicar algoritmo greedy
    while len(nodos) > 1:
        # Ordenar por frecuencia
        nodos.sort(key=lambda n: n.frecuencia)

        # Tomar los dos menores
        n1 = nodos.pop(0)
        n2 = nodos.pop(0)

        # Unirlos
        nuevo = unir_nodos(n1, n2)

        # Insertar nodo combinado
        nodos.append(nuevo)

    # Paso final: raíz del árbol
    return nodos[0]
