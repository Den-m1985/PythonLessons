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


def repeating_elements(lst, n):
    not_repeat = []
    for number in lst:
        if number not in not_repeat:
            not_repeat.append(number)
    #for item in lst:
    #    for j in not_repeat:
    #        if j == item:
    #            not_repeat.append(item)

    return not_repeat


n = 10  # Lenght list
array = consecutive_elements(n)
print(f'Исходный список: {array}')
result = repeating_elements(array, n)
print(result)
