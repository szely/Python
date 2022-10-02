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