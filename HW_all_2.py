# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = str(input('Введите число: '))
number = number.replace('.','')
number = number.replace(',','')
number = number.replace('-','')
my_sum = 0
for i in range(0,len(number)):
    my_sum += int(number[i])
print(f'Сумма цифр в числе равна: {my_sum}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
prod = 1
my_list = []
for i in range(1, number+1):
    prod *= i
    my_list.append(prod)
print(f'Набор произведений от 1 до {number} - {my_list}')

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Ведите число: '))
my_list = []
for i in range(1, number+1):
    part = [i,round((1+1/i)**i)]
    my_list.append(part)
my_dict = dict(my_list)
my_sum = sum(my_dict.values())
print(f'Сумма последовательсности из {number} элементов {my_dict} равна: {my_sum}')

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Ведите число: '))
my_list = []
part = 0
for i in range(-number, number+1):
    my_list.append(i)
file = open('text.txt','r')
prod = 1
for line in file:
    prod *= my_list[int(line)]
print(f'Произведение элементов в списке {my_list} на указанных в файле text.txt позициях равно  {prod}')
file.close()


# Реализуйте алгоритм перемешивания списка.

my_list_1 = [1,2,3,3,9,434,234,123]
my_list_2 = [3,4,5,8,6,2,3,3,3,123]
new_list = my_list_1+my_list_2
new_list = list(set(new_list))
print(new_list)