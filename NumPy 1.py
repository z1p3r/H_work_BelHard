import numpy as np

a = np.random.randint(0,101, (3,3))
print("Сгенерированная матрица:", a)
b = np.std(a)
print("Ср.кв. отклонение:", b )
c = np.linalg.det(a)
print("Определитель:", c )
