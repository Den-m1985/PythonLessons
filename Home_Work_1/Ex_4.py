'''
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

def Input (inputText):
    number = int(input(f'{inputText}'))
    return number

def Calculate(number):
    if  number == 1:
        print('координаты 1й четверти: x > 0; y > 0')
    elif number == 2:
        print('координаты 2й четверти: x < 0; y > 0')
    elif number == 3:
        print('координаты 3й четверти: x < 0; y < 0')
    elif number == 4:
        print('координаты 4й четверти: x > 0; y < 0')
    else:
        print('Что-то пошло не так')


coordinate = Input("Введите номер четверти: ")
Calculate(coordinate)

