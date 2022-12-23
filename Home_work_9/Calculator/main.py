import os
#from telebot import TeleBot, types
import telebot
import messages as m

os.chdir(os.path.dirname(__file__))
'''
Прикрутить бота к задачам с предыдущего семинара:
    2.1 Создать калькулятор для работы с рациональными и комплексными числами, 
    организовать меню, добавив в неё систему логирования
'''

token = open("token.config", "r").read()
bot = telebot.TeleBot(token)
#TOKEN = '' 
#bot = TeleBot(TOKEN)


@bot.message_handler(commands=m.USER_COMMANDS)
def send_welcome(message):
    cmd = message.text.lstrip('/')
    if cmd == 'start':
        bot.reply_to(message, m.OPERATIONS)
    else:
        bot.reply_to(message, m.INFO_MESSAGE)
        

@bot.message_handler()
def answer(msg: types.Message):

    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите уменьшаемое и вычитаемое')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')

        







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


#print(proverka(*importdata()))


bot.polling()

#print(complex(3, 2))  (3+2j)
'''
a = 10
b = 20
a = complex(a)
b = complex(b)
suma = a + b
mult = a * b
print(suma)  (30+0j)
print(mult)  (200+0j)
'''