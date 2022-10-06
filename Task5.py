# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibo(num: int):
    a, b = 1, 1
    size = [0]
    for i in range(num):
        size.append(a)
        size.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return size
print(fibo(int(input('Введите число '))))