import os
from telebot import TeleBot
import messages as m
import datetime
import codecs
os.chdir(os.path.dirname(__file__))

'''
Прикрутить бота к задачам с предыдущего семинара:
    2.1 Создать калькулятор для работы с рациональными и комплексными числами, 
    организовать меню, добавив в неё систему логирования
python -m pip install pytelegrambotapi
'''


token = open("token.config", "r").read()  # прочитай README или config.txt
#token = ''
bot = TeleBot(token)


@bot.message_handler(commands=m.USER_COMMANDS)
def send_welcome(message):
    cmd = message.text.lstrip('/')
    if cmd == 'start':
        bot.reply_to(message, m.OPERATIONS + m.MESSAGE_2 + m.MESSAGE_3)
    else:
        bot.reply_to(message, m.INFO_MESSAGE)


@bot.message_handler()
def send_welcome(message):

    #text = message.text
    text = message.text.split()
    if text[1] == '+':
        bot.reply_to(
            message, text=f'Результат сложения {float(text[0]) + float(text[2])}')
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '-':
        bot.reply_to(
            message, text=f'Результат вычитания {float(text[0]) - float(text[2])}')
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '/':
        if text[2] == '0':
            bot.reply_to(message, text='деление на 0 не допустимо')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)
        else:
            bot.reply_to(
                message, text=f'Результат деления {float(text[0]) / float(text[2])}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '*':
        bot.reply_to(
            message, text=f'Результат умножения {float(text[0]) * float(text[2])}')
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '++':
        bot.reply_to(
            message, text=f'Результат сложения {complex(text[0]) + complex(text[2])}')
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '--':
        bot.reply_to(
            message, text=f'Результат вычитания {complex(text[0]) - complex(text[2])}')
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '—':
        bot.send_message(chat_id=message.from_user.id, text=m.MESSAGE_4)

    elif text[1] == '//':
        if text[2] == '0':
            bot.reply_to(message, text='деление на 0 не допустимо')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)
        else:
            bot.reply_to(message, text=f'Результат деления {complex(text[0]) / complex(text[2])}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

    elif text[1] == '**':
        bot.reply_to(
            message, text=f'Результат умножения {complex(text[0]) * complex(text[2])}')
        bot.send_message(chat_id=message.from_user.id,
                         text=m.MESSAGE_2 + m.MESSAGE_3)

    else:
        bot.reply_to(message, text=m.MESSAGE_1)
    
    log(message, text)
    

def log(message, text):
    dtn = datetime.datetime.now()
    # логирование в 'log_calculator.txt'
    botlogfile = open('log_calculator.txt', 'a', encoding='utf-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' +
          message.from_user.first_name, message.from_user.id,
          'операция: ' + ' '.join(text), file=botlogfile)
    botlogfile.close()
    
    # логирование в 'log'
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(
            f'\n Chat {message.chat.id} User: {message.from_user.first_name} Data: {dtn} Message: {message.text}')


bot.polling(none_stop=True, interval=0)
