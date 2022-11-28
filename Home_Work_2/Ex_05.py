from random import randint
'''
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint
'''


def fill_Array(number):
    lst = []
    for item in range(0, number):
        lst.append(item)
    return lst


def sort(array, num):
    lst = []
    temp = 0
    for i in array:
        i = randint(0, num-1)
        lst.append(array[i])
    return lst


num = 10   # длина списка
array = fill_Array(num)
print(array)
print(sort(array, num))


'''
def mix(lst):
    for i in range(len(lst)):
        new_i = randint(0, len(lst) - 1)
        lst[i], lst[new_i] = lst[new_i], lst[i]
 
 
lst_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]
mix(lst_)
print(lst_)
'''