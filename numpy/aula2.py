import numpy as np
# Aula 2

"""
Aprendendo a utilizar alguns métodos:
    - ravel: transforma o array multidimensional em unidimensional / Porém altera a matriz original
    - flatten: transforma o array multidimensional em unidimensional / Porém faz uma cópia do original
    - reshape: modifica o formato do array 
"""
a = np.arange(9).reshape((3,3))
b = a.flatten()
c = a.ravel()

# print('Array original')
# print(a)
# print(b)
# print(c)

# print('Array b modificado')
# b[2] = 25
# print(a)
# print(b)
# print(c)

# print('Array c modificado')
# c[5] = 120 # nesse caso o ponteiro na memório é o mesmo do array 'a' então também será alterado em 'a', por ter sido utilizado o método RAVEL
# print(a)
# print(b)
# print(c)


"""
Transposta de uma matriz
    - matriz qualquer resultante da troca ordenada das linhas pelas colunas de uma matriz chamada de original
    - para isso apenas usar o '.T'
"""

array1 = np.ones(18).reshape(2,9)
print(f'O shape do array \n{array1} é {array1.shape}')

array2 = array1.T #agora ele alterou para a transposta com shape (9,2)
print(f'O shape do array agora alterado: \n{array2} é {array2.shape}')


"""
Mascaras Booleanas

"""

array = np.arange(21).reshape(3,7)
print(f'Array original é {array}')

mask = (array > 7)
print(f'Array com a mascara aplicada {array[mask]}')

array[mask]= 0
print(f'Array com a modificação {array}')

print('\n\n')
x = np.random.randint(0,10,18)
print(f'Array original é \n{x}')

mask = (x > 7)
print(f'Array com a mascara aplicada \n{x[mask]}')

x[mask]= 0
print(f'Array com a modificação \n{x}')





