import os
from telebot import TeleBot
import messages as m
import Loging
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
    Loging.log(message)


@bot.message_handler()
def send_welcome(message):
    text = message.text.split()
    if len(text) == 3:
        if text[1] == '+':
            answer = float(text[0]) + float(text[2])
            bot.reply_to(message, text=f'Результат сложения {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '-':
            answer = float(text[0]) - float(text[2])
            bot.reply_to(message, text=f'Результат вычитания {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '/':
            if text[2] == '0':
                answer = 'eror'
                bot.reply_to(message, text='деление на 0 не допустимо')
                bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)
            else:
                answer = float(text[0]) / float(text[2])
                bot.reply_to(message, text=f'Результат деления {answer}')
                bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '*':
            answer = float(text[0]) * float(text[2])
            bot.reply_to(message, text=f'Результат умножения {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '++':
            answer = complex(text[0]) + complex(text[2])
            bot.reply_to(message, text=f'Результат сложения {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '--':
            answer = complex(text[0]) + complex(text[2])
            bot.reply_to(message, text=f'Результат вычитания {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '—':
            answer = 'eror'
            bot.send_message(chat_id=message.from_user.id, text=m.MESSAGE_4)

        elif text[1] == '//':
            if text[2] == '0':
                answer = 'eror'
                bot.reply_to(message, text='деление на 0 не допустимо')
                bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)
            else:
                answer = complex(text[0]) / complex(text[2])
                bot.reply_to(message, text=f'Результат деления {answer}')
                bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        elif text[1] == '**':
            answer = complex(text[0]) * complex(text[2])
            bot.reply_to(message, text=f'Результат умножения {answer}')
            bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_2 + m.MESSAGE_3)

        else:
            answer = 'eror'
            bot.reply_to(message, text=m.MESSAGE_1)
    else:  
        answer = 'eror'
        bot.send_message(chat_id=message.from_user.id,text=m.MESSAGE_1 + m.MESSAGE_3)
    
    Loging.log(message, answer)
    

bot.polling(none_stop=True, interval=0)