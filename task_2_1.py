a = float(input("Отрезок а  = "))
b = float(input("Отрезок b = "))
c = float(input("Отрезок c = "))

if a + b > c and a + c > b and b + c > a:
    print("Это треугольник")
else:
    print("Это не треугольник")