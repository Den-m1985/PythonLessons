'''
2. Для натурального n создать список, 
   состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 4: [1, 4, 7, 10, 13] 
'''

N = int(input('N = '))
lst1 = []
for i in range(N + 1):
    lst1.append(3 * i + 1)
print(lst1)

