# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = str(input('Введите число: '))
number = number.replace('.','')
number = number.replace(',','')
number = number.replace('-','')
sum = 0
for i in range(0,len(number)):
    sum = sum + int(number[i])
print(sum)
