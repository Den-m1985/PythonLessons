import os
from telebot import TeleBot, types
import messages as m
import datetime
os.chdir(os.path.dirname(__file__))

'''
Прикрутить бота к задачам с предыдущего семинара: 
    2.2Создать телефонный справочник с возможностью 
    импорта и экспорта данных в нескольких форматах.
python -m pip install pytelegrambotapi
'''


token = open("token.config", "r").read() # прочитай README или config.txt
bot = TeleBot(token)
#TOKEN = '' 
#bot = TeleBot(TOKEN)

# команды Start и Info
@bot.message_handler(commands=m.USER_COMMANDS)
def send_welcome(message):
    cmd = message.text.lstrip('/')
    if cmd == 'start':
        bot.reply_to(message, m.OPERATIONS + m.MESSAGE_2)
    else:
        bot.reply_to(message, m.INFO_MESSAGE)

# прнимаем команду от пользователя
@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    if text == '1':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_3)
    elif text == '2':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text=m.OPERATIONS)
    elif text == '3':
        bot.register_next_step_handler(msg, answer3)
        bot.send_message(chat_id=msg.from_user.id, text=m.OPERATIONS)
    elif text == '4':
        bot.register_next_step_handler(msg, answer4)
        bot.send_message(chat_id=msg.from_user.id, text=m.OPERATIONS)
    elif text == '5':
        bot.register_next_step_handler(msg, answer5)
        bot.send_message(chat_id=msg.from_user.id, text=m.OPERATIONS)
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text + f', а должны: {m.OPERATIONS + m.MESSAGE_2}')



def answer1(msg):   # Сделать добавление нового контакта
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Результат сложения {a + b}')


def answer2(msg):   # Сделать вывод записей на экран
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Результат сложения {a + b}')



# Функция для сохранения документа, отправленного боту
@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(
            bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_1)

    # Можете раскомментировать, если потребуется затем удалять файл после обработки,
    # чтобы не тратить память.
    # Не забудьте импортировать os
    #os.remove(filename)




bot.polling()