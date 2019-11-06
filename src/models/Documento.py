class Documento:

    #Classe que representa um documento

    def __init__(self, texto = ''):
        self.texto = texto
        self.frases = []
        self.entidades = []
        self.palavras = []
        self.palavras_sem_stopwords = []

    def add_frase(self, frase):
        self.frases.append(frase)

    def add_palavras(self, palavras):
        self.palavras.extend(palavras)

    def add_palavras_sem_stopwords(self, palavras_sem_stopwords):
        self.palavras_sem_stopwords.extend(palavras_sem_stopwords)

    def add_entidade(self, entidade):
        self.entidades.append(entidade)