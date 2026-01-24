def generar_codigos(raiz):
    """
    Genera los códigos binarios recorriendo el árbol.
    Retorna un diccionario: {simbolo: codigo}
    """

    codigos = {}

    def recorrer(nodo, codigo_actual):
        if nodo is None:
            return

        # Si es hoja → asignar código
        if nodo.es_hoja():
            codigos[nodo.simbolo] = codigo_actual
            return

        # Recorrido izquierdo = 0
        recorrer(nodo.izquierda, codigo_actual + "0")

        # Recorrido derecho = 1
        recorrer(nodo.derecha, codigo_actual + "1")

    recorrer(raiz, "")
    return codigos


def codificar_mensaje(texto, codigos):
    """
    Convierte el mensaje original en binario usando Huffman.
    """
    mensaje_codificado = ""
    for caracter in texto:
        mensaje_codificado += codigos.get(caracter, "")
    return mensaje_codificado


def decodificar_mensaje(binario, raiz):
    """
    Decodifica un mensaje binario recorriendo el árbol.
    """
    resultado = ""
    nodo_actual = raiz

    for bit in binario:
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.es_hoja():
            resultado += nodo_actual.simbolo
            nodo_actual = raiz

    return resultado
