'''
3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
*Пример:*
- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)
'''


def add_to_lst(input_Text):
    number = int(input(f"{input_Text}"))
    return number


def calculate(number):
    lst = []
    for item in range(1, number + 1):
        lst.append((1+ 1 / item)**item)
    return lst


num = add_to_lst("Введите целое число от 1 и больше: ")
sequence_Numbers = calculate(num)
print(f"Для n = {num}: {sequence_Numbers}")
print(f"Сумма цифр = {sum(sequence_Numbers)}")