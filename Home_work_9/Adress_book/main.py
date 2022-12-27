import os
from telebot import TeleBot, types
import csv
import messages as m
import operations
import import_data
import export_data
os.chdir(os.path.dirname(__file__))

'''
Прикрутить бота к задачам с предыдущего семинара: 
    2.2Создать телефонный справочник с возможностью 
    импорта и экспорта данных в нескольких форматах.
python -m pip install pytelegrambotapi
'''


token = open("token.config", "r").read()  # прочитай README или config.txt
bot = TeleBot(token)
# TOKEN = ''
# bot = TeleBot(TOKEN)


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
    # работает
    if text == '1':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_3)
    # выводит список контактов
    elif text == '2':
        temp = operations.read_contact()
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_5)
        bot.send_message(chat_id=msg.from_user.id, text=temp)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    # экспорт данных в файл пользователя
    elif text == '3':
        bot.register_next_step_handler(msg, answer3)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_6)
    # сохранить в нашу БД от пользователя
    elif text == '4':
        bot.register_next_step_handler(msg, answer4)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_8)
    # поис записи
    elif text == '5':
        bot.register_next_step_handler(msg, answer5)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_9)
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' +
                         msg.text + f', а должны: {m.OPERATIONS + m.MESSAGE_2}')


# добавление нового контакта
def answer1(msg):
    contact = [msg.text.split()]
    operations.write_csv(contact)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_4)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


# выводит список контактов
def answer2(msg):
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


# экспорт данных в файл пользователя
def answer3(msg):
    file_name = msg.text
    export_data.csv_to_json(file_name)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_7)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


# импорт данных в файл от пользователя
def answer4(msg):
    file_name = msg.text
    a = import_data.import_csv(file_name)
    operations.write_csv(a)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_7)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


# поиск контакта
def answer5(msg):
    try:
        search_name = msg.text
        a = str(search_name).title()
        temp = operations.searchcontact(a)
        bot.send_message(chat_id=msg.from_user.id, text=temp)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    except:
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_9)


# Функция для сохранения документа, отправленного боту
@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(
            bot.get_file(msg.document.file_id).file_path))
        
    a = import_data.import_csv('for_adress_book')
    for i in range(len(a)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(a[i])
        
        
            
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_7)

    # Удаляем файл после обработки
    os.remove(filename)


bot.polling()
