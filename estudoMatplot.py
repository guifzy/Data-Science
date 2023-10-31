import numpy as np
import matplotlib.pyplot as plt

#Gráfico de linha
x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x, y, color='g')
ax.scatter(x, z, color='b')
plt.show()

#Gráfico exponencial
valor_x = np.linspace(0, 10, 5)
valor_y = 2**valor_x

plt.plot(valor_x, valor_y)
plt.title('Gráfico da Bárbara')
plt.xlabel('Beleza exponencial')
plt.ylabel('Bárbara')
plt.show()

#gráfico seno
x = np.linspace(0, 100, 100)
y = np.cos(x)
z = np.sin(x)

plt.plot(x, z)
plt.title('Sen Wave')
plt.xlabel('Ângulo')
plt.ylabel('Valor do seno')
plt.show()

#gráfico cos
plt.plot(x,y)
plt.title('Cos Wave')
plt.xlabel('Ângulo')
plt.ylabel('Valor do cosseno')
plt.show()

# Gráfico parábola

x = np.linspace(-10, 10, 20)
y = x**2

plt.plot(x, y)
plt.title('Parábola')
plt.show()
# Como exibir simbolos e cores diferentes
plt.plot(x, y, 'r+') # caso queira uma cor em específico usar 'color='
plt.show()

# Gráfico com várias linhas

x = np.linspace(-5, 5, 50)
plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
plt.title('Seno e Cosseno')
plt.show()

# Gráfico com barra
languages = ['English','French','Spanish','Latin','German']
people = [100, 50, 150, 40, 70]
plt.bar(languages, people)
plt.xlabel('LANGUAGES')
plt.ylabel('NUMBER OF PEOPLE')
plt.show()

#Gráfico de pizza

ax = plt.figure().add_axes((0, 0, 1, 1)) # Define os eixos do tamanho da figura, neste caso a pizza cobre a figura inteira
languages = ['English', 'French', 'Spanish', 'Latin', 'German']
people = [100, 50, 150, 40, 70]
ax.pie(people, labels=languages, autopct='%1.1f%%') #a utopct é a formatação dos dados, no caso só mostra uma casa após a virgula
plt.show()

# Gráfico de dsipersão

x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x, y, color='g')
ax.scatter(x, z, color='b')
plt.show()

# Gráfico de dsipersão 3D

fig3 = plt.figure()
ax = plt.axes(projection='3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()