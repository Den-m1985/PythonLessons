import os
from telebot import TeleBot, types
import csv
import messages as m
import operations
import import_data
import Loging
os.chdir(os.path.dirname(__file__))

'''
Прикрутить бота к задачам с предыдущего семинара: 
    2.2Создать телефонный справочник с возможностью 
    импорта и экспорта данных в нескольких форматах.
python -m pip install pytelegrambotapi
'''

token = open("token.config", "r").read()  # прочитай README или config.txt
# TOKEN = ''
bot = TeleBot(token)


# команды Start и Info
@bot.message_handler(commands=m.USER_COMMANDS)
def send_welcome(message):
    cmd = message.text.lstrip('/')
    if cmd == 'start':
        bot.reply_to(message, m.OPERATIONS + m.MESSAGE_2)
    else:
        bot.reply_to(message, m.INFO_MESSAGE)
    Loging.log(message)


# прнимаем команду от пользователя
@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    if text == '1':
        bot.register_next_step_handler(msg, new_contact)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_3)
        Loging.log(msg, m.MESSAGE_4)

    # выводит список контактов
    elif text == '2':
        print_contacts = operations.read_contact()
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_5)
        bot.send_message(chat_id=msg.from_user.id, text=print_contacts)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
        Loging.log(msg, m.MESSAGE_5)

    # экспорт файла пользователю
    elif text == '3':
        bot.send_document(chat_id=msg.from_user.id, document=open('phonebook.csv', 'rb'))
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_12)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
        Loging.log(msg, m.MESSAGE_11)

    # поис записи
    elif text == '4':
        bot.register_next_step_handler(msg, search_contact)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_9)
        Loging.log(msg, m.MESSAGE_10)

    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + 
                                msg.text + f', а должны: {m.OPERATIONS}')
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
        Loging.log(msg, 'eror')


# добавление нового контакта
def new_contact(msg):
    contact = [msg.text.split()]
    operations.write_csv(contact)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_4)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


# поиск контакта
def search_contact(msg):
    try:
        search_name = msg.text
        a = str(search_name).title()
        temp = operations.searchcontact(a)
        bot.send_message(chat_id=msg.from_user.id, text=temp)
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    except:
        bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_9)


# Сохранения документа, отправленного боту
@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    # скачиваем файл
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(
            bot.get_file(msg.document.file_id).file_path))
    # добавляем в нашу БД из скаченного файла
    name = os.path.splitext(filename)  # отделяем имя от расширения
    temp = import_data.import_csv(name[0])
    for i in range(len(temp)):
        with open('phonebook.csv', "a", newline='', encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(temp[i])
                
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_7)
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    os.remove(filename) # Удаляем файл после обработки

    Loging.log(msg, m.MESSAGE_7)


bot.polling()
