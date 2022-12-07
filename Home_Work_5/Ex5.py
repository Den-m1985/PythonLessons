'''
5* Дан список чисел. 
Найдите все возрастающие последовательности.
Порядок элементов менять нельзя.
*Пример:* 

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
'''
lst = [1, 5, 2, 3, 4, 6, 1, 7]


def consecutive_numbers(lst):
    
    for i in range(len(lst)):
        arr_n = [1]
        arr_n[0] = lst[0]
        for j in range(i, len(lst)):
            if lst[j] > arr_n[-1]:
                arr_n.append(lst[j])
        print(arr_n)
        

consecutive_numbers(lst)