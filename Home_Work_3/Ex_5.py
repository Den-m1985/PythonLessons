'''
Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def fibonachi_plus(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonachi_plus(n-1) + fibonachi_plus(n-2)


def fibonachi_minus(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return fibonachi_minus(n + 2) - fibonachi_minus(n + 1)


num = 10


lst_plus = []
for e in range(0, num + 1):
    lst_plus.append(fibonachi_plus(e))
#print(lst_plus)

lst_minus = []
for e in range(1, num + 1):
    lst_minus.append(fibonachi_minus(-e))
#print(lst_minus)


lst_minus.reverse()
result = lst_minus + lst_plus
print(result)
