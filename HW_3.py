# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Ввкдите значение координату X: '))
y = int(input('Ввкдите значение координату Y: '))

if x > 0 and y > 0:
    print('Это I четверть')
elif x < 0 and y > 0:
    print('Это II четверть')
elif x < 0 and y < 0:
    print('Это III четверть')
elif x > 0 and y < 0:
    print('Это IV четверть')
else:
    print('Введите значения отличные от 0!!!')