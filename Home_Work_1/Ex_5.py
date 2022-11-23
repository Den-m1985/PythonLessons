'''
Напишите программу, которая принимает на вход
координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

def Input (inputText):
    number = int(input(f'{inputText}'))
    return number

def Calculate(x1, y1, x2, y2):
    resalt = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    return resalt


coordinate_x1 = Input("Введите координату x1: ")
coordinate_y1 = Input("Введите координату y1: ")
coordinate_x2 = Input("Введите координату x2: ")
coordinate_y2 = Input("Введите координату y2: ")

resalt = Calculate(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)

print('Расстояние между точками: ')
print(round(resalt, 3))



