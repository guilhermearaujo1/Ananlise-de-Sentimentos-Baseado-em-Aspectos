import spacy

from src.Dic import UtilsReli
from space.SpaceAnalyzer import SpaceAnalyzer
from classificador_polaridade.AnalisadorPolaridade import AnalisadorPolaridade
from sumarizador.Sumarizador import Sumarizador
from models.Documento import Documento
from spacy import displacy

diretorio_corpus = '../../Corpus Reli'

corpus = UtilsReli.ler_corpus_reli(diretorio_corpus)

# print('\n\n\n')
arquivo_dicionario_liwic = (r"E:\tcc2\src\Dic\LIWC-original.txt")
arquivo_dicionario_sentilex = (r"E:\tcc2\src\Dic\sentilex-reduzido.txt")
arquivo_dicionario_reli_positivo = (r"E:\tcc2\src\Dic\reli_positivos.txt")
arquivo_dicionario_reli_negativo = (r"E:\tcc2\src\Dic\reli_negativos.txt")


spaceAnalyzer = SpaceAnalyzer()
analisadorPolaridade = AnalisadorPolaridade([arquivo_dicionario_liwic, arquivo_dicionario_sentilex, arquivo_dicionario_reli_positivo, arquivo_dicionario_reli_negativo])
#texto = 'O Iphone X é muito bom, ele possui uma excelente tela. Porém péssima bateria.'

#Sistema
total_positivos_sistema = 0
total_negativos_sistema = 0
total_neutro_sistema = 0
total_encontrados_sistema = 0
polaridade_encontrada = 0
total_nao_encontrados_sistema = 0
#Comparando Reli
total_acertos_polaridades = 0
total_erros_polaridades = 0
total_nao_encontrados = 0
total = []
total_polaridade = []

total_polaridade_positivo_reli = 0
total_polaridade_negativo_reli = 0

for frase in corpus.frases[:12470]:


    print('\n  Frase:', frase.texto)

    print('    Aspectos ReLi:', frase.dic_aspectos)
    print('    Polaridade dos Aspectos ReLi:', frase.dic_aspectos_polaridade)

    documento = Documento(frase.texto)

    documento_processado = spaceAnalyzer.processar_documento(documento)

    documento_polarizado = analisadorPolaridade.classificar_polaridade(documento_processado)
    total.append(len(frase.dic_aspectos))
    #print(sum(total))
    total_polaridade.append((len(frase.dic_aspectos_polaridade)))
    #print(sum(total_polaridade))
    Sumarizador.sumarizar_resultados(documento_polarizado)



    #if not len(documento_polarizado.items()):
     #   total_nao_encontrados_sistema += 1
    #else:
     #   encontrado_aspecto = False
      #  for key, value in documento_polarizado.items():

       #     if len(value['Aspectos']):

        #        for aspecto in value['Aspectos']:
         #           polaridade = aspecto.get('polaridade', None)

          #          if polaridade:
           #             encontrado_aspecto = True
            #            polaridade = str(polaridade)
             #           if polaridade == '+':
              #              total_positivos_sistema += 1
               #         elif polaridade == '-':
                #            total_negativos_sistema += 1
                 #       elif polaridade == '*':
                  #          total_neutro_sistema += 1

       # if encontrado_aspecto:
        #    total_encontrados_sistema += 1
        #else:
         #   total_nao_encontrados_sistema += 1
#------------------------------------------------------------------------------------------------------------#

    for key, value in frase.dic_aspectos_polaridade.items():
        if value[0] == '+':
            total_polaridade_positivo_reli += 1
            print('Positivo:', total_polaridade_positivo_reli)
        elif value[0] == '-':
            total_polaridade_negativo_reli += 1
            print('Negativo:', total_polaridade_negativo_reli)




    polaridade_encontrada = 0
    if len(frase.dic_aspectos.items()):
         for key, value in documento_polarizado.items():
             for aspecto in value['Aspectos']:
                 try:
                     find_aspecto = frase.dic_aspectos[str(aspecto['nome'])]
                     find_polaridade = frase.dic_aspectos_polaridade[str(find_aspecto)]

                     if len(find_polaridade) and str(find_polaridade[0]) == str(aspecto.get('polaridade', 'não achou')):
                         total_acertos_polaridades += 1
                         print('acertou:', total_acertos_polaridades)
                     elif str(aspecto.get('polaridade', 'não achou')) == '*':
                         pass
                     else:
                         total_erros_polaridades += 1
                         print('errou', total_erros_polaridades)
                     polaridade_encontrada = 1
                     #break
                 except Exception as error:
                     pass

         if polaridade_encontrada == 0:
            total_erros_polaridades += 1
            print('errou:', total_erros_polaridades)
    else:
        total_nao_encontrados += 1

# print("Mostrar hilario, resultado da compração entre o meu sistema(aspectos e polaridade) as anotações do corpus RELI")
print(total_acertos_polaridades, total_erros_polaridades, total_nao_encontrados)

print('    Aspectos:', frase.dic_aspectos)
# #
# #
print('    Aspectos Polaridade:', frase.dic_aspectos_polaridade)
#
print('\n\nTotal frases:', len(corpus.frases))
print('Quantidade de aspectos TOTAL de ASPECTOS do RELI: ', sum(total))
print('Quantidade de polaridade TOTAL do RELI: ', sum(total_polaridade))

print('Qauntidade de polaridades positivas reli: ', total_polaridade_positivo_reli)
print('Qauntidade de polaridades positivas reli: ', total_polaridade_negativo_reli)

#(1781, 876, 750, 9114)

#print('Total de aspectos classificados como positivo: ', total_positivos_sistema ,'\n', 'Total de aspectos classificados como negativo: ',total_negativos_sistema, '\n', 'Total de aspectos classificados como neutro: ', total_neutro_sistema, '\n',
 #     'Total de aspectos NÃO encontrados: ', total_nao_encontrados_sistema)
#print(total_nao_encontrados_sistema, total_encontrados_sistema, total_nao_encontrados_sistema + total_encontrados_sistema)