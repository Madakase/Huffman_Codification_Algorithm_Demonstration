def es_texto_valido(texto):
    """
    Verifica si el texto es válido para ser procesado.
    """
    if texto is None:
        return False

    if not isinstance(texto, str):
        return False

    if len(texto.strip()) == 0:
        return False

    return True


def limpiar_texto(texto):
    """
    Limpia el texto de entrada:
    - elimina saltos de línea
    - elimina tabs
    - normaliza espacios
    """
    if texto is None:
        return ""

    texto = texto.replace("\n", " ")
    texto = texto.replace("\t", " ")
    texto = texto.replace("\r", " ")

    # Normalizar múltiples espacios
    while "  " in texto:
        texto = texto.replace("  ", " ")

    return texto.strip()


def filtrar_caracteres(texto, permitir_espacios=True):
    """
    Permite filtrar caracteres no deseados.
    """
    if texto is None:
        return ""

    resultado = ""

    for c in texto:
        if c.isprintable():
            if c == " ":
                if permitir_espacios:
                    resultado += c
            else:
                resultado += c

    return resultado


def normalizar_entrada(texto):
    """
    Pipeline completo de validación y limpieza.
    """
    if not es_texto_valido(texto):
        return ""

    texto = limpiar_texto(texto)
    texto = filtrar_caracteres(texto)

    return texto


def validar_frecuencias(frecuencias):
    """
    Verifica que las frecuencias sean válidas.
    """
    if not isinstance(frecuencias, dict):
        return False

    if len(frecuencias) == 0:
        return False

    for simbolo, freq in frecuencias.items():
        if not isinstance(freq, int):
            return False
        if freq <= 0:
            return False

    return True

def preparar_datos_visualizacion(arbol):
    """
    Prepara los datos del árbol de Huffman para su representación visual.
    Convierte la estructura de nodos en una forma representable por la UI.
    """

    datos = []

    def recorrer(nodo, nivel=0, posicion=0):
        if nodo is None:
            return

        datos.append({
            "simbolo": nodo.simbolo,
            "frecuencia": nodo.frecuencia,
            "nivel": nivel,
            "posicion": posicion,
            "es_hoja": nodo.es_hoja()
        })

        recorrer(nodo.izquierda, nivel + 1, posicion * 2)
        recorrer(nodo.derecha, nivel + 1, posicion * 2 + 1)

    recorrer(arbol)
    return datos
