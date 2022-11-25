'''
2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
Запрещено использовать функцию factorial из библиотеки math
'''


def add_to_lst(inputText):
    number = int(input(f'{inputText}'))
    return number
     
      
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = add_to_lst("Введите целое число от 2 и больше: ")

list = []
for e in range(1, num + 1):
    list.append(factorial(e))

print(f"Произведения чисел от 1 до {num}:  {list}")
