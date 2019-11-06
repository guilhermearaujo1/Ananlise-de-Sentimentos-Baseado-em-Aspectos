from spacy.lang.pt import lemmatizer
from unicodedata import normalize
import unicodedata
import re


#def remover_acentos(txt):
 #   return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def removerAcentosECaracteresEspeciais(txt):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', txt)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)


def ler_dicionario(arquivo_dicionario):

    dicionario = {}

    with open(arquivo_dicionario, encoding='UTF-8') as arquivo:

        for linha in arquivo.readlines():

            partes = linha.replace('\n', '').split(',')

            palavra = partes[0]

            if palavra in lemmatizer.LOOKUP:
                palavra = lemmatizer.LOOKUP[palavra]

            palavra = removerAcentosECaracteresEspeciais(palavra)

            dicionario[palavra] = int(partes[1])

    return dicionario