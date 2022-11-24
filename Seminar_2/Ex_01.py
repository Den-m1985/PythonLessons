
'''
lst = []
print(dir(lst))

lst = []
 
 
def add_to_lst(item):
    if isinstance(item, int):  #ограничивает тип
        lst.append(item)
 
 
add_to_lst(66)
add_to_lst('ww')
add_to_lst(65.5)
add_to_lst(2)
add_to_lst(None)
print(lst)
'''
'''
1. Напишите программу, которая принимает на вход число N и выдаёт 
    последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81
'''

n = int(input())

count = 1

#5print (f'{n}')
for i in range(n - 1):
    print(f"{count}", end= ', ')
    count = count * (-3)
print(count)


'''
n = int(input('Введите число: '))
lst = []

for i in range (0, n):
    count = (3 ** i) * ((-1) ** i)
    lst.append(count)
print(lst)
'''

