# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
import random

num = int(input('Введите число - '))
size = list(range(0, num))
def creating_a_list_of_numbers(n, s):
    if n < 0:
        print('Число не может быть отрицательным')
        return []
    for a in range(0, n):
        s[a] = random.randint(0, 10)
    return s
def Summ_index_(n, s):
    a = 1
    c = 0
    while a < n:
        c = c + s[a]
        a = a + 2
    return c
print(creating_a_list_of_numbers(num, size))
print(Summ_index_(num, size))


