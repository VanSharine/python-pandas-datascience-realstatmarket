#Carregue o conjunto de dados chamado kc_house_data.csv do HD para a


#função - read_csv()
#biblioteca Pandas

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#mostre as 5 primeiras linhas do conjunto de dados

#print(data.head())

# mostre o numero de colunas e o jmero de linhas do conjunto

#print(data.shape)

#mostre na tela o nome das colunas do conjunto de dados
#print(data.columns)

#mostre o conjunto de dados ordenados pela coluna price
#print(data[['id', 'price']].sort_values('price'))

#mostre na tela o conjunto de dados ordenados pela coluna proce do maior para o menor
print(data[['id', 'price']].sort_values('price', ascending= False))