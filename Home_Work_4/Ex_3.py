'''
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
[1,1,1,2,2,3,5,4,4,7,8,8,7] -> [3,5]
'''
from random import randint


def consecutive_elements(n):
    lst = []
    for item in range(1, n+1):
        lst.append(randint(-10, 10))
    return lst


def repeating_elements(lst):
    not_repeat = []
    i = 1
    while i < len(lst):
        if lst[i] < lst[i-1]:
            not_repeat.append(lst[i])
        i += 1
    return not_repeat


n = 10  # Lenght list
array = consecutive_elements(n)
print(f'Исходный список: {array}')
result = repeating_elements(array)
print(result)
