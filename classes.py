import pandas as pd
import matplotlib.pyplot as plt
from sys import exit

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class Consultas:
    def __init__(self, url):
        self.df = pd.read_csv(url, sep=';', encoding='latin1')


    def mostrar_estabelecimentos(self, estado:str = 'sp', limite_estabelecimentos:int = 10):
        '''
        :param estado: Estado que os hospitais residem
        :param limite_estabelecimentos: quantidade de hospitais que serão mostrados, caso nada seja passado, 10 hospitais serão mostrados
        '''
        estado = estado.upper()
        temp_df = self.df.copy()
        #aqui verifica se o estado está na tabela
        if estado not in self.df['UF'].values:
            exit('Estado não encontrado')

        #Substituindo os itens que faltam por não encontrados.
        temp_df['NU_ENDERECO'] = temp_df['NU_ENDERECO'].replace('S/N', 'Endereço não encontrado')
        temp_df = temp_df.fillna({'NU_ENDERECO': 'Endereço não informado', 'NU_TELEFONE': 'Telefone não informado', 'NO_EMAIL': 'Email não encontrado'})

        #Informações mostradas
        print(temp_df[['NOME_ESTABELECIMENTO', 'NU_TELEFONE', 'NU_ENDERECO', 'NO_BAIRRO', 'NO_EMAIL']][temp_df['UF'] == estado].head(limite_estabelecimentos))


class Analise:
    def __init__(self, url):
        self.df = pd.read_csv(url, sep=';', encoding='latin1')

    def estabelecimentos_por_estado(self):
        novo_df = self.df.copy()
        df_temp = novo_df.groupby(['UF']).nunique()['CNES']
        estados, quant = [*df_temp.index], [*df_temp.values]
        plt.barh(estados, quant)
        plt.xlabel('Quantidade de estabelecimentos')
        plt.ylabel('Estados')
        plt.title('Estabelecimentos de sáude por estado.')
        plt.show()

    def grafico_leitos(self, estado:str = 'SP'):
        '''
        Essa função apresenta um gráfico que nos mostra o crescimento
        :param estado: Coloque o estado que você deseja ver o gráfico
        '''
        estado = estado.upper()
        if estado not in self.df['UF'].values:
            exit('Estado não encontrado')


        leitos_26 = self.df.copy()
        leitos_25 = pd.read_csv('Leitos_2025.csv', sep=';', encoding='latin1')
        leitos_24 = pd.read_csv('Leitos_2024.csv', encoding='latin1')
        leitos_23 = pd.read_csv('Leitos_2023.csv', encoding='latin1')
        leitos_22 = pd.read_csv('Leitos_2022.csv', encoding='latin1')
        leitos_21 = pd.read_csv('Leitos_2021.csv', encoding='latin1')
        leitos_20 = pd.read_csv('Leitos_2020.csv', encoding='latin1')
        leitos_19 = pd.read_csv('Leitos_2019.csv', encoding='latin1')
        leitos_18 = pd.read_csv('Leitos_2018.csv', encoding='latin1')
        leitos_17 = pd.read_csv('Leitos_2017.csv', encoding='latin1')
        leitos_16 = pd.read_csv('Leitos_2016.csv', encoding='latin1')
        leitos_16 = leitos_16.drop_duplicates(subset='CNES')
        leitos_17 = leitos_17.drop_duplicates(subset='CNES')
        leitos_18 = leitos_18.drop_duplicates(subset='CNES')
        leitos_19 = leitos_19.drop_duplicates(subset='CNES')
        leitos_20 = leitos_20.drop_duplicates(subset='CNES')
        leitos_21 = leitos_21.drop_duplicates(subset='CNES')
        leitos_22 = leitos_22.drop_duplicates(subset='CNES')
        leitos_23 = leitos_23.drop_duplicates(subset='CNES')
        leitos_24 = leitos_24.drop_duplicates(subset='CNES')
        leitos_25 = leitos_25.drop_duplicates(subset='CNES')
        leitos_26 = leitos_26.drop_duplicates(subset='CNES')
        agrupado_por_estado26 = leitos_26.groupby(['UF'])['LEITOS_EXISTENTES'].sum()
        agrupado_por_estado25 = leitos_25.groupby(['UF'])['LEITOS_EXISTENTES'].sum()
        agrupado_por_estado24 = leitos_24.groupby(['UF'])['LEITOS_EXISTENTES'].sum()
        agrupado_por_estado23 = leitos_23.groupby(['UF'])['LEITOS_EXISTENTES'].sum()
        agrupado_por_estado22 = leitos_22.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado21 = leitos_21.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado20 = leitos_20.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado19 = leitos_19.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado18 = leitos_18.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado17 = leitos_17.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        agrupado_por_estado16 = leitos_16.groupby(['UF'])['LEITOS EXISTENTE'].sum()
        anos = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026']
        leitos = [
            int(agrupado_por_estado16[estado]),
            int(agrupado_por_estado17[estado]),
            int(agrupado_por_estado18[estado]),
            int(agrupado_por_estado19[estado]),
            int(agrupado_por_estado20[estado]),
            int(agrupado_por_estado21[estado]),
            int(agrupado_por_estado22[estado]),
            int(agrupado_por_estado23[estado]),
            int(agrupado_por_estado24[estado]),
            int(agrupado_por_estado25[estado]),
            int(agrupado_por_estado26[estado]),
        ]
        plt.plot(anos, leitos, marker='o')
        plt.title(f'Crescimento da quantidade de leitos no estado - {estado}')
        plt.xlabel('Ano')
        plt.ylabel('Quantidade de leitos')
        plt.show()
