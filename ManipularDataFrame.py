import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

californiaData = fetch_california_housing()
print(californiaData)
californiaDF = pd.DataFrame(californiaData.data, columns=californiaData.feature_names)
print()

# Adicionando colunas
print("Adicionando uma coluna para o preço: ")
californiaDF['Price'] = californiaData.target
print(californiaDF.head())
print()

# Removendo uma linha
# para remover uma linha, axis=0, para remover uma coluna axis=1
print("Remove uma linha: ")
print(californiaDF.drop(index=0, axis=0))
print()
print("Remove uma coluna: ")
print(californiaDF.drop(columns='MedInc', axis=1))
print()
# para remover permanentemente crie uma variavel para guardar aquele data freme atualizado, EX:
californiaDF_atualizado = californiaDF.drop(index=0, axis=0)

# Como localizar linhas e colunas específicas usando o index
print("Localiza uma linha: ")
print(californiaDF.iloc[2]) # mostra todas as informações do segundo indice
print()
print("Localiza uma coluna: ")
print(californiaDF.iloc[:, 0]) # mostra a primeira coluna
print()
print(californiaDF.iloc[:, 1]) # mostra a segunda coluna
print()
print(californiaDF.iloc[:, 2]) # mostra a terceira coluna
print()
print(californiaDF.iloc[:, -1]) # mostra a ultima coluna

# Correlação entre variáveis:
# Tipos:
# -Correlação Positiva: Quando uma variavel aumenta, uma segunda variavel aumnta e vice versa,
# por exemplo, caso uma casa tenha mais quartos seu preço aumenta, ou seja se uma variavel aumenta
# a outra também aumenta
# -Correlação Negativa: Quando uma variavel aumenta a outra diminui e vice versa, por exemplo,
# caso a taxa de criminalidade aumente o preço diminui, ou seja se uma aumenta a outra diminui
print(californiaDF.corr())