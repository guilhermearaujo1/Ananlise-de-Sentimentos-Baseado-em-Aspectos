class Frase():

    #Classe que representa uma frase

    def __init__(self, id = -1, texto = ''):
        self.id = id
        self.texto = texto
        self.palavras = []
        self.palavras_sem_stopwords = []
        self.stems = []
        self.aspectos = []
        self.entidades = []
        self.pontuacoes = {}
        self.escore_relevancia = 0
        self.escore_relevancia_estimado = 0
        self.is_removido = False

    def add_palavra(self, palavra):
        self.palavras.append(palavra)

    def add_palavras_sem_stopwords(self, palavra):
        self.palavras_sem_stopwords.append(palavra)

    def add_stem(self, stem):
        self.stems.append(stem)

    def add_pontuacao(self, tecnica, pontuacao):
        self.pontuacoes[tecnica] = pontuacao

    def add_aspecto(self, aspecto):
        self.aspectos.append(aspecto)

