'''
Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

def Input (inputText):
    number = int(input(f'{inputText}'))
    return number

def Calculate(number):
    if 0 < number < 6:
        print('Данный день рабочий')
    elif 5 < number < 8:
        print('Данный день выходной')
    else:
        print('Данное число не является днем недели')
        
num = Input("Введите день недели: ")
Calculate(num)