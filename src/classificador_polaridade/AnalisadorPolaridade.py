from Dic import Utils

class AnalisadorPolaridade():

    def __init__(self, dicionarios=[]):

        self.dicionario_polaridade = {}

        for dicionario in dicionarios:
            dicionario = Utils.ler_dicionario(dicionario)
            self.dicionario_polaridade.update(dicionario)



    def classificar_polaridade(self, documento_processado):
        mapping_polaridade = {
            '1': '+',
            '-1': '-',
            '0': '*'
        }

        for key, value in documento_processado.items():

            for aspecto in value['Aspectos']:
                polaridade = Utils.removerAcentosECaracteresEspeciais(aspecto['sentimento'])
                try:
                    aspecto['polaridade'] = mapping_polaridade[str(self.dicionario_polaridade[polaridade])]
                except:
                    pass
        return documento_processado