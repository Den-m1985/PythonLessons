'''
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=2 => 2*x**2 + 4*x + 5 = 0 или x**2 + 5 = 0 или 10*x**2 = 0
'''

from random import randint


def generate_fotmula(n):
    formula = ""
    for i in range(n+1):
        number = randint(1, 11)  # число перед членом
        if i < n-1:
            formula = formula + f"{number}*x**{n-i} + "
        elif i == (n-1):
            formula = formula + f"{number}*x + "
        else:
            formula = formula + f"{number}"
    return formula


def write_to_file(file_name, result):
    with open(file_name, 'w') as f_obj:
        f_obj.write(result)


k = 5
#k1 = randint(0, 101)
#k2 = randint(0, 101)
write_to_file('task_4.txt', generate_fotmula(k))
write_to_file('task_4_2.txt', generate_fotmula(k))
