import pol_number
from operation import sum, subtract, divide, multiply


def proverka(operation, n1, n2):
    result = 0
    if operation == '+':
        result = (f'Сложение \n {sum(n1, n2)}')
    elif operation == '-':
        result = (f'Вычитание \n {subtract(n1, n2)}')
    elif operation == '*':
        result = (f'Умножение \n {multiply(n1, n2)}')
    elif operation == '/':
        result = (f'Деление\n {divide(n1, n2)}')
    else:
        result = ('Неизвестная операция, нормально печатай не путай меня') 
    return result