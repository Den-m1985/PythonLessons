


def importdata():
    operation = int(input('Введите желаемый знак:'))
    n1 = complex(input("Введите первое число: "))
    n2 = complex(input("Введите второе число: "))
    return operation, n1, n2


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


# Сложение
def sum(a, b):
    result = a + b
    return result


# Вычитание
def subtract(a, b):
    result = a - b
    return result


# Умножение
def multiply(a, b):
    result = a * b
    return result


# Деление
def divide(a, b):
    result = a / b
    return result
