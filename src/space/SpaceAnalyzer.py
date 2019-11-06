import spacy

from src.models.Frase import Frase
from src.models.Palavra import Palavra
from src.models.Entidade import Entidade


class SpaceAnalyzer:

    def __init__(self):
        self.nlp = spacy.load('pt_core_news_sm')

    def processar_documento(self, documento):
        documento_spacy = self.nlp(documento.texto)

        aspectos = []
        documento_processado = {}

        for indice, sentenca in enumerate(documento_spacy.sents):

            tokens = [token for token in sentenca]

            label_entidade = ''
            old_label_entidade = None
            _token = ''
            _tokenHead = ''

            for token in tokens:
                # Adiciona as entidades na Lista
                if token.dep_ == 'flat:name':
                    if _token == str(token.head):
                        _tokenHead = str(token.head)
                    label_entidade = str(token.head) + ' ' + str(token)
                elif token.pos_ == 'PROPN':
                    _token = str(token)
                    label_entidade = token



                # Adiciona os aspectos na lista
                if token.pos_ == 'NOUN':

                    if token.head.pos_ == 'ADJ':
                        #print('achou aqui', token.head)
                        try:
                            aspectos.append({
                                'nome': token,
                                'adjetivo': token.head,
                                'sentimento': str(token.head.lemma_)
                            })
                        except:
                            pass

                elif token.dep_ == 'amod' and token.pos_ == 'ADJ':
                    try:

                        aspectos.append({
                            'nome': token.head,
                            'adjetivo': token,
                            'sentimento': str(token.lemma_)
                        })
                    except:
                        pass
                # Verifica se a entidade já existe na Lista
                if label_entidade:
                    try:
                        if _token == _tokenHead:
                            del documento_processado[_token]
                            _tokenHead = ''
                        else:
                            documento_processado[str(label_entidade)] = {
                                'Entidade': label_entidade,
                                'Aspectos': aspectos
                            }
                        if old_label_entidade and label_entidade != old_label_entidade:
                            aspectos = []

                        old_label_entidade = label_entidade
                    except:
                        pass

        return documento_processado