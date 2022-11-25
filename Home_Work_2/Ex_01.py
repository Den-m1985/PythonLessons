'''
1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
*Пример:*
- 6782 -> 23
- 0.56 -> 11
'''


def add_to_lst(inputText):
    entered_list = float(input(f"{inputText}"))
    return entered_list


def Calculate(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

        
num = add_to_lst("Введите число в одну строку без пробелов: ")
sumNums = Calculate(num)
print(f"Сумма цифр = {sumNums}")