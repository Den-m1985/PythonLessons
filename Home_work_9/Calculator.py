import os

os.chdir(os.path.dirname(__file__))
'''
Прикрутить бота к задачам с предыдущего семинара:
    2.1 Создать калькулятор для работы с рациональными и комплексными числами, 
    организовать меню, добавив в неё систему логирования
'''
message = '''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:​
 
+  Сложение
-  Вычитание
/  Деление
*  Умножение
'''
print(message)


def importdata():
    operation = input('Введите желаемый знак:')
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


print(proverka(*importdata()))
