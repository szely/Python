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