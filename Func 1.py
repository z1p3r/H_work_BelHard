import time

logins = ['d1', 'd2', 'd3', 'd4', 'd5']
passwords = ['f1', 'f2', 'f3', 'f4', 'f5']

a = 1
while a <= 3:
    print('Введите логин.')
    l = input()
    print('Введите пароль.')
    p = input()
    if l not in logins or p not in passwords or logins.index(l) != passwords.index(p):
        if a <= 2:
            print('Неправильно. Попробуйте через 5 секунд.')
            time.sleep(5)
        a += 1
    elif logins.index(l) == passwords.index(p):
        print('Вы вошли.')
        break
    if a > 3:
        print('Вы исчерпали свои попытки.')