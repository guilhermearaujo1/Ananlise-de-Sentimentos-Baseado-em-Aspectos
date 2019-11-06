from space.SpaceAnalyzer import SpaceAnalyzer
from classificador_polaridade.AnalisadorPolaridade import AnalisadorPolaridade
from sumarizador.Sumarizador import Sumarizador
from models.Documento import Documento
import glob
from src.Dic import Utils

arquivo_dicionario_liwic = (r"E:\tcc2\src\Dic\LIWC-original.txt")
arquivo_dicionario_sentilex = (r"E:\tcc2\src\Dic\sentilex-reduzido.txt")
arquivo_dicionario_reli_positivo = (r"E:\tcc2\src\Dic\reli_positivos.txt")
arquivo_dicionario_reli_negativo = (r"E:\tcc2\src\Dic\reli_negativos.txt")

spaceAnalyzer = SpaceAnalyzer()
analisadorPolaridade = AnalisadorPolaridade([arquivo_dicionario_liwic, arquivo_dicionario_sentilex, arquivo_dicionario_reli_positivo, arquivo_dicionario_reli_negativo])
#texto = 'O Iphone X é muito bom, ele possui uma excelente tela. Porém péssima bateria.'
texto = 'Mostra as dificuldades de o povo humilde e de as crianças carentes( capitães de a areia )e os motivos de as atitudes que tomam e como são encarados e compreendidos por a elite.'

documento = Documento(texto)

documento_processado = spaceAnalyzer.processar_documento(documento)

documento_polarizado = analisadorPolaridade.classificar_polaridade(documento_processado)

Sumarizador.sumarizar_resultados(documento_polarizado)



