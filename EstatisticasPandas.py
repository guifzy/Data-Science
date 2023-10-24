import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

californiaData = fetch_california_housing()
californiaDF = pd.DataFrame(californiaData.data, columns=californiaData.feature_names)
diabetesDF = pd.read_csv('dataSets/diabetes.csv')
print(diabetesDF.head())
print(diabetesDF.shape)
print()

# Contando os valores de uma coluna
print("Quantos valores tem por coluna:")
print(diabetesDF.value_counts('Outcome')) # Mostra a quantidade de dados de um determinado tipo e o nome da coluna selecionada
print()

# Agrupar os valores com base em suas médias
print("Valores médio de cada linha com base em uma coluna: ")
print(diabetesDF.groupby('Outcome').mean())# groupby agrupa os valores com base em uma coluna e o mean
print()                                     #mostra a média dos valores dos objetos daquela linha
                                            #em relação a coluna

# MÉTRICAS ESTATISTICAS

# Contar a quantidade de valores em cada coluna
print("Quantidade de valores em cada coluna: ")
print(californiaDF.count())
print()

# Média de valores de cada coluna
print("Média dos valores de cada coluna: ")
print(californiaDF.mean())
print()

# Mostra o desvio padrão de cada coluna
print("Desvio padrão de cada coluna: ")
print(californiaDF.std()) # desvio padrão é o quão distante os valores são em relação a média
                          # quanto mais próximo de 0 menor é o desvio padrão e mais uniforme
                          # são os dados
print()

# Mostra o menor valor de cada coluna
print("Menor e maior valor de cada coluna: ")
print(californiaDF.min())
# Mostra o maior valor de cada coluna
print(californiaDF.max())
print()

# Mostra todas as estatísticas anteriores
print("Mostra todas as estatísticas métricas: ")
print(californiaDF.describe())