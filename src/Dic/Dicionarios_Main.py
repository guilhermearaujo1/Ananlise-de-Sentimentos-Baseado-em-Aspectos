from src.Dic import Utils

arquivo_dicionario_liwic = (r"E:\tcc2\src\Dic\LIWC-original.txt")
arquivo_dicionario_sentilex = (r"E:\tcc2\src\Dic\sentilex-reduzido.txt")

#arquivo_dicionario_reli_positivo = (r"E:\tcc2\src\Dic\reli_positivos.txt")
#arquivo_dicionario_reli_negativo = (r"E:\tcc2\src\Dic\reli_negativos.txt")

dicionario_liwic = Utils.ler_dicionario(arquivo_dicionario_liwic)
dicionario_sentilex = Utils.ler_dicionario(arquivo_dicionario_sentilex)

#dicionario_reli_positivo = Utils.ler_dicionario(arquivo_dicionario_reli_positivo)
#arquivo_dicionario_reli_negativo = Utils.ler_dicionario(arquivo_dicionario_reli_negativo)

dicionario_completo = {}

dicionario_completo.update(dicionario_liwic)
dicionario_completo.update(dicionario_sentilex)
#dicionario_completo.update(dicionario_reli_positivo)
#dicionario_completo.update(arquivo_dicionario_reli_negativo)

print('\n\n Dicionário Liwic:', len(dicionario_liwic))
print(' Dicionário Sentilex:', len(dicionario_sentilex))
print(' Dicionário Completo:', len(dicionario_completo))

print('Horrível:', dicionario_completo['horrivel'])
print('Triste:', dicionario_completo['triste'])
print('Gostoso:', dicionario_completo['gostoso'])
print('Excelente:', dicionario_completo['excelente'])
print('Regular:', dicionario_completo['regular'])
print('melhorar', dicionario_completo['melhorar'])
print(dicionario_completo)
