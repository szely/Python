# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Ввeдите номер четверти: '))

if n == 1:
    print('x(0;+inf) y(0;+inf)')
elif n == 2:
    print('x(-inf;0) y(0;+inf)')
elif n == 3:
    print('x(-inf;0) y(-inf;0)')
elif n == 4:
    print('x(0;+inf) y(-inf;0)')
else:
    print('Такой четверти нет!!!')