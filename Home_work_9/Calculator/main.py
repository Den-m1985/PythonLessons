import os
from telebot import TeleBot, types
import messages as m
import operations

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
def answer(msg: types.Message):
    text = msg.text
    bot.register_next_step_handler(msg, operations.proverka(text))
    bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
   

        



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