# Numpy é uma biblioteca para com uma grande coleção de funções matemáticas de alto nível e para operar com array, matriz multidimensionais.

import numpy as np

a1d = np.array([1, 2, 3, 5, 8])
print(a1d)
print(a1d.ndim)
print(a1d.shape)
print(a1d.size)
print(a1d.dtype)
print(a1d.data)
print(a1d.itemsize)

print('\n')



a2d = np.ones((3,5))
print(a2d)

print('\n')

b2d = np.zeros((4,9))
print(b2d)

print()

