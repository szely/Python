# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
my_sum = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        my_sum += my_list[i]
print(f'Сумма элементов на четных позициях в списке {my_list} равна {my_sum}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
my_list_1 = [2, 3, 4, 5, 6]
my_list_2 = [2, 3, 5, 6]

def Pairs(this_list):
    for i in range(math.ceil(len(this_list)/2)):
        my_prod = this_list[i]*this_list[len(this_list)-1-i]
        print(my_prod)

print(f'Произведение пар чисел списка {my_list_1} равно: ')
Pairs(my_list_1)
print(f'Произведение пар чисел списка {my_list_2} равно: ')
Pairs(my_list_2)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01] 

new_list = []
for i in range(len(my_list)):
    if round(my_list[i]%1,2) != 0:
        new_list.append(round(my_list[i]%1,2))

my_min = new_list[0]
for i in range(len(new_list)):
    if new_list[i]<my_min:
        my_min = new_list[i]

my_max = new_list[0]
for i in range(len(new_list)):
    if new_list[i]>my_max:
        my_max = new_list[i]

print(f'Разница между максимальным и минимальным значением дробной части элементов списка {my_list} равна {my_max-my_min}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

my_munber_dec = int(input('Введите число: '))

my_str = ''
while my_munber_dec  > 0:
    my_str += str(my_munber_dec % 2)
    my_munber_dec //= 2

my_munber_bin = ''
for i in range(len(my_str)):
    my_munber_bin += my_str[-i-1]

print(f'Введеное число в двоичной системе равно {my_munber_bin}')


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

n = -int(input('Введите число: '))

def fib(n):
    if n in [-1]:
        return 1
    elif n in [-2]:
        return -1
    elif n < 0:
        return fib(n+2) - fib(n+1)
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

my_list = []
for i in range(n, -n+1):
    my_list.append(fib(i))
print(my_list)

