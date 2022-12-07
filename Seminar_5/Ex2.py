'''
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, что бы выполнить условие
A[i] - 1 = A[i-1]. Найдите это число.
5,6,7,8,9,10,12,13 => 11

2. Напишите программу, удаляющую из текста все слова, содержащие "абв"

3. Дан список чисел. Создайте список, в который порадают числа, описываемые
возрастающую последовательность. порядок элементов менять нельзя.
[1,5,2,3,4,6,1,7] => [1,2,3] или [1,7] или [1,6,7]
если все последовательности найти то рекурсия
'''

# first task
temp = None
with open('seminar5_1.txt') as f_obj:
    for item in map(int, f_obj.read().split( )):
        if temp is None:
            temp = item
        else:
            if item != temp +1:
                print(temp +1)
            temp = item
            
            
with open('seminar5_1.txt', 'r') as f_obj:
    lst = list(map(int, f_obj.read().split( )))
    temp1 = 0     
    for key, item in enumerate(lst):
        if key + 1 < len(lst) and item + 1 != lst[key +1]:
            temp1 = item +1
    print(temp1)  

# second task
text = 'ловатмивами абв пипви апыи'
result = " ".join(list(filter(lambda x: not 'абв' in x, text.split( ))))
print(result)

result2 = list(filter(lambda x: 'абв' not in x.lower(), text.split( )))
print(result2)


# third task

a = [1,5,2,3,4,6,1,7]
'''
res = []
i = 0
k = 0
for j, item in enumerate(a):
    res.append([item])
    print(res)
    for i in range(j, len(a)):
        if a[i] > res[j][k]:
            res[j].append(a[i])
    k = 0
#print(res)
'''

for i in range(len(a)):
    arr_n = [1]
    arr_n[0] = a[0]
    for j in range(i, len(a)):
        if a[j] > arr_n[-1]:
            arr_n.append(a[j])
    print(arr_n)


def get_up(lst):
    ups = [lst[0]]
    for i in lst:
        if i > max(ups):
            ups.append(i)
    return ups
#print(get_up(a))
