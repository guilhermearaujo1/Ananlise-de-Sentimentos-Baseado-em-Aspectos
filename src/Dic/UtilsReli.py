import os

from src.models.CorpusReli import CorpusReli
from src.models.FraseReli import FraseReli


def ler_corpus_reli(diretorio_corpus):

    nomes_arquivos = os.listdir(diretorio_corpus)

    corpus = CorpusReli()

    for nome_arquivo in nomes_arquivos:

        caminho_arquivo = diretorio_corpus + '\\' + nome_arquivo

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        conteudo_frase = ''

        dic_aspectos = {}
        dic_aspectos_polaridade = {}

        for linha in linhas:

            linha = linha.replace('\n', '')

            # if '#Corpo_' in linha:
            #     print('\n   ============ Nova Resenha ================ ')

            if not linha:

                # print('\n     ============ Nova Linha ================ \n')

                # print('     ', dic_aspectos_polaridade)

                # dic_aspectos_polaridade = {}

                if conteudo_frase:

                    frase = FraseReli(texto=conteudo_frase, dic_aspectos=dic_aspectos,
                                  dic_aspectos_polaridade=dic_aspectos_polaridade)

                    corpus.add_frase(frase)

                    conteudo_frase = ''
                    dic_aspectos = {}
                    dic_aspectos_polaridade = {}

                continue

            if linha.startswith('#') or linha.startswith('['):
                continue

            fragmentos = linha.split('\t')

            if fragmentos[0] != fragmentos[1] or fragmentos[0] == '"':
                conteudo_frase += ' '

            conteudo_frase += fragmentos[0]

            # print('       =>', linha, '-', len(fragmentos), '-', fragmentos, '-', conteudo_frase)

            if 'OBJ' in fragmentos[2] and fragmentos[0] not in dic_aspectos:
                dic_aspectos[fragmentos[0]] = fragmentos[2]

            if 'op0' in fragmentos[3]:

                polaridade = fragmentos[3][-1]
                aspecto = fragmentos[3].replace('op', '')
                aspecto = aspecto.replace(polaridade, '')

                aspecto = 'OBJ' + aspecto

                lista_polaridades = []

                if aspecto in dic_aspectos_polaridade:
                    lista_polaridades = dic_aspectos_polaridade[aspecto]

                if polaridade not in lista_polaridades:
                    lista_polaridades.extend(polaridade)

                dic_aspectos_polaridade[aspecto] = lista_polaridades

                # print('             ', aspecto, '--', polaridade)

        frase = FraseReli(texto=conteudo_frase, dic_aspectos=dic_aspectos,
                      dic_aspectos_polaridade=dic_aspectos_polaridade)

        corpus.add_frase(frase)

    return corpus

    # print(dic_aspectos)

