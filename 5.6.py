a = int(input())
b = int(input())
try:
    a = 0
    b = b + 1
    x = (b-1)/(a-1)
except ZeroDivisionError as x:
    print(x)
else:
    Ax = (b - a - 1)
print(Ax)