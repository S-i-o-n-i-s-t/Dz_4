# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
import random
from re import I
num = int(input('Введите количество чисел в списке - '))
size = list(range(0, num))
if num %2 == 0:
    num1 = int(num / 2)
else:
    num1 = int(num / 2) + 1
size1 = list(range(0, num1))
def creating_a_list_of_numbers(n, s):
    for a in range(0, n):
        s[a] = random.randint(0, 10)
    return s
print(f'Список чисел - {creating_a_list_of_numbers(num, size)}')
a = 0
b = num - 1
while a < b:
    size[a] = size[a] * size[b]
    a = a + 1
    b = b - 1
a = 0
while a < num1:
    size1[a] = size[a]
    a = a + 1 
print(f'Произведение пар чисел списка - {size1}')


