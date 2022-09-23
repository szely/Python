# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = bool(input('Ввкдите значение X (True/False): '))
y = bool(input('Ввкдите значение Y (True/False): '))
z = bool(input('Ввкдите значение Z (True/False): '))
n = not (x or y or z) 
m = not x and not y and not z
print(n==m)