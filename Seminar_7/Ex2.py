'''
Создать калькулятор для работы с рациональными и комплексными числами,
 организовать меню, 
   добавив в неё систему логирования.

В рамках этого обсуждения студентам надо нарисовать “архитектуру” 
(например, в виде блок-схемы) для работы данного приложения.
b = complex('12+6j') * complex('5+3j')

print(b)  # (42+66j)

b = complex('12+6j') + 66

print(b)  # (78+6j)


'''




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


   # Подготовим сообщение для пользователя о доступных математических операциях.
# В тройных кавычках можно хранить многострочный текст.
message = '''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:​
 
+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
 
Ваш выбор:
''​'
print(message)
# Запрашиваем у пользователя желаемое действие
operation = input(message)​
 
# Выводим сообщение о выбранной операции или что она отсутствует
if operation == '+':
   print('Сложение')
elif operation == '-':
   print('Вычитание')
elif operation == '/':
   print('Деление')
elif operation == '*':
   print('Умножение')
else:
   print('Неизвестная операция') 
'''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter: 
 
+ : Сложение
- : Вычитание
/ : Деление
* : Умножение 
 
Ваш выбор:
+
 
Сложение
'''

def ask_operation():
    message = '''
    Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:
 
    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение
 
    Ваш выбор:
    '''
 
    # Запрашиваем у пользователя желаемое действие
    operation = input(message) 
 
    return operation



    operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}

op = '+'
n1, n2 = 25, 6

print(operations[op](n1, n2))
