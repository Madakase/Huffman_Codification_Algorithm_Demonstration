from collections import Counter

def normalizar_texto(texto):
    """
    Normaliza el texto de entrada.
    Elimina saltos de línea innecesarios y espacios redundantes.
    """
    if not texto:
        return ""
    return texto.strip()

def contar_frecuencias(texto):
    """
    Cuenta la frecuencia absoluta de cada símbolo.
    Retorna un diccionario: {simbolo: frecuencia}
    """
    texto = normalizar_texto(texto)
    return dict(Counter(texto))

def calcular_probabilidades(frecuencias):
    """
    Calcula la probabilidad de cada símbolo.
    P(s) = frecuencia(s) / total_simbolos
    """
    total = sum(frecuencias.values())
    if total == 0:
        return {}

    probabilidades = {}
    for simbolo, freq in frecuencias.items():
        probabilidades[simbolo] = freq / total

    return probabilidades

def generar_tabla_frecuencias(texto):
    """
    Pipeline completo:
    texto -> frecuencias -> probabilidades
    """
    frec = contar_frecuencias(texto)
    prob = calcular_probabilidades(frec)

    tabla = {}
    for simbolo in frec:
        tabla[simbolo] = {
            "frecuencia": frec[simbolo],
            "probabilidad": prob[simbolo]
        }

    return tabla
