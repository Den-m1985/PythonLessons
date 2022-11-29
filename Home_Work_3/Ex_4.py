'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

number = 45

    
def binar_calculate(number):
    print(bin(number)[2:])
    binar_number = ''
    while number > 0:
        binar_number = str(number % 2) + binar_number
        number = number // 2
    if binar_number == (bin(number)[2:]):
        print(binar_number)


binar_calculate(number)
