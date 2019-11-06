class FraseReli:

    def __init__(self, texto, dic_aspectos, dic_aspectos_polaridade):
        self.texto = texto
        self.dic_aspectos = dic_aspectos
        self.dic_aspectos_polaridade = dic_aspectos_polaridade

    def __repr__(self):
        return self.texto
