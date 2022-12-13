'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.
'''

#Семинар 5. Пересдача
'''
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, что бы выполнить условие
A[i] - 1 = A[i-1]. Найдите это число.
5,6,7,8,9,10,12,13 => 11
'''
temp = None
with open('seminar5_1.txt') as f_obj:
    for item in map(int, f_obj.read().split( )):
        if temp is None:
            temp = item
        else:
            if item != temp +1:
                print(temp +1)
            temp = item
            
            
