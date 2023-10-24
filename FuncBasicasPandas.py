import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

californiaData = fetch_california_housing()

# Criando um data frame com o pandas a partir de um data set
californiaDF = pd.DataFrame(californiaData.data, columns=californiaData.feature_names)
print(californiaDF.head())
print(californiaDF.shape)
print()

# Criando um DataFrame pandas a partir de um arquivo CSV(Excel)
diabetesDF = pd.read_csv('dataSets/diabetes.csv')
print(type(diabetesDF))
print(diabetesDF.head())
print(diabetesDF.shape)
print()

# Coverter um DataFrame pandas em CSV
californiaDF.to_csv('california.csv')
californiaDF.to_excel('california.xlsx')

# Criando DataFrame com valores aleatórios
randomDF = pd.DataFrame(np.random.rand(20, 10))
print(randomDF.head())
print(randomDF.shape)
print()

# Inspeção do DataFrame
print(californiaDF.head()) # 5 primeiros elementos
print(californiaDF.tail()) # 5 ultimos elementos
print(californiaDF.info()) # informações como numero de valores perdidos e tamanho
print(californiaDF.isnull().sum()) # encontra a quantidade de valores perdidos em cada coluna
print()



