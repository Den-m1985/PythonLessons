'''
4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
'''


def add_to_lst(input_Text):
    number = int(input(f"{input_Text}"))
    return number


def fill_Array(number):
    lst = []
    for item in range(- number, number + 1):
        lst.append(item)
    return lst


def calculate(number1, number2, array):
    mult = 0
    mult = array[number1] * array[number2]
    #for item in array:
    #    mult = item[number1-1] * item[number2-1]
    return mult


num = add_to_lst("Введите целое число от 1 и больше: ")

user_num1 = add_to_lst(f"Введите целое число от {0} до {num*2}: ")
if -num < user_num1 > num:
    print('Вы ввели вне интервала, повторите попытку')
    user_num1 = add_to_lst(f"Введите целое число от {0} до {num*2}: ")
user_num2 = add_to_lst(f"Введите целое число от {0} до {num*2}: ")
if -num < user_num1 > num:
    print('Вы ввели вне интервала, повторите попытку')
    user_num2 = add_to_lst(f"Введите целое число от {0} до {num*2}: ")


array = fill_Array(num)
print(array)
multiplication = calculate(user_num1, user_num2, array)
print(f"индексы {user_num1} и {user_num2}")
print(f"Произведение цифр {array[user_num1]} и {array[user_num2]} = {multiplication}")