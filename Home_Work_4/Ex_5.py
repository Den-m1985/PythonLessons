'''
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
2*x**3 + 5*x -3
5*x**2 - 2*x +4
=
2*x**3 + 5*x**2 + 3*x +1
pip install sympy
'''
# В пятом задании вы должны были написать свой алгоритм. На семинаре я говорил, что использовать sympy запрещено.
from sympy import simplify


def read_file(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def write_to_file(file_name, result):
    with open(file_name, 'w') as f_obj:
        f_obj.write(str(result))


file1 = read_file('task_4.txt')
file2 = read_file('task_4_2.txt')
result = simplify(file1 + file2)
print(result)
write_to_file('task_5.txt', result)
