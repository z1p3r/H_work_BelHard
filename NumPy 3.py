import numpy as np

a = np.random.randint(0,101, (3,3))
b = np.random.randint(0,20, (3,3))
c = np.dot(a,b)
print("Произведение матрицы")
print(a)
print("на матрицу")
print(b)
print("Результат: ")
print(c)