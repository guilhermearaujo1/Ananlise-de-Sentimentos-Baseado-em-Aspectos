from spacy import displacy

from Dic import Utils

class Sumarizador:

    def sumarizar_resultados(documento_polarizado):
        total_aspectos = []
        for key, value in documento_polarizado.items():
            for aspecto in value['Aspectos']:
                try:
                    print('{}, {}, {}, {}'.format(key, aspecto['nome'], aspecto['polaridade'], aspecto['sentimento']))
                    total_aspectos.append((aspecto['nome']))
                except:
                    pass
