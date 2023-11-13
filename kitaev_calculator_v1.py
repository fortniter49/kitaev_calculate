print('Здравствуйте, вас приветсвует калькулятор.')
print('Если хотите выйти введите 0, иначе введите 1.')
q1 = input()
while ('1' not in q1 or '0' not in q1) and (len(q1) != 1)\
      or (('1' not in q1 and '0' not in q1) and\
          (len(q1) == 1)) or (len(q1) != 1):
    print('Ошибка. Если вы хотите выйти введите 0, иначе введите 1')
    q1 = input()
q = int(q1)
while q != 0 and q == 1:
    print('Введите число с которыми хотите производить алгоритмы')
    x = float(input('Первое число = '))
    print('Введите цифру обозначающую какое действие вы хотите произвести: ')
    print('1 - сумма')
    print('2 - разность')
    print('3 - умножение')
    print('4 - деление')
    print('5 - целочисленное деление')
    print('6 - взятие остатка')
    print('7 - возведение в степень')
    print('8 - квадратный корень числа')
    print('9 - перевод из любой системы счисления в десятичную')
    print('0 - анализ числа')
    h = int(input())
    if (h != 8) and (h != 9) and (h !=0):
        print('Введите второе число')
        y = float(input('Второе число = '))
    if h == 9:
        print('Введите систему счисления в которой вы ввели первое число')
        y = int(input())
    if h == 1:
        print(x, '+', y, '=', x + y)
    elif h == 2:
        print(x, '-', y, '=', x - y)
    elif h == 3:
        print(x, '*', y, '=', x * y)
    elif h == 4:
        if y != 0:
            print(x, '/', y, '=', x / y)
        else:
            while y == 0:
                print('Нельзя делить на ноль')
                print('Введите второе число')
                y = int(input('второе число = '))
            print(x, '/', y, '=', x / y)
    elif h == 5:
        if y != 0:
            print(x, '//', y, '=', x // y)
        else:
            while y == 0:
                print('Нельзя делить на ноль')
                print('Введите второе число')
                y = int(input('Второе число = '))
            print(x, '//', y, '=', x // y)
    elif h == 6:
        print(x, '%', y, '=', x % y)
    elif h == 7:
        print(x, '**', y, '=', x ** y)
    elif h == 8:
        print(x, '** (1/2) =', x ** (1 / 2))
    elif h == 9:
        g = int(x)
        k = str(g)
        print(int(k, y))
    elif h == 0:
        k1 = int(x)
        k = str(k1)
        print('/Количество разрядов:', len(k))
        a = x / 2
        a1 = int(a)
        if a - a1 == 0:
            print('/Четное число')
        else:
            print('/Нечетное число')
        n = x
        g = 0
        while n > 0:
            n1 = n % 10
            g += n1
            n //= 10
        print('/Сумма цифр числа:', g)
        d = 1
        print('/Все делители числа:')
        while d <= x:
            if x % d == 0:
                print(d)
            d += 1
        b = x ** 0.5
        b1 = int(b)
        if b - b1 == 0:
            print('/Число является полным квадратом', b1)
        else:
            print('/Число не является полным квадратом')
        c = x ** (1 / 3)
        c1 = int(c)
        if c - c1 == 0:
            print('/Число является полным кубом', c1)
        else:
            print('/Число не является полным кубом')
    else:
        print('Ошибка')
    print('Если хотите выйти введите 0 иначе введите 1')
    q = int(input())
print('Конец')
