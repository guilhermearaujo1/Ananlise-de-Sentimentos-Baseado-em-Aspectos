class Palavra():

    #Classe que representa uma palavra

    def __init__(self, id=-1, texto='', stem='', pos='', ehUmaStopWord=False, ehaspecto = ''):
        self.id = id
        self.texto = texto
        self.stem = stem
        self.pos = pos
        self.ehUmaStopWord = ehUmaStopWord
        self.ehaspecto = ehaspecto
