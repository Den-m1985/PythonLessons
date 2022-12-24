import os
from telebot import TeleBot
import messages as m
import datetime
os.chdir(os.path.dirname(__file__))
'''
Прикрутить бота к задачам с предыдущего семинара:
    2.1 Создать калькулятор для работы с рациональными и комплексными числами, 
    организовать меню, добавив в неё систему логирования
'''


token = open("token.config", "r").read() # прочитай README или config.txt
bot = TeleBot(token)
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
def send_welcome(message):
    
    text = message.text
    if text == '+':
        bot.register_next_step_handler(message, sum)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '-':
        bot.register_next_step_handler(message, subtraction)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '//' or text == '/':
        bot.register_next_step_handler(message, devision)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '*':
        bot.register_next_step_handler(message, mult)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '+++':
        bot.register_next_step_handler(message, sum_complex_numbers)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '---':
        bot.register_next_step_handler(message, subtraction_complex_numbers)
        bot.reply_to(message, m.MESSAGE_1)
    else:
        bot.reply_to(message, text='Вы прислали: ' + text +
                        ', а должны были арифметическое действие')
    
    dtn = datetime.datetime.now()
    botlogfile = open('log_calculator.txt', 'a', encoding='utf-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + 
            message.from_user.first_name, message.from_user.id, 
            'операция: ' + text, file=botlogfile)
    botlogfile.close()


def sum(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2) 


def sum_complex_numbers(msg):
    a, b = map(complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)  



def subtraction(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    

def subtraction_complex_numbers(msg):
    a, b = map(complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)  

    
def devision(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    
    
def mult(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


bot.polling()
