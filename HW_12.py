# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
my_list_1 = [2, 3, 4, 5, 6]
my_list_2 = [2, 3, 5, 6]

def pairs(this_list):
    for i in range(math.ceil(len(this_list)/2)):
        my_prod = this_list[i]*this_list[len(this_list)-1-i]
        print(my_prod)

print(f'Произведение пар чисел списка {my_list_1} равно: ')
pairs(my_list_1)
print(f'Произведение пар чисел списка {my_list_2} равно: ')
pairs(my_list_2)