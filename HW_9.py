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