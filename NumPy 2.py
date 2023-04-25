import numpy as np

a = np.random.randint(0,20, (3,3))
print("Сгенерированная матрица:", a)
b = a.sum()
print("Сумма элементов:", b)
c = a.min()
d = a.max()
e = a.size
f = a.var()
print("Минимальный элемент:", c)
print("Максимальный элемент:", d)
print("Кол-во эжлементов:", e)
print("Дисперсия значений элементов массива:", f)