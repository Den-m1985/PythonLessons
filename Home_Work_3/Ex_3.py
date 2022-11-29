'''
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

lst = [1.1, 1.2, 3.1, 5, 10.01]
# print((lst[4]*100)%100)


def calculate(lst):
    lst_result = []
    for item in lst:
        in_Number = item
        in_Numberint = int(in_Number)
        if item != in_Numberint:
            lst_result.append((item*100) % 100)

    max_lst = max(lst_result)
    min_lst = min(lst_result)
    #rusult = round(max_lst, 3) - round(min_lst, 3)
    rusult = max_lst - min_lst
    print(f'max = {max_lst/100}')
    print(f'min = {min_lst/100}')
    print(f'max - min = {rusult/100}')


calculate(lst)
