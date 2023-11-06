import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

# PS: Seaborn tem alguns data sets gratuitos
# Valor gasto x Gorjeta data
tips = sns.load_dataset('tips')
print(tips.head())

# muda o tema dos gráficos
sns.set_theme()

# Gerando gráfico com data set
sns.set_theme()
sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='smoker', style='smoker', size='size')

# Data set iris
# PS: os gráficso normalmente tem pontos importantes a serem analisados, no caso deste,
# o objetivo é descobrir qual será a iris a partir dos parâmentros entregues nas outras colunas
iris = sns.load_dataset('iris')

# Gráfico de dispersão
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)
# Usando outro parâmtro como y
sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)

# Data Set titanic
titanic = sns.load_dataset('titanic')

# Gráfico de contagem, conta a quantidade de linhas em relação aos dados da coluna
sns.countplot(x='class',data=titanic)
sns.countplot(x='survived',data=titanic)

# Gráfico de barra
sns.barplot(x='sex',y='survived',hue='class',data=titanic)

# Importando Data Set de preço de casas na California
californiaData = fetch_california_housing()
print(californiaData)
house = pd.DataFrame(californiaData.data, columns=californiaData.feature_names)
# Adicionando coluna preço
house['Price'] = californiaData.target

print(house.head())

# Gráfico de distribuição
sns.distplot(house['Price'])

#Gráfico de Temperatura baseado na correlação de dados
correlacao = house.corr()

# Gráfico
plt.figure(figsize=(10,10))
sns.heatmap(correlacao, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')
