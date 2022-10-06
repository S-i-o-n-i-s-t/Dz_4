# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
from random import uniform
# from unittest import result
def list_run_num(count: int):
    size = []
    if count <= 0:
        print('Заданное число не может быть отрицательным или = 0')
        return [0.0]
    for i in range(count):
        size.append(round(uniform(1, count), 2))
    return size
def min_max(size: list):
    num_max = num_min = size[0] % 1
    for k in range(1, len(size)):
        num = round(size[k] % 1, 2)
    if num > num_max:
        num_max = num
    elif num < num_min:
        num_min = num
    
    result = round(num_max - num_min, 2)
    print(f'min = {num_min}, max = {num_max}, Difference = {result}')
    return result
all_list = list_run_num(int(input('ВВедите число - ')))
print(all_list)
print(min_max(all_list))       