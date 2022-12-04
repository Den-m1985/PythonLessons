'''
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
24 -> 2 2 2 3
'''


def Input (inputText):
    number = int(input(f'{inputText}'))
    return number


def calculate(n):
    i = 2
    numbers = []
    while i * i <= n:
       while n % i == 0:
           numbers.append(i)
           n = n // i
       i = i + 1
    if n > 1:
       numbers.append(n)
    print(numbers)


n = Input("Введите целое число: ")
calculate(n)

