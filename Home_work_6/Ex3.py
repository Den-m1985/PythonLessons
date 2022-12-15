'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.
'''

# Домашка № 4 Перездача по list comprehension (строка 31) 

# и добавил улучшение в строке 26

'''
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
[1,1,1,2,2,3,5,4,4,7,8,8,7] -> [3,5]
'''
from random import randint


def set_of_numbers(n):
    #arr = [0] * n
    #for i in range(n):
    #    arr[i] = int(random() * 10)
    arr = [randint(0, 9) for _ in range(6)]
    return arr


def sort(lst):
    return [a for a in set(lst) if lst.count(a) < 2]


n = 10  # Lenght list
array = set_of_numbers(n)
print(f'Исходный список: {array}')

sort_list = sort(array)
print(f'Список уникальных цисел: {sort_list}')

