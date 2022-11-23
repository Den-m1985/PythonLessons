'''
Напишите программу, которая принимает на вход 
координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

def Input (inputText):
    number = int(input(f'{inputText}'))
    return number


def Calculate(x, y):
    if  x > 0 and y > 0:
        print('координаты соответствуют 1й четверти')
    elif x < 0 and y > 0:
        print('координаты соответствуют 2й четверти')
    elif x < 0 and y < 0:
        print('координаты соответствуют 3й четверти')
    elif x > 0 and y < 0:
        print('координаты соответствуют 4й четверти')
    else:
        print('Что-то пошло не так')

coordinate_X = Input("Введите координату x: ")
coordinate_Y = Input("Введите координату y: ")
Calculate(coordinate_X, coordinate_Y)
