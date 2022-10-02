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

