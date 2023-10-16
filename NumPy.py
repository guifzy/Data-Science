import numpy as np
from time import process_time


# NUMPY ARRAYS TEMPO DE EXECUÇÃO
python_list = [i for i in range(10000)]

start_time = process_time()

python_list = [i + 5 for i in python_list]

end_time = process_time()

print(float(end_time - start_time))

np_array = np.array([i for i in range(10000)])

start_time = process_time()

np_array += 5

end_time = process_time()

print(float(end_time - start_time))
print()


# NUMPY DECLARAÇÃO DE ARRAYS

list = [1, 2, 3, 4]
print(list)
print(type(list))

numpy_list = np.array([1, 2, 3, 4])
print(numpy_list)
print(type(numpy_list))
# mostra as dimensões do array
print(numpy_list.shape)
print()


# MTRIZES COM NUMPY
print("-TIPOS DE DADOS COM NUMPY:")
nunpay_mtrix = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(nunpay_mtrix)
print(nunpay_mtrix.shape)
print()

# informar o tipo de dados
print("FLOAT:")
nunpay_mtrix = np.array([(1, 2, 3, 4), (5, 6, 7, 8)], dtype=float)
print(nunpay_mtrix)
print()

# matrizes de zeros
print("-MATRIZ DE ZEROS:")
matriz_zero = np.zeros((4, 5))
print(matriz_zero)
print()

# matrizes de uns
print("-MATRIZ DE UNS:")
matriz_um = np.ones((3, 3))
print(matriz_um)
print()

# matriz de numero especifico
print("-MATRIZ COM NUMEROS ESPECÍFICOS:")
matriz = np.full((3, 3), 5)
print(matriz)
print()

# matriz identidade
print("-MATRIZ IDENTIDADE:")
matriz_identidade = np.eye(3)
print(matriz_identidade)
print()

# MATRIZ COM NUMEROS ALEATÓRIOS

print("-MATRIZ ALEATORIA:")
# numeros entre 0 e 1
print("ENTRE 0-1:")
matrizAleatoria = np.random.random((3, 3))
print(matrizAleatoria)
print()
# numeros inteiros aleatorios
print("RANDINT:")
matrizAleatoria = np.random.randint(0, 100, (3, 3))
print(matrizAleatoria)
print()

# ARRAY COM ESPAÇOS LINEARES -> INFORMANDO O TAMANHO E DISTANCIA ENTRE VALORES
print("-ARRAY COM DISTÂNCIA LINEAR:")
print("linspace -> ESPECIFICA O TAMANHO:")
array = np.linspace(10, 30, 5)
print(array)
print()
print("arrange -> ESPECIFICA OS ESPAÇOS LINEARES:")
array = np.arange(10, 30, 5)
print(array)
print()

# CONVERTER ARRAY PARA NUMPY ARRAY
print("-CONVERSÃO PARA NUMPY ARRAY:")
lista = [1, 2, 3, 4]
numpyArray = np.asarray(lista)
print(numpyArray)
print(type(numpy_list))
print()

# ANALISE DE DADOS COM NUMPY
print("-DADOS DO ARRAY/MATRIZ:")
matriz = np.random.randint(10, 90, (5, 5))
print(matriz)
print("Formato:")
print(matriz.shape)
print("Número de dimensões: ")
print(matriz.ndim)
print("Tamanho: ")
print(matriz.size)
print("Tipo de dado: ")
print(matriz.dtype)
print()

#OPERAÇÕES COM ARRAY/MATRIZ

print("-OPERAÇÕES COM NUMPY:")
matriz = np.random.randint(10, 20, (3, 3))
matriz2 = np.random.randint(0, 10, (3, 3))

print(matriz)
print(matriz2)
print("Soma:")
print(np.add(matriz, matriz2))
print("Subtração:")
print(np.subtract(matriz, matriz2))
print("Multiplicação:")
print(np.multiply(matriz, matriz2))
print("Divisão:")
print(np.divide(matriz, matriz2))
print()

print("Matriz transposta: ")
matriz = np.random.randint(0, 10, (2, 3))
print(matriz)
print(matriz.shape)
matriz = np.transpose(matriz)
print(matriz)
print(matriz.shape)
print()

print("Reformatar uma matriz: ")
matriz = np.random.randint(0, 10, (2, 3))
matriz2 = matriz.reshape(3, 2)
print(matriz)
print(matriz.shape)
print(matriz2)
print(matriz2.shape)