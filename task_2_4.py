a = float(input("Рост в метрах: "))
b = float(input("Вес в кг: "))
c = b/(a ** 2)
print(c)
if c > 0 and c <= 18.5:
    print("Недостаток массы")
elif c > 18.5 and c<= 24.9:
    print('Нормальный вес')
elif c >= 25.0 and c <= 29.9:
    print('Избыточная масса')
elif c >= 30.0:
    print('Ожирение')