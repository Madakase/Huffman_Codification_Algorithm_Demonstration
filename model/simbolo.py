class Simbolo:
    """
    Modelo conceptual de un símbolo del alfabeto.

    Representa un elemento del conjunto Σ (alfabeto).
    """

    def __init__(self, caracter):
        self.caracter = caracter
        self.frecuencia = 0
        self.probabilidad = 0.0
        self.codigo = ""

    def incrementar_frecuencia(self, cantidad=1):
        """
        Incrementa la frecuencia del símbolo.
        """
        self.frecuencia += cantidad

    def set_probabilidad(self, probabilidad):
        """
        Asigna la probabilidad al símbolo.
        """
        self.probabilidad = probabilidad

    def set_codigo(self, codigo):
        """
        Asigna el código binario del símbolo.
        """
        self.codigo = codigo

    def obtener_info(self):
        """
        Retorna la información completa del símbolo.
        """
        return {
            "caracter": self.caracter,
            "frecuencia": self.frecuencia,
            "probabilidad": self.probabilidad,
            "codigo": self.codigo
        }

    def __repr__(self):
        return (
            f"Simbolo(caracter='{self.caracter}', "
            f"frecuencia={self.frecuencia}, "
            f"probabilidad={self.probabilidad}, "
            f"codigo='{self.codigo}')"
        )
